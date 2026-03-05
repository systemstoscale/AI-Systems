---
module_id: ops
module_name: Operations & Productivity
module_number: 15
category: business
description: Daily briefings, KPI tracking, inbox management, habit monitoring
env_keys:
  required: []
  optional:
    - key: STRIPE_SECRET_KEY
      label: Stripe Secret Key
      get_url: https://dashboard.stripe.com/apikeys
      hint: "For revenue data"
    - key: ANTHROPIC_API_KEY
      label: Anthropic API Key
      get_url: https://console.anthropic.com/settings/keys
      hint: "For AI-powered summaries"
pip_packages: [python-dotenv, requests]
test_command: "python scripts/daily-brief.py"
estimated_time: "20 minutes"
interactive_steps: true
---

# Instruction: Operations & Productivity Setup

## Goal
Build a personal operations system: daily briefings, productivity check-ins, KPI tracking, inbox management, and habit monitoring. End state: the user starts each day with a clear picture of what matters and ends each day knowing what they accomplished.

## Inputs
- `data_sources` (list): What to pull data from — "stripe", "google_analytics", "crm", "email", "calendar", "slack", "health_tracker"
- `kpis` (list): Key metrics to track (e.g., `["mrr", "pipeline_value", "email_open_rate", "daily_calls"]`)
- `work_hours` (dict): Schedule (e.g., `{"start": "08:00", "end": "18:00", "timezone": "America/New_York"}`)
- `habits` (list, optional): Daily habits to track (e.g., `["exercise", "reading", "meditation"]`)
- `review_cadence` (string): "daily", "daily+weekly", "daily+weekly+monthly"

## Steps

### 1. Set up the Daily Brief (Module #2)

The Daily Brief is the core operations module. It pulls data from all connected sources and generates a morning summary.

**Create `scripts/daily-brief.py`:**
1. Connect to available data sources (check `.env` for configured keys)
2. Pull metrics for the last 24 hours
3. Generate a formatted briefing
4. Save to `outputs/briefs/brief-[YYYY-MM-DD].md`

**Brief template:**
```markdown
# Daily Brief — [Date]

## Revenue
- Yesterday: $X,XXX
- MTD: $XX,XXX (XX% of $XXK target)
- Trend: ↑/↓ X% vs last week

## Pipeline
- Active deals: X ($XXK total value)
- Meetings today: X
- Follow-ups due: X

## Inbox Summary
- Unread: X (X urgent)
- Key messages: [1-3 important emails summarized]

## Calendar
- Next meeting: [Name] at [Time]
- Today's schedule: [X meetings, Y hours blocked]

## Tasks
- Priority 1: [from todo.md or task system]
- Priority 2: [...]
- Priority 3: [...]

## Health (optional)
- Sleep: Xh XXm (score: XX)
- Recovery: XX%
- Steps: X,XXX

## Focus for Today
[AI-generated recommendation based on all the above data]
```

### 2. Connect data sources

Set up connections one at a time. Each is independent — missing sources just show "Not configured."

**Stripe (Revenue):**
1. Get API key from Stripe Dashboard → Developers → API Keys
2. Add `STRIPE_SECRET_KEY` to `.env`
3. The brief pulls: yesterday's revenue, MTD, MRR, recent charges

**Google Calendar:**
1. Set up OAuth via `scripts/connections.py` or Composio
2. The brief pulls: today's events, upcoming meetings, free time slots

**Gmail:**
1. Same OAuth as Calendar (Google scopes include both)
2. The brief pulls: unread count, urgent messages, key threads

**Slack:**
1. Create a Slack app or connect via Composio
2. Add `SLACK_BOT_TOKEN` to `.env`
3. The brief pulls: unread channels, mentions, action items

**Health tracker (Oura, Whoop, Apple Health):**
1. Connect via respective API
2. Add API token to `.env`
3. The brief pulls: sleep score, recovery, readiness

**CRM (HubSpot, Pipedrive, Airtable, etc.):**
1. Connect via API
2. The brief pulls: pipeline value, deal movement, follow-ups due

### 3. Set up Productivity Check-ins (Module #4)

Create `scripts/checkin.py` that runs context-aware check-ins based on time of day:

**Morning check-in (before work):**
```
1. How did you sleep? (1-10 or pull from health tracker)
2. What's your #1 priority today?
3. Any blockers or things you're dreading?
4. Energy level? (1-10)
→ AI sets the day's focus and suggests time blocks
```

**Midday check-in (optional):**
```
1. How's the day going? (on track / behind / ahead)
2. Did you complete your #1 priority?
3. Any fires to put out?
→ AI adjusts afternoon priorities
```

**Evening review:**
```
1. What did you accomplish today?
2. What didn't get done? (Move to tomorrow or drop?)
3. Any lessons or insights?
4. What's tomorrow's #1 priority?
→ AI logs the day and preps tomorrow's brief
```

**Logging:**
Save check-in data to `data/checkins/[YYYY-MM-DD].json`:
```json
{
  "date": "2026-03-04",
  "morning": {
    "sleep_quality": 7,
    "energy": 8,
    "priority": "Close the Smith deal",
    "blockers": "Waiting on proposal feedback"
  },
  "evening": {
    "completed": ["Smith deal closed", "Sent 3 proposals"],
    "not_completed": ["Blog post"],
    "lessons": "Follow up same day, don't wait",
    "tomorrow_priority": "Write blog post"
  }
}
```

### 4. Set up KPI tracking (Module #3)

Create `scripts/fetch-metrics.py` that aggregates key metrics:

**Define KPIs with the user:**

