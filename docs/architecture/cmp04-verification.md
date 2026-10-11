# CMP-04 — Implementation and static inspection record

Date: 2026-10-11. Task: Compiled Type IR. Status: **DEFERRED / NOT VERIFIED**. Automated tests implemented: **0**. Deferred tests executed: **0**. Future documented scenarios: **157**, all **NOT_RUN — DEFERRED**.

## Implemented components

Existing compiler-core implements CompiledTypeIR, CompiledFieldIR, actual TYPE-05/04 reference/constraint aliases, CompiledTypeLowerer, fixed explicitly composed CompiledTypeLoweringPhase and caller-owned exact representation bindings. TypeLoweringResult reuses existing PhaseResult; a complete payload is carried by its typed envelope. Existing CMP-03 union/discriminator/handoff explicitly supports compiled-type-ir with exact origin/scope/original name and full field preservation. Existing CMP-02 diagnostics carry actual phase, exact semantic/field targets and independent IR identity.

Original canonical snapshot/evidence and completed executed preparation gate lowering without rerunning validation. Source definitions are actual original immutable MOD-04 members. Field identity/name/order/type refs/constraints and precise decimal values are preserved. Multi-type processing follows original canonical order and collects deterministic diagnostics; any failed/incomplete type emits no partial output set. Missing DataFacet is incomplete; explicit empty present DataFacet supported. Explicit IDs required; duplicate IR identity handled by existing commit guard. No default phase registration or final artifact generator.

## Changed files

Production modified (1):

- `platform/compiler/compiler-core/src/compiler_core/public.py`

Documentation created (3):

- `docs/compiler/compiled-type-ir.md`
- `docs/architecture/decisions/ADR-0035-compiled-type-ir.md`
- `docs/architecture/cmp04-verification.md`

Documentation modified (5):

- `README.md`
- `docs/architecture/repository-structure.md`
- `docs/architecture/dependency-rules.md`
- `docs/compiler/compiler-foundation.md`
- `docs/compiler/semantic-ir-envelope.md`

Repository archive created (3):

- `test-archive/CMP-04/README.md`
- `test-archive/CMP-04/CMP-04-deferred-tests.md`
- `test-archive/CMP-04/CMP-04-deferred-test-spec.md`

Total: **12** changed files. No automated test/scenario/demo files or test infrastructure. The sole complete detailed specification is [CMP-04-deferred-tests.md](../../test-archive/CMP-04/CMP-04-deferred-tests.md); README/navigation meet standing archive requirements without duplicate scenarios. Previous archive scenarios and genuine historical verification records are preserved.

## Executed static checks — separate from tests

| Check | Actual outcome | Evidence scope |
|---|---|---|
| `python3 scripts/dev.py lint` | Completed successfully | Syntax/whitespace/static architecture |
| `python3 scripts/dev.py build` | Completed successfully | Syntax/boundaries/public MODULE_NAME imports |
| `python3 scripts/dev.py fitness:json --output build/cmp04-fitness.json` | HEALTHY; 44 rules, 0 failed/warnings/exceptions/suppressed/cycles | 9 modules / 45 production sources |
| `python3 scripts/dev.py dependencies:json` | Completed, no cycles | Existing import/manifest graph unchanged |
| `git diff --check` | Completed successfully | Diff formatting |
| Markdown archive inspection | 157 unique stable IDs and 157 deferred scenario statuses | Document count/completeness |
| Package metadata | Python 3.12.14 / PyYAML 6.0.3; Django/DRF absent | Metadata only |

Static checks were repeated after source edits and source inspected. No lowerer, compiled payload/envelope, compiler phase, validation pipeline or Mini Sales scenario was instantiated/executed. No pytest/unittest/manage.py tests, CLI/runtime smoke, custom scenario scripts, deferred cases or executable examples ran. Static success **does not establish behavioral correctness**.

Existing workflow `DEFER_COMPREHENSIVE_TESTS=true` remains unchanged. Inspect actual push/PR comprehensive/smoke step skips before merging and report them as skipped; green CI does not mean deferred tests passed. Starting local source tree equals remote CMP-03 main tree `b1b9052a0edbeea44a03a46bc7cf6954b98cb376` (main `ed0a47150af8b671f96d5d52860e979e2d672916`).

## Decisions and limitations

- Actual MOD-04 TypeDataComposition/one DataFacet is reused; full TYPE-01/general SK-11/richer facet contracts remain unavailable. No silently reconstructed semantic type/module or unsupported facet omission is claimed. Richer facet/HTTP/SK-11 integration cases remain blocked until actual owner contracts exist.
- Field reference and constraint IR are aliases of current closed immutable TYPE-05/04 values, not contradictory wrappers. Primitive meanings remain unchanged; semantic references stay identity-only ElementRef, source type exact ElementVersionRef. No latest/exact field pin selection, lookup, recursive graph or target mapping.
- Presence/nullability remain independent. All supported precise constraint values and canonical field order retained. Structural collection checks reuse DataFacet; TYPE-06/MOD-08 remain the sole semantic validation owners.
- Identity/evidence/member/preparation association is trusted in-process, not authenticated/portable proof or permissions. Direct lowerer is an internal guarded composition API; production entry is original ModelCompiler with explicit phase. No Boolean evidence or authoring route.
- Missing DataFacet is INCOMPLETE, not fabricated empty. Phase failures/incomplete capability never expose partially lowered fields/type sets. Explicit binding coverage and representation tokens remain caller obligations.
- Envelopes match source context/origin/name/full ordered fields; IR remains intermediate and cannot satisfy final artifact output readiness. Default artifact-build remains INCOMPLETE without a real generator. Preparation-only success is a narrower objective.
- Source sidecar retains original exact definition/field canonical associations; actual source spans/selection remain MOD-03/tooling responsibility, and absent mappings are not fabricated. Existing transport/permissions/default disclosure unchanged.
- No SQL/ORM/DRF serializer/API/UI/runtime generation, migrations, optimization, dependency closure, cache, persistence, publishing, deployment or runtime instances. No module/dependency/profile/activation exceptions or runtime import changes.
- No existing compiler HTTP boundary required modifications. No endpoint created. Future applicable HTTP integration remains actual authorized DRF presentation, outside domain.
- All behavioral assumptions remain unverified despite static architecture success. Explicit future verification requires user authorization, fixed revision and actual prerequisite fixtures/upstream contracts.

## Readiness and stop

Bounded compiled type/field payloads, focused lowering, explicit phase and complete deferred specification are ready for review and next-stage planning under stated gaps. **DEFERRED / NOT VERIFIED** remains authoritative. Stop CMP-04; do not begin CMP-05 automatically.
