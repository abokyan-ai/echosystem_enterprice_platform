# CMP-07 — Runtime Artifact Manifest

Date: 2026-10-11. Status: **DEFERRED / NOT VERIFIED**. No assembler/manifest/metadata/compilation/Mini Sales scenario was executed.

## Actual architecture and capability gap

The existing nine-module Python compiler remains authoritative. Current ModelCompiler supports foundation-preparation and artifact-build only. It has no concrete final artifact-producing phase/runtime artifact kind. TypeCompilerPass emits SemanticIREnvelope/CompiledTypeIR, never CompilationArtifact. Current artifact-build remains INCOMPLETE/CMP-010 and yields no complete runtime manifest. Do not fabricate a producer, descriptor, kind, digest, location or success to hide this gap.

Shared compiled-contracts adds RuntimeArtifactDependencyRef, RuntimeArtifactMetadata and RuntimeArtifactDescriptor alongside existing CompilationArtifactKey/Kind/Protocol. They have Kernel-only dependencies and contain no compiler execution/type pass/model-authoring state. Compiler-core owns RuntimeArtifactManifestId, V0 schema, RuntimeArtifactKindSupport, checked compilation association, manifest, assembly result and assembler. No new modules/import edges/runtime imports. Public manifest is currently an in-process bound compiler output description, not a serialized/published runtime package. Future Runtime can use approved shared descriptor/artifact contracts; portable snapshot/configuration provenance and manifest transport require actual downstream contracts before Runtime consumption. No compiler-private IR/state exposed as a runtime contract.

## Minimal origin integration

CompilationResult gains one trailing optional output_origin field, preserving earlier positional arguments, structural result comparison and legacy construction (origin is excluded from generic result equality/repr/hash). ModelCompiler emits CompilationOutputOrigin(original request, original frozen compiler) for every typed-request outcome after execution/gating. Wrong-root input still produces CMP-001 without origin. Original result status, state, artifact protocol and final-generation objectives are unchanged. Origin is immutable, unhashable and identity-based per original compilation invocation; no generated ID/counter/hash/time.

Manifest assembly requires the same original request/compiler objects carried in the result origin, original canonical object/prepared context, same original validation evidence, matching ordered descriptors and COMPLETED/executed=True for all configured phases. CMP-06 drift audit must remain clear. A legacy successful result without output origin fails CMP-038, even if content/phase count looks equal. Semantic equivalence cannot replace provenance gates.

CompilationOutputOrigin retains only original immutable input/configuration, not result/artifacts. RuntimeArtifactManifestCompilationAssociation accepts the actual result as a dataclass InitVar, validates it and extracts complete descriptor/outcome snapshots. It does not store the result or artifact payload instances. Original result origin is preserved in the association as the compilation-output scope marker. Request/source context and approved frozen compiler options remain original in-process values, not cryptographic provenance, portable snapshot IDs or access permissions. Caller-forged typed state is not authenticated proof.

## Supported target and completeness

Only actual BUILD_TARGET (`artifact-build`) can produce a runtime manifest. foundation-preparation's successful zero-artifact objective is not a runtime artifact target and is rejected CMP-035. No new runtime target/profile or zero-artifact runtime option introduced.

Completeness uses the original SUCCEEDED build result, all configured completed/executed phases, EMIT_ARTIFACTS capability, actual nonempty final collection and exact preservation of every artifact descriptor. It is not inferred from count alone. Current CMP-01 contract does not define required per-type output cardinality or target-specific kind schema; do not infer one-to-one type/artifact coverage. Future producer owns its target requirements. Manifest refers only to the actual declared build objective and whole authoritative final inventory, not all future platform coverage.

FAILED/INCOMPLETE results remain their original statuses; return existing original diagnostics plus CMP-031 and no manifest. Missing generator outputs cannot be upgraded to success. Unsupported target/kind/schema/source/binding/integrity rejects atomically. A manually supplied subset, extra descriptor, changed metadata or empty inventory cannot match the checked association.

## Explicit runtime kind approval and producer metadata

RuntimeArtifactManifestAssembler defaults to support=(), meaning no runtime artifact contracts currently approved. An application/compiler owner must explicitly provide RuntimeArtifactKindSupport(existing CompilationArtifactKind, actual frozen dataclass artifact class) when a real producer exists. The approved class must declare original key/kind/scope/target/semantic_dependencies plus manifest_metadata fields. Match exact emitted class and kind; no dynamic import/string plugin discovery/author-controlled trusted kind. Approval records are immutable, sorted by existing kind token; duplicate kind declarations are ambiguous and rejected. This is a small explicit contract list, not a broad target catalog or producer implementation.

