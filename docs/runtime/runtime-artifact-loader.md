# RUN-01 — Runtime Artifact Loader

Implementation status: complete within the available contracts. Testing: **DEFERRED / NOT VERIFIED**. No runtime load has been demonstrated. This is an internal Python service in the selected Django/DRF backend architecture; no HTTP route, ORM model, database, migration, publisher, registry, activation or executor is introduced.

## Inspected repository and capability gaps

The workspace requires Python 3.11+, inspected locally with Python 3.12.14; CI uses 3.11/3.12/3.13. Django and djangorestframework distribution metadata are **NOT_INSTALLED**. `adapters/http/` is a documented future boundary, with no actual authenticated API workflow, permission integration or applicable serializer/view to modify. Installing a framework or creating an endpoint would not supply missing authority.

Inspected Kernel semantic identities, QName, context, versions, ElementRef and SemanticElement protocol; TYPE field IDs/data/constraints/type references; CanonicalModel and bound MOD-08 validation evidence; CMP compiler status/diagnostics/configuration/manifests/materialization/read planning/retrieval; existing runtime marker and adapter/application declarations. Full TYPE-01, SemanticInstance and general SK-11 remain unavailable. No runtime producer, encoder, content format implementation, decoder, approved runtime target, authenticated publisher or trusted load authorizer exists. These gaps are not replaced with invented implementations.

## Ownership and integration

| Owner | Responsibility |
| --- | --- |
| `compiled_contracts.public` | Existing artifact key/kind/origins/dependencies/descriptors; optional immutable content declaration |
| `compiler_core.public` | Original bound manifest, committed receipt, CMP-09 planning/read contracts and diagnostic objects; unchanged |
| `artifact_writer.public` | Existing approved-root read-only filesystem reader; unchanged |
| `runtime_core.public` | Pure runtime requests, authority/source/decoder ports, dispatch, compatibility, bounded immutable output and coordination |
| `runtime_artifact_loader.public` | Explicit tooling composition between actual compiler-owned contracts and neutral runtime contracts |
| Future Django/DRF adapter | Resolve authenticated authority and approved sources, invoke this internal service and present safe outcomes |

The new `runtime-artifact-loader` module is at `tools/runtime-artifact-loader`, with declared compiler-core/runtime-core public dependencies and a narrow tooling profile. Runtime still imports only Kernel and compiled-contracts. No zone relaxation, dependency exception, compiler-to-runtime import, runtime-to-compiler import, private import or bootstrap activation registration. The bridge resolves no files itself and duplicates no filesystem protections.

## Content declaration extension

`RuntimeArtifactMetadata` gains trailing optional `content_declaration=None`, preserving old positional construction and legacy metadata. It contains distinct typed RuntimeArtifactFormatId, RuntimeArtifactFormatVersion, RuntimeTargetId, RuntimeCompatibilityVersion and bounded distinct RuntimeCapabilityId requirements. No concrete format name or artifact kind is approved. This is producer-owned manifest metadata, not guessed from filenames/bytes or a new encoding. Existing descriptor equality, manifest/receipt membership and writer/reader associations automatically retain the declaration. Legacy declarations remain valid for compilation/materialization but insufficient for runtime decoding.

SemanticVersion, manifest V0, IR V0, content format version and runtime compatibility version stay independent. All supported format/runtime compatibility matching is exact; no ranges/latest/migrations. Compilation `artifact-build` is the manifest's build objective, distinct from a runtime target.

## Requests and application orchestration

`CmpRuntimeArtifactLoadRequest` retains the actual CMP-09 ArtifactReadRequest (original manifest, committed receipt, explicit selection, logical approved source and policy), plus RuntimeArtifactLoadContext and RuntimeArtifactLoadPolicy. It never accepts raw bytes, an arbitrary filesystem path, a dictionary payload, a decoder callback or a Boolean authority override.

`RuntimeArtifactLoadingService` receives a trusted injected CMP-09 reader, authorizer, explicit decoder catalog, runtime policy ceilings and existing ArtifactReadPlanner. It bounds the entire manifest count before planning and requires **ALL_DECLARED_ARTIFACTS**. Pure CMP-09 planning rechecks the original canonical/evidence/output association, complete manifest/receipt membership and committed source, byte limits and mandatory digest evidence. This calls no compiler, semantic validator or filesystem reader. A planning failure preserves original CMP diagnostics and maps to RUN-004/005/007/018, with the actual FAILED/INCOMPLETE status. Planning may report missing integrity before missing authority; neither path accesses bytes.

Only after accepted planning does the bridge project a RuntimeArtifactLoadBinding: existing manifest identity/version token, semantic scope, original compilation target, original descriptor objects, selected keys and completeness. This is a **projection**, not a second manifest, copied compiler graph, portable provenance token or authenticated publication record. The tooling source retains the actual CMP request. Binding identity is specific to the original source invocation; equal-looking projections do not authorize another receipt or invocation.

