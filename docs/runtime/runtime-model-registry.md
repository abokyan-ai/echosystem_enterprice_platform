# RUN-02 — Runtime Model Registry

Implementation complete within available contracts; **DEFERRED / NOT VERIFIED**. No registration, lookup, snapshot, concurrency scenario or Mini Sales demonstration was executed. The service is pure Python inside the selected Django/DRF backend architecture; no API, ORM, migrations, persistent/distributed registry, activation or business execution.

## Actual inspected prerequisites

Workspace Python minimum 3.11; local 3.12.14; CI 3.11/3.12/3.13. Django and djangorestframework package metadata: **NOT_INSTALLED**. Existing HTTP adapters and Mini Sales application are documented ownership boundaries, not authenticated API implementations. No actual management workflow requires a serializer/view/service composition change.

Inspected RUN-01 actual RuntimeArtifactLoadResult/LoadedRuntimeArtifactSet, original load authority/context, decoder approval, deep immutable representation guards and verified source associations. Kernel owns ID/Namespace/QName/context/ElementVersionRef/ElementRef and numeric SemanticVersion. Existing TYPE-07 TypeRegistry indexes semantic model data; it is a different responsibility and is not imported or used as fallback. CanonicalModel, MOD validation evidence and CMP-07/08/09 associations stay upstream of Runtime. Full TYPE-01/SemanticInstance/general SK-11 remain unavailable.

There is **no real approved runtime producer/encoder/decoder, registrable decoded definition kind, definition extractor or authenticated registration/inspection authorizer**. RUN-02 supplies the functional registry and explicit unsupported integration point without inventing Customer payloads, formats, authorizations or successful evidence.

## Public contracts and ownership

All production changes are in existing `runtime_core.public`; no new module or cross-module dependency. Runtime still consumes only Kernel and compiled-contracts. Existing source-loading tooling, compiler and RUN-01 composition service stay unchanged. Runtime's stdlib allowlist adds **threading** solely for the implemented private Lock; no other zone ceiling or dependency exception changes. Registry uses no Thread/worker startup, OS/file/network/subprocess facility.

| Contract | Role |
| --- | --- |
| RuntimeModelRegistryScope / RuntimeModelRegistryKey | Explicit semantic context + runtime target, with exact ElementVersionRef |
| RuntimeModelRegistryPolicy | Positive trusted batch/scope/total/snapshot ceilings, REJECT_CONFLICTS and explicit empty policy |
| RuntimeModelRegistrationRequest / Result | Actual original RUN-01 result + destination scope/policy; complete committed IDs or no partial output |
| RuntimeModelDefinitionRepresentation / ExtractionSupport / Catalog | Explicit approved already-decoded node contract and trusted bounded extraction |
| RuntimeModelDefinition | Existing decoded node plus exact key, optional QName, supported kind and original load/artifact evidence |
| RuntimeModelRegistryAuthorizer / Authority | Separate instance/scope/operation/batch/selector-bound authenticated application integration |
| RuntimeModelLookupRequest / Result / MembershipResult | Exact lookup, routine NOT_FOUND and explicit VERSION_REQUIRED |
| NameInspectionRequest / VersionInspectionRequest | Authorized bounded candidate or exact-version enumeration, not resolution |
| RuntimeModelRegistrySnapshot / SnapshotResult | Coherent immutable scoped membership or explicit unavailable/unauthorized result |
| RuntimeModelRegistry / LocalRuntimeModelRegistry | Registry port and real local atomic implementation |

Supported definition kinds are explicit RuntimeModelDefinitionKind tokens, with **zero default approvals**. No Type/Action/Event/Policy/Workflow hierarchy or automatic category registration. Kind is distinct from artifact kind and source encoding.

## Scope, lifetime and identity

The application owner explicitly creates each registry with a nonempty distinct tuple of at most 128 allowed scope coordinates and trusted policy/ports. Each instance begins empty and owns only its local membership. It is not a process-global singleton and is not auto-created by public import, CLI/bootstrap, Django AppConfig or service discovery. Restart/worker replacement loses state; separate instances/processes/workers do not synchronize. This is local authority, not a distributed deployment catalog.

