# Instruction: Data Dashboard

## Goal
Aggregate metrics from multiple data sources into a single structured dict that other modules (Daily Brief, Check-in) can consume.

## Script
`scripts/fetch-metrics.py`

## Steps
1. Run `python scripts/fetch-metrics.py`
2. Review the JSON output
3. Add new data sources by editing the script
4. Other modules import from this script — it's the single source of truth

## Architecture

```
fetch-metrics.py (Data Dashboard)
├── fetch_stripe_metrics()     → Revenue, MRR, subscriptions
├── fetch_pipeline_metrics()   → Email outreach stats (add your tool)
├── fetch_calendar_events()    → Today's meetings (add Google OAuth)
├── fetch_health_data()        → OURA, WHOOP, Apple Health (add tokens)
└── fetch_custom_metrics()     → Anything else you want to track
         │
         ▼
    Structured dict
         │
    ┌────┴────┐
    ▼         ▼
daily-brief  check-in
```

The Data Dashboard doesn't format anything. It returns raw data. Formatting is the job of the module that consumes it (Daily Brief formats for terminal/Slack/Telegram, Check-in formats for interactive use).

## Data Sources

### Stripe (Revenue)
- **Env var:** `STRIPE_SECRET_KEY`
- **Install:** `pip install stripe`
- **Returns:** MRR, active subscriptions, 24h revenue, 7-day revenue

### Email Outreach (Pipeline)
- **Options:** Instantly, Lemlist, Smartlead, Apollo
- **Env var:** Depends on your tool
- **Returns:** Emails sent, opens, replies, active campaigns

### Google Calendar (Meetings)
- **Setup:** OAuth2 with `credentials.json`
- **Scopes:** `calendar.readonly`
- **Returns:** Today's events, attendee count, meeting links

### Health Trackers
- **Options:** OURA, WHOOP, Apple Health (via webhook)
- **Env var:** OAuth tokens or API keys
- **Returns:** Sleep, readiness, recovery, HRV, steps

### Custom Sources
Add any API by creating a new `fetch_*` function:
```python
def fetch_my_custom_data():
    """Pull data from your custom API."""
    api_key = os.getenv("MY_API_KEY")
    if not api_key:
        return None
    # Make API call, return dict
    return {"metric_1": value, "metric_2": value}
```

Then add it to `fetch_all()`:
```python
custom = fetch_my_custom_data()
if custom:
    metrics["custom"] = custom
```

## Output Format
```json
{
  "date": "2026-02-24",
  "generated_at": "2026-02-24T08:00:00",
  "stripe": {"mrr": 5000, "subscriptions": 12, "revenue_24h": 499},
  "pipeline": {"sent": 500, "opens": 200, "replies": 15},
  "calendar": [{"summary": "Team Standup", "start": "09:00"}]
}
```

## Tips
- Start with Stripe only — it's the easiest to set up (just one API key)
- Add sources incrementally — the brief still works if sources are missing
- Run `fetch-metrics.py` standalone to debug individual data sources
- Cache expensive API calls if you're hitting rate limits
