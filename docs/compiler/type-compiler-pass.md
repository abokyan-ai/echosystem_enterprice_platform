# CMP-05 — Type Compiler Pass

Date: 2026-10-11. Status: **DEFERRED / NOT VERIFIED**. Examples below are specifications, not executed evidence.

## Actual composition and responsibilities

`compiler_core.public.TypeCompilerPass(identities)` implements existing `CompilationPhase.execute(request, state) -> CompilationPhaseResult`. Compose through `ModelCompiler(additional_phases=(pass_instance,))`; no new orchestrator or default registration. Its descriptor is `TYPE_COMPILER_PASS_PHASE`, an alias of existing `COMPILED_TYPE_IR_PHASE`: stable `CMP-PHASE-COMPILED-TYPE-IR`, prerequisite `CMP-PHASE-PREPARE`, EMIT_IR, foundation-preparation and artifact-build targets. `CompiledTypeLoweringPhase` aliases the same class, preserving old composition without duplicate phase implementations. Configuring both fails the existing duplicate-descriptor guard.

CMP-04 `CompiledTypeLowerer.lower_payload` is a minimal added seam returning existing CompiledTypeIR on success or existing failed/incomplete CompilationPhaseResult on expected rejection. It alone lowers fields/references/constraints. Its existing `lower` API still returns the original envelope-carrying phase result through a compatibility adapter. No new IR/result/diagnostic hierarchy. CMP-05 invokes lower_payload, owns envelope assembly through actual CMP-03 factory and collects independent expected failures. Unexpected defects propagate; no catch-all conversion.

## Gates and selection

Direct execution reuses the original VALID/READY evidence binding, original canonical object, prepared input/context and completed executed PREPARE-capable prerequisite. It does not rerun validation. Wrong request/state root types raise TypeError; bound-evidence or prepared-state mismatch returns structured failure. Current state envelopes must belong to this original request/context. Original evidence is trusted in-process, not cryptographic provenance or access permission.

Membership and order come only from MOD-04 `list_definitions()`. Select actual TYPE_DEFINITION kind; iterate canonical semantic-ID/numeric-version order. Do not expand from registries, references, namespaces, filesystem or latest-version rules. All explicit exact versions survive independently. Fields retain DataFacet order. Current canonical vocabulary contains only TypeDataComposition; legitimate other kinds cannot yet enter this model. Their future owner passes/whole-build coverage cannot be invented here. Full TYPE-01/general SK-11/richer facets remain upstream gaps. Absent DataFacet returns INCOMPLETE/CMP-022; explicit empty present facet lowers normally.

## Identity, conflicts and atomic handoff

Use existing CompiledTypeIRIdentityBinding for every selected exact type, with independent caller-supplied SemanticIRId tokens scoped to one original CompilationRequest. Determinism means same explicit mapping and original input yield same identities/order; no hashes, UUID generation, counters, addresses, source paths or inferred names. Assignment order cannot affect canonical processing; invalid extra assignments are sorted by semantic-ID/numeric-version for diagnostics. Duplicate source assignments are configuration ValueError; malformed assignments TypeError. Missing coverage is INCOMPLETE/CMP-027; outside membership FAILED/CMP-026.

Before lowering, reject an existing outcome or envelope for this phase (CMP-019): rerun, including equal outputs, is not idempotent. Reject same-pass/existing representation ID collisions (CMP-020) and an occupied exact compiled-type origin even under another producer (CMP-019). Aggregate these conflicts in canonical order with original target and independent IR ID. Preserve unrelated foundation/type state; do not overwrite, remove or append twice. No speculative generic slot registry.

For each successful payload, build V0/COMPILED_TYPE_IR envelope with exact singleton origin, original request/context, actual phase and original matching source sidecar. Factory verifies full canonical payload preservation. Single-type failures gain only missing exact type/IR association; existing field/cause/origin evidence is preserved and contradictory targets raise TypeError. Expected envelope failure joins original lowering diagnostics; continue other selected types. FAILED dominates INCOMPLETE. Either non-completed status returns diagnostics/reason and **no successful envelopes**. Successful candidates are an immutable tuple in canonical order. Preflight `_merge_ir` without mutation; original CMP-01 repeats commit checks and atomically commits complete IR plus artifacts/preparation/outcome. Committed state retains CMP-03 identity-sorted inventory order, distinct from canonical phase emission order. No local staging is externally visible on failure.

## Zero work and objectives

Original VALID/READY empty canonical membership plus empty bindings returns COMPLETED with empty output, no dummy payload/envelope. There is no current target requiring at least one type; do not invent one. Artifact-build still returns INCOMPLETE/CMP-010 without a final EMIT_ARTIFACTS generator and artifacts. Foundation-preparation success is only that narrower objective. Pass completion cannot certify whole-model semantic coverage or publishability. Future targets/other-kind contracts need their owner stages before related deferred cases can run.

