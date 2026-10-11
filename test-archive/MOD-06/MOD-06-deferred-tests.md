# MOD-06 — Deferred Test Specification

Task: MOD-06 — Namespace Resolver

Backend: Python / Django / Django REST Framework

Status: NOT_RUN — DEFERRED

New Tests Implemented: 0

Tests Executed: 0

Dependencies:
- SK-02
- SK-03
- SK-04
- SK-07
- SK-08
- SK-11
- TYPE-07
- MOD-01
- MOD-03
- MOD-05

Documentation date: 2026-10-10 (Asia/Riyadh).

## Future execution prerequisites and boundaries

Execution requires a separate explicit authorization, fixed source revision, Python 3.11+ and registered public source paths/setup, approved actual symbols/bindings/authoring/location snapshots and recorded results. No automated fixture/test code or runner is provided. These entries do not certify correctness. Full SK-11/TYPE-01/TYPE-08/full SK-09 remain unavailable; exact field references still face the TYPE-05/MOD-05 representation gap. Future/conditional DRF cases require a real approved endpoint first.

Boundary misuse of frozen typed contracts raises existing TypeError/value-object errors; ordinary supported resolution failures use MOD-NAMESPACE diagnostics, and environment domain conflicts return NamespaceEnvironmentFactory failures or direct NamespaceEnvironmentError. Aliases are a resolver-only explicit capability, not new MOD-01 source syntax. All alias targets are concrete namespaces; recursive alias-chain/cycle semantics are unsupported, not silently invented. Resolution/capture/binding/location examples were not executed.

Documented scenarios: **146**. All statuses below are NOT_RUN — DEFERRED.

## MOD-06-T001 — Valid environment

- **Test ID:** MOD-06-T001
- **Scenario / category:** A. Resolution environment — Valid environment
- **Objective:** Verify valid environment under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionEnvironment / NamespaceEnvironmentFactory
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Supply explicit context/current namespace and typed symbols/aliases.
- **Expected Result:** Complete frozen environment with owned indexes.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Local-only and visible-only snapshots. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04/07/08, MOD-01 source paths.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T002 — Missing context

- **Test ID:** MOD-06-T002
- **Scenario / category:** A. Resolution environment — Missing context
- **Objective:** Verify missing context under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionEnvironment / NamespaceEnvironmentFactory
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Construct environment with context=None.
- **Expected Result:** Reject developer contract misuse before lookup.
- **Expected Diagnostics:** TypeError.
- **Boundary / Edge Cases:** No inferred context from symbols. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04/07/08, MOD-01 source paths.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T003 — Invalid namespace

- **Test ID:** MOD-06-T003
- **Scenario / category:** A. Resolution environment — Invalid namespace
- **Objective:** Verify invalid namespace under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionEnvironment / NamespaceEnvironmentFactory
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Supply raw text or malformed Namespace through existing parser.
- **Expected Result:** Existing contract rejects rather than parsing filesystem hints.
- **Expected Diagnostics:** TypeError or existing SEM-NS error.
- **Boundary / Edge Cases:** Empty and wildcard namespace. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04/07/08, MOD-01 source paths.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T004 — Empty symbol collection

- **Test ID:** MOD-06-T004
- **Scenario / category:** A. Resolution environment — Empty symbol collection
- **Objective:** Verify empty symbol collection under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionEnvironment / NamespaceEnvironmentFactory
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Valid environment with no symbols and known current namespace.
- **Expected Result:** Environment valid; resolution reports missing target.
- **Expected Diagnostics:** MOD-NAMESPACE-003 on request.
- **Boundary / Edge Cases:** Empty tuples/lists. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04/07/08, MOD-01 source paths.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T005 — Immutable environment

- **Test ID:** MOD-06-T005
- **Scenario / category:** A. Resolution environment — Immutable environment
- **Objective:** Verify immutable environment under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionEnvironment / NamespaceEnvironmentFactory
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Construct with caller-owned symbol/alias/search lists then modify original lists.
- **Expected Result:** Owned sorted tuples/indexes remain unchanged.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Nested symbol/alias writes rejected by frozen values. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04/07/08, MOD-01 source paths.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T006 — Scope isolation

- **Test ID:** MOD-06-T006
- **Scenario / category:** A. Resolution environment — Scope isolation
- **Objective:** Verify scope isolation under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionEnvironment / NamespaceEnvironmentFactory
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Foreign-context symbol is supplied to a single-context environment.
- **Expected Result:** Atomic environment failure, no cross-context opt-in inferred.
- **Expected Diagnostics:** MOD-NAMESPACE-007.
- **Boundary / Edge Cases:** Same QName and ID spelling in foreign context. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04/07/08, MOD-01 source paths.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T007 — Equal-standing sources

- **Test ID:** MOD-06-T007
- **Scenario / category:** A. Resolution environment — Equal-standing sources
- **Objective:** Verify equal-standing sources under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionEnvironment / NamespaceEnvironmentFactory
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Local and visible contributions have no conflicts.
- **Expected Result:** Both contribute without hidden local/registry precedence.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Identical semantic metadata from both sources. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04/07/08, MOD-01 source paths.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T008 — Equivalent input permutations

- **Test ID:** MOD-06-T008
- **Scenario / category:** A. Resolution environment — Equivalent input permutations
- **Objective:** Verify equivalent input permutations under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionEnvironment / NamespaceEnvironmentFactory
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Reorder symbols/aliases/search namespaces with equivalent meaning.
- **Expected Result:** Same normalized environment outcome and resolution meaning.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Numeric version sorting. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04/07/08, MOD-01 source paths.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T009 — Private indexes

- **Test ID:** MOD-06-T009
- **Scenario / category:** A. Resolution environment — Private indexes
- **Objective:** Verify private indexes under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionEnvironment / NamespaceEnvironmentFactory
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Attempt to mutate retained name/identity/alias index membership.
- **Expected Result:** Read-only map/tuple values prevent mutation.
- **Expected Diagnostics:** TypeError developer misuse.
- **Boundary / Edge Cases:** No public mutable dictionary. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04/07/08, MOD-01 source paths.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T010 — Unsupported collections

- **Test ID:** MOD-06-T010
- **Scenario / category:** A. Resolution environment — Unsupported collections
- **Objective:** Verify unsupported collections under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionEnvironment / NamespaceEnvironmentFactory
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Supply set/generator/dictionary as public ordered symbol/alias collections.
- **Expected Result:** Boundary rejects untyped/unordered collection.
- **Expected Diagnostics:** TypeError.
- **Boundary / Edge Cases:** Empty set versus tuple. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04/07/08, MOD-01 source paths.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T011 — Context mismatch request

- **Test ID:** MOD-06-T011
- **Scenario / category:** A. Resolution environment — Context mismatch request
- **Objective:** Verify context mismatch request under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionEnvironment / NamespaceEnvironmentFactory
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Request explicit context differs from environment.context.
- **Expected Result:** Failure without searching either context.
- **Expected Diagnostics:** MOD-NAMESPACE-007.
- **Boundary / Edge Cases:** Empty environments. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04/07/08, MOD-01 source paths.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T012 — No global state

- **Test ID:** MOD-06-T012
- **Scenario / category:** A. Resolution environment — No global state
- **Objective:** Verify no global state under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionEnvironment / NamespaceEnvironmentFactory
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Build two independent environments with overlapping names.
- **Expected Result:** Resolving one does not change the other.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Concurrent request environments. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04/07/08, MOD-01 source paths.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T013 — Local type resolution

- **Test ID:** MOD-06-T013
- **Scenario / category:** B. Local names — Local type resolution
- **Objective:** Verify local type resolution under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local_authoring_symbols
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Customer visible in sales current namespace.
- **Expected Result:** Unique stable Customer identity returned.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Only one version versus multiple same-ID versions. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-02/03/04, MOD-05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T014 — Unknown local name

- **Test ID:** MOD-06-T014
- **Scenario / category:** B. Local names — Unknown local name
- **Objective:** Verify unknown local name under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local_authoring_symbols
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** No visible symbol at searchable QName for Employee.
- **Expected Result:** Failure with explicit request context/expression.
- **Expected Diagnostics:** MOD-NAMESPACE-003.
- **Boundary / Edge Cases:** Empty environment. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-02/03/04, MOD-05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T015 — Duplicate equal local symbols

- **Test ID:** MOD-06-T015
- **Scenario / category:** B. Local names — Duplicate equal local symbols
- **Objective:** Verify duplicate equal local symbols under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local_authoring_symbols
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Same exact name/kind/ID/version appears twice.
- **Expected Result:** Idempotent semantic contribution; no false identity ambiguity.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Different declaration paths may remain diagnostic candidates. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-02/03/04, MOD-05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T016 — Conflicting local coordinate

