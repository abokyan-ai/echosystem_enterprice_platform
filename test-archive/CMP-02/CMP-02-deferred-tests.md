# CMP-02 — Deferred Test Specification

Task: CMP-02 — Compilation Diagnostics

Backend: Python / Django / Django REST Framework

Status: NOT_RUN — DEFERRED

New Tests Implemented: 0

Tests Executed: 0

Documentation date: 2026-10-11

Dependencies: SK-11 (general contract unavailable), MOD-03, MOD-04, MOD-08, MOD-09, CMP-01 and compiled-contracts metadata seams.

This file contains the complete future scenario specification. No executable tests, fixture runners or scenario demonstrations were created or run. Static syntax/build/import/dependency inspection is separate and does not establish behavioral correctness. Pin a source revision, obtain explicit user authorization for future execution, supply actual immutable canonical/validation/source fixtures and preserve original producer objects. General SK-11 factory and standalone facet contracts, concrete generator fixtures and HTTP/auth integrations are unavailable; dependent scenarios remain blocked until their actual owners supply those contracts. Do not substitute invented types or treat unavailable integration as passing.

Each scenario applies specifically to its named behavior and includes positive, invalid and boundary variants as stated. Shared fixture descriptions are specifications, not executed setup.

## CMP-02-T001 — Diagnostic code preservation

- Category: SK-11 Compatibility.
- Component / contract: CompilationDiagnosticEntry / existing diagnostic payload.
- Objective: Verify diagnostic code preservation while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: CMP-01 original diagnostic with CMP-002 code, WARNING severity and an author-controlled message; actual TYPE-06 / MOD-08 diagnostics remain separate.
- Expected behavior: Preserve the exact original payload object and its scalar values; no new severity/factory/general diagnostic framework. General SK-11 factory compatibility is BLOCKED until that upstream contract exists.
- Expected invalid-case diagnostics: Wrong diagnostic or severity type raises TypeError; unavailable SK-11 is recorded as an unmet prerequisite, never passed.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to diagnostic code preservation; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for diagnostic code preservation; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T002 — Severity preservation

- Category: SK-11 Compatibility.
- Component / contract: CompilationDiagnosticEntry / existing diagnostic payload.
- Objective: Verify severity preservation while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: CMP-01 original diagnostic with CMP-002 code, WARNING severity and an author-controlled message; actual TYPE-06 / MOD-08 diagnostics remain separate.
- Expected behavior: Preserve the exact original payload object and its scalar values; no new severity/factory/general diagnostic framework. General SK-11 factory compatibility is BLOCKED until that upstream contract exists.
- Expected invalid-case diagnostics: Wrong diagnostic or severity type raises TypeError; unavailable SK-11 is recorded as an unmet prerequisite, never passed.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to severity preservation; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for severity preservation; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T003 — Message preservation

- Category: SK-11 Compatibility.
- Component / contract: CompilationDiagnosticEntry / existing diagnostic payload.
- Objective: Verify message preservation while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: CMP-01 original diagnostic with CMP-002 code, WARNING severity and an author-controlled message; actual TYPE-06 / MOD-08 diagnostics remain separate.
- Expected behavior: Preserve the exact original payload object and its scalar values; no new severity/factory/general diagnostic framework. General SK-11 factory compatibility is BLOCKED until that upstream contract exists.
- Expected invalid-case diagnostics: Wrong diagnostic or severity type raises TypeError; unavailable SK-11 is recorded as an unmet prerequisite, never passed.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to message preservation; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for message preservation; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T004 — Existing diagnostic factory compatibility

- Category: SK-11 Compatibility.
- Component / contract: CompilationDiagnosticEntry / existing diagnostic payload.
- Objective: Verify existing diagnostic factory compatibility while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: CMP-01 original diagnostic with CMP-002 code, WARNING severity and an author-controlled message; actual TYPE-06 / MOD-08 diagnostics remain separate.
- Expected behavior: Preserve the exact original payload object and its scalar values; no new severity/factory/general diagnostic framework. General SK-11 factory compatibility is BLOCKED until that upstream contract exists.
- Expected invalid-case diagnostics: Wrong diagnostic or severity type raises TypeError; unavailable SK-11 is recorded as an unmet prerequisite, never passed.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to existing diagnostic factory compatibility; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for existing diagnostic factory compatibility; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T005 — No competing diagnostic model

- Category: SK-11 Compatibility.
- Component / contract: CompilationDiagnosticEntry / existing diagnostic payload.
- Objective: Verify no competing diagnostic model while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: CMP-01 original diagnostic with CMP-002 code, WARNING severity and an author-controlled message; actual TYPE-06 / MOD-08 diagnostics remain separate.
- Expected behavior: Preserve the exact original payload object and its scalar values; no new severity/factory/general diagnostic framework. General SK-11 factory compatibility is BLOCKED until that upstream contract exists.
- Expected invalid-case diagnostics: Wrong diagnostic or severity type raises TypeError; unavailable SK-11 is recorded as an unmet prerequisite, never passed.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no competing diagnostic model; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no competing diagnostic model; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T006 — Prerequisite diagnostics

- Category: Compiler Origins.
- Component / contract: CompilationDiagnosticAssociation / origin projection.
- Objective: Verify prerequisite diagnostics while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Explicit associations for each of the six CompilationDiagnosticOrigin values; use an actual scheduled phase outcome for executed phase origins.
- Expected behavior: Retain explicit responsibility independently of ModelDiagnosticOrigin.COMPILER, location and severity; legacy CMP-01 codes use the fixed ownership table, never message classification.
- Expected invalid-case diagnostics: Missing/wrong origin raises TypeError on a new association; PHASE/ARTIFACT_CONSTRUCTION without phase and prerequisite with phase raise ValueError; historical detail-free projection remains explicitly unassociated.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to prerequisite diagnostics; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for prerequisite diagnostics; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T007 — Orchestrator diagnostics

- Category: Compiler Origins.
- Component / contract: CompilationDiagnosticAssociation / origin projection.
- Objective: Verify orchestrator diagnostics while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Explicit associations for each of the six CompilationDiagnosticOrigin values; use an actual scheduled phase outcome for executed phase origins.
- Expected behavior: Retain explicit responsibility independently of ModelDiagnosticOrigin.COMPILER, location and severity; legacy CMP-01 codes use the fixed ownership table, never message classification.
- Expected invalid-case diagnostics: Missing/wrong origin raises TypeError on a new association; PHASE/ARTIFACT_CONSTRUCTION without phase and prerequisite with phase raise ValueError; historical detail-free projection remains explicitly unassociated.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to orchestrator diagnostics; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for orchestrator diagnostics; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T008 — Compiler phase diagnostics

- Category: Compiler Origins.
- Component / contract: CompilationDiagnosticAssociation / origin projection.
- Objective: Verify compiler phase diagnostics while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Explicit associations for each of the six CompilationDiagnosticOrigin values; use an actual scheduled phase outcome for executed phase origins.
- Expected behavior: Retain explicit responsibility independently of ModelDiagnosticOrigin.COMPILER, location and severity; legacy CMP-01 codes use the fixed ownership table, never message classification.
- Expected invalid-case diagnostics: Missing/wrong origin raises TypeError on a new association; PHASE/ARTIFACT_CONSTRUCTION without phase and prerequisite with phase raise ValueError; historical detail-free projection remains explicitly unassociated.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to compiler phase diagnostics; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for compiler phase diagnostics; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T009 — Artifact construction diagnostics

- Category: Compiler Origins.
- Component / contract: CompilationDiagnosticAssociation / origin projection.
- Objective: Verify artifact construction diagnostics while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Explicit associations for each of the six CompilationDiagnosticOrigin values; use an actual scheduled phase outcome for executed phase origins.
- Expected behavior: Retain explicit responsibility independently of ModelDiagnosticOrigin.COMPILER, location and severity; legacy CMP-01 codes use the fixed ownership table, never message classification.
- Expected invalid-case diagnostics: Missing/wrong origin raises TypeError on a new association; PHASE/ARTIFACT_CONSTRUCTION without phase and prerequisite with phase raise ValueError; historical detail-free projection remains explicitly unassociated.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to artifact construction diagnostics; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for artifact construction diagnostics; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T010 — Artifact collection diagnostics

- Category: Compiler Origins.
- Component / contract: CompilationDiagnosticAssociation / origin projection.
- Objective: Verify artifact collection diagnostics while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Explicit associations for each of the six CompilationDiagnosticOrigin values; use an actual scheduled phase outcome for executed phase origins.
- Expected behavior: Retain explicit responsibility independently of ModelDiagnosticOrigin.COMPILER, location and severity; legacy CMP-01 codes use the fixed ownership table, never message classification.
- Expected invalid-case diagnostics: Missing/wrong origin raises TypeError on a new association; PHASE/ARTIFACT_CONSTRUCTION without phase and prerequisite with phase raise ValueError; historical detail-free projection remains explicitly unassociated.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to artifact collection diagnostics; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for artifact collection diagnostics; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T011 — Missing origin handling

- Category: Compiler Origins.
- Component / contract: CompilationDiagnosticAssociation / origin projection.
- Objective: Verify missing origin handling while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Explicit associations for each of the six CompilationDiagnosticOrigin values; use an actual scheduled phase outcome for executed phase origins.
- Expected behavior: Retain explicit responsibility independently of ModelDiagnosticOrigin.COMPILER, location and severity; legacy CMP-01 codes use the fixed ownership table, never message classification.
- Expected invalid-case diagnostics: Missing/wrong origin raises TypeError on a new association; PHASE/ARTIFACT_CONSTRUCTION without phase and prerequisite with phase raise ValueError; historical detail-free projection remains explicitly unassociated.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to missing origin handling; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for missing origin handling; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T012 — Valid phase association

- Category: Phase Association.
- Component / contract: CompilationDiagnosticReporter / CompilerPhaseDiagnosticView.
- Objective: Verify valid phase association while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original ordered phase outcomes, mandatory prepare plus configured future phase; preserve actual execution evidence True/False/None and prerequisites.
- Expected behavior: Use producer phase IDs/outcome order, preserve reason and prerequisite tuple; skipped outcome has no execution diagnostics and False evidence; legacy unknown execution stays None.
- Expected invalid-case diagnostics: Unknown/mismatched phase association, skipped/nonexecuted execution responsibility or inconsistent occurrence evidence raises ValueError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to valid phase association; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for valid phase association; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T013 — Missing phase association

- Category: Phase Association.
- Component / contract: CompilationDiagnosticReporter / CompilerPhaseDiagnosticView.
- Objective: Verify missing phase association while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original ordered phase outcomes, mandatory prepare plus configured future phase; preserve actual execution evidence True/False/None and prerequisites.
- Expected behavior: Use producer phase IDs/outcome order, preserve reason and prerequisite tuple; skipped outcome has no execution diagnostics and False evidence; legacy unknown execution stays None.
- Expected invalid-case diagnostics: Unknown/mismatched phase association, skipped/nonexecuted execution responsibility or inconsistent occurrence evidence raises ValueError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to missing phase association; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for missing phase association; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T014 — Prerequisite-only diagnostic

