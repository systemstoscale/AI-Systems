# Lesson 0: AI Employee Model

**Video length:** 10-15 min | **Format:** Talking head + screen share diagrams

---

### The Problem

You're using AI wrong. Here's what most people do:
- Open ChatGPT or Claude
- Type a long prompt
- Get a mediocre answer
- Try again with a different prompt
- Waste 30 minutes going back and forth
- End up rewriting it yourself anyway

The output is inconsistent because the AI has zero context about who you are, what you do, or what you're trying to achieve. It's like hiring someone and giving them no onboarding, no SOPs, and no tools, then wondering why they can't do the job.

### The Fix: Treat AI Like an Employee

When you hire a new employee, you give them:
- **Onboarding**. Who the company is, what it does, how it works
- **Task guides**. SOPs for the work they'll be doing
- **Tools**. Software, accounts, access to what they need
- **A place to put finished work**. Shared drives, project boards

That's exactly what we're going to build. One folder on your computer with 4 sub-folders:

```
┌────────────────────────────────────────────────────────────────────────┐
│                             YOUR WORKSPACE                             │
│                                                                        │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  ┌───────────┐  │
│  │ context/    │→ │instructions/ │→ │ scripts/      │→ │ outputs/  │  │
│  │             │  │              │  │               │  │           │  │
│  │ WHO YOU ARE │  │  WHAT TO DO  │  │ HOW YOU DO IT │  │  RESULTS  │  │
│  │             │  │              │  │               │  │           │  │
│  └─────────────┘  └──────────────┘  └───────────────┘  └───────────┘  │
│                                                                        │
│   Onboarding       Task Guides        Tools             Deliverables   │
└────────────────────────────────────────────────────────────────────────┘
```

- `context/` = Onboarding. Who you are, your business, your goals.
- `instructions/` = SOPs. Step-by-step task guides the AI follows.
- `scripts/` = Tools. Code that pulls data from APIs, automates actions.
- `outputs/` = Deliverables. Where finished work gets saved.

### Context Stacking

The secret to great AI output is context stacking. You layer information so the AI has the full picture before it does anything.

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│            INTELLIGENT CONVERSATION                 │
│            (Your tasks and requests)                │
│                                                     │
├─────────────────────────────────────────────────────┤
│  Layer 5:  data.md       →  Current numbers         │
├─────────────────────────────────────────────────────┤
│  Layer 4:  strategy.md   →  What matters now        │
├─────────────────────────────────────────────────────┤
│  Layer 3:  personal.md   →  Who you are             │
├─────────────────────────────────────────────────────┤
│  Layer 2:  business.md   →  What the company does   │
├─────────────────────────────────────────────────────┤
│  Layer 1:  CLAUDE.md     →  Workspace rules         │
└─────────────────────────────────────────────────────┘
```

Every time you start a new session, the AI reads all of this first. Then when you give it a task, it has the full picture. Your business, your voice, your goals, your metrics. The output quality difference is massive.

### The 4 Mistakes

```
MISTAKE                             FIX
────────────────────────────────────────────────────────
1. Using AI like a chatbot       →  Reusable commands
2. No context each session       →  /init
3. No planning loops             →  /create-plan
                                    + /implement
4. No external data              →  Scripts that pull
                                    real-time data
```

1. **Chatbot mode.** You chat back and forth, waste tokens, get diluted output. Fix: create reusable command files (instructions) that you run every time.
2. **No context.** Every session starts from zero. Fix: run `/init` every time. Loads your full context in seconds.
3. **No planning.** You try to do everything in one message. Fix: use `/create-plan` to design the workflow, then `/implement` to execute it.
4. **No real data.** The AI is guessing instead of using your actual numbers. Fix: scripts that pull real-time data from APIs.

### The Module System

Context stacking is the foundation. But the real power comes when you layer automation modules on top.

Think of your AI Employee as having departments:

```
┌──────────────────────────────────────────────────────────────┐
│                    AI EMPLOYEE MODULES                        │
│                                                              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐   │
│  │ Context  │ │  Daily   │ │  Data    │ │ Productivity │   │
│  │   OS     │ │  Brief   │ │Dashboard │ │  Check-in    │   │
│  │          │ │          │ │          │ │              │   │
│  │ context/ │ │ Morning  │ │ Metrics  │ │ Goals +      │   │
│  │  init    │ │ briefing │ │ from all │ │ habits +     │   │
│  │          │ │          │ │ sources  │ │ tasks        │   │
│  └──────────┘ └──────────┘ └──────────┘ └──────────────┘   │
│                                                              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐   │
│  │  Slack   │ │ Meeting  │ │  Email   │ │   Mobile     │   │
│  │  Intel   │ │  Intel   │ │ Capture  │ │   Access     │   │
│  │          │ │          │ │          │ │              │   │
│  │ Channel  │ │ Google   │ │  Gmail   │ │  Telegram    │   │
│  │ summaries│ │ Meet     │ │  inbox   │ │  commands    │   │
│  │          │ │ search   │ │  digest  │ │              │   │
│  └──────────┘ └──────────┘ └──────────┘ └──────────────┘   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

Each module is:
- A **script** in `scripts/` that does the work
- An **instruction** in `instructions/` that documents how it works
- A **command** (like `/brief` or `/checkin`) that you run in Claude Code

You don't need all of them. Start with Context (you already have it). Then add Daily Brief. Then add more as you need them.

The modules are independent but composable. Daily Brief pulls from Data Dashboard, which pulls from your integrations. Slack Intelligence feeds into Action Items. Everything connects, but nothing breaks if a module is missing.

### What's Possible: From Personal to Enterprise

> "Everything you just learned is the foundation of what we build at Skalers for enterprise clients. The patterns are identical. The scale is different." — Max

At Skalers.io, we build AI systems that replace entire roles, not just tasks:
- AI Knowledge Base → Instant answers for 300-person teams
- AI Client Acquisition → Autonomous outbound that books calls 24/7
- AI Client Fulfillment → Onboarding, reporting, QA, client comms

Same workspace structure. Same context stacking. Same module system. Just bigger scope.

By the end of this course, you'll have the foundation to build systems like these for yourself or for clients at $20K-$100K per project.
