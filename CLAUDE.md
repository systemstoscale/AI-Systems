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

## Your Rules

### Rule 1: Load context first
At the start of every session, read the context files. If the user runs `/context`, follow that command. Otherwise, read `context/` before doing anything else.

### Rule 2: Check before you create
Before writing new code, check `scripts/` for existing scripts and `instructions/` for existing guides. Only create new files when nothing fits.

### Rule 3: Self-correct when things break
When code fails:
1. Read the error message
2. Fix the code
3. Test it again (ask first if it uses paid API credits)
4. Update the instruction file with what you learned

Every failure makes the system smarter.

### Rule 4: Keep instructions updated
When you discover something new - API limits, edge cases, better approaches - update the relevant instruction. They're living documents.

### Rule 5: Save outputs properly
Generated content goes to `outputs/`. Plans go to `instructions/`. Never leave important work in temporary locations.

## Folder Map

| Folder | Purpose |
|--------|---------|
| `context/` | Business info, your role, strategy |
| `instructions/` | Task guides, plans, reference docs |
| `scripts/` | Code - utilities, data fetchers |
| `outputs/` | Generated work - reports, docs, presentations |

## Self-Correction Loop

```
Error → Read error → Fix code → Test → Update instruction → System improved
```

This is what makes the system get smarter over time. Every fix gets documented so the same mistake never happens twice.

## Key Principles

- **Ask before spending money.** Confirm before running paid APIs.
- **One script, one job.** Keep scripts focused and reusable.
- **Local first.** Save to `outputs/` unless told otherwise.

## Commands

- `/setup` - First-time setup: asks you questions, fills in all context files automatically
- `/context` - Load context and orient yourself for the session (run at start of every session)
