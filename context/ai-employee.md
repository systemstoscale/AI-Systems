# AI Employee - Module Registry

*Track which modules are active and how they're configured.*

## Modules

| # | Module | Status | Script | Command | Description |
|---|--------|--------|--------|---------|-------------|
| 1 | Context OS | Active | -- | `/init` | Loads business context each session |
| 2 | Daily Brief | Not configured | `scripts/daily-brief.py` | `/brief` | Morning briefing: revenue, pipeline, health, tasks |
| 3 | Data Dashboard | Not configured | `scripts/fetch-metrics.py` | -- | Aggregates metrics from all integrations |
| 4 | Productivity | Not configured | -- | `/checkin` | Goal tracking, habit logging, day review |
| 5 | Slack Intelligence | Not configured | `scripts/slack-intel.py` | -- | Channel summaries, action item extraction |
| 6 | Meeting Intelligence | Not configured | `scripts/meeting-intel.py` | -- | Google Meet transcript search, meeting digest |
| 7 | Email Capture | Not configured | `scripts/email-capture.py` | -- | Gmail inbox digest, categorized by urgency |
| 8 | Mobile Access | Not configured | -- | -- | Telegram bot for commands on the go |

**Status options:** `Active` | `Configured` | `Not configured`

## Data Sources

| Source | Status | Env Var | Used By |
|--------|--------|---------|---------|
| Stripe | Not configured | `STRIPE_SECRET_KEY` | Revenue in Daily Brief |
| Google Calendar | Not configured | `credentials.json` (OAuth) | Meetings in Daily Brief |
| Gmail | Not configured | `credentials.json` (OAuth) | Email Capture module |
| Slack | Not configured | `SLACK_BOT_TOKEN` | Slack Intelligence module |
| Telegram | Not configured | `TELEGRAM_BOT_TOKEN` | Mobile Access module |
| Your CRM | Not configured | _(varies)_ | Pipeline in Daily Brief |
| Health Tracker | Not configured | _(varies)_ | Health in Daily Brief |

## How Modules Connect

```
                    ┌──────────────┐
                    │  Daily Brief │  ← The main output
                    └──────┬───────┘
                           │ pulls from
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
     ┌──────────┐   ┌──────────┐   ┌──────────┐
     │   Data   │   │  Email   │   │ Meeting  │
     │Dashboard │   │ Capture  │   │  Intel   │
     └──────────┘   └──────────┘   └──────────┘
            │
     ┌──────┼──────┐
     ▼      ▼      ▼
  Stripe  CRM   Health
```

Modules are independent. If a data source is missing, that section just shows "Not configured" instead of breaking. Add modules one at a time.

## Setup Checklist

1. [ ] Fill in `context/` files (business, personal, strategy)
2. [ ] Run `/init` to verify context loads
3. [ ] Add `STRIPE_SECRET_KEY` to `.env` (for revenue data)
4. [ ] Run `python scripts/daily-brief.py` to test
5. [ ] Set up Google OAuth for Calendar + Gmail (optional)
6. [ ] Create a Telegram bot via @BotFather (optional)
7. [ ] Create a Slack app with bot token (optional)
8. [ ] Update this file as you activate modules
