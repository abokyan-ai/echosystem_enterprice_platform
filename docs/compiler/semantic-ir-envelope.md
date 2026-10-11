# CMP-03 — Semantic IR Envelope

Date: 2026-10-11. Status: **DEFERRED / NOT VERIFIED**. No example or deferred scenario was executed.

## Actual boundary

All contracts live in the existing `compiler_core.public` module. CanonicalModel, CompilationRequest/Context/State/PhaseResult, original MOD-08 evidence, Kernel references and CMP-02 diagnostics are reused. The envelope carries compiler intermediate data and is neither SemanticElement nor CompilationArtifact. No lowering, optimization, complete Type/Action/Event/Policy/UI IR, generator, interpreter, publisher, storage or HTTP endpoint is implemented.

General SK-11 and full TYPE-01 are absent in this repository. CMP-03 composes existing CompilationDiagnostic/TypeValidationSeverity and CMP-02 associations, with no substitute general diagnostic system or compatibility claim for missing SK-11 factories. Python 3.12.14 and PyYAML 6.0.3 are available; Django/DRF dependencies and an applicable compiler HTTP boundary are absent. Domain construction requires no framework setup; future applicable HTTP adapters remain authorized DRF boundaries.

## Identity, version and payload

`SemanticIRId` is an explicit bounded `ir-` prefixed logical representation token, maximum 160 ASCII characters. Its grammar is `ir-[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*`. No random assignment, global counter, semantic ID, artifact key, filename, QName or process address is used to derive it. Identity membership is scoped to **one original CompilationRequest**. Equal tokens in different requests do not establish transferable identity. Duplicate tokens within state, including equal/repeated envelopes, fail closed without overwrite.

`SemanticIRSchemaVersion.V0` has the explicit scalar `0`; caller must supply this enum value. Strings, SemanticVersion, future versions and omitted mandatory arguments are not silently interpreted or migrated. This version belongs to the envelope, separate from semantic/authoring/compiler/artifact versions.

`SemanticIRPayloadKind.FOUNDATION_COORDINATES` is the only supported v0 discriminator. `SemanticIRFoundationPayload(definitions)` is a narrow immutable inventory of explicit exact ElementVersionRef coordinates. It is not a lowered Type IR, canonical definition payload, executable plan or completed build. `SemanticIRPayload` aliases this closed actual payload contract; arbitrary protocols/classes/dicts are not accepted. Future payload kinds require an explicit code/contract extension with owned immutable structure and compatibility rules.

Payload lists are defensively converted to tuples, exact Kernel leaf types are required and duplicate exact coordinates are rejected. Envelope `definition_origins` must equal payload coordinates in the same caller-declared order and every coordinate must exist in the original canonical snapshot. One or many definitions are supported, including explicitly selected exact versions; no names/latest/registry selection. Empty payload is valid only with explicit `model_wide=True` and empty origins. This denotes an intentional model-wide coordinate inventory, not absence of a mandatory payload or successful artifact generation. None payload is rejected.

## Original input and construction

`SemanticIRCanonicalInput(request)` retains the original immutable CompilationRequest. It requires matching canonical/compiler scope, existing supported target and original VALID/READY evidence bound to that exact canonical model object, reusing CMP-01's in-process evidence policy. No TYPE-06/MOD-08 validator runs here. It checks association integrity rather than judging semantic validity. Missing/unbound/invalid/incomplete or wrong-model evidence fails closed. This does not authenticate validation provenance or produce a portable content hash.

`SemanticIREnvelope` fields are explicit identity, schema_version, semantic_context, canonical_input, payload_kind, payload, definition_origins, model_wide, optional produced_by_phase and source_associations. Frozen dataclasses with closed immutable payload/reference types protect nested snapshots. Origin/source lists are copied; arbitrary metadata is not supported. `SemanticIREnvelopeFactory.create` is a thin explicit keyword constructor applying the same intrinsic checks. Expected supplied-value failures raise `SemanticIREnvelopeError` with actual existing compiler diagnostics; missing required Python arguments remain ordinary TypeError at the call signature. No successful envelope is returned after rejection.

`produced_by_phase` uses CMP-01 phase IDs. Generic construction may omit it or declare a candidate producer without claiming execution/completion. Candidate construction has no compiler side effects. Source associations must be actual CanonicalSourceAssociation values already present in the original request and concern declared exact origins. They retain authoring paths only; physical source spans stay with MOD-03/model-loader. No arbitrary provenance graph, fabricated location or line-number identity.