- Category: Phase Association.
- Component / contract: CompilationDiagnosticReporter / CompilerPhaseDiagnosticView.
- Objective: Verify prerequisite-only diagnostic while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original ordered phase outcomes, mandatory prepare plus configured future phase; preserve actual execution evidence True/False/None and prerequisites.
- Expected behavior: Use producer phase IDs/outcome order, preserve reason and prerequisite tuple; skipped outcome has no execution diagnostics and False evidence; legacy unknown execution stays None.
- Expected invalid-case diagnostics: Unknown/mismatched phase association, skipped/nonexecuted execution responsibility or inconsistent occurrence evidence raises ValueError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to prerequisite-only diagnostic; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for prerequisite-only diagnostic; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T015 — Failed phase

- Category: Phase Association.
- Component / contract: CompilationDiagnosticReporter / CompilerPhaseDiagnosticView.
- Objective: Verify failed phase while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original ordered phase outcomes, mandatory prepare plus configured future phase; preserve actual execution evidence True/False/None and prerequisites.
- Expected behavior: Use producer phase IDs/outcome order, preserve reason and prerequisite tuple; skipped outcome has no execution diagnostics and False evidence; legacy unknown execution stays None.
- Expected invalid-case diagnostics: Unknown/mismatched phase association, skipped/nonexecuted execution responsibility or inconsistent occurrence evidence raises ValueError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to failed phase; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for failed phase; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T016 — Skipped phase

- Category: Phase Association.
- Component / contract: CompilationDiagnosticReporter / CompilerPhaseDiagnosticView.
- Objective: Verify skipped phase while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original ordered phase outcomes, mandatory prepare plus configured future phase; preserve actual execution evidence True/False/None and prerequisites.
- Expected behavior: Use producer phase IDs/outcome order, preserve reason and prerequisite tuple; skipped outcome has no execution diagnostics and False evidence; legacy unknown execution stays None.
- Expected invalid-case diagnostics: Unknown/mismatched phase association, skipped/nonexecuted execution responsibility or inconsistent occurrence evidence raises ValueError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to skipped phase; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for skipped phase; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T017 — Deterministic phase ordering

- Category: Phase Association.
- Component / contract: CompilationDiagnosticReporter / CompilerPhaseDiagnosticView.
- Objective: Verify deterministic phase ordering while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original ordered phase outcomes, mandatory prepare plus configured future phase; preserve actual execution evidence True/False/None and prerequisites.
- Expected behavior: Use producer phase IDs/outcome order, preserve reason and prerequisite tuple; skipped outcome has no execution diagnostics and False evidence; legacy unknown execution stays None.
- Expected invalid-case diagnostics: Unknown/mismatched phase association, skipped/nonexecuted execution responsibility or inconsistent occurrence evidence raises ValueError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to deterministic phase ordering; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for deterministic phase ordering; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T018 — No fabricated phase execution

- Category: Phase Association.
- Component / contract: CompilationDiagnosticReporter / CompilerPhaseDiagnosticView.
- Objective: Verify no fabricated phase execution while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original ordered phase outcomes, mandatory prepare plus configured future phase; preserve actual execution evidence True/False/None and prerequisites.
- Expected behavior: Use producer phase IDs/outcome order, preserve reason and prerequisite tuple; skipped outcome has no execution diagnostics and False evidence; legacy unknown execution stays None.
- Expected invalid-case diagnostics: Unknown/mismatched phase association, skipped/nonexecuted execution responsibility or inconsistent occurrence evidence raises ValueError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no fabricated phase execution; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no fabricated phase execution; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T019 — Definition-level association

- Category: Semantic Targets.
- Component / contract: ModelDiagnosticTarget / CompilationDiagnosticAssociation.
- Objective: Verify definition-level association while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Actual exact Customer ElementVersionRef, owned name FieldId and explicit SemanticContextRef; only supported current TypeDataComposition/DataFacet host.
- Expected behavior: Keep exact version, owner definition plus FieldId, related references and context separately; facet occurrence uses explicit authoring path under its definition, not a fabricated standalone semantic identity.
- Expected invalid-case diagnostics: Wrong identity or context type raises TypeError; nonexact primary/related compiler definition references raise ValueError; standalone facet identity is unavailable until an upstream owner defines it.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to definition-level association; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for definition-level association; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T020 — Field-level association

- Category: Semantic Targets.
- Component / contract: ModelDiagnosticTarget / CompilationDiagnosticAssociation.
- Objective: Verify field-level association while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Actual exact Customer ElementVersionRef, owned name FieldId and explicit SemanticContextRef; only supported current TypeDataComposition/DataFacet host.
- Expected behavior: Keep exact version, owner definition plus FieldId, related references and context separately; facet occurrence uses explicit authoring path under its definition, not a fabricated standalone semantic identity.
- Expected invalid-case diagnostics: Wrong identity or context type raises TypeError; nonexact primary/related compiler definition references raise ValueError; standalone facet identity is unavailable until an upstream owner defines it.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to field-level association; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for field-level association; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T021 — Facet-level association

- Category: Semantic Targets.
- Component / contract: ModelDiagnosticTarget / CompilationDiagnosticAssociation.
- Objective: Verify facet-level association while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Actual exact Customer ElementVersionRef, owned name FieldId and explicit SemanticContextRef; only supported current TypeDataComposition/DataFacet host.
- Expected behavior: Keep exact version, owner definition plus FieldId, related references and context separately; facet occurrence uses explicit authoring path under its definition, not a fabricated standalone semantic identity.
- Expected invalid-case diagnostics: Wrong identity or context type raises TypeError; nonexact primary/related compiler definition references raise ValueError; standalone facet identity is unavailable until an upstream owner defines it.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to facet-level association; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for facet-level association; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T022 — Context-level association

- Category: Semantic Targets.
- Component / contract: ModelDiagnosticTarget / CompilationDiagnosticAssociation.
- Objective: Verify context-level association while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Actual exact Customer ElementVersionRef, owned name FieldId and explicit SemanticContextRef; only supported current TypeDataComposition/DataFacet host.
- Expected behavior: Keep exact version, owner definition plus FieldId, related references and context separately; facet occurrence uses explicit authoring path under its definition, not a fabricated standalone semantic identity.
- Expected invalid-case diagnostics: Wrong identity or context type raises TypeError; nonexact primary/related compiler definition references raise ValueError; standalone facet identity is unavailable until an upstream owner defines it.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to context-level association; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for context-level association; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T023 — Exact version preservation

- Category: Semantic Targets.
- Component / contract: ModelDiagnosticTarget / CompilationDiagnosticAssociation.
- Objective: Verify exact version preservation while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Actual exact Customer ElementVersionRef, owned name FieldId and explicit SemanticContextRef; only supported current TypeDataComposition/DataFacet host.
- Expected behavior: Keep exact version, owner definition plus FieldId, related references and context separately; facet occurrence uses explicit authoring path under its definition, not a fabricated standalone semantic identity.
- Expected invalid-case diagnostics: Wrong identity or context type raises TypeError; nonexact primary/related compiler definition references raise ValueError; standalone facet identity is unavailable until an upstream owner defines it.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to exact version preservation; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for exact version preservation; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T024 — No fabricated semantic identity

- Category: Semantic Targets.
- Component / contract: ModelDiagnosticTarget / CompilationDiagnosticAssociation.
- Objective: Verify no fabricated semantic identity while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Actual exact Customer ElementVersionRef, owned name FieldId and explicit SemanticContextRef; only supported current TypeDataComposition/DataFacet host.
- Expected behavior: Keep exact version, owner definition plus FieldId, related references and context separately; facet occurrence uses explicit authoring path under its definition, not a fabricated standalone semantic identity.
- Expected invalid-case diagnostics: Wrong identity or context type raises TypeError; nonexact primary/related compiler definition references raise ValueError; standalone facet identity is unavailable until an upstream owner defines it.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no fabricated semantic identity; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no fabricated semantic identity; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T025 — Valid artifact identity

- Category: Artifact Targets.
- Component / contract: CompilationArtifactTarget / CompilationArtifactDiagnosticView.
- Objective: Verify valid artifact identity while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Existing CompilationArtifactKey and Kind plus BUILD_TARGET; key-only, kind-only, intended-target-only and key conflict with multiple exact semantic dependencies.
- Expected behavior: Project actual typed independent tokens without constructing an artifact; conflict retains key and all candidate semantic dependencies in deterministic candidate/dependency order.
- Expected invalid-case diagnostics: Empty association raises ValueError; semantic ID, filename, dict or wrong artifact token type raises TypeError/ValueError; missing identity is allowed when explicit kind/target is provided.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to valid artifact identity; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for valid artifact identity; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T026 — Artifact-kind-only association

- Category: Artifact Targets.
- Component / contract: CompilationArtifactTarget / CompilationArtifactDiagnosticView.
- Objective: Verify artifact-kind-only association while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Existing CompilationArtifactKey and Kind plus BUILD_TARGET; key-only, kind-only, intended-target-only and key conflict with multiple exact semantic dependencies.
- Expected behavior: Project actual typed independent tokens without constructing an artifact; conflict retains key and all candidate semantic dependencies in deterministic candidate/dependency order.
- Expected invalid-case diagnostics: Empty association raises ValueError; semantic ID, filename, dict or wrong artifact token type raises TypeError/ValueError; missing identity is allowed when explicit kind/target is provided.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to artifact-kind-only association; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for artifact-kind-only association; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T027 — Artifact conflict association

- Category: Artifact Targets.
- Component / contract: CompilationArtifactTarget / CompilationArtifactDiagnosticView.
- Objective: Verify artifact conflict association while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Existing CompilationArtifactKey and Kind plus BUILD_TARGET; key-only, kind-only, intended-target-only and key conflict with multiple exact semantic dependencies.
- Expected behavior: Project actual typed independent tokens without constructing an artifact; conflict retains key and all candidate semantic dependencies in deterministic candidate/dependency order.
- Expected invalid-case diagnostics: Empty association raises ValueError; semantic ID, filename, dict or wrong artifact token type raises TypeError/ValueError; missing identity is allowed when explicit kind/target is provided.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to artifact conflict association; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for artifact conflict association; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T028 — Multiple semantic origins

