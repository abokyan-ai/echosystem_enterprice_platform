# CMP-05 — Implementation and static inspection record

Date: 2026-10-11. Task: Type Compiler Pass. Status: **DEFERRED / NOT VERIFIED**. New automated tests implemented: **0**. Deferred tests executed: **0**. Documented future cases: **129**, all **NOT_RUN — DEFERRED**.

## Implemented components and decisions

Existing compiler-core owns TypeCompilerPass and TYPE_COMPILER_PASS_PHASE (same stable CMP-PHASE-COMPILED-TYPE-IR identity). CompiledTypeLoweringPhase aliases that class; no duplicate pass implementation/configurable identity. Existing CompiledTypeLowerer gains lower_payload with unchanged existing CompiledTypeIR or expected original PhaseResult rejection; legacy lower still adapts to one envelope. Field conversion is implemented once.

Pass gates original bound VALID/READY request and actual completed executed matching preparation, selects supported actual canonical members in canonical ID/numeric-version order, requires caller-owned exact representation bindings, preflights current-state ownership/rerun/exact-origin/IR-ID conflicts, invokes focused lowerer independently, constructs actual CMP-03 V0 type envelopes and aggregates expected failures. Missing per-type diagnostic context is enriched without replacing existing field/cause/origin evidence; contradictory ownership is a programming error. FAILED dominates INCOMPLETE; no partial successful outputs. Existing coordinator alone atomically commits the complete immutable tuple with artifacts/preparation/outcome. Phase emission order is canonical; committed IR inventory remains CMP-03 identity-sorted.

Multiple exact versions preserved, no latest/graph expansion. Empty accepted canonical membership returns empty completed work; artifact-build remains incomplete without actual generator. Self/mutual references stay versionless ElementRef. Original canonical source sidecars retained, no inferred physical spans. Original evidence/contexts/definitions/state untouched and staging local. Existing source reporting and semantic validation owners unchanged.

## Changed repository files

Production modified (1):

- `platform/compiler/compiler-core/src/compiler_core/public.py`

Documentation created (3):

- `docs/compiler/type-compiler-pass.md`
- `docs/architecture/decisions/ADR-0036-type-compiler-pass.md`
- `docs/architecture/cmp05-verification.md`

Documentation modified (5):

- `README.md`
- `docs/architecture/repository-structure.md`
- `docs/architecture/dependency-rules.md`
- `docs/compiler/compiler-foundation.md`
- `docs/compiler/compiled-type-ir.md`

Repository archive created (3):

- `test-archive/CMP-05/README.md`
- `test-archive/CMP-05/CMP-05-deferred-tests.md`
- `test-archive/CMP-05/CMP-05-deferred-test-spec.md`

Total: **12** changed files. Sole detailed case specification: [CMP-05-deferred-tests.md](../../test-archive/CMP-05/CMP-05-deferred-tests.md). README/navigation meet standing policy without duplicated scenarios. Earlier archives/executable tests/historical evidence preserved. No new tests/infrastructure/demo/runner.

## Executed static checks — distinct from deferred tests

| Check | Outcome | Evidence scope |
|---|---|---|
| `python3 scripts/dev.py lint` | Successful | Syntax, whitespace and static boundaries |
| `python3 scripts/dev.py build` | Successful | Syntax/architecture/public MODULE_NAME imports |
| `python3 scripts/dev.py fitness:json --output build/cmp05-fitness.json` | HEALTHY; 44 rules, 0 failures/warnings/exceptions/suppressed/cycles | Existing 9 modules / 45 production sources |
| `python3 scripts/dev.py dependencies:json` | Successful; 0 cycles | Import/manifest ownership |
| `git diff --check` | Successful | Formatting only |
| Archive Markdown inspection | 129 unique IDs / 129 deferred case statuses | Document completeness/count only |
| Package metadata | PyYAML 6.0.3; Django/DRF absent | Installed metadata only |

Static checks repeated after production edits. No pass/lowerer/payload/envelope/validator or Mini Sales scenario instantiated or executed; no pytest/unittest/manage.py tests/CLI/runtime smoke/custom scenario runner/deferred suite execution. Static success does not establish behavioral correctness.

Unchanged workflow DEFER_COMPREHENSIVE_TESTS=true prevents deferred tests indirectly running through CI. Inspect actual push/PR jobs and nine skipped comprehensive/smoke steps per job before merging; report as skipped, never passed tests. Base remote main `74d9599398e6b63f43c86c2e28c730fcda2a9dd1`; starting local tree exactly matched `b98425b103f1794184ec8f72ecb66a9a9715829b`.

## Risks, limits and readiness

Actual canonical vocabulary is closed TypeDataComposition/type/data. Full TYPE-01/general SK-11/richer facets/legitimate other-kind membership remain owner-contract gaps; no speculative generic coverage or semantic-invalid classification. Absent DataFacet incomplete; explicit empty supported. Original in-process accepted state/evidence associations are not authenticated proof or access policy. Explicit request-local identity mapping is caller responsibility; rerun deliberately rejects rather than assuming idempotence. Unexpected programming errors propagate; domain behavior and concurrency remain unverified.

No actual final generator/type-required target or applicable compiler HTTP boundary. No endpoint created, framework integration modified, authentication/permission change, ORM/migration/serializer generation/runtime/deploy/graph/cache/storage/publishing. Existing lower and phase APIs source compatible via adapter/alias; clients relying on class display names should use stable descriptor ID instead.

[Contract and unexecuted Mini Sales](../compiler/type-compiler-pass.md) and [ADR-0036](decisions/ADR-0036-type-compiler-pass.md) describe architectural choices. Future verification requires explicit execution authorization, fixed revision, original actual fixtures and real upstream dependencies for blocked scenarios. Bounded CMP-05 implementation/documentation ready for review and next-stage planning; **DEFERRED / NOT VERIFIED**. Stop; no CMP-06 implementation.