## Typed state and phase integration

Minimal compatible trailing fields add `ir_envelopes` to existing CompilationPhaseResult and `ir_envelopes`/`phase_outcomes` to existing CompilationState. Existing positional arguments remain intact; `CompilationPhase.execute(request, state)` is unchanged. Candidate result tuples preserve emission order; committed state envelopes are sorted by explicit identity token, and original outcomes keep actual phase order. No independent/global IR collection registry is introduced. Failed/incomplete/skipped phase results cannot carry candidate envelopes.

A future producer must explicitly declare `CompilationCapability.EMIT_IR`, return a completed actual phase result and declare its own descriptor ID on each candidate envelope. At the existing coordinator commit point, `_merge_ir` verifies current request identity/context and exact producer ID, then rejects duplicates within and across phases. Expected rejection appends original phase diagnostics plus structured IR failure, marks that actual executed phase FAILED and blocks downstream work under existing policy. IR and artifact state commit together only after both boundaries accept candidates. Artifact conflict discards new intermediate candidates too. No new producer phase is installed and no default IR is generated.

IR membership in state is not compilation output capability. It does not satisfy EMIT_ARTIFACTS or a nonempty final artifact objective. Existing default artifact-build remains INCOMPLETE/CMP-010. Existing explicit preparation-only success is still preparation, even when a future declared phase passes a foundation inventory. Final CompilationResult exposes no new IR payload output or publication claim; downstream phases use compiler-local state.

## Required consumer handoff

`SemanticIRHandoff.require(envelope, request=..., state=..., consumer=..., required_kind=..., required_schema=...)` returns the **same** envelope on acceptance; it does not run the consumer. It checks actual types, supported exact schema/kind, current request and target/context, compatible actual preparation state, and consumer target support. The same original envelope object must already be committed in state. The producing phase must be in state's original outcomes, COMPLETED, executed=True, declare EMIT_IR, differ from the consumer and be an explicit consumer prerequisite. Missing/unknown/failed/skipped/unknown-execution producer or a manually constructed uncommitted candidate cannot establish handoff.

No automatic payload conversion or mandatory success result is fabricated. Expected incompatibility raises SemanticIREnvelopeError; a future phase may return its `.phase_failure(consumer.id)` using the **existing** CompilationPhaseResult FAILED pattern. The adapter retains code/message/severity and enriches missing phase association without replacing conflicting original phase evidence. Unexpected programming exceptions remain visible and are not swallowed. No extra handoff result hierarchy or scheduling service is introduced.

These are trusted in-process evidence associations, not tamperproof execution certificates. Manually assembled state/outcomes remain explicit caller assertions, as in CMP-01; no permission engine or cryptographic provenance is claimed. Consumer descriptor is supplied by its actual phase implementation, not resolved through a second registry.

## Equality and deterministic ordering

Representation token equality, envelope value equality, payload coordinate equality, canonical semantic content and serialization are distinct. SemanticIRCanonicalInput equality means same original request association (`request is other.request`); it does not define semantic equality. Envelope dataclass equality compares declared fields and that association. Thus repeated construction from the same original request and same ordered values can be value-equivalent; same ID alone or a separately reconstructed request is insufficient. Envelopes/input association are unhashable, with no content-address or canonical byte contract.

Origin and source association order is explicit caller order; payload order is never rewritten. State membership order is ordinal logical-token order. No time/random/locale/filesystem/request-state/global registry dependency. Python object identity is used solely for the existing original evidence and committed handoff association policy, never to generate a representation ID.

## Diagnostics and safe presentation

New stable compiler codes are:

| Code | Boundary |
|---|---|
| CMP-011 | Invalid envelope/sequence structure |
| CMP-012 | Unsupported IR envelope schema |
| CMP-013 | Invalid representation identity |
| CMP-014 | Semantic/compiler context or target mismatch |
| CMP-015 | Canonical/request/evidence/origin/source association mismatch |
| CMP-016 | Unsupported payload kind |
| CMP-017 | Payload type/kind/coordinate integrity mismatch, including mutable bags |
| CMP-018 | Missing mandatory payload |
| CMP-019 | Incompatible commit or consumer handoff/producer evidence/capability |
| CMP-020 | Duplicate representation identity |

