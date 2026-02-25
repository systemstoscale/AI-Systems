#!/usr/bin/env python3
"""
Email Capture - Template for AI Employee module.

Reads Gmail inbox, categorizes emails by urgency, and generates a digest.
Feeds into the Daily Brief for the "Action Required" section.

Categories:
  - Action Required: needs a response or decision
  - FYI: notifications, automated messages
  - Marketing: promotional content

Setup:
    1. Enable Gmail API in Google Cloud Console
    2. Download credentials.json to this directory
    3. Run this script once to complete OAuth flow

Usage:
    python scripts/email-capture.py                 # Default (20 emails)
    python scripts/email-capture.py --unread        # Unread only
    python scripts/email-capture.py --count 50      # More emails
"""

import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def get_gmail_service():
    """Get authenticated Gmail service. Same OAuth pattern as meeting-intel.py."""
    try:
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build

        creds = None
        token_path = "token.json"
        creds_path = os.getenv("GOOGLE_CREDENTIALS_PATH", "credentials.json")

        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                from google.auth.transport.requests import Request
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
                creds = flow.run_local_server(port=0)
            with open(token_path, "w") as f:
                f.write(creds.to_json())

        return build("gmail", "v1", credentials=creds)
    except ImportError:
        print("Install: pip install google-api-python-client google-auth-oauthlib")
        return None
    except Exception as e:
        print(f"Gmail auth error: {e}")
        return None


def categorize_email(email):
    """Categorize an email based on labels and sender."""
    labels = set(email.get("labelIds", []))
    from_addr = email.get("from", "").lower()

    if "CATEGORY_PROMOTIONS" in labels or "CATEGORY_UPDATES" in labels:
        return "marketing"

    fyi_patterns = ["noreply", "no-reply", "notifications", "alerts",
                    "github.com", "vercel.com", "stripe.com", "slack.com"]
    if any(p in from_addr for p in fyi_patterns):
        return "fyi"

    if "CATEGORY_SOCIAL" in labels or "CATEGORY_FORUMS" in labels:
        return "fyi"

    return "action_required"


def get_inbox_digest(max_results=20, unread_only=False):
    """Generate categorized inbox digest."""
    service = get_gmail_service()
    if not service:
        return {"available": False, "error": "Gmail not configured"}

    query = "is:inbox is:unread" if unread_only else "is:inbox"

    try:
        results = service.users().messages().list(
            userId="me", q=query, maxResults=max_results
        ).execute()

        messages = results.get("messages", [])

        categorized = {"action_required": [], "fyi": [], "marketing": []}

        for msg_ref in messages:
            msg = service.users().messages().get(
                userId="me", id=msg_ref["id"], format="metadata",
                metadataHeaders=["Subject", "From", "Date"]
            ).execute()

            headers = {h["name"]: h["value"] for h in msg.get("payload", {}).get("headers", [])}

            email = {
                "id": msg["id"],
                "subject": headers.get("Subject", "(No subject)"),
                "from": headers.get("From", ""),
                "date": headers.get("Date", ""),
                "snippet": msg.get("snippet", ""),
                "labelIds": msg.get("labelIds", []),
            }

            category = categorize_email(email)
            categorized[category].append(email)

        return {
            "available": True,
            "total_processed": len(messages),
            "action_required_count": len(categorized["action_required"]),
            "categorized": categorized,
        }
    except Exception as e:
        return {"available": False, "error": str(e)}


def format_digest(digest):
    """Format the digest into readable output."""
    if not digest.get("available"):
        return f"# Inbox Digest\n\nError: {digest.get('error', 'Unknown')}"

    lines = [
        f"# Inbox Digest",
        f"Processed: {digest['total_processed']} | Action Required: {digest['action_required_count']}",
        "",
    ]

    categorized = digest.get("categorized", {})

    action = categorized.get("action_required", [])
    if action:
        lines.append(f"## Action Required ({len(action)})")
        for email in action:
            from_name = email["from"].split("<")[0].strip().strip('"')
            lines.append(f"- **{email['subject']}** - {from_name}")
            if email.get("snippet"):
                lines.append(f"  _{email['snippet'][:100]}_")
        lines.append("")

    fyi = categorized.get("fyi", [])
    if fyi:
        lines.append(f"## FYI ({len(fyi)})")
        for email in fyi[:5]:
            from_name = email["from"].split("<")[0].strip().strip('"')
            lines.append(f"- {email['subject']} - {from_name}")
        if len(fyi) > 5:
            lines.append(f"  _...and {len(fyi) - 5} more_")
        lines.append("")

    marketing = categorized.get("marketing", [])
    if marketing:
        lines.append(f"## Marketing ({len(marketing)} emails)")

    return "\n".join(lines)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Email Capture - Inbox Digest")
    parser.add_argument("--unread", action="store_true", help="Unread only")
    parser.add_argument("--count", type=int, default=20, help="Max emails")
    args = parser.parse_args()

    digest = get_inbox_digest(max_results=args.count, unread_only=args.unread)
    print(format_digest(digest))
