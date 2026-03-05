# AI Systems

Your personal AI workspace. Context, instructions, scripts, outputs - everything your AI needs to do real work.

You are an AI system working in a structured workspace. Think of this like your first day at a job - read your onboarding docs, understand your role, then get to work.

## How This Workspace Works

```
context/       →  instructions/  →  scripts/   →  outputs/
(who you are)     (what to do)      (how)         (results)
```

1. **Context** (`context/`) - Your onboarding. Who the user is, their business, goals, and current data.
2. **Instructions** (`instructions/`) - Task guides, plans, reference docs. Everything you need to do the work.
3. **Scripts** (`scripts/`) - Code that does the actual work. Python, Node, shell - whatever fits.
4. **Outputs** (`outputs/`) - Where finished work goes. Reports, docs, presentations, data.

## Your Rules

### Rule 1: Load context first
At the start of every session, read the context files. If the user runs `/context`, follow that command. Otherwise, read `context/` before doing anything else.

### Rule 2: Check before you create
Before writing new code, check `scripts/` for existing scripts and `instructions/` for existing guides. Only create new files when nothing fits.

### Rule 3: Self-correct when things break
When code fails:
1. Read the error message
2. Fix the code
3. Test it again (ask first if it uses paid API credits)
4. Update the instruction file with what you learned

Every failure makes the system smarter.

### Rule 4: Keep instructions updated
When you discover something new - API limits, edge cases, better approaches - update the relevant instruction. They're living documents.

### Rule 5: Save outputs properly
Generated content goes to `outputs/`. Plans go to `instructions/`. Never leave important work in temporary locations.

### Rule 6: Track tasks and lessons
Keep `context/todo.md` updated with current tasks. When something breaks and you fix it, add the pattern to `context/lessons.md` so the same mistake never happens twice.

## Folder Map

| Folder | Purpose |
|--------|---------|
| `context/` | Business info, your role, strategy, tasks (`todo.md`), patterns (`lessons.md`) |
| `instructions/` | Task guides, plans, reference docs, SOPs (see `_example-*.md` files for reference) |
| `scripts/` | Code - executions, utilities, data fetchers |
| `outputs/` | Generated work - reports, docs, presentations |

## Self-Correction Loop

```
Error → Read error → Fix code → Test → Update instruction → System improved
```

This is what makes the system get smarter over time. Every fix gets documented so the same mistake never happens twice.

## Key Principles

- **Ask before spending money.** Confirm before running paid APIs.
- **One script, one job.** Keep scripts focused and reusable.
- **Local first.** Save to `outputs/` unless told otherwise.
- **Check the skills library.** Before writing custom code, check: https://github.com/anthropics/skills

## Base Modules (Built In)

These come with the template. Install them one at a time with `/install <name>`.

| # | Module | Command | What It Does |
|---|--------|---------|-------------|
| 1 | Context OS | `/context` | Loads business context each session (built in) |
| 2 | Daily Brief | `/brief` | Morning briefing: revenue, pipeline, health, tasks |
| 3 | Data Dashboard | -- | Aggregates metrics from all integrations |
| 4 | Productivity | `/checkin` | Goal tracking, habit logging, day review |
| 5 | Slack Intelligence | -- | Channel summaries, action item extraction |
| 6 | Meeting Intelligence | -- | Google Meet transcript search, meeting digest |
| 7 | Email Capture | -- | Gmail inbox digest, categorized by urgency |
| 8 | Command Center | -- | Telegram bot - AI system on your phone |

**Start here:** Context OS is built in. Run `/setup` to fill your context files, then `/context` at the start of every session.

## The 6 Systems (Coaching Program)

Business automation systems available to coaching clients. Each system adds instruction files and scripts to your workspace.

| # | System | What It Does |
|---|--------|-------------|
| 1 | The Prospecting System | Lead scraping, email enrichment, cold email campaigns |
| 2 | The Content System | Content research, script generation, social publishing |
| 3 | The Acquisition System | Ad monitoring, funnel tracking, optimization |
| 4 | The Partners System | Referral tracking, testimonials, partner management |
| 5 | The Operations System | Daily briefs, dashboards, Telegram commands |
| 6 | The Data System | Market research, competitor tracking, analytics |

Get access: skalers.io → Coaching Program. Install only what you need.

## Commands

- `/setup` - First-time setup: asks you questions, fills in all context files automatically
- `/context` - Load context and orient yourself for the session (run at start of every session)
- `/status` - See all modules, what's installed, what's available, and how to install each one
- `/install <module>` - Install any module: handles API keys, scripts, testing, and registry update
- `/connect` - Connect external tools (Gmail, Calendar, Slack) via Composio or manual API
- `/brief` - Run your daily brief (requires daily-brief module setup)
- `/checkin` - Run a productivity check-in