Existing CompilationDiagnosticAssociation gains optional typed SemanticIRId; authoring CompilationDiagnosticDetails gains only its bounded token projection. Original exact semantic reference, context and actual phase are attached when reliable; factory construction without phase does not fabricate execution origin. Existing source reporting can use declared canonical associations; physical spans are never inferred by IR construction. Generic failures use compiler-orchestrator responsibility and existing ERROR severity. Type/model validation codes remain unchanged.

Existing model-loader JSON adapter has `include_ir_identities=False`; actual bool is required and opt-in emits only the representation token, no envelope/canonical evidence/payload. Existing application caller must authorize disclosure. No public IR CRUD, endpoint, serialization/deserialization format, ORM, migration or ModelSerializer is added.

## Mini Sales — unexecuted contract example

The existing sales.Customer@1.0.0 model retains name String required/nonnullable/max-length 200, active Boolean required/nonnullable and creditLimit Decimal optional/nonnullable/minimum 0/precision 18/scale 2.

After CMP-01 accepts its original validated request, a future approved producer could declare an explicit representation token, schema V0, the unchanged sales SemanticContextRef, SemanticIRCanonicalInput of that request, foundation-coordinate payload containing the exact Customer reference and matching origins, its actual phase ID and approved canonical source associations. This is only the supported coordinate inventory shape, not generated Customer IR. No producer is implemented or run.

A future completed executed EMIT_IR producer can commit that envelope through the existing phase result boundary; a subsequent declared consumer requires it through SemanticIRHandoff. Unsupported schema/kind, None payload, different scope/request, unknown producer and duplicate representation token reject with the corresponding structured code. Merely constructing a candidate or passing a dictionary cannot satisfy handoff or final artifact readiness. Missing actual future producer/consumer fixtures must be supplied before scenario execution.

## Deferred verification and next stage

See [deferred specification](../../test-archive/CMP-03/CMP-03-deferred-tests.md), [ADR-0034](../architecture/decisions/ADR-0034-semantic-ir-envelope.md) and [implementation/static record](../architecture/cmp03-verification.md). Zero automated tests/examples/custom scenario scripts were created or executed. Permitted syntax/build/dependency checks do not prove behavioral correctness. General SK-11, full domain IR, portable evidence binding and applicable HTTP integration remain upstream gaps. Stop CMP-03; do not implement CMP-04 automatically.

## CMP-04 explicit closed payload extension — current policy

The initial CMP-03 foundation-only descriptions above document its introduction. CMP-04 explicitly extends the same V0 envelope to `SemanticIRPayloadKind.COMPILED_TYPE_IR` and actual `CompiledTypeIR`; public payload union is exactly foundation inventory or compiled type. Current constructor/handoff accepts either supported discriminator with exact type matching. Compiled type requires one exact matching origin, model_wide=False, original QName/complete ordered field structure and matching context. Foundation payload behavior is preserved. This extension supersedes foundation-only availability statements without changing schema, source identity, trusted request association or final artifact readiness. [Contract](compiled-type-ir.md). No dynamic registry/generator/API; historical CMP-03 cases remain archived and new compatibility cases are deferred.

## CMP-06 — Deterministic Compilation

Original compiler now requires frozen phase implementations with approved immutable options, captures complete configuration/classes and rejects ambiguity/drift with CMP-029/030. Existing type pass normalizes exact binding mappings; supported semantic comparison uses actual canonical/payload equality separately from original request ownership and physical presentation. No new orchestrator/module/dependency/route/ORM/generator/serialization/hash/runtime. [Contract and unexecuted Mini Sales](deterministic-compilation.md). **139** archived scenarios; tests implemented/executed **0**, **DEFERRED / NOT VERIFIED**. Mutable old extension phases need adaptation; unsupported artifact/byte equality remains explicit. Stop CMP-06.

## CMP-10 in-memory inspection

[IR Inspector](ir-inspector.md) accepts actual envelope/immutable collection/state/phase output, selects stable IDs/kinds/exact origins and projects existing compiled-type structures. No artifact files/Manifest/receipt/serialization or compiler run required. Existing foundation-coordinates has no v0 inspection handler and is explicitly INCOMPLETE; source IR stays unchanged. [179 deferred cases](../../test-archive/CMP-10/CMP-10-deferred-tests.md), tests executed 0.
