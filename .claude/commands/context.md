# Context — Session Initialization

You are starting a new session. Get up to speed.

## Steps

1. **Read context files** in `context/`:
   - `business.md` — company, product, tech stack
   - `personal.md` — who you're working for, preferences
   - `strategy.md` — current goals and priorities

2. **Sync tasks and patterns**:
   - Read `context/lessons.md` — patterns to avoid repeating mistakes
   - Read `context/todo.md` — open items and what's in progress

3. **Scan available skills**:
   - List folders in `.claude/skills/` (reusable workflows)

## Response

After reading, respond with:
- **Who you're working for** (1 sentence)
- **Current top priority** (from strategy)
- **Open tasks** (from todo.md, if any)
- **Recent lessons** (from lessons.md, if any)
- **Available skills** (skills found in `.claude/skills/`)
- Then ask: **"What would you like to work on?"**

Keep it brief. Do NOT dump the full contents of every file.
