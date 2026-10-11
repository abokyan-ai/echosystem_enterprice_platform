# CMP-01 — implementation and separate static-check record

Date: 2026-10-11. Foundation implemented within current contracts; behavioral status **DEFERRED / NOT VERIFIED**. Documented cases: **156**. New automated tests: **0**. Deferred tests executed: **0**.

## Implemented components

compiler_core.public: CompilationStatus/PhaseStatus/Capability/TargetId, explicit PREPARATION_TARGET/BUILD_TARGET, CompilationFailure/Diagnostic, CompilationContext/Request, CompilationPhaseDescriptor/Protocol, PreparedCompilationInput, CompilationState, CompilationPreparationPhase, CompilationPhaseResult/Outcome, CompilationArtifactConflict/Collection, CompilationResult and ModelCompiler. Immutable gate/composition/state/outcome contracts prepare actual canonical inventory, retain diagnostics and atomically expose only successful objective outputs. No concrete artifact generator or universal IR.

compiled_contracts.public: CompilationArtifactKey, CompilationArtifactKind and read-only CompilationArtifact protocol for future owned immutable typed representations. Semantic identity stays separate from artifact membership key; no payload format, hashing, serialization, storage or publication implemented.

model_authoring.public: optional validated_model binding on actual ModelValidationResult, populated by the existing pipeline with its exact request.model. Existing constructors/status semantics remain compatible, but legacy evidence fails closed at compiler entry. ModelDiagnosticExtension/COMPILER origin plus CompilerPhaseDiagnosticView and CompilationDiagnosticReport provide a narrow immutable MOD-09 presentation boundary with actual original diagnostic values/evidence.

model_loader.public: consumes only that public presentation projection, preserves compilation status/phase views separately from actual validation evidence/status/readiness and enriches existing source/report transports. It never imports/executes compiler-core.

## Changed production and governance files

- platform/compiler/compiler-core/src/compiler_core/public.py
- platform/contracts/compiled-contracts/src/compiled_contracts/public.py
- platform/model/model-authoring/src/model_authoring/public.py
- tools/model-loader/src/model_loader/public.py
- architecture.json: one compiler-core -> model-authoring public API edge; no activation/profile/waiver change.

Created documentation:

- docs/compiler/compiler-foundation.md (includes Mini Sales usage, not executed)
- docs/architecture/decisions/ADR-0032-compiler-foundation.md
- docs/architecture/cmp01-verification.md
- test-archive/CMP-01/README.md
- test-archive/CMP-01/CMP-01-deferred-tests.md (156 cases, one detailed collection)
- test-archive/CMP-01/CMP-01-deferred-test-spec.md (standing-name navigation)

Modified documentation: README.md, docs/architecture/repository-structure.md, docs/architecture/dependency-rules.md, docs/model/validation-pipeline.md and docs/model/model-validation-diagnostics.md. Existing test sources/prior archives/historical verification, original Mini Sales, runtime contracts, architecture-policy/exceptions/profiles, activation markers and CI deferral remain intact.

## Architectural decisions

Compiler accepts actual immutable canonical input with explicit context/target and actual bound VALID/READY evidence. Binding uses the same original canonical object, not context/count/equal membership/content/hash. No earlier-stage transformation or validation execution is invoked. Trusted typed in-process association is not a cross-process/provenance/security certificate.

Foundation-preparation can complete with real preparation inventory and no artifacts; artifact-build requires EMIT_ARTIFACTS and nonempty owned output, unavailable by default in CMP-01. Unknown/missing capabilities fail closed as incomplete, not model-invalid semantics. Mandatory preparation cannot be removed. Explicit descriptor snapshots define order/prerequisites/capabilities; no scheduler, parallelism or dynamic discovery. Unexpected phase defects propagate distinctly; blocked phases and discarded candidate outputs are explicit.

Artifact collection sorts explicit logical keys, rejects every duplicate key without last-write-wins and holds frozen typed implementations. Failed/incomplete results expose no successful preparation/artifacts; phase outcomes contain no candidate payloads. Future artifact contracts own payload/IR invariants. No persistence, deployment, control-plane authorization or runtime execution.

MOD-09 receives original diagnostics via an explicit model-authoring-owned presentation projection. Loading tooling keeps its designated profile and inward dependency; compiler implementation/source tooling remain separate. Compilation and validation outcomes stay distinct; original validation evidence and diagnostics are not reinterpreted.

## Separate static activities

- python3 scripts/dev.py lint: syntax/whitespace/architecture succeeded after boundary correction.
- python3 scripts/dev.py build: syntax/boundaries/manifest public MODULE_NAME imports succeeded.
- python3 scripts/dev.py fitness:json --output build/cmp01-fitness.json: all 44 static rules across nine modules/45 production sources, one shared scan; no failures/cycles/warnings/waivers/suppression.
- python3 scripts/dev.py dependencies:json: one justified declared compiler -> authoring API edge, no dependency violations/cycles. Runtime and tooling profiles retained.
- git diff --check: clean patch whitespace.
- Markdown inventory: 156 stable case headings and NOT_RUN — DEFERRED statuses; documentation generation imported no project modules/executed no scenarios.
- Read-only source and installed distribution metadata inspection.

An initial static scan rejected a direct model-loader -> compiler-core presentation import with ARCH-DEP-006. Removed that import/manifest edge and inverted reporting through an explicit model-authoring-owned projection; subsequent checks passed without profile relaxation or waiver. This was a static dependency check, not deferred suite execution.

No ModelCompiler/phase/request/artifact/report scenario, MOD-08 validation run, example or custom deferred runner was executed. No pytest/unittest/manage.py test/tox/nox or CLI/runtime/doctor smoke. Build imports registered public MODULE_NAME values only; it does not establish compiler behavior or produce semantic artifacts. CI comprehensive test/smoke steps remain disabled and must be confirmed skipped.

## Django / DRF, limitations and readiness

Metadata: Python 3.12.14, PyYAML 6.0.3; Django/DRF absent. No existing compiler HTTP API requires modifications, so no endpoint/serializer/ORM/migration/database/dependency upgrade. Future applicable approved APIs remain thin DRF adapters under existing authentication/permissions.

General SK-11/full TYPE-01 remain unavailable; actual bounded diagnostics/current canonical host/data kind are reused. Concrete generator/IR/publisher/control-plane/runtime capabilities are intentionally absent; default artifact-build remains INCOMPLETE. Exact-object evidence does not transfer automatically across serialization/processes. Extension implementation purity/deep future payload immutability, actual validation provenance, source pairing and optional detail disclosure remain caller obligations. No behavioral verification yet.

Foundation is ready for later explicitly authorized verification and subsequent compiler architecture review within these limits. Stop CMP-01; no CMP-02 implemented automatically.