The pure RuntimeArtifactLoadRequest contains that binding, the typed context and bounded policy. Source/authorizer/decoders are injected by trusted hosting composition, never selected through request fields. The internal service is not automatically registered in CLI/bootstrap or exposed to HTTP callers.

## Authorization before access

Default `UnavailableRuntimeArtifactLoadAuthorizer` rejects with INCOMPLETE / RUN-002. An approved application or future Control Plane implementation must authenticate its caller and issue RuntimeArtifactLoadAuthorization through the injected authorizer port. The decision has bounded non-secret source/decision references and binds the **exact** source binding, semantic context, runtime target and ordered selected identities. Missing, Boolean, differently bound, stale or broader decisions are rejected; no caller request field can submit a decision directly.

These in-process dataclasses are not cryptographically unforgeable security tokens. Trust is in the controlled composition boundary and its authenticated authorizer implementation. Direct access to trusted constructors/ports is not an external API. No currently installed integration grants authority. Authority to load grants neither activation nor execution.

## Compatibility and dispatch before byte access

Runtime v0 requires original manifest schema `0`, original compiler objective `artifact-build`, matching semantic context, whole manifest membership and known internal dependency keys. Origin/dependency metadata is bounded by the effective element budget. Subsets (even an explicit set naming every member) are rejected because no package completeness/subset contract exists. Dependencies are not expanded, resolved semantically, searched remotely or topologically sorted. Self/mutual artifact dependency cycles are allowed for independently decoded definitions; a format needing dependency-aware construction is not supported by this decoder contract.

The immutable catalog defaults to zero registrations and zero recognized kinds. Trusted owners may recognize a real producer kind without approving a decoder: RUN-011 then reports unavailable decoding. Unknown kind, absent/unsupported format, unsupported exact version, incompatible runtime target/compatibility version and unknown required capabilities have separate diagnostics. Dispatch is a unique bounded tuple of kind/format/version/runtime target/compatibility version; registration and artifact ordering are deterministic. No filename inference, arbitrary JSON fallback, IR conversion, plugin scan, data-selected import or code deserialization.

Only real owned formats may later supply registrations. An approved decoder must be a frozen slotted class with immutable bounded configuration, declare concrete frozen slotted representation graph classes and attest that it enforces parse limits **before allocation**. That attestation is a trusted approval requirement, not a runtime sandbox or empirical proof. There is no actual decoder implementation to approve in this task. Empty/missing capabilities fail closed without fake bytes or representations.

## Verified reader boundary

After authorization and compatibility approval, `CmpRuntimeArtifactByteSource` calls the injected CMP-09 reader **once** for the complete set, with DIGEST_VERIFIED and the minima of runtime/original read ceilings; the reader can further lower those ceilings. No per-artifact re-read, filesystem enumeration, open, cleanup, write or encoder in RUN-01.

The bridge requires the actual plan/request association, complete selected entry inventory, effective digest policy, non-increased ceilings and original committed descriptor/location/length/digest evidence. FAILED/INCOMPLETE reading returns no bytes to decoding. The neutral RuntimeVerifiedArtifactBytes contains the same descriptor and immutable content plus RuntimeArtifactSourceEvidence: exact original binding/key, logical root/output/location, measured length and approved verified SHA-256. No absolute root path, credentials or raw bytes in repr. CMP-09 owns digest computation and filesystem protections; RUN-01 does not rehash or reinterpret its size-only evidence as cryptographic verification.

The operation-local recording adapter retains **the exact original** CompilationDiagnostic objects in CmpRuntimeArtifactLoadResult, including fields not part of the neutral projection. Runtime diagnostics carry ordered code/message/severity/read-stage/key/kind/manifest/location/source-type projections without turning them into model validation errors. INFO/WARNING/ERROR meaning is preserved. Neutral causes are traceability, not a replacement of full CMP diagnostics.

Digest verification proves declared byte integrity, not publisher authenticity, authorization, activation or execution. SHA-256 must already be supplied through the committed receipt; no digest is fabricated to turn a legacy size-only receipt into a successful runtime load.

## Decoding and output invariants

RuntimeArtifactDecoder consumes RuntimeVerifiedArtifactBytes, context and remaining aggregate parse limits; expected failures use RuntimeArtifactDecodeResult or RuntimeArtifactLoadError. Unexpected programming errors propagate. No broad catch silently substitutes INCOMPLETE for broken code. Decoder diagnostic associations must match this exact manifest/artifact/context/target and are enriched where absent; conflicting associations fail.

Success must return the exact approved representation class. Iterative graph inspection traverses only declared fields of approved frozen slotted dataclasses, existing Kernel/artifact coordinate values, exact tuples and closed scalars (`None`, bool, int, str, bytes). No unrestricted dictionaries, mutable lists/sets, floats, arbitrary objects, callables, dynamic attributes or inherited instance dictionaries. Additional format-specific immutable classes require explicit approval. Actual object cycles are rejected; semantic reference IDs are ordinary leaves and do not imply recursion. Semantic context, exact ElementVersionRef origins and explicit model-wide meaning must equal the descriptor; no generated semantic identity, canonical lookup, constraint inference or business instance.

