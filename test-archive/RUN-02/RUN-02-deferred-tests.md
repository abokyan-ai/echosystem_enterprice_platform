# RUN-02 — Deferred Test Specification

Task: RUN-02 — Runtime Model Registry

Backend: Python / Django / Django REST Framework

Status: NOT_RUN — DEFERRED

New Tests Implemented: 0

Tests Executed: 0

Date: 2026-10-11

Dependencies:
- SK-01
- SK-03
- SK-04
- SK-07
- SK-08
- SK-11
- TYPE-05
- TYPE-07
- TYPE-08
- MOD-04
- CMP-07
- CMP-08
- CMP-09
- RUN-01

## Scope, prerequisites and known limitations

Sole RUN-02 archive; no README/additional archive Markdown, executable cases, test infrastructure, changed existing tests or registration/lookup/concurrency experiment. Historical executed evidence stays untouched. [Actual registry contract](../../docs/runtime/runtime-model-registry.md), [ADR-0043](../../docs/architecture/decisions/ADR-0043-runtime-model-registry.md), [static completion report](../../docs/architecture/run02-verification.md).

Future execution requires explicit later user authorization, fixed revision and actual approved prerequisites. Baseline P: genuine successful original RUN-01 result with complete verified source associations; actual approved decoder-encoded frozen definition nodes; explicit extraction support tied to its original decoder registration; scope/context/runtime target agree; registry owner declares scope/policy and an authenticated authorizer for the exact operation/selectors. No real decoder/extractor/kind/auth integration exists today; positive domain-model scenarios await those capabilities, not fabricated runtime payloads or decisions. Full SK-11/TYPE-01/SemanticInstance unavailable. Django/DRF are NOT_INSTALLED and no current authenticated HTTP workflow applies.

Unless intentionally testing a missing prerequisite, vary only the named condition in P. Construction errors are distinguished from returned result diagnostics. Empty operations require explicit verified-no-change policy and approved zero-definition extraction. V0 rejects all duplicates, including equal content/provenance. Concurrency scenarios need a controlled future authorized harness; no winner identity is assumed, and no harness/thread was created/run here. Source/document review scenarios also remain archived NOT_RUN, separately from essential checks already reported.

## A. Registry Contract

### RUN-02-T001 — Valid registry construction

- **Test ID:** RUN-02-T001
- **Scenario:** Valid registry construction.
- **Objective:** Establish the valid registry construction requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registry construction.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Declare immutable distinct allowed scope tuple, typed positive server policy and explicitly injected trusted authority/extraction catalog. Vary the named construction invariant. Specific condition: Valid registry construction.
- **Expected Result:** Valid local construction is empty and invokes no decoder, registry registration, ORM or worker; invalid configuration is rejected before use. Required invariant: Valid registry construction.
- **Expected Diagnostics:** Constructor TypeError/ValueError; no global-state success claim.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** A. Registry Contract; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T002 — Invalid configuration

- **Test ID:** RUN-02-T002
- **Scenario:** Invalid configuration.
- **Objective:** Establish the invalid configuration requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registry construction.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Declare immutable distinct allowed scope tuple, typed positive server policy and explicitly injected trusted authority/extraction catalog. Vary the named construction invariant. Specific condition: Invalid configuration.
- **Expected Result:** Valid local construction is empty and invokes no decoder, registry registration, ORM or worker; invalid configuration is rejected before use. Required invariant: Invalid configuration.
- **Expected Diagnostics:** Constructor TypeError/ValueError; no global-state success claim.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** A. Registry Contract; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T003 — Explicit scope

- **Test ID:** RUN-02-T003
- **Scenario:** Explicit scope.
- **Objective:** Establish the explicit scope requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registry construction.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Declare immutable distinct allowed scope tuple, typed positive server policy and explicitly injected trusted authority/extraction catalog. Vary the named construction invariant. Specific condition: Explicit scope.
- **Expected Result:** Valid local construction is empty and invokes no decoder, registry registration, ORM or worker; invalid configuration is rejected before use. Required invariant: Explicit scope.
- **Expected Diagnostics:** Constructor TypeError/ValueError; no global-state success claim.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** A. Registry Contract; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T004 — Pure Python independence

- **Test ID:** RUN-02-T004
- **Scenario:** Pure Python independence.
- **Objective:** Establish the pure python independence requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registry construction.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Declare immutable distinct allowed scope tuple, typed positive server policy and explicitly injected trusted authority/extraction catalog. Vary the named construction invariant. Specific condition: Pure Python independence.
- **Expected Result:** Valid local construction is empty and invokes no decoder, registry registration, ORM or worker; invalid configuration is rejected before use. Required invariant: Pure Python independence.
- **Expected Diagnostics:** Constructor TypeError/ValueError; no global-state success claim.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** A. Registry Contract; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T005 — No global singleton

- **Test ID:** RUN-02-T005
- **Scenario:** No global singleton.
- **Objective:** Establish the no global singleton requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registry construction.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Declare immutable distinct allowed scope tuple, typed positive server policy and explicitly injected trusted authority/extraction catalog. Vary the named construction invariant. Specific condition: No global singleton.
- **Expected Result:** Valid local construction is empty and invokes no decoder, registry registration, ORM or worker; invalid configuration is rejected before use. Required invariant: No global singleton.
- **Expected Diagnostics:** Constructor TypeError/ValueError; no global-state success claim.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** A. Registry Contract; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T006 — No ORM coupling

- **Test ID:** RUN-02-T006
- **Scenario:** No ORM coupling.
- **Objective:** Establish the no orm coupling requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registry construction.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Declare immutable distinct allowed scope tuple, typed positive server policy and explicitly injected trusted authority/extraction catalog. Vary the named construction invariant. Specific condition: No ORM coupling.
- **Expected Result:** Valid local construction is empty and invokes no decoder, registry registration, ORM or worker; invalid configuration is rejected before use. Required invariant: No ORM coupling.
- **Expected Diagnostics:** Constructor TypeError/ValueError; no global-state success claim.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** A. Registry Contract; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## B. RUN-01 Prerequisites

### RUN-02-T007 — Successful loaded artifact set

- **Test ID:** RUN-02-T007
- **Scenario:** Successful loaded artifact set.
- **Objective:** Establish the successful loaded artifact set requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** RUN-01 association preflight.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Supply the actual SUCCEEDED RuntimeArtifactLoadResult with the original complete set/context/target and genuine approved nodes.
- **Expected Result:** Proceed to approved extraction and distinct registry authority; no inference from a tuple alone.
- **Expected Diagnostics:** No load failure; missing support/authority reported later as RUN-107/103.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** B. RUN-01 Prerequisites; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T008 — FAILED load result

- **Test ID:** RUN-02-T008
- **Scenario:** FAILED load result.
- **Objective:** Establish the failed load result requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** RUN-01 association preflight.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use a genuine RUN-01 FAILED result without loaded_set.
- **Expected Result:** Registration FAILED and membership unchanged.
- **Expected Diagnostics:** RUN-105.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** B. RUN-01 Prerequisites; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T009 — INCOMPLETE load result

- **Test ID:** RUN-02-T009
- **Scenario:** INCOMPLETE load result.
- **Objective:** Establish the incomplete load result requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** RUN-01 association preflight.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use a genuine RUN-01 INCOMPLETE result without loaded_set.
- **Expected Result:** Registration INCOMPLETE and membership unchanged.
- **Expected Diagnostics:** RUN-105 WARNING.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** B. RUN-01 Prerequisites; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T010 — Missing load evidence

- **Test ID:** RUN-02-T010
- **Scenario:** Missing load evidence.
- **Objective:** Establish the missing load evidence requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** RUN-01 association preflight.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Attempt registration with None, a loaded tuple or LoadedRuntimeArtifactSet instead of actual RuntimeArtifactLoadResult.
- **Expected Result:** Typed construction/root API rejects input; no registration.
- **Expected Diagnostics:** TypeError or RUN-101 for invalid public root.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** B. RUN-01 Prerequisites; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T011 — Mismatched load association

- **Test ID:** RUN-02-T011
- **Scenario:** Mismatched load association.
- **Objective:** Establish the mismatched load association requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** RUN-01 association preflight.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Extractor selects an equal-looking newly copied node or a node from another original loaded artifact/result.
- **Expected Result:** Batch FAILED even if semantic key/text equals existing data; source association is not guessed.
- **Expected Diagnostics:** RUN-106.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** B. RUN-01 Prerequisites; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T012 — No arbitrary runtime definition injection

- **Test ID:** RUN-02-T012
- **Scenario:** No arbitrary runtime definition injection.
- **Objective:** Establish the no arbitrary runtime definition injection requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** RUN-01 association preflight.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Attempt request construction with user-created definitions/authorized=True fields or submit a RuntimeModelDefinition directly as the request.
- **Expected Result:** No caller definition/grant field or implicit loaded evidence; root rejected.
- **Expected Diagnostics:** TypeError or RUN-101.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** B. RUN-01 Prerequisites; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## C. Authorization

### RUN-02-T013 — Valid trusted registration authority

- **Test ID:** RUN-02-T013
- **Scenario:** Valid trusted registration authority.
- **Objective:** Establish the valid trusted registration authority requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registry authority.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Authenticated authorizer returns RuntimeModelRegistryAuthority retaining the exact internal invocation for this instance, source result, scope, REGISTER and all extracted keys.
- **Expected Result:** Only that exact operation is permitted; no inspect/activate/execute rights implied.
- **Expected Diagnostics:** No authority failure.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** C. Authorization; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T014 — Missing authority

- **Test ID:** RUN-02-T014
- **Scenario:** Missing authority.
- **Objective:** Establish the missing authority requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registry authority.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use unavailable registry authorizer with otherwise genuine supported loaded/extraction prerequisites.
- **Expected Result:** INCOMPLETE before state lock publication; no member mutation.
- **Expected Diagnostics:** RUN-103 REGISTRY_AUTHORIZATION.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** C. Authorization; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T015 — Scope mismatch

- **Test ID:** RUN-02-T015
- **Scenario:** Scope mismatch.
- **Objective:** Establish the scope mismatch requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registry authority.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Return authority for a differently scoped internal authorization request or a definition with a wrong scope, keeping other fields equal.
- **Expected Result:** Rejected without data or membership; no context rewriting.
- **Expected Diagnostics:** RUN-104 for decision mismatch; RUN-109/110 for node/context/target mismatch.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** C. Authorization; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T016 — Unauthorized definition

- **Test ID:** RUN-02-T016
- **Scenario:** Unauthorized definition.
- **Objective:** Establish the unauthorized definition requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registry authority.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Trusted authorizer rejects any extracted exact key not permitted by the authenticated registration scope.
- **Expected Result:** Whole batch rejected; cannot register only the allowed subset.
- **Expected Diagnostics:** RUN-104 or original structured authorizer rejection.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** C. Authorization; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T017 — Rejection of caller-supplied Boolean

- **Test ID:** RUN-02-T017
- **Scenario:** Rejection of caller-supplied Boolean.
- **Objective:** Establish the rejection of caller-supplied boolean requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registry authority.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Authorizer returns True/False, or request caller supplies authorized=True.
- **Expected Result:** Boolean is not a typed bound decision; unsupported request option rejected.
- **Expected Diagnostics:** RUN-104 or TypeError.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** C. Authorization; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T018 — Registration versus activation separation

- **Test ID:** RUN-02-T018
- **Scenario:** Registration versus activation separation.
- **Objective:** Establish the registration versus activation separation requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registry authority.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use a trusted authenticated authorizer that binds the exact internal registry invocation, scope, REGISTER operation, extracted exact keys and original load result; vary named permission evidence. Specific condition: Registration versus activation separation.
- **Expected Result:** Only the exact decision permits mutation; load or read permission never grants activation/execution. Required invariant: Registration versus activation separation.
- **Expected Diagnostics:** RUN-103 unavailable authority; RUN-104 Boolean/stale/broader/other-scope decision.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** C. Authorization; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## D. Registry Scope

### RUN-02-T019 — Valid SemanticContextRef

- **Test ID:** RUN-02-T019
- **Scenario:** Valid SemanticContextRef.
- **Objective:** Establish the valid semanticcontextref requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** scope/key isolation.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Create owned instances with explicitly declared context+runtime-target scopes; keep namespace/name equal and vary the named context/target coordinate. Specific condition: Valid SemanticContextRef.
- **Expected Result:** Separate configured scopes own separate exact membership; no namespace/tenant inference or cross-scope fallback. Required invariant: Valid SemanticContextRef.
- **Expected Diagnostics:** RUN-102 undeclared scope; RUN-109 context mismatch; RUN-110 target mismatch; authorized missing scoped key RUN-114 INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** D. Registry Scope; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T020 — Valid runtime target

- **Test ID:** RUN-02-T020
- **Scenario:** Valid runtime target.
- **Objective:** Establish the valid runtime target requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** scope/key isolation.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Create owned instances with explicitly declared context+runtime-target scopes; keep namespace/name equal and vary the named context/target coordinate. Specific condition: Valid runtime target.
- **Expected Result:** Separate configured scopes own separate exact membership; no namespace/tenant inference or cross-scope fallback. Required invariant: Valid runtime target.
- **Expected Diagnostics:** RUN-102 undeclared scope; RUN-109 context mismatch; RUN-110 target mismatch; authorized missing scoped key RUN-114 INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** D. Registry Scope; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T021 — Different semantic contexts

- **Test ID:** RUN-02-T021
- **Scenario:** Different semantic contexts.
- **Objective:** Establish the different semantic contexts requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** scope/key isolation.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Create owned instances with explicitly declared context+runtime-target scopes; keep namespace/name equal and vary the named context/target coordinate. Specific condition: Different semantic contexts.
- **Expected Result:** Separate configured scopes own separate exact membership; no namespace/tenant inference or cross-scope fallback. Required invariant: Different semantic contexts.
- **Expected Diagnostics:** RUN-102 undeclared scope; RUN-109 context mismatch; RUN-110 target mismatch; authorized missing scoped key RUN-114 INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** D. Registry Scope; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T022 — Different runtime targets

- **Test ID:** RUN-02-T022
- **Scenario:** Different runtime targets.
- **Objective:** Establish the different runtime targets requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** scope/key isolation.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Create owned instances with explicitly declared context+runtime-target scopes; keep namespace/name equal and vary the named context/target coordinate. Specific condition: Different runtime targets.
- **Expected Result:** Separate configured scopes own separate exact membership; no namespace/tenant inference or cross-scope fallback. Required invariant: Different runtime targets.
- **Expected Diagnostics:** RUN-102 undeclared scope; RUN-109 context mismatch; RUN-110 target mismatch; authorized missing scoped key RUN-114 INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** D. Registry Scope; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T023 — Tenant independence

- **Test ID:** RUN-02-T023
- **Scenario:** Tenant independence.
- **Objective:** Establish the tenant independence requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** scope/key isolation.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Create owned instances with explicitly declared context+runtime-target scopes; keep namespace/name equal and vary the named context/target coordinate. Specific condition: Tenant independence.
- **Expected Result:** Separate configured scopes own separate exact membership; no namespace/tenant inference or cross-scope fallback. Required invariant: Tenant independence.
- **Expected Diagnostics:** RUN-102 undeclared scope; RUN-109 context mismatch; RUN-110 target mismatch; authorized missing scoped key RUN-114 INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** D. Registry Scope; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T024 — Cross-context registration rejection

