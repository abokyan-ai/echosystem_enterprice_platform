"""Stable machine fields and useful human diagnostics (without business validation)."""
import json


def render_violation(v):
    lines = [f"{v['rule_id']} [{v['severity']}] {v['message']}", f"  From: {v['source']}", f"  To: {v['target']}", f"  Evidence: {v['evidence']}", f"  Resolution: {v['suggested_resolution']}"]
    if v.get("dependency_path"):
        lines.append("  Path: " + " -> ".join(v["dependency_path"]))
    return "\n".join(lines)


def render(report, format="text"):
    if format == "json":
        return json.dumps(report, indent=2, sort_keys=True)
    if format != "text":
        raise ValueError(f"Unknown report format: {format}")
    summary = report["summary"]
    lines = ["Architecture Fitness Report", f"Modules scanned: {summary['modules_scanned']}", f"Rules executed: {summary['rules_executed']}", f"Passed: {summary['passed']} | Failed: {summary['failed']} | Warnings: {summary['warnings']}", f"Exceptions: {summary['exceptions']} | Suppressed: {summary['suppressed']} | Cycles: {summary['cycles']}"]
    for result in report["results"]:
        lines.append(f"{result['rule_id']}: {result['status']}")
    lines.extend(render_violation(v) for v in report["violations"])
    for exception in report["exceptions"]:
        lines.append(f"Exception {exception['id']}: {exception['status']} ({exception['rule_id']}, {exception['source']} -> {exception['target']}, expires {exception['expires_at']})")
    for suppressed in report["suppressed_violations"]:
        lines.append(f"SUPPRESSED by {suppressed['exception_id']}:\n{render_violation(suppressed['violation'])}")
    lines.append(f"Architecture Status: {summary['status']}")
    return "\n".join(lines)
