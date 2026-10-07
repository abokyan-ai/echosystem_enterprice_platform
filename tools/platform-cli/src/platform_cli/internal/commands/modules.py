from platform_cli.public import CommandResult


def execute(context, args):
    configuration = context.services.configuration(context.request)
    host = context.services.host(context.request, configuration, lambda e, m: None)
    try:
        description = context.services.describe(host)
        return CommandResult("modules", {"scope": "local-inspection", "profile": configuration.profile, "state": host.health().state, "modules": description["modules"], "startup_order": description["startup_order"]})
    finally:
        host.dispose()
