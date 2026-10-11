# CMP-03 — Implementation and static inspection record

Date: 2026-10-11. Task: Semantic IR Envelope. Status: **DEFERRED / NOT VERIFIED**. Automated tests implemented: **0**. Deferred tests executed: **0**. Documented future scenarios: **147**, all **NOT_RUN — DEFERRED**.

## Implemented contracts

Existing compiler-core implements SemanticIRId, SemanticIRSchemaVersion V0, SemanticIRPayloadKind, closed SemanticIRFoundationPayload / SemanticIRPayload, SemanticIRCanonicalInput, SemanticIREnvelope, thin factory, SemanticIREnvelopeError and SemanticIRHandoff. Exact original request/evidence/snapshot/context, ordered origins and optional existing source/producer associations are retained. Expected integrity/commit/consumer failures use existing compiler codes CMP-011..020 and CMP-02 associations; phase failure adapts to existing CompilationPhaseResult.

Minimal trailing IR tuples/outcome evidence extend existing phase result/state; future producers explicitly declare EMIT_IR. Existing coordinator verifies candidate origin/context/duplicates before atomic IR/artifact state commit. Consumer boundary requires original committed envelope and actual completed/executed producer prerequisite evidence. No default IR-producing phase, lowering/optimizer or final output is added. IR cannot satisfy artifact objective/capability.

Authoring details carry only optional bounded IR identity token projection. Existing model-loader transport adds default-hidden `include_ir_identities` opt-in; payloads remain compiler-local. No new module/profile/dependency/activation/runtime edge, API, ORM or migrations.

## Changed files

Modified production files (3):

- `platform/compiler/compiler-core/src/compiler_core/public.py`
- `platform/model/model-authoring/src/model_authoring/public.py`
- `tools/model-loader/src/model_loader/public.py`

Created documentation (3):

- `docs/compiler/semantic-ir-envelope.md`
- `docs/architecture/decisions/ADR-0034-semantic-ir-envelope.md`
- `docs/architecture/cmp03-verification.md`

Modified documentation (5):

- `README.md`
- `docs/architecture/repository-structure.md`
- `docs/architecture/dependency-rules.md`
- `docs/compiler/compiler-foundation.md`
- `docs/compiler/compilation-diagnostics.md`

Created archive (3):

- `test-archive/CMP-03/README.md`
- `test-archive/CMP-03/CMP-03-deferred-tests.md`
- `test-archive/CMP-03/CMP-03-deferred-test-spec.md`

Total: **14** changed files. No automated tests, executable examples, custom scenario runner or demonstration producer/consumer phase files. The sole complete detailed scenario document is [CMP-03-deferred-tests.md](../../test-archive/CMP-03/CMP-03-deferred-tests.md); archive README/navigation satisfy the standing repository workflow without duplicating scenarios. Prior archives/history preserved.

## Executed static checks — separate from deferred tests

| Check | Actual outcome | Scope |
|---|---|---|
| `python3 scripts/dev.py lint` | Completed successfully | Syntax/whitespace/static architecture |
| `python3 scripts/dev.py build` | Completed successfully | Syntax, dependency boundaries and public MODULE_NAME imports |
| `python3 scripts/dev.py fitness:json --output build/cmp03-fitness.json` | HEALTHY; 44 rules, 0 failed/warnings/cycles/exceptions/suppressed | 9 modules, 45 production sources |
| `python3 scripts/dev.py dependencies:json` | Completed; no cycles | Existing dependency declarations/observed import graph |
| `git diff --check` | Completed successfully | Diff formatting |
| Markdown inspection | 147 unique stable IDs, 147 deferred scenario statuses | Archive document count/completeness |
| Installed package metadata | Python 3.12.14, PyYAML 6.0.3, Django/DRF unavailable | Metadata inspection only |

Source changes were reinspected and static syntax/build checks repeated after changes. No canonical request, envelope, factory, handoff, compiler/validation pipeline scenario or Mini Sales demonstration was instantiated/executed. No deferred suite, CLI smoke/runtime, pytest/unittest/manage.py test, fixtures or custom scenario script ran. Successful static checks **do not establish semantic/behavioral correctness**.

The existing CI workflow's `DEFER_COMPREHENSIVE_TESTS=true` remains unchanged. Before automatic merge inspect actual push/PR jobs and comprehensive/smoke steps; report skipped steps as skipped, never passed deferred tests. Local starting tree matched remote CMP-02 main tree `290e87334e78ca1158e1721484c9795c4b64078a` (main `706aa90755b6b058ee92cc8355aa63bf80bc7eb3`).

## Decisions and risks

- Identity is explicit, deterministic by caller policy and scoped to one original CompilationRequest; no global registry, random ID, memory-address-derived token, QName/filename or artifact/semantic identity reuse.
- Schema is explicit V0 enum only. Payload contract is a narrow deeply immutable coordinate inventory, not full domain IR. Missing payload fails; explicitly model-wide empty inventory remains intermediate.
- Input/evidence/request and committed-envelope association use existing trusted in-process identity. This is not semantic equality, authenticated provenance, portable content hash/serialization or distributed snapshot binding. Manual typed state/outcome assertions remain caller obligations.
- Envelope/input association are unhashable; declared value equality requires same original request association. Payload/origin/source order is retained; committed state order is explicit ordinal representation-token order. Duplicate ID rejects even equal payloads.
- General SK-11 factory/severity contract and full TYPE-01/domain IR are missing upstream; current diagnostic/severity contracts are reused with no universal substitute. Future compatibility cases remain blocked until actual contracts exist.
- Optional source seam uses original approved canonical associations; physical spans and source selection remain MOD-03/tooling responsibilities. Missing/ambiguous mappings are unavailable. Authorized optional IR identity disclosure/redaction remains application caller responsibility.
- No lowering/optimization/generator/serialization/persistence/cache/publisher/deployment/runtime/API/database is implemented. Default artifact-build remains INCOMPLETE; intermediate inventory does not grant publishability or capabilities.
- No existing compiler HTTP route requires modifications. No endpoint/serializer/ORM/migration/dependency upgrade was created; future applicable backend HTTP integration uses actual authorized DRF adapters.
- All new behavior remains **NOT VERIFIED**; source/import/architecture inspection is not execution evidence.

## Readiness and stop

Bounded CMP-03 envelope/construction/internal handoff and complete deferred specification are ready for review and next-stage planning, subject to missing upstream payload/SK-11/portable evidence contracts and unverified behavior. Future execution requires explicit user authorization, pinned revision and actual prerequisite fixtures/evidence. Stop CMP-03; do not begin CMP-04 automatically.
