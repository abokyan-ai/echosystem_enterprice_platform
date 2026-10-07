"""Source-checkout launcher: set registered paths and replace this process with CLI."""
import json
import os
from pathlib import Path
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    try:
        data = json.loads((root / "architecture.json").read_text())
        env = os.environ.copy()
        env["PYTHONPATH"] = os.pathsep.join([str(root / m["path"] / "src") for m in data["modules"]] + [str(root / "scripts")])
        os.execve(sys.executable, [sys.executable, "-m", "platform_cli", *sys.argv[1:]], env)
    except (OSError, ValueError, KeyError, TypeError):
        print("CLI-LAUNCH-001 [ERROR] Source checkout paths are unavailable; run from a complete checkout.", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
