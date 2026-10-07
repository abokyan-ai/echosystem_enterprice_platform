"""The single local composition root: explicit core registrations, no feature behavior."""
import json
from pathlib import Path
from bootstrap_contracts.public import BootstrapDiagnostic, BootstrapError, HealthStatus, ModuleRegistration
from platform_cli.internal.bootstrap_host import BootstrapBuilder
from platform_cli.internal.registration import CORE_MODULE_IDENTITIES


class BoundaryModule:
    """Lifecycle marker for a registered architectural boundary, not a business module."""
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def health(self):
        return HealthStatus.HEALTHY if self.running else HealthStatus.DEGRADED


def compose_local(root: Path, configuration, event_sink=None):
    try:
        manifest = json.loads((root / "architecture.json").read_text())
        metadata = {m["name"]: m for m in manifest["modules"]}
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise BootstrapError(BootstrapDiagnostic("BOOT-MOD-001", "Module metadata is unreadable")) from exc
    builder = BootstrapBuilder(configuration, event_sink)
    # Identities come from static public imports; manifest data supplies activation requirements.
    for identity in CORE_MODULE_IDENTITIES:
        if identity not in metadata:
            raise BootstrapError(BootstrapDiagnostic("BOOT-MOD-002", "Explicit module identity missing from metadata", identity))
        requires = metadata[identity].get("activation_dependencies", [])
        if not isinstance(requires, list):
            raise BootstrapError(BootstrapDiagnostic("BOOT-MOD-001", "Invalid activation dependency metadata", identity))
        builder.add_module(ModuleRegistration(identity, lambda dependencies, settings: BoundaryModule(), tuple(requires)))
    return builder.build()
