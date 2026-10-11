# RUN-03 — Completion and deferred verification record

Date: 2026-10-11. Task: Semantic Instance Runtime. **DEFERRED / NOT VERIFIED**. New executable tests **0**, deferred tests executed **0**. No manual/custom instance create/update/inspect, registry/snapshot, adapter, evaluator, concurrency or Mini Sales scenario was executed.

## Implemented source components

One new pure Python application composition module, `semantic-instance-runtime`. Production files created:

- `apps/semantic-instance-runtime/src/semantic_instance_runtime/__init__.py` — package only; no startup.
- `apps/semantic-instance-runtime/src/semantic_instance_runtime/public.py` — service/protocols, immutable requests/results/views, context, policy/revision metadata, exact RUN-02 lookup/coherent view, separate instance authority, original schema association, safe FieldId handling, canonical value projection/normalization, supported primitive/bound/length checks, explicit missing evaluators/reference rejection, complete conditional canonical construction, update and inspection, runtime-style diagnostics.

No production core file is changed. `architecture.json` declares the application module and its four existing allowed public edges: Kernel, model-core, compiled-contracts, runtime-core. Existing core dependencies/policy/profiles/activation/CI/executable tests remain unchanged. Application composition is necessary to reuse model FieldId without a forbidden model dependency in runtime-core.

Documentation created: [runtime contract/conditional Mini Sales](../runtime/semantic-instance-runtime.md), [ADR-0044](decisions/ADR-0044-semantic-instance-runtime.md), this record and the sole test archive. Updated: `AGENTS.md`, root `README.md`, `apps/reference-mini-sales/README.md`, architecture index/dependency rules/repository structure. No framework install, HTTP endpoint, serializer engine, ORM model/migration or storage adapter.

## Architecture and capability decisions

Actual TYPE-08 canonical SemanticInstance/InstanceId/Missing/Null/Value **do not exist** in this revision. Opaque Protocols and trusted approval/adapter ports preserve their future ownership; no concrete competing canonical representation or successful fixture is fabricated. Metadata wrapper retains the original canonical instance, original runtime definition and local revision only. Integration reuse cannot be claimed complete until authoritative TYPE-08 exists.

No real RUN-01 domain decoder/producer/authority or RUN-02 definition extraction/kind/authority exists. Current loaded immutable graph does not admit model Enum leaves; no real loadable original FieldDefinition tuple is demonstrated. Complete runtime schema approval, source tuple association and capability gates fail closed. No reconstructed TypeDefinition/CanonicalModel or compiler IR fallback.

One authorized exact RUN-02 lookup per operation; explicit supplied snapshot must contain that same original entry. Separate request-bound instance permissions for create/update/read; no Boolean authority, tenant/QName inference or register/load-right substitution. Defaults are unavailable.

Existing FieldId/presence/nullability/TYPE-05 references/TYPE-06 applicability retained. Approved canonical value classes distinguish Missing/Null/Value. Exact immutable primitive projection; no bool/int confusion, DateTime/Date confusion, string parsing, float Decimal bridge or default generation. Simple inclusive numeric bounds and native string code-point length are implemented. Pattern/Precision/Scale require an explicit approved bound evaluator; current evaluators absent and reference Value assignments unsupported. Missing mandatory evaluator is INCOMPLETE even for optional Missing.

Create validates full state before canonical construction and rechecks complete output. Updates validate original exact binding/context, expected local revision, complete changes and output before returning a new canonical object; old object is untouched. Empty/equal updates also create new object/revision+1. Revisions are local lineage metadata, not SemanticVersion/global CAS/store uniqueness. Default maximum revision 2^63−1; no wrap. Authorized inspect distinguishes known Missing from unknown FieldId and exposes no values on rejection. No persistent state, events, business actions, activation or execution engine.

RuntimeInstanceDiagnostic is a narrow missing-SK-11 association seam reusing current runtime severity/status and original RUN-02 causes. RUN-201…222 preserve typed scope/definition/FieldId/constraint/operation/revision and approved canonical identity where known, without field contents or invented source coordinates. Unexpected adapter programming faults propagate, without partial successful state.

## Deferred archive

Directory: `test-archive/RUN-03/`.

Exactly one file: [RUN-03-deferred-tests.md](../../test-archive/RUN-03/RUN-03-deferred-tests.md).

**200** stable IDs RUN-03-T001…RUN-03-T200: **163** required categories A–V scenarios and **37** implementation-specific scenarios. Every case has component/objective/prerequisites/input/expected behavior/diagnostics/boundaries/integration/acceptance/status, all **NOT_RUN — DEFERRED**. No archive README/additional spec, executable test infrastructure or existing test modifications. Current prerequisite blockers are documented without treating conditional success as actual output.

Future execution requires explicit later permission, fixed revision, genuine canonical/schema/load/registry/authority/evaluator integrations and real safe fixtures. No placeholder class/decoder/permission can turn a missing architectural dependency into verified success. Tests remain deferred.

## Essential static checks

Source syntax/whitespace/architectural lint and build/public MODULE_NAME imports succeeded. Marker imports define contracts only and instantiate no service/registry/instance or adapter. Dependency/architecture fitness **HEALTHY**: **44** static rules, **12** modules, **51** production Python sources, **0** failures/warnings/exceptions/suppressions/cycles. Diff formatting and archive field/ID/status/local documentation link checks are separate static/document inspections.

Python minimum **3.11**, local **3.12.14**, CI matrix **3.11/3.12/3.13**. Django/djangorestframework metadata **NOT_INSTALLED**. No actual authenticated applicable API workflow exists; no new endpoint or ORM/ModelSerializer integration is created. Selected Django/DRF backend ownership is preserved outside pure application/domain contracts.

CI `DEFER_COMPREHENSIVE_TESTS=true` is unchanged. Before merge require six actual completed SUCCESS push/PR static jobs, nine skipped comprehensive/runtime/smoke steps each (**54 skips**). Static green CI does not verify instance semantics. Exact merged PR/main/tree evidence is reported only after actual remote checks.

## Limitations and readiness

Production conditional orchestration and explicit fail-closed boundaries are implemented; **actual TYPE-08/schema/authority/end-to-end integration remains blocked**, not finished or verified. Full TYPE-01/SK-09/SK-11 remain gaps. Port admission currently supports frozen/slotted canonical dataclass variants; any actual future TYPE-08 format/revision must be reconciled rather than overridden. Canonical/schema/evaluator adapters are trusted pure owner code; local immutable/object-association guards are not cryptographic provenance or a sandbox.

Default budgets: 1024 fields, 100000 graph nodes, depth32, 1048576 scalar units, plus canonical identity association ceilings1024 nodes/depth16/4096 units. Repeated graph/provenance checks incur bounded-count traversal cost, not exact RSS/latency limits on trusted adapter code. No instance persistence/uniqueness registry or cross-process state coordination. Optional snapshot membership alone does not confer operation authority or activation.

Ready for source review and later explicitly authorized missing-prerequisite integration/behavioral verification. Semantic runtime/immutability/authorization/concurrency behavior is **NOT VERIFIED**. Stop RUN-03; RUN-04 is not started.