- Category: Artifact Targets.
- Component / contract: CompilationArtifactTarget / CompilationArtifactDiagnosticView.
- Objective: Verify multiple semantic origins while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Existing CompilationArtifactKey and Kind plus BUILD_TARGET; key-only, kind-only, intended-target-only and key conflict with multiple exact semantic dependencies.
- Expected behavior: Project actual typed independent tokens without constructing an artifact; conflict retains key and all candidate semantic dependencies in deterministic candidate/dependency order.
- Expected invalid-case diagnostics: Empty association raises ValueError; semantic ID, filename, dict or wrong artifact token type raises TypeError/ValueError; missing identity is allowed when explicit kind/target is provided.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to multiple semantic origins; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for multiple semantic origins; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T029 — Missing artifact identity

- Category: Artifact Targets.
- Component / contract: CompilationArtifactTarget / CompilationArtifactDiagnosticView.
- Objective: Verify missing artifact identity while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Existing CompilationArtifactKey and Kind plus BUILD_TARGET; key-only, kind-only, intended-target-only and key conflict with multiple exact semantic dependencies.
- Expected behavior: Project actual typed independent tokens without constructing an artifact; conflict retains key and all candidate semantic dependencies in deterministic candidate/dependency order.
- Expected invalid-case diagnostics: Empty association raises ValueError; semantic ID, filename, dict or wrong artifact token type raises TypeError/ValueError; missing identity is allowed when explicit kind/target is provided.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to missing artifact identity; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for missing artifact identity; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T030 — No placeholder artifact generation

- Category: Artifact Targets.
- Component / contract: CompilationArtifactTarget / CompilationArtifactDiagnosticView.
- Objective: Verify no placeholder artifact generation while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Existing CompilationArtifactKey and Kind plus BUILD_TARGET; key-only, kind-only, intended-target-only and key conflict with multiple exact semantic dependencies.
- Expected behavior: Project actual typed independent tokens without constructing an artifact; conflict retains key and all candidate semantic dependencies in deterministic candidate/dependency order.
- Expected invalid-case diagnostics: Empty association raises ValueError; semantic ID, filename, dict or wrong artifact token type raises TypeError/ValueError; missing identity is allowed when explicit kind/target is provided.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no placeholder artifact generation; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no placeholder artifact generation; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T031 — Missing validation evidence

- Category: Compilation Prerequisites.
- Component / contract: CMP-01 prerequisite result / CMP-02 reporting.
- Objective: Verify missing validation evidence while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Results from missing evidence, INVALID, INCOMPLETE, unbound evidence, different canonical object, scope mismatch and unsupported target; fixed original evidence and source associations.
- Expected behavior: Preserve original authoritative FAILED/INCOMPLETE, diagnostics CMP-002/003/004/005/006 as appropriate, validation origins/evidence and skipped phase evidence; never invoke validation.
- Expected invalid-case diagnostics: CMP-002 denotes not-ready evidence, CMP-003 unbound, CMP-004 snapshot mismatch, CMP-005 scope mismatch and CMP-006 unsupported target; no downstream fabricated outputs.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to missing validation evidence; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for missing validation evidence; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T032 — INVALID validation

- Category: Compilation Prerequisites.
- Component / contract: CMP-01 prerequisite result / CMP-02 reporting.
- Objective: Verify invalid validation while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Results from missing evidence, INVALID, INCOMPLETE, unbound evidence, different canonical object, scope mismatch and unsupported target; fixed original evidence and source associations.
- Expected behavior: Preserve original authoritative FAILED/INCOMPLETE, diagnostics CMP-002/003/004/005/006 as appropriate, validation origins/evidence and skipped phase evidence; never invoke validation.
- Expected invalid-case diagnostics: CMP-002 denotes not-ready evidence, CMP-003 unbound, CMP-004 snapshot mismatch, CMP-005 scope mismatch and CMP-006 unsupported target; no downstream fabricated outputs.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to invalid validation; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for invalid validation; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T033 — INCOMPLETE validation

- Category: Compilation Prerequisites.
- Component / contract: CMP-01 prerequisite result / CMP-02 reporting.
- Objective: Verify incomplete validation while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Results from missing evidence, INVALID, INCOMPLETE, unbound evidence, different canonical object, scope mismatch and unsupported target; fixed original evidence and source associations.
- Expected behavior: Preserve original authoritative FAILED/INCOMPLETE, diagnostics CMP-002/003/004/005/006 as appropriate, validation origins/evidence and skipped phase evidence; never invoke validation.
- Expected invalid-case diagnostics: CMP-002 denotes not-ready evidence, CMP-003 unbound, CMP-004 snapshot mismatch, CMP-005 scope mismatch and CMP-006 unsupported target; no downstream fabricated outputs.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to incomplete validation; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for incomplete validation; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T034 — NOT_READY compilation readiness

- Category: Compilation Prerequisites.
- Component / contract: CMP-01 prerequisite result / CMP-02 reporting.
- Objective: Verify not_ready compilation readiness while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Results from missing evidence, INVALID, INCOMPLETE, unbound evidence, different canonical object, scope mismatch and unsupported target; fixed original evidence and source associations.
- Expected behavior: Preserve original authoritative FAILED/INCOMPLETE, diagnostics CMP-002/003/004/005/006 as appropriate, validation origins/evidence and skipped phase evidence; never invoke validation.
- Expected invalid-case diagnostics: CMP-002 denotes not-ready evidence, CMP-003 unbound, CMP-004 snapshot mismatch, CMP-005 scope mismatch and CMP-006 unsupported target; no downstream fabricated outputs.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to not_ready compilation readiness; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for not_ready compilation readiness; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T035 — Canonical snapshot mismatch

- Category: Compilation Prerequisites.
- Component / contract: CMP-01 prerequisite result / CMP-02 reporting.
- Objective: Verify canonical snapshot mismatch while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Results from missing evidence, INVALID, INCOMPLETE, unbound evidence, different canonical object, scope mismatch and unsupported target; fixed original evidence and source associations.
- Expected behavior: Preserve original authoritative FAILED/INCOMPLETE, diagnostics CMP-002/003/004/005/006 as appropriate, validation origins/evidence and skipped phase evidence; never invoke validation.
- Expected invalid-case diagnostics: CMP-002 denotes not-ready evidence, CMP-003 unbound, CMP-004 snapshot mismatch, CMP-005 scope mismatch and CMP-006 unsupported target; no downstream fabricated outputs.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to canonical snapshot mismatch; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for canonical snapshot mismatch; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T036 — Context mismatch

- Category: Compilation Prerequisites.
- Component / contract: CMP-01 prerequisite result / CMP-02 reporting.
- Objective: Verify context mismatch while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Results from missing evidence, INVALID, INCOMPLETE, unbound evidence, different canonical object, scope mismatch and unsupported target; fixed original evidence and source associations.
- Expected behavior: Preserve original authoritative FAILED/INCOMPLETE, diagnostics CMP-002/003/004/005/006 as appropriate, validation origins/evidence and skipped phase evidence; never invoke validation.
- Expected invalid-case diagnostics: CMP-002 denotes not-ready evidence, CMP-003 unbound, CMP-004 snapshot mismatch, CMP-005 scope mismatch and CMP-006 unsupported target; no downstream fabricated outputs.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to context mismatch; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for context mismatch; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T037 — Unsupported compilation target

- Category: Compilation Prerequisites.
- Component / contract: CMP-01 prerequisite result / CMP-02 reporting.
- Objective: Verify unsupported compilation target while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Results from missing evidence, INVALID, INCOMPLETE, unbound evidence, different canonical object, scope mismatch and unsupported target; fixed original evidence and source associations.
- Expected behavior: Preserve original authoritative FAILED/INCOMPLETE, diagnostics CMP-002/003/004/005/006 as appropriate, validation origins/evidence and skipped phase evidence; never invoke validation.
- Expected invalid-case diagnostics: CMP-002 denotes not-ready evidence, CMP-003 unbound, CMP-004 snapshot mismatch, CMP-005 scope mismatch and CMP-006 unsupported target; no downstream fabricated outputs.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to unsupported compilation target; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for unsupported compilation target; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T038 — SUCCEEDED

- Category: Compilation Status.
- Component / contract: CompilationResult / CompilationDiagnosticReport.
- Objective: Verify succeeded while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original succeeded preparation result, failed phase result and incomplete default artifact-build result; include warnings and repeated diagnostics.
- Expected behavior: Preserve the producer status without deriving it from severity/count; empty and warning-only incomplete projections remain incomplete; output count is actual final collection size.
- Expected invalid-case diagnostics: Malformed producer success retains CMP-01 ValueError guards; non-success report with positive successful artifact count raises ValueError; malformed report status raises TypeError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to succeeded; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for succeeded; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T039 — FAILED

- Category: Compilation Status.
- Component / contract: CompilationResult / CompilationDiagnosticReport.
- Objective: Verify failed while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original succeeded preparation result, failed phase result and incomplete default artifact-build result; include warnings and repeated diagnostics.
- Expected behavior: Preserve the producer status without deriving it from severity/count; empty and warning-only incomplete projections remain incomplete; output count is actual final collection size.
- Expected invalid-case diagnostics: Malformed producer success retains CMP-01 ValueError guards; non-success report with positive successful artifact count raises ValueError; malformed report status raises TypeError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to failed; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for failed; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T040 — INCOMPLETE

- Category: Compilation Status.
- Component / contract: CompilationResult / CompilationDiagnosticReport.
- Objective: Verify incomplete while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original succeeded preparation result, failed phase result and incomplete default artifact-build result; include warnings and repeated diagnostics.
- Expected behavior: Preserve the producer status without deriving it from severity/count; empty and warning-only incomplete projections remain incomplete; output count is actual final collection size.
- Expected invalid-case diagnostics: Malformed producer success retains CMP-01 ValueError guards; non-success report with positive successful artifact count raises ValueError; malformed report status raises TypeError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to incomplete; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for incomplete; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T041 — No status inference from diagnostic count

- Category: Compilation Status.
- Component / contract: CompilationResult / CompilationDiagnosticReport.
- Objective: Verify no status inference from diagnostic count while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original succeeded preparation result, failed phase result and incomplete default artifact-build result; include warnings and repeated diagnostics.
- Expected behavior: Preserve the producer status without deriving it from severity/count; empty and warning-only incomplete projections remain incomplete; output count is actual final collection size.
- Expected invalid-case diagnostics: Malformed producer success retains CMP-01 ValueError guards; non-success report with positive successful artifact count raises ValueError; malformed report status raises TypeError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no status inference from diagnostic count; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no status inference from diagnostic count; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T042 — Missing mandatory phase

- Category: Compilation Status.
- Component / contract: CompilationResult / CompilationDiagnosticReport.
- Objective: Verify missing mandatory phase while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original succeeded preparation result, failed phase result and incomplete default artifact-build result; include warnings and repeated diagnostics.
- Expected behavior: Preserve the producer status without deriving it from severity/count; empty and warning-only incomplete projections remain incomplete; output count is actual final collection size.
- Expected invalid-case diagnostics: Malformed producer success retains CMP-01 ValueError guards; non-success report with positive successful artifact count raises ValueError; malformed report status raises TypeError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to missing mandatory phase; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for missing mandatory phase; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T043 — Completed phase with warning

