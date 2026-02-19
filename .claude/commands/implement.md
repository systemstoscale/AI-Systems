# Implement

Execute an implementation plan. If $ARGUMENTS matches a filename in `instructions/`, read that plan. Otherwise, find the most recent plan file in `instructions/` (files starting with `plan-`).

## For Each Step in the Plan

1. **Announce** what you are about to do
2. **Check** if an instruction or script already exists for this step
3. **Execute** the step:
   - If an instruction exists: follow it
   - If creating a new instruction: use the template from `instructions/_template.md`
   - If creating a script: save it to `scripts/`
   - If generating content: save to `outputs/`
4. **Verify** the step worked — run the code, check the output, validate
5. **Self-correct** if something fails:
   - Read the error
   - Fix the code
   - Test again
   - Update the instruction with what you learned
6. **Mark complete** and move to the next step

## When Done

- Update the plan file with completion status
- List all files created or modified
- Summarize what was accomplished
