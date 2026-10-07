# ADR-0005 — Executable Architecture Fitness Functions

Status: Accepted. Date: 2026-10-07.

## Context

ARC-02 has executable dependency rules but discovery/evaluation are coupled and there is no reusable fitness registry/severity/exception/report contract. ARC-03 must extend that foundation, preserve IDs and remain local, fast and framework independent. ADR-0003 already belongs to dependency governance, so this decision uses ADR-0005.

## Decision

Separate manifest/AST discovery from pure policy evaluation. Create a shared ArchitectureModel, central registered ArchitectureRule functions, standardized violation/result/exception models and one execution/reporting engine. Reuse ARC-02 policy as cached model evaluation rather than rewriting it. Add precise code-owned transitive invariants independent of relaxed configuration.

## Fitness function model

Rules declare ID/name/description/category/severity/scope and evaluate the shared model. Registry and result contracts are validated. INFO/WARNING support experimental functions; ERROR/CRITICAL fail. Evaluator crashes/malformed results always fail. Existing IDs retain their meanings; new mandatory precise invariants use ARCH-FIT-DEP IDs where ARC-03 suggestions collide with existing numbers.

## Enforcement

Root build/lint/doctor/architecture commands invoke the baseline. CI writes and uploads machine-readable reports while preserving exit-code failure and the Python matrix. Source is parsed once per run; baseline policy is evaluated once and reused by registered functions. New adapters/language facts enter the model, not each rule.

## Exception strategy

Replace the historical empty-only waiver policy with exact rule/source/target temporary exceptions requiring owner/reason/review reference and ISO creation/expiry dates. Display suppressed evidence and unmatched/expired metadata. Expiry fails even if the original violation no longer exists. No wildcard/permanent/inline suppressions. UTC as-of date is injectable for deterministic tests; CI uses actual date.

## Alternatives

A new heavyweight architecture dependency adds little to this Python skeleton. Per-test filesystem scanners duplicate work. A string search misses language-level imports. Broad ignores or silently downgraded critical rules create false confidence. Renumbering ARC-02 IDs would break traceability.

## Consequences

Tooling lives in existing scripts/architecture_fitness, independent of unittest/platform behavior. A small registry extension plus tests adds a rule without runner redesign. Reports include observational timestamps/durations; semantic determinism excludes those fields. Root tools/scripts remain outside platform-module import enforcement. Critical violations can be narrowly waived only through explicit reviewed metadata; overlapping rules remain separately protected.

## Revisit conditions

Real TypeScript/Angular code, explicit package exports, cross-language artifacts, transitive dependencies, tenant/security/action semantics or substantially larger graphs. Add discovery facts/analyzers and tests as necessary; do not invent unsupported fitness claims.