- **Test ID:** RUN-02-T024
- **Scenario:** Cross-context registration rejection.
- **Objective:** Establish the cross-context registration rejection requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** scope/key isolation.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Create owned instances with explicitly declared context+runtime-target scopes; keep namespace/name equal and vary the named context/target coordinate. Specific condition: Cross-context registration rejection.
- **Expected Result:** Separate configured scopes own separate exact membership; no namespace/tenant inference or cross-scope fallback. Required invariant: Cross-context registration rejection.
- **Expected Diagnostics:** RUN-102 undeclared scope; RUN-109 context mismatch; RUN-110 target mismatch; authorized missing scoped key RUN-114 INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** D. Registry Scope; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T025 — Cross-scope lookup isolation

- **Test ID:** RUN-02-T025
- **Scenario:** Cross-scope lookup isolation.
- **Objective:** Establish the cross-scope lookup isolation requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** scope/key isolation.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Register an exact identity in permitted scope A, then authorize the same exact key lookup in declared scope B.
- **Expected Result:** NOT_FOUND in B, no scope fallback or loading.
- **Expected Diagnostics:** RUN-114 INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** D. Registry Scope; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## E. Runtime Model Definition

### RUN-02-T026 — Typed immutable definition

- **Test ID:** RUN-02-T026
- **Scenario:** Typed immutable definition.
- **Objective:** Establish the typed immutable definition requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** approved decoded definition extraction.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use a genuine successful loaded artifact and explicit support tied to the same actual decoder approval. Select original frozen nodes under the owner-defined contract, then vary named node/kind/origin multiplicity. Specific condition: Typed immutable definition.
- **Expected Result:** Only actual approved immutable encoded nodes become entries; one/many/zero definitions follow explicit support/policy, never artifact count or canonical reconstruction. Required invariant: Typed immutable definition.
- **Expected Diagnostics:** RUN-107 missing/unsupported support; RUN-106 original association; RUN-108 invalid identity/name; RUN-113 immutable invariant failure; RUN-120 unapproved empty batch.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** E. Runtime Model Definition; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T027 — Exact semantic identity

- **Test ID:** RUN-02-T027
- **Scenario:** Exact semantic identity.
- **Objective:** Establish the exact semantic identity requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** approved decoded definition extraction.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use a genuine successful loaded artifact and explicit support tied to the same actual decoder approval. Select original frozen nodes under the owner-defined contract, then vary named node/kind/origin multiplicity. Specific condition: Exact semantic identity.
- **Expected Result:** Only actual approved immutable encoded nodes become entries; one/many/zero definitions follow explicit support/policy, never artifact count or canonical reconstruction. Required invariant: Exact semantic identity.
- **Expected Diagnostics:** RUN-107 missing/unsupported support; RUN-106 original association; RUN-108 invalid identity/name; RUN-113 immutable invariant failure; RUN-120 unapproved empty batch.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** E. Runtime Model Definition; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T028 — QualifiedName

- **Test ID:** RUN-02-T028
- **Scenario:** QualifiedName.
- **Objective:** Establish the qualifiedname requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** approved decoded definition extraction.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use a genuine successful loaded artifact and explicit support tied to the same actual decoder approval. Select original frozen nodes under the owner-defined contract, then vary named node/kind/origin multiplicity. Specific condition: QualifiedName.
- **Expected Result:** Only actual approved immutable encoded nodes become entries; one/many/zero definitions follow explicit support/policy, never artifact count or canonical reconstruction. Required invariant: QualifiedName.
- **Expected Diagnostics:** RUN-107 missing/unsupported support; RUN-106 original association; RUN-108 invalid identity/name; RUN-113 immutable invariant failure; RUN-120 unapproved empty batch.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** E. Runtime Model Definition; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T029 — Supported definition kind

- **Test ID:** RUN-02-T029
- **Scenario:** Supported definition kind.
- **Objective:** Establish the supported definition kind requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** approved decoded definition extraction.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use a genuine successful loaded artifact and explicit support tied to the same actual decoder approval. Select original frozen nodes under the owner-defined contract, then vary named node/kind/origin multiplicity. Specific condition: Supported definition kind.
- **Expected Result:** Only actual approved immutable encoded nodes become entries; one/many/zero definitions follow explicit support/policy, never artifact count or canonical reconstruction. Required invariant: Supported definition kind.
- **Expected Diagnostics:** RUN-107 missing/unsupported support; RUN-106 original association; RUN-108 invalid identity/name; RUN-113 immutable invariant failure; RUN-120 unapproved empty batch.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** E. Runtime Model Definition; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T030 — Verified artifact origin

- **Test ID:** RUN-02-T030
- **Scenario:** Verified artifact origin.
- **Objective:** Establish the verified artifact origin requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** approved decoded definition extraction.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use a genuine successful loaded artifact and explicit support tied to the same actual decoder approval. Select original frozen nodes under the owner-defined contract, then vary named node/kind/origin multiplicity. Specific condition: Verified artifact origin.
- **Expected Result:** Only actual approved immutable encoded nodes become entries; one/many/zero definitions follow explicit support/policy, never artifact count or canonical reconstruction. Required invariant: Verified artifact origin.
- **Expected Diagnostics:** RUN-107 missing/unsupported support; RUN-106 original association; RUN-108 invalid identity/name; RUN-113 immutable invariant failure; RUN-120 unapproved empty batch.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** E. Runtime Model Definition; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T031 — Multiple definitions from one artifact

- **Test ID:** RUN-02-T031
- **Scenario:** Multiple definitions from one artifact.
- **Objective:** Establish the multiple definitions from one artifact requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** approved decoded definition extraction.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Genuine decoder root includes two distinct immutable definition nodes and explicit extractor selects both original objects.
- **Expected Result:** Both exact scoped entries register atomically; artifact count does not limit definition multiplicity.
- **Expected Diagnostics:** No errors if all policies/authority/origins agree.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** E. Runtime Model Definition; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T032 — Non-registrable model-wide artifact

- **Test ID:** RUN-02-T032
- **Scenario:** Non-registrable model-wide artifact.
- **Objective:** Establish the non-registrable model-wide artifact requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** approved decoded definition extraction.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Approved model-wide artifact extractor returns () with allows_no_definitions=True; include it with real definitions or a wholly empty batch.
- **Expected Result:** Artifact contributes no fabricated entry; fully empty batch additionally requires ALLOW_VERIFIED_NO_CHANGE in client/server and exact authority.
- **Expected Diagnostics:** RUN-120 unless whole empty policy is explicitly allowed; missing extraction support RUN-107.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** E. Runtime Model Definition; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T033 — No canonical-model reconstruction

- **Test ID:** RUN-02-T033
- **Scenario:** No canonical-model reconstruction.
- **Objective:** Establish the no canonical-model reconstruction requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** approved decoded definition extraction.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use a genuine successful loaded artifact and explicit support tied to the same actual decoder approval. Select original frozen nodes under the owner-defined contract, then vary named node/kind/origin multiplicity. Specific condition: No canonical-model reconstruction.
- **Expected Result:** Only actual approved immutable encoded nodes become entries; one/many/zero definitions follow explicit support/policy, never artifact count or canonical reconstruction. Required invariant: No canonical-model reconstruction.
- **Expected Diagnostics:** RUN-107 missing/unsupported support; RUN-106 original association; RUN-108 invalid identity/name; RUN-113 immutable invariant failure; RUN-120 unapproved empty batch.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** E. Runtime Model Definition; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## F. Registry Keys

### RUN-02-T034 — Context + ElementVersionRef

- **Test ID:** RUN-02-T034
- **Scenario:** Context + ElementVersionRef.
- **Objective:** Establish the context + elementversionref requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** exact typed key.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use scope+actual ElementVersionRef, varying exact semantic version or human name while preserving original encoded identity. Specific condition: Context + ElementVersionRef.
- **Expected Result:** Exact versions/contexts/targets are distinct; QName/path/object address is never the full key. Required invariant: Context + ElementVersionRef.
- **Expected Diagnostics:** No diagnostic for distinct valid keys; invalid key TypeError/RUN-108; no implicit latest.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** F. Registry Keys; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T035 — Same ID and different versions

- **Test ID:** RUN-02-T035
- **Scenario:** Same ID and different versions.
- **Objective:** Establish the same id and different versions requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** exact typed key.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use scope+actual ElementVersionRef, varying exact semantic version or human name while preserving original encoded identity. Specific condition: Same ID and different versions.
- **Expected Result:** Exact versions/contexts/targets are distinct; QName/path/object address is never the full key. Required invariant: Same ID and different versions.
- **Expected Diagnostics:** No diagnostic for distinct valid keys; invalid key TypeError/RUN-108; no implicit latest.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** F. Registry Keys; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T036 — Same QualifiedName and different IDs

- **Test ID:** RUN-02-T036
- **Scenario:** Same QualifiedName and different IDs.
- **Objective:** Establish the same qualifiedname and different ids requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** exact typed key.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use scope+actual ElementVersionRef, varying exact semantic version or human name while preserving original encoded identity. Specific condition: Same QualifiedName and different IDs.
- **Expected Result:** Exact versions/contexts/targets are distinct; QName/path/object address is never the full key. Required invariant: Same QualifiedName and different IDs.
- **Expected Diagnostics:** No diagnostic for distinct valid keys; invalid key TypeError/RUN-108; no implicit latest.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** F. Registry Keys; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T037 — No artifact path-derived key

- **Test ID:** RUN-02-T037
- **Scenario:** No artifact path-derived key.
- **Objective:** Establish the no artifact path-derived key requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** exact typed key.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use scope+actual ElementVersionRef, varying exact semantic version or human name while preserving original encoded identity. Specific condition: No artifact path-derived key.
- **Expected Result:** Exact versions/contexts/targets are distinct; QName/path/object address is never the full key. Required invariant: No artifact path-derived key.
- **Expected Diagnostics:** No diagnostic for distinct valid keys; invalid key TypeError/RUN-108; no implicit latest.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** F. Registry Keys; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T038 — No Python-object-derived key

- **Test ID:** RUN-02-T038
- **Scenario:** No Python-object-derived key.
- **Objective:** Establish the no python-object-derived key requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** exact typed key.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use scope+actual ElementVersionRef, varying exact semantic version or human name while preserving original encoded identity. Specific condition: No Python-object-derived key.
- **Expected Result:** Exact versions/contexts/targets are distinct; QName/path/object address is never the full key. Required invariant: No Python-object-derived key.
- **Expected Diagnostics:** No diagnostic for distinct valid keys; invalid key TypeError/RUN-108; no implicit latest.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** F. Registry Keys; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T039 — No implicit latest selection

- **Test ID:** RUN-02-T039
- **Scenario:** No implicit latest selection.
- **Objective:** Establish the no implicit latest selection requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** exact typed key.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use scope+actual ElementVersionRef, varying exact semantic version or human name while preserving original encoded identity. Specific condition: No implicit latest selection.
- **Expected Result:** Exact versions/contexts/targets are distinct; QName/path/object address is never the full key. Required invariant: No implicit latest selection.
- **Expected Diagnostics:** No diagnostic for distinct valid keys; invalid key TypeError/RUN-108; no implicit latest.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** F. Registry Keys; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## G. Registration

### RUN-02-T040 — Single-definition registration

- **Test ID:** RUN-02-T040
- **Scenario:** Single-definition registration.
- **Objective:** Establish the single-definition registration requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registration preparation.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use approved extraction from the entire original loaded set, with trusted exact batch authority; vary the named kind/identity/duplicate/context/empty invariant. Specific condition: Single-definition registration.
- **Expected Result:** All individually supported nodes stage before commit; a mandatory violation rejects the entire batch. Required invariant: Single-definition registration.
- **Expected Diagnostics:** RUN-111 duplicate batch; RUN-112 existing exact key; RUN-107 kind; RUN-108 identity; RUN-109 context; RUN-120 empty policy.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** G. Registration; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T041 — Multi-definition registration

- **Test ID:** RUN-02-T041
- **Scenario:** Multi-definition registration.
- **Objective:** Establish the multi-definition registration requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registration preparation.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use approved extraction from the entire original loaded set, with trusted exact batch authority; vary the named kind/identity/duplicate/context/empty invariant. Specific condition: Multi-definition registration.
- **Expected Result:** All individually supported nodes stage before commit; a mandatory violation rejects the entire batch. Required invariant: Multi-definition registration.
- **Expected Diagnostics:** RUN-111 duplicate batch; RUN-112 existing exact key; RUN-107 kind; RUN-108 identity; RUN-109 context; RUN-120 empty policy.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** G. Registration; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T042 — Empty valid registration policy

- **Test ID:** RUN-02-T042
- **Scenario:** Empty valid registration policy.
- **Objective:** Establish the empty valid registration policy requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registration preparation.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Both request and server specify ALLOW_VERIFIED_NO_CHANGE, every artifact’s approved extractor explicitly permits zero nodes, and trusted authority binds original success/scope/zero keys.
- **Expected Result:** SUCCEEDED with registered_identities=() and unchanged local state.
- **Expected Diagnostics:** No errors; REJECT_EMPTY on either policy instead returns RUN-120 INCOMPLETE.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** G. Registration; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T043 — Duplicate within batch

- **Test ID:** RUN-02-T043
- **Scenario:** Duplicate within batch.
- **Objective:** Establish the duplicate within batch requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registration preparation.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Two original approved nodes/artifacts claim the same exact scoped ElementVersionRef, including equal nodes.
- **Expected Result:** Entire batch FAILED, stable conflict diagnostics, no field merge.
- **Expected Diagnostics:** RUN-111.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** G. Registration; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T044 — Conflict with existing definition

- **Test ID:** RUN-02-T044
- **Scenario:** Conflict with existing definition.
- **Objective:** Establish the conflict with existing definition requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registration preparation.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use approved extraction from the entire original loaded set, with trusted exact batch authority; vary the named kind/identity/duplicate/context/empty invariant. Specific condition: Conflict with existing definition.
- **Expected Result:** All individually supported nodes stage before commit; a mandatory violation rejects the entire batch. Required invariant: Conflict with existing definition.
- **Expected Diagnostics:** RUN-111 duplicate batch; RUN-112 existing exact key; RUN-107 kind; RUN-108 identity; RUN-109 context; RUN-120 empty policy.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** G. Registration; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T045 — Unsupported definition kind

- **Test ID:** RUN-02-T045
- **Scenario:** Unsupported definition kind.
- **Objective:** Establish the unsupported definition kind requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registration preparation.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use approved extraction from the entire original loaded set, with trusted exact batch authority; vary the named kind/identity/duplicate/context/empty invariant. Specific condition: Unsupported definition kind.
- **Expected Result:** All individually supported nodes stage before commit; a mandatory violation rejects the entire batch. Required invariant: Unsupported definition kind.
- **Expected Diagnostics:** RUN-111 duplicate batch; RUN-112 existing exact key; RUN-107 kind; RUN-108 identity; RUN-109 context; RUN-120 empty policy.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** G. Registration; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T046 — Invalid semantic identity

