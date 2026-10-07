"""Deterministic AST dependency governance for the registered Python workspace."""
import argparse
import ast
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


class ArchitectureError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Violation:
    rule_id: str
    source: str
    target: str
    location: str
    reason: str
    resolution: str

    def render(self):
        return (f"{self.rule_id}: {self.reason}\n"
                f"  From: {self.source}\n  To: {self.target}\n"
                f"  Location: {self.location}\n  Resolution: {self.resolution}")


def read_json(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError) as exc:
        raise ArchitectureError(f"ARCH-CONFIG-001: Cannot read {path.name}: {exc}") from exc


def load_manifest(root):
    root = root.resolve()
    data = read_json(root / "architecture.json")
    policy = read_json(root / "architecture-policy.json")
    try:
        if data["schema_version"] != 2 or policy["schema_version"] != 1:
            raise ValueError("Unsupported manifest/policy schema version")
        modules, zones = data["modules"], policy["zones"]
        if not modules or not zones:
            raise ValueError("Modules and zones must not be empty")
        if any(set(z["allowed_zones"]) - set(zones) for z in zones.values()):
            raise ValueError("Unknown zone in policy")
        names, packages, paths = set(), set(), []
        for m in modules:
            if not isinstance(m["name"], str) or not m["name"] or m["name"] in names:
                raise ValueError("Duplicate or missing module name")
            if not m["package"].isidentifier() or m["package"] in packages or m["package"] in sys.stdlib_module_names:
                raise ValueError(f"Invalid, duplicate or stdlib-shadowing package: {m['package']}")
            if m["zone"] not in zones or m["language"] != "python" or not m["owner"].strip():
                raise ValueError(f"Invalid zone, language or owner: {m['name']}")
            profile = policy.get("profiles", {}).get(m.get("technology_profile"))
            if m.get("technology_profile") and (not profile or profile["zone"] != m["zone"] or not m["path"].startswith(profile["path_prefix"])):
                raise ValueError(f"Technology profile/ownership mismatch: {m['name']}")
            path = root / m["path"]
            if Path(m["path"]).is_absolute() or ".." in Path(m["path"]).parts or not path.resolve().is_relative_to(root):
                raise ValueError(f"Module path escapes repository: {m['name']}")
            if not m["path"].startswith(zones[m["zone"]]["path_prefix"]):
                raise ValueError(f"Zone/path mismatch: {m['name']}")
            if any(path.resolve().is_relative_to(p) or p.is_relative_to(path.resolve()) for p in paths):
                raise ValueError(f"Overlapping module paths: {m['name']}")
            if m["public_api"] != [m["package"] + ".public"]:
                raise ValueError(f"Public surface must be package.public: {m['name']}")
            if not (path / "src" / m["package"] / "public.py").is_file():
                raise ValueError(f"Missing public entry point: {m['name']}")
            if not isinstance(m["allowed_dependencies"], list) or len(set(m["allowed_dependencies"])) != len(m["allowed_dependencies"]):
                raise ValueError(f"Invalid dependency allowlist: {m['name']}")
            if not isinstance(m["external_dependencies"], list):
                raise ValueError(f"Invalid external dependency list: {m['name']}")
            names.add(m["name"])
            packages.add(m["package"])
            paths.append(path.resolve())
        for m in modules:
            if set(m["allowed_dependencies"]) - names:
                raise ValueError(f"Unknown dependencies: {m['name']}")
            categories = m["dependency_categories"]
            if set(categories) != set(m["allowed_dependencies"]) or any(c not in {"api", "implementation", "development", "test", "adapter", "optional"} for c in categories.values()):
                raise ValueError(f"Dependency categories must cover every edge: {m['name']}")
        exceptions = read_json(root / "docs/architecture/dependency-exceptions.json")
        if exceptions != {"schema_version": 1, "exceptions": []}:
            raise ValueError("Exceptions require reviewed enforcement changes; this baseline permits no waivers")
    except (KeyError, TypeError, AttributeError, ValueError) as exc:
        raise ArchitectureError(f"ARCH-CONFIG-001: {exc}") from exc
    return data


def cycles(graph):
    visited, active, errors = set(), [], []
    def visit(name):
        if name in active:
            errors.append("Circular dependency: " + " -> ".join(active[active.index(name):] + [name]))
            return
        if name in visited:
            return
        active.append(name)
        for dependency in sorted(graph.get(name, [])):
            visit(dependency)
        active.pop()
        visited.add(name)
    for name in sorted(graph):
        visit(name)
    return errors


def import_targets(tree, package, relative_file):
    """Yield resolved absolute import paths and lines, including nested/type-only imports."""
    context = [package, *relative_file.parts[:-1]]
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                yield alias.name, node.lineno
        elif isinstance(node, ast.ImportFrom):
            base = node.module or ""
            if node.level:
                if node.level > len(context):
                    raise ArchitectureError(f"Invalid relative import on line {node.lineno}")
                base = ".".join(context[:len(context)-node.level+1] + ([base] if base else []))
            # from package.public import Symbol resolves the public module, not a submodule.
            yield base, node.lineno
            if not base.endswith(".public"):
                for alias in node.names:
                    yield base + "." + alias.name, node.lineno
            elif any(alias.name.startswith("_") or alias.name == "*" for alias in node.names):
                yield base + ".__private_export__", node.lineno


def analyze(root):
    root = root.resolve()
    data = load_manifest(root)
    policy = read_json(root / "architecture-policy.json")
    modules = {m["name"]: m for m in data["modules"]}
    packages = {m["package"]: m for m in modules.values()}
    zones = policy["zones"]
    registered = {m["name"]: (root / m["path"] / "src" / m["package"]).resolve() for m in modules.values()}
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

    for family in ("platform", "adapters", "apps", "tools"):
        for path in sorted((root / family).rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts:
                continue
            parts = path.relative_to(root).parts
            if path.suffix not in {".py", ".ts", ".tsx", ".js", ".jsx", ".dart"}:
                continue
            # Module test trees are not shipped as production source; src/*/tests is production.
            if any(path.is_relative_to(root / m["path"] / "tests") for m in modules.values()):
                continue
            location = str(path.relative_to(root))
            resolved = path.resolve()
            if not resolved.is_relative_to(root):
                fail("ARCH-REG-001", location, "outside repository", location, "Source symlink escapes repository")
                continue
            owner = next((modules[n] for n, directory in registered.items() if resolved.is_relative_to(directory)), None)
            if owner is None or path.suffix != ".py":
                fail("ARCH-REG-001", location, "module registration", location, "Unregistered source or unsupported production language", "Register ownership and a language analyzer before adding production code.")
                continue
            try:
                tree = ast.parse(path.read_text(), filename=location)
                targets = list(import_targets(tree, owner["package"], resolved.relative_to(registered[owner["name"]])))
            except (SyntaxError, ArchitectureError) as exc:
                fail("ARCH-SOURCE-001", owner["name"], location, location, str(exc), "Fix source syntax or the invalid relative import.")
                continue
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
                for node in ast.walk(tree):
                    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in {"__import__", "exec", "eval"}:
                        fail("ARCH-DYNAMIC-001", owner["name"], node.func.id, f"{location}:{node.lineno}", "Dynamic code/import forbidden in neutral module", "Use static public imports so the dependency graph can be checked.")
            if path.name == "public.py":
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


def check(root):
    return [Violation(**v).render() for v in analyze(root)["violations"]]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--graph", action="store_true")
    args = parser.parse_args()
    try:
        report = analyze(args.root)
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
