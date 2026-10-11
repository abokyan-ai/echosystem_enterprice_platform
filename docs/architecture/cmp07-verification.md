# CMP-07 — Implementation and static inspection record

Date: 2026-10-11. Task: Runtime Artifact Manifest. Status: **DEFERRED / NOT VERIFIED**. Tests implemented: **0**. Deferred tests executed: **0**. Future documented cases: **144**, all **NOT_RUN — DEFERRED**.

## Implemented components and actual integration

compiled-contracts extends existing artifact key/kind/protocol seams with immutable RuntimeArtifactDependencyRef, RuntimeArtifactMetadata and RuntimeArtifactDescriptor. Typed original exact origins versus explicit model-wide origin, distinct internal artifact dependencies and immutable sorted collections; no payload/digest/location duplication. Kernel-only boundary retained.

compiler-core adds explicit caller RuntimeArtifactManifestId, independent V0 schema, approved concrete RuntimeArtifactKindSupport list, checked compilation association, immutable manifest, existing-status assembly result and RuntimeArtifactManifestAssembler. Default kind support empty; actual final runtime artifact producer/kind absent. No placeholder producer/body/descriptor output created.

Original CompilationResult gains trailing optional CompilationOutputOrigin, excluded from generic comparison/repr/hash; original ModelCompiler attaches exact request/compiler invocation binding for typed requests. Legacy result construction/positionals/status/state/artifact abstraction preserved, but unbound legacy success cannot authorize manifest. Assembly requires original bound SUCCEEDED artifact-build, evidence/canonical object/context/target, exact configured completed/executed outcomes, clean CMP-06 configuration audit and complete actual final artifact collection. Checked association accepts result as InitVar, snapshots descriptors/outcomes, retains origin/input/configuration without retaining result/artifact payload instances.

Descriptor extraction matches explicit actual class/kind approval and metadata, preserves canonical origins, verifies complete inventory, rejects duplicates/missing internal dependency and refuses subset/extra/changed metadata. Self/cycles accepted under v0 membership-only policy; no external dependency/lookup/graph/loading order. Key order and numeric exact origin/dependency membership order deterministic; invalid duplicate tie ordering uses kind/typed origin/dependency values only. Diagnostics identify conflicting keys/kinds/origins and declaring/unresolved dependency targets. FAILED/INCOMPLETE compilation preserved, no partial successful manifest. Caller-supplied existing manifest inventory governs same-original-output scope ID conflicts; no global registry.

CMP-02 actual association adds trailing related_artifact_targets/manifest_identity fields; original diagnostic payload/report retained, existing primary projection unchanged. CMP-06 semantic comparison includes new associations. same_declaration compares supported manifest declaration, not body/byte equality or authorization. Current public bound manifest is in-process; shared descriptors are independent future consumer metadata; actual portable provenance/manifest transport remain downstream prerequisites.

## Created and modified repository files

Production modified (2):

- `platform/contracts/compiled-contracts/src/compiled_contracts/public.py`
- `platform/compiler/compiler-core/src/compiler_core/public.py`

Documentation created (3):

- `docs/compiler/runtime-artifact-manifest.md`
- `docs/architecture/decisions/ADR-0038-runtime-artifact-manifest.md`
- `docs/architecture/cmp07-verification.md`

Documentation modified (6):

- `README.md`
- `docs/architecture/repository-structure.md`
- `docs/architecture/dependency-rules.md`
- `docs/compiler/compiler-foundation.md`
- `docs/compiler/compilation-diagnostics.md`
- `docs/compiler/deterministic-compilation.md`

Repository archive created (3):

- `test-archive/CMP-07/README.md`
- `test-archive/CMP-07/CMP-07-deferred-tests.md`
- `test-archive/CMP-07/CMP-07-deferred-test-spec.md`

Total: **14** changed files. [Sole detailed future specification](../../test-archive/CMP-07/CMP-07-deferred-tests.md); README/navigation satisfy standing policy without duplicate scenarios. No automated test/infrastructure/demo/runner changes. Prior archives/tests/genuine historical evidence preserved.

## Executed static checks — separate from deferred verification

