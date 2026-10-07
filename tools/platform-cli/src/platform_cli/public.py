"""CLI-owned adapter contracts; no bootstrap or domain implementation is exported."""
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Mapping, Protocol
from bootstrap_contracts.public import PlatformConfiguration, PlatformHost

MODULE_NAME = "platform-cli"
CLI_VERSION = "0.1.0"
OUTPUT_SCHEMA_VERSION = 1


@dataclass(frozen=True)
class CliDiagnostic:
    code: str
    message: str
    severity: str = "ERROR"
    context: Mapping[str, object] = field(default_factory=dict)
    suggestion: str = "See platform --help and verify local configuration."


class CliError(Exception):
    def __init__(self, exit_code, *diagnostics):
        self.exit_code, self.diagnostics = exit_code, tuple(diagnostics)
        super().__init__("; ".join(d.message for d in diagnostics))


@dataclass(frozen=True)
class PlatformRequest:
    root: Path
    config: Path | None = None
    profile: str | None = None
    enabled_modules: tuple[str, ...] | None = None


@dataclass(frozen=True)
class CommandResult:
    command: str
    data: Mapping[str, object]
    exit_code: int = 0
    diagnostics: tuple[CliDiagnostic, ...] = ()


class CliServices(Protocol):
    """Explicit injected capabilities; implementations belong to local composition."""
    def repository(self, request: PlatformRequest) -> Mapping[str, object]: ...
    def configuration(self, request: PlatformRequest) -> PlatformConfiguration: ...
    def architecture(self, request: PlatformRequest) -> Mapping[str, object]: ...
    def host(self, request: PlatformRequest, configuration: PlatformConfiguration, events: Callable) -> PlatformHost: ...
    def describe(self, host: PlatformHost) -> Mapping[str, object]: ...
