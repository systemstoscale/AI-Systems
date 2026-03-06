"""
fetch-google-doc.py
Fetches a Google Doc by ID and saves its content to outputs/.

Setup:
1. Enable Google Docs API in Google Cloud Console
2. Create a Service Account, download the JSON key
3. Save it as google-credentials.json in your workspace root
4. Share your Google Doc with the service account email (Viewer access)

Usage:
  python3 scripts/fetch-google-doc.py <doc_id_or_url>

Examples:
  python3 scripts/fetch-google-doc.py 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms
  python3 scripts/fetch-google-doc.py "https://docs.google.com/document/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms/edit"
"""

import sys
import os
import re
from datetime import datetime
from pathlib import Path

try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
except ImportError:
    print("Missing dependencies. Run: pip3 install google-auth google-auth-httplib2 google-api-python-client")
    sys.exit(1)

try:
    from dotenv import dotenv_values
    env = dotenv_values(".env")
except ImportError:
    env = {}


def _env(key):
    return env.get(key) or os.environ.get(key) or ""


def extract_doc_id(input_str: str) -> str:
    """Extract doc ID from a full URL or return the raw ID."""
    match = re.search(r"/document/d/([a-zA-Z0-9_-]+)", input_str)
    if match:
        return match.group(1)
    return input_str.strip()


def get_doc_text(doc_id: str, credentials_path: str) -> tuple[str, str]:
    """Fetch document title and plain text content."""
    creds = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=["https://www.googleapis.com/auth/documents.readonly"]
    )
    service = build("docs", "v1", credentials=creds)
    doc = service.documents().get(documentId=doc_id).execute()

    title = doc.get("title", "untitled")

    # Extract text from document body
    lines = []
    for element in doc.get("body", {}).get("content", []):
        para = element.get("paragraph")
        if not para:
            continue
        line_parts = []
        for run in para.get("elements", []):
            text_run = run.get("textRun")
            if text_run:
                line_parts.append(text_run.get("content", ""))
        lines.append("".join(line_parts))

    return title, "".join(lines)


def save_output(title: str, content: str) -> str:
    """Save content to outputs/ and return the file path."""
    Path("outputs").mkdir(exist_ok=True)

    # Sanitize title for filename
    safe_title = re.sub(r"[^\w\s-]", "", title).strip().replace(" ", "-").lower()
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"outputs/transcript-{safe_title}-{date_str}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"*Fetched: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n")
        f.write("---\n\n")
        f.write(content)

    return filename


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/fetch-google-doc.py <doc_id_or_url>")
        sys.exit(1)

    input_arg = sys.argv[1]
    doc_id = extract_doc_id(input_arg)

    credentials_path = _env("GOOGLE_CREDENTIALS_PATH") or "google-credentials.json"
    if not Path(credentials_path).exists():
        print(f"Credentials file not found: {credentials_path}")
        print("Download your service account JSON key from Google Cloud Console")
        print("and save it as google-credentials.json in your workspace root.")
        sys.exit(1)

    print(f"Fetching doc: {doc_id}")
    title, content = get_doc_text(doc_id, credentials_path)
    print(f"Title: {title}")
    print(f"Length: {len(content):,} characters")

    output_path = save_output(title, content)
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()