Defaults: 128 artifacts, 32 MiB/artifact, 128 MiB aggregate input, depth 32, 100,000 decoded element occurrences and 32 MiB conservative scalar budget across the complete decoded set. Text counts four bytes/character, integer storage uses bit-size estimate, bytes count by length. Client settings are bounded by trusted server minima. Repeated immutable values count by occurrence. The traversal also bounds its pending frontier before stacking children. Each later decoder receives the remaining aggregate budget; depth is per representation. These are practical structural bounds, not exact Python heap/RSS or CPU/latency guarantees. No arbitrary parser/subprocess sandbox is added.

LoadedRuntimeArtifact retains descriptor/context/approved typed representation/source evidence/decoder registration and measured decoded budgets, without automatically retaining the original read buffer. Any binary field in a representation must be explicitly owned by its approved format; no default content disclosure is introduced. LoadedRuntimeArtifactSet requires exact authorized complete manifest membership/order, same binding and effective policy, and all aggregate bounds. It is an inactive value output, not a runtime catalog. RuntimeArtifactLoadResult has explicit SUCCEEDED/FAILED/INCOMPLETE; non-success exposes no partial loaded set. A later failure discards locally accumulated representations from the public result.

## Determinism and supported comparison

No timestamps, random identities, global counters, discovery order, request HTTP state or directory enumeration enters runtime loading. Manifest key order is preserved; all decoder support is preflighted before reads/decodes. Decoder diagnostics stay in operation/manifest order.

RuntimeArtifactLoadEquivalence follows CMP-06's supported-observation comparison pattern without importing compiler implementation. It compares explicit status/diagnostic associations (human message text excluded), context, authority references/scope, policy, source facts, concrete decoder implementation classes/configuration, declared graph types and structural representation values. Successful comparison requires the **same original bound source object**; cross-source/compiler-input equivalence is explicitly unsupported. No repeat load/compiler utility, canonical serialization/hash, new global model fingerprint or claim that digest equality proves byte equality. Future verification must control the same actual authorized scope, verified bytes and decoder implementations independently.

## Mini Sales — conceptual only, not executed

Use actual [Customer source](../../examples/authoring/mini-sales.json) and [reference source](../../examples/authoring/mini-sales-references.json). Kernel syntax is `sem_<UUIDv4>` / `fld_<UUIDv4>`, not the illustrative `typ_customer_123` / `fld_name` tokens.

| Coordinate | Existing value |
| --- | --- |
| Context | `sem_550e8400-e29b-41d4-a716-999999999999` |
| QName | `sales.Customer` |
| Customer origin | `sem_550e8400-e29b-41d4-a716-000000000001@1.0.0` |
| Employee origin in reference fixture | `sem_550e8400-e29b-41d4-a716-000000000002@1.0.0` |
| Customer name field | `fld_550e8400-e29b-41d4-a716-000000000001`, required/non-null String, max-length 200 |
| Customer active field | `fld_550e8400-e29b-41d4-a716-000000000002`, required/non-null Boolean |
| Customer creditLimit field | `fld_550e8400-e29b-41d4-a716-000000000003`, optional/non-null Decimal, minimum 0, precision 18, scale 2 |

CMP-05 CompiledTypeIR envelopes describe intermediate compiler state; they are rejected as requests/artifacts here. Real runtime producers/encoders must separately emit owned immutable bytes and declared formats, with complete CMP-07/08/09 evidence. Only then can an authenticated source authorizer plus an approved bounded decoder construct Customer/Employee representations. Preserve only information actually encoded, including Employee's stable self-reference where the eventual format supports it. Do not reconstruct fields/constraints from the canonical model, resolve latest versions or instantiate business records.

Missing authorization => RUN-002 INCOMPLETE. Missing decoder for a recognized real kind => RUN-011 INCOMPLETE; unknown kind => RUN-008 INCOMPLETE. Unsupported version => RUN-010 INCOMPLETE; wrong context => RUN-014 FAILED. Missing file/integrity failure retains CMP-09 diagnostics and prevents complete-set success. Even a future successful load remains inactive and executes no action/event/workflow. No future format or success fixture was created/run here.

## Deferred verification and readiness

Exactly one archive: [RUN-01-deferred-tests.md](../../test-archive/RUN-01/RUN-01-deferred-tests.md). No archive README, automated tests, test infrastructure, scenario script or runtime demonstration. All scenarios **NOT_RUN — DEFERRED**; tests created/executed **0**. Success/format scenarios require a genuinely approved future producer/encoder/decoder, authenticated authorizer, fixed revision and explicit future permission to execute. Historical executed verification remains untouched.

See [ADR-0042](../architecture/decisions/ADR-0042-runtime-artifact-loader.md) and [static completion record](../architecture/run01-verification.md). Framework/API, authenticated publication and domain-specific runtime loading remain unavailable prerequisites. Implementation is ready for review and later authorized verification; no end-to-end success or activation is claimed. Stop RUN-01; RUN-02 was not started.
