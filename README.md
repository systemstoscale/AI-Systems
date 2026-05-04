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

---

## Quick Start

### Prerequisites

- **Node.js 18+** - [Download](https://nodejs.org)
- **Python 3** - For running scripts (already installed on most machines)
- **VS Code** with [Claude Code extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code), or [Google Antigravity](https://antigravity.google) (free tier available)

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

### 3. Start working

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
│   ├── settings.json          # Permissions
│   ├── commands/
│   │   ├── setup.md           # /setup - interactive first-time setup
│   │   └── context.md         # /context - load context each session
│   └── skills/                # Reusable workflows
│       ├── social-media-analysis/
│       │   └── SKILL.md       # Analyze social media profiles
│       └── weekly-report/
│           └── SKILL.md       # Generate weekly business report
│
├── CLAUDE.md                  # AI behavior rules
│
├── context/                   # Your AI system's onboarding
│   ├── business.md            # Your company / project
│   ├── personal.md            # Your role & preferences
│   └── strategy.md            # Current goals & priorities
│
└── outputs/                   # Generated content goes here
```

---

## Commands

| Command | What It Does |
|---------|-------------|
| `/setup` | First-time setup. Asks you questions, fills in all your context files automatically. |
| `/context` | Loads your context so Claude knows who you are. Run at the start of every session. |

---

## Creating Your Own Skills

1. Create a new folder in `.claude/skills/` named after your workflow (e.g. `lead-enrichment`)
2. Create a `SKILL.md` file inside it with four sections: **Goal**, **Inputs**, **Steps**, **Output**
3. Or just describe what you want to Claude — it will design the workflow and create the skill file for you

Any repeatable task should become a skill. Weekly reports. Lead enrichment. Competitor research. Client onboarding. Each one becomes a one-command workflow you never have to re-explain.

---

## Troubleshooting

**"claude: command not found"** - Make sure the Claude Code extension is installed. Restart your terminal.

**Context not loading on `/context`** - Make sure your context files are saved and not still placeholder templates.

**"SCRAPECREATORS_API_KEY not set"** - Open `.env` and add your key. Get one free at [scrapecreators.com](https://scrapecreators.com).

**Script errors** - Make sure you have Python 3 installed: `python3 --version`. No pip installs needed - the script uses standard library only.
