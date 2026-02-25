# Lesson 6: AI Employee Operations
**Video length:** 15-20 min | **Format:** Screen share with tips, demos, and scaling strategies


> You've got the foundation. Now make it fast. In this lesson: YOLO mode for speed, running multiple AI instances in parallel, managing multiple clients, connecting external tools, deploying automations, and the path from personal productivity to building AI systems as a service.

---

### YOLO Mode for Speed

```
SAFE MODE (cs)                     YOLO MODE (cr)
──────────────────────────────────────────────────────
Claude asks permission             Claude just does it
for every action
                                   + auto-primes
Good for learning                  (reads your context
                                    automatically)

"Can I write to this file?"        Just writes it

Slower but safer                   Fast. Use this 90%
                                   of the time.
```

---

### Multiple Instances

- Cmd+\ → new terminal pane
- Type `cr` in each → two Claude instances side by side

Use cases:
- Plan in one terminal, implement in another
- Run a long task in one, start something else in the other
- Research in one, write in the other

---

### Claude Skills / Plugins

Skills are installable packages that add capabilities to your workspace.

Where to find them: github.com/anthropics/skills

Example: PowerPoint skill → turns any markdown report into a .pptx presentation.

---

### The Self-Correction Loop

```
┌───────────┐    ┌───────────┐    ┌───────────┐    ┌───────────┐
│  ERROR     │───→│  READ     │───→│  FIX      │───→│  UPDATE   │
│  happens   │    │  error    │    │  code     │    │  instruc- │
│            │    │  message  │    │  and      │    │  tion     │
│            │    │           │    │  retest   │    │  with     │
│            │    │           │    │           │    │  lesson   │
└───────────┘    └───────────┘    └───────────┘    └───────────┘
                                                        │
                                                        ▼
                                              SYSTEM IS SMARTER
                                              Same mistake never
                                              happens twice
```

Over time, your instruction files accumulate lessons learned. The workspace compounds.

---

### NEW: Managing Multiple Clients / Projects

**From the live call: Brice asked if one instance handles all clients.**

> "Max's answer: Yes. I use one AI employee for everything. Just organize your instructions into subfolders."

```
YOUR WORKSPACE FOR AN AGENCY:

AI-Employee/
├── context/
│   ├── business.md (your agency info)
│   ├── personal.md
│   └── strategy.md
├── instructions/
│   ├── client-acme/
│   │   ├── weekly-report.md
│   │   ├── competitor-tracking.md
│   │   └── content-calendar.md
│   ├── client-techcorp/
│   │   ├── lead-generation.md
│   │   ├── email-sequences.md
│   │   └── monthly-analytics.md
│   └── internal/
│       ├── proposal-generator.md
│       ├── invoice-automation.md
│       └── client-onboarding.md
├── scripts/
│   ├── fetch-acme-analytics.py
│   ├── fetch-techcorp-crm.py
│   └── generate-invoice.py
└── outputs/
    ├── acme/
    ├── techcorp/
    └── internal/
```

**The AI reads the full workspace and knows which instructions belong to which client.**

To run a client-specific task:
```
/implement instructions/client-acme/weekly-report.md
```

---

### NEW: Connecting External Tools (From Live Call)

**Users asked about GoHighLevel, Notion, Stripe, HubSpot integration.**

**The universal process:**

1. Find the integration settings in your tool
2. Generate an API key
3. Add to `.env` file (or paste in Claude chat)
4. Tell Claude what data you want

**Example: GoHighLevel**
```
Settings → API → Create Key → Copy
Add to .env: GHL_API_KEY=your_key_here
Tell Claude: "Pull my lead count, call count, and client count from GoHighLevel"
```

Claude figures out the API endpoints and writes the script.

**Works with:**
- GoHighLevel (CRM/leads)
- Notion (knowledge base)
- Stripe (revenue, subscriptions)
- Airtable (custom databases)
- HubSpot (sales pipeline)
- Any API-enabled tool

---

### NEW: Deploying Automations (From Live Call)

**Users asked: "How do I keep scripts running 24/7 without my computer on?"**

**Two deployment scenarios:**