- **Test ID:** MOD-06-T016
- **Scenario / category:** B. Local names — Conflicting local coordinate
- **Objective:** Verify conflicting local coordinate under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local_authoring_symbols
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Same exact ID/version has different QName or kind.
- **Expected Result:** Environment rejects complete snapshot.
- **Expected Diagnostics:** MOD-NAMESPACE-010.
- **Boundary / Edge Cases:** Equal exact metadata does not fail. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-02/03/04, MOD-05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T017 — Local forward reference

- **Test ID:** MOD-06-T017
- **Scenario / category:** B. Local names — Local forward reference
- **Objective:** Verify local forward reference under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local_authoring_symbols
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Predeclare Invoice and Customer before resolving Invoice.customer.
- **Expected Result:** Customer resolved without registration/construction order dependency.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Referenced symbol appears later in document. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-02/03/04, MOD-05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T018 — Local self-reference

- **Test ID:** MOD-06-T018
- **Scenario / category:** B. Local names — Local self-reference
- **Objective:** Verify local self-reference under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local_authoring_symbols
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Predeclare Employee then resolve Employee.manager name.
- **Expected Result:** Employee stable identity resolved.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Single declaration. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-02/03/04, MOD-05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T019 — Local context mismatch

- **Test ID:** MOD-06-T019
- **Scenario / category:** B. Local names — Local context mismatch
- **Objective:** Verify local context mismatch under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local_authoring_symbols
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Local symbol uses foreign context.
- **Expected Result:** Environment failure with candidate/path if supplied.
- **Expected Diagnostics:** MOD-NAMESPACE-007.
- **Boundary / Edge Cases:** Foreign context sharing namespace. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-02/03/04, MOD-05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T020 — Explicit namespace composition

- **Test ID:** MOD-06-T020
- **Scenario / category:** B. Local names — Explicit namespace composition
- **Objective:** Verify explicit namespace composition under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local_authoring_symbols
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Local name Customer with Namespace.parse sales.
- **Expected Result:** Existing QualifiedName.create semantics used.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Namespace case canonicalization; local name case preserved. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-02/03/04, MOD-05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T021 — No namespace derivation

- **Test ID:** MOD-06-T021
- **Scenario / category:** B. Local names — No namespace derivation
- **Objective:** Verify no namespace derivation under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local_authoring_symbols
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Change source filename while supplying identical environment.
- **Expected Result:** Same semantic target.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** No path-based lookup. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-02/03/04, MOD-05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T022 — No implicit extra namespace search

- **Test ID:** MOD-06-T022
- **Scenario / category:** B. Local names — No implicit extra namespace search
- **Objective:** Verify no implicit extra namespace search under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local_authoring_symbols
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** crm.Customer visible but only sales searchable.
- **Expected Result:** Local Customer remains missing or only sales match.
- **Expected Diagnostics:** MOD-NAMESPACE-003 if only crm exists.
- **Boundary / Edge Cases:** Explicit qualified crm.Customer may still resolve. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-02/03/04, MOD-05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T023 — Explicit extra namespace search

- **Test ID:** MOD-06-T023
- **Scenario / category:** B. Local names — Explicit extra namespace search
- **Objective:** Verify explicit extra namespace search under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local_authoring_symbols
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Include crm in search_namespaces alongside sales.
- **Expected Result:** Both namespaces contribute candidates without priority.
- **Expected Diagnostics:** None if one identity; ambiguity if distinct.
- **Boundary / Edge Cases:** Current namespace always included. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-02/03/04, MOD-05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T024 — Local declaration projection

- **Test ID:** MOD-06-T024
- **Scenario / category:** B. Local names — Local declaration projection
- **Objective:** Verify local declaration projection under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local_authoring_symbols
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Project supported MOD-01 document using local_authoring_symbols.
- **Expected Result:** Existing declared exact coordinates and declaration paths captured.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Empty document. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-02/03/04, MOD-05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T025 — Unsupported projection root/schema

- **Test ID:** MOD-06-T025
- **Scenario / category:** B. Local names — Unsupported projection root/schema
- **Objective:** Verify unsupported projection root/schema under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local_authoring_symbols
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Pass wrong document type or unsupported schema_version.
- **Expected Result:** Atomic symbol snapshot failure.
- **Expected Diagnostics:** MOD-NAMESPACE-002.
- **Boundary / Edge Cases:** No partial local symbols. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-02/03/04, MOD-05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T026 — Exact qualified lookup

- **Test ID:** MOD-06-T026
- **Scenario / category:** C. Qualified names — Exact qualified lookup
- **Objective:** Verify exact qualified lookup under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / AuthoringNameExpression
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Explicit sales.Customer has visible scoped symbol.
- **Expected Result:** Matching stable ID/context/kind returned.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Namespace case normalization only. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04, MOD-01.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T027 — Unknown qualified name

- **Test ID:** MOD-06-T027
- **Scenario / category:** C. Qualified names — Unknown qualified name
- **Objective:** Verify unknown qualified name under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / AuthoringNameExpression
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** sales.Missing absent from supplied visibility.
- **Expected Result:** Failure without another-context/namespace fallback.
- **Expected Diagnostics:** MOD-NAMESPACE-003.
- **Boundary / Edge Cases:** Similar names are not substitutions. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04, MOD-01.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T028 — Invalid qualified syntax

- **Test ID:** MOD-06-T028
- **Scenario / category:** C. Qualified names — Invalid qualified syntax
- **Objective:** Verify invalid qualified syntax under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / AuthoringNameExpression
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Construct authoring expression with malformed dotted text.
- **Expected Result:** Existing MOD-01/Kernel contract rejects before resolution.
- **Expected Diagnostics:** Existing QualifiedNameError / MOD-SCHEMA diagnostics.
- **Boundary / Edge Cases:** Empty segment and whitespace. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04, MOD-01.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T029 — Same QName across contexts

- **Test ID:** MOD-06-T029
- **Scenario / category:** C. Qualified names — Same QName across contexts
- **Objective:** Verify same qname across contexts under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / AuthoringNameExpression
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Separate environments each contain their own sales.Customer.
- **Expected Result:** Each resolves only its own scoped identity.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Combining them rejects context mismatch. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04, MOD-01.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T030 — No cross-context fallback

- **Test ID:** MOD-06-T030
- **Scenario / category:** C. Qualified names — No cross-context fallback
- **Objective:** Verify no cross-context fallback under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / AuthoringNameExpression
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** No local-context match but foreign environment has name.
- **Expected Result:** Resolver does not consult foreign environment.
- **Expected Diagnostics:** MOD-NAMESPACE-003 or request mismatch MOD-NAMESPACE-007.
- **Boundary / Edge Cases:** Context is not namespace. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04, MOD-01.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T031 — Qualified namespace outside local search

- **Test ID:** MOD-06-T031
- **Scenario / category:** C. Qualified names — Qualified namespace outside local search
- **Objective:** Verify qualified namespace outside local search under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / AuthoringNameExpression
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** crm.Customer is explicitly visible but crm not in local search list.
- **Expected Result:** Explicit qualified lookup succeeds.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Does not enable unqualified fallback. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04, MOD-01.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T032 — No similar-name correction

- **Test ID:** MOD-06-T032
- **Scenario / category:** C. Qualified names — No similar-name correction
- **Objective:** Verify no similar-name correction under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / AuthoringNameExpression
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Query customer versus Customer with only case-sensitive local name.
- **Expected Result:** No semantic correction or approximate search.
- **Expected Diagnostics:** MOD-NAMESPACE-003.
- **Boundary / Edge Cases:** QName local case is significant. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03/04, MOD-01.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T033 — Valid explicit alias

- **Test ID:** MOD-06-T033
- **Scenario / category:** D. Explicit aliases — Valid explicit alias
- **Objective:** Verify valid explicit alias under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceAlias / AliasQualifiedNameExpression / environment
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Alias crm maps to concrete customer_management namespace; target symbol visible.
- **Expected Result:** Alias-qualified Customer resolves concrete target identity.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Nested concrete target namespace. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03, MOD-01 syntax boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T034 — Unknown alias

- **Test ID:** MOD-06-T034
- **Scenario / category:** D. Explicit aliases — Unknown alias
- **Objective:** Verify unknown alias under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceAlias / AliasQualifiedNameExpression / environment
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Explicit alias expression references undeclared alias.
- **Expected Result:** Failure even if real namespace has same spelling.
- **Expected Diagnostics:** MOD-NAMESPACE-005.
- **Boundary / Edge Cases:** Empty alias tuple. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03, MOD-01 syntax boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T035 — Equal duplicate alias

- **Test ID:** MOD-06-T035
- **Scenario / category:** D. Explicit aliases — Equal duplicate alias
- **Objective:** Verify equal duplicate alias under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceAlias / AliasQualifiedNameExpression / environment
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Same canonical alias/target supplied twice.
- **Expected Result:** Idempotent normalized alias map.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Different declaration source paths choose deterministic retained record. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03, MOD-01 syntax boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T036 — Conflicting alias

