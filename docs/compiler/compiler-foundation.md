# CMP-01 — Compiler Foundation

Date: 2026-10-11. Foundation implementation available; behavior **DEFERRED / NOT VERIFIED**. No compiler/phase/artifact/report example or automated test executed.

## Actual repository boundaries

Existing compiler-core and compiled-contracts were registered public marker modules, not compiler behavior. Kernel/model-core/model-authoring are Python, so there is no cross-language duplicate contract or migration. General SK-11/full TYPE-01 remain absent; current canonical models support the frozen five-property TypeDataComposition/DataFacet seam. MOD-08 validates that seam; MOD-09 reports its actual diagnostic contracts. No existing Django/DRF compiler interface exists; installed Python 3.12.14/PyYAML 6.0.3, Django/DRF absent. No framework upgrade, endpoint, ORM, migration or DB.

Compiler implementation remains in platform/compiler/compiler-core; stable artifact metadata seams remain in platform/contracts/compiled-contracts. Compiler-core gains one declared public API dependency on model-authoring to consume actual MOD-08 evidence/MOD-09 associations. Model-loader remains restricted to model-authoring. Model/core/runtime never import compiler implementation; runtime still depends only on Kernel/compiled-contracts. No profile relaxation, dependency waiver, new module or activation dependency change.

## Snapshot-bound prerequisite

Inspection found MOD-08 ModelValidationResult lacked an input snapshot association. It now has optional validated_model, populated by ModelValidationPipeline with the exact request.model object after its existing orchestration. This is a backward-compatible field addition; old two-argument constructors keep status/readiness but yield unbound evidence and cannot admit compiler execution. No validation rule/status/warning policy is changed.

CompilationRequest retains actual CanonicalModel, original ModelValidationResult or explicit None, CompilationContext(scope, target) and optional existing MOD-05 source associations. Gate checks explicit scope, VALID/READY and validation_evidence.validated_model is request.canonical_model. Equal context, count, references, membership or supported content does not substitute for exact binding; equal reconstructed/deserialized models fail closed and need new explicitly authorized externally supplied evidence. No hash/serializer/latest lookup or automatic validation run.

This is an in-process typed association emitted by trusted MOD-08 orchestration, not a cryptographic validation certificate, deployment permission or cross-process evidence format. Python callers constructing reports manually must honor their actual execution provenance; arbitrary forged objects/reflection mutation are outside supported contracts. The exact retained model is omitted from repr/equality/hash contribution of the evidence so it is auxiliary and no model fingerprint is implied.

Malformed/unrepresentable requests fail at typed constructors; ModelCompiler.compile wrong root input returns CMP-001 FAILED. None evidence, INCOMPLETE validation or legacy unbound evidence yield INCOMPLETE; INVALID yields FAILED. A different bound model or scope mismatch yields FAILED. All configured phases are reported skipped when the gate blocks; original validation reports remain available without re-running validation.

## Targets and configuration

CompilationContext has explicit semantic scope and a bounded CompilationTargetId, with no HTTP/tenant/organization/DB/runtime/deployment metadata. Two current objective identifiers:

- foundation-preparation: prepare canonical inventory; success explicitly means preparation only and contains no artifacts.
- artifact-build: prepare and emit at least one supported target artifact; CMP-01 supplies no generator, so default execution remains INCOMPLETE.

Unknown typed target tokens fail closed as unsupported capability, never fallback to another platform. Tokens are logical selectors, not permission to generate arbitrary output. No broad platform matrix. ModelCompiler's frozen explicit phase composition is the configuration; no additional options bag is necessary. Core preparation cannot be removed/replaced; an empty additional collection still has that mandatory phase.

## Phases and local state

CompilationPhase exposes an immutable CompilationPhaseDescriptor (stable ID, ordered prerequisites, capability set, target set) and execute(request, state) -> CompilationPhaseResult. ModelCompiler snapshots descriptors at construction, preserving configured order. Duplicate IDs or forward/self/cyclic configured prerequisites are rejected; absent prerequisite IDs remain explicit unavailable capabilities at execution. No sorting scheduler, discovery, dynamic imports, parallel execution or scripts.

Default CompilationPreparationPhase creates PreparedCompilationInput retaining original model/context and exposing existing exact canonical references in canonical order. This inventory is actual preparation output, not universal IR, target artifact or reconstructed definitions. CompilationState is an immutable local transition carrying that preparation and an explicit artifact collection; no generic intermediate dictionary/global workspace.

Additional phase implementations are explicitly injected pure deterministic trusted code and may supply future owned artifacts under EMIT_ARTIFACTS. Immutable descriptor capture cannot prove arbitrary implementation code/state pure; that remains the extension contract. A phase returns completed/failed/incomplete/skipped. Noncompleted phases expose no successful preparation/artifacts and need a reason. Completed phases cannot contain blocking errors. Programming exceptions and malformed phase outputs propagate; only anticipated duplicate-key conflicts are converted to compiler diagnostics.

