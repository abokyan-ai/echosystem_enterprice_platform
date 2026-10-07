"""Tool-independent input and output contracts for executable fitness functions."""
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable


class Severity(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


@dataclass(frozen=True)
class Module:
    id: str
    path: str
    zone: str
    kind: str
    public_api: tuple[str, ...]
    internal_api: tuple[str, ...]
    metadata: dict[str, Any] = field(repr=False)


@dataclass(frozen=True)
class Source:
    file: str
    owner: str | None
    targets: tuple[tuple[str, int], ...] = ()
    dynamic_calls: tuple[tuple[str, int], ...] = ()
    issue: str | None = None
    issue_kind: str | None = None
    classes: tuple[tuple[str, int], ...] = ()


@dataclass(frozen=True)
class ArchitectureException:
    id: str
    rule_id: str
    source: str
    target: str
    reason: str
    owner: str
    created_at: str
    expires_at: str
    review_issue: str


@dataclass(frozen=True)
class ArchitectureModel:
    modules: tuple[Module, ...]
    sources: tuple[Source, ...]
    policy: dict[str, Any]
    exceptions: tuple[ArchitectureException | dict[str, str], ...] = ()
    discovery_metadata: dict[str, Any] = field(default_factory=dict)

    def graph(self, kind="declared"):
        if kind not in {"declared", "observed"}:
            raise ValueError(f"Unknown graph kind: {kind}")
        graph = {m.id: set() for m in self.modules}
        if kind == "declared":
            for module in self.modules:
                graph[module.id].update(module.metadata["allowed_dependencies"])
        else:
            packages = {m.metadata["package"]: m.id for m in self.modules}
            for source in self.sources:
                for target, _ in source.targets:
                    destination = packages.get(target.split(".")[0])
                    if source.owner in graph and destination and destination != source.owner:
                        graph[source.owner].add(destination)
        return graph

    def external_inventory(self):
        packages = {m.metadata["package"] for m in self.modules}
        import sys
        inventory = set()
        for source in self.sources:
            for target, _ in source.targets:
                prefix = target.split(".")[0]
                if prefix not in packages and prefix not in sys.stdlib_module_names and prefix != "__future__":
                    category = self.policy.get("external_dependencies", {}).get(prefix, {}).get("category", "unknown")
                    inventory.add((source.owner, prefix, category))
        return [{"module": owner, "dependency": dependency, "category": category} for owner, dependency, category in sorted(inventory)]


@dataclass(frozen=True)
class ArchitectureViolation:
    rule_id: str
    severity: Severity
    message: str
    source: str
    target: str
    evidence: str
    suggested_resolution: str
    file: str | None = None
    line: int | None = None
    dependency_path: tuple[str, ...] = ()


@dataclass(frozen=True)
class ArchitectureRule:
    id: str
    name: str
    description: str
    category: str
    severity: Severity
    scope: str
    evaluate: Callable[[ArchitectureModel, dict], list[ArchitectureViolation]]


@dataclass
class ArchitectureRuleResult:
    rule_id: str
    status: str
    violations: list[ArchitectureViolation]
    duration_ms: float
    metadata: dict = field(default_factory=dict)
