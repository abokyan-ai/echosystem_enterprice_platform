# RUN-05 — Execution Context

Date: 2026-10-11. Backend ownership: Python / Django / Django REST Framework. **NOT_RUN — DEFERRED / NOT VERIFIED**. New executable tests0; tests executed0. No context construction, derivation, trust-verifier, deadline, registry or Mini Sales experiment was executed.

## Repository contracts and placement

Implemented in existing `platform/runtime/runtime-core/src/runtime_core/public.py`. Runtime-core still depends only on Semantic Kernel and compiled-contracts public APIs. No new module, dependency, policy/profile/activation registration or circular import. RUN-01/02/03/04 retain their specialized contracts; RUN-03/04 do not import ExecutionContext or invoke it. No model/instance/compiler boundary imported into runtime-core.

Inspected actual SK-04 SemanticContextRef and SK-07/08 exact/versionless references, runtime target/capability tokens, RUN-01 load context/evidence and immutable graph, RUN-02 scope/snapshot/definition/authority, RUN-03 instance context/authority and RUN-04 validation context/result. No actual principal/authentication/authorization-for-execution, delegation, active deployment, cancellation or budget-accounting contract exists. Existing load/registry/instance authorizations are operation-specific and cannot authorize execution. Full general SK-11/TYPE-01/TYPE-08 remain gaps; narrow runtime diagnostics reuse current status/severity conventions rather than invent a general diagnostic engine.

Actual Python minimum3.11/local3.12.14/CI3.11,3.12,3.13. Django/djangorestframework are NOT_INSTALLED and no existing applicable authenticated runtime endpoint was found. Domain implementation requires no Django initialization. Django/DRF remains the selected mandatory HTTP framework, outside the pure context domain; no installation, endpoint, serializer, middleware, signal, ORM model or migration was added.

## Public contracts

| Contract | Responsibility |
| --- | --- |
| RuntimeInvocationId | Explicit UUID4 identifying one operation; not SemanticElementId, InstanceId, artifact or revision |
| ExecutionOperationRef | Bounded non-secret logical operation token using existing runtime token validation; not a handler, policy or capability grant |
| ExecutionCorrelationId / ExecutionCausationRef | Explicit UUID4 trace grouping versus immediate predecessor invocation; no event representation or ancestor graph |
| ExecutionConstraints / ExecutionDeadlineStatus | Finite depth/nested ceilings, explicit fixed-offset aware absolute deadline and required-enforcer IDs; explicit-time observation only |
| ExecutionModelSelection | Nonempty bounded exact reference tuple with actual immutable RUN-02 snapshot |
| ExecutionTrustSupport / Verifier / Invocation / Verification / Decision | Owner-approved actual reference classes and pure verification of existing authenticated/authorized evidence, bound to one internal invocation |
| ExecutionPrincipalRef | Structurally admitted original immutable principal reference; wrapping it does not authenticate it |
| ExecutionAuthorizationInput | Structurally admitted original immutable decision reference; wrapping it does not grant authority |
| ExecutionAuthorizationRef | Original actual VERIFIED projection from the configured owner boundary, including exact approved scope/operation/model/constraint dimensions |
| ExecutionContextCreateRequest | Immutable explicit invocation/scope/selection/correlation/constraints/reference associations; absent principal/decision allowed only to report unavailability |
| ExecutionContext | Complete immutable carried invocation associations; not a request, bearer credential, transaction or execution result |
| ExecutionContextDerivationRequest | New explicit ID, model restriction, tighter limits and fresh decision reference; no arbitrary overrides |
| ExecutionContextPolicy / Factory | Trusted construction ceilings, structural consistency, owner evidence verification, create/derive and narrow scope comparison |
| ExecutionContextDiagnostic / Failure / CreationResult | Actual runtime status/severity, RUN-401…424 constant-message diagnostics and no partial successful context |

There is no approved canonical principal category or reference implementation in this revision. Human/service/automation/AI labels cannot prove authentication. Explicit future owner approvals must reuse the real immutable existing principal/decision reference classes, with pure bounded verifier configuration. The actual source references remain preserved, including whatever audience/expiry/revocation/policy-version associations their existing owner contract already supplies; no such fields or systems are invented by RUN-05. Every principal follows the same checks. No trusted fixture/verifier or successful authorization was fabricated.

## Creation and trust boundary

Factory verifies in fixed order: actual request; explicit invocation; semantic context matches registry; correlation and immediate causation; finite distinct numeric-version-ordered exact selection; actual same scoped snapshot and original selected loaded/registered node integrity; owner resource ceilings and unsupported executor/activation requirements; principal/decision availability and owner approval; original invocation-bound verification; audience, operation, exact model coverage and constraint containment. The first expected rejection returns one typed diagnostic. Invalid typed value-object construction raises its narrow TypeError/ValueError before factory invocation. Unexpected trusted adapter programming faults propagate without fabricated success.

