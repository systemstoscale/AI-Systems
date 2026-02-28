#!/usr/bin/env python3
"""
Slack Intelligence - Template for AI Employee module.

Reads Slack channels, extracts action items, and generates summaries.
Feeds into the Daily Brief for context on team activity.

Setup:
    Option A (Composio - recommended):
        python scripts/connections.py connect slack

    Option B (Direct API):
        1. Create a Slack app at api.slack.com/apps
        2. Add bot scopes: channels:history, channels:read
        3. Install to workspace, copy Bot Token
        4. Set SLACK_BOT_TOKEN in .env

Usage:
    python scripts/slack-intel.py                           # All channels
    python scripts/slack-intel.py --channel general         # Specific channel
    python scripts/slack-intel.py --hours 48                # Last 48 hours
"""

import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Add scripts dir to path for connections adapter
sys.path.insert(0, str(Path(__file__).resolve().parent))


# ── Direct API fallback functions ──────────────────────────────

def slack_api(method, token, params=None):
    """Make a Slack API call (direct fallback)."""
    try:
        import requests
    except ImportError:
        print("Install requests: pip install requests")
        return None
    url = f"https://slack.com/api/{method}"
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(url, headers=headers, params=params or {})
    data = resp.json()
    if not data.get("ok"):
        return None
    return data


def list_channels(token):
    """List channels (direct fallback)."""
    data = slack_api("conversations.list", token, {"types": "public_channel,private_channel", "limit": 100})
    if not data:
        return []
    return [
        {"id": c["id"], "name": c["name"], "members": c.get("num_members", 0)}
        for c in data.get("channels", [])
        if c.get("is_member")
    ]


def get_channel_messages(token, channel_id, hours=24):
    """Get recent messages from a channel (direct fallback)."""
    oldest = str((datetime.now() - timedelta(hours=hours)).timestamp())
    data = slack_api("conversations.history", token, {"channel": channel_id, "oldest": oldest, "limit": 100})
    if not data:
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


# ── Core Logic ─────────────────────────────────────────────────

def summarize_channel(channel_name, messages):
    """Generate a summary of channel activity."""
    if not messages:
        return f"**#{channel_name}**: No activity"

    total = len(messages)
    reacted = sum(1 for m in messages if m.get("reactions", 0) > 0)

    return f"**#{channel_name}**: {total} messages ({reacted} with reactions)"


def _get_channels_and_messages(channels_filter, hours):
    """Get channels and their messages using connections adapter or direct API."""
    try:
        from connections import get_slack_channels, get_slack_messages as conn_get_messages
        all_channels = get_slack_channels()
        if all_channels:
            if channels_filter:
                all_channels = [c for c in all_channels if c["name"] in channels_filter]
            result = []
            for ch in all_channels:
                msgs = conn_get_messages(ch["id"], hours=hours)
                result.append((ch, msgs))
            return result
    except ImportError:
        pass

    # Fallback to direct API
    token = os.getenv("SLACK_BOT_TOKEN")
    if not token:
        return None
    all_channels = list_channels(token)
    if not all_channels:
        return None
    if channels_filter:
        all_channels = [c for c in all_channels if c["name"] in channels_filter]
    result = []
    for ch in all_channels:
        msgs = get_channel_messages(token, ch["id"], hours=hours)
        result.append((ch, msgs))
    return result


def get_slack_digest(channels=None, hours=24):
    """Generate a full Slack digest. Uses connections adapter (Composio or direct)."""
    channel_data = _get_channels_and_messages(channels, hours)
    if channel_data is None:
        return {"available": False, "error": "Slack not configured. Run: python scripts/connections.py connect slack"}

    if not channel_data:
        return {"available": False, "error": "No channels accessible"}

    summaries = []
    total_messages = 0

    for channel, messages in channel_data:
        total_messages += len(messages)
        summaries.append({
            "channel": channel["name"],
            "message_count": len(messages),
            "summary": summarize_channel(channel["name"], messages),
        })

    # Sort by activity
    summaries.sort(key=lambda x: x["message_count"], reverse=True)

    return {
        "available": True,
        "channels_checked": len(channel_data),
        "total_messages": total_messages,
        "hours": hours,
        "summaries": summaries,
    }


def format_digest(digest):
    """Format Slack digest into readable output."""
    if not digest.get("available"):
        return f"# Slack Intelligence\n\nError: {digest.get('error', 'Unknown')}"

    lines = [
        f"# Slack Intelligence",
        f"Last {digest['hours']}h | {digest['channels_checked']} channels | {digest['total_messages']} messages",
        "",
    ]

    for s in digest["summaries"]:
        if s["message_count"] > 0:
            lines.append(f"- {s['summary']}")

    quiet = [s for s in digest["summaries"] if s["message_count"] == 0]
    if quiet:
        lines.append(f"\n_Quiet: {', '.join('#' + s['channel'] for s in quiet)}_")

    return "\n".join(lines)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Slack Intelligence")
    parser.add_argument("--channel", help="Specific channel name")
    parser.add_argument("--hours", type=int, default=24, help="Hours to look back")
    args = parser.parse_args()

    channels = [args.channel] if args.channel else None
    digest = get_slack_digest(channels=channels, hours=args.hours)
    print(format_digest(digest))
