# RUN-06 — Runtime Error Model

Date: 2026-10-12. Backend ownership Python / Django / Django REST Framework. **NOT_RUN — DEFERRED / NOT VERIFIED**. New tests0; tests executed0. No error construction/mapping/wrapping/presentation/exception/operation scenario executed.

## Ownership and actual inspection

All new production contracts and adapters live in existing `apps/semantic-instance-runtime/src/semantic_instance_runtime/public.py`, an application composition boundary already allowed to import Kernel/model-core/compiled-contracts/runtime-core. FieldId and canonical InstanceId association belong to model/application owners; putting their shared error composition into runtime-core would require a forbidden model edge. Runtime-core and earlier services never import these application adapters. No new module/edge/zone/profile/activation/CI change or circular dependency. Existing result/service semantics remain unchanged.

Inspected actual Kernel identity/context/version/reference, TYPE-04/05/06 field and validation contracts, MOD-09 aggregation and CMP-02/09 diagnostic associations and reader codes, RUN-01/02 results/diagnostics/exception boundaries, RUN-03/04 canonical/error/evidence/result contracts and RUN-05 context/creation results. General SK-11 Diagnostic/DiagnosticCode/Severity/Report exports are absent; no replacement general diagnostics engine fabricated. Existing narrow RuntimeLoadSeverity reused, original typed runtime diagnostic objects retained as associations. Compiler bridge already exposes RuntimeArtifactReaderDiagnostic and original CMP-09 causes; no compiler import, phase replay or changed compiler result.

Python minimum3.11/local3.12.14/CI3.11,3.12,3.13. Django/djangorestframework metadata NOT_INSTALLED and no existing applicable runtime HTTP response/authentication envelope. No new endpoint, ORM/migration/ModelSerializer/global exception handler, framework initialization or monitoring infrastructure. Django/DRF remains required for applicable future HTTP adaptation outside domain.

## Contracts and semantics

| Contract | Responsibility |
| --- | --- |
| RuntimeErrorDetail | Conflict-safe immutable failure value; does not shadow builtin RuntimeError or inherit Exception |
| RuntimeErrorCode / Category | Closed original machine code and explicit classification, independent of message/severity/HTTP |
| RuntimeErrorOperation | Closed actual load/read/registry/instance/validation/context operation association, no Action execution |
| RuntimeErrorContext | Only actual optional semantic/target/registry/invocation/correlation/cause coordinates; no full ExecutionContext or credentials |
| RuntimeErrorTarget | Original artifact/manifest/exact definitions/canonical identity/FieldId/constraint/revision, no field contents or paths |
| RuntimeErrorDiagnosticAssociation | Original actual existing immutable diagnostic occurrence + source index; not a new generic Diagnostic |
| RuntimeErrorCause / Kind | Flat bounded actual lower failure snapshot or related diagnostic, never a recursive exception graph |
| RuntimeErrorCollection / Policy | Ordered immutable duplicate-preserving failures and explicit omission counts with trusted owner ceilings |
| RuntimeErrorResultAssociation | Observational operation/status/diagnostics/error association, independent detail completeness and original validation completeness; not replacement result |
| RuntimeErrorFactory | Controlled create/wrap/aggregate/map_result/map_expected/from_unexpected, no operation invocation |
| RuntimeErrorPresentationPolicy / PublicItem / PublicView / present_runtime_errors | Pure immutable owner-controlled disclosure projection, no HTTP semantics or authority engine |

The taxonomy includes INVALID_REQUEST, INVALID_STATE, NOT_FOUND, CONFLICT, VALIDATION, AUTHORIZATION, INTEGRITY, COMPATIBILITY, UNSUPPORTED_CAPABILITY, RESOURCE_LIMIT, INFRASTRUCTURE, INTERNAL and UNKNOWN. UNKNOWN explicitly means available detail cannot justify a precise cause. No diagnosis inferred from message, random occurrence ID, timestamp, Python exception class name or localized text. Immutable read-only code/message catalogs are static source definitions, not a mutable error cache or plugin registry.

Reuse all109 original RUN-001…021/101…121/201…222/301…321/401…424 codes exactly. Neutral existing CMP-061…080 reader codes preserved (20 codes). New codes only RUN-501 safe unexpected INTERNAL,502 OSError infrastructure,503 unavailable cause detail,505 nondisclosing public fallback. Unknown factory codes rejected. Raw unknown original reader code remains on actual private diagnostic association; no dynamic public code fabricated.

