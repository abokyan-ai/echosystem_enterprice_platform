# CMP-06 — Implementation and static inspection record

Date: 2026-10-11. Task: Deterministic Compilation. Status: **DEFERRED / NOT VERIFIED**. Automated tests implemented: **0**. Deferred tests executed: **0**. Documented future scenarios: **139**, all **NOT_RUN — DEFERRED**.

## Implemented components

Existing ModelCompiler now captures admitted immutable phase fields and implementation classes in addition to descriptor/order. Pure frozen phase dataclasses with closed explicit value options required; no mutable/live/unordered option framework. CompilationConfigurationError remains ValueError-compatible, retaining structured CMP-029 constructor diagnostics for ambiguous/unsupported configuration. Actual captured drift yields CMP-030 with original CMP-02 origin/phase. Preflight before any execution; recheck after each valid phase result, retain original diagnostics and refuse output commit on drift. Mutating another phase also records executing-phase failure. Original gate, sequential orchestration, prerequisite blocking and immutable atomic commit retained; no alternate engine/policy-disable/scheduler.

TypeCompilerPass copies and normalizes explicit binding mapping by exact semantic-ID/numeric-version; existing canonical type/field/diagnostic order and caller-owned CMP-03 tokens preserved. No lowerer/IR/schema/reference/constraint duplication. Current pure transforms have no ambient environment reads or global counters, no registry expansion.

CompilationResultEquivalence supports explicit requests/configurations/results/states/IR comparison using actual MOD-04 supported-content and existing immutable payload equality. Original accepted evidence/ownership/handoff remain identity-bound; comparison cannot authorize them. Preserve status/target/semantic scope, ordered phase outcomes/diagnostic codes/associations and ordered IR/payloads. Human messages/reasons/source locations are excluded from semantic comparison, retained in reports. Result comparison alone cannot establish input equality or compare internal IR not exposed by result. Artifact payload comparison explicitly unsupported, ValueError rather than metadata-based claim. No portable implementation version/byte/hash guarantee.

## Created and modified repository files

Production modified (1):

- `platform/compiler/compiler-core/src/compiler_core/public.py`

Documentation created (3):

- `docs/compiler/deterministic-compilation.md`
- `docs/architecture/decisions/ADR-0037-deterministic-compilation.md`
- `docs/architecture/cmp06-verification.md`

Documentation modified (6):

- `README.md`
- `docs/architecture/repository-structure.md`
- `docs/architecture/dependency-rules.md`
- `docs/compiler/compiler-foundation.md`
- `docs/compiler/type-compiler-pass.md`
- `docs/compiler/semantic-ir-envelope.md`

Repository archive created (3):

- `test-archive/CMP-06/README.md`
- `test-archive/CMP-06/CMP-06-deferred-tests.md`
- `test-archive/CMP-06/CMP-06-deferred-test-spec.md`

Total: **13** changed files. [Sole detailed deferred scenario document](../../test-archive/CMP-06/CMP-06-deferred-tests.md); README/navigation meet standing archive policy without duplicate scenarios. No automated tests/example runners/test infrastructure created or modified; previous cases/genuine history preserved.

## Executed static checks — not deferred-suite verification

| Check | Outcome | Evidence scope |
|---|---|---|
| `python3 scripts/dev.py lint` | Completed successfully | Syntax/whitespace/static boundaries |
| `python3 scripts/dev.py build` | Completed successfully | Syntax/boundaries/public MODULE_NAME imports |
| `python3 scripts/dev.py fitness:json --output build/cmp06-fitness.json` | HEALTHY; 44 rules, 0 failures/warnings/exceptions/suppressed/cycles | Existing 9 modules / 45 production sources |
| `python3 scripts/dev.py dependencies:json` | Completed; 0 cycles | Actual import/manifest graph |
| `git diff --check` | Completed successfully | Formatting only |
| Archive Markdown inspection | 139 unique IDs / 139 deferred case statuses | Specification count/completeness |
| Package metadata | PyYAML 6.0.3; Django/DRF absent | Installed metadata only |

Static checks repeated after source edits, with source inspected. No compilation/equivalence/configuration-fault/validation/IR/Mini Sales scenario instantiated or executed. No pytest/unittest/manage.py tests, CLI/runtime smoke or custom repeated-run scenario script. Public imports establish basic loadability only, not domain correctness. Static success does not mean deferred tests passed.

Unchanged CI DEFER_COMPREHENSIVE_TESTS=true. Inspect actual push/PR jobs and nine skipped comprehensive/runtime steps per each job before merging; report skips rather than test passes. Starting local tree matches CMP-05 remote main tree `cc71b80875f4d386f0e2563393720360f46dac2e`, main `46f87796622c535c145db28a141572ca7763a20d`.

## Decisions, risks and limitations

- Mandatory rules enforced through original contracts; no redundant policy configuration switch. Explicit ordered composition is semantic; duplicate/forward/cyclic configured prerequisites reject instead of arbitrary scheduling. Missing prerequisite stays INCOMPLETE/unexecuted.
- Frozen dataclass/value vocabulary deliberately tightens phase extension admission. Mutable legacy external phases/fixtures require future authorized adaptation. Actual built-in preparation/type pass remain compatible. Historical executable tests untouched; no claimed behavioral compatibility for unadapted mutable extensions.
- Runtime guard detects captured fields/descriptor/class/composition drift. Cannot certify arbitrary third-party methods, hidden class/ambient state, monkeypatching or deliberate mutation inside trusted frozen leaves; actual implementation purity remains an obligation. Separate in-process class comparison is not portable compiler version identity.
- MOD-04 equality covers current closed captured type/data content, not full absent TYPE-01/richer facets. General SK-11 remains missing; actual CMP-02 diagnostic seam reused. Same membership/count/name alone never proves content. Original accepted state/evidence are trusted in-process, not authenticated provenance or permission.
- Semantic result-observable comparison excludes human/source presentation and validation reports. Failed results do not retain successful preparation or input request; establish actual request/configuration equivalence separately. Internal IR comparisons use explicit state/envelopes; no final-result expansion. Unknown concrete artifact equality fails explicitly rather than implying complete reproducibility.
- Multiple exact versions, numeric order, field order, precise decimals and versionless self/mutual refs preserved. Phase IR canonical order differs legitimately from identity-sorted committed state. No latest/recursive graph/registry mutation.
- Current artifact-build remains INCOMPLETE without final generator. Empty type work is narrow completion. No target-specific generator, serialization/fingerprint/hash/cache/worker/distributed scheduling/storage/publishing/deployment/runtime introduced.
- Django/DRF absent; no applicable compiler HTTP boundary, API/authentication/permission modification, new endpoint, ORM/migration or dependency/module change.
- All semantic/failure/environment/concurrency assumptions remain unverified. Future cases require explicit execution instruction, fixed source/implementation, actual original evidence/configuration fixtures and actual owner contracts for blocked integrations.

## Readiness and stop

Supported immutable configuration, deterministic existing orchestration/type integration and bounded semantic comparison are implementation-ready for review and next-stage planning under stated limits. [Contract/unexecuted Mini Sales](../compiler/deterministic-compilation.md), [ADR-0037](decisions/ADR-0037-deterministic-compilation.md). **DEFERRED / NOT VERIFIED** remains authoritative. Stop CMP-06; do not begin CMP-07 automatically.