Registry key = **RuntimeModelRegistryScope + ElementVersionRef**. Context/target do not follow namespace, tenant, organization, files or Django labels. Scope is independent of tenant permission. Versions coexist; no replacement/latest/migration/compatibility inference. Stable ordering is context ID, target token, semantic ID, **numeric major/minor/patch**. QName case/namespace semantics reuse Kernel; names are inspection metadata, not keys or MOD-06 resolution. Optional absent names have no name-index entry.

## Verified input and explicit definition extraction

Registration accepts an actual RuntimeArtifactLoadResult, never an arbitrary tuple/node/dictionary or a LoadedRuntimeArtifactSet alone. FAILED/INCOMPLETE loads cannot register; actual status is retained as failed/incomplete registration. Success must retain the complete original RUN-01 loaded set and exact matching destination context/target. Existing immutable loaded value contracts are rechecked without reader/decoder/compiler calls. This does not grant authority or prove a new signed publication.

Every mandatory artifact needs an explicitly injected RuntimeModelDefinitionExtractionSupport bound to the **same actual decoder approval object** used by RUN-01. It approves concrete frozen slotted node classes already present in the decoder's closed representation graph, supported definition kinds and whether an artifact may expose zero definitions. The extractor is a frozen slotted pure implementation with bounded immutable configuration and receives the remaining definition-count budget before collection allocation. Default support catalog is empty; missing support is INCOMPLETE / RUN-107.

An extractor selects existing decoded nodes through an explicit format-owned contract; it never opens/re-decodes source bytes or constructs definitions from CanonicalModel/Type IR. An approved node declares typed `identity`, `semantic_context`, `runtime_target`, optional `qualified_name` and `definition_kind` fields. These are a registry integration contract, not a new artifact wire format or domain type. No concrete decoder/extractor implementation is fabricated.

The registry verifies every selected node has the exact approved class, deep immutable graph and **actual membership in the original loaded representation**. Equal-looking copied/new objects are not original load evidence. Membership traversal checks object association only; it does not infer definitions, follow semantic references or use memory addresses as registry keys/content equivalence. Entries reuse the original node without copying fields/business data. Existing Kernel QName/Namespace and the new immutable kind coordinate are admitted by the shared RUN-01 immutable graph guard; this approves no format/decoder automatically.

For explicit per-definition artifact origins, the node's exact ID/version must occur in the original descriptor origin tuple. Model-wide provenance remains model-wide: an explicitly approved format may expose encoded exact nodes or zero individually registrable nodes. Encoded node identities are preserved without inventing descriptor semantic origins. Multiple origins and multiple definitions per artifact remain distinct; artifact count is not definition count.

All declared artifacts are processed; none is silently skipped for missing capability. Empty extraction is accepted only where that artifact's approval explicitly permits it. A complete zero-definition registration additionally requires **ALLOW_VERIFIED_NO_CHANGE** in both request and trusted server policy, valid success evidence and separate authority; otherwise INCOMPLETE / RUN-120. A permitted empty operation succeeds with zero committed IDs and unchanged state, not fake definitions.

## Registration and inspection authority

Possessing a loaded set/load grant/checksum does not authorize registry mutation or schema inspection. A trusted injected authorizer receives an internal RuntimeModelRegistryAuthorizationRequest binding the registry's instance-specific association, exact scope, operation, selected exact identities/name/ElementRef and original load result where applicable. Its RuntimeModelRegistryAuthority must retain **the same internal authorization invocation**, with bounded non-secret source/decision references. Boolean, reused, broader, other-instance, other-operation or differently scoped decisions fail RUN-104.

Default UnavailableRuntimeModelRegistryAuthorizer reports INCOMPLETE / RUN-103. No request field lets a caller submit a grant, extractor or service. Extraction is a pure bounded preparation before registration authority checks the exact derived key list; no mutation occurs before authority. Callbacks run outside the state lock. Missing format support may therefore be reported before unavailable registration authority; neither path alters state or accesses files.

