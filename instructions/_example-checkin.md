# Instruction: Productivity Check-in

## Goal
Run a time-aware productivity check-in that reviews habits, goals, and tasks — then generates a focused action plan for the rest of the day.

## Command
`/checkin`

## When to Run
- **Morning** (before 11 AM) — Set intentions and priorities
- **Midday** (11 AM - 5 PM) — Progress check, unblock, refocus
- **Evening** (after 5 PM) — Day review, log wins, plan tomorrow

## Protocols

### Morning Check-in
1. Read `context/data.md` for current metrics and goals
2. Review yesterday's completed tasks (if tracked)
3. Ask:
   - What's the #1 priority today?
   - What are the top 3 tasks to complete?
   - Energy level (1-10)?
   - Any blockers or concerns?
4. Output: Today's focus plan with prioritized task list

### Midday Check-in
1. Review morning priorities
2. Ask:
   - What's been accomplished so far?
   - What's blocking progress?
   - Is the #1 priority still the right priority?
   - What's the most important thing to finish before end of day?
3. Output: Adjusted priorities with time recommendations

### Evening Check-in
1. Review the day's planned vs actual accomplishments
2. Ask:
   - Rate the day (1-10)
   - List 3 wins (big or small)
   - What's 1 thing that could have gone better?
   - What's the #1 focus for tomorrow?
3. Log results to `context/data.md` (update metrics)
4. Output: Day summary with tomorrow's top priority

## Data Sources
- `context/data.md` — Current metrics, goals, habit streaks
- `context/strategy.md` — Priorities and focus areas
- Task management tool (if integrated)

## Output Format
Markdown displayed in terminal. Optionally saved to `outputs/checkins/` for tracking patterns over time.

## Tips
- Keep each check-in under 2 minutes
- Be honest with ratings — patterns matter more than individual scores
- Track energy levels to find your peak hours
- Review weekly to spot trends (best days, common blockers)

## Customization
Edit the questions to match your workflow:
- Add habit tracking (e.g., "Did you exercise?", "Did you read?")
- Add revenue check (pull from Stripe via `scripts/fetch-metrics.py`)
- Add health data (OURA readiness, sleep score)