#### 1. Websites / Landing Pages
- Built locally with Claude Code
- Hosted on **Vercel** (free tier available)
- Example: Proposal sites, qualification pages, dashboards

**Process:**
1. Build the site locally in `outputs/website/`
2. Tell Claude: "Deploy this to Vercel"
3. Claude pushes to GitHub → auto-deploys to Vercel
4. You get a live URL

---

#### 2. Recurring Scripts / Automations
- For tasks that run daily, weekly, etc.
- Host on **trigger.dev**, **Railway**, or **n8n Cloud**

**Process:**
1. Build the script locally
2. Tell Claude: "Set this up to run every morning at 8am on trigger.dev"
3. Claude creates the deployment config
4. Your script runs automatically without your computer

**Example use cases:**
- Daily lead scraping
- Weekly client reports
- Hourly social media monitoring
- Daily CRM data sync

---

### From Personal Productivity to Building AI Systems

Everything you just learned is the foundation of what we build at Skalers for enterprise clients:

```
YOUR WORKSPACE                       ENTERPRISE AI SYSTEM
──────────────────────────────────────────────────────────────
context/                          →  AI Knowledge Base
  (your business info)                (company-wide RAG database)
                                      Value: $25-40K setup

instructions/                     →  AI Acquisition System
  (your task guides)                  (autonomous outbound SDR)
                                      Value: $45-80K setup

scripts/                          →  AI Fulfillment System
  (your data connectors)              (delivery + operations AI)
                                      Value: $75-120K setup
```

The patterns are identical. The scale is different.

> "The current state of AI is moving beyond simple tasks to replacing entire roles of people in companies. We built an AI coach system for a German company with 300 clients. That's not a task—that's a whole role." — Max

If you want to go deeper:
- Join the free Skalers community at skalers.io
- Learn the IDEA Framework (Instructions → Decisions → Executions → AI)
- Build these systems for clients at $20-100K per project

---
---

# TROUBLESHOOTING GUIDE (NEW)

## Common Setup Issues

### "git: command not found"
**Mac:**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install git
```

**Windows:**
- Download from git-scm.com
- Run installer
- Restart VS Code

---

### "Could not resolve host: github.com"
- Check your internet connection
- Try again
- If using VPN, try disabling it

---

### "Authentication failed" (GitHub)
- Create a GitHub account first: github.com/signup
- Make sure you're logged in
- If still failing, try: `git config --global credential.helper store`

---

### "Permission denied" (Mac)
- VS Code needs file access
- Mac Settings → Security & Privacy → Files and Folders → Allow VS Code

---

### "Module not found" (Python)
```bash
pip3 install requests
```

Or if you have a `requirements.txt`:
```bash
pip3 install -r requirements.txt
```

---

### API key not working
- Check `.env` file formatting
- Correct: `KEY=value` (no spaces)
- Incorrect: `KEY = value` (spaces cause errors)
- Save the file after editing (Cmd+S / Ctrl+S)

---

### "SSL: CERTIFICATE_VERIFY_FAILED"
- This is common on Mac
- Claude will auto-detect and fix it
- Or manually run:
  ```bash
  pip3 install --upgrade certifi
  ```

---

### Claude Code not appearing
- Make sure you opened a folder (File → Open Folder)
- Check that Claude Code extension is installed
- Restart VS Code
- Look for the small Claude icon in the top right

---

### Terminal not opening
- Menu: Terminal → New Terminal
- Or keyboard: Ctrl+` (Mac/Windows)
- Or click the + icon in the bottom panel

---

# BONUS: Pre-Flight Checklist PDF (For Skool)

Create a downloadable PDF with:

**Before Lesson 1:**
- [ ] Claude.ai account ($17/month minimum)
- [ ] GitHub account (free)
- [ ] 15 GB free disk space
- [ ] Stable internet
- [ ] 2 hours for setup

**Before Lesson 2:**
- [ ] VS Code downloaded
- [ ] Claude Code extension installed
- [ ] Git installed (check: `git --version`)
- [ ] Node.js installed (check: `node --version`)
- [ ] Python 3 installed (check: `python3 --version`)

**Before Lesson 3:**
- [ ] Template cloned successfully
- [ ] News API key obtained
- [ ] Demo script ran successfully
- [ ] Context files ready to fill in