The coordinator checks phase prerequisites/target support, retains original phase diagnostics and origin, stops dependent execution safely, reports all remaining phases skipped and never retries with alternate interpretations. A failed phase with no error report gets bounded CMP-008. Prepared output must retain the exact input/context and be declared by PREPARE; artifact output requires EMIT_ARTIFACTS and artifact-build. Artifact scope/target and exact semantic dependencies must agree with the input membership, without reference resolution or semantic validation.

Missing emitter/output after complete preparation yields CMP-010 INCOMPLETE. No nonexistent emission phase is reported as having run. No concrete SQL/API/UI/action/event/policy/workflow/runtime artifact generator or IR is implemented.

## Output/artifact contracts and atomicity

compiled-contracts defines CompilationArtifactKey, CompilationArtifactKind and the read-only CompilationArtifact protocol. A future owned immutable typed artifact payload implements this metadata seam: independent logical key/kind, scope, target token and exact semantic_dependencies. CMP-01 defines no concrete payload format, placeholder artifact, file blob/metadata-only universal IR or storage service. Logical artifact keys are needed for duplicate membership, are not SemanticElementIds/filesystem paths or generated distributed IDs, and support many-to-many semantic dependency relationships.

Compiler-owned CompilationArtifactCollection copies finite inputs, admits frozen dataclass value implementations with actual typed metadata, sorts by logical key and exposes read-only lookup. All duplicate keys conflict, including equal/repeated values; no implicit content-equality/idempotency or last-write-wins policy. Later artifact contracts own deep payload immutability/meaning; no canonical content/hash comparison is claimed.

CompilationResult distinguishes SUCCEEDED/FAILED/INCOMPLETE and retains target, compiler diagnostics, phase outcomes, original validation evidence and optional successful output. Phase outcomes expose status/diagnostics/reason, never candidate artifacts. Failed/incomplete final results always contain an empty artifact collection and no successful preparation; accumulated local candidates are discarded. Successful preparation objective contains no artifacts. Successful build objective needs completed required capabilities and nonempty artifacts. No materialization, publication, activation or runtime registration occurs.

Direct result constructors enforce typed successful-output/readiness/coverage invariants but are reporting contracts, not tamper-proof execution proofs. Compilation success never means deployment authorization or runtime success.

## Diagnostics and MOD-09 bridge

CompilationDiagnostic is a narrow CMP-001..010 prerequisite/capability/phase/output contract using actual TypeValidationSeverity. Compiler limitations are compiler-origin reports, not semantic validation failures. Original MOD-08 diagnostic reports are retained separately and propagated through diagnostic_entries in original order, followed by compiler emissions. Optional exact subject references reuse MOD-09 associations; no physical source import or fabricated span.

General SK-11 is unavailable, so a narrow ModelDiagnosticExtension protocol plus explicit COMPILER origin admits immutable compiler diagnostic values into the existing MOD-09 wrapper, preserving code/message/severity. Existing diagnostic origins cannot be relabeled; no dynamic registry or message/class-name guessing. This does not claim full SK-11 completion.

CompilationResult.diagnostic_report returns actual diagnostic entries, scalar compilation status/target, phase views and original MOD-08 evidence via model-authoring-owned CompilationDiagnosticReport/CompilerPhaseDiagnosticView. These are presentation projections with no artifacts/model serialization, not competing compiler results. Model-loader consumes only this explicit inward contract, preserving its designated adapter profile. Its report can retain compiler status/phase outcomes and original validation evidence independently; an INVALID/INCOMPLETE/FAILED compiler outcome never changes original validation judgment. Combining direct validation plus compilation reporting requires the same actual evidence object; repeated diagnostics remain preserved, not deduplicated. Separate runs require separate reports.

Existing JSON-ready disclosure policy remains bounded by default. Compiler phase IDs/cause codes and actual phase outcomes are explicitly represented without source/semantic/text disclosure unless opted in. Future source-aware reporting needs original explicitly paired MOD-03 context; no stronger provenance or publication authority.

## Mini Sales usage — not executed

The established Customer model remains unchanged. Assume actual canonical_model and validation_result already come from earlier authorized processing/validation, and the result is bound by the updated MOD-08 pipeline. Compiler entry never performs that earlier workflow.

```python
from compiler_core.public import (
    CompilationRequest, CompilationContext, ModelCompiler,
    PREPARATION_TARGET, BUILD_TARGET,
)
from model_loader.public import ModelDiagnosticReporter

preparation_request = CompilationRequest(
    canonical_model, validation_result,
    CompilationContext(canonical_model.scope, PREPARATION_TARGET),
    canonical_source_associations,
)
prepared = ModelCompiler().compile(preparation_request)

build_request = CompilationRequest(
    canonical_model, validation_result,
    CompilationContext(canonical_model.scope, BUILD_TARGET),
    canonical_source_associations,
)
# Expected future default outcome: INCOMPLETE, no Customer artifact fabricated.
build = ModelCompiler().compile(build_request)
report = ModelDiagnosticReporter().report((build.diagnostic_report,), diagnostic_source_context)
```