manifest_metadata must be actual immutable RuntimeArtifactMetadata. It separately declares semantic_origins, model_wide and artifact dependencies. Existing artifact semantic_dependencies are NOT silently reinterpreted as origins, and semantic field references do not imply artifact dependencies. Producer must supply its real origin information explicitly. Empty origins require model_wide=True; exact origins require model_wide=False and at least one original canonical ElementVersionRef. Repeated origins reject. The metadata schema defines origins as membership sets normalized by semantic-ID/numeric-version; no source field order changed.

Descriptor contains existing artifact key/kind and metadata only. No payload, schema-generated code, raw mutable objects, physical path, fake content digest/locator or publication/active flag. Full artifact bodies are neither copied nor retained through the manifest. Metadata is copied from actual emitted approved artifacts and canonical membership is checked. One origin/many origins/model-wide and multiple versions are supported; no latest, QName identity, transitive provenance graph or inferred global origin.

## Dependencies and ordering

RuntimeArtifactDependencyRef preserves existing CompilationArtifactKey and explicitly refers to the current manifest scope only. Dependencies are unique membership sets sorted by artifact key. No external dependency contract currently exists; unsupported external/remote references are not invented or resolved. Every internal key must be present in the final inventory. Report declaring key plus typed related artifact target for the unresolved dependency. Self-dependencies and cycles are allowed by v0 membership policy because no acyclic/load-order requirement exists. No graph solver/topological loading/deployment plan.

Descriptors follow existing CMP-01 artifact-key order. All explicit exact origins follow Kernel ID/numeric-version coordinates; dependencies artifact-key order. Duplicate descriptors reject even equal, never last-write-wins. Invalid same-key descriptors use stable kind/exact-origin/model-wide/dependency tie keys for diagnostic ordering only; diagnostics retain all conflicting artifact key/kind and origin associations. Valid inventory still follows unique artifact key order. Supported metadata/kind errors are gathered in artifact order; origin errors in exact origin order; duplicate/dependency inventory errors in key/dependency order. No timestamp/path/localized-name/database insertion/ambient dictionary iteration controls output.

## Identity, schema and semantic declaration comparison

RuntimeArtifactManifestId is an independent caller-owned bounded token with prefix manifest-, for example manifest-sales.runtime.v0. It is not an artifact/semantic/IR ID and is never generated. Scope: one original CompilationOutputOrigin/invocation. assemble takes existing_manifests as explicit caller-provided inventory; rejects a repeated ID in that original scope and rejects duplicates already in that scope's supplied inventory (CMP-043). Same token in separate invocation scopes is allowed. Default empty inventory establishes no global uniqueness; caller owns completeness of supplied inventory. No global/distributed registry or persistence.

RuntimeArtifactManifestSchemaVersion.V0='0' is an independent strict enum; SemanticVersion/IR schema enum/string do not substitute, and no migration/inferred version. Manifest validates exact identity/schema/scope/target/checked association plus equality to the entire validated descriptor inventory.

same_declaration(other) provides supported manifest metadata equivalence: identity/schema/scope/target/descriptors, kind approvals, CMP-06 independently accepted request/configuration comparison and ordered semantic phase outcomes. Original in-process association remains identity-bound; comparison never authorizes a foreign result. It does not compare actual artifact payloads, verify content digests, prove byte reproducibility or establish portable compiler version equality. Human/source presentation differences are retained outside semantic comparison. Ordinary object equality is identity; use explicit bounded same_declaration for declared structure comparison.

## Assembly and diagnostics

assemble(result, request, compiler=..., identity=..., schema_version=V0, existing_manifests=()) returns RuntimeArtifactManifestAssemblyResult with existing CompilationStatus values. Successful assembly contains complete immutable manifest; FAILED/INCOMPLETE contains diagnostics and no partial manifest. No compiler/validator/lowerer execution, payload execution, file/network read, publication or mutation. The result preserves compiler diagnostics on success and non-success compilation prerequisite. Unexpected programming defects propagate; catch only expected RuntimeArtifactManifestError.

Typed leaf metadata/descriptor/dependency constructors use normal TypeError/ValueError for malformed owned values; compiler-level manifest/assembly ordinary integrity errors use actual CompilationDiagnostic and RuntimeArtifactManifestError. Missing mandatory constructor args remain Python TypeError, not fabricated domain execution evidence. Manifest errors cannot become successful partial output.

