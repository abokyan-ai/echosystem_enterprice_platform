# CMP-04 — Compiled Type IR

Date: 2026-10-11. Status: **DEFERRED / NOT VERIFIED**. No lowering/phase/Mini Sales scenario was executed.

## Scope and actual dependencies

Pure Python `compiler_core.public` adds CompiledTypeIR, CompiledFieldIR, CompiledTypeLowerer, CompiledTypeIRIdentityBinding and explicitly composed CompiledTypeLoweringPhase. Existing TYPE-04 FieldConstraintSet and TYPE-05 TypeRef are reused through `CompiledFieldConstraintsIR` / `CompiledTypeReferenceIR` aliases; TypeLoweringResult aliases the existing CompilationPhaseResult. There is no redundant semantic type, constraint, reference, context, diagnostic or result hierarchy.

Full TYPE-01/general SK-11 remain absent. The actual MOD-04 canonical definition is its closed immutable TypeDataComposition with captured five-property type host and optional one DataFacet. Lowering covers exactly this supported host/data representation, not arbitrary semantic elements or unrepresented facets. Additional Action/Event/Policy/Relationship/facet payloads cannot enter current canonical membership; no claim of their compilation or silent omission is made. Extending their upstream ownership/contracts is prerequisite to support. Runtime TYPE-08 instances are not constructed.

Python 3.12.14 and PyYAML 6.0.3 are installed; Django/DRF are unavailable and no applicable compiler HTTP boundary exists. No dependency upgrades, ORM, database migration, HTTP endpoint, serializer generation or framework initialization.

## Immutable payload and preservation

CompiledTypeIR contains exact `type_identity: ElementVersionRef`, original `qualified_name: QualifiedName`, original `semantic_context: SemanticContextRef` and ordered tuple of CompiledFieldIR. Each compiled field carries original FieldId, FieldName, actual TypeRef and actual FieldConstraintSet. These are immutable semantic values, reused without reparsing or name/ID regeneration. Actual exact types protect against arbitrary mutable or custom reference/payload implementations. Caller field lists are copied into tuples.

Primitive references preserve the established String/Boolean/Integer/Decimal/Date/DateTime/UUID meaning. Semantic references preserve TYPE-05's identity-only ElementRef; they are not changed to exact field pins, latest versions, embedded definitions, foreign keys or runtime references. Source type's exact version remains distinct from those versionless field references. Self/mutual references remain references, without lookup/recursion/dependency closure.

Presence and nullability remain independent FieldConstraintSet dimensions for every valid combination. No default constraints, optionality/nullability inference, SQL width/types, ORM blank/null behavior, UI/API labels or target regex semantics. Min/max-length, minimum/maximum, pattern, precision/scale preserve exact existing values and existing kind-sorted enumeration. Decimal constraints retain their actual precise Decimal/int representation; no float conversion or pattern compilation/execution.

CompiledTypeIR reuses DataFacet's intrinsic uniqueness/portability guarantees for IDs, names and ASCII case collisions. It does not duplicate TYPE-06 constraint applicability or MOD-08 rules. Low-level payload construction establishes structural integrity only, not semantic validation or publishability. The envelope additionally compares original source QName and the full ordered field ID/name/ref/constraint structure against the exact canonical member; a caller-constructed changed payload cannot claim the same original validated input.

Explicitly empty present DataFacet produces zero fields. **Absent DataFacet is not empty**: v0 returns INCOMPLETE/CMP-022 and no envelope. No absent facet is fabricated. Current host seam has at most one DataFacet; duplicate/richer facets are rejected by upstream contracts and remain unavailable compilation capabilities.

## Gated focused lowering

`CompiledTypeLowerer.lower(definition, request=..., state=..., identity=...)` accepts the actual original selected TypeDataComposition. The route checks original request's bound VALID/READY evidence using SemanticIRCanonicalInput, current actual preparation model/context and original mandatory prepare outcome COMPLETED/executed=True/PREPARE capability. Boolean validation flags, authoring documents and registry inputs are not accepted. The definition must be the **same original canonical member object**, not a distinct equal composition or another version. No validator/canonicalizer/loader/resolver is invoked.

This lowerer is an internal pure compiler composition API, not a separate HTTP/authorized build entry point. Production callers use the original `ModelCompiler` gate with the explicitly composed type phase. As in CMP-01/03, original evidence/state are trusted in-process values; manually fabricated typed state/outcome/evidence is not authenticated provenance or an authorization certificate.

A successful TypeLoweringResult (existing PhaseResult) carries one SemanticIREnvelope in `.ir_envelopes`; `.ir_envelopes[0].payload` is actual CompiledTypeIR. Failed/incomplete result carries original structured diagnostics and no successful payload/envelope. Every field is preserved in canonical DataFacet order. Expected field integrity failures retain exact owner/FieldId and are collected in field order; no partial successful type IR escapes. Unexpected programming errors propagate without generic catch/stack diagnostics.

## Explicit multi-type phase and identity policy

`CompiledTypeLoweringPhase(identities)` has fixed descriptor `CMP-PHASE-COMPILED-TYPE-IR`, mandatory `CMP-PHASE-PREPARE`, declared EMIT_IR and explicit support for current PREPARATION_TARGET/BUILD_TARGET. Install it only with `ModelCompiler(additional_phases=(phase,))`; no default/global/scan registration is changed. The phase does not replace orchestration or install a target generator.

