from platform_cli.public import CommandResult
from platform_cli.internal.cli_diagnostics import classify


def execute(context, args):
    checks, diagnostics, codes = [], [], []
    configuration = None
    def check(name, operation):
        try:
            value = operation()
            checks.append({"name": name, "status": "PASS", "details": value if isinstance(value, dict) else {}})
            return value
        except Exception as error:
            failure = classify(error)
            checks.append({"name": name, "status": "FAIL", "diagnostics": [d.code for d in failure.diagnostics]})
            diagnostics.extend(failure.diagnostics)
            codes.append(failure.exit_code)
            return None
    check("Repository", lambda: context.services.repository(context.request))
    configuration = check("Configuration", lambda: context.services.configuration(context.request))
    check("Architecture Fitness", lambda: context.services.architecture(context.request))
    if configuration is not None:
        def graph():
            host = context.services.host(context.request, configuration, lambda e, m: None)
            try:
                return {"startup_order": context.services.describe(host)["startup_order"]}
            finally:
                host.dispose()
        check("Module Graph", graph)
    else:
        checks.append({"name": "Module Graph", "status": "SKIP", "reason": "Configuration check failed"})
    # Stable priority for independent failures: configuration, architecture, bootstrap, general.
    code = next((c for c in (3, 5, 4, 1) if c in codes), 0)
    return CommandResult("doctor", {"status": "unhealthy" if code else "healthy", "checks": checks}, code, tuple(diagnostics))
