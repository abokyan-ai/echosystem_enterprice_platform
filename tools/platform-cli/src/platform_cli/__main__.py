"""In-process platform doctor, without compiler/runtime feature assumptions."""
import argparse
import json
import subprocess
import sys
from pathlib import Path
from platform_cli.internal.registration import REGISTERED_PLATFORM_MODULES
from platform_cli.public import MODULE_NAME


def main():
    parser = argparse.ArgumentParser(prog="platform")
    commands = parser.add_subparsers(dest="command", required=True)
    doctor = commands.add_parser("doctor")
    doctor.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        if sys.version_info < (3, 11):
            raise ValueError("Python 3.11+ is required")
        root = args.root.resolve()
        data = json.loads((root / "architecture.json").read_text())
        subprocess.run([sys.executable, str(root / "scripts/check_architecture.py"), "--root", str(root)], check=True)
        expected = {m["name"] for m in data["modules"]}
        if expected != REGISTERED_PLATFORM_MODULES | {MODULE_NAME}:
            raise ValueError("Module registration mismatch: update the CLI's explicit public registration imports")
        print(f"Doctor OK: Python {sys.version.split()[0]}, configuration, {len(data['modules'])} public modules, dependency wiring")
        return 0
    except (OSError, ValueError, KeyError, TypeError, ImportError, subprocess.CalledProcessError) as exc:
        print(f"Doctor failed: {exc}. Run from the repository using python3 scripts/dev.py doctor.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