- **Test ID:** RUN-02-T046
- **Scenario:** Invalid semantic identity.
- **Objective:** Establish the invalid semantic identity requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registration preparation.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use approved extraction from the entire original loaded set, with trusted exact batch authority; vary the named kind/identity/duplicate/context/empty invariant. Specific condition: Invalid semantic identity.
- **Expected Result:** All individually supported nodes stage before commit; a mandatory violation rejects the entire batch. Required invariant: Invalid semantic identity.
- **Expected Diagnostics:** RUN-111 duplicate batch; RUN-112 existing exact key; RUN-107 kind; RUN-108 identity; RUN-109 context; RUN-120 empty policy.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** G. Registration; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T047 — Context mismatch

- **Test ID:** RUN-02-T047
- **Scenario:** Context mismatch.
- **Objective:** Establish the context mismatch requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** registration preparation.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use approved extraction from the entire original loaded set, with trusted exact batch authority; vary the named kind/identity/duplicate/context/empty invariant. Specific condition: Context mismatch.
- **Expected Result:** All individually supported nodes stage before commit; a mandatory violation rejects the entire batch. Required invariant: Context mismatch.
- **Expected Diagnostics:** RUN-111 duplicate batch; RUN-112 existing exact key; RUN-107 kind; RUN-108 identity; RUN-109 context; RUN-120 empty policy.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** G. Registration; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## H. Atomicity

### RUN-02-T048 — All entries succeed

- **Test ID:** RUN-02-T048
- **Scenario:** All entries succeed.
- **Objective:** Establish the all entries succeed requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** atomic copy-on-write update.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Prepare at least Customer/Employee or two genuine supported nodes; arrange named first/later/commit conflict while retaining an earlier immutable snapshot. Specific condition: All entries succeed.
- **Expected Result:** Whole batch publishes once or membership stays unchanged; readers see whole old/new state and old snapshots are immutable. Required invariant: All entries succeed.
- **Expected Diagnostics:** Corresponding RUN-106/107/108/109/110/111/112/118; no partial registered IDs in failed result.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** H. Atomicity; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T049 — First entry invalid

- **Test ID:** RUN-02-T049
- **Scenario:** First entry invalid.
- **Objective:** Establish the first entry invalid requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** atomic copy-on-write update.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Prepare at least Customer/Employee or two genuine supported nodes; arrange named first/later/commit conflict while retaining an earlier immutable snapshot. Specific condition: First entry invalid.
- **Expected Result:** Whole batch publishes once or membership stays unchanged; readers see whole old/new state and old snapshots are immutable. Required invariant: First entry invalid.
- **Expected Diagnostics:** Corresponding RUN-106/107/108/109/110/111/112/118; no partial registered IDs in failed result.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** H. Atomicity; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T050 — Later entry invalid

- **Test ID:** RUN-02-T050
- **Scenario:** Later entry invalid.
- **Objective:** Establish the later entry invalid requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** atomic copy-on-write update.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Prepare at least Customer/Employee or two genuine supported nodes; arrange named first/later/commit conflict while retaining an earlier immutable snapshot. Specific condition: Later entry invalid.
- **Expected Result:** Whole batch publishes once or membership stays unchanged; readers see whole old/new state and old snapshots are immutable. Required invariant: Later entry invalid.
- **Expected Diagnostics:** Corresponding RUN-106/107/108/109/110/111/112/118; no partial registered IDs in failed result.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** H. Atomicity; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T051 — Conflict on existing key

- **Test ID:** RUN-02-T051
- **Scenario:** Conflict on existing key.
- **Objective:** Establish the conflict on existing key requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** atomic copy-on-write update.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Prepare at least Customer/Employee or two genuine supported nodes; arrange named first/later/commit conflict while retaining an earlier immutable snapshot. Specific condition: Conflict on existing key.
- **Expected Result:** Whole batch publishes once or membership stays unchanged; readers see whole old/new state and old snapshots are immutable. Required invariant: Conflict on existing key.
- **Expected Diagnostics:** Corresponding RUN-106/107/108/109/110/111/112/118; no partial registered IDs in failed result.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** H. Atomicity; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T052 — No partial membership

- **Test ID:** RUN-02-T052
- **Scenario:** No partial membership.
- **Objective:** Establish the no partial membership requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** atomic copy-on-write update.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Prepare at least Customer/Employee or two genuine supported nodes; arrange named first/later/commit conflict while retaining an earlier immutable snapshot. Specific condition: No partial membership.
- **Expected Result:** Whole batch publishes once or membership stays unchanged; readers see whole old/new state and old snapshots are immutable. Required invariant: No partial membership.
- **Expected Diagnostics:** Corresponding RUN-106/107/108/109/110/111/112/118; no partial registered IDs in failed result.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** H. Atomicity; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T053 — Previous snapshot unchanged

- **Test ID:** RUN-02-T053
- **Scenario:** Previous snapshot unchanged.
- **Objective:** Establish the previous snapshot unchanged requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** atomic copy-on-write update.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Prepare at least Customer/Employee or two genuine supported nodes; arrange named first/later/commit conflict while retaining an earlier immutable snapshot. Specific condition: Previous snapshot unchanged.
- **Expected Result:** Whole batch publishes once or membership stays unchanged; readers see whole old/new state and old snapshots are immutable. Required invariant: Previous snapshot unchanged.
- **Expected Diagnostics:** Corresponding RUN-106/107/108/109/110/111/112/118; no partial registered IDs in failed result.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** H. Atomicity; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T054 — Atomic commit

- **Test ID:** RUN-02-T054
- **Scenario:** Atomic commit.
- **Objective:** Establish the atomic commit requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** atomic copy-on-write update.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Prepare at least Customer/Employee or two genuine supported nodes; arrange named first/later/commit conflict while retaining an earlier immutable snapshot. Specific condition: Atomic commit.
- **Expected Result:** Whole batch publishes once or membership stays unchanged; readers see whole old/new state and old snapshots are immutable. Required invariant: Atomic commit.
- **Expected Diagnostics:** Corresponding RUN-106/107/108/109/110/111/112/118; no partial registered IDs in failed result.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** H. Atomicity; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## I. Duplicate Semantics

### RUN-02-T055 — Exact equivalent duplicate

- **Test ID:** RUN-02-T055
- **Scenario:** Exact equivalent duplicate.
- **Objective:** Establish the exact equivalent duplicate requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** duplicate/conflict policy.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Re-submit an already registered exact scoped key with identical original node/content/provenance.
- **Expected Result:** FAILED under v0 policy; no guessed idempotent replay, old entry unchanged.
- **Expected Diagnostics:** RUN-112.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** I. Duplicate Semantics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T056 — Exact conflicting duplicate

- **Test ID:** RUN-02-T056
- **Scenario:** Exact conflicting duplicate.
- **Objective:** Establish the exact conflicting duplicate requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** duplicate/conflict policy.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Re-submit the same exact key with different typed node/content/name/provenance from a genuine second loaded source.
- **Expected Result:** FAILED; preserves the original registration and all other batch members remain uncommitted.
- **Expected Diagnostics:** RUN-112.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** I. Duplicate Semantics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T057 — Different versions

- **Test ID:** RUN-02-T057
- **Scenario:** Different versions.
- **Objective:** Establish the different versions requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** duplicate/conflict policy.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use an existing exact scoped key and re-submit the original/equivalent/conflicting node, or vary exact version/context. Specific condition: Different versions.
- **Expected Result:** V0 rejects every existing exact key including equal content; distinct exact keys coexist. No repr/hash/QName equality or last-write-wins. Required invariant: Different versions.
- **Expected Diagnostics:** RUN-112 for every existing exact scoped key; no idempotent success claim.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** I. Duplicate Semantics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T058 — Different semantic contexts

- **Test ID:** RUN-02-T058
- **Scenario:** Different semantic contexts.
- **Objective:** Establish the different semantic contexts requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** duplicate/conflict policy.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use an existing exact scoped key and re-submit the original/equivalent/conflicting node, or vary exact version/context. Specific condition: Different semantic contexts.
- **Expected Result:** V0 rejects every existing exact key including equal content; distinct exact keys coexist. No repr/hash/QName equality or last-write-wins. Required invariant: Different semantic contexts.
- **Expected Diagnostics:** RUN-112 for every existing exact scoped key; no idempotent success claim.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** I. Duplicate Semantics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T059 — No last-write-wins

- **Test ID:** RUN-02-T059
- **Scenario:** No last-write-wins.
- **Objective:** Establish the no last-write-wins requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** duplicate/conflict policy.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use an existing exact scoped key and re-submit the original/equivalent/conflicting node, or vary exact version/context. Specific condition: No last-write-wins.
- **Expected Result:** V0 rejects every existing exact key including equal content; distinct exact keys coexist. No repr/hash/QName equality or last-write-wins. Required invariant: No last-write-wins.
- **Expected Diagnostics:** RUN-112 for every existing exact scoped key; no idempotent success claim.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** I. Duplicate Semantics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T060 — No QualifiedName-only comparison

- **Test ID:** RUN-02-T060
- **Scenario:** No QualifiedName-only comparison.
- **Objective:** Establish the no qualifiedname-only comparison requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** duplicate/conflict policy.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use an existing exact scoped key and re-submit the original/equivalent/conflicting node, or vary exact version/context. Specific condition: No QualifiedName-only comparison.
- **Expected Result:** V0 rejects every existing exact key including equal content; distinct exact keys coexist. No repr/hash/QName equality or last-write-wins. Required invariant: No QualifiedName-only comparison.
- **Expected Diagnostics:** RUN-112 for every existing exact scoped key; no idempotent success claim.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** I. Duplicate Semantics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## J. Exact Lookup

### RUN-02-T061 — Existing exact key

- **Test ID:** RUN-02-T061
- **Scenario:** Existing exact key.
- **Objective:** Establish the existing exact key requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** authorized exact lookup.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Under trusted LOOKUP authority query the registered original ElementVersionRef and exact scope.
- **Expected Result:** FOUND one original immutable definition with source associations.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** J. Exact Lookup; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T062 — Missing exact key

- **Test ID:** RUN-02-T062
- **Scenario:** Missing exact key.
- **Objective:** Establish the missing exact key requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** authorized exact lookup.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Under trusted LOOKUP authority query an unregistered exact ElementVersionRef, including a missing version of a present ID.
- **Expected Result:** NOT_FOUND, no semantic invalidity/placeholder or fallback.
- **Expected Diagnostics:** RUN-114 INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** J. Exact Lookup; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T063 — Wrong context

- **Test ID:** RUN-02-T063
- **Scenario:** Wrong context.
- **Objective:** Establish the wrong context requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** authorized exact lookup.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Query actual scoped ElementVersionRef under LOOKUP authority; alter requested context/target/version or absent identity. Specific condition: Wrong context.
- **Expected Result:** FOUND preserves original immutable entry; NOT_FOUND is routine, invokes no loader/compiler/filesystem or fallback. Required invariant: Wrong context.
- **Expected Diagnostics:** RUN-114 INFO for authorized missing key; RUN-102 undeclared scope; RUN-103/104 authority; RUN-101 malformed root.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** J. Exact Lookup; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T064 — Wrong target

- **Test ID:** RUN-02-T064
- **Scenario:** Wrong target.
- **Objective:** Establish the wrong target requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** authorized exact lookup.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Query actual scoped ElementVersionRef under LOOKUP authority; alter requested context/target/version or absent identity. Specific condition: Wrong target.
- **Expected Result:** FOUND preserves original immutable entry; NOT_FOUND is routine, invokes no loader/compiler/filesystem or fallback. Required invariant: Wrong target.
- **Expected Diagnostics:** RUN-114 INFO for authorized missing key; RUN-102 undeclared scope; RUN-103/104 authority; RUN-101 malformed root.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** J. Exact Lookup; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T065 — Wrong version

- **Test ID:** RUN-02-T065
- **Scenario:** Wrong version.
- **Objective:** Establish the wrong version requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** authorized exact lookup.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Query actual scoped ElementVersionRef under LOOKUP authority; alter requested context/target/version or absent identity. Specific condition: Wrong version.
- **Expected Result:** FOUND preserves original immutable entry; NOT_FOUND is routine, invokes no loader/compiler/filesystem or fallback. Required invariant: Wrong version.
- **Expected Diagnostics:** RUN-114 INFO for authorized missing key; RUN-102 undeclared scope; RUN-103/104 authority; RUN-101 malformed root.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** J. Exact Lookup; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T066 — No automatic loading

- **Test ID:** RUN-02-T066
- **Scenario:** No automatic loading.
- **Objective:** Establish the no automatic loading requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** authorized exact lookup.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Query actual scoped ElementVersionRef under LOOKUP authority; alter requested context/target/version or absent identity. Specific condition: No automatic loading.
- **Expected Result:** FOUND preserves original immutable entry; NOT_FOUND is routine, invokes no loader/compiler/filesystem or fallback. Required invariant: No automatic loading.
- **Expected Diagnostics:** RUN-114 INFO for authorized missing key; RUN-102 undeclared scope; RUN-103/104 authority; RUN-101 malformed root.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** J. Exact Lookup; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T067 — No compiler registry fallback

- **Test ID:** RUN-02-T067
- **Scenario:** No compiler registry fallback.
- **Objective:** Establish the no compiler registry fallback requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** authorized exact lookup.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Query actual scoped ElementVersionRef under LOOKUP authority; alter requested context/target/version or absent identity. Specific condition: No compiler registry fallback.
- **Expected Result:** FOUND preserves original immutable entry; NOT_FOUND is routine, invokes no loader/compiler/filesystem or fallback. Required invariant: No compiler registry fallback.
- **Expected Diagnostics:** RUN-114 INFO for authorized missing key; RUN-102 undeclared scope; RUN-103/104 authority; RUN-101 malformed root.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** J. Exact Lookup; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## K. Identity-Only References

### RUN-02-T068 — ElementRef without version

- **Test ID:** RUN-02-T068
- **Scenario:** ElementRef without version.
- **Objective:** Establish the elementref without version requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** versionless lookup and enumeration.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Look up actual ElementRef with zero, one and several registered exact versions.
- **Expected Result:** VERSION_REQUIRED in every case; available versions need a separate authorized enumeration.
- **Expected Diagnostics:** RUN-116 INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** K. Identity-Only References; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T069 — Available exact versions

- **Test ID:** RUN-02-T069
- **Scenario:** Available exact versions.
- **Objective:** Establish the available exact versions requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** versionless lookup and enumeration.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Invoke versions(RuntimeModelVersionInspectionRequest) with its own ENUMERATE_VERSIONS grant.
- **Expected Result:** All exact versions returned numerically ordered without a selected definition.
- **Expected Diagnostics:** RUN-114 INFO if empty; RUN-117 if enumeration bound exceeded.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** K. Identity-Only References; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T070 — Version required

- **Test ID:** RUN-02-T070
- **Scenario:** Version required.
- **Objective:** Establish the version required requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** versionless lookup and enumeration.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Query actual ElementRef in a scope containing zero/one/multiple exact versions; separately request ENUMERATE_VERSIONS authority where needed. Specific condition: Version required.
- **Expected Result:** Lookup always requires an exact version, even for one candidate. Authorized enumeration exposes all numeric ordered versions without selection. Required invariant: Version required.
- **Expected Diagnostics:** RUN-116 INFO VERSION_REQUIRED; RUN-114 INFO for empty enumeration; RUN-103/104 for absent inspection permission.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** K. Identity-Only References; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T071 — No highest-version default

