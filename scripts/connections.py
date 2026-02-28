#!/usr/bin/env python3
"""
Connection Adapter - Universal tool connection layer for AI Employee.

Provides a unified interface for accessing external services.
Tries Composio first (one-click OAuth), falls back to direct API.

Supported providers:
  - Google (Gmail, Calendar, Drive) — Composio or credentials.json
  - Slack — Composio or SLACK_BOT_TOKEN
  - (More providers can be added following the same pattern)

Setup:
    Option A (Composio - recommended):
        1. Set COMPOSIO_API_KEY in .env
        2. Run: python scripts/connections.py connect google

    Option B (Direct API):
        Follow setup instructions in each module script.

Usage:
    python scripts/connections.py status              # Show connected tools
    python scripts/connections.py connect google      # Connect Google via Composio
    python scripts/connections.py connect slack       # Connect Slack via Composio
    python scripts/connections.py disconnect google   # Disconnect

    As a library:
        from connections import get_gmail_messages, get_calendar_events, composio_available
"""

import os
import sys
from pathlib import Path
from typing import Optional
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# Add shared integrations to path
_shared = Path(__file__).resolve().parent.parent.parent / "_shared" / "scripts"
if str(_shared) not in sys.path:
    sys.path.insert(0, str(_shared))


# ── Composio Client (lazy load) ───────────────────────────────

_composio_client = None


def _get_composio():
    """Get or create Composio client singleton."""
    global _composio_client
    if _composio_client is None:
        try:
            from integrations.composio_client import ComposioClient
            _composio_client = ComposioClient()
        except ImportError:
            return None
    return _composio_client


def composio_available(provider: Optional[str] = None) -> bool:
    """Check if Composio is configured and optionally if a provider is connected."""
    client = _get_composio()
    if not client or not client.available:
        return False
    if provider:
        return client.is_connected(provider)
    return True


# ── Gmail ──────────────────────────────────────────────────────

def get_gmail_messages(max_results: int = 20, unread_only: bool = False) -> list:
    """Get Gmail messages. Tries Composio first, falls back to direct API.

    Returns list of dicts with: id, subject, from, date, snippet, labelIds
    """
    if composio_available("google"):
        return _gmail_via_composio(max_results, unread_only)
    return _gmail_via_direct(max_results, unread_only)


def _gmail_via_composio(max_results: int, unread_only: bool) -> list:
    """Fetch Gmail messages via Composio."""
    client = _get_composio()
    if not client:
        return []

    try:
        query = "is:inbox is:unread" if unread_only else "is:inbox"
        result = client.execute_tool("GMAIL_SEARCH_EMAILS", {
            "query": query,
            "max_results": max_results,
        })

        if not result.get("successful", False):
            print(f"Composio Gmail error: {result.get('error', 'unknown')}")
            return []

        data = result.get("data", {})
        messages = data.get("messages", data.get("emails", []))

        # Normalize to standard format
        normalized = []
        for msg in messages:
            normalized.append({
                "id": msg.get("id", ""),
                "subject": msg.get("subject", "(No subject)"),
                "from": msg.get("from", msg.get("sender", "")),
                "date": msg.get("date", ""),
                "snippet": msg.get("snippet", msg.get("body_preview", "")),
                "labelIds": msg.get("labelIds", msg.get("labels", [])),
            })
        return normalized

    except Exception as e:
        print(f"Composio Gmail error: {e}")
        return []


def _gmail_via_direct(max_results: int, unread_only: bool) -> list:
    """Fetch Gmail messages via direct Google API (existing flow)."""
    try:
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build

        SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
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

        service = build("gmail", "v1", credentials=creds)
        query = "is:inbox is:unread" if unread_only else "is:inbox"

        results = service.users().messages().list(
            userId="me", q=query, maxResults=max_results
        ).execute()

        messages = []
        for msg_ref in results.get("messages", []):
            msg = service.users().messages().get(
                userId="me", id=msg_ref["id"], format="metadata",
                metadataHeaders=["Subject", "From", "Date"]
            ).execute()
            headers = {h["name"]: h["value"] for h in msg.get("payload", {}).get("headers", [])}
            messages.append({
                "id": msg["id"],
                "subject": headers.get("Subject", "(No subject)"),
                "from": headers.get("From", ""),
                "date": headers.get("Date", ""),
                "snippet": msg.get("snippet", ""),
                "labelIds": msg.get("labelIds", []),
            })
        return messages

    except ImportError:
        print("Direct Gmail not available. Install: pip install google-api-python-client google-auth-oauthlib")
        print("Or connect via Composio: python scripts/connections.py connect google")
        return []
    except Exception as e:
        print(f"Direct Gmail error: {e}")
        return []


# ── Calendar ───────────────────────────────────────────────────