This snippet was not executed. Expected future preparation outcome: SUCCEEDED for foundation-preparation only; expected artifact-build outcome: INCOMPLETE. INVALID/INCOMPLETE/unbound/different-model evidence blocks phase execution. String precision applicability remains TYPE-06's judgment, not compiler logic.

See [ADR-0032](../architecture/decisions/ADR-0032-compiler-foundation.md), [static record](../architecture/cmp01-verification.md), [archive](../../test-archive/CMP-01/CMP-01-deferred-tests.md). Stop CMP-01; no CMP-02.

## CMP-02 compatibility extension

[Compilation diagnostics](compilation-diagnostics.md) adds optional immutable producer associations, recorded phase execution/prerequisites and lossless original occurrence guards to existing results. `.diagnostic_report` delegates to the pure reporter while preserving original status/evidence. Actual conflict key/related semantic dependencies are retained at the existing collection exception; collision algorithm and compilation objectives are unchanged. No new phase, generator, validator or source processing. Historical CMP-01 evidence remains factual; new behavior is deferred/unverified.

## CMP-03 compatible internal state extension

[Semantic IR Envelope](semantic-ir-envelope.md) adds trailing IR envelope tuples to phase result/state and original outcomes to state. Future explicit EMIT_IR producers commit typed candidates only after original-input/context/phase/duplicate checks; consumers require actual committed membership and completed executed prerequisite evidence. Existing phase execute interface is unchanged. IR does not satisfy artifact output readiness; no default producer/lowering installed. New behavior is deferred/unverified; preserve historical CMP-01 evidence.

## CMP-04 explicit type lowering integration

[Compiled Type IR](compiled-type-ir.md) adds a fixed explicitly composed EMIT_IR phase requiring actual completed executed preparation and original VALID/READY canonical binding. Caller supplies one exact definition → independent IR ID binding per selected type. Missing capability/coverage is incomplete, invalid structural association failed, and neither exposes partial IR. Default compiler composition/artifact objectives are unchanged; no target generator is installed. Historical verification retained; new behavior remains deferred/unverified.

## CMP-05 — Type Compiler Pass

Existing compiler-core now exposes TypeCompilerPass, reusing CMP-04 lower_payload and CMP-03 factory; old CompiledTypeLoweringPhase aliases the same implementation/stable identity. Canonical multi-version ordering, explicit request-local IDs, collision/rerun/exact-origin guards and atomic existing coordinator handoff; no partial failure output. No dependency/module/HTTP/ORM/runtime/generator additions. [Contract and unexecuted Mini Sales](type-compiler-pass.md). **129** deferred scenarios, tests created/executed **0**, **DEFERRED / NOT VERIFIED**. Stop CMP-05.

## CMP-06 — Deterministic Compilation

Original compiler now requires frozen phase implementations with approved immutable options, captures complete configuration/classes and rejects ambiguity/drift with CMP-029/030. Existing type pass normalizes exact binding mappings; supported semantic comparison uses actual canonical/payload equality separately from original request ownership and physical presentation. No new orchestrator/module/dependency/route/ORM/generator/serialization/hash/runtime. [Contract and unexecuted Mini Sales](deterministic-compilation.md). **139** archived scenarios; tests implemented/executed **0**, **DEFERRED / NOT VERIFIED**. Mutable old extension phases need adaptation; unsupported artifact/byte equality remains explicit. Stop CMP-06.

## CMP-07 — Runtime Artifact Manifest

Shared compiled-contracts owns immutable artifact origins/dependencies/descriptors; compiler-core owns bound manifest/V0/assembly using original result status and complete final artifact collection. Original result gains trailing optional request/configuration output origin; legacy unbound result cannot authorize manifest. Typed artifact/manifest diagnostic associations extend compatibly; semantic comparison includes them. No generator/runtime imports/API/ORM/storage/hash/deploy added. Current Type IR-only build stays INCOMPLETE, default runtime-kind approvals empty. [Contract and unexecuted Mini Sales](runtime-artifact-manifest.md). **144** deferred scenarios, tests implemented/executed **0**, **DEFERRED / NOT VERIFIED**. Stop CMP-07.

## CMP-08 — Artifact Writer

Pure writer contracts/preflight/plan/result/receipt reuse original CMP-01 result and CMP-07 assembly; exact approved byte fields only. Secure Linux filesystem materialization is owned by separate constrained `tools/artifact-writer`, never imported by compiler. FAIL_IF_EXISTS complete-directory NOREPLACE commit, explicit synchronization and owned cleanup. [Contract](artifact-writer.md), [static record](../architecture/cmp08-verification.md), [158 deferred cases](../../test-archive/CMP-08/CMP-08-deferred-tests.md). Tests implemented/executed 0; **DEFERRED / NOT VERIFIED**. No generator/publication/API/runtime additions. Stop CMP-08.
