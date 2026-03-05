# Connect — Link External Tools

You are helping the user connect their external tools (Gmail, Calendar, Slack, etc.) via Composio or manual API setup.

## Steps

1. Run `python scripts/connections.py status` to see what's currently connected.

2. Show the results to the user in a clear format:
   - Which tools are connected (and how — Composio or Direct API)
   - Which tools are not connected

3. Ask: **"Which tool would you like to connect? (Google, Slack, or skip)"**

4. If they choose a tool:

   **If COMPOSIO_API_KEY is set in .env:**
   - Run `python scripts/connections.py connect <provider>` (e.g., `google` or `slack`)
   - This opens a browser for OAuth — tell them to complete authorization
   - Confirm when connected

   **If COMPOSIO_API_KEY is NOT set:**
   - Ask: "Do you have a Composio account? You can get a free one at https://composio.dev"
   - If yes: Ask them to add `COMPOSIO_API_KEY=<their-key>` to `.env`, then run the connect command
   - If no/skip: Guide them through the direct API setup:
     - **Google**: "Follow the instructions in `scripts/email-capture.py` header — you'll need a Google Cloud Console project with Gmail + Calendar APIs enabled"
     - **Slack**: "Create a Slack app at api.slack.com/apps, add bot scopes (channels:history, channels:read), install to workspace, and set `SLACK_BOT_TOKEN` in `.env`"

5. After connecting, run `python scripts/connections.py status` again to verify.

6. Say: **"Tool connected! Your AI Systems modules (Email Capture, Meeting Intelligence, etc.) will now use this connection automatically."**

## Important
- Don't force Composio — some users prefer direct API keys
- If they say "skip" or "later", that's fine — remind them they can run `/connect` anytime
- This command can be run multiple times — it's additive