- **Test ID:** RUN-02-T071
- **Scenario:** No highest-version default.
- **Objective:** Establish the no highest-version default requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** versionless lookup and enumeration.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Query actual ElementRef in a scope containing zero/one/multiple exact versions; separately request ENUMERATE_VERSIONS authority where needed. Specific condition: No highest-version default.
- **Expected Result:** Lookup always requires an exact version, even for one candidate. Authorized enumeration exposes all numeric ordered versions without selection. Required invariant: No highest-version default.
- **Expected Diagnostics:** RUN-116 INFO VERSION_REQUIRED; RUN-114 INFO for empty enumeration; RUN-103/104 for absent inspection permission.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** K. Identity-Only References; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T072 — No registration-order default

- **Test ID:** RUN-02-T072
- **Scenario:** No registration-order default.
- **Objective:** Establish the no registration-order default requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** versionless lookup and enumeration.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Query actual ElementRef in a scope containing zero/one/multiple exact versions; separately request ENUMERATE_VERSIONS authority where needed. Specific condition: No registration-order default.
- **Expected Result:** Lookup always requires an exact version, even for one candidate. Authorized enumeration exposes all numeric ordered versions without selection. Required invariant: No registration-order default.
- **Expected Diagnostics:** RUN-116 INFO VERSION_REQUIRED; RUN-114 INFO for empty enumeration; RUN-103/104 for absent inspection permission.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** K. Identity-Only References; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T073 — No arbitrary version selection

- **Test ID:** RUN-02-T073
- **Scenario:** No arbitrary version selection.
- **Objective:** Establish the no arbitrary version selection requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** versionless lookup and enumeration.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Query actual ElementRef in a scope containing zero/one/multiple exact versions; separately request ENUMERATE_VERSIONS authority where needed. Specific condition: No arbitrary version selection.
- **Expected Result:** Lookup always requires an exact version, even for one candidate. Authorized enumeration exposes all numeric ordered versions without selection. Required invariant: No arbitrary version selection.
- **Expected Diagnostics:** RUN-116 INFO VERSION_REQUIRED; RUN-114 INFO for empty enumeration; RUN-103/104 for absent inspection permission.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** K. Identity-Only References; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## L. QualifiedName Inspection

### RUN-02-T074 — One exact match

- **Test ID:** RUN-02-T074
- **Scenario:** One exact match.
- **Objective:** Establish the one exact match requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** scoped name inspection.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use a Kernel QualifiedName associated with one/multiple semantic IDs or versions in the same declared scope under INSPECT_NAME authority. Specific condition: One exact match.
- **Expected Result:** One candidate FOUND; multiple AMBIGUOUS with all stable ordered candidates, no first/latest/MOD-06 resolution. Required invariant: One exact match.
- **Expected Diagnostics:** RUN-115 INFO ambiguity; RUN-114 INFO absent name; RUN-117 over inspection bound; RUN-103/104 authority.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** L. QualifiedName Inspection; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T075 — Multiple versions

- **Test ID:** RUN-02-T075
- **Scenario:** Multiple versions.
- **Objective:** Establish the multiple versions requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** scoped name inspection.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use a Kernel QualifiedName associated with one/multiple semantic IDs or versions in the same declared scope under INSPECT_NAME authority. Specific condition: Multiple versions.
- **Expected Result:** One candidate FOUND; multiple AMBIGUOUS with all stable ordered candidates, no first/latest/MOD-06 resolution. Required invariant: Multiple versions.
- **Expected Diagnostics:** RUN-115 INFO ambiguity; RUN-114 INFO absent name; RUN-117 over inspection bound; RUN-103/104 authority.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** L. QualifiedName Inspection; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T076 — Multiple semantic identities

- **Test ID:** RUN-02-T076
- **Scenario:** Multiple semantic identities.
- **Objective:** Establish the multiple semantic identities requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** scoped name inspection.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Register different exact stable IDs with the same optional QualifiedName within one scope.
- **Expected Result:** Exact keys stay distinct; name query returns all candidates as ambiguous.
- **Expected Diagnostics:** RUN-115 INFO for name inspection, no name-derived merge.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** L. QualifiedName Inspection; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T077 — Ambiguous name

- **Test ID:** RUN-02-T077
- **Scenario:** Ambiguous name.
- **Objective:** Establish the ambiguous name requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** scoped name inspection.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use a Kernel QualifiedName associated with one/multiple semantic IDs or versions in the same declared scope under INSPECT_NAME authority. Specific condition: Ambiguous name.
- **Expected Result:** One candidate FOUND; multiple AMBIGUOUS with all stable ordered candidates, no first/latest/MOD-06 resolution. Required invariant: Ambiguous name.
- **Expected Diagnostics:** RUN-115 INFO ambiguity; RUN-114 INFO absent name; RUN-117 over inspection bound; RUN-103/104 authority.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** L. QualifiedName Inspection; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T078 — Stable candidate ordering

- **Test ID:** RUN-02-T078
- **Scenario:** Stable candidate ordering.
- **Objective:** Establish the stable candidate ordering requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** scoped name inspection.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use a Kernel QualifiedName associated with one/multiple semantic IDs or versions in the same declared scope under INSPECT_NAME authority. Specific condition: Stable candidate ordering.
- **Expected Result:** One candidate FOUND; multiple AMBIGUOUS with all stable ordered candidates, no first/latest/MOD-06 resolution. Required invariant: Stable candidate ordering.
- **Expected Diagnostics:** RUN-115 INFO ambiguity; RUN-114 INFO absent name; RUN-117 over inspection bound; RUN-103/104 authority.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** L. QualifiedName Inspection; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T079 — No MOD-06 namespace resolution

- **Test ID:** RUN-02-T079
- **Scenario:** No MOD-06 namespace resolution.
- **Objective:** Establish the no mod-06 namespace resolution requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** scoped name inspection.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use a Kernel QualifiedName associated with one/multiple semantic IDs or versions in the same declared scope under INSPECT_NAME authority. Specific condition: No MOD-06 namespace resolution.
- **Expected Result:** One candidate FOUND; multiple AMBIGUOUS with all stable ordered candidates, no first/latest/MOD-06 resolution. Required invariant: No MOD-06 namespace resolution.
- **Expected Diagnostics:** RUN-115 INFO ambiguity; RUN-114 INFO absent name; RUN-117 over inspection bound; RUN-103/104 authority.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** L. QualifiedName Inspection; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## M. Registry Snapshots

### RUN-02-T080 — Empty snapshot

- **Test ID:** RUN-02-T080
- **Scenario:** Empty snapshot.
- **Objective:** Establish the empty snapshot requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** immutable snapshot.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Under SNAPSHOT authority, capture the named empty/nonempty membership before/after an atomic registration. Specific condition: Empty snapshot.
- **Expected Result:** Complete one-scope tuple with immutable original entries, no iterator/view over changing indexes; previous snapshots remain unchanged. Required invariant: Empty snapshot.
- **Expected Diagnostics:** RUN-117 unavailable over snapshot limit; RUN-103/104 authority; no error for valid empty snapshot.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** M. Registry Snapshots; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T081 — Nonempty snapshot

- **Test ID:** RUN-02-T081
- **Scenario:** Nonempty snapshot.
- **Objective:** Establish the nonempty snapshot requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** immutable snapshot.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Under SNAPSHOT authority, capture the named empty/nonempty membership before/after an atomic registration. Specific condition: Nonempty snapshot.
- **Expected Result:** Complete one-scope tuple with immutable original entries, no iterator/view over changing indexes; previous snapshots remain unchanged. Required invariant: Nonempty snapshot.
- **Expected Diagnostics:** RUN-117 unavailable over snapshot limit; RUN-103/104 authority; no error for valid empty snapshot.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** M. Registry Snapshots; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T082 — Immutable definitions

- **Test ID:** RUN-02-T082
- **Scenario:** Immutable definitions.
- **Objective:** Establish the immutable definitions requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** immutable snapshot.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Under SNAPSHOT authority, capture the named empty/nonempty membership before/after an atomic registration. Specific condition: Immutable definitions.
- **Expected Result:** Complete one-scope tuple with immutable original entries, no iterator/view over changing indexes; previous snapshots remain unchanged. Required invariant: Immutable definitions.
- **Expected Diagnostics:** RUN-117 unavailable over snapshot limit; RUN-103/104 authority; no error for valid empty snapshot.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** M. Registry Snapshots; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T083 — Immutable membership

- **Test ID:** RUN-02-T083
- **Scenario:** Immutable membership.
- **Objective:** Establish the immutable membership requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** immutable snapshot.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Under SNAPSHOT authority, capture the named empty/nonempty membership before/after an atomic registration. Specific condition: Immutable membership.
- **Expected Result:** Complete one-scope tuple with immutable original entries, no iterator/view over changing indexes; previous snapshots remain unchanged. Required invariant: Immutable membership.
- **Expected Diagnostics:** RUN-117 unavailable over snapshot limit; RUN-103/104 authority; no error for valid empty snapshot.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** M. Registry Snapshots; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T084 — Stable ordering

- **Test ID:** RUN-02-T084
- **Scenario:** Stable ordering.
- **Objective:** Establish the stable ordering requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** immutable snapshot.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Under SNAPSHOT authority, capture the named empty/nonempty membership before/after an atomic registration. Specific condition: Stable ordering.
- **Expected Result:** Complete one-scope tuple with immutable original entries, no iterator/view over changing indexes; previous snapshots remain unchanged. Required invariant: Stable ordering.
- **Expected Diagnostics:** RUN-117 unavailable over snapshot limit; RUN-103/104 authority; no error for valid empty snapshot.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** M. Registry Snapshots; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T085 — Previous snapshot unchanged after registration

- **Test ID:** RUN-02-T085
- **Scenario:** Previous snapshot unchanged after registration.
- **Objective:** Establish the previous snapshot unchanged after registration requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** immutable snapshot.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Under SNAPSHOT authority, capture the named empty/nonempty membership before/after an atomic registration. Specific condition: Previous snapshot unchanged after registration.
- **Expected Result:** Complete one-scope tuple with immutable original entries, no iterator/view over changing indexes; previous snapshots remain unchanged. Required invariant: Previous snapshot unchanged after registration.
- **Expected Diagnostics:** RUN-117 unavailable over snapshot limit; RUN-103/104 authority; no error for valid empty snapshot.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** M. Registry Snapshots; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T086 — No half-committed batch visibility

- **Test ID:** RUN-02-T086
- **Scenario:** No half-committed batch visibility.
- **Objective:** Establish the no half-committed batch visibility requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** immutable snapshot.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Under SNAPSHOT authority, capture the named empty/nonempty membership before/after an atomic registration. Specific condition: No half-committed batch visibility.
- **Expected Result:** Complete one-scope tuple with immutable original entries, no iterator/view over changing indexes; previous snapshots remain unchanged. Required invariant: No half-committed batch visibility.
- **Expected Diagnostics:** RUN-117 unavailable over snapshot limit; RUN-103/104 authority; no error for valid empty snapshot.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** M. Registry Snapshots; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## N. Concurrency

### RUN-02-T087 — Concurrent different-key registrations

- **Test ID:** RUN-02-T087
- **Scenario:** Concurrent different-key registrations.
- **Objective:** Establish the concurrent different-key registrations requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** local thread consistency.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Future authorized barrier harness prepares two genuine disjoint batches, releasing their commit contention in either order.
- **Expected Result:** Both accepted within capacity, union retained, no lost update; sorted completed membership independent of scheduling.
- **Expected Diagnostics:** No conflicts, or RUN-118 if combined latest-state capacity is exceeded.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** N. Concurrency; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T088 — Concurrent same-key equivalent registration

- **Test ID:** RUN-02-T088
- **Scenario:** Concurrent same-key equivalent registration.
- **Objective:** Establish the concurrent same-key equivalent registration requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** local thread consistency.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Future authorized threads contend using equal original node/content with one exact scoped key.
- **Expected Result:** At most one commits; remaining contenders fail without overwrite or replay success.
- **Expected Diagnostics:** RUN-112 for losers; winner identity not asserted.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** N. Concurrency; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T089 — Concurrent same-key conflicting registration

- **Test ID:** RUN-02-T089
- **Scenario:** Concurrent same-key conflicting registration.
- **Objective:** Establish the concurrent same-key conflicting registration requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** local thread consistency.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Future authorized threads contend with differing approved nodes/provenance for one exact scoped key.
- **Expected Result:** At most one commits; old/new snapshot is whole; no last-write-wins after publication.
- **Expected Diagnostics:** RUN-112 for losers; no deterministic winner claim.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** N. Concurrency; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T090 — Reader during batch commit

- **Test ID:** RUN-02-T090
- **Scenario:** Reader during batch commit.
- **Objective:** Establish the reader during batch commit requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** local thread consistency.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Future authorized observation harness reads exact/name/snapshot state before/while/after a two-entry batch commit, with callbacks outside the lock.
- **Expected Result:** Each read linearizes to whole old or whole new state; never one committed batch entry alone.
- **Expected Diagnostics:** No torn state; routine old-state absence RUN-114 may be legitimate.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** N. Concurrency; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T091 — No torn snapshot

- **Test ID:** RUN-02-T091
- **Scenario:** No torn snapshot.
- **Objective:** Establish the no torn snapshot requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** local thread consistency.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Future authorized harness coordinates concurrent legitimate register/read calls with observation barriers; do not run a harness or create threads now. Vary the named concurrent same/different-key condition. Specific condition: No torn snapshot.
- **Expected Result:** Disjoint valid batches commit without lost update; exact-key contenders cannot overwrite. Reader captures whole old/new state; winner identity is scheduling-dependent. Required invariant: No torn snapshot.
- **Expected Diagnostics:** One same-key contender SUCCEEDED and others RUN-112, including equivalent duplicate; expected input failures retain previous membership.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** N. Concurrency; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T092 — No lost update

- **Test ID:** RUN-02-T092
- **Scenario:** No lost update.
- **Objective:** Establish the no lost update requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** local thread consistency.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Future authorized harness coordinates concurrent legitimate register/read calls with observation barriers; do not run a harness or create threads now. Vary the named concurrent same/different-key condition. Specific condition: No lost update.
- **Expected Result:** Disjoint valid batches commit without lost update; exact-key contenders cannot overwrite. Reader captures whole old/new state; winner identity is scheduling-dependent. Required invariant: No lost update.
- **Expected Diagnostics:** One same-key contender SUCCEEDED and others RUN-112, including equivalent duplicate; expected input failures retain previous membership.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** N. Concurrency; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T093 — No process-global registry singleton

- **Test ID:** RUN-02-T093
- **Scenario:** No process-global registry singleton.
- **Objective:** Establish the no process-global registry singleton requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** local thread consistency.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Future authorized harness coordinates concurrent legitimate register/read calls with observation barriers; do not run a harness or create threads now. Vary the named concurrent same/different-key condition. Specific condition: No process-global registry singleton.
- **Expected Result:** Disjoint valid batches commit without lost update; exact-key contenders cannot overwrite. Reader captures whole old/new state; winner identity is scheduling-dependent. Required invariant: No process-global registry singleton.
- **Expected Diagnostics:** One same-key contender SUCCEEDED and others RUN-112, including equivalent duplicate; expected input failures retain previous membership.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** N. Concurrency; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## O. Immutability

### RUN-02-T094 — Deeply immutable definitions

