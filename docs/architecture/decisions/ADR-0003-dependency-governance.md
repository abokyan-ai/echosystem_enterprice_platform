# ADR-0003 — Dependency Direction and Executable Governance

Status: Accepted. Date: 2026-10-07.

## Context

ARC-01 has six Python modules and basic AST checks, but lacks explicit zones, stable diagnostics, production/test protections and distinct observed/declared graphs. ADR-0002 already records Python tooling, so this decision uses ADR-0003 rather than overwriting it.

## Decision

Use a versioned module manifest and separate zone policy as two levels of allowlist. Keep AST source analysis, public contract enforcement, restricted standard library profiles and explicitly owned external approvals. Make the CLI's public registration imports static and declare them as development edges. Validate both declared and observed graphs; fail build/CI on violations. Document selected Angular/PrimeNG, Django/DRF and mock-data profiles without implementing them in a governance task.

## Rules

DR-001..DR-012 map to ARCH-DEP-001..012. Supporting API/cycle/allowlist/external/registration/source/configuration/dynamic rules have stable IDs. Tests include AT-DEP-001..012 and negative fixtures beyond them. Runtime cannot import authoring model or source parsers; adapter/profile dependencies point inward to contracts.

## Enforcement strategy

Deterministic Python AST parsing, registered source ownership, zone/path consistency, exact public surfaces and DFS graphs. Root commands run real repository validation and a separate fixture suite. Unsupported production languages fail closed until their analyzer exists.

## Alternatives

Documentation alone cannot reject code. Blacklists miss unknown frameworks. A heavyweight monorepo framework or external architecture library is unnecessary for this Python skeleton. Dynamic inspection hides static dependency edges. Separate semantic IR/runtime contract modules are premature before their APIs diverge.

## Consequences

New modules need zone/owner/public surface/categories/declarations; root tooling discovers them. Doctor's explicit registration imports require updating when adding a module to its registration set. Frameworks remain adapters. Public types must be defined as contracts, not aliases to internal implementations. Strict runtime JSON denial must be revisited explicitly if safe serialization becomes necessary.

## Exception policy

No exceptions currently. Empty central registry; nonempty registries fail until a narrowly scoped reviewed waiver implementation and full metadata are added. No inline suppressions.

## Revisit conditions

Actual TypeScript/Angular code, framework/package manifests, packaging/transitive dependencies, new contract zones, reflection requirements or an operational extraction need. Expand tests and analyzers with real modules while preserving stable ownership and rule IDs.
