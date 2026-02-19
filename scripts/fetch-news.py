#!/usr/bin/env python3
"""
Fetch latest news on any topic using NewsAPI.

Usage:
    python3 scripts/fetch-news.py                    # Default: AI news
    python3 scripts/fetch-news.py "climate change"   # Custom topic

Requires:
    NEWS_API_KEY in .env file (free at https://newsapi.org/register)

No pip install needed — uses Python standard library only.
"""

import os
import sys
import json
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path


def load_env():
    """Load .env file into environment variables."""
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip())


def fetch_news(topic, api_key):
    """Fetch latest articles from NewsAPI."""
    params = urllib.parse.urlencode({
        "q": topic,
        "sortBy": "publishedAt",
        "pageSize": 10,
        "language": "en",
        "apiKey": api_key,
    })
    url = f"https://newsapi.org/v2/everything?{params}"

    req = urllib.request.Request(url, headers={"User-Agent": "AIDE/1.0"})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())


def main():
    load_env()

    api_key = os.environ.get("NEWS_API_KEY")
    if not api_key:
        print("ERROR: NEWS_API_KEY not found.\n")
        print("  1. Get a free key at https://newsapi.org/register")
        print("  2. Add it to your .env file:  NEWS_API_KEY=your_key_here")
        sys.exit(1)

    topic = sys.argv[1] if len(sys.argv) > 1 else "artificial intelligence"

    print(f"Fetching latest news on: {topic}")

    try:
        data = fetch_news(topic, api_key)
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print("ERROR: Invalid API key. Check your NEWS_API_KEY in .env")
        elif e.code == 429:
            print("ERROR: Rate limit hit. Free tier allows 100 requests/day.")
        else:
            print(f"ERROR: HTTP {e.code} — {e.reason}")
        sys.exit(1)

    if data.get("status") != "ok":
        print(f"ERROR: {data.get('message', 'Unknown error from NewsAPI')}")
        sys.exit(1)

    articles = data.get("articles", [])
    if not articles:
        print(f"No articles found for '{topic}'. Try a broader search term.")
        sys.exit(0)

    # Build markdown output
    lines = [
        f"# Latest News: {topic.title()}",
        f"*Fetched: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        f"*Source: NewsAPI | {len(articles)} articles*",
        "",
        "---",
        "",
    ]

    for i, article in enumerate(articles, 1):
        title = article.get("title", "Untitled")
        source = article.get("source", {}).get("name", "Unknown")
        description = article.get("description") or "No description available."
        url = article.get("url", "")
        published = article.get("publishedAt", "")[:10]

        lines.extend([
            f"## {i}. {title}",
            f"**Source:** {source} | **Date:** {published}",
            "",
            description,
            "",
            f"[Read full article]({url})",
            "",
            "---",
            "",
        ])

    # Save to outputs/
    output_dir = Path(__file__).parent.parent / "outputs"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "latest-news.md"
    output_file.write_text("\n".join(lines))

    print(f"Done — {len(articles)} articles saved to outputs/latest-news.md")


if __name__ == "__main__":
    main()
