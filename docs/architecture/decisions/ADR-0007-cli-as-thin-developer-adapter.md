# ADR-0007: Platform CLI as a thin developer adapter

Status: Accepted for ARC-05

## Context

ARC-04 delivered doctor/run and a local bootstrap host, but command dispatch, output and lifecycle orchestration shared one entry file. Future commands need discoverable registration and testable diagnostics without introducing a second CLI or domain logic.

## Decision

Retain the single Python CLI and standard-library argparse. Use explicit command definitions with tuple paths, a small invocation context and injected public CLI/hosting capability contracts. Root parsing dispatches through definitions; handlers orchestrate existing bootstrap and architecture capabilities. Bootstrap lifecycle and configuration remain ARC-04-owned implementations.

Separate CommandResult data, human/JSON rendering, diagnostic classification and operational events. Introduce CLI version 0.1.0 and experimental output schema 1. Define exit codes 0–5 for success/general/input/config/bootstrap/architecture. Preserve codes through source launchers and development aliases. Provide five real local commands and no placeholders.

The CLI is tooling, not semantic core. No platform domain behavior or database access is introduced. Architecture fitness enforces direction and public imports; semantic business-logic detection is explicitly deferred.

## Consequences and revisit conditions

No external CLI framework/container is necessary. Modules/health inspect a new unstarted local host, not a remote daemon. Version/help do not load configuration. In-process fake service tests avoid subprocesses for every unit case; subprocess integration verifies real entry points and signals.

Revisit for remote control plane/authentication, plugin-provided commands, interactive shell, multi-workspace context or cloud profiles. These features require explicit contracts and are not enabled now. ADR-0005 already belongs to architecture fitness, so this decision uses the next free identifier, ADR-0007.
