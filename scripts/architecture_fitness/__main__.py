"""Local fitness CLI; filtering is for investigation, CI runs the entire baseline."""
import argparse
import json
from datetime import date, datetime, timezone
from pathlib import Path
from .discovery import discover
from .engine import execute
from .reporting import render


def main():
    parser = argparse.ArgumentParser(prog="architecture-fitness")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--rule", action="append", default=[])
    parser.add_argument("--category")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--as-of", type=date.fromisoformat)
    parser.add_argument("--warnings-as-errors", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        model = discover(args.root)
        report = execute(model, rule_ids=args.rule, category=args.category, as_of=args.as_of, warnings_as_errors=args.warnings_as_errors)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        # Configuration/discovery failures also have a machine-readable, failing result.
        from .model import ArchitectureViolation, Severity
        from dataclasses import asdict
        violation = asdict(ArchitectureViolation("ARCH-CONFIG-001", Severity.ERROR, str(exc), "repository configuration", "fitness harness", "discovery/selection", "Fix configuration, exception metadata or the selected rule/category."))
        report = {"schema_version": 1, "timestamp": datetime.now(timezone.utc).isoformat(), "as_of": (args.as_of or datetime.now(timezone.utc).date()).isoformat(), "rules": [], "results": [{"rule_id": "ARCH-CONFIG-001", "status": "FAIL", "violations": [violation], "duration_ms": 0, "metadata": {}}], "violations": [violation], "exceptions": [], "suppressed_violations": [], "summary": {"status": "FAILED", "modules_scanned": 0, "rules_executed": 0, "passed": 0, "failed": 1, "warnings": 0, "exceptions": 0, "suppressed": 0, "cycles": 0}}
    result = render(report, args.format)
    if args.output:
        try:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(result + "\n")
        except OSError as exc:
            print(json.dumps({"error": f"Cannot write report: {exc}"}) if args.format == "json" else f"Cannot write report: {exc}")
            return 1
    print(result)
    return 1 if report["summary"]["status"] == "FAILED" else 0


if __name__ == "__main__":
    raise SystemExit(main())
