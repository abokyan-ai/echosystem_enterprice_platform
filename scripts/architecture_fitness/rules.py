"""Central rule registration and reusable graph-based fitness functions."""
from collections import deque
from .governance import evaluate_governance
from .model import ArchitectureRule, ArchitectureViolation, Severity


class RuleRegistry:
    def __init__(self, rules=()):
        self._rules = {}
        for rule in rules:
            self.register(rule)

    def register(self, rule):
        if not rule.id or rule.id in self._rules:
            raise ValueError(f"Duplicate or invalid rule ID: {rule.id}")
        if not all((rule.name, rule.description, rule.category, rule.scope)) or not isinstance(rule.severity, Severity) or not callable(rule.evaluate):
            raise ValueError(f"Incomplete rule contract: {rule.id}")
        self._rules[rule.id] = rule
        return rule

    def all(self):
        return tuple(self._rules[k] for k in sorted(self._rules))

    def select(self, ids=(), category=None):
        unknown = set(ids) - self._rules.keys()
        if unknown:
            raise ValueError(f"Unknown rule ID: {', '.join(sorted(unknown))}")
        if category and category not in {r.category for r in self.all()}:
            raise ValueError(f"Unknown category: {category}")
        return tuple(r for r in self.all() if (not ids or r.id in ids) and (not category or r.category == category))


def baseline(model, context):
    if "baseline" not in context:
        context["baseline"] = evaluate_governance(model)
    return context["baseline"]


def legacy_rule(rule_id, name, category, severity):
    def evaluate(model, context):
        return [ArchitectureViolation(rule_id, severity, v["reason"], v["source"], v["target"], v["location"], v["resolution"], file=v["location"].rsplit(":", 1)[0], line=int(v["location"].rsplit(":", 1)[1]) if ":" in v["location"] and v["location"].rsplit(":", 1)[1].isdigit() else None) for v in baseline(model, context)["violations"] if v["rule_id"] == rule_id]
    return ArchitectureRule(rule_id, name, name, category, severity, "Registered production modules", evaluate)


def forbidden_path_rule(rule_id, name, source_zone, target_zone):
    """Code-owned invariant, independent of a relaxed configuration allowlist."""
    def evaluate(model, context):
        modules = {m.id: m for m in model.modules}
        findings = {}
        for kind in ("declared", "observed"):
            graph = model.graph(kind)
            for source in sorted(m.id for m in model.modules if m.zone == source_zone):
                queue = deque([(source, (source,))])
                visited = {source}
                while queue:
                    current, path = queue.popleft()
                    for target in sorted(graph.get(current, ())):
                        if target not in modules:
                            continue
                        new_path = path + (target,)
                        if modules[target].zone == target_zone:
                            findings.setdefault((source, target, new_path), ArchitectureViolation(rule_id, Severity.CRITICAL, name, source, target, f"{kind} graph: {' -> '.join(new_path)}", "Extract a stable owned contract or invert dependency through a port.", dependency_path=new_path))
                        if target not in visited:
                            visited.add(target)
                            queue.append((target, new_path))
        return list(findings.values())
    return ArchitectureRule(rule_id, name, name, "dependency", Severity.CRITICAL, source_zone, evaluate)