- **Test ID:** RUN-02-T094
- **Scenario:** Deeply immutable definitions.
- **Objective:** Establish the deeply immutable definitions requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** deep immutability/private state.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use approved frozen slotted nodes and actual original loaded objects; inspect exposed result/snapshot tuples, then introduce named hidden mutable state through a controlled future malformed contract. Specific condition: Deeply immutable definitions.
- **Expected Result:** No caller-visible mutable index or mutable definition reference; all legitimate public values are immutable, callbacks cannot mutate membership via result objects. Required invariant: Deeply immutable definitions.
- **Expected Diagnostics:** RUN-113/RUN-020 for malformed loaded graph; extraction approval TypeError; no mutable output.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** O. Immutability; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T095 — No mutable decoded payload references

- **Test ID:** RUN-02-T095
- **Scenario:** No mutable decoded payload references.
- **Objective:** Establish the no mutable decoded payload references requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** deep immutability/private state.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use approved frozen slotted nodes and actual original loaded objects; inspect exposed result/snapshot tuples, then introduce named hidden mutable state through a controlled future malformed contract. Specific condition: No mutable decoded payload references.
- **Expected Result:** No caller-visible mutable index or mutable definition reference; all legitimate public values are immutable, callbacks cannot mutate membership via result objects. Required invariant: No mutable decoded payload references.
- **Expected Diagnostics:** RUN-113/RUN-020 for malformed loaded graph; extraction approval TypeError; no mutable output.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** O. Immutability; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T096 — Immutable registration request

- **Test ID:** RUN-02-T096
- **Scenario:** Immutable registration request.
- **Objective:** Establish the immutable registration request requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** deep immutability/private state.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use approved frozen slotted nodes and actual original loaded objects; inspect exposed result/snapshot tuples, then introduce named hidden mutable state through a controlled future malformed contract. Specific condition: Immutable registration request.
- **Expected Result:** No caller-visible mutable index or mutable definition reference; all legitimate public values are immutable, callbacks cannot mutate membership via result objects. Required invariant: Immutable registration request.
- **Expected Diagnostics:** RUN-113/RUN-020 for malformed loaded graph; extraction approval TypeError; no mutable output.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** O. Immutability; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T097 — Immutable result

- **Test ID:** RUN-02-T097
- **Scenario:** Immutable result.
- **Objective:** Establish the immutable result requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** deep immutability/private state.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use approved frozen slotted nodes and actual original loaded objects; inspect exposed result/snapshot tuples, then introduce named hidden mutable state through a controlled future malformed contract. Specific condition: Immutable result.
- **Expected Result:** No caller-visible mutable index or mutable definition reference; all legitimate public values are immutable, callbacks cannot mutate membership via result objects. Required invariant: Immutable result.
- **Expected Diagnostics:** RUN-113/RUN-020 for malformed loaded graph; extraction approval TypeError; no mutable output.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** O. Immutability; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T098 — Immutable snapshot

- **Test ID:** RUN-02-T098
- **Scenario:** Immutable snapshot.
- **Objective:** Establish the immutable snapshot requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** deep immutability/private state.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use approved frozen slotted nodes and actual original loaded objects; inspect exposed result/snapshot tuples, then introduce named hidden mutable state through a controlled future malformed contract. Specific condition: Immutable snapshot.
- **Expected Result:** No caller-visible mutable index or mutable definition reference; all legitimate public values are immutable, callbacks cannot mutate membership via result objects. Required invariant: Immutable snapshot.
- **Expected Diagnostics:** RUN-113/RUN-020 for malformed loaded graph; extraction approval TypeError; no mutable output.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** O. Immutability; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T099 — Private mutable indexes

- **Test ID:** RUN-02-T099
- **Scenario:** Private mutable indexes.
- **Objective:** Establish the private mutable indexes requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** deep immutability/private state.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use approved frozen slotted nodes and actual original loaded objects; inspect exposed result/snapshot tuples, then introduce named hidden mutable state through a controlled future malformed contract. Specific condition: Private mutable indexes.
- **Expected Result:** No caller-visible mutable index or mutable definition reference; all legitimate public values are immutable, callbacks cannot mutate membership via result objects. Required invariant: Private mutable indexes.
- **Expected Diagnostics:** RUN-113/RUN-020 for malformed loaded graph; extraction approval TypeError; no mutable output.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** O. Immutability; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T100 — No external mutation of registry contents

- **Test ID:** RUN-02-T100
- **Scenario:** No external mutation of registry contents.
- **Objective:** Establish the no external mutation of registry contents requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** deep immutability/private state.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use approved frozen slotted nodes and actual original loaded objects; inspect exposed result/snapshot tuples, then introduce named hidden mutable state through a controlled future malformed contract. Specific condition: No external mutation of registry contents.
- **Expected Result:** No caller-visible mutable index or mutable definition reference; all legitimate public values are immutable, callbacks cannot mutate membership via result objects. Required invariant: No external mutation of registry contents.
- **Expected Diagnostics:** RUN-113/RUN-020 for malformed loaded graph; extraction approval TypeError; no mutable output.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** O. Immutability; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## P. Resource Limits

### RUN-02-T101 — Maximum batch size

- **Test ID:** RUN-02-T101
- **Scenario:** Maximum batch size.
- **Objective:** Establish the maximum batch size requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** trusted capacity and enumeration limits.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** For batch/scope/total/snapshot limits L, arrange L-1, L and L+1 controlled future memberships or requested bounds, and a client limit above the server. Specific condition: Maximum batch size.
- **Expected Result:** Trusted minima and latest-state capacity enforced; excess batch commits nothing, excess snapshot returns no truncated data. Required invariant: Maximum batch size.
- **Expected Diagnostics:** RUN-118 mutation capacity; RUN-117 inspection capacity; constructor ValueError for Boolean/zero/negative limits.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** P. Resource Limits; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T102 — Maximum scope size

- **Test ID:** RUN-02-T102
- **Scenario:** Maximum scope size.
- **Objective:** Establish the maximum scope size requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** trusted capacity and enumeration limits.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** For batch/scope/total/snapshot limits L, arrange L-1, L and L+1 controlled future memberships or requested bounds, and a client limit above the server. Specific condition: Maximum scope size.
- **Expected Result:** Trusted minima and latest-state capacity enforced; excess batch commits nothing, excess snapshot returns no truncated data. Required invariant: Maximum scope size.
- **Expected Diagnostics:** RUN-118 mutation capacity; RUN-117 inspection capacity; constructor ValueError for Boolean/zero/negative limits.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** P. Resource Limits; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T103 — Maximum total definitions

- **Test ID:** RUN-02-T103
- **Scenario:** Maximum total definitions.
- **Objective:** Establish the maximum total definitions requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** trusted capacity and enumeration limits.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** For batch/scope/total/snapshot limits L, arrange L-1, L and L+1 controlled future memberships or requested bounds, and a client limit above the server. Specific condition: Maximum total definitions.
- **Expected Result:** Trusted minima and latest-state capacity enforced; excess batch commits nothing, excess snapshot returns no truncated data. Required invariant: Maximum total definitions.
- **Expected Diagnostics:** RUN-118 mutation capacity; RUN-117 inspection capacity; constructor ValueError for Boolean/zero/negative limits.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** P. Resource Limits; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T104 — Snapshot limit

- **Test ID:** RUN-02-T104
- **Scenario:** Snapshot limit.
- **Objective:** Establish the snapshot limit requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** trusted capacity and enumeration limits.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Configure membership capacity greater than snapshot limit; capture L entries then L+1 while exact lookup remains permitted.
- **Expected Result:** L snapshot complete; L+1 snapshot INCOMPLETE with no snapshot or truncation, exact lookup still works.
- **Expected Diagnostics:** RUN-117.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** P. Resource Limits; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T105 — Limit exceeded

- **Test ID:** RUN-02-T105
- **Scenario:** Limit exceeded.
- **Objective:** Establish the limit exceeded requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** trusted capacity and enumeration limits.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** For batch/scope/total/snapshot limits L, arrange L-1, L and L+1 controlled future memberships or requested bounds, and a client limit above the server. Specific condition: Limit exceeded.
- **Expected Result:** Trusted minima and latest-state capacity enforced; excess batch commits nothing, excess snapshot returns no truncated data. Required invariant: Limit exceeded.
- **Expected Diagnostics:** RUN-118 mutation capacity; RUN-117 inspection capacity; constructor ValueError for Boolean/zero/negative limits.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** P. Resource Limits; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T106 — No partial registration on limit failure

- **Test ID:** RUN-02-T106
- **Scenario:** No partial registration on limit failure.
- **Objective:** Establish the no partial registration on limit failure requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** trusted capacity and enumeration limits.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** For batch/scope/total/snapshot limits L, arrange L-1, L and L+1 controlled future memberships or requested bounds, and a client limit above the server. Specific condition: No partial registration on limit failure.
- **Expected Result:** Trusted minima and latest-state capacity enforced; excess batch commits nothing, excess snapshot returns no truncated data. Required invariant: No partial registration on limit failure.
- **Expected Diagnostics:** RUN-118 mutation capacity; RUN-117 inspection capacity; constructor ValueError for Boolean/zero/negative limits.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** P. Resource Limits; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## Q. Diagnostics

### RUN-02-T107 — Invalid request

- **Test ID:** RUN-02-T107
- **Scenario:** Invalid request.
- **Objective:** Establish the invalid request requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** existing runtime diagnostics.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Trigger the named condition through the actual public API with other prerequisites valid and inspect scope/exact ID/name/kind/operation/source associations. Specific condition: Invalid request.
- **Expected Result:** Closed runtime codes/stages/severity, stable ordered diagnostics and genuine provenance; no compiler phase/status or fabricated source location. Required invariant: Invalid request.
- **Expected Diagnostics:** Corresponding RUN-101…121; original RUN-01 causes retained when value invariants fail; NOT_FOUND/VERSION_REQUIRED/AMBIGUOUS are INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** Q. Diagnostics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T108 — Missing authorization

- **Test ID:** RUN-02-T108
- **Scenario:** Missing authorization.
- **Objective:** Establish the missing authorization requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** existing runtime diagnostics.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Trigger the named condition through the actual public API with other prerequisites valid and inspect scope/exact ID/name/kind/operation/source associations. Specific condition: Missing authorization.
- **Expected Result:** Closed runtime codes/stages/severity, stable ordered diagnostics and genuine provenance; no compiler phase/status or fabricated source location. Required invariant: Missing authorization.
- **Expected Diagnostics:** Corresponding RUN-101…121; original RUN-01 causes retained when value invariants fail; NOT_FOUND/VERSION_REQUIRED/AMBIGUOUS are INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** Q. Diagnostics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T109 — Load evidence mismatch

- **Test ID:** RUN-02-T109
- **Scenario:** Load evidence mismatch.
- **Objective:** Establish the load evidence mismatch requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** existing runtime diagnostics.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Trigger the named condition through the actual public API with other prerequisites valid and inspect scope/exact ID/name/kind/operation/source associations. Specific condition: Load evidence mismatch.
- **Expected Result:** Closed runtime codes/stages/severity, stable ordered diagnostics and genuine provenance; no compiler phase/status or fabricated source location. Required invariant: Load evidence mismatch.
- **Expected Diagnostics:** Corresponding RUN-101…121; original RUN-01 causes retained when value invariants fail; NOT_FOUND/VERSION_REQUIRED/AMBIGUOUS are INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** Q. Diagnostics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T110 — Unsupported definition kind

- **Test ID:** RUN-02-T110
- **Scenario:** Unsupported definition kind.
- **Objective:** Establish the unsupported definition kind requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** existing runtime diagnostics.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Trigger the named condition through the actual public API with other prerequisites valid and inspect scope/exact ID/name/kind/operation/source associations. Specific condition: Unsupported definition kind.
- **Expected Result:** Closed runtime codes/stages/severity, stable ordered diagnostics and genuine provenance; no compiler phase/status or fabricated source location. Required invariant: Unsupported definition kind.
- **Expected Diagnostics:** Corresponding RUN-101…121; original RUN-01 causes retained when value invariants fail; NOT_FOUND/VERSION_REQUIRED/AMBIGUOUS are INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** Q. Diagnostics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T111 — Duplicate batch identity

- **Test ID:** RUN-02-T111
- **Scenario:** Duplicate batch identity.
- **Objective:** Establish the duplicate batch identity requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** existing runtime diagnostics.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Trigger the named condition through the actual public API with other prerequisites valid and inspect scope/exact ID/name/kind/operation/source associations. Specific condition: Duplicate batch identity.
- **Expected Result:** Closed runtime codes/stages/severity, stable ordered diagnostics and genuine provenance; no compiler phase/status or fabricated source location. Required invariant: Duplicate batch identity.
- **Expected Diagnostics:** Corresponding RUN-101…121; original RUN-01 causes retained when value invariants fail; NOT_FOUND/VERSION_REQUIRED/AMBIGUOUS are INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** Q. Diagnostics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T112 — Existing definition conflict

- **Test ID:** RUN-02-T112
- **Scenario:** Existing definition conflict.
- **Objective:** Establish the existing definition conflict requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** existing runtime diagnostics.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Trigger the named condition through the actual public API with other prerequisites valid and inspect scope/exact ID/name/kind/operation/source associations. Specific condition: Existing definition conflict.
- **Expected Result:** Closed runtime codes/stages/severity, stable ordered diagnostics and genuine provenance; no compiler phase/status or fabricated source location. Required invariant: Existing definition conflict.
- **Expected Diagnostics:** Corresponding RUN-101…121; original RUN-01 causes retained when value invariants fail; NOT_FOUND/VERSION_REQUIRED/AMBIGUOUS are INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** Q. Diagnostics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T113 — Scope mismatch

- **Test ID:** RUN-02-T113
- **Scenario:** Scope mismatch.
- **Objective:** Establish the scope mismatch requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** existing runtime diagnostics.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Return authority for a differently scoped internal authorization request or a definition with a wrong scope, keeping other fields equal.
- **Expected Result:** Rejected without data or membership; no context rewriting.
- **Expected Diagnostics:** RUN-104 for decision mismatch; RUN-109/110 for node/context/target mismatch.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** Q. Diagnostics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T114 — Version required

- **Test ID:** RUN-02-T114
- **Scenario:** Version required.
- **Objective:** Establish the version required requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** existing runtime diagnostics.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Trigger the named condition through the actual public API with other prerequisites valid and inspect scope/exact ID/name/kind/operation/source associations. Specific condition: Version required.
- **Expected Result:** Closed runtime codes/stages/severity, stable ordered diagnostics and genuine provenance; no compiler phase/status or fabricated source location. Required invariant: Version required.
- **Expected Diagnostics:** Corresponding RUN-101…121; original RUN-01 causes retained when value invariants fail; NOT_FOUND/VERSION_REQUIRED/AMBIGUOUS are INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** Q. Diagnostics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T115 — Not found

- **Test ID:** RUN-02-T115
- **Scenario:** Not found.
- **Objective:** Establish the not found requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** existing runtime diagnostics.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Trigger the named condition through the actual public API with other prerequisites valid and inspect scope/exact ID/name/kind/operation/source associations. Specific condition: Not found.
- **Expected Result:** Closed runtime codes/stages/severity, stable ordered diagnostics and genuine provenance; no compiler phase/status or fabricated source location. Required invariant: Not found.
- **Expected Diagnostics:** Corresponding RUN-101…121; original RUN-01 causes retained when value invariants fail; NOT_FOUND/VERSION_REQUIRED/AMBIGUOUS are INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** Q. Diagnostics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T116 — Ambiguous name

