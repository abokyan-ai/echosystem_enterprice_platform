"""Rule execution, exception matching and severity policy; no filesystem discovery."""
from dataclasses import asdict
from datetime import date, datetime, timezone
from time import perf_counter
from .model import ArchitectureException, ArchitectureRuleResult, ArchitectureViolation, Severity
from .rules import baseline, default_registry


class HarnessError(ValueError):
    pass


def validate_exceptions(exceptions, registry, today):
    known = {rule.id for rule in registry.all()}
    seen = set()
    scopes = set()
    for item in exceptions:
        required = {"id", "rule_id", "source", "target", "reason", "owner", "created_at", "expires_at", "review_issue"}
        if set(item) != required or any(not isinstance(v, str) or not v.strip() for v in item.values()):
            raise HarnessError("Exception has missing/invalid fields")
        if item["id"] in seen or item["rule_id"] not in known:
            raise HarnessError(f"Duplicate exception or unknown rule: {item['id']}")
        if any(any(c in item[k] for c in "*?[]") for k in ("source", "target", "rule_id")):
            raise HarnessError("Exception scope must be exact; wildcards are forbidden")
        try:
            created, expires = date.fromisoformat(item["created_at"]), date.fromisoformat(item["expires_at"])
        except ValueError as exc:
            raise HarnessError("Exception dates must be ISO dates") from exc
        if created > today or expires <= created:
            raise HarnessError("Exception creation/expiry dates are invalid")
        scope = (item["rule_id"], item["source"], item["target"])
        if scope in scopes:
            raise HarnessError("Duplicate exception scope")
        scopes.add(scope)
        seen.add(item["id"])


def execute(model, registry=None, rule_ids=(), category=None, as_of=None, warnings_as_errors=False):
    registry = registry or default_registry()
    today = as_of or datetime.now(timezone.utc).date()
    selected = registry.select(rule_ids, category)
    if not selected:
        raise HarnessError("No rules selected")
    exceptions = tuple(asdict(e) if isinstance(e, ArchitectureException) else e for e in model.exceptions)
    validate_exceptions(exceptions, registry, today)
    context = {}
    results, suppressed = [], []
    dispositions = {e["id"]: {**e, "status": "expired" if date.fromisoformat(e["expires_at"]) <= today else "unmatched", "matches": 0} for e in exceptions}
    exception_errors = []
    for exception in exceptions:
        if dispositions[exception["id"]]["status"] == "expired":
            exception_errors.append(ArchitectureViolation("ARCH-EXC-001", Severity.ERROR, "Architecture exception expired", exception["source"], exception["target"], exception["id"], "Remove the waiver and fix the violation, or review a new narrowly scoped exception."))
    for rule in selected:
        start = perf_counter()
        try:
            findings = list(rule.evaluate(model, context))
            if any(not isinstance(v, ArchitectureViolation) or v.rule_id != rule.id or v.severity != rule.severity for v in findings):
                raise TypeError("Rule returned invalid violation contract/severity/ID")
        except Exception as exc:
            findings = [ArchitectureViolation(rule.id, rule.severity, f"Rule evaluator error: {type(exc).__name__}: {exc}", "rule evaluator", rule.id, "engine", "Fix the evaluator; an evaluator error never becomes a passing rule.")]
            # Evaluator exceptions always fail, including warning-only experimental rules.
            evaluator_failed = True
        else:
            evaluator_failed = False
        active = []
        for violation in sorted(findings, key=lambda v: (v.source, v.target, v.evidence, v.message)):
            match = next((e for e in exceptions if e["rule_id"] == violation.rule_id and e["source"] == violation.source and e["target"] == violation.target and date.fromisoformat(e["expires_at"]) > today), None) if not evaluator_failed else None
            if match:
                disposition = dispositions[match["id"]]
                disposition["status"] = "applied"
                disposition["matches"] += 1
                suppressed.append({"exception_id": match["id"], "violation": asdict(violation)})
            else:
                active.append(violation)
        failure = evaluator_failed or any(v.severity in {Severity.ERROR, Severity.CRITICAL} or (warnings_as_errors and v.severity == Severity.WARNING) for v in active)
        status = "FAIL" if failure else "WARNING" if any(v.severity == Severity.WARNING for v in active) else "PASS"
        results.append(ArchitectureRuleResult(rule.id, status, active, round((perf_counter() - start) * 1000, 3), {"evaluated_violations": len(findings), "suppressed_count": len(findings) - len(active), "evaluator_failed": evaluator_failed}))
    if exception_errors:
        results.append(ArchitectureRuleResult("ARCH-EXC-001", "FAIL", exception_errors, 0.0))
    all_violations = [asdict(v) for result in results for v in result.violations]
    failed = sum(result.status == "FAIL" for result in results)
    graph = baseline(model, context)
    return {
        "schema_version": 1,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "as_of": today.isoformat(),
        "rules": [{"id": rule.id, "name": rule.name, "description": rule.description, "category": rule.category, "severity": rule.severity.value, "scope": rule.scope} for rule in selected],
        "results": [asdict(result) for result in results],
        "violations": all_violations,
        "exceptions": sorted(dispositions.values(), key=lambda e: e["id"]),
        "suppressed_violations": suppressed,
        "architecture": graph,
        "external_dependencies": model.external_inventory(),
        "discovery": model.discovery_metadata,
        "summary": {"status": "FAILED" if failed else "HEALTHY", "modules_scanned": len(model.modules), "rules_executed": len(selected), "passed": sum(r.status == "PASS" for r in results if r.rule_id != "ARCH-EXC-001"), "failed": failed, "warnings": sum(v["severity"] == Severity.WARNING for v in all_violations), "exceptions": len(exceptions), "suppressed": len(suppressed), "cycles": graph["cycle_count"]},
    }