def default_registry():
    registry = RuleRegistry()
    definitions = [
        ("ARCH-DEP-001", "Kernel independence", "dependency", Severity.CRITICAL),
        ("ARCH-DEP-002", "Semantic model independence", "dependency", Severity.CRITICAL),
        ("ARCH-DEP-003", "Compiler direction", "dependency", Severity.CRITICAL),
        ("ARCH-DEP-004", "Runtime authoring independence", "dependency", Severity.CRITICAL),
        ("ARCH-DEP-005", "Compiled contract independence", "dependency", Severity.CRITICAL),
        ("ARCH-DEP-006", "Infrastructure inversion", "dependency", Severity.CRITICAL),
        ("ARCH-DEP-007", "Application direction", "dependency", Severity.CRITICAL),
        ("ARCH-DEP-008", "Experience neutrality", "experience", Severity.CRITICAL),
        ("ARCH-DEP-009", "Frontend contract direction", "experience", Severity.ERROR),
        ("ARCH-DEP-010", "Tooling isolation", "dependency", Severity.ERROR),
        ("ARCH-DEP-011", "Production/test separation", "module", Severity.ERROR),
        ("ARCH-DEP-012", "Specific semantic ownership", "naming", Severity.ERROR),
        ("ARCH-CYCLE-001", "No architectural cycles", "cycle", Severity.CRITICAL),
        ("ARCH-API-001", "Cross-module public API only", "public-api", Severity.CRITICAL),
        ("ARCH-API-002", "Public contract cannot expose local internals", "public-api", Severity.ERROR),
        ("ARCH-ALLOW-001", "Explicit module allowlist", "dependency", Severity.ERROR),
        ("ARCH-EXT-001", "External dependency approval", "external-dependency", Severity.ERROR),
        ("ARCH-REG-001", "Source analyzer and module ownership", "module", Severity.ERROR),
        ("ARCH-SOURCE-001", "Source syntax and relative import validity", "module", Severity.ERROR),
        ("ARCH-DYNAMIC-001", "Static neutral-module imports", "module", Severity.ERROR),
    ]
    for row in definitions:
        registry.register(legacy_rule(*row))
    # ARC-02 IDs retain their established meanings; new precise invariants get FIT IDs.
    for rule_id, name, source, target in [
        ("ARCH-FIT-DEP-001", "Kernel must not depend on Runtime", "kernel", "runtime"),
        ("ARCH-FIT-DEP-002", "Kernel must not depend on Compiler", "kernel", "compiler"),
        ("ARCH-FIT-DEP-003", "Semantic Model must not depend on Runtime", "model", "runtime"),
        ("ARCH-FIT-DEP-004", "Platform must not depend on Adapters", "kernel", "adapter"),
        ("ARCH-FIT-DEP-005", "Platform must not depend on Applications", "kernel", "application"),
        ("ARCH-FIT-DEP-006", "Runtime must not depend on Authoring Model", "runtime", "model"),
    ]:
        if rule_id in {"ARCH-FIT-DEP-004", "ARCH-FIT-DEP-005"}:
            rules = [forbidden_path_rule(rule_id, name, zone, target) for zone in ("kernel", "model", "compiled-contracts", "compiler", "runtime", "experience")]
            registry.register(ArchitectureRule(rule_id, name, name, "dependency", Severity.CRITICAL, "All platform zones", lambda m, c, rs=rules: [v for r in rs for v in r.evaluate(m, c)]))
        else:
            registry.register(forbidden_path_rule(rule_id, name, source, target))
    for new_id, old_id, name, category in [
        ("ARCH-EXP-001", "ARCH-DEP-008", "Experience framework neutrality", "experience"),
        ("ARCH-TEST-001", "ARCH-DEP-011", "No production dependency on tests", "module"),
        ("ARCH-MOD-001", "ARCH-REG-001", "Every source belongs to a governed module", "module"),
    ]:
        old_rule = next(rule for rule in registry.all() if rule.id == old_id)
        def evaluate(model, context, r=old_rule, rule_id=new_id):
            from dataclasses import replace
            return [replace(v, rule_id=rule_id) for v in r.evaluate(model, context)]
        registry.register(ArchitectureRule(new_id, name, name, category, old_rule.severity, old_rule.scope, evaluate))
    def kernel_external(model, context):
        kernels = {m.id for m in model.modules if m.zone == "kernel"}
        old_rule = next(rule for rule in registry.all() if rule.id == "ARCH-EXT-001")
        from dataclasses import replace
        return [replace(v, rule_id="ARCH-EXTDEP-001", severity=Severity.CRITICAL) for v in old_rule.evaluate(model, context) if v.source in kernels]
    registry.register(ArchitectureRule("ARCH-EXTDEP-001", "Restricted kernel dependencies", "Kernel must not depend on infrastructure/framework packages", "external-dependency", Severity.CRITICAL, "kernel", kernel_external))
    return registry
