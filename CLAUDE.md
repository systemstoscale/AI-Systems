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
2. Read `context/lessons.md` - review patterns to avoid repeating mistakes
3. Read `context/todo.md` - check what's in progress and what's next
4. Scan `.claude/skills/` for available skills
5. Respond with: who you're working for, current priority, open tasks, then ask what to work on

## How You Work

### 1. Plan First
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- Write the plan to `context/todo.md` with checkable items before starting
- If something goes sideways, STOP and re-plan immediately. Do not keep pushing.
- Write detailed specs upfront to reduce ambiguity

### 2. Use Subagents
- Offload research, exploration, and parallel analysis to subagents
- One task per subagent for focused execution
- Keep the main context window clean

### 3. Self-Improvement Loop
- After ANY correction: update `context/lessons.md` with the pattern
- Write rules that prevent the same mistake from happening again
- Review `context/lessons.md` at session start

### 4. Verify Before Done
- Never mark a task complete without proving it works
- Run tests, check logs, demonstrate correctness
- Ask yourself: "Would a staff engineer approve this?"

### 5. Demand Elegance
- For non-trivial changes: pause and ask "is there a more elegant way?"
- Skip this for simple, obvious fixes - do not over-engineer

### 6. Autonomous Bug Fixing
- When given a bug report: just fix it
- Point at logs, errors, failing tests, then resolve them
- Zero context switching required from the user

## Your Rules

### Rule 1: Load context first
Always run through the Session Start steps above. Never skip `lessons.md` or `todo.md` - they contain critical patterns and the current task state.

### Rule 2: Plan before acting
Enter plan mode for any task with 3+ steps. Write the plan to `context/todo.md`. Check items off as you go. If the plan breaks down mid-execution, stop and re-plan.

### Rule 3: Connect external data the right way
When pulling data from outside the workspace, always follow this pattern:

```
1. Credentials go in .env (API key, OAuth token, or credentials file)
2. Script fetches the data and saves it to outputs/
3. Instruction reads outputs/ and processes it
4. Report saved back to outputs/
```

This applies to every external tool: Google Drive, Sheets, Calendar, Stripe, Airtable, any API. Never hardcode credentials. Never skip saving the raw data to `outputs/` first.

### Rule 4: Self-correct when things break
When code fails:
1. Read the error message
2. Fix the code
3. Test it again (ask first if it uses paid API credits)
4. Add the pattern to `context/lessons.md` so it never happens again

Every failure makes the system smarter.

### Rule 5: Check before you create
Before writing new code, check `.claude/skills/` for existing skills. Only create new files when nothing fits.

### Rule 6: Keep context current
When something changes during a session, update the relevant file immediately:
- New pattern discovered → update `context/lessons.md`
- Task completed or added → update `context/todo.md`
- New tool or API quirk → update the relevant skill file

### Rule 7: Save outputs properly
Generated content goes to `outputs/`. Plans go to `context/todo.md`. Never leave important work in a temporary location.

## Folder Map

| Path | Purpose |
|------|---------|
| `context/business.md` | Company, product, tech stack |
| `context/personal.md` | Your name, role, preferences |
| `context/strategy.md` | Goals, priorities, what's NOT a priority |
| `context/todo.md` | Active tasks: in progress, up next, done |
| `context/lessons.md` | Patterns learned: API quirks, fixes, rules |
| `.claude/skills/` | Reusable workflows — each skill is a task guide Claude runs on demand |
| `outputs/` | Generated work: reports, docs, data |

## Self-Improvement Loop

```
Error → Read error → Fix code → Test → Update lessons.md → System improved
Task done → Mark complete in todo.md → Keep context current
```

Every fix is captured in `context/lessons.md` so the same mistake never happens twice. Every session starts with the accumulated knowledge of every previous session.

## Key Principles

- **Ask before spending money.** Confirm before running paid APIs.
- **One script, one job.** Keep scripts focused and reusable.
- **Local first.** Save to `outputs/` unless told otherwise.
- **Simplicity first.** Make every change as simple as possible. Minimal code impact.
- **No laziness.** Find root causes. No temporary fixes. Senior developer standards.

## Commands

- `/setup` - First-time setup: asks you questions, fills in all context files automatically
- `/context` - Load context, check tasks, orient for the session (run at start of every session)
