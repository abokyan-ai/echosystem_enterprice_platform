from platform_cli.public import CLI_VERSION, CommandResult


def execute(context, args):
    return CommandResult("version", {"version": CLI_VERSION})
