# ADR-0037 — Enforce immutable explicit compiler composition and bounded semantic comparison

Date: 2026-10-11. Status: implemented; DEFERRED / NOT VERIFIED.

## Context

Existing canonical ordering, precise immutable payload values, explicit request-local IR tokens, sequential phases, ordered diagnostics and atomic state transitions already encode most determinism requirements. Mutable external phase options and descriptor drift were not rejected; binding mapping order affected configuration equality; original-request envelope equality could not compare separately accepted equivalent inputs.

## Decision

Keep original ModelCompiler and TypeCompilerPass. Require frozen dataclass phase implementations with a small closed immutable option vocabulary; snapshot full configuration/implementation classes and audit before execution and after each valid result. Structured CMP-029 constructor rejection covers unsupported/ambiguous configuration, and CMP-030 detects captured drift without commit. Configured order is semantic, no scheduler/sort or policy-disable option. Existing extension admission is intentionally stricter.

Normalize type representation binding mapping order by exact ID/numeric-version while preserving MOD-04 definition order, DataFacet fields, original diagnostic emission, canonical phase IR order and CMP-03 identity-sorted committed inventory. Reuse exact caller tokens, collision/slot guards and existing atomic coordinator, not hashes or generated identifiers.

Provide CompilationResultEquivalence with explicit requests/configurations/results/states/IR methods using actual supported equality. Separate original ownership/authorization from semantic comparison and physical presentation. Exclude human/source metadata from semantic comparison while retaining it in reports. Refuse concrete artifact equivalence without its real payload contract. Result observables alone do not establish input equivalence or expose internal IR.

## Consequences

Supported determinism is enforceable through immutable admitted configuration and current pure transformations. No claim of arbitrary ambient-dependent third-party method detection, full unimplemented semantic-content equality, portable compiler identity or byte reproducibility. Mutable old phase extensions/doubles need explicit frozen configuration adaptation in future authorized verification; old source/tests/history preserved. No framework route/ORM/generator/runtime/serialization/hash/cache/parallelism/deploy changes. Stop CMP-06.
