# AI Employee

Set up an AI employee in minutes. Give it context about you and your business, teach it your workflows, and let it do the work.

---

## How It Works

AI Employee is a workspace template for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). It turns Claude into an AI employee by giving it:

1. **Context** — Who you are, what your business does, your current goals
2. **Instructions** — Step-by-step task guides it can follow
3. **Scripts** — Code it can run to pull data, automate tasks, etc.
4. **Outputs** — A place to save finished work

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

- **Node.js 18+** — [Download](https://nodejs.org)
- **Python 3** — For running scripts (already installed on most machines)
- **VS Code** with [Claude Code extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code), or [Antigravity](https://antigravity.devcycle.cc)

### 1. Clone and open

```bash
git clone https://github.com/systemstoscale/AI-Employee.git
cd AI-Employee
```

Open the folder in VS Code or Antigravity.

### 2. Add your API key

Get a free NewsAPI key at [newsapi.org/register](https://newsapi.org/register) (takes 30 seconds), then add it to your `.env` file:

```
NEWS_API_KEY=your_key_here
```

### 3. Run the setup

Start Claude Code, then run the interactive setup — it asks you questions and fills in all your context files automatically:

```
/setup
```

Claude will ask about your business, your role, your goals, and your current metrics. Answer the questions and it writes everything for you. Takes about 5 minutes.

> Want to fill in the files manually instead? Check `context/_examples.md` for three filled-in examples to use as a guide.

### 4. Start working

After setup, every new session just needs:
```
/init
```

This loads your context so Claude knows who you are. Then ask it to do something — follow an instruction, create a plan, or just chat.

---

## Try It — Live Demo

Once you have your API key set up, try the full pipeline:

**Step 1:** Fetch the latest AI news
```bash
python3 scripts/fetch-news.py
```
This pulls 10 articles from NewsAPI and saves them to `outputs/latest-news.md`.

**Step 2:** Start Claude Code and prime it
```
/init
```

**Step 3:** Ask Claude to create content from the news
```
Follow the news-to-content instruction using the news you just fetched.
```

Claude will read the news, pick the best stories, and generate LinkedIn posts, tweets, and a newsletter snippet — all in your brand voice.

You can customize the topic too:
```bash
python3 scripts/fetch-news.py "climate tech"
python3 scripts/fetch-news.py "startup funding"
python3 scripts/fetch-news.py "remote work"
```

---

## What's In the Box

```
AI-Employee/
├── .claude/
│   ├── settings.json          # Permissions (safe mode)
│   └── commands/
│       ├── setup.md           # /setup — interactive first-time setup
│       ├── init.md            # /init — load context
│       ├── create-plan.md     # /create-plan — plan a task
│       ├── implement.md       # /implement — execute a plan
│       ├── brief.md           # /brief — daily briefing
│       └── checkin.md         # /checkin — productivity check-in
│
├── CLAUDE.md                  # AI behavior rules
│
├── context/                   # Your AI employee's onboarding
│   ├── business.md            # Your company / project
│   ├── personal.md            # Your role & preferences
│   ├── strategy.md            # Current goals & priorities
│   ├── data.md                # Current metrics (optional)
│   ├── ai-employee.md         # Module registry (track active modules)
│   └── _examples.md           # 3 filled-in examples to learn from
│
├── instructions/              # Task guides and plans
│   ├── _template.md           # Template for new instructions
│   └── _example-*.md          # 10 example instructions
│
├── scripts/                   # Code that does the work
│   ├── fetch-news.py          # Fetch latest news from NewsAPI
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
| `/init` | Loads your context so Claude knows who you are. Run at the start of every session. |
| `/create-plan` | Creates a step-by-step plan for a task. Saves it to `instructions/`. |
| `/implement` | Executes the most recent plan, self-correcting when things break. |
| `/brief` | Generates your daily briefing (revenue, pipeline, health, tasks). |
| `/checkin` | Runs a productivity check-in based on time of day. |

---

## AI Employee Modules

Beyond context stacking, the workspace supports automation modules. Each adds a capability you can activate independently.

| # | Module | Script | What It Does |
|---|--------|--------|-------------|
| 1 | Context OS | -- | Loads business context each session (`/init`) |
| 2 | Daily Brief | `daily-brief.py` | Morning briefing: revenue, pipeline, health, tasks |
| 3 | Data Dashboard | `fetch-metrics.py` | Aggregates metrics from your integrations |
| 4 | Productivity | -- | Goal tracking, habit logging, day review (`/checkin`) |
| 5 | Slack Intelligence | `slack-intel.py` | Channel summaries, action item extraction |
| 6 | Meeting Intelligence | `meeting-intel.py` | Google Meet transcript search, meeting digest |
| 7 | Email Capture | `email-capture.py` | Gmail inbox digest, categorized by urgency |
| 8 | Mobile Access | -- | Telegram bot for commands on the go |

**Start with Context OS** (already built in). Then add Daily Brief (just needs a Stripe key). Layer on more modules as you need them. Each module is a standalone script in `scripts/` — nothing breaks if you skip one.

Track which modules you've activated in `context/ai-employee.md`.

---

## Examples

Examples are built into the workspace — no setup needed:

- **`context/_examples.md`** — Three filled-in context examples showing how to fill in your own files
- **`instructions/_example-*.md`** — Ten example instructions:

| File | Use Case |
|------|----------|
| `_example-news-to-content.md` | Fetch news and turn it into social content |
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

Or use `/create-plan` to have Claude design a new workflow for you.

---

## Troubleshooting

**"claude: command not found"** — Make sure the Claude Code extension is installed. Restart your terminal.

**Context not loading on `/init`** — Make sure your context files are saved and not still placeholder templates.

**"NEWS_API_KEY not found"** — Open `.env` and add your key. Get one free at [newsapi.org/register](https://newsapi.org/register).

**Script errors** — Make sure you have Python 3 installed: `python3 --version`. No pip installs needed — the script uses standard library only.