- **Test ID:** RUN-02-T116
- **Scenario:** Ambiguous name.
- **Objective:** Establish the ambiguous name requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** existing runtime diagnostics.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Trigger the named condition through the actual public API with other prerequisites valid and inspect scope/exact ID/name/kind/operation/source associations. Specific condition: Ambiguous name.
- **Expected Result:** Closed runtime codes/stages/severity, stable ordered diagnostics and genuine provenance; no compiler phase/status or fabricated source location. Required invariant: Ambiguous name.
- **Expected Diagnostics:** Corresponding RUN-101…121; original RUN-01 causes retained when value invariants fail; NOT_FOUND/VERSION_REQUIRED/AMBIGUOUS are INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** Q. Diagnostics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T117 — Deterministic diagnostic ordering

- **Test ID:** RUN-02-T117
- **Scenario:** Deterministic diagnostic ordering.
- **Objective:** Establish the deterministic diagnostic ordering requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** existing runtime diagnostics.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use reverse source/definition order with several duplicate or existing-key conflicts at versions 1.2.0 and 1.10.0.
- **Expected Result:** Registry conflict collection is stable by semantic ID and numeric version; no timestamp/thread-order sort.
- **Expected Diagnostics:** Ordered RUN-111/112 diagnostics.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** Q. Diagnostics; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## R. Provenance

### RUN-02-T118 — Exact source artifact identity

- **Test ID:** RUN-02-T118
- **Scenario:** Exact source artifact identity.
- **Objective:** Establish the exact source artifact identity requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** source provenance.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Inspect a found entry’s loaded_artifact/source_evidence against the actual original successful source.
- **Expected Result:** Exact existing key/manifest/binding/logical location/verified digest association preserved; no path-derived semantic key.
- **Expected Diagnostics:** No diagnostic for valid provenance.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** R. Provenance; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T119 — Manifest association

- **Test ID:** RUN-02-T119
- **Scenario:** Manifest association.
- **Objective:** Establish the manifest association requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** source provenance.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use an actual original load result and artifact with exact descriptor/manifest/source evidence and select encoded nodes under approved extraction; vary named origin association. Specific condition: Manifest association.
- **Expected Result:** Entries retain exact loaded node/artifact/load associations without invented origin IDs or duplicated read-buffer storage. Required invariant: Manifest association.
- **Expected Diagnostics:** RUN-106 on copied/substituted node or original association; no fabricated SourceLocation or raw-byte endpoint.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** R. Provenance; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T120 — Loaded artifact association

- **Test ID:** RUN-02-T120
- **Scenario:** Loaded artifact association.
- **Objective:** Establish the loaded artifact association requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** source provenance.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use an actual original load result and artifact with exact descriptor/manifest/source evidence and select encoded nodes under approved extraction; vary named origin association. Specific condition: Loaded artifact association.
- **Expected Result:** Entries retain exact loaded node/artifact/load associations without invented origin IDs or duplicated read-buffer storage. Required invariant: Loaded artifact association.
- **Expected Diagnostics:** RUN-106 on copied/substituted node or original association; no fabricated SourceLocation or raw-byte endpoint.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** R. Provenance; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T121 — Multiple semantic origins

- **Test ID:** RUN-02-T121
- **Scenario:** Multiple semantic origins.
- **Objective:** Establish the multiple semantic origins requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** source provenance.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use an actual original load result and artifact with exact descriptor/manifest/source evidence and select encoded nodes under approved extraction; vary named origin association. Specific condition: Multiple semantic origins.
- **Expected Result:** Entries retain exact loaded node/artifact/load associations without invented origin IDs or duplicated read-buffer storage. Required invariant: Multiple semantic origins.
- **Expected Diagnostics:** RUN-106 on copied/substituted node or original association; no fabricated SourceLocation or raw-byte endpoint.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** R. Provenance; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T122 — No fabricated source location

- **Test ID:** RUN-02-T122
- **Scenario:** No fabricated source location.
- **Objective:** Establish the no fabricated source location requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** source provenance.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use an actual original load result and artifact with exact descriptor/manifest/source evidence and select encoded nodes under approved extraction; vary named origin association. Specific condition: No fabricated source location.
- **Expected Result:** Entries retain exact loaded node/artifact/load associations without invented origin IDs or duplicated read-buffer storage. Required invariant: No fabricated source location.
- **Expected Diagnostics:** RUN-106 on copied/substituted node or original association; no fabricated SourceLocation or raw-byte endpoint.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** R. Provenance; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T123 — No raw artifact byte storage

- **Test ID:** RUN-02-T123
- **Scenario:** No raw artifact byte storage.
- **Objective:** Establish the no raw artifact byte storage requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** source provenance.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use an actual original load result and artifact with exact descriptor/manifest/source evidence and select encoded nodes under approved extraction; vary named origin association. Specific condition: No raw artifact byte storage.
- **Expected Result:** Entries retain exact loaded node/artifact/load associations without invented origin IDs or duplicated read-buffer storage. Required invariant: No raw artifact byte storage.
- **Expected Diagnostics:** RUN-106 on copied/substituted node or original association; no fabricated SourceLocation or raw-byte endpoint.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** R. Provenance; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## S. Django / DRF

### RUN-02-T124 — Pure Python registry domain

- **Test ID:** RUN-02-T124
- **Scenario:** Pure Python registry domain.
- **Objective:** Establish the pure python registry domain requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** Django/DRF boundary.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Inspect current pure registry and documented adapters, then future actual authenticated HTTP workflow when installed and explicitly requested. Specific condition: Pure Python registry domain.
- **Expected Result:** No framework initialization/ORM/migration/unrequested endpoint; future adapter resolves trusted authority/scope and bounded safe response. Required invariant: Pure Python registry domain.
- **Expected Diagnostics:** No HTTP success claim while integration is absent; RUN-103 missing authority; architecture diagnostics for forbidden imports.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** S. Django / DRF; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T125 — No database models

- **Test ID:** RUN-02-T125
- **Scenario:** No database models.
- **Objective:** Establish the no database models requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** Django/DRF boundary.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Inspect current pure registry and documented adapters, then future actual authenticated HTTP workflow when installed and explicitly requested. Specific condition: No database models.
- **Expected Result:** No framework initialization/ORM/migration/unrequested endpoint; future adapter resolves trusted authority/scope and bounded safe response. Required invariant: No database models.
- **Expected Diagnostics:** No HTTP success claim while integration is absent; RUN-103 missing authority; architecture diagnostics for forbidden imports.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** S. Django / DRF; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T126 — No migrations

- **Test ID:** RUN-02-T126
- **Scenario:** No migrations.
- **Objective:** Establish the no migrations requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** Django/DRF boundary.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Inspect current pure registry and documented adapters, then future actual authenticated HTTP workflow when installed and explicitly requested. Specific condition: No migrations.
- **Expected Result:** No framework initialization/ORM/migration/unrequested endpoint; future adapter resolves trusted authority/scope and bounded safe response. Required invariant: No migrations.
- **Expected Diagnostics:** No HTTP success claim while integration is absent; RUN-103 missing authority; architecture diagnostics for forbidden imports.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** S. Django / DRF; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T127 — Existing authorized API integration

- **Test ID:** RUN-02-T127
- **Scenario:** Existing authorized API integration.
- **Objective:** Establish the existing authorized api integration requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** Django/DRF boundary.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Inspect actual current adapters/apps: there is no authenticated Django/DRF runtime-management workflow; future execution requires genuine installed integration.
- **Expected Result:** No speculative API or ModelSerializer created now; internal registry ports remain fail-closed and ready for future composition.
- **Expected Diagnostics:** RUN-103 unavailable authority; no fake HTTP success.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** S. Django / DRF; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T128 — No unrestricted register endpoint

- **Test ID:** RUN-02-T128
- **Scenario:** No unrestricted register endpoint.
- **Objective:** Establish the no unrestricted register endpoint requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** Django/DRF boundary.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Inspect current pure registry and documented adapters, then future actual authenticated HTTP workflow when installed and explicitly requested. Specific condition: No unrestricted register endpoint.
- **Expected Result:** No framework initialization/ORM/migration/unrequested endpoint; future adapter resolves trusted authority/scope and bounded safe response. Required invariant: No unrestricted register endpoint.
- **Expected Diagnostics:** No HTTP success claim while integration is absent; RUN-103 missing authority; architecture diagnostics for forbidden imports.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** S. Django / DRF; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T129 — No cross-context metadata disclosure

- **Test ID:** RUN-02-T129
- **Scenario:** No cross-context metadata disclosure.
- **Objective:** Establish the no cross-context metadata disclosure requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** Django/DRF boundary.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Inspect current pure registry and documented adapters, then future actual authenticated HTTP workflow when installed and explicitly requested. Specific condition: No cross-context metadata disclosure.
- **Expected Result:** No framework initialization/ORM/migration/unrequested endpoint; future adapter resolves trusted authority/scope and bounded safe response. Required invariant: No cross-context metadata disclosure.
- **Expected Diagnostics:** No HTTP success claim while integration is absent; RUN-103 missing authority; architecture diagnostics for forbidden imports.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** S. Django / DRF; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T130 — Existing permission enforcement

- **Test ID:** RUN-02-T130
- **Scenario:** Existing permission enforcement.
- **Objective:** Establish the existing permission enforcement requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** Django/DRF boundary.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Inspect current pure registry and documented adapters, then future actual authenticated HTTP workflow when installed and explicitly requested. Specific condition: Existing permission enforcement.
- **Expected Result:** No framework initialization/ORM/migration/unrequested endpoint; future adapter resolves trusted authority/scope and bounded safe response. Required invariant: Existing permission enforcement.
- **Expected Diagnostics:** No HTTP success claim while integration is absent; RUN-103 missing authority; architecture diagnostics for forbidden imports.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** S. Django / DRF; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## T. Mini Sales

### RUN-02-T131 — Customer@1.0.0 registration

- **Test ID:** RUN-02-T131
- **Scenario:** Customer@1.0.0 registration.
- **Objective:** Establish the customer@1.0.0 registration requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** conditional Mini Sales.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use actual Customer sem_...000001 and Employee sem_...000002 @1.0.0 in context sem_...999999999999, only once genuine owned decoder/extractor/source authority exist. Vary the named scenario. Specific condition: Customer@1.0.0 registration.
- **Expected Result:** Preserve actual encoded definitions/exact versions/self-reference; complete atomic registration, missing key routine, no active/business instance or execution. Required invariant: Customer@1.0.0 registration.
- **Expected Diagnostics:** RUN-114 @2.0.0 absent; RUN-116 ElementRef; RUN-112 duplicate; corresponding preflight failure leaves batch unchanged; no fabricated success fixture.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** T. Mini Sales; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T132 — Employee@1.0.0 registration

- **Test ID:** RUN-02-T132
- **Scenario:** Employee@1.0.0 registration.
- **Objective:** Establish the employee@1.0.0 registration requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** conditional Mini Sales.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use actual Customer sem_...000001 and Employee sem_...000002 @1.0.0 in context sem_...999999999999, only once genuine owned decoder/extractor/source authority exist. Vary the named scenario. Specific condition: Employee@1.0.0 registration.
- **Expected Result:** Preserve actual encoded definitions/exact versions/self-reference; complete atomic registration, missing key routine, no active/business instance or execution. Required invariant: Employee@1.0.0 registration.
- **Expected Diagnostics:** RUN-114 @2.0.0 absent; RUN-116 ElementRef; RUN-112 duplicate; corresponding preflight failure leaves batch unchanged; no fabricated success fixture.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** T. Mini Sales; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T133 — Exact Customer lookup

- **Test ID:** RUN-02-T133
- **Scenario:** Exact Customer lookup.
- **Objective:** Establish the exact customer lookup requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** conditional Mini Sales.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use actual Customer sem_...000001 and Employee sem_...000002 @1.0.0 in context sem_...999999999999, only once genuine owned decoder/extractor/source authority exist. Vary the named scenario. Specific condition: Exact Customer lookup.
- **Expected Result:** Preserve actual encoded definitions/exact versions/self-reference; complete atomic registration, missing key routine, no active/business instance or execution. Required invariant: Exact Customer lookup.
- **Expected Diagnostics:** RUN-114 @2.0.0 absent; RUN-116 ElementRef; RUN-112 duplicate; corresponding preflight failure leaves batch unchanged; no fabricated success fixture.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** T. Mini Sales; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T134 — Missing Customer@2.0.0

- **Test ID:** RUN-02-T134
- **Scenario:** Missing Customer@2.0.0.
- **Objective:** Establish the missing customer@2.0.0 requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** conditional Mini Sales.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Query actual Customer ElementVersionRef at 2.0.0 while only genuine @1.0.0/@1.1.0 are registered.
- **Expected Result:** NOT_FOUND, no substituted version.
- **Expected Diagnostics:** RUN-114 INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** T. Mini Sales; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T135 — Customer ElementRef version-required response

- **Test ID:** RUN-02-T135
- **Scenario:** Customer ElementRef version-required response.
- **Objective:** Establish the customer elementref version-required response requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** conditional Mini Sales.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use actual Customer ElementRef sem_550e8400-e29b-41d4-a716-000000000001 under LOOKUP permission.
- **Expected Result:** VERSION_REQUIRED even with Customer@1.0.0 alone; no highest-version choice.
- **Expected Diagnostics:** RUN-116 INFO.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** T. Mini Sales; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T136 — Customer@1.0.0 and Customer@1.1.0 coexistence

- **Test ID:** RUN-02-T136
- **Scenario:** Customer@1.0.0 and Customer@1.1.0 coexistence.
- **Objective:** Establish the customer@1.0.0 and customer@1.1.0 coexistence requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** conditional Mini Sales.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Once actually encoded and independently verified, register both versions with their exact identities and allowed source scope.
- **Expected Result:** Both keys persist; name inspection reports ordered ambiguous candidates without activation.
- **Expected Diagnostics:** RUN-115 INFO for shared-name inspection.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** T. Mini Sales; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T137 — Employee self-reference preservation

- **Test ID:** RUN-02-T137
- **Scenario:** Employee self-reference preservation.
- **Objective:** Establish the employee self-reference preservation requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** conditional Mini Sales.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Genuine approved Employee node contains immutable versionless ElementRef to its own semantic ID.
- **Expected Result:** Reference stays unchanged; no recursive instantiation, version selection, graph binding or cycle rejection.
- **Expected Diagnostics:** No reference-resolution diagnostic.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** T. Mini Sales; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T138 — Customer duplicate conflict

- **Test ID:** RUN-02-T138
- **Scenario:** Customer duplicate conflict.
- **Objective:** Establish the customer duplicate conflict requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** conditional Mini Sales.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use actual Customer sem_...000001 and Employee sem_...000002 @1.0.0 in context sem_...999999999999, only once genuine owned decoder/extractor/source authority exist. Vary the named scenario. Specific condition: Customer duplicate conflict.
- **Expected Result:** Preserve actual encoded definitions/exact versions/self-reference; complete atomic registration, missing key routine, no active/business instance or execution. Required invariant: Customer duplicate conflict.
- **Expected Diagnostics:** RUN-114 @2.0.0 absent; RUN-116 ElementRef; RUN-112 duplicate; corresponding preflight failure leaves batch unchanged; no fabricated success fixture.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** T. Mini Sales; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T139 — Atomic Customer/Employee batch failure

