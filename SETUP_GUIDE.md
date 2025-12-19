# IDEA Framework Setup Guide
**Instructions, Decisions, Executions, AI**

Set up a reliable AI-powered development environment in under 15 minutes.

---

## What You're Building

An environment where **you write instructions** and **AI runs code**.

Why? AI is smart but inconsistent. If AI is 90% accurate per step, after 5 steps you're down to 59% success. The fix: let AI focus on decisions while reliable code does the actual work.

---

## The IDEA Framework

```
instructions/     →     AI     →     executions/
 (what to do)       (decides)      (does the work)
```

| Folder | What It Contains |
|--------|------------------|
| `instructions/` | Markdown files explaining tasks |
| `executions/` | Python code that does the actual work |

**The AI sits in the middle** - it reads your instructions, makes decisions, and runs the right code.

---

## Prerequisites

### Install Node.js

Claude Code requires Node.js 18 or higher.

**Check if you have it:**
```bash
node --version
```

If you see `v18.x.x` or higher, skip to the next section.

**Install Node.js:**

**Mac (using Homebrew):**
```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Node.js
brew install node
```

**Mac/Linux (using nvm - recommended):**
```bash
# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Restart terminal, then:
nvm install 20
nvm use 20
```

**Windows:**
Download from https://nodejs.org (LTS version)

**Verify:**
```bash
node --version   # Should show v18+
npm --version    # Should show 9+
```

---

## Step 1: Choose Your Editor

### Option A: Antigravity (Recommended)
Antigravity is a Cursor fork with Claude Code built-in.

1. Download from: https://antigravity.devcycle.cc
2. Install (drag to Applications on Mac, run installer on Windows)
3. Open Antigravity
4. Claude Code is ready in the terminal

### Option B: VS Code + Claude Code Extension
Use your existing VS Code setup.

1. Open VS Code
2. Go to Extensions (`Cmd+Shift+X` / `Ctrl+Shift+X`)
3. Search for "Claude Code"
4. Click Install on the official Anthropic extension
5. Restart VS Code
6. Open Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
7. Type "Claude Code" and select "Open Claude Code"

---

## Step 2: Set Up Your Project

```bash
# Clone the framework
git clone https://github.com/YOUR_USERNAME/TheIDEAFramework.git
cd TheIDEAFramework

# Run the setup script
./setup.sh

# Add your API keys
nano .env
```

---

## Step 3: Understanding the Files

After setup, you'll have:

```
TheIDEAFramework/
├── .claude/settings.json  → What Claude Code can do
├── .env                   → Your API keys (never commit)
├── .gitignore             → Protects secrets from git
├── temp/                  → Scratch space
├── CLAUDE.md              → AI behavior rules
├── instructions/          → What to do (task guides)
└── executions/            → How to do it (Python code)
```

### What each file does:

**CLAUDE.md** - The AI's instruction manual. Tells it how to behave.

**.claude/settings.json** - Permissions. What commands Claude Code can run without asking.

**.env** - Your API keys. Never commit this file.

**instructions/** - Markdown files explaining how to do tasks.

**executions/** - Python code that actually does the work.

**temp/** - Temporary files. Safe to delete anytime.

---

## How Everything Connects

```
┌─────────────────────────────────────────────┐
│                   YOU                       │
│           "Scrape this website"             │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│               CLAUDE.md                     │
│         (tells AI how to behave)            │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│              CLAUDE CODE                    │
│                                             │
│  1. Reads instructions/scrape_website.md    │
│  2. Runs executions/scrape.py               │
│  3. If error → fixes → updates instruction  │
│                                             │
└──────────────────────┬──────────────────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
    instructions/  executions/    .env
     (guides)       (code)      (API keys)
                       │
                       ▼
                    temp/
                 (scratch)
                       │
                       ▼
                   OUTPUT
              (Sheets, files)
```

---

## Quick Reference

| File/Folder | Purpose | Commit to Git? |
|-------------|---------|----------------|
| `CLAUDE.md` | AI behavior rules | Yes |
| `.claude/settings.json` | Permissions | Yes |
| `instructions/` | Task guides | Yes |
| `executions/` | Python code | Yes |
| `.env.example` | Template | Yes |
| `.env` | Actual API keys | **NO** |
| `temp/` | Temporary files | **NO** |

---

## Test Your Setup

1. Open your project in Antigravity or VS Code
2. Open the terminal
3. Type `claude` (or open Claude Code from command palette)
4. Try:

```
What files are in this project?
```

Then:

```
Create an instruction for downloading images from URLs
```

Then:

```
Now create the execution for it
```

The AI should:
- Create `instructions/download_images.md`
- Create `executions/download_images.py`
- Follow your project's format

---

## The Self-Correction Loop

This is what makes the system get smarter:

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

**Example:**
1. Code hits API rate limit
2. AI sees "429 Too Many Requests"
3. AI adds delay between requests
4. Works now
5. AI updates instruction: "Note: API limited to 100 req/min"

Next time, anyone using this instruction knows about the limit.

---

## Troubleshooting

**"claude: command not found"**
- Antigravity: Close and reopen terminal
- VS Code: Make sure extension is installed, use Command Palette

**"Node.js not found"**
- Run `node --version`
- If missing, follow install steps above

**Permission errors**
- Check `.claude/settings.json` is valid JSON
- Add the specific command to `allow` array

**Code can't find API keys**
- Make sure `.env` exists
- No quotes around values: `API_KEY=abc123` not `API_KEY="abc123"`

---

## Summary

1. **Install Node.js** (v18+)
2. **Get an editor** (Antigravity or VS Code + extension)
3. **Run setup script**
4. **Add API keys** to `.env`
5. **Start building**

The IDEA Framework: **Instructions** tell the AI what to do. **Executions** do the actual work. **AI** makes **Decisions** and connects them, self-correcting when things break.

---

## What's Next?

1. **Create your first instruction** - Pick a task you do often
2. **Let AI build the execution** - Describe what it should do
3. **Test and refine** - Run it, fix errors, update instructions
4. **Build your library** - Each instruction+execution makes the system more capable

Happy building!
