# AIDE — AI Digital Employee

Set up an AI employee in minutes. Give it context about you and your business, teach it your workflows, and let it do the work.

---

## How It Works

AIDE is a workspace template for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). It turns Claude into a digital employee by giving it:

1. **Context** — Who you are, what your business does, your current goals
2. **Instructions** — Step-by-step task guides it can follow
3. **Scripts** — Code it can run to pull data, automate tasks, etc.
4. **Outputs** — A place to save finished work

```
context/       →  instructions/  →  scripts/   →  outputs/
(who you are)     (what to do)      (how)         (results)
```

When something breaks, AIDE doesn't just fail — it learns:

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
git clone https://github.com/YOUR_USERNAME/aide-workspace.git
cd aide-workspace
```

Open the folder in VS Code or Antigravity.

### 2. Add your API key

Get a free NewsAPI key at [newsapi.org/register](https://newsapi.org/register) (takes 30 seconds), then add it to your `.env` file:

```
NEWS_API_KEY=your_key_here
```

### 3. Fill in your context

These files are your AI employee's onboarding. The more you fill in, the better it works.

**`context/business.md`** — Your company or project
- Name, what you do, products/services, audience, tech stack

**`context/personal.md`** — You
- Your name, role, communication style, what you use this for

**`context/strategy.md`** — What matters now
- Top priority, current goals, key metrics, what's NOT a priority

**`context/data.md`** — Current numbers (optional)
- Latest metrics, data sources

> Not sure what to write? Check `context/_examples.md` for three filled-in examples (content agency, student, consulting firm).

### 4. Start working

1. Open the terminal in VS Code
2. Start Claude Code
3. Type `/project:prime` to load your context
4. Ask Claude to do something — follow an instruction, create a plan, or just chat

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
/project:prime
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
aide-workspace/
├── .claude/
│   ├── settings.json          # Permissions (safe mode)
│   └── commands/
│       ├── prime.md           # /project:prime — load context
│       ├── create-plan.md     # /project:create-plan — plan a task
│       └── implement.md       # /project:implement — execute a plan
│
├── CLAUDE.md                  # AI behavior rules
│
├── context/                   # Your AI employee's onboarding
│   ├── business.md            # Your company / project
│   ├── personal.md            # Your role & preferences
│   ├── strategy.md            # Current goals & priorities
│   ├── data.md                # Current metrics (optional)
│   └── _examples.md           # 3 filled-in examples to learn from
│
├── instructions/              # Task guides and plans
│   ├── _template.md           # Template for new instructions
│   └── _example-*.md          # 7 example instructions (news, blogs, reports...)
│
├── scripts/                   # Code that does the work
│   └── fetch-news.py          # Fetch latest news from NewsAPI
│
└── outputs/                   # Generated content goes here
```

---

## Commands

| Command | What It Does |
|---------|-------------|
| `/project:prime` | Loads your context so Claude knows who you are. Run at the start of every session. |
| `/project:create-plan` | Creates a step-by-step plan for a task. Saves it to `instructions/`. |
| `/project:implement` | Executes the most recent plan, self-correcting when things break. |

---

## Examples

Examples are built into the workspace — no setup needed:

- **`context/_examples.md`** — Three filled-in context examples showing how to fill in your own files
- **`instructions/_example-*.md`** — Seven example instructions:

| File | Use Case |
|------|----------|
| `_example-news-to-content.md` | Fetch news and turn it into social content |
| `_example-write-blog-post.md` | SEO blog writing |
| `_example-repurpose-content.md` | Multi-platform content repurposing |
| `_example-research-paper.md` | Academic paper writing |
| `_example-study-guide.md` | Exam study guides |
| `_example-weekly-report.md` | Weekly status reports |
| `_example-competitor-analysis.md` | Competitor research |

---

## Creating Your Own Instructions

1. Copy `instructions/_template.md`
2. Fill in the sections (Goal, Inputs, Steps, Output, etc.)
3. Save it in `instructions/`

Or use `/project:create-plan` to have Claude design a new workflow for you.

---

## Troubleshooting

**"claude: command not found"** — Make sure the Claude Code extension is installed. Restart your terminal.

**Context not loading on `/project:prime`** — Make sure your context files are saved and not still placeholder templates.

**"NEWS_API_KEY not found"** — Open `.env` and add your key. Get one free at [newsapi.org/register](https://newsapi.org/register).

**Script errors** — Make sure you have Python 3 installed: `python3 --version`. No pip installs needed — the script uses standard library only.

