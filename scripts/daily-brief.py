#!/usr/bin/env python3
"""
Daily Brief - Template for AI Employee module.

Configure your data sources below, then run:
    python scripts/daily-brief.py

This template pulls from:
- Stripe (revenue)
- Your task list
- Any custom data sources you add

Customize the sections and data sources to match your business.
"""

import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def get_revenue():
    """Pull revenue data from Stripe. Configure STRIPE_SECRET_KEY in .env"""
    api_key = os.getenv("STRIPE_SECRET_KEY")
    if not api_key:
        return {"available": False, "reason": "STRIPE_SECRET_KEY not set in .env"}

    try:
        import stripe
        stripe.api_key = api_key

        subs = stripe.Subscription.list(status="active", limit=100)
        mrr = 0
        for sub in subs.data:
            try:
                items = sub.get("items", {})
                items_data = items.get("data", []) if isinstance(items, dict) else getattr(items, "data", [])
                if items_data:
                    item = items_data[0]
                    price = item.get("price", {}) if isinstance(item, dict) else getattr(item, "price", {})
                    unit = price.get("unit_amount", 0) if isinstance(price, dict) else getattr(price, "unit_amount", 0)
                    mrr += (unit or 0)
            except Exception:
                continue

        return {"available": True, "mrr": mrr / 100, "subscriptions": len(subs.data)}
    except ImportError:
        return {"available": False, "reason": "pip install stripe"}
    except Exception as e:
        return {"available": False, "reason": str(e)}


def format_brief():
    """Generate the daily brief."""
    date = datetime.now().strftime("%A, %B %d")
    lines = [f"# Daily Brief - {date}", ""]

    # Revenue
    rev = get_revenue()
    if rev.get("available"):
        lines.append("## Revenue")
        lines.append(f"- MRR: ${rev['mrr']:,.0f}")
        lines.append(f"- Active subscriptions: {rev['subscriptions']}")
    else:
        lines.append(f"## Revenue\n_{rev.get('reason', 'Not configured')}_")
    lines.append("")

    # Add your own sections here:
    # - Pipeline stats (email outreach, leads)
    # - Task overview
    # - Health data (OURA, WHOOP)
    # - Calendar events

    lines.append("---")
    lines.append(f"_Generated at {datetime.now().strftime('%I:%M %p')}_")

    return "\n".join(lines)


if __name__ == "__main__":
    print(format_brief())