- Category: Compilation Status.
- Component / contract: CompilationResult / CompilationDiagnosticReport.
- Objective: Verify completed phase with warning while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original succeeded preparation result, failed phase result and incomplete default artifact-build result; include warnings and repeated diagnostics.
- Expected behavior: Preserve the producer status without deriving it from severity/count; empty and warning-only incomplete projections remain incomplete; output count is actual final collection size.
- Expected invalid-case diagnostics: Malformed producer success retains CMP-01 ValueError guards; non-success report with positive successful artifact count raises ValueError; malformed report status raises TypeError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to completed phase with warning; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for completed phase with warning; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T044 — Failed phase with multiple diagnostics

- Category: Compilation Status.
- Component / contract: CompilationResult / CompilationDiagnosticReport.
- Objective: Verify failed phase with multiple diagnostics while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original succeeded preparation result, failed phase result and incomplete default artifact-build result; include warnings and repeated diagnostics.
- Expected behavior: Preserve the producer status without deriving it from severity/count; empty and warning-only incomplete projections remain incomplete; output count is actual final collection size.
- Expected invalid-case diagnostics: Malformed producer success retains CMP-01 ValueError guards; non-success report with positive successful artifact count raises ValueError; malformed report status raises TypeError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to failed phase with multiple diagnostics; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for failed phase with multiple diagnostics; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T045 — Precise source association

- Category: Source Locations.
- Component / contract: MOD-09 source enrichment / MOD-03 indexes.
- Objective: Verify precise source association while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Explicit canonical definition/field association and optional AuthoringSchemaPath; immutable SourceLocationIndex selected by an explicit ModelSourceId; collision related targets.
- Expected behavior: Use reliable existing authoring paths and actual index coordinates; explicit paths precede inferred mapping; missing/ambiguous maps remain unavailable; already located entries are returned intact.
- Expected invalid-case diagnostics: Wrong source context/index types raise TypeError; duplicate indexes for one source raise ValueError; absent target-config mapping has no fabricated span; multi-source association requires explicit caller source selection.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to precise source association; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for precise source association; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T046 — Related source locations

- Category: Source Locations.
- Component / contract: MOD-09 source enrichment / MOD-03 indexes.
- Objective: Verify related source locations while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Explicit canonical definition/field association and optional AuthoringSchemaPath; immutable SourceLocationIndex selected by an explicit ModelSourceId; collision related targets.
- Expected behavior: Use reliable existing authoring paths and actual index coordinates; explicit paths precede inferred mapping; missing/ambiguous maps remain unavailable; already located entries are returned intact.
- Expected invalid-case diagnostics: Wrong source context/index types raise TypeError; duplicate indexes for one source raise ValueError; absent target-config mapping has no fabricated span; multi-source association requires explicit caller source selection.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to related source locations; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for related source locations; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T047 — Missing physical source location

- Category: Source Locations.
- Component / contract: MOD-09 source enrichment / MOD-03 indexes.
- Objective: Verify missing physical source location while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Explicit canonical definition/field association and optional AuthoringSchemaPath; immutable SourceLocationIndex selected by an explicit ModelSourceId; collision related targets.
- Expected behavior: Use reliable existing authoring paths and actual index coordinates; explicit paths precede inferred mapping; missing/ambiguous maps remain unavailable; already located entries are returned intact.
- Expected invalid-case diagnostics: Wrong source context/index types raise TypeError; duplicate indexes for one source raise ValueError; absent target-config mapping has no fabricated span; multi-source association requires explicit caller source selection.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to missing physical source location; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for missing physical source location; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T048 — No fabricated coordinates

- Category: Source Locations.
- Component / contract: MOD-09 source enrichment / MOD-03 indexes.
- Objective: Verify no fabricated coordinates while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Explicit canonical definition/field association and optional AuthoringSchemaPath; immutable SourceLocationIndex selected by an explicit ModelSourceId; collision related targets.
- Expected behavior: Use reliable existing authoring paths and actual index coordinates; explicit paths precede inferred mapping; missing/ambiguous maps remain unavailable; already located entries are returned intact.
- Expected invalid-case diagnostics: Wrong source context/index types raise TypeError; duplicate indexes for one source raise ValueError; absent target-config mapping has no fabricated span; multi-source association requires explicit caller source selection.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no fabricated coordinates; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no fabricated coordinates; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T049 — Existing diagnostic location preservation

- Category: Source Locations.
- Component / contract: MOD-09 source enrichment / MOD-03 indexes.
- Objective: Verify existing diagnostic location preservation while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Explicit canonical definition/field association and optional AuthoringSchemaPath; immutable SourceLocationIndex selected by an explicit ModelSourceId; collision related targets.
- Expected behavior: Use reliable existing authoring paths and actual index coordinates; explicit paths precede inferred mapping; missing/ambiguous maps remain unavailable; already located entries are returned intact.
- Expected invalid-case diagnostics: Wrong source context/index types raise TypeError; duplicate indexes for one source raise ValueError; absent target-config mapping has no fabricated span; multi-source association requires explicit caller source selection.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to existing diagnostic location preservation; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for existing diagnostic location preservation; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T050 — Compiler target configuration locations

- Category: Source Locations.
- Component / contract: MOD-09 source enrichment / MOD-03 indexes.
- Objective: Verify compiler target configuration locations while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Explicit canonical definition/field association and optional AuthoringSchemaPath; immutable SourceLocationIndex selected by an explicit ModelSourceId; collision related targets.
- Expected behavior: Use reliable existing authoring paths and actual index coordinates; explicit paths precede inferred mapping; missing/ambiguous maps remain unavailable; already located entries are returned intact.
- Expected invalid-case diagnostics: Wrong source context/index types raise TypeError; duplicate indexes for one source raise ValueError; absent target-config mapping has no fabricated span; multi-source association requires explicit caller source selection.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to compiler target configuration locations; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for compiler target configuration locations; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T051 — Single diagnostic

- Category: Diagnostic Aggregation.
- Component / contract: CompilationDiagnosticReporter / immutable ordered entries.
- Objective: Verify single diagnostic while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original diagnostics with repeated object occurrences and distinct equal-valued messages, gate/orchestrator/phase/collection/result diagnostics in producer order.
- Expected behavior: Keep validation entries first with original origins; keep every compiler diagnostic occurrence in authoritative CMP-01 emission order; ownership uses original object occurrence, not text/equality deduplication.
- Expected invalid-case diagnostics: Missing original phase occurrence, too few repeated occurrences or out-of-range association index raises ValueError; malformed context/pairs raises TypeError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to single diagnostic; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for single diagnostic; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T052 — Multiple diagnostics

- Category: Diagnostic Aggregation.
- Component / contract: CompilationDiagnosticReporter / immutable ordered entries.
- Objective: Verify multiple diagnostics while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original diagnostics with repeated object occurrences and distinct equal-valued messages, gate/orchestrator/phase/collection/result diagnostics in producer order.
- Expected behavior: Keep validation entries first with original origins; keep every compiler diagnostic occurrence in authoritative CMP-01 emission order; ownership uses original object occurrence, not text/equality deduplication.
- Expected invalid-case diagnostics: Missing original phase occurrence, too few repeated occurrences or out-of-range association index raises ValueError; malformed context/pairs raises TypeError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to multiple diagnostics; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for multiple diagnostics; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T053 — Multiple phase origins

- Category: Diagnostic Aggregation.
- Component / contract: CompilationDiagnosticReporter / immutable ordered entries.
- Objective: Verify multiple phase origins while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original diagnostics with repeated object occurrences and distinct equal-valued messages, gate/orchestrator/phase/collection/result diagnostics in producer order.
- Expected behavior: Keep validation entries first with original origins; keep every compiler diagnostic occurrence in authoritative CMP-01 emission order; ownership uses original object occurrence, not text/equality deduplication.
- Expected invalid-case diagnostics: Missing original phase occurrence, too few repeated occurrences or out-of-range association index raises ValueError; malformed context/pairs raises TypeError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to multiple phase origins; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for multiple phase origins; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T054 — Prerequisite and phase diagnostics

- Category: Diagnostic Aggregation.
- Component / contract: CompilationDiagnosticReporter / immutable ordered entries.
- Objective: Verify prerequisite and phase diagnostics while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original diagnostics with repeated object occurrences and distinct equal-valued messages, gate/orchestrator/phase/collection/result diagnostics in producer order.
- Expected behavior: Keep validation entries first with original origins; keep every compiler diagnostic occurrence in authoritative CMP-01 emission order; ownership uses original object occurrence, not text/equality deduplication.
- Expected invalid-case diagnostics: Missing original phase occurrence, too few repeated occurrences or out-of-range association index raises ValueError; malformed context/pairs raises TypeError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to prerequisite and phase diagnostics; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for prerequisite and phase diagnostics; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T055 — Lossless aggregation

- Category: Diagnostic Aggregation.
- Component / contract: CompilationDiagnosticReporter / immutable ordered entries.
- Objective: Verify lossless aggregation while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original diagnostics with repeated object occurrences and distinct equal-valued messages, gate/orchestrator/phase/collection/result diagnostics in producer order.
- Expected behavior: Keep validation entries first with original origins; keep every compiler diagnostic occurrence in authoritative CMP-01 emission order; ownership uses original object occurrence, not text/equality deduplication.
- Expected invalid-case diagnostics: Missing original phase occurrence, too few repeated occurrences or out-of-range association index raises ValueError; malformed context/pairs raises TypeError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to lossless aggregation; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for lossless aggregation; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T056 — Explicit duplicate handling

- Category: Diagnostic Aggregation.
- Component / contract: CompilationDiagnosticReporter / immutable ordered entries.
- Objective: Verify explicit duplicate handling while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original diagnostics with repeated object occurrences and distinct equal-valued messages, gate/orchestrator/phase/collection/result diagnostics in producer order.
- Expected behavior: Keep validation entries first with original origins; keep every compiler diagnostic occurrence in authoritative CMP-01 emission order; ownership uses original object occurrence, not text/equality deduplication.
- Expected invalid-case diagnostics: Missing original phase occurrence, too few repeated occurrences or out-of-range association index raises ValueError; malformed context/pairs raises TypeError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to explicit duplicate handling; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for explicit duplicate handling; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T057 — Deterministic ordering

- Category: Diagnostic Aggregation.
- Component / contract: CompilationDiagnosticReporter / immutable ordered entries.
- Objective: Verify deterministic ordering while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original diagnostics with repeated object occurrences and distinct equal-valued messages, gate/orchestrator/phase/collection/result diagnostics in producer order.
- Expected behavior: Keep validation entries first with original origins; keep every compiler diagnostic occurrence in authoritative CMP-01 emission order; ownership uses original object occurrence, not text/equality deduplication.
- Expected invalid-case diagnostics: Missing original phase occurrence, too few repeated occurrences or out-of-range association index raises ValueError; malformed context/pairs raises TypeError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to deterministic ordering; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for deterministic ordering; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T058 — Total count

