"""
Fetch social media profile data for @scalermax
Platforms: Instagram, LinkedIn (scalermax), YouTube (scalermax)
Uses: ScrapeCreators API
"""

import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SCRAPECREATORS_API_KEY")
HEADERS = {"x-api-key": API_KEY}
HANDLE = "scalermax"


def fetch(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    r.raise_for_status()
    return r.json()


def get_instagram():
    print("Fetching Instagram profile...")
    return fetch(
        "https://api.scrapecreators.com/v1/instagram/profile",
        params={"handle": HANDLE}
    )


def get_linkedin():
    print("Fetching LinkedIn profile...")
    return fetch(
        "https://api.scrapecreators.com/v1/linkedin/profile",
        params={"handle": HANDLE}
    )


def get_youtube():
    print("Fetching YouTube channel...")
    return fetch(
        "https://api.scrapecreators.com/v1/youtube/channel",
        params={"handle": HANDLE}
    )


if __name__ == "__main__":
    results = {}

    for platform, fn in [("instagram", get_instagram), ("linkedin", get_linkedin), ("youtube", get_youtube)]:
        try:
            results[platform] = fn()
            print(f"  {platform}: OK")
        except Exception as e:
            results[platform] = {"error": str(e)}
            print(f"  {platform}: FAILED — {e}")

    # Save raw output
    out_path = "outputs/social-profiles-raw.json"
    os.makedirs("outputs", exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nSaved to {out_path}")
    print(json.dumps(results, indent=2))