Every public membership/lookup/name/version/snapshot operation invokes the authorizer for its **own operation and selector** before observing member data. A versionless lookup grant does not automatically authorize version enumeration; a name query does not implicitly grant whole-scope snapshot rights. Mutation results contain only submitted committed identities and original source association, not an unrequested whole-scope snapshot of other definitions. Snapshots require separate read authority.

These are in-process trusted composition contracts, not cryptographically unforgeable tokens or a sandbox for malicious injected Python. Hosting must authenticate callers and authorize the actual source/selector. No current installed adapter supplies those decisions. No tenant policy engine, activation authority or execution authority is introduced.

## Duplicate/conflict and atomicity policy

V0 **REJECT_CONFLICTS** rejects every existing exact scoped key, even a byte-identical/equal-looking definition or repeated original object. No verified replay equivalence contract exists, so there is no guessed idempotence, repr/hash comparison, last-write-wins, force-overwrite or field merging. Different exact versions/contexts/targets are separate entries. Different stable identities sharing a QName coexist as distinct keys and are reported ambiguous during name inspection.

Preparation builds private immutable entries, validates original association/encoded type/identity/name/kind/context/target/immutability, counts all selected definitions and detects duplicate batch keys. Duplicate diagnostics are emitted in stable key order. Two artifacts defining one exact identity are a duplicate conflict, not a merge. Any expected failure yields no committed identities; state remains unchanged.

After exact batch authority, a **private Lock** protects checking the current state, all existing-key conflicts/capacity, constructing the complete new state/result and one publication assignment. Thus a concurrent writer checks the latest state, not an outdated preflight snapshot. New read-only MappingProxy indexes and immutable tuple memberships are derived in canonical order. Result construction precedes publication, so an expected result validation failure cannot leave a hidden committed batch. No arbitrary extractor/authorizer/decoder callback runs while the lock is held.

Readers capture one immutable state/index tuple under the same lock, then construct bounded results outside it. They see a whole old or whole new membership, never half a batch or an iterator over mutable state. Previously returned snapshots keep their original tuple/definitions when later registrations occur. Concurrent disjoint valid batches have no lost update; same-key contenders cannot overwrite each other. Which conflicting caller commits first depends on thread scheduling and is **not** claimed deterministic. Completed equivalent membership enumerates deterministically.

No remove/update/rollback/active-version pointer, global registry, service activation/container or distributed lock.

## Lookup, inspection and snapshots

| Operation | Behavior |
| --- | --- |
| `lookup(RuntimeModelLookupRequest)` with ElementVersionRef | FOUND with one actual immutable entry, or routine NOT_FOUND / RUN-114 INFO |
| Exact lookup with ElementRef | VERSION_REQUIRED / RUN-116 INFO even when only one version exists; no automatic candidates disclosed |
| `contains` | Same authorized lookup semantics; true/false only for FOUND/NOT_FOUND, otherwise unknown (`None`) |
| `versions` | Separately authorized ElementRef enumeration returns all exact versions in numeric order, never selects one |
| `inspect_name` | One exact candidate FOUND; multiple versions/IDs AMBIGUOUS / RUN-115 INFO with ordered full candidates |
| `snapshot(scope)` | Separately authorized coherent complete immutable scoped snapshot, including a valid empty snapshot |

Routine absence does not label a definition semantically invalid. Malformed roots return INVALID_REQUEST; invalid/undeclared scope or mismatched authority fails without data; missing required authorization/capacity produces explicit INCOMPLETE. Exact lookup has no AMBIGUOUS fallback in coherent state. No auto-loading, filesystem scan, TypeRegistry/Compiler lookup, name fallback or version substitution. Snapshot/name/version inventories above their bound return INCOMPLETE / RUN-117 with no partial/truncated output.

## Limits and diagnostics

Defaults: 1024 definitions/registration, 8192/scope, 32768 total registry definitions and 8192 snapshot/name/version candidates. Request mutation limits use server minima and the stricter empty policy; they never alter server inspection configuration. Trusted scope/count/capacity checks occur before commit; snapshot capacity may be smaller than allowed membership and then exact lookup remains available while full snapshots are explicitly unavailable.

