# Lesson 1: AI Employee Creation
**Video length:** 20-25 min | **Format:** Full screen share, every click shown, with troubleshooting


> In this lesson, you'll install everything you need, troubleshoot common issues, clone the template, and run a live demo that fetches real AI news. We'll show every step, including what to do when things break. By the end of this video, you'll have a working AI employee on your machine.

---

### CRITICAL: Two Interfaces You'll Use

Before we start, understand this: you'll be using TWO different places to type things.

```
┌─────────────────────────────────────────────────────────┐
│  VS CODE WINDOW                                         │
│                                                         │
│  ┌──────────────────────┐  ┌──────────────────────┐    │
│  │  TERMINAL            │  │  CLAUDE CODE CHAT    │    │
│  │  (Left side)         │  │  (Right side)        │    │
│  │                      │  │                      │    │
│  │  $ git clone ...     │  │  💬 "Fetch the      │    │
│  │  $ python3 script.py │  │      latest news     │    │
│  │  $ node --version    │  │      about AI"       │    │
│  │                      │  │                      │    │
│  │  For: Git, Python,   │  │  For: Talking to    │    │
│  │  Node commands       │  │  your AI employee    │    │
│  └──────────────────────┘  └──────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

**Terminal** = Run code, install things, check versions
**Claude Code** = Chat with your AI employee

Keep this in mind as we go through the setup.

---

### Step 1: Download and Install VS Code

1. Go to **code.visualstudio.com**
2. Download for your machine (Mac/Windows/Linux)
3. Install it (drag to Applications on Mac, run installer on Windows)
4. Open VS Code

**Alternative:** Download **Antigravity** (VS Code fork with Claude built-in) from antigravity.devcycle.cc

---

### Step 2: Install Claude Code Extension

1. In VS Code, click the **Extensions** icon (left sidebar, looks like 4 squares)
2. Search: **"Claude Code"**
3. Find **"Claude Code for VS Code"** (official Anthropic extension)
4. Click **Install**
5. You'll see a small Claude icon appear at the top right

**Note:** You need to open a folder first for the Claude icon to appear. If you don't see it, don't worry—we'll open a folder in a moment.

---

### Step 3: Open the Terminal

1. In VS Code: **Terminal → New Terminal** (or press Ctrl+` / Cmd+`)
2. A terminal panel appears at the bottom
3. This is where you'll type commands like `git`, `python3`, `node`

**Common issue:** On Mac, it might say "zsh" or "bash". Either is fine.

---

### Step 4: Pre-Flight Checks (Install Missing Tools)

Now we check if you have the required tools. Type these commands in the **TERMINAL** (not Claude chat):

```bash
git --version
```
**Expected:** `git version 2.x.x` or higher

```bash
node --version
```
**Expected:** `v18.x.x` or higher

```bash
python3 --version
```
**Expected:** `Python 3.x.x`

---

### TROUBLESHOOTING: If Commands Not Found

#### If `git: command not found`

**Mac:**
1. Install Homebrew first (if you don't have it):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Then install Git:
   ```bash
   brew install git
   ```
3. Verify: `git --version`

**Windows:**
1. Download from **git-scm.com**
2. Run the installer
3. Restart VS Code
4. Verify: `git --version`

---

#### If `node: command not found`

1. Go to **nodejs.org**
2. Download the **LTS version** (green button)
3. Install it
4. Restart VS Code
5. Verify: `node --version`

---

#### If `python3: command not found`

**Mac:**
```bash
brew install python3
```

**Windows:**
1. Download from **python.org**
2. ✅ Check "Add Python to PATH" during installation
3. Install
4. Verify: `python3 --version` (or just `python --version` on Windows)

---

### Step 5: Connect to Claude.ai

1. Go to **claude.ai**
2. Sign up or log in
3. Subscribe to **Pro** ($17/month minimum)
   - Don't use the free tier—it's rate-limited and won't work for this course
4. In VS Code, click the **Claude icon** (top right)
5. Click **"Use Claude.ai subscription"**
6. Click **Authorize** in the browser window that opens
7. You're connected

**Note:** You'll see this VS Code wants to open a page. Allow it.

---

### Step 6: Create a GitHub Account (If You Don't Have One)

1. Go to **github.com/signup**
2. Sign up (free account is fine)
3. Verify your email
4. That's it—you're ready to clone

**Why:** We need this to download the template repository.

---

### Step 7: Create Your Workspace Folder

1. In VS Code: **File → Open Folder**
2. Navigate to your **Documents** folder (or wherever you want to keep this)
3. Create a new folder: **"AI-Employee"** (or name it after your business)
4. Click **Open**
5. If VS Code asks "Do you trust the authors?", click **Yes, I trust**

Now you have an empty folder open in VS Code.

---

### Step 8: Clone the AI Employee Template

1. In the **TERMINAL** (bottom panel), paste this command:

```bash
git clone https://github.com/systemstoscale/AI-Employee.git .
```

**Note:** The `.` at the end means "clone into THIS folder" (the one you just opened).

2. Press **Enter**

3. You'll see files downloading

4. When it's done, look at the left sidebar—you should see:
   - `context/`
   - `instructions/`
   - `scripts/`
   - `outputs/`
   - `CLAUDE.md`
   - `.env`

**TROUBLESHOOTING:**

- **"Could not resolve host"** → Check your internet connection
- **"Authentication failed"** → Make sure you created a GitHub account (Step 6)
- **"Permission denied"** → The repo might be private. Contact support or check if you're logged into GitHub
- **"fatal: destination path ... already exists"** → The folder isn't empty. Create a NEW empty folder and try again

---

### Step 9: Quick Tour of the Workspace

Click through the folders on the left sidebar:

**context/** — Your onboarding files
- `business.md` → What your company does
- `personal.md` → Who you are, your role
- `strategy.md` → Current goals and priorities
- `data.md` → Your metrics (leads, revenue, etc.)
- `_examples.md` → Filled-in examples you can copy

**instructions/** — Task guides (SOPs for your AI)
- `_example-news-to-content.md` → Turn news into social posts
- `_example-weekly-report.md` → Generate weekly reports
- `_example-write-blog-post.md` → Write SEO blog posts
- 7 total example instructions

**scripts/** — Code that fetches external data
- `fetch-news.py` → Pulls latest news from NewsAPI
- `_example.py` → Template for new scripts

**outputs/** — Where finished work gets saved
- (Empty for now—this is where your AI will save deliverables)

**CLAUDE.md** — The rules your AI follows every session

**.env** — Where you'll store API keys (never commit this to Git!)

---

### Step 10: Get Your Free News API Key

We're going to use a free news API to demonstrate the full pipeline.

1. Go to **newsapi.org/register**
2. Fill in:
   - First name
   - Email
   - Password
3. Click **Submit**
4. Check your email and verify (if required)
5. Copy your **API Key** (big string of letters/numbers)

---

### Step 11: Add the API Key to Your Workspace

You have **two ways** to add API keys:

#### OPTION 1: Manual (Recommended)

1. In VS Code, open the `.env` file (left sidebar)
2. You'll see:
   ```
   NEWS_API_KEY=
   ```
3. Paste your key right after the `=` (no spaces):
   ```
   NEWS_API_KEY=abc123yourkeyhere
   ```
4. Save the file (Cmd+S or Ctrl+S)

#### OPTION 2: Let AI Do It

1. Click the **Claude icon** (top right)
2. Paste your API key in the chat
3. Type: "Add this News API key to my .env file"
4. Claude will update the file for you

**IMPORTANT:** Never paste API keys in the terminal. It won't work.

---

### Step 12: Run the Live Demo

Now for the moment of truth. We're going to fetch real news and see it saved to `outputs/`.

1. In the **TERMINAL**, type:

```bash
python3 scripts/fetch-news.py
```

2. Press **Enter**

3. You'll see:
   ```
   Fetching news about: artificial intelligence
   ✓ Fetched 10 articles
   ✓ Saved to outputs/latest-news.md
   ```

4. In VS Code, click **outputs/** → **latest-news.md**

5. You'll see 10 real AI news articles with:
   - Headline
   - Description
   - Source
   - Published date
   - URL

**If it works:** Congrats! Your workspace is set up correctly.

**If it fails:**

- **"No module named 'requests'"** → Run: `pip3 install requests`
- **"Invalid API key"** → Check your `.env` file. Make sure there's no space after `=`
- **"SSL certificate"** → Claude will auto-detect and fix this if you proceed to Step 13

---

### Step 13: Let Claude Turn News Into Content

Now we'll see the AI process that news data and create social media content.

1. Click the **Claude icon** (top right)
2. Type:
   ```
   /init
   ```
3. Claude will read all your context files (might take 10-15 seconds)

4. Then type:
   ```
   Follow the news-to-content instruction using the news you just fetched.
   ```

5. Claude will:
   - Read `outputs/latest-news.md`
   - Pick the 3 best stories
   - Write 3 LinkedIn posts with hooks
   - Write 6 tweets (2 per story)
   - Write a newsletter snippet
   - Save everything to `outputs/news-content-[date].md`

6. Open the output file and see the finished content

**Self-Correction Demo:**

If Claude encounters an error (like the SSL issue from the live call), watch what happens:
- It reads the error message
- Googles the solution
- Updates the script
- Re-runs the script
- Confirms it works
- Updates the instruction file so it never fails again

This is the self-correction loop that makes the system smarter over time.

---

### Step 14: Try Other Topics

Want to see it work with different topics? Edit the script:

```bash
python3 scripts/fetch-news.py "startup funding"
python3 scripts/fetch-news.py "remote work"
python3 scripts/fetch-news.py "your niche here"
```

Then tell Claude to process the new articles.

---

### What You Just Built

You now have:
- ✅ A local AI workspace on your machine
- ✅ Context files that give the AI your full business picture
- ✅ Pre-built instructions for common tasks
- ✅ A working script that fetches real external data
- ✅ A live demo that turned news into social content in 60 seconds

This is the foundation. Next lesson, we'll teach your AI employee everything about you and your business.

---
---
