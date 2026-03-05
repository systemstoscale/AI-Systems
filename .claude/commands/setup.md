# Setup — Interactive Workspace Onboarding

You are setting up this workspace for a new user. Your job is to interview them, then fill in all their context files automatically.

## How This Works

Ask questions in **4 short rounds**. After each round, immediately write the answers to the correct file. Keep it conversational — like onboarding a new team member.

## Round 1: Business Context → writes to `context/business.md`

Ask all of these in ONE message:
1. What's your company or project name?
2. What do you do in 1-2 sentences? (What problem do you solve?)
3. What industry are you in?
4. What stage are you at? (Pre-revenue / Growing / Established)
5. What are your main products or services? (List them briefly)
6. Who do you serve? (Your customers/audience)
7. What's their biggest pain point?
8. What tools/platforms do you use? (Tech stack)
9. Any key links? (Website, social, etc.)

After they answer: Write their responses into `context/business.md` using the existing template structure. Keep their words — don't over-polish.

## Round 2: Personal Context → writes to `context/personal.md`

Ask all of these in ONE message:
1. What's your name?
2. What's your role/title?
3. How much coding experience do you have? (None / Beginner / Intermediate / Advanced)
4. How do you prefer communication? (Brief and direct / Detailed explanations / Step-by-step)
5. What output format do you prefer? (Markdown / Plain text / Slides / Other)
6. Should I ask before taking actions, or move fast? (Ask first / Move fast / Somewhere in between)
7. What will you mainly use this workspace for? (List 2-3 things)
8. Any pet peeves? Things you hate seeing in AI output? (e.g., filler phrases, generic intros, emoji overuse)

After they answer: Write their responses into `context/personal.md`.

## Round 3: Strategy Context → writes to `context/strategy.md`

Ask all of these in ONE message:
1. What's your #1 priority right now? (1-2 sentences)
2. What are your top 2-3 goals? (Include timeframes if you have them)
3. Any active projects? (What's in progress and what's the next step?)
4. What key metrics do you track? (With current values if you know them)
5. What's NOT a priority right now? (Things I should ignore or deprioritize)

After they answer: Write their responses into `context/strategy.md` with today's date.

## Round 4: Data Context (Optional) → writes to `context/data.md`

Ask in ONE message:
1. Do you have any current metrics or data you want me to know about? (Analytics, revenue, followers, pipeline — anything relevant)
2. Where does this data come from? (Google Analytics, CRM, manual tracking, etc.)

If they say "skip" or "none" or "not right now" — leave `context/data.md` as the default template and move on.

After they answer: Write their responses into `context/data.md`.

## Round 5: Tool Connections (Optional) → uses `scripts/connections.py`

Ask in ONE message:
1. Want to connect your external tools? This lets your AI Systems read your Gmail, check your calendar, and pull Slack summaries automatically.
2. You can connect via **Composio** (one-click OAuth, recommended) or set up API keys manually later.
3. Available tools: **Google** (Gmail + Calendar), **Slack**

If they want Composio:
1. Ask if they have a Composio account (free at https://composio.dev)
2. Have them set `COMPOSIO_API_KEY` in `.env`
3. Run `python scripts/connections.py connect google` for Google
4. Run `python scripts/connections.py connect slack` for Slack

If they want to skip:
Say "No problem — you can connect tools later anytime with `/connect`."

## Round 6: Command Center (Optional) → `instructions/command-center-setup.md`

Ask in ONE message:
1. Do you want to access your AI Systems from your phone via Telegram?
2. This gives you a Telegram bot that has full access to your workspace — chat, voice notes, photo analysis, charts, and PDFs.
3. It requires: a Telegram account, an Anthropic API key, and Python 3.12+.

If they want it:
1. Walk them through `instructions/command-center-setup.md` step by step
2. Help them create the bot, group, get the group ID
3. Set env vars in `.env`
4. Install dependencies and test startup

If they want to skip:
Say "No problem — you can set up the Command Center later. Follow `instructions/command-center-setup.md` when you're ready."

## After All Rounds

1. Read back a brief summary of everything you captured — 4-5 bullet points max
2. Run the init workflow: read all context files, scan instructions and scripts
3. Respond with the standard init output:
   - Who you're working for (1 sentence)
   - Current top priority (1 sentence)
   - Available tools (list of instructions and scripts)
   - Connected tools (if any were set up in Round 5)
4. Then say: **"Your AI system is set up and ready. What would you like to work on?"**

## Important Rules

- Ask each round as ONE message with all questions numbered. Don't drip-feed questions one at a time.
- Write to the files IMMEDIATELY after each round — don't wait until the end.
- Use the user's actual words. Don't rewrite their answers into corporate language.
- If an answer is vague, use it anyway. They can refine later.
- Keep the energy practical and fast — this should feel like 5 minutes, not a bureaucratic form.