| Category | Example KPIs | Source |
|----------|-------------|--------|
| Revenue | MRR, ARR, Revenue growth %, Churn | Stripe |
| Sales | Pipeline value, Close rate, Avg deal size | CRM |
| Marketing | Leads/week, CAC, Email open rate, Social followers | Various |
| Product | Active users, Churn rate, NPS | Analytics |
| Operations | Tasks completed, Response time | Internal |

Create `data/kpis.json` to store targets and actuals:
```json
{
  "mrr": {"target": 50000, "current": 42000, "unit": "dollars"},
  "pipeline_value": {"target": 200000, "current": 175000, "unit": "dollars"},
  "weekly_calls": {"target": 15, "current": 12, "unit": "count"},
  "email_response_time": {"target": 4, "current": 6, "unit": "hours"}
}
```

**Weekly KPI report:**
Create `instructions/weekly-review.md` that generates:
- KPI dashboard (actuals vs targets)
- Week-over-week trends
- Top wins
- Biggest gaps
- Focus areas for next week

Save to `outputs/reviews/weekly-[YYYY-WXX].md`.

### 5. Set up inbox management

Create `instructions/inbox-workflow.md`:

**Email triage system:**

| Priority | Signal | Action | Response Time |
|----------|--------|--------|---------------|
| Urgent | From VIP list, contains "urgent"/"asap" | Handle immediately | < 1 hour |
| Important | Client emails, revenue-related | Handle today | < 4 hours |
| Normal | Everything else | Batch process 2x/day | < 24 hours |
| Low | Newsletters, notifications, FYI | Weekly review or skip | When convenient |

Create `scripts/email-triage.py` that:
1. Pulls unread emails (via Gmail API)
2. Classifies by priority using AI
3. Generates a digest: urgent items first, then important, then summary of rest
4. Saves to `outputs/inbox-digest-[YYYY-MM-DD].md`

**VIP list:**
Define in `data/vip-contacts.json`:
```json
[
  {"email": "client@example.com", "name": "Important Client", "priority": "urgent"},
  {"email": "investor@fund.com", "name": "Investor", "priority": "urgent"},
  {"email": "partner@company.com", "name": "Key Partner", "priority": "important"}
]
```

### 6. Set up habit tracking (optional)

If the user wants to track personal habits alongside business metrics:

Create a simple tracker in `data/habits/`:
```json
{
  "date": "2026-03-04",
  "habits": {
    "exercise": true,
    "reading": true,
    "meditation": false,
    "journaling": true,
    "no_phone_first_hour": false
  },
  "streaks": {
    "exercise": 12,
    "reading": 5,
    "meditation": 0,
    "journaling": 3,
    "no_phone_first_hour": 0
  }
}
```

Include habit streaks in the Daily Brief and evening review.

### 7. Set up automation (cron / scheduled runs)

**Daily automation schedule:**
```
06:00 — Fetch health data (if connected)
06:30 — Pull all metrics (revenue, pipeline, email)
07:00 — Generate and display Daily Brief
12:00 — Midday check-in prompt (optional)
18:00 — Evening review prompt
23:00 — Log day's data, prep tomorrow
```

**Implementation options:**
- **cron**: Simple scheduled execution (`crontab -e`)
- **launchd**: macOS native scheduler (plist files)
- **n8n**: Visual workflow automation
- **Command Center**: Telegram-triggered on-demand

For most users, on-demand via `/brief` and `/checkin` commands is sufficient to start. Add cron later when the habit is established.

### 8. Test the system

1. [ ] Daily Brief generates with available data sources
2. [ ] Check-in prompts appear at correct times (or on-demand)
3. [ ] KPI tracking correctly pulls from connected sources
4. [ ] Email triage classifies messages accurately
5. [ ] Data saves correctly to `data/` directory
6. [ ] Weekly review generates with trends and insights
7. [ ] Missing data sources show "Not configured" (not errors)

## Script
- `scripts/daily-brief.py` — Morning briefing generator
- `scripts/checkin.py` — Productivity check-in system
- `scripts/fetch-metrics.py` — KPI aggregation
- `scripts/email-triage.py` — Inbox management

## Output
- `outputs/briefs/brief-[YYYY-MM-DD].md` — Daily briefings
- `outputs/reviews/weekly-[YYYY-WXX].md` — Weekly reviews
- `outputs/inbox-digest-[YYYY-MM-DD].md` — Email digests
- `data/checkins/` — Check-in logs
- `data/kpis.json` — KPI targets and actuals
- `data/habits/` — Habit tracking data

## Requirements
- At least one data source connected (Stripe, Google, Slack, etc.)
- `ANTHROPIC_API_KEY` in `.env` (for AI-powered summaries and classification)
- Python 3, `requests` library
- OAuth credentials for Google (Gmail + Calendar) if using those modules

## Edge Cases
- **No data sources connected**: Generate a brief with just tasks and calendar. Add data sources over time.
- **Stripe in test mode**: Make sure to use the live key, not test key. Test keys return test data only.
- **Gmail OAuth token expires**: Tokens refresh automatically, but if `credentials.json` is missing, re-run OAuth flow.
- **Health data not syncing**: Check API token expiry. Oura tokens expire every 30 days.
- **Too much inbox noise**: Tighten the priority rules. Add more contacts to the "low priority" auto-skip list.
- **User stops doing check-ins**: Don't nag. Make check-ins valuable by showing streaks and progress. If they skip 3 days, ask once if they want to adjust the cadence.

## Notes
- Start with the Daily Brief only. Add check-ins and KPIs after the daily habit is established.
- The brief should take 2 minutes to read. If it's longer, cut sections.
- Best time for morning brief: 30 minutes before the user typically starts work.
- Evening reviews are the highest-ROI habit. Reflection compounds into better decision-making.
- The goal is awareness, not micromanagement. Track the metrics that actually drive the business forward.
- After each week, update this file with what data sources are most useful and which sections get skipped.
