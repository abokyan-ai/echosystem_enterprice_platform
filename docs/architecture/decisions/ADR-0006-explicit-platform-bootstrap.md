# ADR-0006: Explicit local platform bootstrap

Status: Accepted for ARC-04

## Context

Doctor and static public imports validate boundaries but cannot compose a runnable host or manage resource lifecycle. Core modules must remain independent of executable/infrastructure initialization.

## Decision

Keep concrete builder, host, configuration loading and composition in CLI internals. Extract only small framework-neutral hosting contracts into a registered `bootstrap-contracts` module. Register core boundary markers explicitly; select future adapters only at outer composition boundaries. Reuse architecture metadata with a separate activation dependency field, deterministic topological startup and reverse cleanup.

Provide one synchronous local host with test-only explicit override support. Validate complete configuration before constructing instances. Factories are resource-free; start/stop own resource acquisition and cleanup. Aggregate cleanup failures and retain failed resources for retry. Reject restart after shutdown; build another host.

## Consequences

The repository now has seven source modules and 34 fitness rules. Core markers remain behavior-free. No framework/container/plugin scanner is installed. Hosting contracts do not depend on CLI; bootstrap is not a global service locator. Direct CLI hosts handle SIGINT/SIGTERM. Synchronous callbacks must terminate themselves; deadlines/concurrent lifecycle and deployment/secrets policies require later decisions.
