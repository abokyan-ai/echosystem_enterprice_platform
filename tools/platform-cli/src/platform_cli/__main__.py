"""In-process platform doctor, without compiler/runtime feature assumptions."""
import argparse
import importlib
import json
import subprocess
import sys
from pathlib import Path


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
        for module in data["modules"]:
            public = importlib.import_module(module["package"] + ".public")
            if public.MODULE_NAME != module["name"]:
                raise ValueError(f"Module registration mismatch: {module['name']}")
        print(f"Doctor OK: Python {sys.version.split()[0]}, configuration, {len(data['modules'])} public modules, dependency wiring")
        return 0
    except (OSError, ValueError, KeyError, TypeError, ImportError, subprocess.CalledProcessError) as exc:
        print(f"Doctor failed: {exc}. Run from the repository using python3 scripts/dev.py doctor.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
