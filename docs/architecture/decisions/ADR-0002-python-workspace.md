# ADR-0002 — Standard-Library Python Workspace for ARC-01

Status: Accepted. Date: 2026-10-07.

## Context

No language, build system, package manager, framework, tests, CI or established convention exists in the empty repository. ARC-01 needs executable boundary verification and CLI without infrastructure.

## Decision

Use Python 3.11+, unittest, AST import analysis, JSON module registration and a small root command runner. No pip packages are needed. Source packages have separate roots and a single public entry point. Build verifies syntax/public imports and bundles the source workspace; it is not a released wheel. Use EditorConfig and executable syntax/whitespace lint instead of unused formatter tooling.

## Alternatives considered

TypeScript/npm would provide static typing but require additional compiler/package tooling. A full Python packaging/monorepo framework would add dependencies for an unreleased skeleton. A polyglot repository is premature until target requirements exist.

## Consequences

Clone → validate/install → build → tests → doctor works without package network access. Static typing and wire schemas are not yet supplied. Python is replaceable at contractual boundaries, but changing implementation language still requires engineering. UI frameworks and infrastructure remain adapters; this decision does not select React, Angular, Flutter or a DB.

## Future revisit conditions

Before semantic API implementation, assess strong typing, schema evolution, publishing/distribution, performance and frontend/mobile interoperability. Add real schemas/packaging only when needed and keep dependency rules equivalent if changing language/tooling.
