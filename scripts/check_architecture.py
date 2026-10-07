"""Static module rules. No third-party packages are needed."""
import argparse
import ast
import json
import sys
from pathlib import Path


class ArchitectureError(ValueError):
    pass


def load_manifest(root):
    data = json.loads((root / "architecture.json").read_text())
    if data.get("schema_version") != 1:
        raise ArchitectureError("Unsupported architecture manifest version")
    modules = data["modules"]
    names = {m["name"] for m in modules}
    packages = {m["package"] for m in modules}
    if len(names) != len(modules) or len(packages) != len(modules):
        raise ArchitectureError("Duplicate module name or package")
    for m in modules:
        if not m["package"].isidentifier():
            raise ArchitectureError(f"Invalid package: {m['package']}")
        path = (root / m["path"]).resolve()
        if not path.is_relative_to(root.resolve()):
            raise ArchitectureError(f"Module path escapes repository: {m['name']}")
        if set(m["allowed_dependencies"]) - names:
            raise ArchitectureError(f"Unknown dependencies: {m['name']}")
        if not (path / "src" / m["package"] / "public.py").is_file():
            raise ArchitectureError(f"Missing public entry point: {m['name']}")
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
    for name in graph:
        visit(name)
    return errors


def check(root):
    data = load_manifest(root)
    modules = data["modules"]
    by_package = {m["package"]: m for m in modules}
    graph = {m["name"]: set(m["allowed_dependencies"]) for m in modules}
    errors = cycles(graph)
    # Independent invariants cannot be relaxed by editing a module's allowlist.
    for m in modules:
        for name in m["allowed_dependencies"]:
            target = next(x for x in modules if x["name"] == name)
            if m["path"].startswith("platform/") and not target["path"].startswith("platform/"):
                errors.append(f"Platform dependency forbidden: {m['name']} -> {name}")
        forbidden = {
            "semantic-kernel": {"compiler-core", "runtime-core", "model-core", "compiled-contracts"},
            "model-core": {"compiler-core", "runtime-core"},
            "compiled-contracts": {"model-core", "compiler-core", "runtime-core"},
            "compiler-core": {"runtime-core"},
            "runtime-core": {"model-core", "compiler-core"},
        }.get(m["name"], set())
        for name in set(m["allowed_dependencies"]) & forbidden:
            errors.append(f"Boundary dependency forbidden: {m['name']} -> {name}")
    registered = {m["package"]: (root / m["path"] / "src" / m["package"]).resolve() for m in modules}
    for family in ("platform", "adapters", "apps", "tools"):
        for source in (root / family).rglob("*.py"):
            if "__pycache__" in source.parts:
                continue
            # Unit test files are checked through test execution; production code must be registered.
            if "tests" in source.relative_to(root).parts:
                continue
            source = source.resolve()
            owner = next((by_package[p] for p, directory in registered.items() if source.is_relative_to(directory)), None)
            if owner is None:
                errors.append(f"Unregistered source file: {source.relative_to(root)}")
                continue
            try:
                tree = ast.parse(source.read_text(), filename=str(source))
            except SyntaxError as exc:
                errors.append(f"Syntax error: {source.relative_to(root)}:{exc.lineno}: {exc.msg}")
                continue
            rel = source.relative_to(registered[owner["package"]])
            context = [owner["package"], *rel.parts[:-1]]
            for node in ast.walk(tree):
                targets = []
                if isinstance(node, ast.Import):
                    targets = [a.name for a in node.names]
                elif isinstance(node, ast.ImportFrom):
                    base = node.module or ""
                    if node.level:
                        if node.level > len(context):
                            errors.append(f"Invalid relative import: {source.relative_to(root)}:{node.lineno}")
                            continue
                        base = ".".join(context[:len(context)-node.level+1] + ([base] if base else []))
                    targets = [base] + [base + "." + a.name for a in node.names]
                elif isinstance(node, ast.Call) and owner["path"].startswith("platform/"):
                    if isinstance(node.func, ast.Name) and node.func.id in {"__import__", "exec", "eval"}:
                        errors.append(f"Dynamic code/import forbidden in platform: {source.relative_to(root)}:{node.lineno}")
                for target in targets:
                    first = target.split(".")[0]
                    location = f"{source.relative_to(root)}:{node.lineno}"
                    if first in by_package:
                        dependency = by_package[first]
                        if dependency["name"] != owner["name"]:
                            if dependency["name"] not in owner["allowed_dependencies"]:
                                errors.append(f"Module dependency violation: {owner['name']} -> {dependency['name']} at {location}")
                            # Only public.py and its exported attributes form a cross-module API.
                            if not target.startswith(first + ".public") or target.split(".")[1] != "public":
                                errors.append(f"Public API violation: {target} at {location}; use {first}.public")
                    elif first not in sys.stdlib_module_names and first != "__future__":
                        errors.append(f"Unapproved external import: {target} at {location}")
                    elif owner["path"].startswith("platform/") and first in {"sqlite3", "http", "urllib", "socket"}:
                        errors.append(f"Infrastructure import forbidden in platform: {target} at {location}")
                    elif owner["path"].startswith("platform/") and first in {"importlib", "runpy"}:
                        errors.append(f"Dynamic import module forbidden in platform: {target} at {location}")
    return sorted(set(errors))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        errors = check(args.root.resolve())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Architecture configuration error: {exc}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Architecture OK: declared graph, source imports, public APIs and registration")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