| Code | Actual violation |
|---|---|
| CMP-031 | Authoritative compilation is FAILED/INCOMPLETE |
| CMP-032 | Unsupported manifest schema |
| CMP-033 | Invalid independent manifest identity |
| CMP-034 | Semantic context mismatch |
| CMP-035 | Unsupported/mismatched runtime manifest target |
| CMP-036 | Exact canonical/evidence/origin mismatch |
| CMP-037 | Unapproved kind/concrete artifact contract or ambiguous approval |
| CMP-038 | Missing original output binding or unmatched configured completion |
| CMP-039 | Incomplete artifact manifest metadata |
| CMP-040 | Unknown internal artifact dependency |
| CMP-041 | Duplicate artifact descriptor identity |
| CMP-042 | Missing/different/incomplete final artifact inventory |
| CMP-043 | Manifest identity collision in original invocation scope |

CMP-02 association gains trailing typed related_artifact_targets and manifest_identity fields; old positional arguments preserved. Compiler diagnostic original payload retains all associations, so existing reports preserve primary/related artifact/manifest evidence. Existing general model projection still presents its existing primary artifact view; no new HTTP DTO/UI is invented. CMP-06 semantic diagnostic comparison includes new typed associations. Actual canonical/source associations may enrich reports, never fabricate physical location or artifact origin/ID. Full SK-11 remains unavailable; original seam is used.

## Mini Sales — unexecuted contract specification

Use original sales scope sem_550e8400-e29b-41d4-a716-999999999999; Customer sem_550e8400-e29b-41d4-a716-000000000001 and Employee sem_550e8400-e29b-41d4-a716-000000000002, actual fld_ UUID fields/constraints from existing Mini Sales files. Prompt typ_customer_123/fld_name aliases are not actual identities. Current original artifact-build with Customer/Employee Type IR only is INCOMPLETE/CMP-010; assembler retains its diagnostics plus CMP-031/INCOMPLETE, no runtime manifest. Preparation success still cannot certify runtime output (CMP-035).

A future owned immutable runtime metadata artifact producer, approved kind/schema/actual artifact class and valid BUILD_TARGET result are prerequisites for positive artifact cases. Hypothetical Customer and Employee artifacts keep their actual producer-supplied existing CompilationArtifactKeys; no keys/artifact bodies are fabricated here. Explicit metadata declares Customer@1.0.0 and Employee@1.0.0 exact origins. A future Customer@1.1.0 origin is retained separately only if explicitly canonical and represented; multiple artifacts per source/many origins per artifact are allowed. Employee.manager's versionless semantic self-reference does not automatically declare artifact dependency.

If real Employee artifact explicitly depends on Customer artifact, that key must exist. Missing key -> CMP-040 with declaring/dependency association, no fetch or partial manifest. Two descriptors claiming same key -> CMP-041, not overwrite. Changing supported metadata relative to the checked inventory -> CMP-042. Positive future assembly preserves original output association and complete immutable key-ordered declarations under manifest-sales.runtime.v0/V0. All positive producer-dependent scenarios remain blocked until actual producer/approved kind exists; none was generated or executed.

## Boundaries, verification and stop

Python domain is independent of Django initialization; PyYAML 6.0.3 installed, Django/DRF absent. No applicable compiler HTTP boundary needed modification. No new endpoint/auth/permissions/ORM/migration, runtime imports/loading/execution/instance/action/event registration, publisher/activation/Control Plane authority, file storage/digest/hash/cache/serialization/deployment. Runtime descriptor metadata is not an artifact payload and manifest integrity is not permission or availability.

[ADR-0038](../architecture/decisions/ADR-0038-runtime-artifact-manifest.md), [implementation/static record](../architecture/cmp07-verification.md), [sole detailed deferred specification](../../test-archive/CMP-07/CMP-07-deferred-tests.md). Tests implemented/executed 0; DEFERRED / NOT VERIFIED. Static checks establish syntax/loadability/boundaries only. Future execution needs explicit authorization, pinned revision and real owner fixtures/contracts. Stop CMP-07; no CMP-08.

## CMP-08 consumer

[Artifact Writer](artifact-writer.md) requires the original successful assembly and supplied final compilation result, rechecks original invocation/configuration/evidence and exact descriptor membership, then matches original artifact objects to explicitly approved byte fields. Manifest remains metadata; no payload added or IR promotion. Writer receipt records real complete materialization only, not publication/runtime authority. Linux infrastructure is separate tooling; runtime imports unchanged. **158** CMP-08 cases deferred, tests executed **0**.