- **Test ID:** MOD-06-T036
- **Scenario / category:** D. Explicit aliases — Conflicting alias
- **Objective:** Verify conflicting alias under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceAlias / AliasQualifiedNameExpression / environment
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Same alias maps to two different namespaces.
- **Expected Result:** Atomic environment failure naming alias/targets.
- **Expected Diagnostics:** MOD-NAMESPACE-006.
- **Boundary / Edge Cases:** Source primary/related paths retained if supplied. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03, MOD-01 syntax boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T037 — Direct alias expansion

- **Test ID:** MOD-06-T037
- **Scenario / category:** D. Explicit aliases — Direct alias expansion
- **Objective:** Verify direct alias expansion under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceAlias / AliasQualifiedNameExpression / environment
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Alias target spelling also matches another declared alias name.
- **Expected Result:** Resolve only concrete target namespace once.
- **Expected Diagnostics:** None if concrete symbol exists.
- **Boundary / Edge Cases:** No recursive alias expansion. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03, MOD-01 syntax boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T038 — Alias scope isolation

- **Test ID:** MOD-06-T038
- **Scenario / category:** D. Explicit aliases — Alias scope isolation
- **Objective:** Verify alias scope isolation under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceAlias / AliasQualifiedNameExpression / environment
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Alias exists in environment A but not B.
- **Expected Result:** B's explicit alias use fails without global sharing.
- **Expected Diagnostics:** MOD-NAMESPACE-005.
- **Boundary / Edge Cases:** Same semantic context, different environments. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03, MOD-01 syntax boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T039 — Alias versus ordinary QName

- **Test ID:** MOD-06-T039
- **Scenario / category:** D. Explicit aliases — Alias versus ordinary QName
- **Objective:** Verify alias versus ordinary qname under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceAlias / AliasQualifiedNameExpression / environment
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Both crm namespace and crm alias target have Customer symbols.
- **Expected Result:** Ordinary dotted name resolves real crm; explicit alias variant resolves concrete target.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** No alias shadowing of qualified names. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03, MOD-01 syntax boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T040 — No chain syntax

- **Test ID:** MOD-06-T040
- **Scenario / category:** D. Explicit aliases — No chain syntax
- **Objective:** Verify no chain syntax under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceAlias / AliasQualifiedNameExpression / environment
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Attempt alias target payload as NamespaceAlias instead of Namespace.
- **Expected Result:** Constructor rejects alias-to-alias payload.
- **Expected Diagnostics:** TypeError.
- **Boundary / Edge Cases:** Concrete namespace named after alias stays concrete. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03, MOD-01 syntax boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T041 — No cycle traversal

- **Test ID:** MOD-06-T041
- **Scenario / category:** D. Explicit aliases — No cycle traversal
- **Objective:** Verify no cycle traversal under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceAlias / AliasQualifiedNameExpression / environment
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Supply direct concrete aliases a to b and b to a.
- **Expected Result:** No recursion or alias graph; each target remains a namespace.
- **Expected Diagnostics:** None unless target symbol missing.
- **Boundary / Edge Cases:** Alias-cycle engine is inapplicable to v0. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03, MOD-01 syntax boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T042 — Invalid alias token

- **Test ID:** MOD-06-T042
- **Scenario / category:** D. Explicit aliases — Invalid alias token
- **Objective:** Verify invalid alias token under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceAlias / AliasQualifiedNameExpression / environment
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Multi-segment Namespace or raw alias string used in NamespaceAlias.
- **Expected Result:** Boundary rejects non-single canonical alias.
- **Expected Diagnostics:** TypeError / existing namespace syntax error.
- **Boundary / Edge Cases:** Canonical namespace case normalization. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03, MOD-01 syntax boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T043 — No MOD-01 syntax extension

- **Test ID:** MOD-06-T043
- **Scenario / category:** D. Explicit aliases — No MOD-01 syntax extension
- **Objective:** Verify no mod-01 syntax extension under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceAlias / AliasQualifiedNameExpression / environment
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Submit alias discriminator through decoded authoring schema.
- **Expected Result:** Existing schema remains closed; explicit capability only available via resolver request.
- **Expected Diagnostics:** Existing MOD-SCHEMA diagnostics.
- **Boundary / Edge Cases:** Ordinary dotted text remains a qualified name. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03, MOD-01 syntax boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T044 — Alias absent target symbol

- **Test ID:** MOD-06-T044
- **Scenario / category:** D. Explicit aliases — Alias absent target symbol
- **Objective:** Verify alias absent target symbol under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceAlias / AliasQualifiedNameExpression / environment
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Declared alias expands to concrete namespace with no symbol.
- **Expected Result:** Name lookup fails rather than inventing identity.
- **Expected Diagnostics:** MOD-NAMESPACE-003.
- **Boundary / Edge Cases:** Alias exists but target does not. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03, MOD-01 syntax boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T045 — Alias declaration locations

- **Test ID:** MOD-06-T045
- **Scenario / category:** D. Explicit aliases — Alias declaration locations
- **Objective:** Verify alias declaration locations under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceAlias / AliasQualifiedNameExpression / environment
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Conflicting aliases have source paths.
- **Expected Result:** Environment diagnostic identifies sorted primary/related paths.
- **Expected Diagnostics:** MOD-NAMESPACE-006.
- **Boundary / Edge Cases:** Missing paths remain absent. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-02/03, MOD-01 syntax boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T046 — Stable semantic identity

- **Test ID:** MOD-06-T046
- **Scenario / category:** E. Identity preservation — Stable semantic identity
- **Objective:** Verify stable semantic identity under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** ResolvedSemanticTarget / SemanticSymbol / NamespaceResolver
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** QName lookup maps to known sem UUID symbol.
- **Expected Result:** Actual existing ID appears in ElementRef.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** No ID derived from local-name text. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-01/03/07/08, TYPE-07 selected ownership.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T047 — Name-to-identity mapping

- **Test ID:** MOD-06-T047
- **Scenario / category:** E. Identity preservation — Name-to-identity mapping
- **Objective:** Verify name-to-identity mapping under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** ResolvedSemanticTarget / SemanticSymbol / NamespaceResolver
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Supply one explicitly visible symbol for sales.Customer.
- **Expected Result:** Result contains reference, context, kind and matching QName tuple.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Result is not merely normalized text. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-01/03/07/08, TYPE-07 selected ownership.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T048 — Rename stability

- **Test ID:** MOD-06-T048
- **Scenario / category:** E. Identity preservation — Rename stability
- **Objective:** Verify rename stability under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** ResolvedSemanticTarget / SemanticSymbol / NamespaceResolver
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Same ID appears at sales.Customer v1 and crm.Customer v2.
- **Expected Result:** Identity lookup preserves ID and reports recorded matching names.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** No arbitrary current name/version selected. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-01/03/07/08, TYPE-07 selected ownership.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T049 — Historical name scope

- **Test ID:** MOD-06-T049
- **Scenario / category:** E. Identity preservation — Historical name scope
- **Objective:** Verify historical name scope under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** ResolvedSemanticTarget / SemanticSymbol / NamespaceResolver
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Only renamed newer symbol is visible.
- **Expected Result:** Old QName does not become permanent alias.
- **Expected Diagnostics:** MOD-NAMESPACE-003.
- **Boundary / Edge Cases:** Explicitly visible old version permits old name only at its recorded coordinate. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-01/03/07/08, TYPE-07 selected ownership.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T050 — No generated IDs

- **Test ID:** MOD-06-T050
- **Scenario / category:** E. Identity preservation — No generated IDs
- **Objective:** Verify no generated ids under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** ResolvedSemanticTarget / SemanticSymbol / NamespaceResolver
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Resolve renamed/aliased names against supplied symbols.
- **Expected Result:** All output IDs are from those symbols.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Never random/time/name-based identity. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-01/03/07/08, TYPE-07 selected ownership.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T051 — No canonical alias leakage

- **Test ID:** MOD-06-T051
- **Scenario / category:** E. Identity preservation — No canonical alias leakage
- **Objective:** Verify no canonical alias leakage under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** ResolvedSemanticTarget / SemanticSymbol / NamespaceResolver
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Resolve explicit crm alias to customer_management.Customer.
- **Expected Result:** Reference carries stable ID only; matching name is concrete QName.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Alias text not stored as ElementRef payload. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-01/03/07/08, TYPE-07 selected ownership.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T052 — Identity expression bypass

- **Test ID:** MOD-06-T052
- **Scenario / category:** E. Identity preservation — Identity expression bypass
- **Objective:** Verify identity expression bypass under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** ResolvedSemanticTarget / SemanticSymbol / NamespaceResolver
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** AuthoringIdentityExpression points to visible ID with several names.
- **Expected Result:** Lookup uses identity index without QName re-resolution.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Renamed versions. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-01/03/07/08, TYPE-07 selected ownership.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T053 — Unknown identity

