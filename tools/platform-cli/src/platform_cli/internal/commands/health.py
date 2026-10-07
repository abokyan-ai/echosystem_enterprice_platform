from dataclasses import asdict
from bootstrap_contracts.public import HealthStatus
from platform_cli.public import CliDiagnostic, CommandResult


def execute(context, args):
    configuration = context.services.configuration(context.request)
    host = context.services.host(context.request, configuration, lambda e, m: None)
    try:
        health = host.health()
        code = 1 if health.status == HealthStatus.UNHEALTHY else 0
        return CommandResult("health", {"scope": "local-inspection", "profile": configuration.profile, "health": asdict(health)}, code, (CliDiagnostic("CLI-HEALTH-001", "Local platform health is unhealthy"),) if code else ())
    finally:
        host.dispose()
