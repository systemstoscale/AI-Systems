#!/usr/bin/env python3
"""
Slack Intelligence - Template for AI Employee module.

Reads Slack channels, extracts action items, and generates summaries.
Feeds into the Daily Brief for context on team activity.

Setup:
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
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()


def get_slack_client():
    """Get a simple Slack API wrapper using requests."""
    token = os.getenv("SLACK_BOT_TOKEN")
    if not token:
        return None, "SLACK_BOT_TOKEN not set in .env"
    return token, None


def slack_api(method, token, params=None):
    """Make a Slack API call."""
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
        print(f"Slack API error: {data.get('error', 'unknown')}")
        return None
    return data


def list_channels(token):
    """List channels the bot has access to."""
    data = slack_api("conversations.list", token, {
        "types": "public_channel,private_channel",
        "limit": 100,
    })
    if not data:
        return []

    return [
        {"id": c["id"], "name": c["name"], "members": c.get("num_members", 0)}
        for c in data.get("channels", [])
        if c.get("is_member")
    ]


def get_channel_messages(token, channel_id, hours=24):
    """Get recent messages from a channel."""
    oldest = str((datetime.now() - timedelta(hours=hours)).timestamp())

    data = slack_api("conversations.history", token, {
        "channel": channel_id,
        "oldest": oldest,
        "limit": 100,
    })
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


def summarize_channel(channel_name, messages):
    """Generate a summary of channel activity."""
    if not messages:
        return f"**#{channel_name}**: No activity"

    total = len(messages)
    reacted = sum(1 for m in messages if m.get("reactions", 0) > 0)

    return f"**#{channel_name}**: {total} messages ({reacted} with reactions)"


def get_slack_digest(channels=None, hours=24):
    """Generate a full Slack digest."""
    token, error = get_slack_client()
    if error:
        return {"available": False, "error": error}

    all_channels = list_channels(token)
    if not all_channels:
        return {"available": False, "error": "No channels accessible"}

    # Filter to specific channels if requested
    if channels:
        all_channels = [c for c in all_channels if c["name"] in channels]

    summaries = []
    total_messages = 0

    for channel in all_channels:
        messages = get_channel_messages(token, channel["id"], hours=hours)
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
        "channels_checked": len(all_channels),
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