All selected refs require ElementVersionRef; ElementRef yields VERSION_REQUIRED even with one available version. Multiple explicit exact refs supported up to128, preserving actual numeric version order. Duplicates/reordered selection rejected rather than implicitly selecting/normalizing. No QName latest selection, transitive graph closure, registry lookup/registration or target switch. A required actual snapshot is carried, not a mutable registry or invented snapshot hash/deployment ID. Only original selected loaded nodes are re-inspected structurally; no artifact read/load/decode or semantic/instance validation rerun. Authorized application must supply the genuine RUN-02 membership snapshot. Local object/source association checks are not a cryptographic origin or active-deployment certificate.

Principal/decision inputs must first be wrapped in the exact owner-approved immutable association contracts. Raw strings/dicts/Boolean/HTTP users/session tokens cannot enter typed requests. Wrappers only establish representation safety; factory does not trust them without configured verifier. Its result must be actual ExecutionTrustVerification for the same internally created invocation and preserve original principal/decision wrappers. VERIFIED must expose all approved dimensions; missing dimension cannot be silently ignored. Request scope/target/operation must match actual approved coordinates, all selected versions must be covered and requested bounds no broader. DENIED→FAILED, UNAVAILABLE→INCOMPLETE. No policy language, evaluator, authentication provider or authorization store exists here. The owner verifier is a pure offline verification port for actual prior established evidence, not an authorization fallback.

Default factory has no trust support and cannot produce a successful protected context. Missing snapshot→RUN-419, missing principal→408, missing decision→410, absent verifier→419 according to preceding prerequisites. Principal wrappers from another owner→409; foreign decision/projection/scope/operation/models/constraints→411 or wrong audience/target405. Caller `authorized=True` is rejected by the typed reference boundary, never accepted as authority.

SUCCEEDED requires the complete context and no ERROR. FAILED means established structural/trust invariant violation. INCOMPLETE means prerequisite/evidence/enforcer unavailable. Empty diagnostics are insufficient for success; failed/incomplete results have diagnostics and context=None. No denied/partial context exposed.

## Immutable data and explicit propagation

Context, request, association, verification, constraints, selection and correlation/cause records are frozen/slotted; all inventories are tuples. Successful verification retains only admitted immutable reference source graphs and actual immutable original snapshots. Credential source fields and verification/request associations are repr-hidden, and diagnostics never echo principal/decision payloads. Actual owner approval must expose non-secret references: syntax checks cannot detect a secret that resembles a logical token. Approved references must never retain passwords, cookies or access tokens.

Reference graph admission uses exact approved frozen/slotted types, closed UUID/bool/int/None/logical-token strings, fixed-offset aware datetime and tuples; no arbitrary object inspection, bytes/dict/list/custom timezone/Enum/subclass/cycles. Default bounds1024 nodes/depth16/4096 scalar units, token length160; combined principal+decision graph checked before verifier. Future genuine reference formats must be reconciled with these constraints rather than replaced by competing identity classes.

Consumers receive ExecutionContext as an explicit argument/value. No global current context, thread-local/contextvars authority, hidden request, environment default or parent chain. A direct structurally valid Python context is not an externally verifiable credential; do not deserialize untrusted context objects as trusted. Later protected executor must recheck real authority under its established contract, regardless of historically successful context creation. No permanent authorization guarantee.

SemanticContextRef owns meaning. RuntimeModelRegistryScope binds meaning+target membership. Neither is tenant/organization/permission. No tenant or organization association added because no actual typed owner contract is available. No host/path/Django app/name inference.

## Root, derivation and narrowing

Root has explicit invocation/correlation, optionally an explicit immediate invocation cause. Its own invocation cannot cause itself. No random ID/clock generation; supplied operational UUID4 differs from compiler determinism. No root global uniqueness/invocation allocator/store claim.

Derive requires actual complete parent from the same owner trust support and restricted typed child request. Rechecks parent consistency and current existing source evidence through the owner verifier; a historical context is not a permanent credential. Child receives fresh explicit ID distinct from parent, same semantic context/target/operation/principal/correlation, immediate parent invocation as cause, exact model subset using the very same captured snapshot, tighter depth/count/deadline constraints, and explicitly supplied decision input for fresh child invocation-bound verification. No full parent/proof/context chain retained in child.

Only exact operation equality and typed exact-model subset supported; no generic permission lattice/scope solver. No new models, new versions, replacement snapshot, target, principal, tenant, organization or correlation overrides. Delegation contract absent, so principal change is unsupported and cannot be requested through derivation. Fresh authorization is not permission to bypass strict narrowing in this v0 operation. A separately authorized new root is a different operation, not an implicit child privilege expansion.

remaining_depth decreases by at least1 and parent depth0 rejects; parent maximum_nested_invocations0 rejects child. Child nested ceiling cannot rise. Deadline cannot be dropped or extended; parent without specified deadline can receive a more restrictive explicit child deadline. Parent required enforcer IDs cannot be removed by containment comparison, but any mandatory enforcer requirement is currently unavailable. No mutation of parent or consumed-budget reset. These descriptions do not track consumed sibling calls, enforce concurrency/resource accounting or schedule business work.

