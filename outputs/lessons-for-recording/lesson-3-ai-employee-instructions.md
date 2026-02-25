# Lesson 3: AI Employee Instructions
**Video length:** 15-20 min | **Format:** Screen share, building a real instruction live


> Instructions are reusable task guides your AI follows every time, like SOPs for your digital employee. In this lesson, you'll learn the create-plan, implement loop and build your first custom workflow from scratch. This is where the real power is.

---

### How Instructions Work

An instruction is just a text file with:
- A goal (what it accomplishes)
- Inputs (what info it needs)
- Steps (what to do, in order)
- Output format (where to save, how to structure)

```
┌────────────────────────────────────────────────────┐
│  instructions/_example-news-to-content.md          │
│                                                    │
│  Goal:    Turn news into social content            │
│  Inputs:  topic, platforms                         │
│  Steps:                                            │
│    1. Run fetch-news.py                            │
│    2. Pick 3 best stories                          │
│    3. Write LinkedIn posts                         │
│    4. Write tweets                                 │
│    5. Write newsletter snippet                     │
│  Output:  outputs/news-content-[date].md           │
└────────────────────────────────────────────────────┘
```

Why this beats chatting:
- **Consistent.** Same quality every time
- **Fast.** No re-explaining
- **Reusable.** Run it daily, weekly, whenever

The template includes 7 example instructions.

---

### The Planning Loop

```
┌───────────────┐     ┌────────────────┐     ┌───────────────┐
│  YOU          │     │  CREATE PLAN   │     │  IMPLEMENT    │
│               │     │                │     │               │
│ "I want to   │────→│  Claude reads  │────→│  Claude       │
│  automate    │     │  workspace,    │     │  executes     │
│  my weekly   │     │  designs the   │     │  every step,  │
│  report"     │     │  full plan     │     │  creates      │
│               │     │                │     │  files,       │
│               │     │  Saves to      │     │  self-        │
│               │     │  instructions/ │     │  corrects     │
└───────────────┘     └────────────────┘     └───────────────┘
                                                    │
                                                    ▼
                                         ┌───────────────────┐
                                         │  ERROR?           │
                                         │  Read → Fix →     │
                                         │  Retest → Update  │
                                         │  instruction      │
                                         └───────────────────┘
```

1. Type: `/create-plan I want to automate writing a weekly LinkedIn recap of what I worked on`
2. Claude reads the workspace, analyzes what exists, writes a detailed plan
3. Type: `/implement`
4. Claude creates the instruction file, updates CLAUDE.md, tests it

---

### Build Your First Custom Instruction Live

Pick a real task. Suggestions:
- "Automate my weekly email newsletter from rough notes"
- "Create a competitor analysis report from a company name"
- "Turn a meeting transcript into action items and follow-ups"

---

### What's Possible: Real Examples from Skalers

At Skalers.io, we build AI systems for 7-9 figure companies. The same model applies at any scale:

```
WHAT WE AUTOMATE AT SKALERS          YOUR VERSION
────────────────────────────────────────────────────────
AI Knowledge Base                  →  context/ files
  (company data → instant             that give your
  answers for any employee)            AI full context

AI Client Acquisition              →  instructions/
  (autonomous outbound that            that automate
  books calls 24/7)                    your outreach

AI Client Fulfillment              →  scripts/ that
  (onboarding, reporting,              pull data + do
  QA, client comms)                    the actual work
```

The difference between a $5K task automation and a $50K+ role automation is scope, but the building blocks are the same. Context. Instructions. Scripts. Outputs.

You're learning the foundation that scales from personal productivity to enterprise systems.

---
---
