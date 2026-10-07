from dataclasses import asdict
from bootstrap_contracts.public import HealthStatus
from platform_cli.public import CliDiagnostic, CliError, CommandResult
from platform_cli.internal.cli_diagnostics import classify


def configure(parser):
    parser.add_argument("--once", action="store_true", help="Start, report startup health, then stop")


def execute(context, args):
    configuration = context.services.configuration(context.request)
    host = context.services.host(context.request, configuration, context.output.event)
    failure = None
    result = None
    with context.signal_scope():
        try:
            host.start()
            health = host.health()
            description = context.services.describe(host)
            code = 1 if health.status == HealthStatus.UNHEALTHY else 0
            result = CommandResult("run", {"scope": "local-run", "profile": configuration.profile, "health": asdict(health), "startup_order": description["startup_order"], "startup_ms": description["startup_ms"], "module_startup_ms": description["module_startup_ms"], "once": args.once}, code, (CliDiagnostic("CLI-HEALTH-001", "Started host reported unhealthy status"),) if code else ())
            # Persistent hosts stream one startup result; cleanup errors go to stderr.
            if not args.once:
                context.output.result(result)
                if not code:
                    context.cancellation.wait()
        except KeyboardInterrupt:
            context.cancellation.set()
            failure = CliError(4, CliDiagnostic("CLI-CANCEL-001", "Local host interrupted during startup or execution", suggestion="Retry the local run when ready."))
        except Exception as error:
            failure = classify(error)
        finally:
            try:
                host.dispose()
            except Exception as error:
                cleanup = classify(error)
                if failure is None:
                    failure = cleanup
                else:
                    failure = CliError(failure.exit_code, *failure.diagnostics, *cleanup.diagnostics)
    if failure:
        raise failure
    return result if args.once else (result.exit_code if result else 0)
