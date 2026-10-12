# RUN-06 — Completion and deferred verification record

Date: 2026-10-12. Task: Runtime Error Model. Backend Python / Django / Django REST Framework. **NOT_RUN — DEFERRED / NOT VERIFIED**. New executable tests0, tests executed0. No error construction/mapping/wrapping/presentation/exception experiment or archived case executed.

## Production components and source files

Only production source modified: `apps/semantic-instance-runtime/src/semantic_instance_runtime/public.py`.

Implemented/exported RuntimeErrorDetail (avoids builtin RuntimeError shadowing), RuntimeErrorCode/Category/Operation/Context/Target/DiagnosticAssociation/CauseKind/Cause/Collection/ResultAssociation/Policy/Factory and RuntimeErrorPresentationPolicy/PublicItem/PublicView/present_runtime_errors. Factory methods actual create/wrap/aggregate/map_result/map_expected/from_unexpected; no interfaces-only placeholder. Source runtime services and their authoritative results/statuses unchanged.

Closed read-only mapping covers109 original RUN codes plus20 actual neutral CMP reader codes; controlled fallbacks501 INTERNAL/502 OSError infrastructure/503 unknown detail/505 public nondisclosure. Existing RuntimeLoadSeverity and original typed diagnostic sources reused, not a new generic Diagnostic or competing severity. Runtime Error taxonomy explicit, known digest mismatch retains reader INTEGRITY, unknown detail remains honest UNKNOWN. Constant safe templates, no str(exception)/message-derived code.

Application placement reuses current four governed dependencies and owned FieldId/canonical identity associations without forbidden runtime-core→model import or upstream runtime→application dependency. No module/dependency/zone/profile/policy/activation/CI changes or cycle. No new production file/module;12 modules/51 source files retained. Compiler neutral bridge preserves actual CMP diagnostic causes without new compiler import/phase execution. General SK-11 is absent; no fake canonical diagnostic/report contract created.

Typed optional context/targets preserve source coordinates, source contradiction rejected. Flat nonrecursive known cause snapshots and original diagnostic occurrence refs; warnings RELATED rather than direct failure cause, shared correlation not causal evidence. Ordered duplicate-preserving aggregation, explicit omission counts/bounded depth, retention completeness independent of status/root-cause discovery.

All actual load/registry/instance/validation/context result families mapped observationally with explicit compatible operation. Original NOT_FOUND/AMBIGUOUS routine, INVALID/INCOMPLETE/VALID and validation complete unchanged. RUN-03 actual retained validation report becomes related evidence; no rule/value operation rerun. Expected narrow exceptions project equivalent non-success result only. Unexpected transformation explicit outer boundary only; expected exceptions not INTERNAL, process/cancellation/groups re-raised, no new broad catch or logging/retry framework.

Default public projection one generic505 UNKNOWN, no targets/context/causes/source messages/correlation. Trusted server allowlist may choose known code and exact already-approved correlation, no target disclosure contract invented. HTTP/envelope/auth/permission/nondisclosure remain actual application/DRF owner responsibility.

## Architectural documentation

Created [contract/conditional Mini Sales](../runtime/runtime-error-model.md), [ADR-0047](decisions/ADR-0047-runtime-error-model.md), this record and sole deferred archive. Updated AGENTS.md, root README.md, apps/reference-mini-sales/README.md, docs/architecture/README.md, docs/architecture/dependency-rules.md, docs/architecture/repository-structure.md. Earlier archives/source semantic contracts preserved.

No artifact reading/loading/decoding/registration, model/instance validation, context construction, mutable state, persistence, retry/recovery, policy/Action/Event/Workflow/tracing/external monitoring or RUN-07.

## Django / DRF integration

Python minimum3.11/local3.12.14/CI3.11,3.12,3.13. Actual Django/djangorestframework metadata NOT_INSTALLED. No existing applicable runtime API/response envelope or authorization boundary required modification, no endpoint introduced. No ORM/migration/ModelSerializer/global exception handler/framework initialization. Django/DRF remains mandatory future HTTP adapter; pure projection available without assuming HTTP statuses or altering auth/permissions.

## Deferred archive

Directory **test-archive/RUN-06/**. Exactly [RUN-06-deferred-tests.md](../../test-archive/RUN-06/RUN-06-deferred-tests.md); no README/additional archive/executable scaffolding.

**204** stable cases RUN-06-T001…RUN-06-T204: **164** required A–U scenarios +**40** implementation-specific V cases. Every case has objective/component/prerequisites/setup/expected result/diagnostics/boundaries/integration/acceptance/status, all **NOT_RUN — DEFERRED**. New/executed tests **0**; existing test suites unchanged.

Future execution requires explicit later permission, fixed revision and genuine actual typed source failures/evidence, trusted owner policies and applicable application permissions. Positive scenarios requiring canonical TYPE-08/decoder/schema/trust/HTTP interface remain BLOCKED until real authorized capability work exists. No placeholder source/authority/instance may demonstrate unavailable architecture as successful.

## Essential static checks

Permitted source syntax/whitespace/architecture lint, marker-only MODULE_NAME imports/build, static fitness/dependencies, AST/table source coverage and Markdown/diff/archive inspection are separate from deferred behavioral verification. No factory/service/context/mapper constructor or method executed. Actual local syntax/whitespace/architecture lint, build/marker-only imports and dependency discovery succeeded. Static fitness HEALTHY:44 rules/12 modules/51 production sources, zero failures/warnings/exceptions/suppressions/cycles. Static AST table review covers all109 original runtime codes;204 archive IDs/fields/statuses/sole-file, local Markdown links and diff formatting valid. Existing executable suites unchanged. No behavioral error mapping executed.

Actual unchanged fitness44 rules/12 modules/51 production sources. CI DEFER_COMPREHENSIVE_TESTS=true unchanged; Actual pull-request matrix has three completed SUCCESS static jobs across3.11/3.12/3.13 and nine deferred comprehensive/runtime/smoke steps each (**27 skips**). No independent push-event run was observed for this head; do not invent six jobs or54 skips. Require the final current PR head matrix to complete successfully with all deferred steps skipped before merge. Skipped tests never passed, static green does not verify runtime mapping. Actual PR/main/tree merge evidence reported after remote verification.

## Risks, limitations and readiness

Production error model/factories/adapters/projection implemented. **Behavior NOT VERIFIED**, source integration assumptions deferred. General SK-11 and canonical TYPE-08/schema/trust/evaluator/source-fixture/API prerequisite gaps retained. No approved target-disclosure contract: targets always hidden publicly, detailed code disclosure requires real server/application approval. Original internal diagnostics may retain sensitive immutable source text; no generic serializer should expose them. Owner-controlled templates protect public view, not authorization or cryptographic origin.

Default128 errors/256 diagnostics/32 causes/depth8/128 target refs/256 safe-message characters. Hard1024 errors/diagnostic refs,128 causes/targets,depth32,1024 controlled chars; limited source-sensitive classification1024 reader occurrences. Original source references shared, not source-memory/CPU/RSS guarantee; scanning already materialized source inventory costs time. UNKNOWN classification/causes have unavailable detail, original code/type preserved privately where unsupported. No durable occurrence ID or automatic logging/recovery, causal graph flat with no recursively representable cycles.

Ready for source review and later explicitly authorized behavioral verification and genuine missing interface/prerequisite integration. Stop RUN-06; no RUN-07 automatically.
