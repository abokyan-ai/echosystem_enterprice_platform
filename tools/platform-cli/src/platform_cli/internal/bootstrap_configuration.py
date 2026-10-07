"""Configuration loading/binding without runtime, business or cloud semantics."""
import copy
import json
import os
from pathlib import Path
from types import MappingProxyType
from bootstrap_contracts.public import BootstrapDiagnostic, BootstrapError, PlatformConfiguration

FIELDS = {"profile", "enabled_modules", "module_settings"}


def validate_configuration(configuration):
    if not isinstance(configuration, PlatformConfiguration):
        raise BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "Expected platform configuration contract"))
    if not isinstance(configuration.profile, str) or configuration.profile not in {"development", "test", "production"}:
        raise BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "Unsupported configuration profile", setting="profile"))
    enabled = configuration.enabled_modules
    if enabled is not None and (not isinstance(enabled, tuple) or any(not isinstance(m, str) or not m for m in enabled) or len(set(enabled)) != len(enabled)):
        raise BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "Enabled modules must be unique module IDs", setting="enabled_modules"))
    if not isinstance(configuration.module_settings, dict) and not isinstance(configuration.module_settings, MappingProxyType):
        raise BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "Module settings must be a mapping", setting="module_settings"))
    if any(not isinstance(name, str) or not isinstance(settings, dict) for name, settings in configuration.module_settings.items()):
        raise BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "Each module owns a settings object", setting="module_settings"))
    return configuration


def bind(values):
    if not isinstance(values, dict) or set(values) - FIELDS:
        raise BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "Unknown or invalid top-level configuration field"))
    enabled = values.get("enabled_modules")
    if enabled is not None and not isinstance(enabled, (list, tuple)):
        raise BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "Enabled modules must be a list", setting="enabled_modules"))
    configuration = PlatformConfiguration(values.get("profile", "development"), tuple(enabled) if enabled is not None else None, copy.deepcopy(values.get("module_settings", {})))
    return validate_configuration(configuration)


def load_configuration(path: Path | None = None, environment=None, overrides=None):
    """Precedence: defaults < file < environment < CLI (settings merge by module)."""
    values = {"profile": "development", "enabled_modules": None, "module_settings": {}}
    def merge(layer):
        if not isinstance(layer, dict) or set(layer) - FIELDS:
            raise BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "Invalid configuration fields"))
        if "module_settings" in layer:
            if not isinstance(layer["module_settings"], dict) or any(not isinstance(v, dict) for v in layer["module_settings"].values()):
                raise BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "Invalid module settings", setting="module_settings"))
            for name, settings in layer["module_settings"].items():
                values["module_settings"].setdefault(name, {}).update(copy.deepcopy(settings))
        for field in ("profile", "enabled_modules"):
            if field in layer:
                values[field] = layer[field]
    if path is not None:
        try:
            merge(json.loads(path.read_text()))
        except (OSError, ValueError) as exc:
            if isinstance(exc, BootstrapError):
                raise
            raise BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "Configuration file is unreadable or invalid JSON", setting="config_file")) from exc
    env = os.environ if environment is None else environment
    layer = {}
    if "PLATFORM_PROFILE" in env:
        layer["profile"] = env["PLATFORM_PROFILE"]
    if "PLATFORM_MODULES" in env:
        layer["enabled_modules"] = [m.strip() for m in env["PLATFORM_MODULES"].split(",") if m.strip()]
    if "PLATFORM_MODULE_SETTINGS" in env:
        try:
            layer["module_settings"] = json.loads(env["PLATFORM_MODULE_SETTINGS"])
        except ValueError as exc:
            raise BootstrapError(BootstrapDiagnostic("BOOT-CONFIG-001", "Invalid environment settings JSON", setting="PLATFORM_MODULE_SETTINGS")) from exc
    merge(layer)
    merge(overrides or {})
    return bind(values)