Every selected canonical definition requires an explicit CompiledTypeIRIdentityBinding(exact reference, SemanticIRId). No representation ID is generated from source name/semantic ID, timestamp, counter or random state. Duplicate source assignments are ambiguous configuration and rejected at construction. Missing assignment is INCOMPLETE/CMP-027; outside-membership assignment is FAILED/CMP-026. Assignment order never changes processing order: definitions follow MOD-04's original canonical ID/numeric-version order, fields their original DataFacet order.

The phase independently processes all selected definitions in canonical order and collects original lowering diagnostics. Any failed type makes phase FAILED; if only unsupported capability/absent facet is incomplete, phase INCOMPLETE. Either case exposes **no partial set of envelopes**, even if other definitions lowered internally. When all types complete, each gets its own immutable payload/envelope; explicit empty canonical membership produces no invented type. The existing CMP-03 commit boundary rejects within/across-phase repeated IR IDs (CMP-020), retains original failure evidence and prevents downstream completion/commit.

## CMP-03 integration and compiler objectives

SemanticIRPayloadKind explicitly extends to COMPILED_TYPE_IR (`compiled-type-ir`). The public payload union is now exactly foundation-coordinate payload or CompiledTypeIR. Schema remains explicit envelope V0; no schema migration or dynamic registry. A compiled type envelope requires exactly one origin equal to payload.type_identity, model_wide=False, matching scope and complete original canonical type structure. Its identity is the caller's independent IR token; its producer is the actual fixed type phase. Original canonical source associations for that exact definition/fields are preserved as optional authoring sidecar.

SemanticIRHandoff accepts either supported discriminator only when the required kind matches actual payload. Foundation/type mismatch fails CMP-017 without conversion. Existing same-request/committed-envelope/completed executed producer/prerequisite checks remain. Source spans stay MOD-03/model-loader; no source line or path enters semantic/IR identity.

IR is intermediate. A successful type-lowering phase does **not** mean artifact-build succeeded. With no actual final generator, the original artifact-build result remains INCOMPLETE/CMP-010 and exposes no final artifacts. A caller explicitly selecting foundation-preparation can complete that narrower objective with typed internal IR, without claiming publishability. Final result does not expose compiler-local payloads as artifacts/runtime definitions. No SQL/ORM/API/OpenAPI/UI/runtime generator, optimizer, graph engine, storage/cache, publisher, deployment or execution.

## Diagnostic contracts

Actual existing CompilationDiagnostic/TypeValidationSeverity and CMP-02 association/source reporting are reused; no general SK-11 replacement.

| Code | Meaning |
|---|---|
| CMP-021 | Unsupported definition/type lowering capability (INCOMPLETE warning) |
| CMP-022 | Absent DataFacet capability (INCOMPLETE warning) |
| CMP-023 | Invalid compiled field or field collection; delegated intrinsic cause retained |
| CMP-024 | Unsupported compiled type reference/primitive contract |
| CMP-025 | Unsupported compiled constraint contract |
| CMP-026 | Canonical member/input/preparation/identity-assignment mismatch |
| CMP-027 | Missing explicit representation identity coverage (INCOMPLETE warning) |
| CMP-028 | Invalid compiled type payload identity/name/context |

Existing IR CMP-011..020 still describe envelope/schema/kind/current-request/commit errors. Type/field lowering issues carry actual fixed phase, exact original type and owned FieldId where available, plus independent IR identity. Intrinsic constructor failures without phase use orchestrator association; adaptation adds actual phase without replacing existing evidence. Original TYPE/MOD validation status/codes remain unchanged. Unsupported compiler capability is never relabeled as semantic invalidity. General SK-11 factory compatibility remains blocked pending its real implementation.

## Mini Sales example — documented, not executed

Use the established sales.Customer@1.0.0 with original actual repository-valid semantic UUID identity, original field UUID IDs and sales-context. Prompt aliases such as typ_customer_123/fld_name are descriptive only and are not valid substitutes for the repository's sem_/fld_ UUIDv4 contracts.

The expected payload keeps:

| Field | Actual reference | Presence | Nullability | Existing value constraints |
|---|---|---|---|---|
| name | String PrimitiveTypeRef | Required | NonNullable | max-length 200 |
| active | Boolean PrimitiveTypeRef | Required | NonNullable | none |
| creditLimit | Decimal PrimitiveTypeRef | Optional | NonNullable | minimum 0, precision 18, scale 2 |

After obtaining the original accepted request/evidence through the existing pipeline in a **future authorized verification**, supply explicit binding of its exact Customer ElementVersionRef to a caller-owned representation token such as ir-sales.customer.type. Compose CompiledTypeLoweringPhase in ModelCompiler. Its internal result should carry COMPILED_TYPE_IR/V0 envelope with exact Customer origin, unchanged scope and fields in name/active/creditLimit order, plus original supported source associations. A future explicitly declared consumer uses existing SemanticIRHandoff against compiler-local state and its type phase prerequisite. No such producer/lowering/consumer example has been run here. No target artifact or verified end-to-end output is claimed.

## Deferred verification and readiness

The complete future specification is [CMP-04-deferred-tests.md](../../test-archive/CMP-04/CMP-04-deferred-tests.md); [ADR-0035](../architecture/decisions/ADR-0035-compiled-type-ir.md) and [static record](../architecture/cmp04-verification.md) document boundaries. All scenarios remain NOT_RUN — DEFERRED; automated tests created/executed 0. Static checks cannot establish correctness. Full TYPE-01/richer facets/SK-11, portable authenticated binding, generators and applicable compiler API remain upstream gaps. Stop CMP-04; do not implement CMP-05 automatically.