- **Test ID:** MOD-06-T053
- **Scenario / category:** E. Identity preservation — Unknown identity
- **Objective:** Verify unknown identity under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** ResolvedSemanticTarget / SemanticSymbol / NamespaceResolver
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Explicit ElementRef not represented by supplied symbols.
- **Expected Result:** Failure under explicit visibility.
- **Expected Diagnostics:** MOD-NAMESPACE-003.
- **Boundary / Edge Cases:** Existing elsewhere does not make it visible. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-01/03/07/08, TYPE-07 selected ownership.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T054 — Invalid nested identity

- **Test ID:** MOD-06-T054
- **Scenario / category:** E. Identity preservation — Invalid nested identity
- **Objective:** Verify invalid nested identity under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** ResolvedSemanticTarget / SemanticSymbol / NamespaceResolver
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Construct symbol/target/request reference with wrong nested ID type.
- **Expected Result:** Typed boundary rejects before lookup.
- **Expected Diagnostics:** TypeError.
- **Boundary / Edge Cases:** Corrupted frozen-value bypass is unsupported. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-01/03/07/08, TYPE-07 selected ownership.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T055 — Identity without version inference

- **Test ID:** MOD-06-T055
- **Scenario / category:** F. Version semantics — Identity without version inference
- **Objective:** Verify identity without version inference under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / ElementRef / ElementVersionRef
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Same QName/ID has several explicit visible versions.
- **Expected Result:** Result ElementRef carries no chosen version.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Version input permutations. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-07/08, TYPE-07, MOD-05 exact field pin gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T056 — Exact version request

- **Test ID:** MOD-06-T056
- **Scenario / category:** F. Version semantics — Exact version request
- **Objective:** Verify exact version request under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / ElementRef / ElementVersionRef
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** QName request explicitly asks for 1.0.0.
- **Expected Result:** Return exact ElementVersionRef only if visible.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Newer 1.1.0 must not replace request. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-07/08, TYPE-07, MOD-05 exact field pin gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T057 — Unknown exact version

- **Test ID:** MOD-06-T057
- **Scenario / category:** F. Version semantics — Unknown exact version
- **Objective:** Verify unknown exact version under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / ElementRef / ElementVersionRef
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Stable identity exists but requested version absent.
- **Expected Result:** Version failure with all relevant candidate coordinates.
- **Expected Diagnostics:** MOD-NAMESPACE-009.
- **Boundary / Edge Cases:** Patch version miss. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-07/08, TYPE-07, MOD-05 exact field pin gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T058 — Multiple registered versions

- **Test ID:** MOD-06-T058
- **Scenario / category:** F. Version semantics — Multiple registered versions
- **Objective:** Verify multiple registered versions under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / ElementRef / ElementVersionRef
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Combine symbols captured from separately explicit bound TYPE-07 views.
- **Expected Result:** Identity-only request remains unversioned.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** No latest choice. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-07/08, TYPE-07, MOD-05 exact field pin gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T059 — No latest shortcut

- **Test ID:** MOD-06-T059
- **Scenario / category:** F. Version semantics — No latest shortcut
- **Objective:** Verify no latest shortcut under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / ElementRef / ElementVersionRef
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Supply request payload latest/current/default/preferred.
- **Expected Result:** Existing SemanticVersion contract rejects unsupported pin.
- **Expected Diagnostics:** SemanticVersionError / TypeError at request boundary.
- **Boundary / Edge Cases:** No version compatibility policy. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-07/08, TYPE-07, MOD-05 exact field pin gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T060 — Exact authoring expression

- **Test ID:** MOD-06-T060
- **Scenario / category:** F. Version semantics — Exact authoring expression
- **Objective:** Verify exact authoring expression under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / ElementRef / ElementVersionRef
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Existing AuthoringVersionExpression targets visible exact coordinate.
- **Expected Result:** Authored exact pin preserved in result.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** exact_version argument absent. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-07/08, TYPE-07, MOD-05 exact field pin gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T061 — Conflicting exact requirements

- **Test ID:** MOD-06-T061
- **Scenario / category:** F. Version semantics — Conflicting exact requirements
- **Objective:** Verify conflicting exact requirements under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / ElementRef / ElementVersionRef
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** AuthoringVersionExpression pin differs from request.exact_version.
- **Expected Result:** Failure rather than silently choose either.
- **Expected Diagnostics:** MOD-NAMESPACE-001.
- **Boundary / Edge Cases:** Equal pins permitted. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-07/08, TYPE-07, MOD-05 exact field pin gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T062 — Renamed exact version mismatch

- **Test ID:** MOD-06-T062
- **Scenario / category:** F. Version semantics — Renamed exact version mismatch
- **Objective:** Verify renamed exact version mismatch under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / ElementRef / ElementVersionRef
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Query old QName at version whose visible symbol has new QName.
- **Expected Result:** Exact lookup does not treat old name as alias for renamed version.
- **Expected Diagnostics:** MOD-NAMESPACE-009.
- **Boundary / Edge Cases:** Identity expression may find exact renamed coordinate. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-07/08, TYPE-07, MOD-05 exact field pin gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T063 — Missing exact identity

- **Test ID:** MOD-06-T063
- **Scenario / category:** F. Version semantics — Missing exact identity
- **Objective:** Verify missing exact identity under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / ElementRef / ElementVersionRef
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Exact authored identity absent from visibility.
- **Expected Result:** Name/identity missing failure with exact pin retained.
- **Expected Diagnostics:** MOD-NAMESPACE-003.
- **Boundary / Edge Cases:** No invented target. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-07/08, TYPE-07, MOD-05 exact field pin gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T064 — Numeric candidate order

- **Test ID:** MOD-06-T064
- **Scenario / category:** F. Version semantics — Numeric candidate order
- **Objective:** Verify numeric candidate order under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / ElementRef / ElementVersionRef
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Visible versions include 1.2.0 and 1.10.0.
- **Expected Result:** Candidate ordering uses existing numeric SemanticVersion.
- **Expected Diagnostics:** None or expected ambiguity diagnostic.
- **Boundary / Edge Cases:** Textual lexical order must not choose version. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-07/08, TYPE-07, MOD-05 exact field pin gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T065 — ElementRef compatibility

- **Test ID:** MOD-06-T065
- **Scenario / category:** F. Version semantics — ElementRef compatibility
- **Objective:** Verify elementref compatibility under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / ElementRef / ElementVersionRef
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Successful unpinned name resolution.
- **Expected Result:** Existing identity-only ElementRef compatible with TYPE-05.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Reference has no namespace/version field. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-07/08, TYPE-07, MOD-05 exact field pin gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T066 — ElementVersionRef compatibility

- **Test ID:** MOD-06-T066
- **Scenario / category:** F. Version semantics — ElementVersionRef compatibility
- **Objective:** Verify elementversionref compatibility under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / ElementRef / ElementVersionRef
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Successful exact name/identity resolution.
- **Expected Result:** Existing exact reference retained through binding bridge.
- **Expected Diagnostics:** None in resolver; current MOD-05 rejects exact field pin later.
- **Boundary / Edge Cases:** No downgrade at bridge. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-07/08, TYPE-07, MOD-05 exact field pin gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T067 — Local symbols before registration

- **Test ID:** MOD-06-T067
- **Scenario / category:** G. Symbol sources — Local symbols before registration
- **Objective:** Verify local symbols before registration under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Project new document declarations not registered.
- **Expected Result:** Symbols visible after explicit environment construction.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Forward and self targets. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T068 — Registry-backed selected symbols

- **Test ID:** MOD-06-T068
- **Scenario / category:** G. Symbol sources — Registry-backed selected symbols
- **Objective:** Verify registry-backed selected symbols under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Supply actual immutable TypeRegistryLookup and explicit ElementRefs.
- **Expected Result:** Capture only selected canonical type coordinates.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Empty selection produces empty success. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T069 — Local and registry ownership collision

- **Test ID:** MOD-06-T069
- **Scenario / category:** G. Symbol sources — Local and registry ownership collision
- **Objective:** Verify local and registry ownership collision under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Distinct local/selected registry IDs own same QName.
- **Expected Result:** Environment rejects rather than local override.
- **Expected Diagnostics:** MOD-NAMESPACE-010.
- **Boundary / Edge Cases:** Historical visible versions included. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T070 — Same identity across sources

- **Test ID:** MOD-06-T070
- **Scenario / category:** G. Symbol sources — Same identity across sources
- **Objective:** Verify same identity across sources under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Local and selected registry symbols have same ID and compatible coordinates.
- **Expected Result:** Both sources compose without ambiguity.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Same-ID different versions allowed. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T071 — Different identities same QName

- **Test ID:** MOD-06-T071
- **Scenario / category:** G. Symbol sources — Different identities same QName
- **Objective:** Verify different identities same qname under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Two visible symbols share exact QName but different IDs.
- **Expected Result:** Complete environment rejected.
- **Expected Diagnostics:** MOD-NAMESPACE-010.
- **Boundary / Edge Cases:** Does not silently choose first registered. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T072 — No automatic registration

