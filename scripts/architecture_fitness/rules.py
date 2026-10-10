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
    contract_rule = legacy_rule("ARCH-BOOT-CONTRACT-001", "Hosting contracts remain independent", "dependency", Severity.CRITICAL)
    contract_paths = [forbidden_path_rule("ARCH-BOOT-CONTRACT-001", "Hosting contracts remain independent", "bootstrap-contracts", target) for target in ("kernel", "model", "compiled-contracts", "compiler", "runtime", "experience", "adapter", "application", "tooling")]
    registry.register(ArchitectureRule("ARCH-BOOT-CONTRACT-001", "Hosting contracts remain independent", "Independent hosting contracts", "dependency", Severity.CRITICAL, "bootstrap-contracts", lambda m, c: contract_rule.evaluate(m, c) + [v for r in contract_paths for v in r.evaluate(m, c)]))
    for rule_id, name, target in (
        ("ARCH-BOOT-002", "Adapter selection belongs to outer composition boundaries", "adapter"),
        ("ARCH-BOOT-003", "Core must not depend on bootstrap implementation/tooling", "tooling"),
        ("ARCH-BOOT-004", "Platform must not depend on applications", "application"),
    ):
        rules = [forbidden_path_rule(rule_id, name, zone, target) for zone in ("kernel", "model", "compiled-contracts", "compiler", "runtime", "experience", "bootstrap-contracts")]
        registry.register(ArchitectureRule(rule_id, name, name, "dependency", Severity.CRITICAL, "All platform zones", lambda m, c, rs=rules: [v for r in rs for v in r.evaluate(m, c)]))
    cli_paths = [forbidden_path_rule("ARCH-CLI-001", "Platform core must not depend on CLI/tooling", zone, "tooling") for zone in ("kernel", "model", "compiled-contracts", "compiler", "runtime", "experience", "bootstrap-contracts")]
    registry.register(ArchitectureRule("ARCH-CLI-001", "Core/CLI direction", "Core cannot depend on CLI/tooling", "dependency", Severity.CRITICAL, "All platform zones", lambda m, c: [v for r in cli_paths for v in r.evaluate(m, c)]))
    def cli_public(model, context):
        from dataclasses import replace
        return [replace(v, rule_id="ARCH-CLI-002") for v in legacy_rule("ARCH-API-001", "CLI public imports", "public-api", Severity.CRITICAL).evaluate(model, context) if v.source == "platform-cli"]
    registry.register(ArchitectureRule("ARCH-CLI-002", "CLI uses public contracts", "CLI cross-module imports use only public surfaces", "public-api", Severity.CRITICAL, "platform-cli", cli_public))
    def cli_adapter(model, context):
        adapters = {m.metadata["package"]: m for m in model.modules if m.zone == "adapter"}
        findings = []
        for source in model.sources:
            if source.owner != "platform-cli":
                continue
            for target, line in source.targets:
                owner = adapters.get(target.split(".")[0])
                if owner and target not in owner.public_api:
                    findings.append(ArchitectureViolation("ARCH-CLI-003", Severity.CRITICAL, "CLI must not import adapter internals", source.owner, owner.id, target, "Inject the adapter's public contract from the composition root.", file=source.file, line=line))
        return findings
    registry.register(ArchitectureRule("ARCH-CLI-003", "No CLI adapter internals", "CLI must use public adapter contracts", "public-api", Severity.CRITICAL, "platform-cli", cli_adapter))
    def semantic_id_owner(model, context):
        return [ArchitectureViolation("ARCH-SK-001", Severity.CRITICAL, "SemanticElementId definitions belong to semantic-kernel", source.owner or "unregistered", "semantic-kernel", "class SemanticElementId", "Use semantic_kernel.public.SemanticElementId; do not duplicate its definition.", file=source.file, line=line) for source in model.sources for name, line in source.classes if name == "SemanticElementId" and source.owner != "semantic-kernel"]
    registry.register(ArchitectureRule("ARCH-SK-001", "Semantic identity ownership", "SemanticElementId class definitions belong to Semantic Kernel", "module", Severity.CRITICAL, "Production class declarations", semantic_id_owner))
    kernel_paths = [forbidden_path_rule("ARCH-SK-002", "Semantic Kernel must remain independent of non-kernel modules", "kernel", target) for target in ("model", "compiled-contracts", "compiler", "runtime", "experience", "adapter", "application", "tooling", "bootstrap-contracts")]
    registry.register(ArchitectureRule("ARCH-SK-002", "Semantic identity independence", "Kernel must not depend on non-kernel modules", "dependency", Severity.CRITICAL, "kernel", lambda m, c: [v for r in kernel_paths for v in r.evaluate(m, c)]))
    def kernel_public(model, context):
        from dataclasses import replace
        public_files = {s.file for s in model.sources if s.owner == "semantic-kernel" and s.file.endswith("/public.py")}
        prohibited = {"ARCH-API-001", "ARCH-API-002", "ARCH-EXT-001", "ARCH-DEP-001", "ARCH-DEP-004", "ARCH-DEP-005", "ARCH-DEP-006", "ARCH-DEP-007", "ARCH-DEP-010"}
        findings = []
        for finding in baseline(model, context)["violations"]:
            filename = finding["location"].rsplit(":", 1)[0]
            if finding["source"] == "semantic-kernel" and filename in public_files and finding["rule_id"] in prohibited:
                violation = legacy_rule(finding["rule_id"], "Kernel public dependency", "public-api", Severity.CRITICAL)
                findings.extend(replace(v, rule_id="ARCH-SK-003") for v in violation.evaluate(model, context) if v.source == "semantic-kernel" and v.file == filename and v.target == finding["target"])
        return list({(v.file, v.line, v.target, v.message): v for v in findings}.values())
    registry.register(ArchitectureRule("ARCH-SK-003", "Kernel public contract neutrality", "Kernel public source must not import forbidden infrastructure or internal surfaces", "public-api", Severity.CRITICAL, "semantic-kernel public.py", kernel_public))
    def namespace_owner(model, context):
        return [ArchitectureViolation("ARCH-SK-NS-001", Severity.CRITICAL, "Namespace definitions belong to semantic-kernel", source.owner or "unregistered", "semantic-kernel", "class Namespace", "Use semantic_kernel.public.Namespace; do not duplicate its definition.", file=source.file, line=line) for source in model.sources for name, line in source.classes if name == "Namespace" and source.owner != "semantic-kernel"]
    registry.register(ArchitectureRule("ARCH-SK-NS-001", "Semantic namespace ownership", "Namespace class definitions belong to Semantic Kernel", "module", Severity.CRITICAL, "Production class declarations", namespace_owner))
    def qualified_name_owner(model, context):
        return [ArchitectureViolation("ARCH-SK-QN-001", Severity.CRITICAL, "QualifiedName definitions belong to semantic-kernel", source.owner or "unregistered", "semantic-kernel", "class QualifiedName", "Use semantic_kernel.public.QualifiedName; do not duplicate its definition.", file=source.file, line=line) for source in model.sources for name, line in source.classes if name == "QualifiedName" and source.owner != "semantic-kernel"]
    registry.register(ArchitectureRule("ARCH-SK-QN-001", "Qualified semantic name ownership", "QualifiedName class definitions belong to Semantic Kernel", "module", Severity.CRITICAL, "Production class declarations", qualified_name_owner))
    return registry
