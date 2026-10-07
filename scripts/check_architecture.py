"""ARC-02 compatible commands backed by ARC-03 shared discovery/evaluation."""
import argparse
import json
import sys
from pathlib import Path
from architecture_source import ArchitectureError, Violation, cycles, import_targets, load_manifest
from architecture_fitness.discovery import discover
from architecture_fitness.governance import evaluate_governance
from architecture_fitness.engine import execute
from architecture_fitness.reporting import render_violation


def analyze(root):
    return evaluate_governance(discover(root))

def check(root):
    report = execute(discover(root))
    return [render_violation(v) for v in report["violations"]] if report["summary"]["status"] == "FAILED" else []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--graph", action="store_true")
    args = parser.parse_args()
    try:
        fitness = execute(discover(args.root))
        report = fitness["architecture"]
        report["violations"] = [{"rule_id": v["rule_id"], "source": v["source"], "target": v["target"], "location": v["evidence"], "reason": v["message"], "resolution": v["suggested_resolution"]} for v in fitness["violations"]]

    except (OSError, ValueError, KeyError, TypeError) as exc:
        if args.format == "json":
            print(json.dumps({"error": str(exc), "rule_id": "ARCH-CONFIG-001"}, sort_keys=True))
        else:
            print(f"Architecture configuration error: {exc}", file=sys.stderr)
        return 1
    if args.format == "json":
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        if args.graph:
            for module in report["modules"]:
                print(f"{module['module']} [{module['zone']}] | observed: {', '.join(module['observed_dependencies']) or '-'} | declared: {', '.join(module['declared_dependencies']) or '-'}")
        for v in report["violations"]:
            print(Violation(**v).render(), file=sys.stderr)
        print(f"Architecture {'FAILED' if report['violations'] else 'OK'}: {len(report['modules'])} modules, {len(report['violations'])} dependency violations, {report['cycle_count']} cycles detected")
    return 1 if report["violations"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
