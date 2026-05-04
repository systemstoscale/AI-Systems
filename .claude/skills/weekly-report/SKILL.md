# Weekly Business Report

Generate a weekly summary of what happened, what's working, and what to focus on next week.

## Inputs
- Current week (auto-detected from today's date)
- Key metrics to include (from `context/strategy.md`)

## Steps

1. Read `context/todo.md` — note what was completed this week, what's still open, and what's blocked.

2. Read `context/strategy.md` — review current goals and priorities.

3. Read `context/lessons.md` — note any patterns or fixes logged this week.

4. Pull any available metrics (check `outputs/` for recent data files and read what exists).

5. Write the report:
   - **This week:** what was completed (pull from todo.md done items)
   - **What's working:** wins, momentum, positive signals
   - **What needs attention:** open blockers, at-risk items
   - **Focus for next week:** top 3 priorities based on strategy.md
   - **Metrics snapshot:** key numbers (use whatever data is available)

6. Save to `outputs/weekly-report-[date].md`.

7. Update `context/todo.md`:
   - Move completed items from "In Progress" to "Done"
   - Add next week's top priorities to "Up Next"

## Output

`outputs/weekly-report-[YYYY-MM-DD].md` — concise, scannable, built for a 5-minute Friday review.
