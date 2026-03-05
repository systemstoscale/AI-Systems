# AI Systems

Set up an AI system in minutes. Give it context about you and your business, teach it your workflows, and let it do the work.

---

## How It Works

AI Systems is a workspace template for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). It turns Claude into an AI system by giving it:

1. **Context** - Who you are, what your business does, your current goals
2. **Instructions** - Step-by-step task guides it can follow
3. **Scripts** - Code it can run to pull data, automate tasks, etc.
4. **Outputs** - A place to save finished work

```
context/       →  instructions/  →  scripts/   →  outputs/
(who you are)     (what to do)      (how)         (results)
```

When something breaks, it doesn't just fail. It learns:

```
Error → Read error → Fix code → Test → Update instruction → System improved
```

Every failure makes the system smarter. Fixes get documented so the same mistake never happens twice.

---

## Quick Start

### Prerequisites

- **Node.js 18+** - [Download](https://nodejs.org)
- **Python 3** - For running scripts (already installed on most machines)
- **VS Code** with [Claude Code extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code), or [Google Antigravity](https://antigravity.google) (free tier available, AI built in)

### 1. Clone and open

```bash
git clone https://github.com/systemstoscale/AI-Systems.git
cd AI-Systems
```

Open the folder in VS Code or Antigravity.

### 2. Run the setup

Start Claude Code, then run the interactive setup - it asks you questions and fills in all your context files automatically:

```
/setup
```

Takes about 5 minutes. Answer the questions and it writes everything for you.

> Want to fill in the files manually instead? Check `context/_examples.md` for three filled-in examples.

### 3. See what's available

```
/status
```

Shows all 15 modules, what's installed, what's missing, and the exact command to install each one.

### 4. Install modules

```
/install daily-brief
/install prospecting
/install command-center
```

One command per module. The AI handles everything - checks prerequisites, asks for API keys (with links to get them), creates scripts, tests, and updates the registry. You just paste keys when asked.

### 5. Start working

Every new session:
```
/context
```

This loads your context so Claude knows who you are. Then ask it to do something - follow an instruction, create a plan, or just chat.

---

## Try It - Live Demo

Once you have your API key set up, try the full pipeline:

**Step 1:** Load your context
```
/context
```

**Step 2:** Ask Claude to fetch your social media data
```
Scrape my YouTube and Instagram profiles using ScrapeCreators. My handle is yourhandle.
```

**Step 3:** Ask Claude to analyze your social presence
```
Analyze the social media data you just pulled and create a growth strategy with actionable recommendations.
```

Claude will read your social data, analyze your reach, engagement, and content, then generate a report saved to `outputs/`.

---

## What's In the Box

```
AI-Systems/
├── .claude/
│   ├── settings.json          # Permissions (safe mode)
│   └── commands/
│       ├── setup.md           # /setup - interactive first-time setup
│       ├── context.md         # /context - load context each session
│       ├── brief.md           # /brief - daily briefing
│       └── checkin.md         # /checkin - productivity check-in
│
├── CLAUDE.md                  # AI behavior rules
│
├── context/                   # Your AI system's onboarding
│   ├── business.md            # Your company / project
│   ├── personal.md            # Your role & preferences
│   ├── strategy.md            # Current goals & priorities
│   ├── data.md                # Current metrics (optional)
│   ├── todo.md                # Running task list
│   ├── lessons.md             # Patterns learned from mistakes
│   └── ai-systems.md         # Module registry (track active modules)
│
├── instructions/              # Task guides and plans
│   ├── _template.md           # Template for new instructions
│   └── _example-*.md          # 10 example instructions
│
├── scripts/                   # Code that does the work
│   ├── fetch-social.py        # Fetch social media profiles (ScrapeCreators)
│   ├── daily-brief.py         # Morning briefing (Stripe + custom)
│   ├── fetch-metrics.py       # Metrics aggregation layer
│   ├── meeting-intel.py       # Google Meet transcript search
│   ├── email-capture.py       # Gmail inbox digest
│   ├── slack-intel.py         # Slack channel summaries
│   └── fetch-social-profiles.py  # Social media data
│
└── outputs/                   # Generated content goes here
```

---

## Commands

| Command | What It Does |
|---------|-------------|
| `/setup` | First-time setup. Asks you questions, fills in all your context files automatically. |
| `/context` | Loads your context so Claude knows who you are. Run at the start of every session. |
| `/status` | Shows all modules, what's installed, what's missing, and how to install each one. |
| `/install <module>` | Installs any module. Handles API keys, scripts, testing, and registry. |
| `/connect` | Connect external tools (Gmail, Calendar, Slack) via Composio or manual API. |
| `/brief` | Generates your daily briefing (revenue, pipeline, health, tasks). |
| `/checkin` | Runs a productivity check-in based on time of day. |

---

## AI Systems Modules

Every module installs with one command: `/install <module-name>`. Each is independent - nothing breaks if you skip one.

### Core Modules

| # | Module | Install | What It Does |
|---|--------|---------|-------------|
| 1 | Context OS | _(built in)_ | Loads your business context each session (`/context`) |
| 2 | Daily Brief | `/install daily-brief` | Morning briefing: revenue, pipeline, health, tasks |
| 3 | Data Dashboard | `/install data-dashboard` | Aggregates metrics from your integrations |
| 4 | Productivity | `/install productivity` | Goal tracking, habit logging, day review (`/checkin`) |
| 5 | Slack Intelligence | `/install slack-intel` | Channel summaries, action item extraction |
| 6 | Meeting Intelligence | `/install meeting-intel` | Google Meet transcript search, meeting digest |
| 7 | Email Capture | `/install email-capture` | Gmail inbox digest, categorized by urgency |
| 8 | Command Center | `/install command-center` | Telegram bot - AI Systems on your phone |

### Business Modules

| # | Module | Install | What It Does |
|---|--------|---------|-------------|
| 9 | Prospecting | `/install prospecting` | Lead scraping, enrichment, cold email, reply classification |
| 10 | Content Pipeline | `/install content` | Topic research, scripts, social repurposing, publishing |
| 11 | Paid Ads | `/install ads` | Ad monitoring, alerts, optimization recommendations |
| 12 | Image Generation | `/install images` | AI image generation for brand assets and thumbnails |
| 13 | Video Creation | `/install video` | AI voice, avatar, auto-editing, clip extraction |
| 14 | Partnerships | `/install partners` | Referral tracking, testimonials, partner program |
| 15 | Operations | `/install ops` | Daily briefs, KPIs, inbox management, habits |

**Start with Context OS** (already built in). Run `/status` to see what's available, then install one module at a time.

Track which modules you've activated in `context/ai-systems.md`.

---

## Examples

Examples are built into the workspace - no setup needed:

- **`instructions/_example-*.md`** - Example instructions:

| File | Use Case |
|------|----------|
| `_example-social-media-analysis.md` | Analyze your social presence and create a growth strategy |
| `_example-write-blog-post.md` | SEO blog writing |
| `_example-repurpose-content.md` | Multi-platform content repurposing |
| `_example-research-paper.md` | Academic paper writing |
| `_example-study-guide.md` | Exam study guides |
| `_example-weekly-report.md` | Weekly status reports |
| `_example-competitor-analysis.md` | Competitor research |
| `_example-daily-brief.md` | Daily briefing module setup |
| `_example-data-dashboard.md` | Metrics aggregation setup |
| `_example-checkin.md` | Productivity check-in setup |

---

## Creating Your Own Instructions

1. Copy `instructions/_template.md`
2. Fill in the sections (Goal, Inputs, Steps, Output, etc.)
3. Save it in `instructions/`

Or just describe what you want to Claude - it will design the workflow and create the instruction file for you.

---

## Troubleshooting

**"claude: command not found"** - Make sure the Claude Code extension is installed. Restart your terminal.

**Context not loading on `/context`** - Make sure your context files are saved and not still placeholder templates.

**"SCRAPECREATORS_API_KEY not set"** - Open `.env` and add your key. Get one free at [scrapecreators.com](https://scrapecreators.com).

**Script errors** - Make sure you have Python 3 installed: `python3 --version`. No pip installs needed - the script uses standard library only.

