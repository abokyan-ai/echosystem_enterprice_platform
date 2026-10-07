"""Small hosting contracts; concrete wiring and host implementations live in CLI."""
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Mapping, Protocol
import re

MODULE_NAME = "bootstrap-contracts"


class HostState(str, Enum):
    BUILT = "built"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"
    DISPOSED = "disposed"


class HealthStatus(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"


@dataclass(frozen=True)
class BootstrapDiagnostic:
    code: str
    message: str
    module: str | None = None
    dependency: str | None = None
    setting: str | None = None
    path: tuple[str, ...] = ()

    def render(self):
        details = [f"{self.code}: {self.message}"]
        if self.module:
            details.append(f"Module: {self.module}")
        if self.dependency:
            details.append(f"Dependency: {self.dependency}")
        if self.setting:
            details.append(f"Setting: {self.setting}")
        if self.path:
            details.append("Path: " + " -> ".join(self.path))
        return " | ".join(details)


class BootstrapError(ValueError):
    def __init__(self, *diagnostics: BootstrapDiagnostic):
        self.diagnostics = tuple(diagnostics)
        super().__init__("\n".join(d.render() for d in diagnostics))


class PlatformModule(Protocol):
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def health(self) -> HealthStatus: ...


def no_settings(settings: Mapping[str, object]) -> None:
    if settings:
        raise BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "This module has no configurable settings"))


@dataclass(frozen=True)
class ModuleRegistration:
    id: str
    factory: Callable[[Mapping[str, PlatformModule], Mapping[str, object]], PlatformModule]
    requires: tuple[str, ...] = ()
    validate_settings: Callable[[Mapping[str, object]], None] = no_settings
    kind: str = "core"

    def __post_init__(self):
        if not isinstance(self.id, str) or not re.fullmatch(r"[a-z][a-z0-9.-]*", self.id) or not callable(self.factory) or not callable(self.validate_settings) or not isinstance(self.kind, str) or self.kind not in {"core", "adapter"}:
            raise BootstrapError(BootstrapDiagnostic("BOOT-MOD-001", "Invalid module registration"))
        if not isinstance(self.requires, tuple) or any(not isinstance(d, str) or not re.fullmatch(r"[a-z][a-z0-9.-]*", d) for d in self.requires) or len(set(self.requires)) != len(self.requires):
            raise BootstrapError(BootstrapDiagnostic("BOOT-MOD-001", "Invalid activation dependency declaration", self.id))


@dataclass(frozen=True)
class PlatformConfiguration:
    profile: str = "development"
    enabled_modules: tuple[str, ...] | None = None
    module_settings: Mapping[str, Mapping[str, object]] = field(default_factory=dict)


@dataclass(frozen=True)
class ModuleHealth:
    id: str
    status: HealthStatus
    started: bool


@dataclass(frozen=True)
class PlatformHealth:
    state: HostState
    status: HealthStatus
    registered_modules: tuple[str, ...]
    started_modules: tuple[str, ...]
    failed_modules: tuple[str, ...]
    modules: tuple[ModuleHealth, ...]
    diagnostics: tuple[BootstrapDiagnostic, ...]


class PlatformHost(Protocol):
    def start(self) -> None: ...
    def health(self) -> PlatformHealth: ...
    def stop(self) -> None: ...
    def dispose(self) -> None: ...