def get_calendar_events(days: int = 1) -> list:
    """Get calendar events. Tries Composio first, falls back to direct API.

    Returns list of dicts with: summary, start, end, attendees, meet_link
    """
    if composio_available("google") or composio_available("google_calendar"):
        return _calendar_via_composio(days)
    return _calendar_via_direct(days)


def _calendar_via_composio(days: int) -> list:
    """Fetch calendar events via Composio."""
    client = _get_composio()
    if not client:
        return []

    try:
        now = datetime.utcnow()
        if days <= 1:
            time_min = now.replace(hour=0, minute=0, second=0).isoformat() + "Z"
            time_max = (now.replace(hour=0, minute=0, second=0) + timedelta(days=1)).isoformat() + "Z"
        else:
            time_min = (now - timedelta(days=days)).isoformat() + "Z"
            time_max = now.isoformat() + "Z"

        result = client.execute_tool("GOOGLE_CALENDAR_LIST_EVENTS", {
            "calendar_id": "primary",
            "time_min": time_min,
            "time_max": time_max,
        })

        if not result.get("successful", False):
            print(f"Composio Calendar error: {result.get('error', 'unknown')}")
            return []

        data = result.get("data", {})
        events = data.get("items", data.get("events", []))

        normalized = []
        for event in events:
            attendees = event.get("attendees", [])
            normalized.append({
                "summary": event.get("summary", "(No title)"),
                "start": event.get("start", {}).get("dateTime", ""),
                "end": event.get("end", {}).get("dateTime", ""),
                "attendees": len(attendees) if isinstance(attendees, list) else 0,
                "meet_link": event.get("hangoutLink", ""),
            })
        return normalized

    except Exception as e:
        print(f"Composio Calendar error: {e}")
        return []


def _calendar_via_direct(days: int) -> list:
    """Fetch calendar events via direct Google API (existing flow)."""
    try:
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build

        SCOPES = [
            "https://www.googleapis.com/auth/calendar.readonly",
            "https://www.googleapis.com/auth/drive.readonly",
        ]
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

        service = build("calendar", "v3", credentials=creds)
        now = datetime.utcnow()

        if days <= 1:
            start = now.replace(hour=0, minute=0, second=0).isoformat() + "Z"
            end = (now.replace(hour=0, minute=0, second=0) + timedelta(days=1)).isoformat() + "Z"
        else:
            start = (now - timedelta(days=days)).isoformat() + "Z"
            end = now.isoformat() + "Z"

        events_result = service.events().list(
            calendarId="primary",
            timeMin=start,
            timeMax=end,
            singleEvents=True,
            orderBy="startTime",
        ).execute()

        meetings = []
        for event in events_result.get("items", []):
            attendees = event.get("attendees", [])
            meet_link = event.get("hangoutLink", "")
            if attendees or meet_link:
                meetings.append({
                    "summary": event.get("summary", "(No title)"),
                    "start": event.get("start", {}).get("dateTime", ""),
                    "end": event.get("end", {}).get("dateTime", ""),
                    "attendees": len(attendees),
                    "meet_link": meet_link,
                })
        return meetings

    except ImportError:
        print("Direct Calendar not available. Install: pip install google-api-python-client google-auth-oauthlib")
        print("Or connect via Composio: python scripts/connections.py connect google")
        return []
    except Exception as e:
        print(f"Direct Calendar error: {e}")
        return []


# ── Slack ──────────────────────────────────────────────────────

def get_slack_channels() -> list:
    """Get Slack channels. Tries Composio first, falls back to direct API.

    Returns list of dicts with: id, name, members
    """
    if composio_available("slack"):
        return _slack_channels_via_composio()
    return _slack_channels_via_direct()


def get_slack_messages(channel_id: str, hours: int = 24) -> list:
    """Get Slack messages from a channel. Tries Composio first, falls back to direct API.

    Returns list of dicts with: text, user, ts, reactions
    """
    if composio_available("slack"):
        return _slack_messages_via_composio(channel_id, hours)
    return _slack_messages_via_direct(channel_id, hours)


def _slack_channels_via_composio() -> list:
    client = _get_composio()
    if not client:
        return []
    try:
        result = client.execute_tool("SLACK_LIST_CHANNELS", {
            "types": "public_channel,private_channel",
            "limit": 100,
        })
        if not result.get("successful", False):
            return []
        data = result.get("data", {})
        channels = data.get("channels", [])
        return [
            {"id": c.get("id", ""), "name": c.get("name", ""), "members": c.get("num_members", 0)}
            for c in channels
            if c.get("is_member")
        ]
    except Exception as e:
        print(f"Composio Slack channels error: {e}")
        return []


