# AI Systems - Module Registry

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
| 8 | Command Center | Not configured | `apps/command/` | -- | Telegram bot — AI Systems on your phone |
| | | | | | |
| | **Business Modules** | | | | |
| 9 | Prospecting | Not configured | -- | `/install prospecting` | Lead scraping, enrichment, cold email, reply classification |
| 10 | Content Pipeline | Not configured | -- | `/install content` | Topic research, scripts, social repurposing, publishing |
| 11 | Paid Ads | Not configured | -- | `/install ads` | Ad monitoring, alerts, optimization recommendations |
| 12 | Image Generation | Not configured | -- | `/install images` | AI image generation for brand assets and thumbnails |
| 13 | Video Creation | Not configured | -- | `/install video` | AI voice, avatar, auto-editing, clip extraction |
| 14 | Partnerships | Not configured | -- | `/install partners` | Referral tracking, testimonials, partner program |
| 15 | Operations | Not configured | -- | `/install ops` | Daily briefs, KPIs, inbox management, habits |

**Status options:** `Active` | `Configured` | `Not configured`

**Install any module:** `/install <module-name>` — the AI handles everything.

## Data Sources

| Source | Status | Auth Method | Used By |
|--------|--------|-------------|---------|
| Google (Gmail + Calendar) | Not configured | Composio OAuth OR `credentials.json` | Email Capture, Meeting Intel, Daily Brief |
| Slack | Not configured | Composio OAuth OR `SLACK_BOT_TOKEN` | Slack Intelligence module |
| Stripe | Not configured | `STRIPE_SECRET_KEY` (direct) | Revenue in Daily Brief |
| Telegram | Not configured | `COMMAND_CENTER_BOT_TOKEN` (direct) | Command Center module |
| Your CRM | Not configured | _(varies)_ | Pipeline in Daily Brief |
| Health Tracker | Not configured | _(varies)_ | Health in Daily Brief |

## Tool Connections

Two ways to connect external tools:

**Option A: Composio (recommended)**
Set `COMPOSIO_API_KEY` in `.env`, then run `/connect` or `python scripts/connections.py connect <provider>`.
One-click OAuth — no Google Cloud Console, no Slack app creation needed.

**Option B: Direct API keys**
Follow setup instructions in each script file. More control, more setup steps.

Scripts automatically detect which method is available (Composio first, direct fallback).

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

1. [ ] Run `/setup` — fill in context files (business, personal, strategy)
2. [ ] Run `/init` — verify context loads
3. [ ] Run `/connect` — link Google + Slack via Composio
4. [ ] Run `/status` — see what's available
5. [ ] Run `/install <module>` — install modules one at a time
6. [ ] This file updates automatically as you install modules
