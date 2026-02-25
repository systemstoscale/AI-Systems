# Create Plan

Create a detailed implementation plan for: $ARGUMENTS

## Steps

1. **Understand the goal** — What is the user trying to accomplish? Ask clarifying questions if unclear.
2. **Check existing resources**:
   - Search `instructions/` for relevant task guides
   - Search `scripts/` for existing code that could help
   - Search `context/` for relevant business context
3. **Identify what exists vs. what needs to be created**
4. **Break into numbered steps** — Each step should have a clear deliverable
5. **Estimate complexity** — Simple (minutes) / Medium (under an hour) / Complex (multiple sessions)

## Output

Save the plan to `instructions/plan-[descriptive-name].md` with this structure:

```
# Plan: [Title]
Created: [date]

## Goal
[1-2 sentences]

## Existing Resources
- [List any existing instructions or scripts that apply]

## Steps
1. [Step with clear deliverable]
2. [Step with clear deliverable]
...

## New Files Needed
- [List any new instructions or scripts to create]

## Questions
- [Anything that needs clarification before implementing]
```

After saving, display the plan and tell the user: "Ready to implement? Run `/implement`"
