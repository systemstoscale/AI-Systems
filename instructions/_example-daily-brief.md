# Instruction: Daily Brief

## Goal
Generate a morning briefing that covers revenue, pipeline, tasks, meetings, and health metrics — all in one view.

## Script
`scripts/daily-brief.py`

## Command
`/brief`

## When to Run
Every morning at the start of work. Can also be automated via cron job or Railway to send to Slack/Telegram.

## Steps
1. Run `python scripts/daily-brief.py`
2. Review the output for accuracy
3. If data sources are missing, check `.env` for API keys
4. Use the brief to decide your top priorities for the day

## Sections

### Revenue (Stripe)
- MRR (Monthly Recurring Revenue)
- Active subscription count
- Last 24h revenue and transaction count
- 7-day revenue trend

### Pipeline (Email Outreach)
- Active campaigns
- Emails sent, open rate, reply rate
- Top campaigns by reply rate
- Requires integration with your email outreach tool (Instantly, Lemlist, etc.)

### Tasks
- Todo / In Progress / Blocked counts
- Overdue items (highlighted)
- Due today items
- Urgent items

### Health (Optional)
- Sleep score, readiness score (OURA)
- Recovery, strain (WHOOP)
- HRV, resting heart rate
- Steps, active calories

### Meetings (Optional)
- Today's scheduled meetings from Google Calendar
- Number of attendees per meeting
- Requires Google OAuth setup

### Inbox (Optional)
- Unread email count
- Emails requiring action vs FYI vs marketing
- Requires Google OAuth setup (Gmail)

## Configuration

### Required
Set in `.env`:
- `STRIPE_SECRET_KEY` — For revenue data

### Optional
- `SLACK_BOT_TOKEN` + `SLACK_CHANNEL_ID` — Post brief to Slack
- `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` — Post brief to Telegram
- Google OAuth `credentials.json` — For Calendar + Gmail data

## Output Formats
- **Terminal**: Formatted markdown (default)
- **Slack**: Block Kit formatted message
- **Telegram**: HTML formatted message

## Customization
Edit `scripts/daily-brief.py` to:
- Add/remove sections based on your data sources
- Change formatting (markdown, HTML, Slack blocks)
- Add custom data sources (CRM, project management, etc.)
- Set up automated delivery via cron

## Automation
To send the brief automatically every morning:
1. Deploy to Railway, Render, or any cron-capable host
2. Set cron schedule: `0 7 * * *` (daily at 7 AM)
3. Configure Slack and/or Telegram tokens for delivery
