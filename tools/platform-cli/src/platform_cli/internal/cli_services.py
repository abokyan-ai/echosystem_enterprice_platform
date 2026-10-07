"""Local adapter wiring ARC-04 and the public fitness CLI; handlers use CliServices."""
import json
import subprocess
import sys
from platform_cli.public import CliDiagnostic, CliError, MODULE_NAME
from platform_cli.internal.bootstrap_configuration import load_configuration
from platform_cli.internal.composition import compose_local
from platform_cli.internal.registration import REGISTERED_PLATFORM_MODULES


class LocalCliServices:
    def repository(self, request):
        try:
            data = json.loads((request.root / "architecture.json").read_text())
            if sys.version_info < (3, 11):
                raise ValueError("Python version")
            if {m["name"] for m in data["modules"]} != REGISTERED_PLATFORM_MODULES | {MODULE_NAME}:
                raise ValueError("Public registration mismatch")
            for name in ("architecture-policy.json", "scripts/architecture_fitness/__main__.py"):
                if not (request.root / name).is_file():
                    raise ValueError("Missing repository capability")
            return {"python": sys.version.split()[0], "public_modules": len(data["modules"])}
        except (OSError, ValueError, KeyError, TypeError) as exc:
            raise CliError(1, CliDiagnostic("CLI-REPO-001", "Repository structure, Python version or explicit public registrations are invalid", suggestion="Select the platform repository with --root and check its registered modules.")) from exc

    def configuration(self, request):
        path = request.config or request.root / "config/development.json"
        if not path.is_absolute():
            path = request.root / path
        overrides = {}
        if request.profile is not None:
            overrides["profile"] = request.profile
        if request.enabled_modules is not None:
            overrides["enabled_modules"] = request.enabled_modules
        return load_configuration(path, overrides=overrides)

    def architecture(self, request):
        # The ARC-03 CLI is the existing public tooling interface, not its internals.
        result = subprocess.run([sys.executable, "-m", "architecture_fitness", "--root", str(request.root), "--format", "json"], capture_output=True, text=True)
        try:
            report = json.loads(result.stdout)
            summary = report["summary"]
            if not isinstance(summary, dict) or "status" not in summary:
                raise ValueError("Invalid report")
        except (ValueError, KeyError, TypeError) as exc:
            raise CliError(5, CliDiagnostic("CLI-ARCH-001", "Architecture fitness interface is unavailable or returned an invalid report", suggestion="Run python3 scripts/dev.py fitness from the repository.")) from exc
        if result.returncode or summary["status"] == "FAILED":
            raise CliError(5, *(CliDiagnostic(v["rule_id"], v["message"], v.get("severity", "ERROR"), {"source": v.get("source"), "target": v.get("target"), "evidence": v.get("evidence")}, v.get("resolution", "Review architecture rules.")) for v in report.get("violations", [])), CliDiagnostic("CLI-ARCH-001", "Architecture validation failed", suggestion="Run python3 scripts/dev.py fitness for the full report."))
        return summary

    def host(self, request, configuration, events):
        return compose_local(request.root, configuration, events)

    def describe(self, host):
        snapshot = host.health()
        by_id = {m.id: m for m in snapshot.modules}
        return {"startup_order": host.order, "startup_ms": host.startup_ms, "module_startup_ms": dict(host.module_startup_ms), "modules": [{"id": name, "dependencies": registration.requires, "kind": registration.kind, "status": by_id[name].status, "started": by_id[name].started} for name, registration in sorted(host.registrations.items())]}
