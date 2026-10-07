"""Root development commands; generated outputs belong in build/."""
import argparse
import json
import os
import py_compile
import subprocess
import sys
import sysconfig
import zipfile
from pathlib import Path
from check_architecture import check, load_manifest

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["install", "build", "test", "test:architecture", "doctor", "lint", "dependencies", "dependencies:json", "check:architecture", "fitness", "fitness:json", "run", "cli", "modules", "health", "version"])
    args, fitness_options = parser.parse_known_args()
    if fitness_options and args.command not in {"fitness", "fitness:json", "doctor", "run", "cli", "modules", "health", "version"}:
        parser.error("Extra options are supported by fitness and CLI commands")
    try:
        if sys.version_info < (3, 11):
            raise ValueError("Python 3.11+ is required")
        if args.command in {"cli", "doctor", "run", "modules", "health", "version"}:
            arguments = ([] if args.command == "cli" else [args.command]) + fitness_options
            os.execve(sys.executable, [sys.executable, str(ROOT / "scripts/platform_cli_launcher.py"), *arguments], os.environ.copy())
        data = load_manifest(ROOT)
        env = os.environ.copy()
        env["PYTHONPATH"] = os.pathsep.join([sysconfig.get_path("stdlib")] + [str(ROOT / m["path"] / "src") for m in data["modules"]] + [str(ROOT / "scripts")])
        def run(*arguments):
            subprocess.run([sys.executable, *arguments], cwd=ROOT, env=env, check=True)
        if args.command == "install":
            print("Ready: standard-library-only workspace; no dependencies to install")
        elif args.command in {"build", "lint"}:
            errors = check(ROOT)
            if errors:
                raise ValueError("\n".join(errors))
            files = sorted(p for family in ("platform", "adapters", "apps", "tools", "scripts", "tests") for p in (ROOT / family).rglob("*.py")) + [ROOT / "bin/platform"]
            for p in files:
                py_compile.compile(str(p), cfile=str(ROOT / "build" / "bytecode" / p.relative_to(ROOT).with_suffix(".pyc")), doraise=True)
                for number, line in enumerate(p.read_text().splitlines(), 1):
                    if line != line.rstrip() or "\t" in line:
                        raise ValueError(f"Whitespace violation: {p.relative_to(ROOT)}:{number}")
            if args.command == "build":
                output = ROOT / "build" / "platform-workspace.zip"
                with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
                    for directory, subdirs, filenames in os.walk(ROOT):
                        subdirs[:] = sorted(d for d in subdirs if d not in {".git", "build", "__pycache__", ".venv"} and not d.startswith("tmp"))
                        for filename in sorted(filenames):
                            p = Path(directory) / filename
                            if not filename.startswith((".env", "local.")):
                                archive.write(p, p.relative_to(ROOT))
                for m in data["modules"]:
                    run("-c", f"from {m['package']}.public import MODULE_NAME; assert MODULE_NAME == {m['name']!r}")
                print(f"Build OK: syntax, boundaries, public imports; {output.relative_to(ROOT)}")
            else:
                print("Lint OK: syntax, whitespace, architecture")
        elif args.command in {"fitness", "fitness:json"}:
            options = ["--format", "json"] if args.command == "fitness:json" else []
            run("-m", "architecture_fitness", *options, *fitness_options)
        elif args.command in {"dependencies", "dependencies:json", "check:architecture"}:
            options = ["--graph"] if args.command != "check:architecture" else []
            if args.command == "dependencies:json":
                options += ["--format", "json"]
            run("scripts/check_architecture.py", *options)
        elif args.command == "test:architecture":
            run("-m", "architecture_fitness")
            run("-m", "unittest", "discover", "-s", "tests/architecture", "-v")
        elif args.command == "test":
            env["PYTHONPATH"] += os.pathsep + str(ROOT / "tests")
            for m in data["modules"]:
                run("-m", "unittest", "discover", "-s", str(Path(m["path"]) / "tests"), "-v")
            for family in ("unit", "architecture", "contracts", "integration", "e2e"):
                if any((ROOT / "tests" / family).glob("test*.py")):
                    run("-m", "unittest", "discover", "-s", f"tests/{family}", "-v")
                else:
                    print(f"Deferred test suite: {family} (no behavior implemented)")
    except subprocess.CalledProcessError as exc:
        print(f"{args.command} failed: {exc}", file=sys.stderr)
        return 1
    except (OSError, ValueError, KeyError, TypeError, py_compile.PyCompileError) as exc:
        print(f"{args.command} failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