- **Test ID:** RUN-02-T139
- **Scenario:** Atomic Customer/Employee batch failure.
- **Objective:** Establish the atomic customer/employee batch failure requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** conditional Mini Sales.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use actual Customer sem_...000001 and Employee sem_...000002 @1.0.0 in context sem_...999999999999, only once genuine owned decoder/extractor/source authority exist. Vary the named scenario. Specific condition: Atomic Customer/Employee batch failure.
- **Expected Result:** Preserve actual encoded definitions/exact versions/self-reference; complete atomic registration, missing key routine, no active/business instance or execution. Required invariant: Atomic Customer/Employee batch failure.
- **Expected Diagnostics:** RUN-114 @2.0.0 absent; RUN-116 ElementRef; RUN-112 duplicate; corresponding preflight failure leaves batch unchanged; no fabricated success fixture.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** T. Mini Sales; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T140 — No activation after registration

- **Test ID:** RUN-02-T140
- **Scenario:** No activation after registration.
- **Objective:** Establish the no activation after registration requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** conditional Mini Sales.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Use actual Customer sem_...000001 and Employee sem_...000002 @1.0.0 in context sem_...999999999999, only once genuine owned decoder/extractor/source authority exist. Vary the named scenario. Specific condition: No activation after registration.
- **Expected Result:** Preserve actual encoded definitions/exact versions/self-reference; complete atomic registration, missing key routine, no active/business instance or execution. Required invariant: No activation after registration.
- **Expected Diagnostics:** RUN-114 @2.0.0 absent; RUN-116 ElementRef; RUN-112 duplicate; corresponding preflight failure leaves batch unchanged; no fabricated success fixture.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** T. Mini Sales; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## U. Architectural Boundaries

### RUN-02-T141 — No compiler invocation

- **Test ID:** RUN-02-T141
- **Scenario:** No compiler invocation.
- **Objective:** Establish the no compiler invocation requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Review new production imports and call paths for the named excluded capability; future observations require explicit execution permission. Specific condition: No compiler invocation.
- **Expected Result:** Registry only stages/indexes approved loaded definitions and reads local immutable membership; no named excluded behavior or RUN-03. Required invariant: No compiler invocation.
- **Expected Diagnostics:** No invented fallback; ARCH dependency diagnostics for prohibited edges; ordinary invalid/unsupported input RUN-101/107.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** U. Architectural Boundaries; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T142 — No artifact decoding

- **Test ID:** RUN-02-T142
- **Scenario:** No artifact decoding.
- **Objective:** Establish the no artifact decoding requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Review new production imports and call paths for the named excluded capability; future observations require explicit execution permission. Specific condition: No artifact decoding.
- **Expected Result:** Registry only stages/indexes approved loaded definitions and reads local immutable membership; no named excluded behavior or RUN-03. Required invariant: No artifact decoding.
- **Expected Diagnostics:** No invented fallback; ARCH dependency diagnostics for prohibited edges; ordinary invalid/unsupported input RUN-101/107.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** U. Architectural Boundaries; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T143 — No filesystem reading

- **Test ID:** RUN-02-T143
- **Scenario:** No filesystem reading.
- **Objective:** Establish the no filesystem reading requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Review new production imports and call paths for the named excluded capability; future observations require explicit execution permission. Specific condition: No filesystem reading.
- **Expected Result:** Registry only stages/indexes approved loaded definitions and reads local immutable membership; no named excluded behavior or RUN-03. Required invariant: No filesystem reading.
- **Expected Diagnostics:** No invented fallback; ARCH dependency diagnostics for prohibited edges; ordinary invalid/unsupported input RUN-101/107.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** U. Architectural Boundaries; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T144 — No implicit latest selection

- **Test ID:** RUN-02-T144
- **Scenario:** No implicit latest selection.
- **Objective:** Establish the no implicit latest selection requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Review new production imports and call paths for the named excluded capability; future observations require explicit execution permission. Specific condition: No implicit latest selection.
- **Expected Result:** Registry only stages/indexes approved loaded definitions and reads local immutable membership; no named excluded behavior or RUN-03. Required invariant: No implicit latest selection.
- **Expected Diagnostics:** No invented fallback; ARCH dependency diagnostics for prohibited edges; ordinary invalid/unsupported input RUN-101/107.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** U. Architectural Boundaries; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T145 — No distributed registry

- **Test ID:** RUN-02-T145
- **Scenario:** No distributed registry.
- **Objective:** Establish the no distributed registry requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Review new production imports and call paths for the named excluded capability; future observations require explicit execution permission. Specific condition: No distributed registry.
- **Expected Result:** Registry only stages/indexes approved loaded definitions and reads local immutable membership; no named excluded behavior or RUN-03. Required invariant: No distributed registry.
- **Expected Diagnostics:** No invented fallback; ARCH dependency diagnostics for prohibited edges; ordinary invalid/unsupported input RUN-101/107.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** U. Architectural Boundaries; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T146 — No database persistence

- **Test ID:** RUN-02-T146
- **Scenario:** No database persistence.
- **Objective:** Establish the no database persistence requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Review new production imports and call paths for the named excluded capability; future observations require explicit execution permission. Specific condition: No database persistence.
- **Expected Result:** Registry only stages/indexes approved loaded definitions and reads local immutable membership; no named excluded behavior or RUN-03. Required invariant: No database persistence.
- **Expected Diagnostics:** No invented fallback; ARCH dependency diagnostics for prohibited edges; ordinary invalid/unsupported input RUN-101/107.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** U. Architectural Boundaries; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T147 — No activation

- **Test ID:** RUN-02-T147
- **Scenario:** No activation.
- **Objective:** Establish the no activation requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Review new production imports and call paths for the named excluded capability; future observations require explicit execution permission. Specific condition: No activation.
- **Expected Result:** Registry only stages/indexes approved loaded definitions and reads local immutable membership; no named excluded behavior or RUN-03. Required invariant: No activation.
- **Expected Diagnostics:** No invented fallback; ARCH dependency diagnostics for prohibited edges; ordinary invalid/unsupported input RUN-101/107.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** U. Architectural Boundaries; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T148 — No business instance creation

- **Test ID:** RUN-02-T148
- **Scenario:** No business instance creation.
- **Objective:** Establish the no business instance creation requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Review new production imports and call paths for the named excluded capability; future observations require explicit execution permission. Specific condition: No business instance creation.
- **Expected Result:** Registry only stages/indexes approved loaded definitions and reads local immutable membership; no named excluded behavior or RUN-03. Required invariant: No business instance creation.
- **Expected Diagnostics:** No invented fallback; ARCH dependency diagnostics for prohibited edges; ordinary invalid/unsupported input RUN-101/107.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** U. Architectural Boundaries; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T149 — No action dispatch

- **Test ID:** RUN-02-T149
- **Scenario:** No action dispatch.
- **Objective:** Establish the no action dispatch requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Review new production imports and call paths for the named excluded capability; future observations require explicit execution permission. Specific condition: No action dispatch.
- **Expected Result:** Registry only stages/indexes approved loaded definitions and reads local immutable membership; no named excluded behavior or RUN-03. Required invariant: No action dispatch.
- **Expected Diagnostics:** No invented fallback; ARCH dependency diagnostics for prohibited edges; ordinary invalid/unsupported input RUN-101/107.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** U. Architectural Boundaries; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T150 — No event emission

- **Test ID:** RUN-02-T150
- **Scenario:** No event emission.
- **Objective:** Establish the no event emission requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Review new production imports and call paths for the named excluded capability; future observations require explicit execution permission. Specific condition: No event emission.
- **Expected Result:** Registry only stages/indexes approved loaded definitions and reads local immutable membership; no named excluded behavior or RUN-03. Required invariant: No event emission.
- **Expected Diagnostics:** No invented fallback; ARCH dependency diagnostics for prohibited edges; ordinary invalid/unsupported input RUN-101/107.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** U. Architectural Boundaries; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T151 — No runtime execution

- **Test ID:** RUN-02-T151
- **Scenario:** No runtime execution.
- **Objective:** Establish the no runtime execution requirement while preserving exact identity, authority, atomicity and inactive definitions.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual baseline P, except the deliberately absent named prerequisite; genuine owned decoder/extractor/authority for successful membership assertions.
- **Input / Setup:** Review new production imports and call paths for the named excluded capability; future observations require explicit execution permission. Specific condition: No runtime execution.
- **Expected Result:** Registry only stages/indexes approved loaded definitions and reads local immutable membership; no named excluded behavior or RUN-03. Required invariant: No runtime execution.
- **Expected Diagnostics:** No invented fallback; ARCH dependency diagnostics for prohibited edges; ordinary invalid/unsupported input RUN-101/107.
- **Boundary / Edge Cases:** Zero/one/multiple definitions and exact versions; first/later invalid entry; repeated same key versus distinct version/context/target; limit-1/limit/limit+1 where applicable. Concurrent winner identity is not assumed.
- **Integration Dependencies:** U. Architectural Boundaries; actual RUN-01 original loaded evidence, Kernel typed identity/name/version, trusted registry authorizer/extractor, private local state and public immutable result contracts.
- **Acceptance Criteria:** Exact expected status/error and stable associations/order, complete committed keys or unchanged state, no partial result, implicit selection, authority expansion or activation; capture genuine future evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## V. Additional implementation-specific boundaries

### RUN-02-T152 — Actual numeric version ordering

- **Test ID:** RUN-02-T152
- **Scenario:** Actual numeric version ordering.
- **Objective:** Verify actual numeric version ordering against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Use the same encoded identity with 1.2.0, 1.10.0 and 2.0.0, inserted in reverse order.
- **Expected Result:** Snapshot and version enumeration order by numeric components, not lexical text.
- **Expected Diagnostics:** No ordering error.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T153 — Separate target membership

- **Test ID:** RUN-02-T153
- **Scenario:** Separate target membership.
- **Objective:** Verify separate target membership against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Use two explicitly declared scopes with same context and different runtime targets; load/source/node match each target.
- **Expected Result:** Independent keys and snapshots, no target inference.
- **Expected Diagnostics:** RUN-110 mismatched source; authorized other target absence RUN-114.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T154 — Registry instance-bound authority

- **Test ID:** RUN-02-T154
- **Scenario:** Registry instance-bound authority.
- **Objective:** Verify registry instance-bound authority against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Authorizer reuses a decision from another registry with equal-looking scopes.
- **Expected Result:** Rejected before mutation/read.
- **Expected Diagnostics:** RUN-104.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T155 — Stale invocation authority

- **Test ID:** RUN-02-T155
- **Scenario:** Stale invocation authority.
- **Objective:** Verify stale invocation authority against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Return a previously valid decision for the same scope/selector/source but another authorization invocation.
- **Expected Result:** Exact current invocation association required.
- **Expected Diagnostics:** RUN-104.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T156 — Register grant cannot inspect

- **Test ID:** RUN-02-T156
- **Scenario:** Register grant cannot inspect.
- **Objective:** Verify register grant cannot inspect against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Return a REGISTER-bound authority when LOOKUP/SNAPSHOT/INSPECT_NAME is requested.
- **Expected Result:** No member data returned under mutation-only authority.
- **Expected Diagnostics:** RUN-104.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T157 — Lookup grant cannot enumerate

- **Test ID:** RUN-02-T157
- **Scenario:** Lookup grant cannot enumerate.
- **Objective:** Verify lookup grant cannot enumerate against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Authorize versionless lookup but deny ENUMERATE_VERSIONS.
- **Expected Result:** Version-required response does not disclose available versions; enumeration separately unavailable/denied.
- **Expected Diagnostics:** RUN-116 then RUN-103/104 as appropriate.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T158 — Name grant cannot snapshot

- **Test ID:** RUN-02-T158
- **Scenario:** Name grant cannot snapshot.
- **Objective:** Verify name grant cannot snapshot against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Grant one QName inspection and return that decision for whole-scope snapshot.
- **Expected Result:** Snapshot reveals no unrelated schema.
- **Expected Diagnostics:** RUN-104.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T159 — Mutation response excludes unrelated snapshot

- **Test ID:** RUN-02-T159
- **Scenario:** Mutation response excludes unrelated snapshot.
- **Objective:** Verify mutation response excludes unrelated snapshot against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Register a submitted new batch alongside existing unrelated definitions under mutation-only permission.
- **Expected Result:** Result contains only submitted committed IDs and original load association; no whole-scope post-snapshot.
- **Expected Diagnostics:** No unrelated metadata disclosure.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T160 — Empty request/server policy conjunction

- **Test ID:** RUN-02-T160
- **Scenario:** Empty request/server policy conjunction.
- **Objective:** Verify empty request/server policy conjunction against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Set ALLOW_VERIFIED_NO_CHANGE on only the request or only the server with valid zero-node support.
- **Expected Result:** Effective stricter REJECT_EMPTY prevents successful no-change registration.
- **Expected Diagnostics:** RUN-120 INCOMPLETE.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T161 — Unknown extractor capability

- **Test ID:** RUN-02-T161
- **Scenario:** Unknown extractor capability.
- **Objective:** Verify unknown extractor capability against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Use actual successful loaded artifact whose decoder approval has no extraction support.
- **Expected Result:** INCOMPLETE, no entry guessed from origins or arbitrary attributes.
- **Expected Diagnostics:** RUN-107.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T162 — Equal-looking decoder approval

- **Test ID:** RUN-02-T162
- **Scenario:** Equal-looking decoder approval.
- **Objective:** Verify equal-looking decoder approval against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Supply extraction support associated with an equal-looking different decoder registration object.
- **Expected Result:** Explicit original decoder approval association missing.
- **Expected Diagnostics:** RUN-107.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T163 — Duplicate extraction dispatch

- **Test ID:** RUN-02-T163
- **Scenario:** Duplicate extraction dispatch.
- **Objective:** Verify duplicate extraction dispatch against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Configure two supports with the same decoder dispatch key.
- **Expected Result:** Catalog rejects ambiguity before use.
- **Expected Diagnostics:** ValueError.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T164 — Undeclared definition class

- **Test ID:** RUN-02-T164
- **Scenario:** Undeclared definition class.
- **Objective:** Verify undeclared definition class against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Attempt support for a node class absent from decoder representation_types.
- **Expected Result:** Approval rejected; registry cannot widen decoded graph types.
- **Expected Diagnostics:** TypeError.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T165 — Missing explicit node fields

- **Test ID:** RUN-02-T165
- **Scenario:** Missing explicit node fields.
- **Objective:** Verify missing explicit node fields against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Support a frozen node lacking identity/context/target/name/kind field declaration.
- **Expected Result:** Approval rejected instead of attribute guessing.
- **Expected Diagnostics:** TypeError.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T166 — Mutable extractor options

- **Test ID:** RUN-02-T166
- **Scenario:** Mutable extractor options.
- **Objective:** Verify mutable extractor options against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Register a frozen extractor holding list/dict/service/callback configuration.
- **Expected Result:** Existing immutable graph guard rejects unsafe config; no dynamically selected extractor.
- **Expected Diagnostics:** RUN-020 or approval TypeError.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T167 — Extractor invalid result root