def _slack_channels_via_direct() -> list:
    import requests as req
    token = os.getenv("SLACK_BOT_TOKEN")
    if not token:
        return []
    resp = req.get("https://slack.com/api/conversations.list", headers={"Authorization": f"Bearer {token}"}, params={"types": "public_channel,private_channel", "limit": 100})
    data = resp.json()
    if not data.get("ok"):
        return []
    return [
        {"id": c["id"], "name": c["name"], "members": c.get("num_members", 0)}
        for c in data.get("channels", [])
        if c.get("is_member")
    ]


def _slack_messages_via_composio(channel_id: str, hours: int) -> list:
    client = _get_composio()
    if not client:
        return []
    try:
        oldest = str((datetime.now() - timedelta(hours=hours)).timestamp())
        result = client.execute_tool("SLACK_GET_CHANNEL_HISTORY", {
            "channel": channel_id,
            "oldest": oldest,
            "limit": 100,
        })
        if not result.get("successful", False):
            return []
        data = result.get("data", {})
        messages = []
        for msg in data.get("messages", []):
            if msg.get("subtype") in ("channel_join", "channel_leave", "bot_message"):
                continue
            messages.append({
                "text": msg.get("text", ""),
                "user": msg.get("user", ""),
                "ts": msg.get("ts", ""),
                "reactions": len(msg.get("reactions", [])),
            })
        return messages
    except Exception as e:
        print(f"Composio Slack messages error: {e}")
        return []


def _slack_messages_via_direct(channel_id: str, hours: int) -> list:
    import requests as req
    token = os.getenv("SLACK_BOT_TOKEN")
    if not token:
        return []
    oldest = str((datetime.now() - timedelta(hours=hours)).timestamp())
    resp = req.get("https://slack.com/api/conversations.history", headers={"Authorization": f"Bearer {token}"}, params={"channel": channel_id, "oldest": oldest, "limit": 100})
    data = resp.json()
    if not data.get("ok"):
        return []
    messages = []
    for msg in data.get("messages", []):
        if msg.get("subtype") in ("channel_join", "channel_leave", "bot_message"):
            continue
        messages.append({
            "text": msg.get("text", ""),
            "user": msg.get("user", ""),
            "ts": msg.get("ts", ""),
            "reactions": len(msg.get("reactions", [])),
        })
    return messages


# ── Status / Connect ──────────────────────────────────────────

def status() -> dict:
    """Get connection status for all providers."""
    providers = {
        "Google (Gmail + Calendar)": "google",
        "Slack": "slack",
    }

    result = {}
    composio = _get_composio()
    composio_configured = composio and composio.available

    for label, slug in providers.items():
        if composio_configured and composio.is_connected(slug):
            result[label] = "Connected (Composio)"
        elif slug == "google" and os.path.exists("token.json"):
            result[label] = "Connected (Direct API)"
        elif slug == "slack" and os.getenv("SLACK_BOT_TOKEN"):
            result[label] = "Connected (Direct API)"
        else:
            result[label] = "Not connected"

    return {
        "composio_configured": composio_configured,
        "providers": result,
    }


def connect_tool(provider: str) -> bool:
    """Connect a tool via Composio interactive OAuth flow."""
    client = _get_composio()
    if not client or not client.available:
        print("Error: COMPOSIO_API_KEY not set in .env")
        print("Get your free API key at https://composio.dev")
        return False
    return client.connect_interactive(provider)


# ── CLI Interface ──────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI Employee Tool Connections")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    subparsers.add_parser("status", help="Show connection status")

    connect_parser = subparsers.add_parser("connect", help="Connect a tool")
    connect_parser.add_argument("provider", help="Provider to connect (google, slack)")

    disconnect_parser = subparsers.add_parser("disconnect", help="Disconnect a tool")
    disconnect_parser.add_argument("provider", help="Provider to disconnect")

    args = parser.parse_args()

    if args.command == "status":
        s = status()
        if not s["composio_configured"]:
            print("Composio: Not configured (set COMPOSIO_API_KEY in .env for one-click OAuth)")
        else:
            print("Composio: Configured")
        print()
        for label, state in s["providers"].items():
            icon = "+" if "Connected" in state else "-"
            print(f"  {icon} {label}: {state}")
        print()
        print("Connect tools: python scripts/connections.py connect <provider>")

    elif args.command == "connect":
        connect_tool(args.provider)

    elif args.command == "disconnect":
        client = _get_composio()
        if client and client.available:
            connections = client.list_connections()
            for c in connections:
                if c.get("appName", "").lower() == args.provider.lower():
                    client.revoke_connection(c["id"])
                    print(f"Disconnected {args.provider}")
                    break
            else:
                print(f"No Composio connection found for {args.provider}")
        else:
            print("Composio not configured. Remove API keys manually from .env")

    else:
        parser.print_help()