## Diagnostics, immutability and boundary

Existing CMP-02 phase/result reporting retains actual diagnostic objects, phase, exact type/owned field targets, cause codes and optional independent IR identities. Existing source sidecars and model-loader location-index projection supply original source enrichment; absent physical locations stay absent. No guessed source spans/provenance graph. Envelope factory diagnostics retain original origin plus phase adaptation. Type failure diagnostics retain CMP-04 field association. Immutable request/context/model/evidence/state remain untouched. Bindings copied to tuples; all staging/function dependencies are local with no global mutable state/counters/cache. Self/mutual semantic references stay versionless ElementRef, never recursive payloads or graph closure.

Pure Python in existing compiler-core only; no Django/DRF dependency or applicable existing compiler HTTP route. No endpoint, permissions change, ORM model/migration, serializers/generators, runtime, deployment, persistence or publishing. Nine-module dependency graph unchanged.

## Mini Sales — unexecuted integration specification

Use original sales scope `sem_550e8400-e29b-41d4-a716-999999999999`. Existing `examples/authoring/mini-sales.json` supplies Customer ID ending `000000000001`, fields `fld_550e8400-e29b-41d4-a716-000000000001` (name), `...000000000002` (active), `...000000000003` (creditLimit). Its fields preserve String/Required/NonNull/max-length 200, Boolean/Required/NonNull/no value constraints, Decimal/Optional/NonNull/minimum 0/precision 18/scale 2. Existing `mini-sales-references.json` supplies Employee semantic ID `sem_550e8400-e29b-41d4-a716-000000000002` and manager FieldId `fld_550e8400-e29b-41d4-a716-000000000012`, Optional/Nullable, with a name reference to sales.Employee. Future authorized upstream binding must turn this into actual versionless ElementRef to Employee; CMP-05 does not parse or resolve it. Do not substitute prompt aliases typ_customer_123/fld_name.

A future original canonical snapshot explicitly containing Customer@1.0.0, Customer@1.1.0 and Employee@1.0.0 uses caller tokens ir-sales.customer.v1.0.0, ir-sales.customer.v1.1.0 and ir-sales.employee.v1.0.0. Customer 1.1 is a specified future fixture variation, not silently selected from the existing file. Supply original VALID/READY evidence and canonical sidecars. Expected phase output: three distinct envelopes in Customer 1.0, Customer 1.1, Employee 1.0 order, original exact origins/field contracts and Employee manager identity-only self-reference. No Department inclusion unless explicit canonical membership and binding require it.

Negative Employee variants: valid absent DataFacet fixture yields CMP-022/INCOMPLETE and no Customer envelope output; a controlled future lowerer collaborator reporting an expected Employee field failure yields FAILED, retains Employee/manager diagnostics, and returns no partial Customer output. Do not fabricate invalid immutable canonical objects or reclassify invalid semantic input as accepted evidence: actual invalid Employee semantics stop at original MOD-08/CMP-01 gate. Future authorized defect-fault coverage must distinguish expected structured rejection from unexpected exception propagation. None of these examples or scenarios was executed.

## Verification and stop

[Detailed deferred specification](../../test-archive/CMP-05/CMP-05-deferred-tests.md), [ADR-0036](../architecture/decisions/ADR-0036-type-compiler-pass.md), [implementation/static record](../architecture/cmp05-verification.md). Automated tests created/executed: 0. Static checks are separate from behavioral verification. Stop CMP-05; no CMP-06 implementation.

## CMP-06 — Deterministic Compilation

Original compiler now requires frozen phase implementations with approved immutable options, captures complete configuration/classes and rejects ambiguity/drift with CMP-029/030. Existing type pass normalizes exact binding mappings; supported semantic comparison uses actual canonical/payload equality separately from original request ownership and physical presentation. No new orchestrator/module/dependency/route/ORM/generator/serialization/hash/runtime. [Contract and unexecuted Mini Sales](deterministic-compilation.md). **139** archived scenarios; tests implemented/executed **0**, **DEFERRED / NOT VERIFIED**. Mutable old extension phases need adaptation; unsupported artifact/byte equality remains explicit. Stop CMP-06.

## CMP-10 explicit output inspection

[IR Inspector](ir-inspector.md) can consume actual TypeCompilerPass PhaseResult.ir_envelopes or separately available committed state/tuple without rerunning the pass. Projects in existing IR identity collection order while preserving payload field/origin order. Inspection success does not change an incomplete/failed later compilation, and final CompilationResult does not expose missing internal IR/state. No demo or scenario execution; 179 future cases deferred.
