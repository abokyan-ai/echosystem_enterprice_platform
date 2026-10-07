"""One filesystem/AST discovery pass. No fitness rule runs in this adapter."""
import ast
from pathlib import Path
from architecture_source import ArchitectureError, import_targets, load_manifest, read_json
from .model import ArchitectureException, ArchitectureModel, Module, Source


def discover(root: Path):
    root = root.resolve()
    data = load_manifest(root)
    policy = read_json(root / "architecture-policy.json")
    metadata = {m["name"]: m for m in data["modules"]}
    modules = tuple(Module(m["name"], m["path"], m["zone"], "contract" if m["zone"] in {"kernel", "model", "compiled-contracts", "experience"} else m["zone"], tuple(m["public_api"]), (m["package"] + ".internal",), m) for m in sorted(metadata.values(), key=lambda m: m["name"]))
    registered = {m.id: (root / m.path / "src" / m.metadata["package"]).resolve() for m in modules}
    sources = []
    scans = 0
    for family in ("platform", "adapters", "apps", "tools"):
        for path in sorted((root / family).rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts or path.suffix not in {".py", ".ts", ".tsx", ".js", ".jsx", ".dart"}:
                continue
            if any(path.is_relative_to(root / m.path / "tests") for m in modules):
                continue
            filename = str(path.relative_to(root))
            resolved = path.resolve()
            owner = next((name for name, directory in registered.items() if resolved.is_relative_to(directory)), None)
            if not resolved.is_relative_to(root):
                sources.append(Source(filename, None, issue="Source symlink escapes repository", issue_kind="registration"))
                continue
            if owner is None or path.suffix != ".py":
                sources.append(Source(filename, owner, issue="Unregistered source or unsupported production language", issue_kind="registration"))
                continue
            try:
                tree = ast.parse(path.read_text(), filename=filename)
                scans += 1
                targets = tuple(import_targets(tree, metadata[owner]["package"], resolved.relative_to(registered[owner])))
                nodes = tuple(ast.walk(tree))
                calls = tuple((node.func.id, node.lineno) for node in nodes if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in {"__import__", "exec", "eval"})
                classes = tuple((node.name, node.lineno) for node in nodes if isinstance(node, ast.ClassDef))
                sources.append(Source(filename, owner, targets, calls, classes=classes))
            except (SyntaxError, ArchitectureError) as exc:
                sources.append(Source(filename, owner, issue=str(exc), issue_kind="syntax"))
    exceptions = read_json(root / "docs/architecture/dependency-exceptions.json")["exceptions"]
    return ArchitectureModel(modules, tuple(sources), policy, tuple(ArchitectureException(**e) for e in exceptions), {"adapter": "python-ast-workspace", "files_parsed": scans, "scan_passes": 1})
