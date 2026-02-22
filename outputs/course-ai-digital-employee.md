# AI Digital Employee — $97 Skool Course

## Course Overview

**Name:** AI Digital Employee
**Price:** $97
**Platform:** Skool
**Tagline:** Set up an AI employee that knows your business, follows your workflows, and does the work — in under an hour.
**Promise:** By the end of this course, you'll have a fully configured AI workspace that automates your repetitive work using Claude Code.

**Who it's for:**
- Founders and business owners who want AI to handle operations, content, and research
- Employees who want to automate parts of their role
- Students who want to automate coursework and research
- Anyone who's tried ChatGPT but wants something that actually remembers who they are

**Format:** 7 lessons. Each lesson = 1 video. Watch it, do it, move on.

---

## Lesson 1: Why You're Using AI Wrong (10-15 min)

*Record: Talking head + screen share diagrams*

**What you'll cover:**
1. The chatbot trap — most people have long, messy conversations with no structure, no memory, no consistency
2. The fix — treat AI like an employee: give it onboarding (context), task guides (instructions), and tools (scripts)
3. The workspace model — one folder with 4 sub-folders:
   - `context/` = onboarding (who you are, what you do)
   - `instructions/` = SOPs (how to do each task)
   - `scripts/` = tools (code that pulls data)
   - `outputs/` = deliverables (finished work)
4. Context stacking — the 5 layers that make AI output actually good:
   - CLAUDE.md → business.md → personal.md → strategy.md → data.md
   - Show the diagram: each layer builds on the last
5. The 4 mistakes beginners make:
   - No context → bad output
   - Chatbot mode → inconsistent results
   - No planning loops → janky workflows
   - No scripts → no real-time data

**On screen:** Context stacking diagram, before/after quality comparison, workspace folder structure

**End with:** "Now you understand the model. Next lesson, we set it up."

---

## Lesson 2: Setup — Clone to Working in 15 Minutes (15-20 min)

*Record: Full screen share, step by step*

**What you'll cover:**

**Part 1 — Install the tools (5 min)**
1. Download VS Code from code.visualstudio.com (or Antigravity from antigravity.devcycle.cc)
2. Open VS Code, go to Extensions, search "Claude Code", install it
3. Open terminal (Terminal → New Terminal)
4. Verify: `node --version` (need 18+), `python3 --version` (need 3.x)
5. Reassure: "This is not coding. It's chatting with a bot inside a folder."

**Part 2 — Clone the template (3 min)**
1. Open terminal in VS Code
2. Run: `git clone https://github.com/systemstoscale/AI-Digital-Employee.git`
3. File → Open Folder → select the cloned folder
4. Quick tour: walk through every folder and file on screen. 30 seconds max.

**Part 3 — Get your free API key (2 min)**
1. Go to newsapi.org/register
2. Create account (name, email, password — 30 seconds)
3. Copy the API key
4. Open `.env` in VS Code, paste it after `NEWS_API_KEY=`
5. Save

**Part 4 — Set up your shortcut aliases (3 min)**

IMPORTANT: Explain clearly that there are TWO places you type things:
- The **regular terminal** — where you run normal commands like `python3`, `git`, etc.
- **Inside Claude Code** — where you chat with the AI and use `/project:` commands

The aliases let you start Claude Code with one command from ANY terminal window.

1. Open your terminal (regular terminal, NOT inside Claude Code)
2. Run this command — copy and paste it exactly:
   ```
   echo '
   # AIDE — AI Digital Employee aliases
   alias cs="cd /path/to/AI-Digital-Employee && claude"
   alias cr="cd /path/to/AI-Digital-Employee && claude --dangerously-skip-permissions -p /project:prime"' >> ~/.zshrc
   ```
   (Replace `/path/to/AI-Digital-Employee` with wherever you cloned the repo)
3. Close and reopen your terminal (or run `source ~/.zshrc`)
4. Now test it:
   - Type `cs` → starts Claude Code in safe mode (asks permission before doing things)
   - Type `cr` → starts Claude Code in YOLO mode AND auto-primes (no permission prompts, reads your context automatically, ready to go instantly)

Explain what each does:
- `cs` = **Claude Safe** — starts Claude Code, you manually type `/project:prime` to load context
- `cr` = **Claude Risky** — starts Claude Code with all permissions, auto-loads your context. This is what you'll use 90% of the time.

On screen: Show the terminal, paste the command, close and reopen, type `cr`, watch it auto-prime.

"From now on, every time you want to use your AI employee, you just open a terminal and type `cr`. Two letters. That's it."

**Part 5 — Run the live demo (5 min)**
1. In terminal (before starting Claude): `python3 scripts/fetch-news.py`
2. Open `outputs/latest-news.md` — show 10 real articles
3. Type `cr` to start Claude Code in YOLO mode — it auto-primes
4. Type: "Follow the news-to-content instruction using the news you just fetched"
5. Watch Claude generate LinkedIn posts, tweets, and a newsletter snippet
6. Open the output file — show the finished content
7. Bonus: `python3 scripts/fetch-news.py "startup funding"` — show custom topics

