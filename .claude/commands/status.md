# Status — Module Dashboard

Show the user what's installed, what's available, and how to install each module.

## Steps

1. **Run preflight** — `python scripts/preflight.py --json` to get system status.

2. **Check each module's actual state** by verifying:
   - Do the script files exist?
   - Are the required env keys set in `.env`?
   - Is Google OAuth configured? (check for `token.json` or Composio)

3. **Read `context/ai-systems.md`** for the registry status column.

4. **Scan `instructions/` for YAML frontmatter** — files starting with `---` contain module metadata. Parse `module_id`, `env_keys`, and `scripts` fields.

5. **Display the dashboard** in this exact format:

```
=== AI Systems Status ===

System:
  Python: 3.12.1 ✓  |  Node: 20.11.0 ✓
  Composio: ✓ Connected  |  Google OAuth: ✓ Connected

Core Modules:
  1. Context OS         ✓ Active                    /init
  2. Daily Brief        ○ Not configured             /install daily-brief
  3. Data Dashboard     ○ Not configured             /install data-dashboard
  4. Productivity       ✓ Active                    /checkin
  5. Slack Intel        ○ Missing: SLACK_BOT_TOKEN   /install slack-intel
  6. Meeting Intel      ○ Missing: Google OAuth      /connect
  7. Email Capture      ○ Missing: Google OAuth      /connect
  8. Command Center     ○ Not configured             /install command-center

Business Modules:
  9.  Prospecting       ○ Not configured             /install prospecting
  10. Content Pipeline  ○ Not configured             /install content
  11. Paid Ads          ○ Not configured             /install ads
  12. Image Generation  ○ Not configured             /install images
  13. Video Creation    ○ Not configured             /install video
  14. Partnerships      ○ Not configured             /install partners
  15. Operations        ○ Not configured             /install ops

Run /install <module> to set up any module.
```

## Status Logic

- **✓ Active** — Scripts exist AND required env keys set
- **✓ Configured** — Scripts exist, partially set up (some optional keys missing)
- **○ Missing: [KEY]** — Specific missing requirement
- **○ Not configured** — Scripts don't exist yet

## Rules

- Use ✓ for working, ○ for not working
- Be specific about what's missing — show the key name or connection needed
- Always show the command to fix it
- Keep it to one screen — no scrolling
- Don't read instruction file contents, just check file existence and env keys