Code classification explicitly mapped from real boundaries. Required/null/primitive/constraint violations are VALIDATION; registry conflict CONFLICT; load evidence mismatch INTEGRITY; missing evaluator UNSUPPORTED_CAPABILITY; authority conditions AUTHORIZATION; expected exact absence NOT_FOUND. Existing state binding/context mismatch and invalid parent classified INVALID_STATE. Reader-failed RUN-006 consults actual existing lower ERROR reader evidence: known digest/size/integrity mismatch stays INTEGRITY rather than generic invalid model/infrastructure. Other known reader categories preserved where available; no evidence or excessive uninspected category inventory remains UNKNOWN. Classification scans at most1024 retained/original reader occurrences and does not read bytes or execute the reader.

Every safe message is a controlled fixed category template (and public505 template), validated against code/category. No original diagnostic.message or str(exception) becomes a safe message. Severity is actual existing RuntimeLoadSeverity; authoritative status remains separate. Warning/info associations never automatically create fatal error. No HTTP status encoded into domain category/code.

## Result interoperability

Factory.map_result requires an actual supported result and compatible explicit RuntimeErrorOperation. It reads immutable status/diagnostics only; no original result/context/instance/registry mutation or validator/load/registration/context construction. Explicit operation cannot contradict original instance or registry diagnostic operation. Context creation versus derivation must be supplied explicitly because the source creation-result type does not encode method provenance.

Supported results: RUN-01 load; RUN-02 registration, lookup/name inspection, membership, version enumeration, snapshot; RUN-03 create/update and inspection; RUN-04 validation; RUN-05 context create/derive. Original source_status retained as its actual enum, never string-normalized or reclassified. Validation VALID/INVALID/INCOMPLETE and complete flag preserved independently of error retention completeness. Existing RUN-04 INVALID with gaps remains INVALID and complete=false; mapping does not rerun a rule.

Successful/valid/read Missing outcomes contain no added failures; warnings remain original diagnostic references. Lookup NOT_FOUND and AMBIGUOUS are routine outcomes, no fatal errors by default. Optional include_not_found=True creates appropriate expected absence associations without changing source NOT_FOUND; it does not cause registry corruption/retry/latest fallback. AMBIGUOUS stays routine. Failure/incomplete without usable ERROR diagnostic receives controlled503 UNKNOWN; cause knowledge and detail completeness explicitly unavailable, never invented root mismatch. Failed/incomplete reports expose no partial successful state because original result contract remains authoritative.

RUN-03 result.validation_result is an actual known lower report association. Primary operation error retains its mapped validation failures as RELATED_DIAGNOSTIC snapshots, not guessed one-field root causality. Original FIELD/InstanceId/constraint/revision source associations retained. Canonical InstanceId remains the actual existing opaque owner-approved RuntimeInstanceIdentityAssociation; no new concrete identity or instance fabricated. TYPE-08 remains absent.

map_expected accepts existing RuntimeInstanceError create/update and RuntimeArtifactLoadError load/register/snapshot only. It constructs an equivalent non-success existing result for the same actual status/diagnostics/retained lower evidence, then uses the result adapter; no successful result or operation fabricated. Original Python exception object is not stored. Unsupported exception/operation pair rejects. Other services' existing result-returning boundaries are consumed directly.

## Contexts, targets and diagnostics

Pre-context failure needs no invocation. Factory merges actual source coordinates with explicit trusted RuntimeErrorContext only where source lacks coordinates; contradiction raises rather than overwriting scope/invocation. RuntimeErrorContext.from_execution extracts coordinates from an existing actual immutable context without constructing/verifying/executing it. No tenant/organization/name inference or correlation-as-authority.

Targets retain original typed artifact identity/kind, validated bounded original manifest token, exact semantic origins, canonical identity association, FieldId, ConstraintKind and local revision. Original invalid/overlong manifest is not turned into a semantic ID or truncated synthetic token; it is omitted with explicit count, while private original diagnostic remains available. No absolute/relative storage path in target. Limits apply to exact-definition tuple; original order preserved, no last-write-wins. No target authorization/disclosure contract currently exists, so public projection omits all targets.

Original typed load/reader/instance/validation/context diagnostics retained repr-hidden with occurrence index. Messages, private reader paths, source details and canonical identity representation can be sensitive internally; they are never serialized by public projection. Actual immutable source references are shared without copying arbitrary text or source graphs. This is narrow interoperability with actual existing diagnostics, not a duplicate SK-11 or compiler hierarchy. No generic arbitrary diagnostic extension/plugin admission.

## Causes and aggregation

Reader lower ERROR diagnostics and RUN-03 original registry causes establish direct lower associations. Warning/info lower conditions are RELATED_DIAGNOSTIC, not direct failure causes. Registry causes preserve actual registry operation when known; reader cause carries actual ARTIFACT_READ operation without introducing a compiler dependency. Lower unknown code preserved only as actual private association, code=None/UNKNOWN, no made-up cause.