- **Test ID:** MOD-06-T072
- **Scenario / category:** G. Symbol sources — No automatic registration
- **Objective:** Verify no automatic registration under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Resolve local symbols with registry snapshot present elsewhere.
- **Expected Result:** No TypeRegistry.register or mutation operation.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Snapshot remains identical. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T073 — Explicit lookup selection only

- **Test ID:** MOD-06-T073
- **Scenario / category:** G. Symbol sources — Explicit lookup selection only
- **Objective:** Verify explicit lookup selection only under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Existing lookup contains additional identities not in references argument.
- **Expected Result:** Adapter never fetches or makes them visible.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Selection input duplicates normalize. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T074 — Unbound multi-version lookup

- **Test ID:** MOD-06-T074
- **Scenario / category:** G. Symbol sources — Unbound multi-version lookup
- **Objective:** Verify unbound multi-version lookup under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Plain TypeLookup raises actual TypeRegistryAmbiguityError.
- **Expected Result:** Atomic capture failure with delegated code/identity.
- **Expected Diagnostics:** MOD-NAMESPACE-011 / TYPE-REG-006.
- **Boundary / Edge Cases:** Caller must bind versions externally. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T075 — Missing selected identity

- **Test ID:** MOD-06-T075
- **Scenario / category:** G. Symbol sources — Missing selected identity
- **Objective:** Verify missing selected identity under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** TypeLookup returns None for one selected ID.
- **Expected Result:** Capture failure with no partial symbols.
- **Expected Diagnostics:** MOD-NAMESPACE-003.
- **Boundary / Edge Cases:** Other selected identities valid. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T076 — Mismatched lookup identity

- **Test ID:** MOD-06-T076
- **Scenario / category:** G. Symbol sources — Mismatched lookup identity
- **Objective:** Verify mismatched lookup identity under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Port returns host whose ID differs from requested reference.
- **Expected Result:** Capture fails before trusting host.
- **Expected Diagnostics:** MOD-NAMESPACE-002.
- **Boundary / Edge Cases:** Valid five properties with wrong ID. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T077 — Invalid lookup host

- **Test ID:** MOD-06-T077
- **Scenario / category:** G. Symbol sources — Invalid lookup host
- **Objective:** Verify invalid lookup host under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Port returns untyped root/name/context/kind/version values.
- **Expected Result:** Capture atomic invalid-environment failure.
- **Expected Diagnostics:** MOD-NAMESPACE-002.
- **Boundary / Edge Cases:** Wrong nested namespace/context identity. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T078 — Foreign lookup context

- **Test ID:** MOD-06-T078
- **Scenario / category:** G. Symbol sources — Foreign lookup context
- **Objective:** Verify foreign lookup context under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Selected host context differs from capture scope.
- **Expected Result:** Capture failure preserving candidate metadata.
- **Expected Diagnostics:** MOD-NAMESPACE-007.
- **Boundary / Edge Cases:** Namespace matches but context does not. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T079 — Non-type lookup host

- **Test ID:** MOD-06-T079
- **Scenario / category:** G. Symbol sources — Non-type lookup host
- **Objective:** Verify non-type lookup host under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** TypeLookup returns another semantic kind.
- **Expected Result:** Adapter rejects type-source contribution.
- **Expected Diagnostics:** MOD-NAMESPACE-008.
- **Boundary / Edge Cases:** Generic manually supplied symbols may represent other approved kinds. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T080 — Stable port snapshot

- **Test ID:** MOD-06-T080
- **Scenario / category:** G. Symbol sources — Stable port snapshot
- **Objective:** Verify stable port snapshot under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Capture symbols from actual immutable selected view then replace caller reference.
- **Expected Result:** Frozen environment uses captured values only.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Mutable/custom port stability is caller obligation. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T081 — Unexpected port error

- **Test ID:** MOD-06-T081
- **Scenario / category:** G. Symbol sources — Unexpected port error
- **Objective:** Verify unexpected port error under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Custom lookup raises unrelated programming exception.
- **Expected Result:** Unexpected failure remains visible, not disguised as missing name.
- **Expected Diagnostics:** Original unexpected exception.
- **Boundary / Edge Cases:** No blanket exception swallowing. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T082 — No full-definition content comparison

- **Test ID:** MOD-06-T082
- **Scenario / category:** G. Symbol sources — No full-definition content comparison
- **Objective:** Verify no full-definition content comparison under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Equal symbol metadata but differing unseen fields in source definitions.
- **Expected Result:** Resolver does not pretend to certify full definition equality.
- **Expected Diagnostics:** None from symbol metadata; later TYPE-07/MOD-04 owns content conflict.
- **Boundary / Edge Cases:** No field graph traversal. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T083 — Unseen registry history

- **Test ID:** MOD-06-T083
- **Scenario / category:** G. Symbol sources — Unseen registry history
- **Objective:** Verify unseen registry history under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** local_authoring_symbols / TypeLookupSymbolAdapter
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Selected view excludes historical name/version.
- **Expected Result:** Resolver sees only selected symbols; registry still governs registration ownership.
- **Expected Diagnostics:** None unless selected collision.
- **Boundary / Edge Cases:** No global catalog fallback. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, TYPE-07 TypeLookup and bound views.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T084 — Multiple searchable candidates

- **Test ID:** MOD-06-T084
- **Scenario / category:** H. Ambiguity and kind safeguards — Multiple searchable candidates
- **Objective:** Verify multiple searchable candidates under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / NamespaceResolutionDiagnostic
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** sales.Customer and crm.Customer have distinct IDs; both namespaces explicitly searchable.
- **Expected Result:** Atomic ambiguous-name failure with both candidates.
- **Expected Diagnostics:** MOD-NAMESPACE-004.
- **Boundary / Edge Cases:** Default current-only search is different explicit policy. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-03/06/07, explicit search policy.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T085 — Explicit ambiguity diagnostic

- **Test ID:** MOD-06-T085
- **Scenario / category:** H. Ambiguity and kind safeguards — Explicit ambiguity diagnostic
- **Objective:** Verify explicit ambiguity diagnostic under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / NamespaceResolutionDiagnostic
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Ambiguous local request has source path and expected kind/version.
- **Expected Result:** Diagnostic retains expression/context/pin/candidate identities/names.
- **Expected Diagnostics:** MOD-NAMESPACE-004.
- **Boundary / Edge Cases:** No successful target. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-03/06/07, explicit search policy.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T086 — Deterministic candidate ordering

- **Test ID:** MOD-06-T086
- **Scenario / category:** H. Ambiguity and kind safeguards — Deterministic candidate ordering
- **Objective:** Verify deterministic candidate ordering under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / NamespaceResolutionDiagnostic
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Permute visible candidates and registration source input.
- **Expected Result:** Same sorted candidate diagnostic tuple.
- **Expected Diagnostics:** MOD-NAMESPACE-004.
- **Boundary / Edge Cases:** Numeric versions and source path tie-breaks. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-03/06/07, explicit search policy.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T087 — No first match selection

- **Test ID:** MOD-06-T087
- **Scenario / category:** H. Ambiguity and kind safeguards — No first match selection
- **Objective:** Verify no first match selection under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / NamespaceResolutionDiagnostic
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Place different Customer identity first in local/visible input.
- **Expected Result:** Ambiguity remains regardless of order.
- **Expected Diagnostics:** MOD-NAMESPACE-004.
- **Boundary / Edge Cases:** Local source has no hidden priority. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-03/06/07, explicit search policy.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T088 — Expected kind not disambiguator

- **Test ID:** MOD-06-T088
- **Scenario / category:** H. Ambiguity and kind safeguards — Expected kind not disambiguator
- **Objective:** Verify expected kind not disambiguator under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / NamespaceResolutionDiagnostic
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Two identities match local name, one has requested kind.
- **Expected Result:** Fail ambiguity before kind requirement can choose identity.
- **Expected Diagnostics:** MOD-NAMESPACE-004.
- **Boundary / Edge Cases:** One identity wrong kind. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-03/06/07, explicit search policy.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T089 — Exact version not disambiguator

- **Test ID:** MOD-06-T089
- **Scenario / category:** H. Ambiguity and kind safeguards — Exact version not disambiguator
- **Objective:** Verify exact version not disambiguator under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / NamespaceResolutionDiagnostic
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Two identities match name but requested version appears on only one.
- **Expected Result:** Fail ambiguity rather than silently choose identity by version.
- **Expected Diagnostics:** MOD-NAMESPACE-004.
- **Boundary / Edge Cases:** One version absent. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-03/06/07, explicit search policy.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T090 — Unique identity wrong kind

- **Test ID:** MOD-06-T090
- **Scenario / category:** H. Ambiguity and kind safeguards — Unique identity wrong kind
- **Objective:** Verify unique identity wrong kind under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / NamespaceResolutionDiagnostic
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** One visible target is not expected_kind.
- **Expected Result:** Explicit mismatch without conversion.
- **Expected Diagnostics:** MOD-NAMESPACE-008.
- **Boundary / Edge Cases:** Same-ID versions must have consistent kind. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-03/06/07, explicit search policy.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T091 — Identity kind conflict