## Deadlines, cancellation, activation and limits

Deadline is absolute aware datetime using exact builtin timezone (UTC or fixed offset). Naive datetime, arbitrary tzinfo and relative timeout are rejected at typed construction. No clock inside factory: structural acceptance is time-independent and does not claim an expired deadline is usable. ExecutionContext.deadline_status(now) requires explicit trusted aware current time and returns NOT_SPECIFIED / BEFORE_DEADLINE / REACHED (equal deadline is REACHED). It neither executes nor cancels anything. Authorization lifetime is separately checked by the trusted existing verifier when supported. Context creation does not prove execution has begun.

Default construction ceilings128 selected refs/10000 snapshot definitions/depth64/nested4096. Constraints actual nonnegative ints bounded by2^31−1; zero is explicit prohibition of later nesting, not unlimited. Default description depth16/nested64; required capability tuple≤32 in stable order. No arbitrary budget dictionary/negative unlimited resource budgets. No actual enforcer/cancellation/active deployment/delegation contract exists. Requesting mandatory enforcer IDs→RUN-415 INCOMPLETE; requiring active deployment→RUN-424 INCOMPLETE. No Boolean active flag or registry membership turns into activation proof.

Bounded graph counts are not exact CPU/RSS guarantees for arbitrary trusted Python verifier code. Selected original-node integrity inspections have repeated bounded traversal cost. Snapshot data is shared immutable original evidence, not deep-copied. No accounting ledger, scheduler, distributed tracing/cancellation/context propagation or transaction coordinator.

## Diagnostics

| Code | Boundary |
| --- | --- |
| RUN-401/402/403 | Wrong request / invocation / semantic scope |
| RUN-404/405/406/407 | Registry semantic mismatch / target-audience mismatch / exact version required / selection membership-order mismatch |
| RUN-408/409/410/411 | Missing principal / foreign-untrusted principal / missing-unavailable authorization / wrong authority evidence or coverage |
| RUN-412/413/414/415 | Correlation / causation / deadline / unsupported mandatory enforcer |
| RUN-416/417/418/419 | Child escalation / deadline extension / unsupported principal change vocabulary / unavailable prerequisite |
| RUN-420/421/422/423/424 | Construction resource ceiling / no child permitted / trusted denial / invalid parent / missing activation evidence |

414/418 identify boundary vocabulary; invalid deadline is rejected by ExecutionConstraints constructor and principal changes are excluded by the restricted derivation request, so the current factory does not fabricate these diagnostics for unavailable operations. Diagnostic associations include actual available invocation/context/registry/exact reference/correlation/cause; no invented source location/time/secret or unrelated tenant. Derivation rejections after a typed candidate exists carry child coordinates; rejected malformed parent/constructor has only what is actually known.

## Conditional Mini Sales

Reuse actual source [Mini Sales](../../examples/authoring/mini-sales.json) and [reference definitions](../../examples/authoring/mini-sales-references.json), with genuine previously loaded/registered snapshot prerequisites from [RUN-02](runtime-model-registry.md). sales-context is actual `sem_550e8400-e29b-41d4-a716-999999999999`. Exact Customer `sem_550e8400-e29b-41d4-a716-000000000001@1.0.0`; Employee `sem_550e8400-e29b-41d4-a716-000000000002@1.0.0`. Short typ_customer_123 / sales_invocation_001 prompt labels are conceptual, not valid repository coordinates. Operational invocation/correlation require actual explicit UUID4 values from approved application identity allocation, never constructed here for a fixture.

With genuine authenticated principal+existing Customer operation decision, complete matching target/scope, exact registered Customer1.0.0 and approved bounded evidence verifier, root construction can conditionally succeed. Employee-only decision cannot cover Customer (RUN-411), missing authority410 or trust integration419 returns INCOMPLETE, snapshot scope mismatch404/405 rejects. Customer1.1.0 does not replace selected1.0.0; absent exact membership407 rejects. Child exact subset preserves correlation, causes parent, preserves principal, narrows depth/count/deadline and uses fresh child verification. Child deadline extension417 or new Employee/version416 rejects. No Customer instance created/modified/validated, no Action/Event/Policy/Workflow or activation executed.

This is documentation, not an executed example or actual fixture. Principal/decision/decoder/extractor/registry authorization and activated deployment integrations remain missing. No successful trust evidence was fabricated.

## Completion and deferred verification

Exactly [test-archive/RUN-05/RUN-05-deferred-tests.md](../../test-archive/RUN-05/RUN-05-deferred-tests.md), no README/additional archive/executable scaffolding. [ADR-0046](../architecture/decisions/ADR-0046-execution-context.md) and [completion/static record](../architecture/run05-verification.md). Only permitted static syntax/build/marker/architecture/doc checks; no context/deadline/trust experiment. Conditional implementation ready for review and separately authorized real prerequisite integration; trusted end-to-end context creation/derivation **BLOCKED / NOT VERIFIED**. Stop RUN-05, no RUN-06.
