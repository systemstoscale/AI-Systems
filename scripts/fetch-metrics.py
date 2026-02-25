#!/usr/bin/env python3
"""
Fetch Metrics - Template for AI Employee Data Dashboard.

Generic metrics aggregation script. Configure your data sources below.
Returns a structured dict that daily-brief.py can use.

Data sources to configure:
- Stripe (revenue, subscriptions)
- Your CRM or lead tracking tool
- Google Calendar (meetings today)
- Custom APIs

Usage:
    python scripts/fetch-metrics.py
"""

import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def fetch_stripe_metrics():
    """Fetch revenue metrics from Stripe."""
    api_key = os.getenv("STRIPE_SECRET_KEY")
    if not api_key:
        return None

    try:
        import stripe
        stripe.api_key = api_key
        from datetime import timedelta

        subs = stripe.Subscription.list(status="active", limit=100)
        mrr = sum(
            (s.get("items", {}).get("data", [{}])[0].get("price", {}).get("unit_amount", 0) or 0)
            for s in subs.data
        )

        yesterday = int((datetime.now() - timedelta(days=1)).timestamp())
        charges = stripe.Charge.list(created={"gte": yesterday}, limit=100)
        revenue_24h = sum(c.amount for c in charges.data if c.paid and not c.refunded)

        return {
            "mrr": mrr / 100,
            "subscriptions": len(subs.data),
            "revenue_24h": revenue_24h / 100,
        }
    except Exception as e:
        return {"error": str(e)}


def fetch_all():
    """Fetch all configured metrics."""
    metrics = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "generated_at": datetime.now().isoformat(),
    }

    # Stripe
    stripe_data = fetch_stripe_metrics()
    if stripe_data:
        metrics["stripe"] = stripe_data

    # Add more data sources here:
    # metrics["pipeline"] = fetch_pipeline_metrics()
    # metrics["calendar"] = fetch_calendar_events()

    return metrics


if __name__ == "__main__":
    data = fetch_all()
    print(json.dumps(data, indent=2, default=str))