- **Test ID:** MOD-06-T091
- **Scenario / category:** H. Ambiguity and kind safeguards — Identity kind conflict
- **Objective:** Verify identity kind conflict under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / NamespaceResolutionDiagnostic
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Same ID has different kinds across versions in environment.
- **Expected Result:** Environment rejects complete snapshot.
- **Expected Diagnostics:** MOD-NAMESPACE-010.
- **Boundary / Edge Cases:** Explicit kind safeguard is not TYPE-06 validation. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-03/06/07, explicit search policy.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T092 — Current-only precedence behavior

- **Test ID:** MOD-06-T092
- **Scenario / category:** H. Ambiguity and kind safeguards — Current-only precedence behavior
- **Objective:** Verify current-only precedence behavior under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / NamespaceResolutionDiagnostic
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Only current_namespace is searchable though other names visible.
- **Expected Result:** Search only explicitly selected namespace.
- **Expected Diagnostics:** None or MOD-NAMESPACE-003.
- **Boundary / Edge Cases:** Not a fallback/shadowing rule. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** SK-03/06/07, explicit search policy.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T093 — Self-reference resolution

- **Test ID:** MOD-06-T093
- **Scenario / category:** I. Reference cycles — Self-reference resolution
- **Objective:** Verify self-reference resolution under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local symbol projection
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Employee.manager requests predeclared Employee.
- **Expected Result:** Identity target returned without constructing Employee fields.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Single symbol. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-08, explicit symbol environment.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T094 — Forward reference resolution

- **Test ID:** MOD-06-T094
- **Scenario / category:** I. Reference cycles — Forward reference resolution
- **Objective:** Verify forward reference resolution under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local symbol projection
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** A requests later declared B.
- **Expected Result:** B resolves from predeclared environment.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Source declaration ordering changed. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-08, explicit symbol environment.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T095 — Mutual references

- **Test ID:** MOD-06-T095
- **Scenario / category:** I. Reference cycles — Mutual references
- **Objective:** Verify mutual references under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local symbol projection
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Separate requests A.b to B and B.a to A in one explicit environment.
- **Expected Result:** Each identity resolves without recursive expansion.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Longer cycles. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-08, explicit symbol environment.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T096 — No recursive target expansion

- **Test ID:** MOD-06-T096
- **Scenario / category:** I. Reference cycles — No recursive target expansion
- **Objective:** Verify no recursive target expansion under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local symbol projection
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Symbol's definition would reference many other symbols.
- **Expected Result:** Resolver consults only coordinate indexes.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** No type graphs traversed. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-08, explicit symbol environment.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T097 — No infinite alias/reference loop

- **Test ID:** MOD-06-T097
- **Scenario / category:** I. Reference cycles — No infinite alias/reference loop
- **Objective:** Verify no infinite alias/reference loop under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / local symbol projection
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Cyclic semantic references and direct alias namespace spellings supplied.
- **Expected Result:** One bounded resolution per request; no recursion.
- **Expected Diagnostics:** None or normal missing diagnostic.
- **Boundary / Edge Cases:** No cycle rejection by default. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01, SK-08, explicit symbol environment.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T098 — Existing binding creation

- **Test ID:** MOD-06-T098
- **Scenario / category:** J. MOD-05 integration — Existing binding creation
- **Objective:** Verify existing binding creation under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** bind_namespace_target / NamespaceFieldBindingResult
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Resolve a type identity and supply facet/field coordinate plus stable FieldId.
- **Expected Result:** Existing ResolvedFieldBinding has original target reference.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** No new binding class substitutes for existing contract. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-05 ResolvedFieldBinding, TYPE-05, SK-08.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T099 — Canonicalizer input shape

- **Test ID:** MOD-06-T099
- **Scenario / category:** J. MOD-05 integration — Canonicalizer input shape
- **Objective:** Verify canonicalizer input shape under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** bind_namespace_target / NamespaceFieldBindingResult
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Caller inserts successful bridge binding into existing ResolvedTypeBinding/ResolvedAuthoringModel.
- **Expected Result:** Shape compatible; resolver never builds model itself.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Full orchestration belongs to caller/future stage. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-05 ResolvedFieldBinding, TYPE-05, SK-08.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T100 — Unresolved bridge rejection

- **Test ID:** MOD-06-T100
- **Scenario / category:** J. MOD-05 integration — Unresolved bridge rejection
- **Objective:** Verify unresolved bridge rejection under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** bind_namespace_target / NamespaceFieldBindingResult
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Resolution failure passed to bridge.
- **Expected Result:** No binding; original diagnostic tuple preserved.
- **Expected Diagnostics:** Original MOD-NAMESPACE diagnostic.
- **Boundary / Edge Cases:** No fabricated reference. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-05 ResolvedFieldBinding, TYPE-05, SK-08.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T101 — No canonical model construction

- **Test ID:** MOD-06-T101
- **Scenario / category:** J. MOD-05 integration — No canonical model construction
- **Objective:** Verify no canonical model construction under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** bind_namespace_target / NamespaceFieldBindingResult
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Inspect resolver/adapter/bridge calls.
- **Expected Result:** No CanonicalModelFactory/Canonicalizer/definition/facet/field construction.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Symbol projection uses coordinates only. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-05 ResolvedFieldBinding, TYPE-05, SK-08.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T102 — No duplicate reference contract

- **Test ID:** MOD-06-T102
- **Scenario / category:** J. MOD-05 integration — No duplicate reference contract
- **Objective:** Verify no duplicate reference contract under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** bind_namespace_target / NamespaceFieldBindingResult
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Compare successful bridge target type with existing SK refs.
- **Expected Result:** Existing ElementRef/ElementVersionRef reused.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Alias never adds target namespace metadata. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-05 ResolvedFieldBinding, TYPE-05, SK-08.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T103 — Exact pin preservation

- **Test ID:** MOD-06-T103
- **Scenario / category:** J. MOD-05 integration — Exact pin preservation
- **Objective:** Verify exact pin preservation under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** bind_namespace_target / NamespaceFieldBindingResult
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Bridge successful exact target.
- **Expected Result:** Exact reference remains exact; no weakened ElementRef.
- **Expected Diagnostics:** None from bridge; MOD-05 later MOD-TRANSFORM-007.
- **Boundary / Edge Cases:** Current TYPE-05 limitation explicit. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-05 ResolvedFieldBinding, TYPE-05, SK-08.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T104 — Non-type bridge target

- **Test ID:** MOD-06-T104
- **Scenario / category:** J. MOD-05 integration — Non-type bridge target
- **Objective:** Verify non-type bridge target under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** bind_namespace_target / NamespaceFieldBindingResult
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Resolve generic non-type symbol without expected_kind then bridge.
- **Expected Result:** Binding failure because semantic field requires type kind.
- **Expected Diagnostics:** MOD-NAMESPACE-008.
- **Boundary / Edge Cases:** Resolver itself can return explicitly approved non-type symbol. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-05 ResolvedFieldBinding, TYPE-05, SK-08.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T105 — Invalid field identity/coordinate

- **Test ID:** MOD-06-T105
- **Scenario / category:** J. MOD-05 integration — Invalid field identity/coordinate
- **Objective:** Verify invalid field identity/coordinate under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** bind_namespace_target / NamespaceFieldBindingResult
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Bridge gets raw FieldId, negative index or boolean.
- **Expected Result:** Reject developer misuse before constructing binding.
- **Expected Diagnostics:** TypeError.
- **Boundary / Edge Cases:** Zero indices accepted. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-05 ResolvedFieldBinding, TYPE-05, SK-08.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T106 — No MOD-07 orchestration

- **Test ID:** MOD-06-T106
- **Scenario / category:** J. MOD-05 integration — No MOD-07 orchestration
- **Objective:** Verify no mod-07 orchestration under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** bind_namespace_target / NamespaceFieldBindingResult
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Inspect changed API and production path.
- **Expected Result:** No complete reference-binding pipeline or model builder introduced.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Definition bindings remain caller supplied. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-05 ResolvedFieldBinding, TYPE-05, SK-08.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T107 — Name not found diagnostic

- **Test ID:** MOD-06-T107
- **Scenario / category:** K. Diagnostics and physical locations — Name not found diagnostic
- **Objective:** Verify name not found diagnostic under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Unknown local/qualified/identity request.
- **Expected Result:** Known code, context and expression preserved.
- **Expected Diagnostics:** MOD-NAMESPACE-003.
- **Boundary / Edge Cases:** No source required. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T108 — Ambiguous name diagnostic

- **Test ID:** MOD-06-T108
- **Scenario / category:** K. Diagnostics and physical locations — Ambiguous name diagnostic
- **Objective:** Verify ambiguous name diagnostic under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Multiple explicitly searchable identity targets.
- **Expected Result:** Stable candidate IDs/QNames/versions retained.
- **Expected Diagnostics:** MOD-NAMESPACE-004.
- **Boundary / Edge Cases:** All candidates available without full definitions. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T109 — Invalid alias diagnostic