**On screen:** Every click, every command, every output file

**End with:** "You just automated content creation with a free API in 15 minutes. Now let's make it yours."

---

## Lesson 3: Context — Onboard Your AI Employee (15-20 min)

*Record: Screen share, filling in real files live*

**What you'll cover:**

**business.md (5 min)**
- Open the file, walk through each placeholder
- Fill it in live for your own business (or a demo business)
- What to include: company name, what you do, products/services, audience + their pain point, tech stack, key links
- Tip: more detail = better output. Don't be vague.
- Mistake: writing "we help businesses grow" — be specific about HOW

**personal.md (4 min)**
- Fill in: name, role, coding experience level
- Communication style: brief and direct? step-by-step? detailed?
- Output format: markdown? slides? plain text?
- Risk tolerance: should the AI ask before acting, or move fast?
- Pet peeves: tell it what you hate (filler phrases, generic intros, etc.)

**strategy.md (4 min)**
- Top priority: your #1 focus right now (1-2 sentences)
- Current goals: 2-3 goals with timeframes
- Active projects: what's in progress, what's the next step
- Key metrics: the numbers you track
- What's NOT a priority: crucial — stops the AI from wasting time on stuff that doesn't matter right now

**data.md — optional (2 min)**
- When to use: you have metrics from analytics, CRM, etc.
- Paste in your latest numbers
- Can be updated manually or with a script later

**Test it (3 min)**
- Run `/project:prime` with your filled-in context
- Claude should now know who you are, what you do, what you're working on
- Test: ask it a question about your business — the answer should reflect YOUR context
- Show the difference: same question before context vs. after context

**On screen:** Side-by-side of each file being filled in, then the /prime output

**End with:** "Your AI employee is now onboarded. It knows your business. Next: teach it what to do."

---

## Lesson 4: Instructions — Teach It Your Workflows (15-20 min)

*Record: Screen share, building a real instruction live*

**What you'll cover:**

**How instructions work (3 min)**
- An instruction = a text file with: goal, inputs, steps, output format
- Why this beats chatting: same quality every time, saves you from re-explaining
- Quick tour of `_template.md` — the structure every instruction follows
- Quick tour of the 7 included examples — name each one and what it does

**The planning loop (5 min)**
- The two power commands: `/project:create-plan` and `/project:implement`
- Demo: `/project:create-plan I want to automate my weekly LinkedIn posting`
- Watch Claude: it reads the workspace, analyzes what exists, writes a detailed plan
- Show the plan file — steps, files to create, decisions made
- Then: `/project:implement` — watch Claude execute every step

**Build your first custom instruction live (7 min)**
- Pick a real task (e.g., "write a weekly email newsletter from my notes")
- Run `/project:create-plan`
- Review the plan together — point out how Claude considers existing context and files
- Run `/project:implement`
- Watch it create the instruction file, update CLAUDE.md, and wire everything together
- Test the new instruction — run it and show the output

**The self-correction loop (3 min)**
- What happens when something fails: Claude reads the error, fixes the code, retests
- Show it in action if possible (intentionally break something)
- Claude updates the instruction's "Notes" section with what it learned
- Over time, instructions get smarter — this is the key differentiator

**On screen:** create-plan output, implement running live, the finished instruction file, the output

**End with:** "You now have reusable commands. Run them anytime, get consistent results. Next: real-time data."

---

## Lesson 5: Scripts — Connect Real-Time Data (10-15 min)

*Record: Screen share, adding a new script live*

**What you'll cover:**

**What scripts do and why you don't need to code (2 min)**
- Scripts = small programs that pull external data into your workspace
- You don't write them — Claude writes them for you
- The fetch-news.py is proof: it fetches 10 articles with zero coding from you
- Pattern: script fetches data → saves to outputs/ → instruction processes it

**Add a new script with Claude — live (8 min)**
- Pick a practical example: "I want to pull the top posts from Hacker News" (or YouTube data, or Google Trends)
- Run: `/project:create-plan I want a script that fetches the top 10 Hacker News posts and saves them to outputs/`
- Watch Claude research the approach, decide on the right API, write the plan
- Run: `/project:implement`
- Watch Claude write the script, test it, save it to scripts/
- Run the script manually to verify it works
- Show the output file
- If it fails: show the self-correction loop live — Claude reads error, fixes, retries

**Free APIs worth knowing (2 min)**
- NewsAPI — news (already included, 100 req/day free)
- Serper — Google search results (2,500 free credits)
- Apify — web scraping (free tier)
- Any API: add the key to .env, tell Claude what you want, let it build the script

**On screen:** create-plan for a new script, implement running, the finished script, the output

**End with:** "Your AI employee can now pull live data from the internet. Next: real workflows you can copy."

---

## Lesson 6: Real-World Workflows You Can Steal (15-20 min)

*Record: Screen share, running each workflow end to end*

**What you'll cover:**

**Workflow 1: Content Creator (5 min)**
- Context: content marketing agency (show the example from `_examples.md`)
- Run the full pipeline live:
  1. `python3 scripts/fetch-news.py "saas marketing"`
  2. `/project:prime`
  3. "Follow the news-to-content instruction"