| Check | Actual outcome | Scope |
|---|---|---|
| `python3 scripts/dev.py lint` | Completed successfully | Syntax/whitespace/static boundaries |
| `python3 scripts/dev.py build` | Completed successfully | Syntax/boundaries/public MODULE_NAME imports |
| `python3 scripts/dev.py fitness:json --output build/cmp07-fitness.json` | HEALTHY; 44 rules, 0 failures/warnings/exceptions/suppressed/cycles | 9 modules / 45 production sources |
| `python3 scripts/dev.py dependencies:json` | Completed; 0 cycles | Import/manifest graph |
| `git diff --check` | Completed successfully | Formatting only |
| Archive Markdown inspection | 144 unique IDs / 144 deferred case statuses | Document count/completeness |
| Package metadata | PyYAML 6.0.3; Django/DRF absent | Installed metadata only |

Static checks repeated after source edits and code inspected. No artifact metadata/manifest/assembler/compiler/output-origin/comparison/validation or Mini Sales scenario instantiated or executed. No pytest/unittest/manage.py tests, CLI/runtime smoke/custom scenario scripts. Public imports establish loadability only; no successful manifest/artifact output has been produced or behavior verified.

CI DEFER_COMPREHENSIVE_TESTS=true unchanged. Inspect actual push/PR job results and nine skipped comprehensive/runtime steps in every job before merging; report them as skipped, not passed tests. Starting local tree equals CMP-06 remote main tree `accbd5280900130d6e44f78d604f8eb3c20b97dd`, main `aa8e53d3afdf42c5af6f97c6918b21c5a7a6986d`.

## Architectural decisions, limits and risks

- Current artifact-build target requires real artifacts/all configured success; preparation-only zero-output target is not a runtime manifest objective. No per-type artifact count or future kind schema is invented. Current IR-only build remains incomplete; positive final producer-dependent cases are blocked until actual owned producer/kind exists.
- Explicit existing artifact identity/kind reused; metadata origin/dependency semantics are producer declarations, never inferred from semantic_dependencies or type refs. Dependencies internal membership only; self/cycles allowed, external dependencies absent, no lookup/load solver.
- Runtime kind approval is explicit owner/application trust input matched to exact frozen class; no author token auto-trust, dynamic import, payload execution or metadata dict. Future producer must provide actual closed manifest_metadata. Existing artifact payload immutability is its owner's obligation; manifest retains metadata only and does not claim payload integrity/equality.
- Distinct caller manifest token and strict V0 scoped to original invocation. Caller must supply complete known manifest inventory for uniqueness; no global proof from default empty inventory. Repeated metadata assembly alone is not registry/publication/activation.
- Origin/evidence/configuration associations are original trusted in-process objects, not authenticated/portable snapshots or compiler version IDs. Full TYPE-01/general SK-11/richer facets remain absent. Shared descriptor contracts may support future approved consumers; portable manifest/provenance/serialization/digest/locator standards need owner work before Runtime use. Runtime imports remain unchanged, no dependency on internal type pass/state added.
- Bounded manifest declaration comparison excludes body/byte and human/physical source presentation. Original source sidecars remain optional report enrichment, never identity/authority. New typed related artifact/manifest evidence retained on original CMP diagnostic payload; no speculative HTTP/transport projection created.
- Unexpected implementation defects propagate; no ordinary manifest error hides them. All domain, fault, immutability, completeness and determinism assumptions remain unverified.
- No Django/DRF installed or applicable compiler HTTP adapter; no new endpoint/auth/permission/ORM/migration. No target producer/SQL/UI generation/payload storage/serialization/hash/cache/publishing/activation/deploy/Control Plane authority/runtime loading/execution.

## Readiness and stop

Working bounded manifest contracts, explicit real-artifact assembly/integrity and complete deferred archive ready for review/next-stage planning. Actual successful runtime build depends on future real artifact producer/kind and stronger portable contracts. [Contract/unexecuted Mini Sales](../compiler/runtime-artifact-manifest.md), [ADR-0038](decisions/ADR-0038-runtime-artifact-manifest.md). **DEFERRED / NOT VERIFIED**. Stop CMP-07; do not begin CMP-08.