- **Test ID:** MOD-06-T109
- **Scenario / category:** K. Diagnostics and physical locations — Invalid alias diagnostic
- **Objective:** Verify invalid alias diagnostic under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Explicit alias absent or malformed boundary value.
- **Expected Result:** Missing alias gives domain diagnostic; malformed constructor rejected.
- **Expected Diagnostics:** MOD-NAMESPACE-005 or boundary TypeError.
- **Boundary / Edge Cases:** Ordinary QName never treated as alias. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T110 — Context diagnostic

- **Test ID:** MOD-06-T110
- **Scenario / category:** K. Diagnostics and physical locations — Context diagnostic
- **Objective:** Verify context diagnostic under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Request/environment or symbol scope mismatch.
- **Expected Result:** Explicit context mismatch without fallback.
- **Expected Diagnostics:** MOD-NAMESPACE-007.
- **Boundary / Edge Cases:** Candidate context retained where available. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T111 — Kind diagnostic

- **Test ID:** MOD-06-T111
- **Scenario / category:** K. Diagnostics and physical locations — Kind diagnostic
- **Objective:** Verify kind diagnostic under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Unique target does not match expected kind.
- **Expected Result:** Kind mismatch independently of semantic validation.
- **Expected Diagnostics:** MOD-NAMESPACE-008.
- **Boundary / Edge Cases:** Expected kind optional. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T112 — Version diagnostic

- **Test ID:** MOD-06-T112
- **Scenario / category:** K. Diagnostics and physical locations — Version diagnostic
- **Objective:** Verify version diagnostic under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Exact requested coordinate missing.
- **Expected Result:** Pin and available matched candidates retained.
- **Expected Diagnostics:** MOD-NAMESPACE-009.
- **Boundary / Edge Cases:** Unknown name stays MOD-NAMESPACE-003. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T113 — Expression source location

- **Test ID:** MOD-06-T113
- **Scenario / category:** K. Diagnostics and physical locations — Expression source location
- **Objective:** Verify expression source location under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Request carries exact authoring source path; matching tracked loaded document supplied.
- **Expected Result:** Existing MOD-03 expression span attached externally.
- **Expected Diagnostics:** None or original failure code retained.
- **Boundary / Edge Cases:** Unicode/CRLF sources. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T114 — Related collision locations

- **Test ID:** MOD-06-T114
- **Scenario / category:** K. Diagnostics and physical locations — Related collision locations
- **Objective:** Verify related collision locations under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Symbol/alias collision diagnostic contains related_paths.
- **Expected Result:** Exact locations attached in same positions with missing entries None.
- **Expected Diagnostics:** Original MOD-NAMESPACE-006/010 retained.
- **Boundary / Edge Cases:** First/related declaration nodes. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T115 — Absent physical index

- **Test ID:** MOD-06-T115
- **Scenario / category:** K. Diagnostics and physical locations — Absent physical index
- **Objective:** Verify absent physical index under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** LoadedAuthoringDocument locations=None.
- **Expected Result:** Resolver/sidecar still works; physical positions absent.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Source path may remain typed. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T116 — Missing indexed node

- **Test ID:** MOD-06-T116
- **Scenario / category:** K. Diagnostics and physical locations — Missing indexed node
- **Objective:** Verify missing indexed node under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Some request/related paths absent from index.
- **Expected Result:** No fabricated or nearest-node location.
- **Expected Diagnostics:** None / original domain diagnostic.
- **Boundary / Edge Cases:** Missing related locations retain tuple positions. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T117 — Deterministic diagnostics

- **Test ID:** MOD-06-T117
- **Scenario / category:** K. Diagnostics and physical locations — Deterministic diagnostics
- **Objective:** Verify deterministic diagnostics under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Equivalent environment inputs supplied in different order.
- **Expected Result:** Same sorted collision/candidate/source path diagnostics.
- **Expected Diagnostics:** Exact relevant codes.
- **Boundary / Edge Cases:** No source-file first-match selection. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T118 — No mutable source index

- **Test ID:** MOD-06-T118
- **Scenario / category:** K. Diagnostics and physical locations — No mutable source index
- **Objective:** Verify no mutable source index under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Attach locations to valid result.
- **Expected Result:** Original SourceLocationIndex unchanged.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Success and failure. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T119 — Wrong document pairing obligation

- **Test ID:** MOD-06-T119
- **Scenario / category:** K. Diagnostics and physical locations — Wrong document pairing obligation
- **Objective:** Verify wrong document pairing obligation under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Supply same-shaped unrelated loaded source to location helper.
- **Expected Result:** Caller obligation explicit; helper cannot certify provenance.
- **Expected Diagnostics:** No false provenance/authority guarantee.
- **Boundary / Edge Cases:** Cross-document paths must be paired correctly. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T120 — Located result invariants

- **Test ID:** MOD-06-T120
- **Scenario / category:** K. Diagnostics and physical locations — Located result invariants
- **Objective:** Verify located result invariants under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Build sidecar with changed/missing domain diagnostic or wrong related length.
- **Expected Result:** Presentation contract rejects contradictory payload.
- **Expected Diagnostics:** ValueError developer misuse.
- **Boundary / Edge Cases:** Typed domain result preserved exactly. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T121 — Alias declaration path

- **Test ID:** MOD-06-T121
- **Scenario / category:** K. Diagnostics and physical locations — Alias declaration path
- **Objective:** Verify alias declaration path under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Conflicting aliases have optional declaration paths.
- **Expected Result:** Domain primary/related paths preserved without identity derivation.
- **Expected Diagnostics:** MOD-NAMESPACE-006.
- **Boundary / Edge Cases:** No path is mandatory. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T122 — General SK-11 gap

- **Test ID:** MOD-06-T122
- **Scenario / category:** K. Diagnostics and physical locations — General SK-11 gap
- **Objective:** Verify general sk-11 gap under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolutionDiagnostic / locate_namespace_resolution
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Inspect actual import/diagnostic contracts.
- **Expected Result:** Narrow current seam documented; no fabricated generic diagnostics model.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Full SK-11 requires separate real implementation. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** MOD-01 paths, MOD-03 actual location/index, SK-11 gap.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T123 — Pure Python domain

- **Test ID:** MOD-06-T123
- **Scenario / category:** L. Python / Django / DRF — Pure Python domain
- **Objective:** Verify pure python domain under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** Pure domain resolver / optional presentation
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Import registered public modules without Django/DRF installed.
- **Expected Result:** Public contracts import independently of frameworks.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Supported Python 3.11..3.13. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Repository architecture and future applicable DRF boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T124 — No ORM coupling

- **Test ID:** MOD-06-T124
- **Scenario / category:** L. Python / Django / DRF — No ORM coupling
- **Objective:** Verify no orm coupling under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** Pure domain resolver / optional presentation
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Inspect resolver/environment/symbol/adapter definitions.
- **Expected Result:** No ORM model/query/migration/database access.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Symbols are frozen domain coordinates. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Repository architecture and future applicable DRF boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T125 — No unnecessary endpoint

- **Test ID:** MOD-06-T125
- **Scenario / category:** L. Python / Django / DRF — No unnecessary endpoint
- **Objective:** Verify no unnecessary endpoint under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** Pure domain resolver / optional presentation
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Inspect routes/API production changes.
- **Expected Result:** No new public resolution endpoint or unrestricted catalog.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Required DRF stack does not imply route creation. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Repository architecture and future applicable DRF boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T126 — Existing DRF compatibility conditional

- **Test ID:** MOD-06-T126
- **Scenario / category:** L. Python / Django / DRF — Existing DRF compatibility conditional
- **Objective:** Verify existing drf compatibility conditional under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** Pure domain resolver / optional presentation
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** If future approved existing authoring endpoint requires resolution.
- **Expected Result:** Thin transport mapping preserves domain/security boundaries.
- **Expected Diagnostics:** Governed future API mapping; not implemented now.
- **Boundary / Edge Cases:** Real endpoint prerequisite first. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Repository architecture and future applicable DRF boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T127 — No mutable singleton

- **Test ID:** MOD-06-T127
- **Scenario / category:** L. Python / Django / DRF — No mutable singleton
- **Objective:** Verify no mutable singleton under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** Pure domain resolver / optional presentation
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Inspect module-level resolver/index state.
- **Expected Result:** Only immutable support vocabulary; per-environment owned state.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** No global caches/service locator. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Repository architecture and future applicable DRF boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T128 — Concurrent environments

- **Test ID:** MOD-06-T128
- **Scenario / category:** L. Python / Django / DRF — Concurrent environments
- **Objective:** Verify concurrent environments under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** Pure domain resolver / optional presentation
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Future authorized concurrent requests use different frozen environments.
- **Expected Result:** No state/alias/symbol leakage.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Identical names map to different IDs by scope. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Repository architecture and future applicable DRF boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T129 — No serializer resolution engine

