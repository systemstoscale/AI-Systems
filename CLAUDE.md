# AI Systems

Your personal AI workspace. Context, instructions, scripts, outputs - everything your AI needs to do real work.

You are an AI system working in a structured workspace. Think of this like your first day at a job - read your onboarding docs, understand your role, then get to work.

## How This Workspace Works

```
context/       →  instructions/  →  scripts/   →  outputs/
(who you are)     (what to do)      (how)         (results)
```

1. **Context** (`context/`) - Your onboarding. Who the user is, their business, goals, and current data.
2. **Instructions** (`instructions/`) - Task guides, plans, reference docs. Everything you need to do the work.
3. **Scripts** (`scripts/`) - Code that does the actual work. Python, Node, shell - whatever fits.
4. **Outputs** (`outputs/`) - Where finished work goes. Reports, docs, presentations, data.

## Session Start

At the start of every session (or when `/context` is run):

1. Read `context/business.md`, `context/personal.md`, `context/strategy.md`
2. Read `context/lessons.md` — review patterns to avoid repeating mistakes
3. Read `context/todo.md` — check what's in progress and what's next
4. Scan `instructions/` and `scripts/` for available tools
5. Respond with: who you're working for, current priority, open tasks, then ask what to work on

## Your Rules

### Rule 1: Load context first
Always run through the Session Start steps above. Never skip `lessons.md` or `todo.md` — they contain critical patterns and the current task state.

### Rule 2: Plan before acting
For any task with 3+ steps or architectural decisions, write a plan to `context/todo.md` before starting. Check it off as you go.

### Rule 3: Self-correct when things break
When code fails:
1. Read the error message
2. Fix the code
3. Test it again (ask first if it uses paid API credits)
4. Add the pattern to `context/lessons.md` so it never happens again

Every failure makes the system smarter.

### Rule 4: Check before you create
Before writing new code, check `scripts/` for existing scripts and `instructions/` for existing guides. Only create new files when nothing fits.

### Rule 5: Keep context current
When something changes during a session, update the relevant file immediately:
- New pattern discovered → update `context/lessons.md`
- Task completed or added → update `context/todo.md`
- New tool or API quirk → update the relevant instruction file

### Rule 6: Save outputs properly
Generated content goes to `outputs/`. Plans go to `context/todo.md`. Never leave important work in a temporary location.

## Folder Map

| Path | Purpose |
|------|---------|
| `context/business.md` | Company, product, tech stack |
| `context/personal.md` | Your name, role, preferences |
| `context/strategy.md` | Goals, priorities, what's NOT a priority |
| `context/todo.md` | Active tasks — in progress, up next, done |
| `context/lessons.md` | Patterns learned — API quirks, fixes, rules |
| `instructions/` | Task guides, plans, reference docs |
| `scripts/` | Code — utilities, data fetchers, automations |
| `outputs/` | Generated work — reports, docs, data |

## Self-Improvement Loop

```
Error → Read error → Fix code → Test → Update lessons.md → System improved
Task done → Mark complete in todo.md → Keep context current
```

This is what makes the system get smarter over time. Every fix is captured in `context/lessons.md` so the same mistake never happens twice. Every session starts with the accumulated knowledge of every previous session.

## Key Principles

- **Ask before spending money.** Confirm before running paid APIs.
- **One script, one job.** Keep scripts focused and reusable.
- **Local first.** Save to `outputs/` unless told otherwise.

## Commands

- `/setup` - First-time setup: asks you questions, fills in all context files automatically
- `/context` - Load context, check tasks, orient for the session (run at start of every session)
