#!/usr/bin/env python3
"""
Preflight Check — Verify system prerequisites for AI Systems.

Usage:
    python scripts/preflight.py          # Pretty print
    python scripts/preflight.py --json   # JSON output
"""

import sys
import os
import json
import subprocess
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def check_python():
    v = sys.version_info
    ver = f"{v.major}.{v.minor}.{v.micro}"
    if v >= (3, 12):
        return {"status": "ok", "version": ver, "note": "All modules supported"}
    elif v >= (3, 9):
        return {"status": "warn", "version": ver, "note": "Command Center needs 3.12+"}
    else:
        return {"status": "fail", "version": ver, "note": "Minimum 3.9 required"}


def check_node():
    if not shutil.which("node"):
        return {"status": "warn", "version": None, "note": "Not found (optional)"}
    try:
        r = subprocess.run(["node", "--version"], capture_output=True, text=True, timeout=5)
        return {"status": "ok", "version": r.stdout.strip(), "note": ""}
    except Exception:
        return {"status": "warn", "version": None, "note": "Found but version check failed"}


def check_env():
    env_path = ROOT / ".env"
    if not env_path.exists():
        return {"status": "fail", "keys": [], "note": "No .env file. Copy .env.example to .env"}
    keys = []
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            if v.strip():
                keys.append(k.strip())
    if not keys:
        return {"status": "warn", "keys": [], "note": ".env exists but no keys configured"}
    return {"status": "ok", "keys": keys, "note": f"{len(keys)} keys configured"}


def check_context():
    results = {}
    for name in ["business.md", "personal.md", "strategy.md"]:
        path = ROOT / "context" / name
        if not path.exists():
            results[name] = {"status": "fail", "note": "Missing"}
            continue
        content = path.read_text()
        words = len(content.split())
        if words < 30:
            results[name] = {"status": "warn", "note": "Looks like a template — run /setup"}
        else:
            results[name] = {"status": "ok", "note": f"{words} words"}
    return results


def check_package(pkg):
    import_map = {
        "python-dotenv": "dotenv",
        "claude-agent-sdk": "claude_agent_sdk",
        "Pillow": "PIL",
    }
    try:
        __import__(import_map.get(pkg, pkg.replace("-", "_")))
        return True
    except ImportError:
        return False


def check_composio():
    key = os.getenv("COMPOSIO_API_KEY")
    if not key:
        return {"status": "not_configured", "note": "COMPOSIO_API_KEY not set"}
    return {"status": "configured", "note": "Key set — run /connect to link tools"}


def check_google_oauth():
    if (ROOT / "token.json").exists():
        return {"status": "ok", "note": "token.json found"}
    if os.getenv("COMPOSIO_API_KEY"):
        return {"status": "maybe", "note": "Composio configured — run /connect to verify"}
    return {"status": "not_configured", "note": "No token.json or Composio"}


def check_system_pkg(name, cmd):
    if not shutil.which(name):
        return {"status": "missing", "note": f"{name} not found"}
    try:
        r = subprocess.run(cmd.split(), capture_output=True, text=True, timeout=5)
        line = (r.stdout or r.stderr).split("\n")[0].strip()[:60]
        return {"status": "ok", "note": line}
    except Exception:
        return {"status": "ok", "note": "Found"}


def run(json_output=False):
    # Try loading .env
    try:
        from dotenv import load_dotenv
        load_dotenv(ROOT / ".env")
    except ImportError:
        pass

    results = {
        "python": check_python(),
        "node": check_node(),
        "env": check_env(),
        "context": check_context(),
        "composio": check_composio(),
        "google_oauth": check_google_oauth(),
        "packages": {
            p: check_package(p)
            for p in ["python-dotenv", "requests", "stripe", "aiogram", "claude-agent-sdk"]
        },
        "system": {
            "ffmpeg": check_system_pkg("ffmpeg", "ffmpeg -version"),
        },
    }

    if json_output:
        print(json.dumps(results, indent=2))
        return results

    icon = {"ok": "✓", "warn": "~", "fail": "✗", "missing": "✗",
            "not_configured": "○", "configured": "✓", "maybe": "~"}

    print("=== Preflight Check ===\n")

    py = results["python"]
    print(f"  {icon[py['status']]} Python: {py['version']}  {py['note']}")

    nd = results["node"]
    print(f"  {icon[nd['status']]} Node: {nd['version'] or 'not found'}  {nd['note']}")

    env = results["env"]
    print(f"  {icon[env['status']]} .env: {env['note']}")

    print("\n  Context files:")
    for fname, info in results["context"].items():
        print(f"    {icon[info['status']]} {fname}: {info['note']}")

    comp = results["composio"]
    goog = results["google_oauth"]
    print(f"\n  {icon[comp['status']]} Composio: {comp['note']}")
    print(f"  {icon[goog['status']]} Google OAuth: {goog['note']}")

    print("\n  Packages:")
    for pkg, ok in results["packages"].items():
        print(f"    {'✓' if ok else '○'} {pkg}")

    ffmpeg = results["system"]["ffmpeg"]
    print(f"\n  {icon[ffmpeg['status']]} ffmpeg: {ffmpeg['note']}")

    # Summary
    fails = sum(1 for v in [py, nd, env] if v.get("status") == "fail")
    print()
    if fails:
        print(f"  {fails} issue(s) to fix before installing modules.")
    else:
        print("  Ready to install modules. Run /status to see available modules.")

    return results


if __name__ == "__main__":
    run(json_output="--json" in sys.argv)
