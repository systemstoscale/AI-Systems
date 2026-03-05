---
module_id: command-center
module_name: Command Center
module_number: 8
category: core
description: Telegram bot for mobile access to AI Systems
env_keys:
  required:
    - key: COMMAND_CENTER_BOT_TOKEN
      label: Telegram Bot Token
      get_url: https://t.me/BotFather
      hint: "Send /newbot to @BotFather, choose a name and username, copy the token"
    - key: COMMAND_CENTER_GROUP_ID
      label: Telegram Group ID
      get_url: null
      hint: "Create a group, add the bot, enable Topics, get ID via invite link"
    - key: ANTHROPIC_API_KEY
      label: Anthropic API Key
      get_url: https://console.anthropic.com/settings/keys
      hint: "Starts with sk-ant-"
  optional: []
pip_packages: [aiogram, python-dotenv, markdown, openai, matplotlib, claude-agent-sdk]
python_version: "3.12+"
test_command: null
estimated_time: "15 minutes"
interactive_steps: true
---

# Command Center Setup Guide (Module #8: Mobile Access)

Your AI Systems, accessible from your phone via Telegram.

---

## Prerequisites

- **Python 3.12+** (union types, match statements require 3.11+)
- **Anthropic API key** (in `.env.shared` as `ANTHROPIC_API_KEY`)
- **Telegram account** on your phone

---

## Step 1: Create Telegram Bot

1. Open Telegram, search for **@BotFather**
2. Send `/newbot`
3. Choose a **display name** (e.g., "My AI Systems")
4. Choose a **username** (must end in `bot`, e.g., `mycompany_ai_bot`)
5. Copy the **bot token** (looks like `1234567890:AAE...`)

## Step 2: Create Telegram Group

1. Create a new Telegram group (name it whatever you want, e.g., "HQ")
2. Add your bot to the group
3. **Enable Topics**: Group Settings → Topics → On

## Step 3: Configure Bot Settings (CRITICAL)

These two settings are **required** or the bot won't receive messages:

### 3a. Disable Group Privacy
1. Open @BotFather
2. Send `/mybots` → select your bot
3. **Bot Settings** → **Group Privacy** → **Turn off**

> Without this, the bot only sees `/commands`, not regular messages.

### 3b. Promote Bot to Admin
1. In your group, tap the group name → **Members**
2. Find your bot → **Promote to Admin**
3. Save (no special permissions needed, just the admin role)

> In topic-enabled groups, non-admin bots cannot receive messages at all.

### 3c. Re-add Bot After Privacy Change
If you changed Group Privacy after the bot was already in the group:
1. **Remove** the bot from the group
2. **Re-add** the bot
3. **Promote to admin** again

> The privacy setting change only takes effect for groups joined AFTER the change.

## Step 4: Get Group ID

1. Send any message in the group
2. Visit: `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`
3. Look for `"chat": {"id": -100XXXXXXXXXX}` — that's your group ID
4. If the result is empty, make sure the bot is admin and Group Privacy is OFF

**Shortcut**: If your invite link is `t.me/c/1234567890/1`, your group ID is `-1001234567890` (prefix `-100` + the number).

## Step 5: Set Environment Variables

Add to your `.env.shared` (or `.env`):

```
COMMAND_CENTER_BOT_TOKEN=your-bot-token-here
COMMAND_CENTER_GROUP_ID=-100your-group-id-here
```

## Step 6: Install Dependencies

```bash
python3.12 -m venv .venv
.venv/bin/pip install aiogram python-dotenv markdown openai matplotlib claude-agent-sdk
```

Optional (for PDF reports):
```bash
.venv/bin/pip install weasyprint
```

## Step 7: Create Data Directory

```bash
mkdir -p data/command/photos
```

## Step 8: Test Startup

```bash
.venv/bin/python3.12 run_command_center.py
```

You should see:
```
SKALERS COMMAND CENTER v1.0
✓ Config loaded
✓ Log directory
✓ Telegram (@your_bot_username)
Online — polling for messages
```

Send a message in your Telegram group. The first message takes ~30 seconds (priming the workspace context). Subsequent messages are faster (~10-15s).

## Step 9: Keep Running (Optional)

### macOS (launchd)

Create `~/Library/LaunchAgents/com.command-center.bot.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.command-center.bot</string>
    <key>ProgramArguments</key>
    <array>
        <string>/path/to/your/workspace/.venv/bin/python3.12</string>
        <string>/path/to/your/workspace/run_command_center.py</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/path/to/your/workspace</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/path/to/your/workspace/data/command/bot.log</string>
    <key>StandardErrorPath</key>
    <string>/path/to/your/workspace/data/command/bot.log</string>
</dict>
</plist>
```

Load it:
```bash
launchctl load ~/Library/LaunchAgents/com.command-center.bot.plist
```

### Linux (systemd)

Create `/etc/systemd/system/command-center.service`:

```ini
[Unit]
Description=AI Systems Command Center
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/path/to/your/workspace
ExecStart=/path/to/your/workspace/.venv/bin/python3.12 run_command_center.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable command-center
sudo systemctl start command-center
```

---

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Bot doesn't receive messages | Group Privacy is ON | Disable in @BotFather → Bot Settings → Group Privacy |
| Still no messages after privacy change | Bot was in group before the change | Remove and re-add bot to group |
| Empty `getUpdates` result | Bot is not admin in topic-enabled group | Promote bot to admin |
| `TelegramConflictError` on startup | Another instance is already polling | Kill all `run_command_center.py` processes |
| First message takes 30+ seconds | Normal — agent is priming workspace context | Wait; subsequent messages are faster |
| `weasyprint` import error | Not installed | `pip install weasyprint` (optional, only for PDF reports) |
| `CLAUDECODE` env var conflict | Running bot inside Claude Code session | Bot auto-removes this var on startup |

---

## How It Works

1. **You send a message** in the Telegram group
2. **Bot batches** rapid-fire messages (1.5s debounce window)
3. **First message primes** the agent — reads CLAUDE.md, business context, strategy (costs ~$0.02-0.10)
4. **Agent runs** your request with full workspace access (file read/write, web search, scripts)
5. **Response delivered** as Telegram message, file, photo, or PDF depending on length/content
6. **Session persists** — agent remembers prior conversation within the topic

### Commands
- Message in **General topic** → persistent agent with full context
- `/reboot` → restart the bot process
