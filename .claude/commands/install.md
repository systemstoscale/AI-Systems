# Install Module — $ARGUMENTS

You are installing the "$ARGUMENTS" module. Handle everything — the user only provides API keys when asked and approves file creation.

## Phase 0: Resolve Module

Map the argument to an instruction file. Check both built-in modules and coaching systems:

### Built-in Modules (in template)

| Argument | # | Instruction File |
|----------|---|-----------------|
| context-os | 1 | (built-in — confirm active, remind about /init) |
| daily-brief | 2 | instructions/_example-daily-brief.md |
| data-dashboard | 3 | instructions/_example-data-dashboard.md |
| productivity | 4 | instructions/_example-checkin.md |
| slack-intel | 5 | (inline — needs SLACK_BOT_TOKEN or Composio) |
| meeting-intel | 6 | (inline — needs Google OAuth) |
| email-capture | 7 | (inline — needs Google OAuth) |
| command-center | 8 | instructions/command-center-setup.md |

### The 6 Systems (coaching program, delivered as zip)

| Argument | System | Instruction File |
|----------|--------|-----------------|
| prospecting | The Prospecting System | instructions/prospecting-setup.md |
| content | The Content System | instructions/content-pipeline-setup.md |
| ads | The Acquisition System | instructions/paid-ads-setup.md |
| partners | The Partners System | instructions/partnership-setup.md |
| operations | The Operations System | instructions/operations-setup.md |
| data | The Data System | instructions/data-system-setup.md |

For coaching systems: check if the instruction file exists. If not, the user doesn't have the system yet. Tell them:
```
System not found. The [system name] is part of the coaching program (6 systems, $6K/6 months).

If you already have access:
1. Download the system zip
2. Extract it into this folder (files merge into instructions/ and scripts/)
3. Run /install [system name] again

Learn more: skalers.io
```

If no argument or unrecognized: list available modules (both built-in and add-on) and ask which one.

## Phase 1: Preflight

Run `python scripts/preflight.py --json` if the script exists. If Python is missing or .env doesn't exist, stop and help fix.

Check if module is already installed (script exists + keys set). If yes, ask: "Already installed. Reconfigure?"

## Phase 2: Read Instruction

Read the instruction file. If it has YAML frontmatter (between `---` markers), parse:
- `env_keys.required` and `env_keys.optional` — what API keys are needed
- `pip_packages` — what to install
- `system_packages` — system dependencies (ffmpeg, etc.)
- `test_command` — how to verify it works
- `depends_on` — prerequisite modules

If no frontmatter, extract requirements from the ## Requirements section.

## Phase 3: Dependencies

If `depends_on` lists other modules, check if they're installed. If missing: "This needs [X] first. Install it now?"

## Phase 4: API Keys

For each **required** key:
1. Check if already in `.env`
2. If missing, ask the user — ONE key at a time:
   ```
   I need your [label].
   → Get it here: [get_url]
   → Hint: [hint]

   Paste your key:
   ```
3. Add to `.env` under a section comment (e.g., `# Prospecting`)
4. Validate format if possible (sk_live_, sk-ant-, etc.)

For each **optional** key:
1. Check if already set
2. If missing: "Want to set up [label]? It enables [feature]. You can skip and add later."
3. If skip, move on. Don't push.

## Phase 5: Packages

Install missing pip packages: `pip install [packages]`
Check system packages (e.g., ffmpeg). If missing, show install command for their platform.

## Phase 6: Create Scripts

This is the core. Read the full instruction file and follow its Steps section:

1. For each script listed — check if it already exists
2. If exists: "Script exists. Overwrite or skip?"
3. If not: create it following the instruction's specifications
4. Follow patterns from existing scripts in `scripts/`:
   - Load `.env` with python-dotenv
   - Handle missing env vars gracefully (show "Not configured", don't crash)
   - Include docstring with usage
   - Use `if __name__ == "__main__"` pattern

For modules with `interactive_steps: true`:
- Follow the Steps interactively — ask the user questions from the instruction
- Use answers to customize scripts (e.g., prospecting asks about lead source, niche, offer)

## Phase 7: Test

If `test_command` exists, run it. Show output. If it fails:
1. Read the error
2. Fix the issue
3. Test again
If still failing after 2 attempts, explain what's wrong and how to fix manually.

## Phase 8: Update Registry

Read `context/ai-systems.md` if it exists. Update the module's status to "Configured" or "Active". Write the file.

## Phase 9: Confirm

```
=== [Module Name] Installed ===

Scripts created:
  ✓ scripts/[script-name].py

Environment:
  ✓ API_KEY_NAME (set)
  ○ OPTIONAL_KEY (skipped)

Test: Passed ✓

Next: /status to see all modules
```

## Inline Modules (no instruction file)

### slack-intel
1. Check SLACK_BOT_TOKEN in .env or Composio
2. If neither: ask for token (get at https://api.slack.com/apps) or run `/connect`
3. Verify `scripts/slack-intel.py` exists
4. Test: `python scripts/slack-intel.py`
5. Update registry

### meeting-intel
1. Check Google OAuth (token.json or Composio)
2. If neither: run `/connect` for Google
3. Verify `scripts/meeting-intel.py` exists
4. Test: `python scripts/meeting-intel.py`
5. Update registry

### email-capture
1. Same as meeting-intel but with `scripts/email-capture.py`

## Rules

- **One question at a time.** Never dump a wall of setup steps.
- **Show progress.** "✓ Keys configured. Installing packages..."
- **Be specific about errors.** "STRIPE_SECRET_KEY is missing" not "configuration incomplete"
- **Don't push optional keys** unless the user asks.
- **Recover gracefully.** If a test fails, diagnose and fix.
- **Keep .env organized.** Section comments above each module's keys.