- Category: Diagnostic Summary.
- Component / contract: CompilationDiagnosticReport.summary / read-only grouping.
- Objective: Verify total count while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Compiler entries with ERROR/WARNING/INFO, separate validation entries and empty/incomplete projection; repeated identical messages count as separate occurrences.
- Expected behavior: Derive compiler-only total and each supported severity count; combined MOD-09 summary remains distinct; group counts cover every associated entry without changing status.
- Expected invalid-case diagnostics: Invalid manual summary (negative/bool/inconsistent totals) raises ValueError; unavailable full SK-11 severity extensions are not invented.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to total count; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for total count; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T059 — Error count

- Category: Diagnostic Summary.
- Component / contract: CompilationDiagnosticReport.summary / read-only grouping.
- Objective: Verify error count while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Compiler entries with ERROR/WARNING/INFO, separate validation entries and empty/incomplete projection; repeated identical messages count as separate occurrences.
- Expected behavior: Derive compiler-only total and each supported severity count; combined MOD-09 summary remains distinct; group counts cover every associated entry without changing status.
- Expected invalid-case diagnostics: Invalid manual summary (negative/bool/inconsistent totals) raises ValueError; unavailable full SK-11 severity extensions are not invented.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to error count; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for error count; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T060 — Warning count

- Category: Diagnostic Summary.
- Component / contract: CompilationDiagnosticReport.summary / read-only grouping.
- Objective: Verify warning count while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Compiler entries with ERROR/WARNING/INFO, separate validation entries and empty/incomplete projection; repeated identical messages count as separate occurrences.
- Expected behavior: Derive compiler-only total and each supported severity count; combined MOD-09 summary remains distinct; group counts cover every associated entry without changing status.
- Expected invalid-case diagnostics: Invalid manual summary (negative/bool/inconsistent totals) raises ValueError; unavailable full SK-11 severity extensions are not invented.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to warning count; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for warning count; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T061 — Information count where supported

- Category: Diagnostic Summary.
- Component / contract: CompilationDiagnosticReport.summary / read-only grouping.
- Objective: Verify information count where supported while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Compiler entries with ERROR/WARNING/INFO, separate validation entries and empty/incomplete projection; repeated identical messages count as separate occurrences.
- Expected behavior: Derive compiler-only total and each supported severity count; combined MOD-09 summary remains distinct; group counts cover every associated entry without changing status.
- Expected invalid-case diagnostics: Invalid manual summary (negative/bool/inconsistent totals) raises ValueError; unavailable full SK-11 severity extensions are not invented.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to information count where supported; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for information count where supported; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T062 — Counts by phase

- Category: Diagnostic Summary.
- Component / contract: CompilationDiagnosticReport.summary / read-only grouping.
- Objective: Verify counts by phase while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Compiler entries with ERROR/WARNING/INFO, separate validation entries and empty/incomplete projection; repeated identical messages count as separate occurrences.
- Expected behavior: Derive compiler-only total and each supported severity count; combined MOD-09 summary remains distinct; group counts cover every associated entry without changing status.
- Expected invalid-case diagnostics: Invalid manual summary (negative/bool/inconsistent totals) raises ValueError; unavailable full SK-11 severity extensions are not invented.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to counts by phase; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for counts by phase; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T063 — Counts by origin

- Category: Diagnostic Summary.
- Component / contract: CompilationDiagnosticReport.summary / read-only grouping.
- Objective: Verify counts by origin while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Compiler entries with ERROR/WARNING/INFO, separate validation entries and empty/incomplete projection; repeated identical messages count as separate occurrences.
- Expected behavior: Derive compiler-only total and each supported severity count; combined MOD-09 summary remains distinct; group counts cover every associated entry without changing status.
- Expected invalid-case diagnostics: Invalid manual summary (negative/bool/inconsistent totals) raises ValueError; unavailable full SK-11 severity extensions are not invented.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to counts by origin; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for counts by origin; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T064 — Empty report

- Category: Diagnostic Summary.
- Component / contract: CompilationDiagnosticReport.summary / read-only grouping.
- Objective: Verify empty report while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Compiler entries with ERROR/WARNING/INFO, separate validation entries and empty/incomplete projection; repeated identical messages count as separate occurrences.
- Expected behavior: Derive compiler-only total and each supported severity count; combined MOD-09 summary remains distinct; group counts cover every associated entry without changing status.
- Expected invalid-case diagnostics: Invalid manual summary (negative/bool/inconsistent totals) raises ValueError; unavailable full SK-11 severity extensions are not invented.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to empty report; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for empty report; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T065 — INCOMPLETE result with no diagnostics

- Category: Diagnostic Summary.
- Component / contract: CompilationDiagnosticReport.summary / read-only grouping.
- Objective: Verify incomplete result with no diagnostics while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Compiler entries with ERROR/WARNING/INFO, separate validation entries and empty/incomplete projection; repeated identical messages count as separate occurrences.
- Expected behavior: Derive compiler-only total and each supported severity count; combined MOD-09 summary remains distinct; group counts cover every associated entry without changing status.
- Expected invalid-case diagnostics: Invalid manual summary (negative/bool/inconsistent totals) raises ValueError; unavailable full SK-11 severity extensions are not invented.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to incomplete result with no diagnostics; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for incomplete result with no diagnostics; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T066 — Filter by severity

- Category: Filtering and Grouping.
- Component / contract: Report filtering/grouping and located MOD-09 helpers.
- Objective: Verify filter by severity while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Typed severity/origin, exact semantic target and artifact projection filters; scheduled phase ID or None; immutable original and located reports.
- Expected behavior: Filters return ordered tuples and never mutate or deduplicate; origin/phase/severity grouping returns MappingProxyType values of tuples; related semantic origins are searchable in compiler projection.
- Expected invalid-case diagnostics: Wrong severity/origin/target/artifact type raises TypeError; malformed phase ID raises ValueError; no general query language or implicit partial artifact matching.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to filter by severity; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for filter by severity; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T067 — Filter by origin

- Category: Filtering and Grouping.
- Component / contract: Report filtering/grouping and located MOD-09 helpers.
- Objective: Verify filter by origin while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Typed severity/origin, exact semantic target and artifact projection filters; scheduled phase ID or None; immutable original and located reports.
- Expected behavior: Filters return ordered tuples and never mutate or deduplicate; origin/phase/severity grouping returns MappingProxyType values of tuples; related semantic origins are searchable in compiler projection.
- Expected invalid-case diagnostics: Wrong severity/origin/target/artifact type raises TypeError; malformed phase ID raises ValueError; no general query language or implicit partial artifact matching.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to filter by origin; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for filter by origin; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T068 — Filter by phase

- Category: Filtering and Grouping.
- Component / contract: Report filtering/grouping and located MOD-09 helpers.
- Objective: Verify filter by phase while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Typed severity/origin, exact semantic target and artifact projection filters; scheduled phase ID or None; immutable original and located reports.
- Expected behavior: Filters return ordered tuples and never mutate or deduplicate; origin/phase/severity grouping returns MappingProxyType values of tuples; related semantic origins are searchable in compiler projection.
- Expected invalid-case diagnostics: Wrong severity/origin/target/artifact type raises TypeError; malformed phase ID raises ValueError; no general query language or implicit partial artifact matching.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to filter by phase; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for filter by phase; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T069 — Filter by semantic target

- Category: Filtering and Grouping.
- Component / contract: Report filtering/grouping and located MOD-09 helpers.
- Objective: Verify filter by semantic target while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Typed severity/origin, exact semantic target and artifact projection filters; scheduled phase ID or None; immutable original and located reports.
- Expected behavior: Filters return ordered tuples and never mutate or deduplicate; origin/phase/severity grouping returns MappingProxyType values of tuples; related semantic origins are searchable in compiler projection.
- Expected invalid-case diagnostics: Wrong severity/origin/target/artifact type raises TypeError; malformed phase ID raises ValueError; no general query language or implicit partial artifact matching.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to filter by semantic target; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for filter by semantic target; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T070 — Filter by artifact target

- Category: Filtering and Grouping.
- Component / contract: Report filtering/grouping and located MOD-09 helpers.
- Objective: Verify filter by artifact target while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Typed severity/origin, exact semantic target and artifact projection filters; scheduled phase ID or None; immutable original and located reports.
- Expected behavior: Filters return ordered tuples and never mutate or deduplicate; origin/phase/severity grouping returns MappingProxyType values of tuples; related semantic origins are searchable in compiler projection.
- Expected invalid-case diagnostics: Wrong severity/origin/target/artifact type raises TypeError; malformed phase ID raises ValueError; no general query language or implicit partial artifact matching.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to filter by artifact target; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for filter by artifact target; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T071 — No report mutation

- Category: Filtering and Grouping.
- Component / contract: Report filtering/grouping and located MOD-09 helpers.
- Objective: Verify no report mutation while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Typed severity/origin, exact semantic target and artifact projection filters; scheduled phase ID or None; immutable original and located reports.
- Expected behavior: Filters return ordered tuples and never mutate or deduplicate; origin/phase/severity grouping returns MappingProxyType values of tuples; related semantic origins are searchable in compiler projection.
- Expected invalid-case diagnostics: Wrong severity/origin/target/artifact type raises TypeError; malformed phase ID raises ValueError; no general query language or implicit partial artifact matching.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no report mutation; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no report mutation; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T072 — Stable grouping

- Category: Filtering and Grouping.
- Component / contract: Report filtering/grouping and located MOD-09 helpers.
- Objective: Verify stable grouping while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Typed severity/origin, exact semantic target and artifact projection filters; scheduled phase ID or None; immutable original and located reports.
- Expected behavior: Filters return ordered tuples and never mutate or deduplicate; origin/phase/severity grouping returns MappingProxyType values of tuples; related semantic origins are searchable in compiler projection.
- Expected invalid-case diagnostics: Wrong severity/origin/target/artifact type raises TypeError; malformed phase ID raises ValueError; no general query language or implicit partial artifact matching.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to stable grouping; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for stable grouping; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T073 — Immutable diagnostic entries

- Category: Immutability and Determinism.
- Component / contract: Frozen associations/reports and finite evidence snapshots.
- Objective: Verify immutable diagnostic entries while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Provide list inputs for related targets/paths, occurrence pairs, prerequisites and result diagnostics; retain originals then mutate caller lists after construction.
- Expected behavior: Internal tuples remain stable; original result, evidence, canonical model and source index unchanged; no time/random/HTTP/database/global state used in reporting.
- Expected invalid-case diagnostics: Assignment to frozen objects and mutation of mapping proxies is rejected; invalid finite-sequence shapes raise TypeError; repeated override indices raise ValueError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to immutable diagnostic entries; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for immutable diagnostic entries; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T074 — Immutable reports

