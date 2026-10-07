"""Small explicit registration over argparse, including real nested command paths."""
from dataclasses import dataclass
import re
from typing import Callable
from platform_cli.internal.commands import doctor, health, modules, run, version


@dataclass(frozen=True)
class CommandDefinition:
    path: tuple[str, ...]
    help: str
    handler: Callable
    configure: Callable | None = None


class CommandRegistry:
    def __init__(self, definitions=()):
        self.definitions = []
        for definition in definitions:
            self.register(definition)

    def register(self, definition):
        if not isinstance(definition.path, tuple) or not definition.path or not callable(definition.handler) or any(not isinstance(part, str) or not re.fullmatch(r"[a-z][a-z0-9-]*", part) for part in definition.path) or any(d.path == definition.path or d.path[:len(definition.path)] == definition.path or definition.path[:len(d.path)] == d.path for d in self.definitions):
            raise ValueError("Invalid, duplicate or conflicting command path")
        self.definitions.append(definition)
        return self

    def attach(self, parser, options):
        groups = {(): parser.add_subparsers(dest="command", title="Commands")}
        for definition in self.definitions:
            for length in range(1, len(definition.path) + 1):
                path = definition.path[:length]
                if path in groups:
                    continue
                parent = groups[path[:-1]]
                leaf = length == len(definition.path)
                child = parent.add_parser(path[-1], help=definition.help if leaf else f"{path[-1]} commands", description=definition.help if leaf else None)
                options(child)
                if leaf:
                    child.set_defaults(definition=definition)
                    if definition.configure:
                        definition.configure(child)
                else:
                    groups[path] = child.add_subparsers(dest="subcommand_" + str(length), required=True)


def default_registry():
    return CommandRegistry((
        CommandDefinition(("version",), "Show the CLI version", version.execute),
        CommandDefinition(("doctor",), "Diagnose repository, configuration, architecture and module graph", doctor.execute),
        CommandDefinition(("run",), "Start the local platform host until Ctrl+C or SIGTERM", run.execute, run.configure),
        CommandDefinition(("modules",), "Inspect enabled module identities and activation dependencies without starting", modules.execute),
        CommandDefinition(("health",), "Inspect a freshly built local host; does not query another running process", health.execute),
    ))
