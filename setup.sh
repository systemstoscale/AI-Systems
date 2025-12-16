#!/bin/bash
# =============================================================================
# IDEA Framework - Project Setup
# Instructions, Decisions, Executions, AI
#
# Creates a complete AI agent development environment
#
# Usage: ./setup.sh [project_name]
#        If no name provided, creates "my-idea-project"
# =============================================================================

set -e

PROJECT_NAME="${1:-my-idea-project}"

echo ""
echo "=============================================="
echo "  IDEA Framework Setup"
echo "  Instructions, Decisions, Executions, AI"
echo "=============================================="
echo ""
echo "Creating project: $PROJECT_NAME"
echo ""

# Create project directory
mkdir -p "$PROJECT_NAME"
cd "$PROJECT_NAME"

# Create folder structure
echo "[1/7] Creating folder structure..."
mkdir -p .claude instructions executions temp

# Create Claude Code settings with comprehensive permissions
echo "[2/7] Configuring Claude Code permissions..."
cat > .claude/settings.json << 'EOF'
{
  "permissions": {
    "allow": [
      "Bash(cat:*)",
      "Bash(cd:*)",
      "Bash(chmod:*)",
      "Bash(cp:*)",
      "Bash(curl:*)",
      "Bash(echo:*)",
      "Bash(find:*)",
      "Bash(git:*)",
      "Bash(grep:*)",
      "Bash(head:*)",
      "Bash(ls:*)",
      "Bash(mkdir:*)",
      "Bash(mv:*)",
      "Bash(node:*)",
      "Bash(npm:*)",
      "Bash(npx:*)",
      "Bash(pip:*)",
      "Bash(pip3:*)",
      "Bash(python:*)",
      "Bash(python3:*)",
      "Bash(rm:*)",
      "Bash(sed:*)",
      "Bash(source:*)",
      "Bash(tail:*)",
      "Bash(touch:*)",
      "Bash(which:*)",
      "Bash(wc:*)",
      "Edit",
      "Read",
      "Write",
      "Glob",
      "Grep",
      "WebFetch",
      "WebSearch"
    ]
  }
}
EOF

# Create .env template
echo "[3/7] Creating environment template..."
cat > .env.example << 'EOF'
# =============================================================================
# Environment Variables
# Copy this file to .env and fill in your values
# =============================================================================

# AI APIs (add the ones you use)
OPENAI_API_KEY=
ANTHROPIC_API_KEY=

# Add your other API keys below
# GOOGLE_API_KEY=
# AIRTABLE_API_KEY=
EOF

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    cp .env.example .env
fi

# Create .gitignore
echo "[4/7] Creating .gitignore..."
cat > .gitignore << 'EOF'
# Secrets - NEVER commit
.env
credentials.json
token.json
*.pem
*.key

# Temporary files
temp/
__pycache__/
*.pyc
.DS_Store

# IDE
.vscode/
.idea/
EOF

# Create CLAUDE.md (the AI's instruction manual)
echo "[5/7] Creating CLAUDE.md..."
cat > CLAUDE.md << 'EOF'
# IDEA Framework
**Instructions, Decisions, Executions, AI**

You are an AI assistant using the IDEA Framework. Your job is to read instructions and run executions—not do everything yourself.

## How It Works

```
instructions/     →     AI (you)     →     executions/
 (what to do)         (decisions)        (does the work)
```

1. **Instructions** (`instructions/`) - Markdown files explaining tasks
2. **AI** - You read instructions, make decisions, run the right executions
3. **Executions** (`executions/`) - Python code that does the actual work

**Why?** AI is smart but inconsistent. Code is reliable. Together = best of both.

## Your Rules

### Rule 1: Check before you create
Before writing code, check `executions/` first. Only create new scripts when needed.

### Rule 2: Self-correct when things break
When code fails:
1. Read the error message
2. Fix the code
3. Test it again (ask first if it uses paid API credits)
4. Update the instruction file with what you learned

### Rule 3: Keep instructions updated
When you discover something new (API limits, edge cases, better approaches), update the instruction file. They're living documents.

## Folder Structure

```
instructions/   → What to do (markdown files)
executions/     → How to do it (Python code)
temp/           → Temporary files (safe to delete)
.env            → API keys (never commit)
```

## Self-Correction Loop

```
Error → Fix code → Test → Update instruction → System improved
```

Every failure makes the system smarter.

## Key Principles

- **Local files are temporary.** Final outputs go to cloud services.
- **Everything in `temp/` can be deleted.** It's scratch space.
- **One script, one job.** Keep executions focused.
- **Ask before spending money.** Confirm before running paid APIs.

## Summary

Read instructions. Make decisions. Run executions. Fix problems. Update instructions.

Be practical. Be reliable. Self-correct.
EOF

# Copy for other AI assistants
cp CLAUDE.md AGENTS.md
cp CLAUDE.md GEMINI.md

# Create instruction template
echo "[6/7] Creating instruction template..."
cat > instructions/_template.md << 'EOF'
# Instruction: [Task Name]

## Goal
[What this accomplishes in 1-2 sentences]

## Inputs
- `input_name` (type): What this is
- `optional_input` (type, optional): What this is

## Execution
`executions/script_name.py`

## Outputs
- What gets created
- Where it's saved

## Requirements
- Required environment variables
- Required Python packages

## Edge Cases
- **[Situation]**: How to handle it

## Notes
- Things learned while using this
EOF

# Create a sample execution script
echo "[7/7] Creating sample execution..."
cat > executions/_example.py << 'EOF'
#!/usr/bin/env python3
"""
Example execution script.
Delete this file once you understand the structure.

Usage:
    python3 executions/_example.py

All executions should:
1. Load environment variables from .env
2. Take clear inputs
3. Produce clear outputs
4. Handle errors gracefully
"""

import os
from pathlib import Path

# Load .env file (requires: pip install python-dotenv)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not installed, using system env vars

def main():
    """Main function - replace with your logic."""
    print("Hello from the IDEA Framework!")
    print(f"Working directory: {Path.cwd()}")

    # Example: reading an env var
    api_key = os.getenv("EXAMPLE_API_KEY", "not-set")
    print(f"EXAMPLE_API_KEY is: {'configured' if api_key != 'not-set' else 'not configured'}")

if __name__ == "__main__":
    main()
EOF

echo ""
echo "=============================================="
echo "  Setup Complete!"
echo "=============================================="
echo ""
echo "Project structure:"
echo ""
echo "  $PROJECT_NAME/"
echo "  ├── .claude/settings.json  → Claude Code permissions"
echo "  ├── .env                   → Your API keys (fill this in)"
echo "  ├── .env.example           → Template for .env"
echo "  ├── .gitignore             → Protects secrets"
echo "  ├── temp/                  → Temporary working files"
echo "  ├── CLAUDE.md              → AI instructions"
echo "  ├── instructions/          → What to do (task guides)"
echo "  │   └── _template.md       → Template for new instructions"
echo "  └── executions/            → How to do it (Python code)"
echo "      └── _example.py        → Sample script (delete when ready)"
echo ""
echo "Next steps:"
echo ""
echo "  1. cd $PROJECT_NAME"
echo "  2. Fill in your API keys in .env"
echo "  3. Open in Antigravity or VS Code"
echo "  4. Start Claude Code and begin building!"
echo ""
echo "Optional: Install python-dotenv for .env support:"
echo "  pip install python-dotenv"
echo ""
