"""Executable composition boundary and local lifecycle commands."""
import argparse
from dataclasses import asdict
import json
import signal
import subprocess
import sys
import threading
from pathlib import Path
from bootstrap_contracts.public import BootstrapError, HealthStatus
from platform_cli.internal.bootstrap_configuration import load_configuration
from platform_cli.internal.composition import compose_local
from platform_cli.internal.registration import REGISTERED_PLATFORM_MODULES
from platform_cli.public import MODULE_NAME


def main():
    parser = argparse.ArgumentParser(prog="platform")
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("doctor", "run"):
        command = commands.add_parser(name)
        command.add_argument("--root", type=Path, default=Path.cwd())
        command.add_argument("--config", type=Path)
        command.add_argument("--profile", choices=("development", "test", "production"))
        command.add_argument("--modules", help="Comma-separated enabled module IDs; empty selects none")
        if name == "run":
            command.add_argument("--once", action="store_true", help="Start, report health, then stop")
            command.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    try:
        if sys.version_info < (3, 11):
            raise ValueError("Python 3.11+ is required")
        root = args.root.resolve()
        overrides = {}
        if args.profile is not None:
            overrides["profile"] = args.profile
        if args.modules is not None:
            overrides["enabled_modules"] = [m.strip() for m in args.modules.split(",") if m.strip()]
        config_path = args.config or root / "config/development.json"
        if not config_path.is_absolute():
            config_path = root / config_path
        configuration = load_configuration(config_path, overrides=overrides)
        if args.command == "doctor":
            data = json.loads((root / "architecture.json").read_text())
            subprocess.run([sys.executable, str(root / "scripts/check_architecture.py"), "--root", str(root)], check=True)
            expected = {m["name"] for m in data["modules"]}
            if expected != REGISTERED_PLATFORM_MODULES | {MODULE_NAME}:
                raise ValueError("Module registration mismatch: update explicit public registration imports")
            host = compose_local(root, configuration)
            host.dispose()
            print(f"Doctor OK: Python {sys.version.split()[0]}, configuration, {len(data['modules'])} public modules, activation wiring")
            return 0
        def event_sink(event, module):
            print(event + (f": {module}" if module else ""), file=sys.stderr, flush=True)
        host = compose_local(root, configuration, event_sink)
        shutdown = threading.Event()
        previous = {}
        # Install handlers before startup, restore them even when construction/startup fails.
        try:
            if not args.once:
                for sig in (signal.SIGINT, signal.SIGTERM):
                    previous[sig] = signal.getsignal(sig)
                    signal.signal(sig, lambda signum, frame: shutdown.set())
            host.start()
            health = host.health()
            if args.format == "json":
                print(json.dumps({"profile": host.profile, "health": asdict(health), "startup_order": host.order, "startup_ms": host.startup_ms, "module_startup_ms": host.module_startup_ms}, sort_keys=True), flush=True)
            else:
                print(f"Platform {health.status.value}: {len(health.started_modules)} modules; profile={host.profile}; startup={host.startup_ms:.3f}ms", flush=True)
            if not args.once and health.status != HealthStatus.UNHEALTHY:
                shutdown.wait()
            return 1 if health.status == HealthStatus.UNHEALTHY else 0
        finally:
            original = sys.exc_info()[1]
            try:
                host.dispose()
            except BootstrapError as cleanup:
                if isinstance(original, BootstrapError):
                    raise BootstrapError(*original.diagnostics, *cleanup.diagnostics) from original
                raise
            finally:
                for sig, handler in previous.items():
                    signal.signal(sig, handler)
    except BootstrapError as exc:
        print(("Doctor failed: " if args.command == "doctor" else "") + str(exc), file=sys.stderr)
        return 1
    except (OSError, ValueError, KeyError, TypeError, ImportError, subprocess.CalledProcessError) as exc:
        print(f"{args.command} failed: {exc}. Run using python3 scripts/dev.py {args.command}.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
