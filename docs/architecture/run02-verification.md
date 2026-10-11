# RUN-02 — Completion and deferred verification record

Date: 2026-10-11. Runtime Model Registry. **DEFERRED / NOT VERIFIED**. Automated tests created **0**. Deferred tests executed **0**. No registration, lookup, snapshot, version/name inspection, concurrency, Mini Sales or custom smoke scenario was executed.

## Actual source and configuration inventory

Production Python modified: **1** file, `platform/runtime/runtime-core/src/runtime_core/public.py`.

Implemented RuntimeModelRegistryScope/Key/Policy, exact ElementVersionRef identity, definition-kind coordinate and explicit approved extraction protocol/catalog, original decoded-node/evidence association, RuntimeModelDefinition, registration request/result, independently bound registry authority, exact lookup/membership/name/version inspection, immutable snapshot/result, LocalRuntimeModelRegistry and private copy-on-write indexes/Lock. Existing runtime diagnostic model gains registry codes/stages and trailing typed associations; existing supported load diagnostic comparison includes them. Existing Kernel QName/Namespace and immutable definition-kind coordinates extend shared graph inspection without granting any decoder/kind approval.

Configuration modified: `architecture-policy.json`, runtime stdlib adds only `threading` for the implemented private Lock. No Thread/worker or background startup. `architecture.json`, module/dependency/activation declarations, constrained loading composition profile, compiler/reader/writer/authoring code, existing executable tests, dependency exceptions and CI deferral are unchanged. Runtime still imports only Kernel/compiled-contracts plus eligible stdlib; no compiler/TypeRegistry/framework/OS/file/network import.

Documentation created: [registry contract and conditional Mini Sales](../runtime/runtime-model-registry.md), [ADR-0043](decisions/ADR-0043-runtime-model-registry.md), this completion record and sole archive. Existing root README/AGENTS, architecture index/dependency rules/structure and reference application notes updated. No API, ORM/migration, new module or placeholder domain decoder/extractor.

## Deferred test archive

Directory: `test-archive/RUN-02/`.

Exactly one Markdown specification: [RUN-02-deferred-tests.md](../../test-archive/RUN-02/RUN-02-deferred-tests.md).

**198** stable cases RUN-02-T001…RUN-02-T198: **151** required scenarios in categories A–U plus **47** implementation-specific cases. Every case documents test ID/scenario/objective/component/prerequisites/input/expected result/diagnostics/boundaries/integration/acceptance/status. Every execution status is **NOT_RUN — DEFERRED**.

No archive README/additional specification, test scaffolds/infrastructure or existing test changes. Future execution requires explicit later user instruction, fixed revision and actual owned RUN-01 producers/decoders/immutable definition nodes/extraction/authority prerequisites before positive membership scenarios; concurrency scenarios need a future controlled authorized harness. Current source/docs inspection is separate, not execution of those archived cases.

## Essential static checks executed

Syntax/whitespace/architecture lint and build/public MODULE_NAME imports succeeded. Public import defines registry classes but creates no registry or thread and runs no registration/lookup method. Architecture fitness **HEALTHY**: **44 static rules**, **11 modules**, **49 production Python sources**, **0** failures/warnings/exceptions/suppressions/cycles. Dependency graph preserves runtime independence; diff formatting clean. Archive field/ID/status/count and local Markdown links inspected as documentation checks.

Local Python **3.12.14**, minimum **3.11**, current CI matrix **3.11/3.12/3.13**. Django/djangorestframework metadata **NOT_INSTALLED**; no framework initialization/test or existing authorized API integration to modify. Selected Django/DRF backend transport ownership remains unchanged.

CI keeps `DEFER_COMPREHENSIVE_TESTS=true`. Before merging, require actual **six** completed successful push/PR static jobs, each with its **nine** comprehensive/runtime/smoke steps **skipped** (**54 skips**). Green static CI is not deferred-suite success. Exact PR/main/tree outcome is reported after remote evidence is checked.

## Architectural decisions and material limitations

Each application-owned instance has an explicit bounded scope allowlist and independent local lifetime. Keys are context+runtime target+exact semantic ID/version, ordering numeric. Multiple versions/identities sharing a name coexist; names return ordered ambiguity, ElementRef always requires a version, enumeration separately authorized. No source loading/decoding/compiler fallback, implicit latest or semantic binding.

Only actual successful RUN-01 evidence with original approved immutable encoded nodes can stage entries. Every artifact needs explicit extraction support; empty catalog defaults INCOMPLETE. Registration authority differs from load/read/activation/execution rights; every inspection needs its own bound grant. Default authorizer is unavailable. Mutation response contains submitted committed IDs, not unrelated post-state snapshot data. In-process frozen contracts/associations are not cryptographic authority tokens or a sandbox against malicious same-process code.

Duplicate batch/existing exact keys, including equivalent records, are rejected without guessed replay equivalence. Private lock checks latest conflicts/capacity and atomically publishes fully constructed immutable state/result; readers capture whole coherent old/new data. Old snapshots remain unchanged. Concurrent winner identity is unspecified. Copy-on-write rebuilds and repeated bounded graph/association checks incur traversal/sorting cost; count budgets are not exact heap/RSS/latency guarantees. Original loaded evidence may retain other decoded source-set members, without copying read buffers or creating an artifact store. Snapshot capacity can be below membership capacity and then full snapshot/name/version enumeration is explicitly unavailable without truncation; exact lookup remains supported.

No real runtime decoder/extractor, approved definition kind or authenticated registry authority exists today; no successful registration or Mini Sales output was fabricated. Full TYPE-01/SemanticInstance/SK-11 and applicable authenticated Django/DRF workflow remain gaps. Each instance/process/worker is isolated; restart loses membership, no persistence/distributed synchronization.

Implementation is ready for source review and later explicitly authorized verification/integration. Runtime and concurrency behavior remain **NOT VERIFIED**. Stop RUN-02; RUN-03 not begun.

Detected malformed internal immutable index shapes, wrong scoped exact keys and duplicate/unordered inspection entries fail with RUN-121, separately from routine absence. These local guards do not audit every private index on every lookup or defend against arbitrary malicious same-process memory mutation; deleted index entries are not guaranteed detectable. Oversized inventories may reject capacity before detailed inspection.
