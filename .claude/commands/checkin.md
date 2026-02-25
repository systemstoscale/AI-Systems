# Productivity Check-in

Run a time-aware productivity check-in.

## Steps

1. Determine time of day:
   - Before 11 AM → Morning protocol
   - 11 AM - 5 PM → Midday protocol
   - After 5 PM → Evening protocol

2. **Morning:** Ask about today's intention, top 3 priorities, and energy level. Review yesterday's wins if available.

3. **Midday:** Ask what's been accomplished, what's blocking progress, and what's the most important thing to finish before end of day.

4. **Evening:** Ask for a day rating (1-10), 3 wins, 1 thing to improve, and tomorrow's focus.

5. If `scripts/daily-brief.py` exists, pull any relevant data (goals, tasks, habits) to inform the check-in.

Keep it conversational and brief. The check-in should take less than 2 minutes.