- Show output: 3 LinkedIn posts, 6 tweets, newsletter snippet
- Then: "Follow the write-blog-post instruction on the topic: why SaaS companies need a content calendar"
- Show output: full 1,500-word blog post with SEO metadata
- Then: "Follow the repurpose-content instruction using the blog post you just wrote"
- Show output: the blog post turned into social content
- Time comparison: this took 5 minutes. Doing it manually takes 3+ hours.

**Workflow 2: Business Operations (5 min)**
- Context: consulting firm ops manager
- "Follow the weekly-report instruction. Here are my notes: [paste rough notes]"
- Show output: formatted status report with highlights, project updates, metrics
- "Follow the competitor-analysis instruction for [company name]"
- Show output: structured competitor profile with comparison table

**Workflow 3: Student (5 min)**
- Context: CS student
- "Follow the research-paper instruction. Topic: consistency models in distributed databases"
- Show the multi-step process: research question → sources → bibliography → outline
- "Follow the study-guide instruction for distributed systems, focusing on consensus algorithms"
- Show output: study guide with key concepts, practice questions, answers

**Build your own (3 min)**
- Recap the pattern: identify a repeating task → create-plan → implement → test → iterate
- Encourage: "Pick ONE task you do every week. Automate it before moving on."

**On screen:** Each workflow running, outputs side by side

**End with:** "You've seen 6 workflows across 3 different roles. Pick the one closest to yours, customize the context, and start using it today."

---

## Lesson 7: Level Up — Power User Tips (10-15 min)

*Record: Screen share with tips and demos*

**What you'll cover:**

**YOLO mode (3 min)**
- Safe mode (default): Claude asks permission for every action — good for learning
- YOLO mode: Claude moves fast, no permission prompts — good for speed
- How to set it up: shell aliases `cs` (safe) and `cr` (YOLO + auto-prime)
- Show the command to set aliases, then demo: `cr` → instant primed session
- When to use which: safe mode when experimenting, YOLO when you know what you're doing

**Multiple instances (2 min)**
- Command+backslash → new terminal
- Run `cr` in each → two Claude instances side by side
- Use case: plan in one terminal, implement in another
- Use case: run a long task in one, start something else in the other

**Skills — plugins for your workspace (3 min)**
- Skills = installable packages that add capabilities
- Where to find them: github.com/anthropics/skills
- Example: PowerPoint skill — turns any markdown report into a .pptx presentation
- How to install: download the skill, put it in your workspace, Claude detects it
- Browse the marketplace for ideas

**MCP integrations — advanced (3 min)**
- MCP = Model Context Protocol — lets Claude connect to external services
- Example: connect to Apify for YouTube channel scraping
- Example: connect to a CRM, database, or internal tool
- When to use MCP vs. a simple script: MCP for ongoing connections, scripts for one-off data pulls
- Note: "This is advanced. Start with scripts. Graduate to MCP when you need it."

**Keep improving (2 min)**
- Review the "Notes" section of your instructions after each run
- Update your strategy.md weekly or monthly
- Share your best instructions in the community
- The workspace compounds: every run makes it smarter

**On screen:** YOLO mode demo, multiple terminals, skills marketplace, MCP config

**End with:** "You now have everything you need. The template, the context, the instructions, the scripts. Go build. Share what you create in the community. I'll see you there."

---

## Course Assets Included

| Asset | What It Is |
|-------|-----------|
| AIDE Template Repo | Full workspace template (GitHub link) |
| 7 Example Instructions | Ready-to-use task guides for content, research, reports |
| fetch-news.py Script | Working script with free NewsAPI integration |
| 3 Example Contexts | Filled-in examples for content creator, student, business ops |
| Skool Community Access | Ask questions, share templates, get help |

---

## Skool Setup Notes

**Community Name:** AI Digital Employee
**Price:** $97
**Classroom:** 7 lessons, each is 1 video

| # | Lesson | Video Length | Format |
|---|--------|-------------|--------|
| 1 | Why You're Using AI Wrong | 10-15 min | Talking head + diagrams |
| 2 | Setup — Clone to Working | 15-20 min | Full screen share |
| 3 | Context — Onboard Your AI | 15-20 min | Screen share, filling in files |
| 4 | Instructions — Teach It Workflows | 15-20 min | Screen share, live build |
| 5 | Scripts — Connect Real-Time Data | 10-15 min | Screen share, live build |
| 6 | Real-World Workflows | 15-20 min | Screen share, running workflows |
| 7 | Level Up — Power User Tips | 10-15 min | Screen share, tips + demos |

**Total recording time: ~90-120 minutes across 7 videos**

**Community Features:**
- Pinned post: GitHub repo link + quick start checklist
- Channel: "Share Your Instructions" — members post their custom instructions
- Channel: "Troubleshooting" — help each other
- Weekly post: new instruction idea or workflow tip

**Drip Schedule (optional):**
- Lessons 1-2: Available immediately (get them set up and seeing results fast)
- Lessons 3-5: Unlock after 3 days
- Lessons 6-7: Unlock after 7 days
