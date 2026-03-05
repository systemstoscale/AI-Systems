# Composio Setup — Universal Tool Connections

## Goal
Connect external tools (Gmail, Calendar, Slack, etc.) via Composio's one-click OAuth instead of manual API key setup.

## Inputs
- Composio account (free at https://composio.dev)
- COMPOSIO_API_KEY from the Composio dashboard

## Steps

### 1. Create a Composio Account
1. Go to https://composio.dev and sign up (free tier: 1,000 actions/month)
2. Navigate to your dashboard settings
3. Copy your API key

### 2. Add API Key to Environment
Add to your `.env` file:
```
COMPOSIO_API_KEY=your_key_here
```

### 3. Connect Providers
Run the connection command for each tool you want:

```bash
# Connect Google (Gmail + Calendar + Drive)
python scripts/connections.py connect google

# Connect Slack
python scripts/connections.py connect slack
```

Each command opens your browser for OAuth authorization. Complete the flow and the connection is stored.

### 4. Verify Connections
```bash
python scripts/connections.py status
```

Should show connected tools and their status.

### 5. Test Modules
```bash
# Test Email Capture
python scripts/email-capture.py --count 5

# Test Meeting Intelligence
python scripts/meeting-intel.py

# Test Slack Intelligence
python scripts/slack-intel.py --hours 24
```

Each module automatically detects Composio connections and uses them.

## Script
`scripts/connections.py` — the connection adapter

## Output
Connected external tools available to all AI Systems modules.

## Requirements
- `COMPOSIO_API_KEY` in `.env`
- Internet access for OAuth flow
- Browser to complete authorization

## Edge Cases
- **No COMPOSIO_API_KEY**: Scripts fall back to direct API keys (credentials.json, SLACK_BOT_TOKEN)
- **Expired OAuth token**: Composio handles token refresh automatically. If it fails, run `python scripts/connections.py connect <provider>` again
- **Rate limits**: Composio free tier allows 1,000 actions/month. Upgrade if needed at composio.dev/pricing

## Notes
- Composio is optional. All modules work with direct API keys too.
- Each provider connection is independent — connecting Google doesn't affect Slack.
- Run `/connect` anytime to add or check tool connections.