**You're ready!**

---

# RECORDING PRIORITIES

Based on what worked in the live call:

### MUST RE-RECORD:
1. **Lesson 2** — Add full Git installation, terminal vs Claude Code diagram, troubleshooting
2. **Lesson 3** — Show `/setup` running OR manual setup matching live call

### HIGH PRIORITY ADDITIONS:
3. **Lesson 5** — Add GoHighLevel or Notion live connection demo
4. **Lesson 6** — Add automated proposal workflow (was the biggest wow moment)
5. **Lesson 7** — Add multi-client management section, deployment guide

### BONUS CONTENT (Optional):
6. Landing page builder workflow
7. Advanced: Managing 10+ clients at scale
8. Deep dive: Deploying to Vercel + trigger.dev

---

# KEY QUOTES TO USE IN COURSE

> "AI replaces roles, not tasks. That's the business opportunity." — Max

> "Everything you just learned is the foundation of what we build at Skalers for enterprise clients. The patterns are identical. The scale is different." — Max

> "I advise against spending time learning extensive traditional coding languages. Current AI tools like Claude Code can handle complex requests through simple, conversational instructions." — Max

> "Successful software often features only one core capability, like generating YouTube thumbnails, to prevent projects from becoming too complex, which wastes time and delays profitability." — Max

> "The setup is the hardest part. Once users see outputs/latest-news.md populate with real data, they immediately 'get it' and start asking high-value questions about real business applications." — From call analysis

---

# SKOOL SETUP CHECKLIST

## Community Settings
- **Name:** AI Employee
- **Price:** $97
- **Access:** Classroom + Community

## Classroom Structure

| # | Lesson Title | Video Length | Status |
|---|-------------|-------------|--------|
| 1 | Why Your AI Sucks (And How to Fix It) | 10-15 min | ✅ Ready |
| 2 | Install and Run Your First Demo | 20-25 min | 🔄 RE-RECORD |
| 3 | Teach It Who You Are | 15-20 min | 🔄 RE-RECORD |
| 4 | Build Your First Automated Workflow | 15-20 min | ✅ Ready |
| 5 | Connect Any API in Minutes | 15-20 min | ✅ Updated |
| 6 | Steal These 7 Workflows | 20-25 min | ✅ Updated |
| 7 | 10x Your Speed | 15-20 min | ✅ Updated |

## Pinned Post (Copy-Paste)

```
START HERE 👇

1. Read the Pre-Flight Checklist (pinned below)
2. Watch Lesson 1 (10 min) — Understand the model
3. Watch Lesson 2 (20 min) — Get set up + run the live demo
4. Watch Lesson 3 (15 min) — Onboard your AI with /setup
5. Watch Lessons 4-7 at your own pace

📦 Template repo: github.com/systemstoscale/AI-Employee
🔑 Free API key: newsapi.org/register
❓ Stuck? Post in #troubleshooting

Common issues already solved:
- Git installation
- API key setup
- Terminal confusion
- Permission errors

Check the Troubleshooting doc first, then post if still stuck.
```

## Community Channels

1. **#general** — Main discussion
2. **#share-your-workflows** — Members post their custom instructions
3. **#troubleshooting** — Help with setup and errors
4. **#wins** — Show what your AI employee produced
5. **#business-opportunities** — For those building AI systems for clients

## Drip Schedule (Optional)

- Lessons 1-3: Available immediately (get them set up and seeing results fast)
- Lessons 4-5: Unlock after 3 days
- Lessons 6-7: Unlock after 7 days
- Bonus content: Unlock after posting first win

## CTA for Skalers (End of Lesson 7)

```
Want to build AI systems like this for clients at $20-100K per project?

Join the free Skalers community: skalers.io

Learn the IDEA Framework. Build the 3 core AI systems.
Land your first client in 90 days.

Real examples from the community:
- AI Knowledge Base for coaching company (300 clients)
- AI SDR for agency (books 20+ calls/month autonomously)
- AI Fulfillment system (saves 40 hours/week in client ops)

Same patterns you just learned. Enterprise scale. High-ticket pricing.
```

---

**END OF UPDATED COURSE**