- Category: Immutability and Determinism.
- Component / contract: Frozen associations/reports and finite evidence snapshots.
- Objective: Verify immutable reports while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Provide list inputs for related targets/paths, occurrence pairs, prerequisites and result diagnostics; retain originals then mutate caller lists after construction.
- Expected behavior: Internal tuples remain stable; original result, evidence, canonical model and source index unchanged; no time/random/HTTP/database/global state used in reporting.
- Expected invalid-case diagnostics: Assignment to frozen objects and mutation of mapping proxies is rejected; invalid finite-sequence shapes raise TypeError; repeated override indices raise ValueError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to immutable reports; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for immutable reports; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T075 — Unchanged CompilationResult

- Category: Immutability and Determinism.
- Component / contract: Frozen associations/reports and finite evidence snapshots.
- Objective: Verify unchanged compilationresult while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Provide list inputs for related targets/paths, occurrence pairs, prerequisites and result diagnostics; retain originals then mutate caller lists after construction.
- Expected behavior: Internal tuples remain stable; original result, evidence, canonical model and source index unchanged; no time/random/HTTP/database/global state used in reporting.
- Expected invalid-case diagnostics: Assignment to frozen objects and mutation of mapping proxies is rejected; invalid finite-sequence shapes raise TypeError; repeated override indices raise ValueError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to unchanged compilationresult; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for unchanged compilationresult; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T076 — Unchanged ModelValidationResult

- Category: Immutability and Determinism.
- Component / contract: Frozen associations/reports and finite evidence snapshots.
- Objective: Verify unchanged modelvalidationresult while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Provide list inputs for related targets/paths, occurrence pairs, prerequisites and result diagnostics; retain originals then mutate caller lists after construction.
- Expected behavior: Internal tuples remain stable; original result, evidence, canonical model and source index unchanged; no time/random/HTTP/database/global state used in reporting.
- Expected invalid-case diagnostics: Assignment to frozen objects and mutation of mapping proxies is rejected; invalid finite-sequence shapes raise TypeError; repeated override indices raise ValueError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to unchanged modelvalidationresult; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for unchanged modelvalidationresult; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T077 — Unchanged source index

- Category: Immutability and Determinism.
- Component / contract: Frozen associations/reports and finite evidence snapshots.
- Objective: Verify unchanged source index while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Provide list inputs for related targets/paths, occurrence pairs, prerequisites and result diagnostics; retain originals then mutate caller lists after construction.
- Expected behavior: Internal tuples remain stable; original result, evidence, canonical model and source index unchanged; no time/random/HTTP/database/global state used in reporting.
- Expected invalid-case diagnostics: Assignment to frozen objects and mutation of mapping proxies is rejected; invalid finite-sequence shapes raise TypeError; repeated override indices raise ValueError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to unchanged source index; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for unchanged source index; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T078 — Equivalent inputs produce equivalent reports

- Category: Immutability and Determinism.
- Component / contract: Frozen associations/reports and finite evidence snapshots.
- Objective: Verify equivalent inputs produce equivalent reports while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Provide list inputs for related targets/paths, occurrence pairs, prerequisites and result diagnostics; retain originals then mutate caller lists after construction.
- Expected behavior: Internal tuples remain stable; original result, evidence, canonical model and source index unchanged; no time/random/HTTP/database/global state used in reporting.
- Expected invalid-case diagnostics: Assignment to frozen objects and mutation of mapping proxies is rejected; invalid finite-sequence shapes raise TypeError; repeated override indices raise ValueError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to equivalent inputs produce equivalent reports; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for equivalent inputs produce equivalent reports; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T079 — No mutable global diagnostic registry

- Category: Immutability and Determinism.
- Component / contract: Frozen associations/reports and finite evidence snapshots.
- Objective: Verify no mutable global diagnostic registry while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Provide list inputs for related targets/paths, occurrence pairs, prerequisites and result diagnostics; retain originals then mutate caller lists after construction.
- Expected behavior: Internal tuples remain stable; original result, evidence, canonical model and source index unchanged; no time/random/HTTP/database/global state used in reporting.
- Expected invalid-case diagnostics: Assignment to frozen objects and mutation of mapping proxies is rejected; invalid finite-sequence shapes raise TypeError; repeated override indices raise ValueError.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no mutable global diagnostic registry; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no mutable global diagnostic registry; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T080 — Pure Python diagnostic domain

- Category: Django / DRF.
- Component / contract: Pure Python domain / explicit existing transport.
- Objective: Verify pure python diagnostic domain while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Current repository with no Django/DRF compiler HTTP route; use ModelDiagnosticReporter plus model_diagnostic_report_payload.
- Expected behavior: Keep framework-free diagnostic domain and explicit JSON projection; existing authorized future HTTP consumers must use DRF; no endpoint/serializer/ORM/migration is introduced in this task.
- Expected invalid-case diagnostics: Future HTTP integration is BLOCKED until an applicable endpoint/auth envelope exists; compilation failure must not implicitly choose HTTP 500; no permission bypass.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to pure python diagnostic domain; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for pure python diagnostic domain; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T081 — No ORM persistence

- Category: Django / DRF.
- Component / contract: Pure Python domain / explicit existing transport.
- Objective: Verify no orm persistence while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Current repository with no Django/DRF compiler HTTP route; use ModelDiagnosticReporter plus model_diagnostic_report_payload.
- Expected behavior: Keep framework-free diagnostic domain and explicit JSON projection; existing authorized future HTTP consumers must use DRF; no endpoint/serializer/ORM/migration is introduced in this task.
- Expected invalid-case diagnostics: Future HTTP integration is BLOCKED until an applicable endpoint/auth envelope exists; compilation failure must not implicitly choose HTTP 500; no permission bypass.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no orm persistence; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no orm persistence; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T082 — Existing DRF serializer integration

- Category: Django / DRF.
- Component / contract: Pure Python domain / explicit existing transport.
- Objective: Verify existing drf serializer integration while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Current repository with no Django/DRF compiler HTTP route; use ModelDiagnosticReporter plus model_diagnostic_report_payload.
- Expected behavior: Keep framework-free diagnostic domain and explicit JSON projection; existing authorized future HTTP consumers must use DRF; no endpoint/serializer/ORM/migration is introduced in this task.
- Expected invalid-case diagnostics: Future HTTP integration is BLOCKED until an applicable endpoint/auth envelope exists; compilation failure must not implicitly choose HTTP 500; no permission bypass.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to existing drf serializer integration; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for existing drf serializer integration; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T083 — HTTP status versus compilation status

- Category: Django / DRF.
- Component / contract: Pure Python domain / explicit existing transport.
- Objective: Verify http status versus compilation status while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Current repository with no Django/DRF compiler HTTP route; use ModelDiagnosticReporter plus model_diagnostic_report_payload.
- Expected behavior: Keep framework-free diagnostic domain and explicit JSON projection; existing authorized future HTTP consumers must use DRF; no endpoint/serializer/ORM/migration is introduced in this task.
- Expected invalid-case diagnostics: Future HTTP integration is BLOCKED until an applicable endpoint/auth envelope exists; compilation failure must not implicitly choose HTTP 500; no permission bypass.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to http status versus compilation status; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for http status versus compilation status; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T084 — Existing permissions preserved

- Category: Django / DRF.
- Component / contract: Pure Python domain / explicit existing transport.
- Objective: Verify existing permissions preserved while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Current repository with no Django/DRF compiler HTTP route; use ModelDiagnosticReporter plus model_diagnostic_report_payload.
- Expected behavior: Keep framework-free diagnostic domain and explicit JSON projection; existing authorized future HTTP consumers must use DRF; no endpoint/serializer/ORM/migration is introduced in this task.
- Expected invalid-case diagnostics: Future HTTP integration is BLOCKED until an applicable endpoint/auth envelope exists; compilation failure must not implicitly choose HTTP 500; no permission bypass.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to existing permissions preserved; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for existing permissions preserved; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T085 — No unnecessary REST endpoint

- Category: Django / DRF.
- Component / contract: Pure Python domain / explicit existing transport.
- Objective: Verify no unnecessary rest endpoint while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Current repository with no Django/DRF compiler HTTP route; use ModelDiagnosticReporter plus model_diagnostic_report_payload.
- Expected behavior: Keep framework-free diagnostic domain and explicit JSON projection; existing authorized future HTTP consumers must use DRF; no endpoint/serializer/ORM/migration is introduced in this task.
- Expected invalid-case diagnostics: Future HTTP integration is BLOCKED until an applicable endpoint/auth envelope exists; compilation failure must not implicitly choose HTTP 500; no permission bypass.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no unnecessary rest endpoint; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no unnecessary rest endpoint; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T086 — Safe API representation

- Category: Django / DRF.
- Component / contract: Pure Python domain / explicit existing transport.
- Objective: Verify safe api representation while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Current repository with no Django/DRF compiler HTTP route; use ModelDiagnosticReporter plus model_diagnostic_report_payload.
- Expected behavior: Keep framework-free diagnostic domain and explicit JSON projection; existing authorized future HTTP consumers must use DRF; no endpoint/serializer/ORM/migration is introduced in this task.
- Expected invalid-case diagnostics: Future HTTP integration is BLOCKED until an applicable endpoint/auth envelope exists; compilation failure must not implicitly choose HTTP 500; no permission bypass.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to safe api representation; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for safe api representation; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T087 — No source-controlled message execution

- Category: Security.
- Component / contract: model_diagnostic_report_payload disclosure controls.
- Objective: Verify no source-controlled message execution while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original diagnostic message containing code-looking text/path-looking text and bounded artifact metadata; request default and explicitly authorized disclosure booleans.
- Expected behavior: No message evaluation, stack capture, filesystem access or arbitrary repr; defaults hide text/source/semantic/artifact identities; actual field allowlist excludes physical filename/content/trace; caller authorizes opt-in details.
- Expected invalid-case diagnostics: Nonboolean flags or wrong report raises TypeError; opt-in messages/source IDs may contain sensitive author content and require existing caller permissions/redaction; formatter is not a secret scanner.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no source-controlled message execution; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no source-controlled message execution; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T088 — No stack trace leakage

- Category: Security.
- Component / contract: model_diagnostic_report_payload disclosure controls.
- Objective: Verify no stack trace leakage while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original diagnostic message containing code-looking text/path-looking text and bounded artifact metadata; request default and explicitly authorized disclosure booleans.
- Expected behavior: No message evaluation, stack capture, filesystem access or arbitrary repr; defaults hide text/source/semantic/artifact identities; actual field allowlist excludes physical filename/content/trace; caller authorizes opt-in details.
- Expected invalid-case diagnostics: Nonboolean flags or wrong report raises TypeError; opt-in messages/source IDs may contain sensitive author content and require existing caller permissions/redaction; formatter is not a secret scanner.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no stack trace leakage; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no stack trace leakage; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T089 — No credentials in diagnostic reports