- **Test ID:** RUN-02-T167
- **Scenario:** Extractor invalid result root.
- **Objective:** Verify extractor invalid result root against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Approved extractor returns dict/None rather than RuntimeModelDefinitionExtractionResult.
- **Expected Result:** Batch FAILED, old membership untouched.
- **Expected Diagnostics:** RUN-119.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T168 — Extractor late non-success

- **Test ID:** RUN-02-T168
- **Scenario:** Extractor late non-success.
- **Objective:** Verify extractor late non-success against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** First artifact selects valid nodes; later artifact returns FAILED/INCOMPLETE with structured diagnostics.
- **Expected Result:** No node from the batch commits; diagnostics preserve operation/source and original non-success status.
- **Expected Diagnostics:** RUN-119 plus actual extractor diagnostics.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T169 — Extractor over-budget collection

- **Test ID:** RUN-02-T169
- **Scenario:** Extractor over-budget collection.
- **Objective:** Verify extractor over-budget collection against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Return remaining+1 original definition nodes; do not silently stop at remaining.
- **Expected Result:** Whole registration FAILED without truncation.
- **Expected Diagnostics:** RUN-118.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T170 — Zero remaining budget metadata artifact

- **Test ID:** RUN-02-T170
- **Scenario:** Zero remaining budget metadata artifact.
- **Objective:** Verify zero remaining budget metadata artifact against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** After exact batch limit, process an explicitly no-definition metadata artifact returning ().
- **Expected Result:** All mandatory artifacts processed; allowed zero contribution does not cause false overflow.
- **Expected Diagnostics:** No error if all other policy/authority gates pass.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T171 — Zero remaining budget later definition

- **Test ID:** RUN-02-T171
- **Scenario:** Zero remaining budget later definition.
- **Objective:** Verify zero remaining budget later definition against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** After exact batch limit, later approved artifact exposes one mandatory node.
- **Expected Result:** Whole batch FAILED; none silently omitted.
- **Expected Diagnostics:** RUN-118.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T172 — Copied decoded node rejected

- **Test ID:** RUN-02-T172
- **Scenario:** Copied decoded node rejected.
- **Objective:** Verify copied decoded node rejected against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Extractor constructs an equal immutable copy of an encoded node.
- **Expected Result:** Equality is not original source membership; batch rejected.
- **Expected Diagnostics:** RUN-106.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T173 — Node from another artifact rejected

- **Test ID:** RUN-02-T173
- **Scenario:** Node from another artifact rejected.
- **Objective:** Verify node from another artifact rejected against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Extractor selects a legitimate frozen node from another loaded representation.
- **Expected Result:** Actual membership in the selected original artifact required.
- **Expected Diagnostics:** RUN-106.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T174 — Encoded origin outside explicit metadata

- **Test ID:** RUN-02-T174
- **Scenario:** Encoded origin outside explicit metadata.
- **Objective:** Verify encoded origin outside explicit metadata against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** A non-model-wide artifact exposes a typed exact node identity absent from its declared semantic_origins.
- **Expected Result:** Association mismatch rejected without inventing origins.
- **Expected Diagnostics:** RUN-106.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T175 — Encoded model-wide nodes

- **Test ID:** RUN-02-T175
- **Scenario:** Encoded model-wide nodes.
- **Objective:** Verify encoded model-wide nodes against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** A genuine approved model-wide format explicitly includes typed exact definition nodes in its loaded graph.
- **Expected Result:** Approved extraction preserves encoded keys while descriptor origin tuple stays empty/model_wide; no fabricated per-definition descriptor origins.
- **Expected Diagnostics:** No error when all actual contracts agree.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T176 — Unnamed definition

- **Test ID:** RUN-02-T176
- **Scenario:** Unnamed definition.
- **Objective:** Verify unnamed definition against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Genuine node qualified_name=None under supported kind and scope.
- **Expected Result:** Exact key registration/lookup works; no invented QName or name-index entry.
- **Expected Diagnostics:** Name query routine NOT_FOUND if no other matching entry.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T177 — QName case semantics

- **Test ID:** RUN-02-T177
- **Scenario:** QName case semantics.
- **Objective:** Verify qname case semantics against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Use actual Kernel normalized Namespace and case-preserving local names.
- **Expected Result:** Inspection matches exact existing Kernel QName semantics, no locale/namespace resolution.
- **Expected Diagnostics:** RUN-114 for distinct exact human name.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T178 — Invalid exact identity leaves

- **Test ID:** RUN-02-T178
- **Scenario:** Invalid exact identity leaves.
- **Objective:** Verify invalid exact identity leaves against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Use raw ID/version text or wrong typed version inside a controlled malformed node.
- **Expected Result:** Registry rejects before commit; no identity/version generation.
- **Expected Diagnostics:** RUN-108.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T179 — Scope count bound

- **Test ID:** RUN-02-T179
- **Scenario:** Scope count bound.
- **Objective:** Verify scope count bound against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Construct with zero, 1, 128 and 129 distinct actual declared scopes.
- **Expected Result:** Only 1..128 allowed; duplicate scopes rejected.
- **Expected Diagnostics:** ValueError.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T180 — Boolean policy limit rejected

- **Test ID:** RUN-02-T180
- **Scenario:** Boolean policy limit rejected.
- **Objective:** Verify boolean policy limit rejected against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Use True/False for each four positive integer policy settings.
- **Expected Result:** Reject instead of accepting bool as int.
- **Expected Diagnostics:** ValueError.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T181 — Zero/negative policy limit rejected

- **Test ID:** RUN-02-T181
- **Scenario:** Zero/negative policy limit rejected.
- **Objective:** Verify zero/negative policy limit rejected against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Use 0/-1 for each capacity setting.
- **Expected Result:** Configuration/request construction rejects before registration.
- **Expected Diagnostics:** ValueError.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T182 — Client capacity cannot raise server

- **Test ID:** RUN-02-T182
- **Scenario:** Client capacity cannot raise server.
- **Objective:** Verify client capacity cannot raise server against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Request greater batch/scope/total ceilings than owner policy.
- **Expected Result:** Server minima enforced against current membership at commit.
- **Expected Diagnostics:** RUN-118 for excess.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T183 — Latest-state scope capacity

- **Test ID:** RUN-02-T183
- **Scenario:** Latest-state scope capacity.
- **Objective:** Verify latest-state scope capacity against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Two concurrent disjoint batches each fit old scope count but jointly exceed scope maximum.
- **Expected Result:** One may commit; later capacity decision sees current count and rejects wholly.
- **Expected Diagnostics:** RUN-118 for capacity loser, no scheduling winner assertion.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T184 — Latest-state total capacity

- **Test ID:** RUN-02-T184
- **Scenario:** Latest-state total capacity.
- **Objective:** Verify latest-state total capacity against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Two distinct allowed scopes concurrently add batches whose union exceeds total capacity.
- **Expected Result:** Global per-instance total checked under lock, no lost/over-capacity update.
- **Expected Diagnostics:** RUN-118.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T185 — Name candidate overflow

- **Test ID:** RUN-02-T185
- **Scenario:** Name candidate overflow.
- **Objective:** Verify name candidate overflow against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Allowed name maps to more entries than maximum_snapshot_entries.
- **Expected Result:** INCOMPLETE without any truncated candidates or first-version selection.
- **Expected Diagnostics:** RUN-117.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T186 — Version enumeration overflow

- **Test ID:** RUN-02-T186
- **Scenario:** Version enumeration overflow.
- **Objective:** Verify version enumeration overflow against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Registered versions for one scoped ID exceed maximum_snapshot_entries.
- **Expected Result:** INCOMPLETE with no partial references; exact lookup unaffected.
- **Expected Diagnostics:** RUN-117.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T187 — Unexpected construction/allocation fault

- **Test ID:** RUN-02-T187
- **Scenario:** Unexpected construction/allocation fault.
- **Objective:** Verify unexpected construction/allocation fault against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** During future controlled verification cause an unexpected state/result construction exception before publication.
- **Expected Result:** Exception propagates and old state remains; no hidden commit or fake success.
- **Expected Diagnostics:** Original programming/allocation exception.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T188 — Callbacks outside private lock

- **Test ID:** RUN-02-T188
- **Scenario:** Callbacks outside private lock.
- **Objective:** Verify callbacks outside private lock against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Use approved authorizer/extractor observation hooks in future controlled harness.
- **Expected Result:** No callback executes while state lock held; no arbitrary decoder/authority execution inside commit.
- **Expected Diagnostics:** No callback-induced torn state/deadlock claim without actual evidence.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T189 — Private immutable indexes

- **Test ID:** RUN-02-T189
- **Scenario:** Private immutable indexes.
- **Objective:** Verify private immutable indexes against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Inspect completed snapshots/result contract and production state construction.
- **Expected Result:** No private MappingProxy index, mutable source dict or lock is exposed through public membership methods.
- **Expected Diagnostics:** No mutation surface in result.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T190 — No default runtime registry

- **Test ID:** RUN-02-T190
- **Scenario:** No default runtime registry.
- **Objective:** Verify no default runtime registry against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Import public MODULE_NAME and inspect hosting/bootstrap composition source only.
- **Expected Result:** No registry singleton/instance, worker or environment-dependent configuration created by import.
- **Expected Diagnostics:** No automatic registration/activation.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T191 — Independent local instances

- **Test ID:** RUN-02-T191
- **Scenario:** Independent local instances.
- **Objective:** Verify independent local instances against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Create two future owned instances with equal scopes; register only in one.
- **Expected Result:** Second instance remains empty, no global/process-shared membership.
- **Expected Diagnostics:** Authorized lookup on second RUN-114.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T192 — Cross-worker isolation documented

- **Test ID:** RUN-02-T192
- **Scenario:** Cross-worker isolation documented.
- **Objective:** Verify cross-worker isolation documented against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Review lifecycle and future controlled process replacement scenario once approved.
- **Expected Result:** No in-memory state survival or cross-process synchronization promised.
- **Expected Diagnostics:** No distributed consistency claim.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T193 — Extractor diagnostic association mismatch

- **Test ID:** RUN-02-T193
- **Scenario:** Extractor diagnostic association mismatch.
- **Objective:** Verify extractor diagnostic association mismatch against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Return a typed extractor diagnostic for another context/target/artifact/manifest/registry scope/operation.
- **Expected Result:** Reject incorrect association rather than falsely relabel it.
- **Expected Diagnostics:** RUN-119.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T194 — Missing extractor diagnostic associations

- **Test ID:** RUN-02-T194
- **Scenario:** Missing extractor diagnostic associations.
- **Objective:** Verify missing extractor diagnostic associations against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Expected extractor failure omits optional invocation associations.
- **Expected Result:** Actual scope/source/REGISTER operation added while original code/severity/stage/order retained.
- **Expected Diagnostics:** Actual structured diagnostic and RUN-119 summary.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T195 — Shared runtime diagnostic compatibility

- **Test ID:** RUN-02-T195
- **Scenario:** Shared runtime diagnostic compatibility.
- **Objective:** Verify shared runtime diagnostic compatibility against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Inspect existing loader diagnostic construction/comparison after trailing registry fields and Kernel name leaves are added.
- **Expected Result:** Old positional arguments/statuses remain; new associations included in semantic comparison; no generic diagnostic replacement.
- **Expected Diagnostics:** No compatibility claim based on execution; future tests deferred.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T196 — No byte buffer duplication

- **Test ID:** RUN-02-T196
- **Scenario:** No byte buffer duplication.
- **Objective:** Verify no byte buffer duplication against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Inspect entry provenance against original actual loaded object graph.
- **Expected Result:** No RetrievedArtifact.content field/copy or new artifact store; expressly approved binary node fields remain internal and unfabricated.
- **Expected Diagnostics:** No default raw-byte disclosure.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T197 — No registration experiments

- **Test ID:** RUN-02-T197
- **Scenario:** No registration experiments.
- **Objective:** Verify no registration experiments against actual RUN-02 production contracts.
- **Component:** Registry preparation/authority/extraction/commit/lookup/snapshot or shared runtime diagnostic/state boundary named by the scenario.
- **Prerequisites:** Fixed revision and explicit later execution permission; genuine P for behavioral assertions. Concurrency/observation harness only when future verification is authorized, never production placeholder fixtures.
- **Input / Setup:** Review current work and CI command evidence.
- **Expected Result:** Only syntax/build/public markers/architecture/document checks; no custom registry/lookup/thread smoke scenarios.
- **Expected Diagnostics:** 0 deferred tests executed, NOT_RUN — DEFERRED.
- **Boundary / Edge Cases:** Absent/exact/mismatched associations; one/multiple artifacts or nodes; zero/limit/one-over-limit budgets; before/during/after atomic commit without a scheduling winner claim.
- **Integration Dependencies:** Original RUN-01 loaded result and approved graph/extraction association, Kernel exact identity/version/name, explicit local scopes/policy/authority and immutable membership results.
- **Acceptance Criteria:** Match documented state/output/diagnostics exactly; no partial mutation or disclosure, no fabricated provenance or execution; retain actual future evidence without relabeling deferred cases as passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-02-T198 — Detectable internal registry corruption

- **Test ID:** RUN-02-T198
- **Scenario:** Detectable malformed immutable indices and mismatched scoped entries.
- **Objective:** Distinguish internal integrity failure from ordinary absence without exposing partial inventory.
- **Component:** LocalRuntimeModelRegistry private state shape, exact lookup, name/version inspection and scoped snapshot guards.
- **Prerequisites:** Explicit later execution permission, fixed revision, genuine approved RUN-01 evidence/extraction/authority and a controlled corruption harness. No harness is created or executed now.
- **Input / Setup:** In a future isolated harness replace the private state/index shape, assign a present exact key to None or another keyed entry, replace an inventory tuple with None/list, or supply mismatched scope/name/identity, duplicate or unordered references/definitions.
- **Expected Result:** Authorized affected reads return FAILED with no definitions/versions/snapshot; malformed state blocks commit without publishing new membership. Valid empty immutable indices still produce routine absence/empty snapshot. Prior untouched snapshots stay unchanged.
- **Expected Diagnostics:** ERROR RUN-121 REGISTRY_INTEGRITY_FAILURE, never routine RUN-114 for a detected malformed entry or silent filtering/truncation. Existing scope/operation associations retained where available.
- **Boundary / Edge Cases:** Empty/one/multiple entries, exact present-None versus missing key, wrong scope/name/version, duplicate/order anomalies, malformed state before commit. Counts above inspection budget may reject RUN-117 before traversing oversized inventories. No full private-memory audit or detection guarantee for deleted index entries/arbitrary malicious same-process mutation.
- **Integration Dependencies:** Existing runtime diagnostic/status model, Kernel coordinates, typed frozen registry entries and private immutable copy-on-write state.
- **Acceptance Criteria:** Detect documented integrity violations before returning their contents or publishing malformed new state; preserve ordinary absence semantics and explicit resource limits. Record real future evidence without claiming comprehensive tamper resistance.
- **Execution Status:** NOT_RUN — DEFERRED

## Documentation summary

Total documented scenarios: **198**. New executable tests: **0**. Tests executed: **0**. Status: **DEFERRED / NOT VERIFIED**. Every scenario remains **NOT_RUN — DEFERRED**. Stop RUN-02; RUN-03 not started.
