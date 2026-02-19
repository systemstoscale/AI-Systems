# Instruction: Weekly Status Report

## Goal
Generate a weekly status report summarizing project progress, team hours, blockers, and priorities for the coming week. This report is shared with leadership every Monday morning.

## Inputs
- `week_ending` (date, optional): The Friday date for the reporting week. Defaults to the most recent Friday.
- `project_updates` (text): A rough list of what happened on each active project this week. Can be bullet points, notes, or even a brain dump — the AI will organize it.
- `hours_data` (text, optional): Hours logged per project. If not provided, the report will include a placeholder for manual entry.
- `blockers` (text, optional): Anything slowing down progress.

## Steps
1. **Ask for inputs** — If the user has not provided project updates, ask: "What happened on each active project this week? Just give me rough notes and I will organize them."
2. **Review context** — Read `context/strategy.md` to check current goals and metrics. The report should tie progress back to strategic priorities.
3. **Organize updates by project** — Group the raw notes into a section per active project with:
   - What was accomplished
   - Current status (On Track / At Risk / Blocked)
   - Next steps
4. **Compile the report** using this structure:
   ```
   # Weekly Status Report — Week Ending [date]

   ## Highlights
   - [Top 2-3 wins or milestones from the week]

   ## Project Updates
   ### [Project Name]
   - **Status**: On Track / At Risk / Blocked
   - **Completed**: [What got done]
   - **Next Steps**: [What happens next week]
   (repeat for each project)

   ## Hours Summary
   | Project | Hours | Notes |
   |---------|-------|-------|
   | [name]  | [hrs] | [notes] |

   ## Blockers
   - [List anything slowing progress, with suggested resolution]

   ## Lowlights
   - [Things that did not go well or need attention]

   ## Next Week Priorities
   1. [Priority 1]
   2. [Priority 2]
   3. [Priority 3]

   ## Metrics Check
   - Client onboarding time: [current] (target: 7 days)
   - Client NPS: [current] (target: 85+)
   - Consultant utilization: [current] (target: 75%)
   ```
5. **Save the report** to `outputs/weekly-report-[YYYY-MM-DD].md` using the week-ending date in the filename.
6. **Display a summary** — After saving, show the user the Highlights and Next Week Priorities sections so they can quickly review before sharing.

## Script
No script required. This is a text-generation task handled entirely by the AI.

## Output
- Markdown file saved to `outputs/weekly-report-[YYYY-MM-DD].md`

## Requirements
- Context files must be filled in (at minimum `context/strategy.md` for metrics and goals)

## Edge Cases
- **User provides very sparse notes**: Ask follow-up questions for each project rather than guessing. Example: "You mentioned the onboarding project — what specifically happened this week?"
- **No hours data available**: Include the Hours Summary table with "TBD" entries and note at the top that hours need to be filled in manually.
- **No blockers**: Replace the Blockers section with "No blockers reported this week."
- **First report ever**: If there are no previous reports in `outputs/`, skip any comparison to prior weeks. Mention this is the first report in the series.

## Notes
- Keep language clear and professional. Leadership reads this quickly — short sentences, no jargon.
- The Metrics Check section should pull targets from `context/strategy.md`. If metrics have been updated, use the latest values.
- If previous weekly reports exist in `outputs/`, reference them to note trends (e.g., "Onboarding time improved from 18 days to 14 days since last report").