- Category: Security.
- Component / contract: model_diagnostic_report_payload disclosure controls.
- Objective: Verify no credentials in diagnostic reports while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original diagnostic message containing code-looking text/path-looking text and bounded artifact metadata; request default and explicitly authorized disclosure booleans.
- Expected behavior: No message evaluation, stack capture, filesystem access or arbitrary repr; defaults hide text/source/semantic/artifact identities; actual field allowlist excludes physical filename/content/trace; caller authorizes opt-in details.
- Expected invalid-case diagnostics: Nonboolean flags or wrong report raises TypeError; opt-in messages/source IDs may contain sensitive author content and require existing caller permissions/redaction; formatter is not a secret scanner.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no credentials in diagnostic reports; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no credentials in diagnostic reports; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T090 — No unrestricted absolute path exposure

- Category: Security.
- Component / contract: model_diagnostic_report_payload disclosure controls.
- Objective: Verify no unrestricted absolute path exposure while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original diagnostic message containing code-looking text/path-looking text and bounded artifact metadata; request default and explicitly authorized disclosure booleans.
- Expected behavior: No message evaluation, stack capture, filesystem access or arbitrary repr; defaults hide text/source/semantic/artifact identities; actual field allowlist excludes physical filename/content/trace; caller authorizes opt-in details.
- Expected invalid-case diagnostics: Nonboolean flags or wrong report raises TypeError; opt-in messages/source IDs may contain sensitive author content and require existing caller permissions/redaction; formatter is not a secret scanner.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no unrestricted absolute path exposure; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no unrestricted absolute path exposure; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T091 — No unauthorized model information disclosure

- Category: Security.
- Component / contract: model_diagnostic_report_payload disclosure controls.
- Objective: Verify no unauthorized model information disclosure while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original diagnostic message containing code-looking text/path-looking text and bounded artifact metadata; request default and explicitly authorized disclosure booleans.
- Expected behavior: No message evaluation, stack capture, filesystem access or arbitrary repr; defaults hide text/source/semantic/artifact identities; actual field allowlist excludes physical filename/content/trace; caller authorizes opt-in details.
- Expected invalid-case diagnostics: Nonboolean flags or wrong report raises TypeError; opt-in messages/source IDs may contain sensitive author content and require existing caller permissions/redaction; formatter is not a secret scanner.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no unauthorized model information disclosure; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no unauthorized model information disclosure; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T092 — Validation-not-ready report

- Category: Mini Sales.
- Component / contract: Documented Mini Sales integration.
- Objective: Verify validation-not-ready report while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Existing sales.Customer@1.0.0 with name/active/creditLimit fields and MOD-08 evidence; specified gate/phase/conflict results and canonical source association.
- Expected behavior: Produce reports preserving Customer exact identity when explicitly supplied, failure/readiness/status and original conflict key/related sources; default build remains incomplete with zero successful artifacts.
- Expected invalid-case diagnostics: Actual CMP-002, CMP-007, CMP-009 and phase CMP-008 retained when present; future artifact generator fixtures are unavailable and must be supplied before scenario execution.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to validation-not-ready report; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for validation-not-ready report; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T093 — Missing compiler phase report

- Category: Mini Sales.
- Component / contract: Documented Mini Sales integration.
- Objective: Verify missing compiler phase report while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Existing sales.Customer@1.0.0 with name/active/creditLimit fields and MOD-08 evidence; specified gate/phase/conflict results and canonical source association.
- Expected behavior: Produce reports preserving Customer exact identity when explicitly supplied, failure/readiness/status and original conflict key/related sources; default build remains incomplete with zero successful artifacts.
- Expected invalid-case diagnostics: Actual CMP-002, CMP-007, CMP-009 and phase CMP-008 retained when present; future artifact generator fixtures are unavailable and must be supplied before scenario execution.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to missing compiler phase report; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for missing compiler phase report; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T094 — Artifact identity conflict

- Category: Mini Sales.
- Component / contract: Documented Mini Sales integration.
- Objective: Verify artifact identity conflict while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Existing sales.Customer@1.0.0 with name/active/creditLimit fields and MOD-08 evidence; specified gate/phase/conflict results and canonical source association.
- Expected behavior: Produce reports preserving Customer exact identity when explicitly supplied, failure/readiness/status and original conflict key/related sources; default build remains incomplete with zero successful artifacts.
- Expected invalid-case diagnostics: Actual CMP-002, CMP-007, CMP-009 and phase CMP-008 retained when present; future artifact generator fixtures are unavailable and must be supplied before scenario execution.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to artifact identity conflict; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for artifact identity conflict; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T095 — Failed compiler phase

- Category: Mini Sales.
- Component / contract: Documented Mini Sales integration.
- Objective: Verify failed compiler phase while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Existing sales.Customer@1.0.0 with name/active/creditLimit fields and MOD-08 evidence; specified gate/phase/conflict results and canonical source association.
- Expected behavior: Produce reports preserving Customer exact identity when explicitly supplied, failure/readiness/status and original conflict key/related sources; default build remains incomplete with zero successful artifacts.
- Expected invalid-case diagnostics: Actual CMP-002, CMP-007, CMP-009 and phase CMP-008 retained when present; future artifact generator fixtures are unavailable and must be supplied before scenario execution.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to failed compiler phase; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for failed compiler phase; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T096 — Semantic Customer association

- Category: Mini Sales.
- Component / contract: Documented Mini Sales integration.
- Objective: Verify semantic customer association while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Existing sales.Customer@1.0.0 with name/active/creditLimit fields and MOD-08 evidence; specified gate/phase/conflict results and canonical source association.
- Expected behavior: Produce reports preserving Customer exact identity when explicitly supplied, failure/readiness/status and original conflict key/related sources; default build remains incomplete with zero successful artifacts.
- Expected invalid-case diagnostics: Actual CMP-002, CMP-007, CMP-009 and phase CMP-008 retained when present; future artifact generator fixtures are unavailable and must be supplied before scenario execution.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to semantic customer association; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for semantic customer association; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T097 — No fabricated compiled artifact

- Category: Mini Sales.
- Component / contract: Documented Mini Sales integration.
- Objective: Verify no fabricated compiled artifact while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Existing sales.Customer@1.0.0 with name/active/creditLimit fields and MOD-08 evidence; specified gate/phase/conflict results and canonical source association.
- Expected behavior: Produce reports preserving Customer exact identity when explicitly supplied, failure/readiness/status and original conflict key/related sources; default build remains incomplete with zero successful artifacts.
- Expected invalid-case diagnostics: Actual CMP-002, CMP-007, CMP-009 and phase CMP-008 retained when present; future artifact generator fixtures are unavailable and must be supplied before scenario execution.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no fabricated compiled artifact; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no fabricated compiled artifact; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T098 — No semantic rule implementation

- Category: Architectural Boundaries.
- Component / contract: Architectural dependency and responsibility boundaries.
- Objective: Verify no semantic rule implementation while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Inspect current module manifest/import graph and invoke only reporting in future authorized execution with recording collaborators.
- Expected behavior: Reporting never validates, resolves, canonicalizes, schedules/executes phases, creates artifacts, deploys, runs runtime or persists diagnostics; existing architecture graph unchanged.
- Expected invalid-case diagnostics: Illegal dependency or side-effect requirement is a future acceptance failure; malformed production collaborator exceptions are not converted to stack-bearing diagnostics.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no semantic rule implementation; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no semantic rule implementation; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T099 — No namespace resolution

- Category: Architectural Boundaries.
- Component / contract: Architectural dependency and responsibility boundaries.
- Objective: Verify no namespace resolution while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Inspect current module manifest/import graph and invoke only reporting in future authorized execution with recording collaborators.
- Expected behavior: Reporting never validates, resolves, canonicalizes, schedules/executes phases, creates artifacts, deploys, runs runtime or persists diagnostics; existing architecture graph unchanged.
- Expected invalid-case diagnostics: Illegal dependency or side-effect requirement is a future acceptance failure; malformed production collaborator exceptions are not converted to stack-bearing diagnostics.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no namespace resolution; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no namespace resolution; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T100 — No canonicalization

- Category: Architectural Boundaries.
- Component / contract: Architectural dependency and responsibility boundaries.
- Objective: Verify no canonicalization while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Inspect current module manifest/import graph and invoke only reporting in future authorized execution with recording collaborators.
- Expected behavior: Reporting never validates, resolves, canonicalizes, schedules/executes phases, creates artifacts, deploys, runs runtime or persists diagnostics; existing architecture graph unchanged.
- Expected invalid-case diagnostics: Illegal dependency or side-effect requirement is a future acceptance failure; malformed production collaborator exceptions are not converted to stack-bearing diagnostics.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no canonicalization; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no canonicalization; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T101 — No compiler phase execution

- Category: Architectural Boundaries.
- Component / contract: Architectural dependency and responsibility boundaries.
- Objective: Verify no compiler phase execution while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Inspect current module manifest/import graph and invoke only reporting in future authorized execution with recording collaborators.
- Expected behavior: Reporting never validates, resolves, canonicalizes, schedules/executes phases, creates artifacts, deploys, runs runtime or persists diagnostics; existing architecture graph unchanged.
- Expected invalid-case diagnostics: Illegal dependency or side-effect requirement is a future acceptance failure; malformed production collaborator exceptions are not converted to stack-bearing diagnostics.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no compiler phase execution; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no compiler phase execution; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T102 — No artifact construction

- Category: Architectural Boundaries.
- Component / contract: Architectural dependency and responsibility boundaries.
- Objective: Verify no artifact construction while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Inspect current module manifest/import graph and invoke only reporting in future authorized execution with recording collaborators.
- Expected behavior: Reporting never validates, resolves, canonicalizes, schedules/executes phases, creates artifacts, deploys, runs runtime or persists diagnostics; existing architecture graph unchanged.
- Expected invalid-case diagnostics: Illegal dependency or side-effect requirement is a future acceptance failure; malformed production collaborator exceptions are not converted to stack-bearing diagnostics.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no artifact construction; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no artifact construction; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T103 — No deployment

- Category: Architectural Boundaries.
- Component / contract: Architectural dependency and responsibility boundaries.
- Objective: Verify no deployment while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Inspect current module manifest/import graph and invoke only reporting in future authorized execution with recording collaborators.
- Expected behavior: Reporting never validates, resolves, canonicalizes, schedules/executes phases, creates artifacts, deploys, runs runtime or persists diagnostics; existing architecture graph unchanged.
- Expected invalid-case diagnostics: Illegal dependency or side-effect requirement is a future acceptance failure; malformed production collaborator exceptions are not converted to stack-bearing diagnostics.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no deployment; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no deployment; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T104 — No runtime execution

