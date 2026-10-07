"""ARC-02 policy evaluation preserved over a shared discovered model, without I/O."""
import sys
from dataclasses import asdict
from architecture_source import Violation, cycles

def evaluate_governance(model):
    data = {"modules": [m.metadata for m in model.modules]}
    policy = model.policy
    modules = {m["name"]: m for m in data["modules"]}
    packages = {m["package"]: m for m in modules.values()}
    zones = policy["zones"]
    declared = {name: set(m["allowed_dependencies"]) for name, m in modules.items()}
    observed = {name: set() for name in modules}
    external = {name: set() for name in modules}
    violations = set()

    def fail(rule, source, target, location, reason, resolution="Use an explicitly owned public contract or invert through a port."):
        violations.add(Violation(rule, source, target, location, reason, resolution))

    def edge(owner, target, location):
        source, destination = owner["name"], target["name"]
        if source == destination:
            return
        if destination not in declared[source]:
            fail("ARCH-ALLOW-001", source, destination, location, "Undeclared module dependency", "Declare a permitted API edge; never add an edge merely to bypass a zone rule.")
        if target["zone"] not in zones[owner["zone"]]["allowed_zones"]:
            rule = zones[owner["zone"]]["rule_id"]
            if owner["zone"] not in {"adapter", "application", "tooling"}:
                rule = {"adapter": "ARCH-DEP-006", "application": "ARCH-DEP-007", "tooling": "ARCH-DEP-010"}.get(target["zone"], rule)
            fail(rule, source, destination, location, "Forbidden architectural zone dependency")
        profile = policy.get("profiles", {}).get(owner.get("technology_profile"))
        if profile and target["zone"] not in profile["allowed_zones"]:
            fail("ARCH-DEP-009" if owner.get("technology_profile") == "angular-primeng" else "ARCH-DEP-006", source, destination, location, "Adapter profile must depend only on its designated platform contracts")
        if owner["dependency_categories"].get(destination) == "test":
            fail("ARCH-DEP-011", source, destination, location, "Production module declares a test dependency", "Keep test-only dependencies in tests outside production source.")
        if owner["zone"] not in {"adapter", "application", "tooling"} and owner["dependency_categories"].get(destination) in {"implementation", "adapter", "development"}:
            fail("ARCH-API-001", source, destination, location, "Neutral module dependency must be an API/optional contract")

    for name, m in sorted(modules.items()):
        if name in policy["generic_names"] or m["package"] in policy["generic_names"]:
            fail("ARCH-DEP-012", name, name, "architecture.json", "Generic dumping-ground module name", "Assign a specific semantic owner and contract name.")
        for target in sorted(declared[name]):
            edge(m, modules[target], "architecture.json")
        for prefix in m["external_dependencies"]:
            approval = policy["external_dependencies"].get(prefix)
            if not approval or m["zone"] not in approval["allowed_zones"] or m.get("technology_profile") != approval["profile"] or not m["path"].startswith(approval["path_prefix"]):
                fail("ARCH-EXT-001", name, prefix, "architecture.json", "External dependency approval/profile/ownership mismatch", "Approve a narrowly owned dependency at its framework/adapter boundary.")
    for description in cycles(declared):
        fail("ARCH-CYCLE-001", "declared graph", description, "architecture.json", description, "Extract a contract, invert a dependency or move ownership; remove the cycle.")

    for source in model.sources:
        location = source.file
        if source.issue:
            fail("ARCH-REG-001" if source.issue_kind == "registration" else "ARCH-SOURCE-001", source.owner or location, "module registration" if source.issue_kind == "registration" else location, location, source.issue, "Register a source analyzer/owner or fix invalid source syntax.")
            continue
        owner = modules[source.owner]
        targets = source.targets
        for target, line in targets:
            first = target.split(".")[0]
            at = f"{location}:{line}"
            if any(part in {"tests", "fixtures", "test_utils", "mocks"} or part.startswith("test_") for part in target.split(".")) or first == "unittest":
                fail("ARCH-DEP-011", owner["name"], target, at, "Production code depends on test code", "Move the import to a test tree. Production mock-data adapters are not test fixtures.")
            if first in packages:
                dependency = packages[first]
                if dependency["name"] != owner["name"]:
                    observed[owner["name"]].add(dependency["name"])
                    edge(owner, dependency, at)
                    if target != dependency["public_api"][0]:
                        fail("ARCH-API-001", owner["name"], target, at, "Public API violation", f"Import only {dependency['public_api'][0]} and explicitly exported public names.")
            elif first in sys.stdlib_module_names or first == "__future__":
                allowed = zones[owner["zone"]]["stdlib"]
                if "*" not in allowed and first not in allowed:
                    fail(zones[owner["zone"]]["rule_id"], owner["name"], target, at, "Standard-library capability not approved in neutral zone", "Keep parsing, networking, persistence and framework integration in their owning boundaries.")
            else:
                external[owner["name"]].add(first)
                if first not in owner["external_dependencies"]:
                    fail("ARCH-EXT-001", owner["name"], target, at, "Unapproved external import", "Declare and approve the dependency in the owning module/profile; keep framework types out of neutral contracts.")
                if owner["zone"] not in {"adapter", "application", "tooling"}:
                    fail(zones[owner["zone"]]["rule_id"], owner["name"], target, at, "Framework/infrastructure leakage into a neutral zone")
        if owner["zone"] not in {"adapter", "application", "tooling"}:
            for call, line in source.dynamic_calls:
                fail("ARCH-DYNAMIC-001", owner["name"], call, f"{location}:{line}", "Dynamic code/import forbidden in neutral module", "Use static public imports so the dependency graph can be checked.")
        if location.endswith("/public.py"):
            # Prevent leaking a local internal class via a public alias or annotated import.
            for target, line in targets:
                if target.startswith(owner["package"] + ".") and target != owner["package"] + ".public":
                    fail("ARCH-API-002", owner["name"], target, f"{location}:{line}", "Public contract imports local implementation", "Define contract types in the public surface; keep implementation behind contracts.")
    for description in cycles(observed):
        fail("ARCH-CYCLE-001", "observed graph", description, "source imports", description, "Invert dependencies through independent contracts.")
    return {
        "schema_version": 1,
        "modules": [{"module": name, "zone": m["zone"], "owner": m["owner"], "public_api": m["public_api"], "declared_dependencies": sorted(declared[name]), "observed_dependencies": sorted(observed[name]), "observed_external_imports": sorted(external[name]), "dependency_categories": m["dependency_categories"]} for name, m in sorted(modules.items())],
        "violations": [asdict(v) for v in sorted(violations)],
        "cycle_count": len(cycles(declared)) + len(cycles(observed)),
    }