- **Test ID:** MOD-06-T129
- **Scenario / category:** L. Python / Django / DRF — No serializer resolution engine
- **Objective:** Verify no serializer resolution engine under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** Pure domain resolver / optional presentation
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Inspect production HTTP boundary when supplied in future stage.
- **Expected Result:** Serializers do transport only; domain resolves.
- **Expected Diagnostics:** None for current no-API stage.
- **Boundary / Edge Cases:** Conditional future adapter. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Repository architecture and future applicable DRF boundary.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T130 — Customer within sales

- **Test ID:** MOD-06-T130
- **Scenario / category:** M. Mini Sales — Customer within sales
- **Objective:** Verify customer within sales under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** Established authoring example / unexecuted usage
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Project established Customer declaration and sales current namespace.
- **Expected Result:** Existing Customer stable ID resolved from local name.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Valid sem UUID, not typ_customer_123 placeholder. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** examples/authoring/mini-sales.json and .yaml, MOD-01/03/05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T131 — Explicit sales.Customer

- **Test ID:** MOD-06-T131
- **Scenario / category:** M. Mini Sales — Explicit sales.Customer
- **Objective:** Verify explicit sales.customer under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** Established authoring example / unexecuted usage
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Exact qualified expression against same environment.
- **Expected Result:** Same Customer identity/context/QName.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** No alias reinterpretation. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** examples/authoring/mini-sales.json and .yaml, MOD-01/03/05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T132 — Customer ID preservation

- **Test ID:** MOD-06-T132
- **Scenario / category:** M. Mini Sales — Customer ID preservation
- **Objective:** Verify customer id preservation under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** Established authoring example / unexecuted usage
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Resolve the established example through local symbol coordinates.
- **Expected Result:** sem_550e8400-e29b-41d4-a716-000000000001 retained.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Source file extension irrelevant. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** examples/authoring/mini-sales.json and .yaml, MOD-01/03/05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T133 — Exact Customer version

- **Test ID:** MOD-06-T133
- **Scenario / category:** M. Mini Sales — Exact Customer version
- **Objective:** Verify exact customer version under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** Established authoring example / unexecuted usage
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Request visible Customer 1.0.0 explicitly.
- **Expected Result:** Exact ElementVersionRef retains 1.0.0.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Adding visible 1.1.0 does not choose latest. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** examples/authoring/mini-sales.json and .yaml, MOD-01/03/05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T134 — Alias-qualified Customer

- **Test ID:** MOD-06-T134
- **Scenario / category:** M. Mini Sales — Alias-qualified Customer
- **Objective:** Verify alias-qualified customer under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** Established authoring example / unexecuted usage
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Supply resolver-only crm to concrete customer_management and visible Customer symbol.
- **Expected Result:** Explicit alias request returns concrete QName and stable ID.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Ordinary crm.Customer stays real QName. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** examples/authoring/mini-sales.json and .yaml, MOD-01/03/05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T135 — Ambiguous Customer namespaces

- **Test ID:** MOD-06-T135
- **Scenario / category:** M. Mini Sales — Ambiguous Customer namespaces
- **Objective:** Verify ambiguous customer namespaces under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** Established authoring example / unexecuted usage
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Supply two distinct Customer identities with sales/crm explicitly searchable.
- **Expected Result:** Ambiguity with deterministic candidates.
- **Expected Diagnostics:** MOD-NAMESPACE-004.
- **Boundary / Edge Cases:** No current namespace hidden preference. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** examples/authoring/mini-sales.json and .yaml, MOD-01/03/05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T136 — Local Employee self-reference

- **Test ID:** MOD-06-T136
- **Scenario / category:** M. Mini Sales — Local Employee self-reference
- **Objective:** Verify local employee self-reference under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** Established authoring example / unexecuted usage
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Caller supplies local Employee declared symbol before manager request.
- **Expected Result:** Same stable Employee identity resolved without registry.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Additional example is documentation only, no new fixture code. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** examples/authoring/mini-sales.json and .yaml, MOD-01/03/05.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T137 — No package resolution

- **Test ID:** MOD-06-T137
- **Scenario / category:** N. Architectural boundaries — No package resolution
- **Objective:** Verify no package resolution under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / adapters / bridge
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Resolve against finite supplied environment.
- **Expected Result:** No package lookup/install/discovery.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Missing name fails normally. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Architecture manifest/policy, standing deferred-test requirement.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T138 — No import recursion

- **Test ID:** MOD-06-T138
- **Scenario / category:** N. Architectural boundaries — No import recursion
- **Objective:** Verify no import recursion under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / adapters / bridge
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Inspect source and resolve explicit symbols.
- **Expected Result:** No recursive import or source loading.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** No wildcard namespace imports. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Architecture manifest/policy, standing deferred-test requirement.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T139 — No semantic validation engine

- **Test ID:** MOD-06-T139
- **Scenario / category:** N. Architectural boundaries — No semantic validation engine
- **Objective:** Verify no semantic validation engine under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / adapters / bridge
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Resolve kind and identity only.
- **Expected Result:** TYPE-06 constraint applicability/graph validation not invoked.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Kind safeguard is bounded. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Architecture manifest/policy, standing deferred-test requirement.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T140 — No canonicalization

- **Test ID:** MOD-06-T140
- **Scenario / category:** N. Architectural boundaries — No canonicalization
- **Objective:** Verify no canonicalization under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / adapters / bridge
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Inspect resolver operation and bridge.
- **Expected Result:** No type/data/field/canonical model construction or Canonicalizer invocation.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Symbol projection is coordinate-only. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Architecture manifest/policy, standing deferred-test requirement.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T141 — No compiler

- **Test ID:** MOD-06-T141
- **Scenario / category:** N. Architectural boundaries — No compiler
- **Objective:** Verify no compiler under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / adapters / bridge
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Inspect dependency graph.
- **Expected Result:** No compiler artifacts/jobs/services used.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Output is semantic target only. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Architecture manifest/policy, standing deferred-test requirement.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T142 — No runtime execution

- **Test ID:** MOD-06-T142
- **Scenario / category:** N. Architectural boundaries — No runtime execution
- **Objective:** Verify no runtime execution under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / adapters / bridge
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Inspect dependencies and request algorithm.
- **Expected Result:** No runtime lookup/action/event execution.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Resolution context is authoring semantic scope. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Architecture manifest/policy, standing deferred-test requirement.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T143 — No authorization logic

- **Test ID:** MOD-06-T143
- **Scenario / category:** N. Architectural boundaries — No authorization logic
- **Objective:** Verify no authorization logic under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / adapters / bridge
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Inspect context/environment metadata.
- **Expected Result:** No tenant/org/security grants inferred from visibility.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** HTTP authorization remains external. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Architecture manifest/policy, standing deferred-test requirement.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T144 — No implicit namespace inference

- **Test ID:** MOD-06-T144
- **Scenario / category:** N. Architectural boundaries — No implicit namespace inference
- **Objective:** Verify no implicit namespace inference under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / adapters / bridge
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Request uses explicit environment namespace values.
- **Expected Result:** No namespace derived from path/database/tenant/name similarity.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Current namespace always explicit. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Architecture manifest/policy, standing deferred-test requirement.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T145 — No automatic global visibility

- **Test ID:** MOD-06-T145
- **Scenario / category:** N. Architectural boundaries — No automatic global visibility
- **Objective:** Verify no automatic global visibility under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / adapters / bridge
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Selected lookup adapter and local symbols determine visibility.
- **Expected Result:** Registry contents not enumerated automatically.
- **Expected Diagnostics:** None.
- **Boundary / Edge Cases:** Unselected identities absent. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Architecture manifest/policy, standing deferred-test requirement.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

## MOD-06-T146 — No test implementation/execution

- **Test ID:** MOD-06-T146
- **Scenario / category:** N. Architectural boundaries — No test implementation/execution
- **Objective:** Verify no test implementation/execution under explicit semantic visibility without inventing identity, selecting an unspecified version or changing semantic definitions.
- **Component:** NamespaceResolver / adapters / bridge
- **Prerequisites:** Explicit future authorization; fixed revision; supported Python and registered source paths; actual listed contracts and approved typed input. Use existing constructor/schema boundaries for unrepresentable payloads; future DRF scenarios require their real separately approved endpoint.
- **Input / Setup:** Inspect changed sources/archive/CI.
- **Expected Result:** No new executable tests/runner; deferred CI steps skipped.
- **Expected Diagnostics:** NOT_RUN — DEFERRED.
- **Boundary / Edge Cases:** Historical tests and execution evidence preserved. Preserve failed boundaries rather than silently repairing unsupported data.
- **Integration Dependencies:** Architecture manifest/policy, standing deferred-test requirement.
- **Acceptance Criteria:** Observe and record the stated target/failure boundary, exact relevant diagnostic and deterministic ordering, with no environment/registry/source-index mutation, alias leakage, canonicalization or hidden lookup/version policy. Unexpected programming errors remain distinguishable from expected resolution failure.
- **Execution Status:** NOT_RUN — DEFERRED