Original RUN-01 count/depth/element/scalar limits still constrain every loaded graph. Extracted classes/nodes are checked without parsing bytes. Definition wrappers retain shared original decoded/source associations; there is no duplicated RetrievedArtifact buffer or filesystem store. A future approved typed representation may expressly own binary fields; this task invents none and exposes no raw byte API. Retaining original loaded-set associations can retain other decoded members of that source set. Count bounds do not guarantee exact heap/RSS/CPU/latency; graph validation/association checks and copy-on-write rebuilds cost bounded traversal/sorting, not constant time. No general quota manager.

Reuse the existing RuntimeArtifactLoadDiagnostic/Failure/Stage/severity/status/expected-error model. Add registry codes **RUN-101…RUN-121**, registry stages and trailing typed scope/exact-definition/QName/kind/operation associations; old positional arguments remain valid. No second generic diagnostics framework or compiler-phase outcome. Shared supported load equivalence includes new associations. Registry diagnostic factory adds actual manifest/artifact and original semantic origins where known; no fabricated SourceLocation, bytes, credentials, private root or stack trace. Extractor diagnostics must match the actual invocation and are enriched where absent. Original RUN-01 warnings remain available on retained original load evidence. Unexpected programming faults propagate rather than becoming fake incomplete success.

## Mini Sales — conditional, unexecuted

Reuse [actual Customer fixture](../../examples/authoring/mini-sales.json) and [reference fixture](../../examples/authoring/mini-sales-references.json). Actual context: `sem_550e8400-e29b-41d4-a716-999999999999`; exact Customer origin: `sem_550e8400-e29b-41d4-a716-000000000001@1.0.0`; Employee: `sem_550e8400-e29b-41d4-a716-000000000002@1.0.0`. Illustrative `typ_customer_123` / `fld_name` are not valid Kernel IDs.

Only after real owned producer/encoder/decoder/extractor and authority integrations exist, a successful RUN-01 result could supply encoded Customer/Employee nodes. Atomic registration exposes both or neither; exact Customer@1.0.0 lookup returns that original definition; missing @2.0.0 returns NOT_FOUND. Customer ElementRef always requires explicit version selection. A separately produced @1.1.0 can coexist with @1.0.0; `sales.Customer` inspection then returns both ordered candidates without activation. Preserve encoded Employee self-reference as an immutable identity leaf; do not bind latest versions or recursively instantiate business objects. Same Customer exact key is rejected without overwriting; later Employee failure leaves previous membership unchanged.

Customer field definitions and constraints are only retained if actually encoded in the supported future runtime node. No reconstruction from canonical model or CompiledTypeIR, no constraint evaluation against records, semantic instance creation, action/event/policy/workflow execution or handler startup. No Mini Sales source/code/artifact/success fixture was fabricated or executed.

## Deferred archive and readiness

Exactly one [RUN-02 deferred archive](../../test-archive/RUN-02/RUN-02-deferred-tests.md), every case **NOT_RUN — DEFERRED**. No test scaffolds, modifications to existing tests, registration/lookup scripts, concurrency experiments or smoke verification. Essential syntax/build/public MODULE_NAME imports/architecture/document inspection are separately recorded in [completion record](../architecture/run02-verification.md); they do not prove runtime/concurrency correctness.

See [ADR-0043](../architecture/decisions/ADR-0043-runtime-model-registry.md). Source is ready for review and later explicitly authorized verification when prerequisites exist. In-memory cross-process isolation, missing decoder/extraction/kind/authority integrations, snapshot capacity and unverified concurrency assumptions remain limitations. Stop RUN-02; RUN-03 not started.

Detected malformed internal immutable index shapes, wrong scoped exact keys and duplicate/unordered inspection entries fail with RUN-121, separately from routine absence. These local guards do not audit every private index on every lookup or defend against arbitrary malicious same-process memory mutation; deleted index entries are not guaranteed detectable. Oversized inventories may reject capacity before detailed inspection.
