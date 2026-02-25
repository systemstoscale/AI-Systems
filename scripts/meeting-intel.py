#!/usr/bin/env python3
"""
Meeting Intelligence - Template for AI Employee module.

Search Google Meet transcripts, list upcoming meetings, and generate digests.
Requires Google OAuth setup (see instructions/health-integration-setup.md for OAuth pattern).

Setup:
    1. Enable Google Calendar API + Drive API in Google Cloud Console
    2. Download credentials.json to this directory
    3. Run this script once to complete OAuth flow
    4. Transcript access requires Google Meet transcription enabled

Usage:
    python scripts/meeting-intel.py                     # Today's meetings
    python scripts/meeting-intel.py --days 7            # Last 7 days
    python scripts/meeting-intel.py --search "budget"   # Search transcripts
"""

import os
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# Google API scopes needed
SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]


def get_google_service(service_name, version):
    """
    Get an authenticated Google API service.
    You'll need to implement OAuth2 flow — see Google's quickstart:
    https://developers.google.com/calendar/api/quickstart/python
    """
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

        return build(service_name, version, credentials=creds)
    except ImportError:
        print("Install Google API libraries: pip install google-api-python-client google-auth-oauthlib")
        return None
    except Exception as e:
        print(f"Google auth error: {e}")
        return None


def list_meetings(days=1):
    """List meetings from Google Calendar."""
    service = get_google_service("calendar", "v3")
    if not service:
        return []

    now = datetime.utcnow()
    start = (now - timedelta(days=days)).isoformat() + "Z"
    end = now.isoformat() + "Z" if days > 0 else (now + timedelta(days=1)).isoformat() + "Z"

    # For today's meetings, look forward
    if days <= 1:
        start = now.replace(hour=0, minute=0, second=0).isoformat() + "Z"
        end = (now.replace(hour=0, minute=0, second=0) + timedelta(days=1)).isoformat() + "Z"

    events = service.events().list(
        calendarId="primary",
        timeMin=start,
        timeMax=end,
        singleEvents=True,
        orderBy="startTime",
    ).execute()

    meetings = []
    for event in events.get("items", []):
        attendees = event.get("attendees", [])
        meet_link = event.get("hangoutLink", "")
        # Filter to actual meetings (has attendees or Meet link)
        if attendees or meet_link:
            meetings.append({
                "summary": event.get("summary", "(No title)"),
                "start": event.get("start", {}).get("dateTime", ""),
                "end": event.get("end", {}).get("dateTime", ""),
                "attendees": len(attendees),
                "meet_link": meet_link,
            })
    return meetings


def search_transcripts(query, days=30):
    """Search Google Meet transcripts in Drive."""
    service = get_google_service("drive", "v3")
    if not service:
        return []

    after = (datetime.utcnow() - timedelta(days=days)).strftime("%Y-%m-%d")
    q = f"fullText contains '{query}' and mimeType='text/plain' and name contains 'Transcript' and modifiedTime > '{after}'"

    results = service.files().list(
        q=q, pageSize=10, fields="files(id, name, modifiedTime, webViewLink)"
    ).execute()

    return results.get("files", [])


def format_meetings(meetings, title="Today's Meetings"):
    """Format meetings into readable output."""
    if not meetings:
        return f"# {title}\n\nNo meetings found."

    lines = [f"# {title}", ""]
    for m in meetings:
        start = m.get("start", "")
        if "T" in start:
            try:
                dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
                time_str = dt.strftime("%I:%M %p")
            except ValueError:
                time_str = start
        else:
            time_str = ""

        att = f" ({m['attendees']} attendees)" if m.get("attendees") else ""
        lines.append(f"- **{m['summary']}** — {time_str}{att}")

    return "\n".join(lines)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Meeting Intelligence")
    parser.add_argument("--days", type=int, default=1, help="Days to look back")
    parser.add_argument("--search", help="Search transcripts for keyword")
    args = parser.parse_args()

    if args.search:
        results = search_transcripts(args.search)
        if results:
            print(f"# Transcript Search: '{args.search}'\n")
            for doc in results:
                print(f"- {doc['name']} — {doc.get('webViewLink', '')}")
        else:
            print(f"No transcripts found matching '{args.search}'")
    else:
        meetings = list_meetings(days=args.days)
        print(format_meetings(meetings))