Factory.wrap requires an actual lower RuntimeErrorDetail. Direct bounded snapshot + flat retained deeper snapshots carry depth, original operation/context/target and first actual diagnostic when present. No recursive RuntimeError pointer, exception object, full ancestor context or graph service. Obvious structural cycles cannot be represented by this closed nonrecursive shape; repeated codes/targets are not incorrectly rejected as cycles because no unique occurrence ID exists. Existing causal depths increment; beyond owner/hard depth counted as omitted. Shared correlation or invocation causation never automatically creates error cause.

Aggregation accepts ordered source collections and appends in caller-declared operation-stage/source-result order; preserves upstream diagnostic order and duplicate occurrences even equal messages. No set ordering, localized sort, clock/thread completion order/pointer certificate or deduplication. Limits bound errors, diagnostic refs, target refs, cause count/depth and controlled messages; every omitted item has explicit count. Detail completeness describes retained known detail, not discovery of all root causes, operation success or validation completeness. UNKNOWN classification or an unknown related cause is explicitly not complete. No silent internal truncation or false-success mapping.

Default owner budgets:128 errors,256 diagnostics,32 causes,depth8,128 exact targets,256 controlled-message characters. Hard bounds1024 errors/diagnostics,128 causes,depth32/targets128,1024 message chars; policy requires all controlled templates fit and never trims code/message semantics. Referenced original source data already exists and is immutable; retention bounds are not CPU/RSS quotas or source-payload-size proof. Large diagnostic sources still incur scanning costs; no new copies of raw field/artifact data.

## Unexpected failures and public boundary

from_unexpected is an explicit outer application boundary transform of an already observed exception, not broad catches installed around domain services. OSError→502 INFRASTRUCTURE, other genuine Exception→501 INTERNAL. No exception name/text/traceback/source object retained; actual supplied trusted coordinates may remain. Existing expected narrow runtime rejections must use map_expected and cannot be relabeled INTERNAL.

KeyboardInterrupt/SystemExit/asyncio cancellation BaseException, concurrent futures cancellation and all exception groups re-raised unchanged. No process termination/cancellation swallowed. Arbitrary client object claim rejected. Caller retains existing logging/rethrow policy outside transform; no new logger/global handler, retry/recovery/fault masking, automatic events or monitoring. No recoverability guarantee.

Public projection defaults to one generic stable505/UNKNOWN controlled item, no correlation or targets/diagnostics/causes/context/exception. Explicit trusted server policy may allow specific known codes/categories and an already authorized correlation coordinate that exactly matches the internal error. Policy is a presentation choice, not user authorization; external request fields must never configure it. Even with allowlist, targets and causal details remain excluded because no actual target-disclosure contract exists. Public limited flag is explicit for redaction/omission/capacity limits, without changing internal source status or claiming complete detail.

HTTP statuses/envelopes/authentication/permissions/403-versus404 nondisclosure remain at the actual application/DRF boundary. No applicable existing interface was found; none fabricated. Default generic view prevents accidental exact-resource/authority leakage; any detailed-code disclosure must be selected by genuine approved application conventions later.

## Conditional Mini Sales

Reuse actual existing UUID source definitions, not typ_customer_123/fld_name prompt tokens. Customer `sem_550e8400-e29b-41d4-a716-000000000001@1.0.0`, Employee `sem_550e8400-e29b-41d4-a716-000000000002@1.0.0`, sales context `sem_550e8400-e29b-41d4-a716-999999999999`. Actual FieldId source UUIDs from [Mini Sales](../../examples/authoring/mini-sales.json).

Exact Customer2.0.0 absent stays NOT_FOUND, no1.0.0 fallback; optional error code114/categoryNOT_FOUND only when consumer needs it. Conflicting Customer1.0.0 registration code112/CONFLICT. Required name Missing RUN-309/VALIDATION, Null credit RUN-310/VALIDATION with original FieldId, unavailable decimal evaluator RUN-319/UNSUPPORTED_CAPABILITY and original INCOMPLETE retained. Known negative credit plus absent evaluator stays INVALID/complete=false with both known error types. Employee reader CMP-074 linked to RUN-006 preserves INTEGRITY and actual reader cause, no absolute path public. Execution semantic scope mismatch404/INVALID_REQUEST; missing authority410/AUTHORIZATION with original INCOMPLETE, no invented context. Actual supplied invocation/correlation may be retained, never interpreted as causality or permission.

These are future conditional associations of genuine original outcomes, not executed examples. No fabricated decoder/canonical instance/trusted decision/fault experiment, no value validation/update/load/register/context operation repeated. All current TYPE-08/schema/principal/authorization/evaluator gaps remain unchanged.

Exactly one [deferred archive](../../test-archive/RUN-06/RUN-06-deferred-tests.md), [ADR-0047](../architecture/decisions/ADR-0047-runtime-error-model.md), [completion/static record](../architecture/run06-verification.md). Ready for source review and later explicitly authorized behavioral verification and genuine missing integration. Stop RUN-06; no RUN-07.
