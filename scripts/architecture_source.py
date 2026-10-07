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
        if exceptions.get("schema_version") != 1 or not isinstance(exceptions.get("exceptions"), list):
            raise ValueError("Invalid exception registry schema")
        for exception in exceptions["exceptions"]:
            required = {"id", "rule_id", "source", "target", "reason", "owner", "created_at", "expires_at", "review_issue"}
            if set(exception) != required or any(not isinstance(v, str) or not v.strip() for v in exception.values()):
                raise ValueError("Exception requires exact rule/source/target, owner, reason, dates and review reference")
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
