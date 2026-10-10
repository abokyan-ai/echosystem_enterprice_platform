# MOD-04 — Canonical Model Contract: repository test archive

Task ID/title: **MOD-04 — Canonical Model Contract**. Date: **2026-10-10 (Asia/Riyadh)**.
Testing status: **DEFERRED / NOT VERIFIED**. Each new scenario: **NOT_RUN — DEFERRED**.
Scenarios: **95**. Current-task tests created: **0**. Tests executed: **0**. Pre-existing test code/results preserved.
Single detailed file: [MOD-04-deferred-tests.md](MOD-04-deferred-tests.md).
Standing-name navigation: [MOD-04-deferred-test-spec.md](MOD-04-deferred-test-spec.md).

## Implementation scope and architectural dependencies

Existing model_core.public adds CanonicalModel, explicit closed CanonicalDefinition vocabulary/kind catalog, immutable exact membership lookup/order/comparison, factory/construction result/domain error and intrinsic diagnostics. One explicit SemanticContextRef, caller-selected multiple exact versions, idempotent equal exact membership and atomic conflicting-content/name/scope rejection. Existing TYPE-07 frozen host capture/deep-value admission helpers and immutable semantic values are reused without constructing/wrapping/registering a concrete registry.

Dependencies: actual Kernel IDs/names/context/kinds/versions/references and model-core DataFacet/fields/TypeRef/constraints; source/authoring remain upstream independent contracts. Full TYPE-01 and general SK-11 remain missing, with TYPE-08/full SK-09 incomplete. V0 explicitly uses the existing provisional TypeDataComposition seam; no new TypeDefinition is invented. Future kinds require actual owned contracts/explicit extension. No new module/edge/profile or framework dependency is added; nine-module inventory and five activation markers unchanged.

Production file: [model_core.public](../../platform/model/model-core/src/model_core/public.py).
Contract/Mini Sales documented usage: [canonical-model.md](../../docs/model/canonical-model.md).
Decision: [ADR-0026](../../docs/architecture/decisions/ADR-0026-canonical-model-contract.md).
Exact files/static activities: [mod04-verification.md](../../docs/architecture/mod04-verification.md).

## Conditions for future execution and limitations

Require explicit user authorization, fixed source/archive revisions, Python/module paths, existing immutable domain compositions, recorded scope/exact reference/content comparison/diagnostic evidence and explicit provisional versus reconciled foundation target. No automatic fixture/test infrastructure is introduced. Conditional DRF/source association checks require an actual authorized future adapter and existing security conventions. Preserve stable IDs/history and genuine earlier execution evidence; new archive NOT_RUN does not invalidate historical tests.

Current semantics cover only five captured host values plus optional current DataFacet, not full missing TYPE-01/unknown host attributes/future facets. General SK-11 integration is provisional. Semantic field references remain existing identity-only values while membership is exact; no target binding/closure/global validity claim. Selected name ownership excludes unselected catalog history. Capturing a mutable host is not synchronized concurrent reading. No canonical serialization/hash/model version or source/provenance/tenant metadata bag is supplied. No Django/DRF endpoint/serializer/ORM/migration/DB is added. No resolver/canonicalizer/compiler/runtime/persistence or registry orchestration is performed.

Ready for review and later pipeline design within actual contracts, with semantic completeness/behavioral verification gaps explicit. Stop at MOD-04; no MOD-05 automatically implemented.
