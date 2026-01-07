# IDEA Framework
**Instructions, Decisions, Executions, AI**

A simple framework for building reliable AI-powered automation.

---

## The Problem

AI is smart but inconsistent. If AI is 90% accurate per step, after 5 steps you're down to 59% success.

## The Solution

Let AI focus on **decisions** while reliable code handles **execution**.

```
instructions/     →     AI     →     executions/
 (what to do)       (decides)      (does the work)
```

---

## How It Works

| Folder | What It Contains |
|--------|------------------|
| `instructions/` | Markdown files explaining tasks |
| `executions/` | Python code that does the actual work |
| `temp/` | Temporary files (safe to delete) |

**The AI sits in the middle** - it reads your instructions, makes decisions, and runs the right code.

**Example:**
1. You say: "Scrape this website"
2. AI reads `instructions/scrape_website.md`
3. AI runs `executions/scrape.py`
4. If something breaks, AI fixes it and updates the instruction

---

## Quick Start

### Prerequisites

- **Node.js 18+** - [Download here](https://nodejs.org)
- **Antigravity** or **VS Code with Claude Code extension**
  - Antigravity: https://antigravity.devcycle.cc
  - VS Code: Search "Claude Code" in Extensions

### Setup

```bash
# Clone this repo
git clone https://github.com/YOUR_USERNAME/TheIDEAFramework.git
cd TheIDEAFramework

# Run the setup script
./setup.sh

# Fill in your API keys
nano .env

# Open in your editor and start Claude Code
```

---

## Project Structure

After running `setup.sh`, you get:

```
TheIDEAFramework/
├── .claude/settings.json  → Claude Code permissions
├── .env                   → Your API keys (never commit)
├── .gitignore             → Protects secrets
├── temp/                  → Scratch space
├── CLAUDE.md              → AI behavior rules
├── instructions/          → What to do
│   └── _template.md       → Template for new instructions
└── executions/            → How to do it
    └── _example.py        → Sample script
```

---

## The Self-Correction Loop

This is what makes the system get smarter over time:

```
1. Code fails
      ↓
2. AI reads error
      ↓
3. AI fixes code
      ↓
4. AI tests again
      ↓
5. AI updates instruction with what it learned
      ↓
6. System is now smarter
```

Every failure improves the system.

---

## Claude Skills Library

Before writing custom code, check if a community skill already exists.

**Browse skills:** https://github.com/travisvn/awesome-claude-skills

| Category | Skills |
|----------|--------|
| Documents | docx, pdf, pptx, xlsx |
| Creative | canvas-design, algorithmic-art |
| Development | artifacts-builder, webapp-testing |
| Data | CSV summarizer, D3.js, postgres |

---

## Creating Instructions

Use the template in `instructions/_template.md`:

```markdown
# Instruction: Download Images

## Goal
Download images from a list of URLs.

## Inputs
- `urls` (list): URLs of images to download
- `output_dir` (string, optional): Where to save (default: temp/)

## Skills
- None (custom execution)

## Execution
`executions/download_images.py`

## Outputs
- Downloaded images in the output directory

## Requirements
- `requests` package

## Notes
- Max 10 concurrent downloads to avoid rate limits
```

Then ask the AI: "Create the execution script for downloading images"

---

## File Reference

| File | Purpose | Commit to Git? |
|------|---------|----------------|
| `CLAUDE.md` | AI behavior rules | Yes |
| `.claude/settings.json` | Permissions | Yes |
| `instructions/` | Task guides | Yes |
| `executions/` | Python code | Yes |
| `.env.example` | Template | Yes |
| `.env` | Actual API keys | **NO** |
| `temp/` | Temporary files | **NO** |

---

## Why "IDEA"?

- **I**nstructions - What to do
- **D**ecisions - AI figures out how
- **E**xecutions - Code does the work
- **A**I - Connects it all

You have an IDEA. AI executes it.

---

## License

MIT - Do whatever you want with it.
