# Lesson 2: AI Employee Onboarding
**Video length:** 15-20 min | **Format:** Screen share, showing BOTH approaches


> You wouldn't hire an employee without onboarding them. In this lesson, you'll fill in your context files so your AI knows who you are, what your business does, your goals, and your metrics. We'll show two ways: automated setup with one command, and manual setup so you see exactly what goes into each file.

---

### Why Context Matters

Without context, every conversation with your AI starts from zero. You have to re-explain:
- Who you are
- What your business does
- What you're trying to achieve
- What's important right now

With context files, the AI reads your full business picture at the start of every session. It remembers everything. The output quality jumps 10x.

---

### Two Ways to Set Up Context

#### Way 1: Automated Setup (Faster)

1. Open Claude Code (click the Claude icon in VS Code)
2. Type:
   ```
   /setup
   ```
3. Claude asks you questions in 4 rounds
4. You answer naturally (just type like you're explaining to a new hire)
5. Claude writes all 4 context files automatically

**Rounds:**
- Round 1: Your Business → writes `business.md`
- Round 2: You → writes `personal.md`
- Round 3: Your Strategy → writes `strategy.md`
- Round 4: Your Data → writes `data.md` (optional)

6. At the end, Claude auto-primes and says "Your AI employee is set up and ready."

---

#### Way 2: Manual Setup (More Control)

**This is what we'll show in the video, so you see exactly what goes into each file.**

1. Open `context/_examples.md`
2. Look at the 3 examples:
   - Content marketing agency
   - CS student
   - Consulting firm ops manager
3. Pick the one closest to your role
4. Copy the relevant sections
5. Paste into your own context files and customize

We'll walk through filling in each file:

---

### File 1: business.md

**What it's for:** High-level overview of your company.

```markdown
# Business Context

## Company
- **Name:** [Your Business Name]
- **Industry:** [e.g., Marketing agency, SaaS, Coaching]
- **What we do:** [1-2 sentences]
- **Who we serve:** [Your ideal customer]

## Products/Services
- [Product 1]: [Brief description]
- [Product 2]: [Brief description]

## Tech Stack
- [Tools you use regularly]

## Key Links
- Website: [URL]
- Dashboard: [URL if applicable]
- CRM: [URL if applicable]
```

**Example from live call (Max's agency):**
```markdown
# Business Context

## Company
- **Name:** Skalers.io
- **Industry:** AI systems for businesses
- **What we do:** Build AI employees that replace entire roles in 7-9 figure companies
- **Who we serve:** Established businesses ($30K/month+) ready to automate client acquisition and fulfillment

## Products/Services
- AI Knowledge Base (RAG database for instant company-wide answers)
- AI Client Acquisition (autonomous outbound SDR that books calls 24/7)
- AI Client Fulfillment (delivery + operations AI)

## Tech Stack
- Claude Code (development)
- Supabase (database)
- Vercel (hosting)
- n8n (workflow automation)
- Airtable (CRM)
- Instantly (cold email)

## Key Links
- Website: https://skalers.io
- Tools page: https://skalers.io/tools
```

---

### File 2: personal.md

**What it's for:** Who you are, your role, how you like to work.

```markdown
# Personal Context

## Who I Am
- **Name:** [Your name]
- **Role:** [Your title/position]
- **Coding experience:** [Advanced / Intermediate / Beginner / None]

## Communication Preferences
- **Style:** [e.g., Brief and direct / Detailed explanations / Conversational]
- **Output format:** [e.g., Markdown / Google Docs / Plain text]
- **Ask before taking action:** [Yes / No]
  - Yes = Claude asks permission before running code or making changes (safer for beginners)
  - No = Claude executes immediately (YOLO mode—faster once you're comfortable)

## Pet Peeves
- [Things that annoy you or waste time]

## Stories & Voice
- [Recurring stories you tell]
- [Key phrases you use]
- [Your communication style for content]
```

**Example:**
```markdown
# Personal Context

## Who I Am
- **Name:** Max
- **Role:** Founder / Systems Architect
- **Coding experience:** Advanced (but prefer AI writes it)

## Communication Preferences
- **Style:** Brief and direct. No fluff.
- **Output format:** Markdown, always.
- **Ask before taking action:** No (YOLO mode)

## Pet Peeves
- Over-engineering. Build the simplest version that works.
- Endless chat conversations. Use instructions instead.
- Repeating myself. That's why we have context files.

## Stories & Voice
- "AI replaces roles, not tasks"
- "Same patterns, different scale"
- "If you can't close a client in two calls, you're doing it wrong"
```

---

### File 3: strategy.md

**What it's for:** What you're working on RIGHT NOW.

```markdown
# Strategy Context

## Current Focus
**#1 Priority:** [The ONE thing that matters most this month]

## Top 3 Goals
1. [Goal 1]
2. [Goal 2]
3. [Goal 3]

## Active Projects
- [Project 1]: [Status]
- [Project 2]: [Status]

## Metrics That Matter
- [Metric 1]: [Target]
- [Metric 2]: [Target]

## NOT a Priority
- [Things you're explicitly NOT focusing on right now]
```

**Example:**
```markdown
# Strategy Context

## Current Focus
**#1 Priority:** Launch AI Employee course at $97. Get 100 members in 30 days.

## Top 3 Goals
1. Record all 7 lessons by March 1
2. Set up Skool community with templates and workflows
3. Drive traffic via YouTube + free community

## Active Projects
- AI Employee course (in progress)
- 10xLeads.io course refresh (maintenance)
- Client project: German coaching company AI system (delivery)

## Metrics That Matter
- Course signups: Target 100 in first month
- YouTube views: 10K/month
- Community engagement: 50+ active members

## NOT a Priority
- New client acquisition (pipeline is full through Q2)
- Social media growth (YouTube only, no Instagram/TikTok)
- Building new products (focus = courses + current clients)
```

---

### File 4: data.md (Optional)

**What it's for:** Current numbers from your business.

This file is optional for now. You can fill it in later once you connect APIs to pull metrics automatically.

```markdown
# Data Context

## Current Metrics (as of [date])
- **Leads:** [number]
- **Calls booked:** [number]
- **Active clients:** [number]
- **MRR:** $[amount]

## Data Sources
- [Tool 1]: [What data it provides]
- [Tool 2]: [What data it provides]

## API Keys Connected
- [List of tools you've integrated]
```

---

### After You Fill In the Files

1. Save all changes (Cmd+S / Ctrl+S)

2. Test that it worked. In Claude Code, type:
   ```
   /init
   ```

3. Claude will read all your context files and summarize:
   - Who you are
   - What your business does
   - What you're focused on
   - What matters right now

4. If the summary looks right, you're done

5. From now on, start every session with `/init` (or use the `cr` alias from Lesson 2)

---

### Pro Tip: Update Context Regularly

Your context files are living documents. Update them when:
- You start a new project
- Your #1 priority changes
- You hit a goal and set a new one
- You connect a new tool or data source

The more current your context, the better your AI's output.

---

### What Good Context Looks Like

Open `context/_examples.md` and read all 3 examples:
1. Content marketing agency founder
2. CS student
3. Consulting firm ops manager

Notice how each one:
- Is specific (not generic)
- Includes real goals and metrics
- Shows personality and preferences
- Focuses on what matters NOW

Your context should be the same.

---

### Next Steps

Now that your AI knows who you are, it's time to teach it what to do. In Lesson 4, we'll build your first custom automated workflow from scratch.

---
---
