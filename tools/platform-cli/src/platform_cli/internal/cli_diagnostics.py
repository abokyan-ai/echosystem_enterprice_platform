"""Classification and safe rendering inputs; bootstrap diagnostics remain their source."""
from bootstrap_contracts.public import BootstrapError
from platform_cli.public import CliDiagnostic, CliError


def classify(error):
    if isinstance(error, CliError):
        return error
    if isinstance(error, BootstrapError):
        code = 3 if any(d.code == "BOOT-CONFIG-001" for d in error.diagnostics) else 4
        return CliError(code, *(CliDiagnostic(d.code, d.message, context={key: value for key, value in {"module": d.module, "dependency": d.dependency, "setting": d.setting, "path": d.path}.items() if value}, suggestion="Verify module selection, activation dependencies and module-owned configuration.") for d in error.diagnostics))
    # Do not echo arbitrary exception text: it can contain credentials/configuration.
    return CliError(1, CliDiagnostic("CLI-INTERNAL-001", "Unexpected local CLI failure", suggestion="Retry with --verbose for an exception type; inspect local configuration."))