- Category: Architectural Boundaries.
- Component / contract: Architectural dependency and responsibility boundaries.
- Objective: Verify no runtime execution while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Inspect current module manifest/import graph and invoke only reporting in future authorized execution with recording collaborators.
- Expected behavior: Reporting never validates, resolves, canonicalizes, schedules/executes phases, creates artifacts, deploys, runs runtime or persists diagnostics; existing architecture graph unchanged.
- Expected invalid-case diagnostics: Illegal dependency or side-effect requirement is a future acceptance failure; malformed production collaborator exceptions are not converted to stack-bearing diagnostics.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no runtime execution; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no runtime execution; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T105 — No new diagnostic persistence

- Category: Architectural Boundaries.
- Component / contract: Architectural dependency and responsibility boundaries.
- Objective: Verify no new diagnostic persistence while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Inspect current module manifest/import graph and invoke only reporting in future authorized execution with recording collaborators.
- Expected behavior: Reporting never validates, resolves, canonicalizes, schedules/executes phases, creates artifacts, deploys, runs runtime or persists diagnostics; existing architecture graph unchanged.
- Expected invalid-case diagnostics: Illegal dependency or side-effect requirement is a future acceptance failure; malformed production collaborator exceptions are not converted to stack-bearing diagnostics.
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no new diagnostic persistence; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no new diagnostic persistence; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T106 — Occurrence override outside result

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify occurrence override outside result while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Context index equal to diagnostic count.
- Expected behavior: ValueError before report creation.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to occurrence override outside result; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for occurrence override outside result; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T107 — Negative occurrence index

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify negative occurrence index while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Context pair (-1, valid association).
- Expected behavior: TypeError, no indexing from end.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to negative occurrence index; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for negative occurrence index; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T108 — Boolean occurrence index

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify boolean occurrence index while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Context pair (True, valid association).
- Expected behavior: TypeError, boolean is not an integer coordinate.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to boolean occurrence index; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for boolean occurrence index; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T109 — Duplicate occurrence index

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify duplicate occurrence index while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Two context pairs for the same index.
- Expected behavior: ValueError, no last-write-wins.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to duplicate occurrence index; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for duplicate occurrence index; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T110 — Malformed override pair

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify malformed override pair while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Dict, one-item pair or three-item pair.
- Expected behavior: TypeError, no arbitrary metadata context.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to malformed override pair; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for malformed override pair; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T111 — Existing producer association conflict

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify existing producer association conflict while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Override changes original association origin/target.
- Expected behavior: ValueError, original producer evidence retained.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to existing producer association conflict; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for existing producer association conflict; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T112 — Exact semantic target conflict

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify exact semantic target conflict while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original diagnostic reference differs from association reference.
- Expected behavior: ValueError, no semantic relabeling.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to exact semantic target conflict; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for exact semantic target conflict; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T113 — Phase association conflict

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify phase association conflict while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original phase_id differs from association phase_id.
- Expected behavior: ValueError, no producer phase substitution.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to phase association conflict; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for phase association conflict; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T114 — Too few repeated occurrences

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify too few repeated occurrences while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: One diagnostic object occurs twice in phase outcomes but once in result.
- Expected behavior: CompilationResult ValueError; no lossy set-membership acceptance.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to too few repeated occurrences; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for too few repeated occurrences; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T115 — Equal replacement is not original occurrence

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify equal replacement is not original occurrence while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Distinct equal-valued diagnostic in result instead of original phase object.
- Expected behavior: CompilationResult ValueError; preserve original phase payload identity.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to equal replacement is not original occurrence; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for equal replacement is not original occurrence; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T116 — Repeated same object is lossless

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify repeated same object is lossless while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Same original payload occurs twice in one phase and twice in result.
- Expected behavior: Both occurrences retained and counted; no identity deduplication.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to repeated same object is lossless; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for repeated same object is lossless; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T117 — Shared payload across phases

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify shared payload across phases while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Same original diagnostic without phase_id reused by two actual outcomes and twice in result.
- Expected behavior: Assign earliest unmatched occurrence in actual outcome order; preserve both phase owners.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to shared payload across phases; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for shared payload across phases; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T118 — Nonexecuted phase association

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify nonexecuted phase association while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Orchestrator unavailable outcome has executed=False and PHASE association.
- Expected behavior: ValueError, not phase execution evidence.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to nonexecuted phase association; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for nonexecuted phase association; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T119 — Legacy execution uncertainty

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify legacy execution uncertainty while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Manually created historical phase outcome executed=None.
- Expected behavior: Project None; never infer execution from status alone.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to legacy execution uncertainty; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for legacy execution uncertainty; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T120 — Prerequisite scope association

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify prerequisite scope association while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Context mismatch diagnostic plus explicit actual request SemanticContextRef.
- Expected behavior: Retain scope association without changing CanonicalModel or evidence.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to prerequisite scope association; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for prerequisite scope association; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T121 — Null compiler target

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify null compiler target while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Invalid root input result has target=None.
- Expected behavior: Report failed original status with no invented target.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to null compiler target; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for null compiler target; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T122 — Kind-only artifact construction

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify kind-only artifact construction while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Explicit intended artifact kind with actual executed phase but no candidate artifact.
- Expected behavior: Retain association; count stays original final output count.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to kind-only artifact construction; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for kind-only artifact construction; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T123 — Target-only artifact association

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify target-only artifact association while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Only BUILD_TARGET and artifact-construction origin with actual phase.
- Expected behavior: Retain intended target without invented key/kind/artifact.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to target-only artifact association; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for target-only artifact association; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T124 — Artifact key lexical boundary

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify artifact key lexical boundary while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Existing typed key at maximum 160 chars and invalid 161 chars.
- Expected behavior: Use compiled-contracts validation; valid original projection retained, invalid key rejected.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to artifact key lexical boundary; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for artifact key lexical boundary; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T125 — Artifact kind lexical boundary

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify artifact kind lexical boundary while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Existing typed kind at maximum 80 chars and invalid 81 chars.
- Expected behavior: Use compiled-contracts validation; no diagnostic-only alternate identity policy.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to artifact kind lexical boundary; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for artifact kind lexical boundary; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T126 — Colliding candidates have no arbitrary primary

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify colliding candidates have no arbitrary primary while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Conflict candidates share key and multiple semantic dependencies.
- Expected behavior: All related exact definitions retained in candidate/dependency order; primary absent unless explicitly provided.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to colliding candidates have no arbitrary primary; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for colliding candidates have no arbitrary primary; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T127 — Missing related source mapping

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify missing related source mapping while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Related targets include one mapped and one unmapped exact definition.
- Expected behavior: Keep every semantic related target; emit only reliable related authoring paths, no guessed span for missing target.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to missing related source mapping; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for missing related source mapping; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T128 — Explicit source path precedence

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify explicit source path precedence while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Caller supplies field expression path and broader canonical declaration path exists.
- Expected behavior: Preserve explicit expression path; do not replace it with declaration fallback.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to explicit source path precedence; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for explicit source path precedence; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T129 — Ambiguous canonical source association

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify ambiguous canonical source association while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Same exact target maps to two distinct authoring paths.
- Expected behavior: Mapping unavailable; original diagnostic/target preserved.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to ambiguous canonical source association; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for ambiguous canonical source association; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T130 — Historical projection missing compiler details

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify historical projection missing compiler details while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Existing ModelDiagnosticEntry compiler extension has no details.
- Expected behavior: Keep entry; origin grouping includes None and phase grouping preserves legacy explicit phase ID.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to historical projection missing compiler details; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for historical projection missing compiler details; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T131 — Compiler and combined summary differ

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify compiler and combined summary differ while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Original validation error plus compiler warning.
- Expected behavior: Compiler summary counts only warning; combined MOD-09 summary also counts validation error; original statuses unchanged.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to compiler and combined summary differ; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for compiler and combined summary differ; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T132 — Default artifact disclosure

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify default artifact disclosure while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Artifact association exists and default payload options used.
- Expected behavior: No artifact key/kind/target payload; count is exposed only as producer membership.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to default artifact disclosure; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for default artifact disclosure; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T133 — Authorized artifact disclosure

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify authorized artifact disclosure while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: include_artifact_targets=True with approved caller authorization.
- Expected behavior: Allowlisted key/kind/target only; no payload/path or publication claims.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to authorized artifact disclosure; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for authorized artifact disclosure; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T134 — Artifact disclosure boolean guard

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify artifact disclosure boolean guard while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: include_artifact_targets=1 or text.
- Expected behavior: TypeError; no truthiness-based exposure.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to artifact disclosure boolean guard; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for artifact disclosure boolean guard; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T135 — Report non-success positive artifact count

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify report non-success positive artifact count while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: failed/incomplete projection with artifact_count=1.
- Expected behavior: ValueError, no successful artifacts on unsuccessful result.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to report non-success positive artifact count; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for report non-success positive artifact count; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T136 — Report legacy unavailable artifact count

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify report legacy unavailable artifact count while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Historical projection default artifact_count=None.
- Expected behavior: Represent unavailable count as None, not invented zero.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to report legacy unavailable artifact count; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for report legacy unavailable artifact count; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

## CMP-02-T137 — No result reconstruction from filters

- Category: Additional contract and edge coverage.
- Component / contract: CMP-02 association / reporting / explicit transport.
- Objective: Verify no result reconstruction from filters while preserving original diagnostic semantics and authoritative compiler state.
- Prerequisites: Explicit later test authorization, fixed repository revision, actual CMP-01/MOD-08/MOD-09 fixtures and upstream contracts needed for this scenario; source scenarios require MOD-03 indexes; artifact scenarios require actual compiled-contracts tokens.
- Inputs / setup: Filter all entries from a failed/incomplete report.
- Expected behavior: Return empty tuple; retain original status/phase outcomes/evidence.
- Expected invalid-case diagnostics: Apply the stated TypeError/ValueError guard where invalid; valid cases retain original diagnostic and no synthesized validation result..
- Boundary / edge cases: Include absence of optional evidence, empty and repeated occurrences, exact-version distinctions, invalid typed values and caller-list mutation when applicable to no result reconstruction from filters; retain unavailable evidence explicitly, never invent it.
- Integration dependencies: CMP-01 producer, MOD-09 domain envelope, MOD-03/model-loader enrichment, MOD-04 canonical ownership, MOD-08 original validation evidence; missing general SK-11 or HTTP contracts must be recorded as blocked where applicable.
- Acceptance criteria: Observe the stated behavior for no result reconstruction from filters; original code/message/severity/status and all input objects remain unchanged; ordering, count and disclosure checks match the documented contract; capture actual evidence before assigning any executed status.
- Execution status: NOT_RUN — DEFERRED

