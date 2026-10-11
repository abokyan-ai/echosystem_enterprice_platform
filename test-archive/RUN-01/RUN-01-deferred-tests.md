# RUN-01 — Deferred Test Specification

Task: RUN-01 — Runtime Artifact Loader

Backend: Python / Django / Django REST Framework

Status: NOT_RUN — DEFERRED

New Tests Implemented: 0

Tests Executed: 0

Date: 2026-10-11

Dependencies:
- SK-01
- SK-04
- SK-07
- SK-08
- SK-11
- TYPE-02 / TYPE-03 / TYPE-04 / TYPE-05 / TYPE-08 (where actually available)
- MOD-04
- MOD-08
- CMP-01
- CMP-02
- CMP-06
- CMP-07
- CMP-08
- CMP-09

## Scope, prerequisites and limitations

This sole RUN-01 archive specifies future verification; it is not execution evidence. See [implementation contract](../../docs/runtime/runtime-artifact-loader.md), [ADR-0042](../../docs/architecture/decisions/ADR-0042-runtime-artifact-loader.md) and [static completion report](../../docs/architecture/run01-verification.md). No executable fixture, test infrastructure, archive README or extra archive Markdown is created. Historical executed tests/records stay intact.

Future execution requires explicit later user authorization, a fixed repository revision, actual original accepted CMP output/manifest/committed receipt/approved source, verified digest evidence, controlled trusted authorizer and genuine approved format/encoder/decoder before positive domain-format scenarios. Those producer/decoder/authority integrations do not exist today. No sample wire format or fabricated runtime artifact is authorized by this archive. Django/DRF are selected but NOT_INSTALLED; HTTP scenarios additionally require a genuine authenticated workflow. Full SK-11/TYPE-01/SemanticInstance are unavailable prerequisites, not invented replacements.

Baseline P: actual CMP-07 V0 complete artifact-build manifest, same original compilation association and bound validation, complete CMP-08 committed receipt with explicit SHA-256, CMP-09 ALL selection/logical approved source, typed runtime context/server limits, exact trusted authorizer decision, real bounded approved decoder and frozen concrete representations. P is a future controlled fixture prerequisite, not a fixture produced/run during RUN-01. Unless testing absent prerequisites, vary only the named input and keep the rest of P valid. Expected construction rejections are distinguished from returned runtime load results.

All security/source-format execution must use controlled future fixtures and existing approved reader protections, never arbitrary real user files. Pure source/doc review scenarios are also archived NOT_RUN; current syntax/architecture checks are separately reported and never counted as these cases.

## A. Loader Contract

### RUN-01-T001 — Valid loader invocation

- **Test ID:** RUN-01-T001
- **Scenario:** Valid loader invocation.
- **Objective:** Establish the valid loader invocation requirement without weakening authority, integrity or runtime boundaries.
- **Component:** loader/request.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Construct the actual typed application/core request with manifest V0, ALL selection and explicit runtime context; vary the named request/target field or injected port. Scenario-specific variation: Valid loader invocation.
- **Expected Result:** Positive invocation proceeds only with actual approved prerequisites; malformed request is FAILED without reading or decoding. Named requirement: Valid loader invocation.
- **Expected Diagnostics:** RUN-001 for invalid roots; constructor TypeError for invalid nested contract; RUN-013 for mismatched target.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** A. Loader Contract; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T002 — Invalid request

- **Test ID:** RUN-01-T002
- **Scenario:** Invalid request.
- **Objective:** Establish the invalid request requirement without weakening authority, integrity or runtime boundaries.
- **Component:** loader/request.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Pass None, dict, bool and SemanticIREnvelope as the loader/application request root.
- **Expected Result:** FAILED with no read/decoder invocation or loaded set.
- **Expected Diagnostics:** RUN-001.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** A. Loader Contract; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T003 — Missing load context

- **Test ID:** RUN-01-T003
- **Scenario:** Missing load context.
- **Objective:** Establish the missing load context requirement without weakening authority, integrity or runtime boundaries.
- **Component:** loader/request.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Attempt typed construction without RuntimeArtifactLoadContext or with None/raw dictionary.
- **Expected Result:** Construction rejects the malformed request; no runtime effects.
- **Expected Diagnostics:** TypeError, no fabricated load success.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** A. Loader Contract; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T004 — Unsupported runtime target

- **Test ID:** RUN-01-T004
- **Scenario:** Unsupported runtime target.
- **Objective:** Establish the unsupported runtime target requirement without weakening authority, integrity or runtime boundaries.
- **Component:** loader/request.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Request a runtime target absent from the approved decoder registrations while the producer declaration identifies an exact target.
- **Expected Result:** INCOMPLETE for unavailable support; FAILED when declaration and context disagree.
- **Expected Diagnostics:** RUN-013.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** A. Loader Contract; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T005 — Pure Python independence

- **Test ID:** RUN-01-T005
- **Scenario:** Pure Python independence.
- **Objective:** Establish the pure python independence requirement without weakening authority, integrity or runtime boundaries.
- **Component:** loader/request.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Construct the actual typed application/core request with manifest V0, ALL selection and explicit runtime context; vary the named request/target field or injected port. Scenario-specific variation: Pure Python independence.
- **Expected Result:** Positive invocation proceeds only with actual approved prerequisites; malformed request is FAILED without reading or decoding. Named requirement: Pure Python independence.
- **Expected Diagnostics:** RUN-001 for invalid roots; constructor TypeError for invalid nested contract; RUN-013 for mismatched target.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** A. Loader Contract; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T006 — No arbitrary decoder invocation

- **Test ID:** RUN-01-T006
- **Scenario:** No arbitrary decoder invocation.
- **Objective:** Establish the no arbitrary decoder invocation requirement without weakening authority, integrity or runtime boundaries.
- **Component:** loader/request.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Construct the actual typed application/core request with manifest V0, ALL selection and explicit runtime context; vary the named request/target field or injected port. Scenario-specific variation: No arbitrary decoder invocation.
- **Expected Result:** Positive invocation proceeds only with actual approved prerequisites; malformed request is FAILED without reading or decoding. Named requirement: No arbitrary decoder invocation.
- **Expected Diagnostics:** RUN-001 for invalid roots; constructor TypeError for invalid nested contract; RUN-013 for mismatched target.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** A. Loader Contract; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## B. Authorization Prerequisites

### RUN-01-T007 — Valid trusted authorization evidence

- **Test ID:** RUN-01-T007
- **Scenario:** Valid trusted authorization evidence.
- **Objective:** Establish the valid trusted authorization evidence requirement without weakening authority, integrity or runtime boundaries.
- **Component:** authorization port.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Injected authenticated authorizer issues the exact same binding object/context and full ordered selected keys with non-secret source/decision references.
- **Expected Result:** Authorization succeeds only for that invocation; later support/read/decode gates remain mandatory.
- **Expected Diagnostics:** None for authority gate.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** B. Authorization Prerequisites; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T008 — Missing authorization evidence

- **Test ID:** RUN-01-T008
- **Scenario:** Missing authorization evidence.
- **Objective:** Establish the missing authorization evidence requirement without weakening authority, integrity or runtime boundaries.
- **Component:** authorization port.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use UnavailableRuntimeArtifactLoadAuthorizer with otherwise valid digest-bound preflight evidence.
- **Expected Result:** INCOMPLETE before source.read or any decoder is called; no loaded set.
- **Expected Diagnostics:** RUN-002, AUTHORIZATION stage.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** B. Authorization Prerequisites; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T009 — Mismatched manifest authorization scope

- **Test ID:** RUN-01-T009
- **Scenario:** Mismatched manifest authorization scope.
- **Objective:** Establish the mismatched manifest authorization scope requirement without weakening authority, integrity or runtime boundaries.
- **Component:** authorization port.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use a trusted authenticated authorizer tied to the exact bridge binding, original semantic scope/runtime target and ordered full selected keys; vary only the named evidence association. Scenario-specific variation: Mismatched manifest authorization scope.
- **Expected Result:** Only the matching trusted decision permits loading; unavailable authority is INCOMPLETE and invalid/broader association is FAILED; no activation. Named requirement: Mismatched manifest authorization scope.
- **Expected Diagnostics:** RUN-002 unavailable, RUN-003 mismatched/Boolean decision, no diagnostic for a valid decision.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** B. Authorization Prerequisites; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T010 — Mismatched runtime target

- **Test ID:** RUN-01-T010
- **Scenario:** Mismatched runtime target.
- **Objective:** Establish the mismatched runtime target requirement without weakening authority, integrity or runtime boundaries.
- **Component:** authorization port.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use a trusted authenticated authorizer tied to the exact bridge binding, original semantic scope/runtime target and ordered full selected keys; vary only the named evidence association. Scenario-specific variation: Mismatched runtime target.
- **Expected Result:** Only the matching trusted decision permits loading; unavailable authority is INCOMPLETE and invalid/broader association is FAILED; no activation. Named requirement: Mismatched runtime target.
- **Expected Diagnostics:** RUN-002 unavailable, RUN-003 mismatched/Boolean decision, no diagnostic for a valid decision.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** B. Authorization Prerequisites; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T011 — Unauthorized artifact selection

- **Test ID:** RUN-01-T011
- **Scenario:** Unauthorized artifact selection.
- **Objective:** Establish the unauthorized artifact selection requirement without weakening authority, integrity or runtime boundaries.
- **Component:** authorization port.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Authorizer returns a strict subset, extra key, reordered or repeated key inventory for the requested ALL set.
- **Expected Result:** FAILED; no wider/narrower permission is silently accepted.
- **Expected Diagnostics:** RUN-003, or authority constructor rejection for duplicates.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** B. Authorization Prerequisites; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T012 — Rejection of caller-supplied Boolean authorization

- **Test ID:** RUN-01-T012
- **Scenario:** Rejection of caller-supplied Boolean authorization.
- **Objective:** Establish the rejection of caller-supplied boolean authorization requirement without weakening authority, integrity or runtime boundaries.
- **Component:** authorization port.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Authorizer returns True or caller attempts an authorized=True request option.
- **Expected Result:** True is rejected as a decision; unsupported request option is a constructor error; no byte access.
- **Expected Diagnostics:** RUN-003 or constructor TypeError.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** B. Authorization Prerequisites; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T013 — No activation from load authorization

- **Test ID:** RUN-01-T013
- **Scenario:** No activation from load authorization.
- **Objective:** Establish the no activation from load authorization requirement without weakening authority, integrity or runtime boundaries.
- **Component:** authorization port.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use a trusted authenticated authorizer tied to the exact bridge binding, original semantic scope/runtime target and ordered full selected keys; vary only the named evidence association. Scenario-specific variation: No activation from load authorization.
- **Expected Result:** Only the matching trusted decision permits loading; unavailable authority is INCOMPLETE and invalid/broader association is FAILED; no activation. Named requirement: No activation from load authorization.
- **Expected Diagnostics:** RUN-002 unavailable, RUN-003 mismatched/Boolean decision, no diagnostic for a valid decision.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** B. Authorization Prerequisites; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## C. Manifest Integrity

### RUN-01-T014 — Valid CMP-07 manifest

- **Test ID:** RUN-01-T014
- **Scenario:** Valid CMP-07 manifest.
- **Objective:** Establish the valid cmp-07 manifest requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP manifest / bridge planning.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use original completed artifact output association, original V0 manifest and descriptors exactly as captured by CMP-07.
- **Expected Result:** Existing CMP planning accepts its associations without executing the compiler; runtime authority/support still required.
- **Expected Diagnostics:** No manifest failure; default missing authority/decoder is accurately reported later.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** C. Manifest Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T015 — Unsupported manifest schema version

- **Test ID:** RUN-01-T015
- **Scenario:** Unsupported manifest schema version.
- **Objective:** Establish the unsupported manifest schema version requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP manifest / bridge planning.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use an actual completed original CMP artifact-build association and manifest, then vary the named schema/context/target/member coordinate without reconstructing it from storage. Scenario-specific variation: Unsupported manifest schema version.
- **Expected Result:** Only original complete manifest V0 and exact association survive preflight; malformed declarations expose no bytes/loaded set. Named requirement: Unsupported manifest schema version.
- **Expected Diagnostics:** RUN-004 with original CMP manifest causes; RUN-014 context; duplicate constructor rejection/original CMP-041; no diagnostics on accepted facts.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** C. Manifest Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T016 — Manifest context mismatch

- **Test ID:** RUN-01-T016
- **Scenario:** Manifest context mismatch.
- **Objective:** Establish the manifest context mismatch requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP manifest / bridge planning.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use an actual completed original CMP artifact-build association and manifest, then vary the named schema/context/target/member coordinate without reconstructing it from storage. Scenario-specific variation: Manifest context mismatch.
- **Expected Result:** Only original complete manifest V0 and exact association survive preflight; malformed declarations expose no bytes/loaded set. Named requirement: Manifest context mismatch.
- **Expected Diagnostics:** RUN-004 with original CMP manifest causes; RUN-014 context; duplicate constructor rejection/original CMP-041; no diagnostics on accepted facts.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** C. Manifest Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T017 — Manifest target mismatch

- **Test ID:** RUN-01-T017
- **Scenario:** Manifest target mismatch.
- **Objective:** Establish the manifest target mismatch requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP manifest / bridge planning.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use an actual completed original CMP artifact-build association and manifest, then vary the named schema/context/target/member coordinate without reconstructing it from storage. Scenario-specific variation: Manifest target mismatch.
- **Expected Result:** Only original complete manifest V0 and exact association survive preflight; malformed declarations expose no bytes/loaded set. Named requirement: Manifest target mismatch.
- **Expected Diagnostics:** RUN-004 with original CMP manifest causes; RUN-014 context; duplicate constructor rejection/original CMP-041; no diagnostics on accepted facts.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** C. Manifest Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T018 — Missing artifact descriptor

- **Test ID:** RUN-01-T018
- **Scenario:** Missing artifact descriptor.
- **Objective:** Establish the missing artifact descriptor requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP manifest / bridge planning.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use an actual completed original CMP artifact-build association and manifest, then vary the named schema/context/target/member coordinate without reconstructing it from storage. Scenario-specific variation: Missing artifact descriptor.
- **Expected Result:** Only original complete manifest V0 and exact association survive preflight; malformed declarations expose no bytes/loaded set. Named requirement: Missing artifact descriptor.
- **Expected Diagnostics:** RUN-004 with original CMP manifest causes; RUN-014 context; duplicate constructor rejection/original CMP-041; no diagnostics on accepted facts.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** C. Manifest Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T019 — Duplicate artifact identity

- **Test ID:** RUN-01-T019
- **Scenario:** Duplicate artifact identity.
- **Objective:** Establish the duplicate artifact identity requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP manifest / bridge planning.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Attempt manifest/binding construction with two descriptors sharing one key, including byte-identical metadata.
- **Expected Result:** Collision is rejected without overwrite/equality exception.
- **Expected Diagnostics:** Original CMP-041 or binding ValueError; no successful load.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** C. Manifest Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T020 — No manifest reconstruction from files

- **Test ID:** RUN-01-T020
- **Scenario:** No manifest reconstruction from files.
- **Objective:** Establish the no manifest reconstruction from files requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP manifest / bridge planning.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use an actual completed original CMP artifact-build association and manifest, then vary the named schema/context/target/member coordinate without reconstructing it from storage. Scenario-specific variation: No manifest reconstruction from files.
- **Expected Result:** Only original complete manifest V0 and exact association survive preflight; malformed declarations expose no bytes/loaded set. Named requirement: No manifest reconstruction from files.
- **Expected Diagnostics:** RUN-004 with original CMP manifest causes; RUN-014 context; duplicate constructor rejection/original CMP-041; no diagnostics on accepted facts.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** C. Manifest Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## D. Materialization Receipt

### RUN-01-T021 — Valid CMP-08 receipt

- **Test ID:** RUN-01-T021
- **Scenario:** Valid CMP-08 receipt.
- **Objective:** Establish the valid cmp-08 receipt requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP materialization / planning.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use the actual receipt bound to the same compilation association and exact ordered descriptors/logical source; omit or substitute the named receipt/entry/location/association. Scenario-specific variation: Valid CMP-08 receipt.
- **Expected Result:** Rejected receipt/source/evidence cannot enter runtime decoding; valid materialization remains traceable without granting authority. Named requirement: Valid CMP-08 receipt.
- **Expected Diagnostics:** Actual CMP read receipt/location diagnostics retained, RUN-005 for receipt mismatch; request constructor rejection for missing receipt.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** D. Materialization Receipt; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T022 — Missing receipt

- **Test ID:** RUN-01-T022
- **Scenario:** Missing receipt.
- **Objective:** Establish the missing receipt requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP materialization / planning.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Attempt application request construction with no actual ArtifactMaterializationReceipt in the CMP read request.
- **Expected Result:** Existing CMP request rejects before planning/IO/decoding.
- **Expected Diagnostics:** Original CMP-064 typed prerequisite rejection; no invented receipt.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** D. Materialization Receipt; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T023 — Manifest/receipt mismatch

- **Test ID:** RUN-01-T023
- **Scenario:** Manifest/receipt mismatch.
- **Objective:** Establish the manifest/receipt mismatch requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP materialization / planning.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use the actual receipt bound to the same compilation association and exact ordered descriptors/logical source; omit or substitute the named receipt/entry/location/association. Scenario-specific variation: Manifest/receipt mismatch.
- **Expected Result:** Rejected receipt/source/evidence cannot enter runtime decoding; valid materialization remains traceable without granting authority. Named requirement: Manifest/receipt mismatch.
- **Expected Diagnostics:** Actual CMP read receipt/location diagnostics retained, RUN-005 for receipt mismatch; request constructor rejection for missing receipt.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** D. Materialization Receipt; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T024 — Compilation association mismatch

- **Test ID:** RUN-01-T024
- **Scenario:** Compilation association mismatch.
- **Objective:** Establish the compilation association mismatch requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP materialization / planning.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use the actual receipt bound to the same compilation association and exact ordered descriptors/logical source; omit or substitute the named receipt/entry/location/association. Scenario-specific variation: Compilation association mismatch.
- **Expected Result:** Rejected receipt/source/evidence cannot enter runtime decoding; valid materialization remains traceable without granting authority. Named requirement: Compilation association mismatch.
- **Expected Diagnostics:** Actual CMP read receipt/location diagnostics retained, RUN-005 for receipt mismatch; request constructor rejection for missing receipt.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** D. Materialization Receipt; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T025 — Unknown committed location

- **Test ID:** RUN-01-T025
- **Scenario:** Unknown committed location.
- **Objective:** Establish the unknown committed location requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP materialization / planning.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use the actual receipt bound to the same compilation association and exact ordered descriptors/logical source; omit or substitute the named receipt/entry/location/association. Scenario-specific variation: Unknown committed location.
- **Expected Result:** Rejected receipt/source/evidence cannot enter runtime decoding; valid materialization remains traceable without granting authority. Named requirement: Unknown committed location.
- **Expected Diagnostics:** Actual CMP read receipt/location diagnostics retained, RUN-005 for receipt mismatch; request constructor rejection for missing receipt.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** D. Materialization Receipt; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T026 — No fabricated materialization evidence

- **Test ID:** RUN-01-T026
- **Scenario:** No fabricated materialization evidence.
- **Objective:** Establish the no fabricated materialization evidence requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP materialization / planning.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use the actual receipt bound to the same compilation association and exact ordered descriptors/logical source; omit or substitute the named receipt/entry/location/association. Scenario-specific variation: No fabricated materialization evidence.
- **Expected Result:** Rejected receipt/source/evidence cannot enter runtime decoding; valid materialization remains traceable without granting authority. Named requirement: No fabricated materialization evidence.
- **Expected Diagnostics:** Actual CMP read receipt/location diagnostics retained, RUN-005 for receipt mismatch; request constructor rejection for missing receipt.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** D. Materialization Receipt; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## E. CMP-09 Reader Integration

### RUN-01-T027 — Successful verified read

- **Test ID:** RUN-01-T027
- **Scenario:** Successful verified read.
- **Objective:** Establish the successful verified read requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP-09 source bridge.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use the injected existing CMP reader under forced DIGEST_VERIFIED; supply the named read status, filesystem failure or measured integrity condition and retain original diagnostic objects. Scenario-specific variation: Successful verified read.
- **Expected Result:** Only a fully selected verified read enters decoding once; FAILED/INCOMPLETE status persists and no partial loaded set is emitted. Named requirement: Successful verified read.
- **Expected Diagnostics:** RUN-006 plus original CMP-069/070/073/074 etc. as appropriate; missing digest preflight RUN-007 with CMP-075; reader warnings/info remain ordered causes.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** E. CMP-09 Reader Integration; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T028 — Reader FAILED outcome

- **Test ID:** RUN-01-T028
- **Scenario:** Reader FAILED outcome.
- **Objective:** Establish the reader failed outcome requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP-09 source bridge.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use the injected existing CMP reader under forced DIGEST_VERIFIED; supply the named read status, filesystem failure or measured integrity condition and retain original diagnostic objects. Scenario-specific variation: Reader FAILED outcome.
- **Expected Result:** Only a fully selected verified read enters decoding once; FAILED/INCOMPLETE status persists and no partial loaded set is emitted. Named requirement: Reader FAILED outcome.
- **Expected Diagnostics:** RUN-006 plus original CMP-069/070/073/074 etc. as appropriate; missing digest preflight RUN-007 with CMP-075; reader warnings/info remain ordered causes.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** E. CMP-09 Reader Integration; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T029 — Reader INCOMPLETE outcome

- **Test ID:** RUN-01-T029
- **Scenario:** Reader INCOMPLETE outcome.
- **Objective:** Establish the reader incomplete outcome requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP-09 source bridge.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use the injected existing CMP reader under forced DIGEST_VERIFIED; supply the named read status, filesystem failure or measured integrity condition and retain original diagnostic objects. Scenario-specific variation: Reader INCOMPLETE outcome.
- **Expected Result:** Only a fully selected verified read enters decoding once; FAILED/INCOMPLETE status persists and no partial loaded set is emitted. Named requirement: Reader INCOMPLETE outcome.
- **Expected Diagnostics:** RUN-006 plus original CMP-069/070/073/074 etc. as appropriate; missing digest preflight RUN-007 with CMP-075; reader warnings/info remain ordered causes.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** E. CMP-09 Reader Integration; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T030 — Missing artifact file

- **Test ID:** RUN-01-T030
- **Scenario:** Missing artifact file.
- **Objective:** Establish the missing artifact file requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP-09 source bridge.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use the injected existing CMP reader under forced DIGEST_VERIFIED; supply the named read status, filesystem failure or measured integrity condition and retain original diagnostic objects. Scenario-specific variation: Missing artifact file.
- **Expected Result:** Only a fully selected verified read enters decoding once; FAILED/INCOMPLETE status persists and no partial loaded set is emitted. Named requirement: Missing artifact file.
- **Expected Diagnostics:** RUN-006 plus original CMP-069/070/073/074 etc. as appropriate; missing digest preflight RUN-007 with CMP-075; reader warnings/info remain ordered causes.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** E. CMP-09 Reader Integration; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T031 — Size mismatch

- **Test ID:** RUN-01-T031
- **Scenario:** Size mismatch.
- **Objective:** Establish the size mismatch requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP-09 source bridge.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use the injected existing CMP reader under forced DIGEST_VERIFIED; supply the named read status, filesystem failure or measured integrity condition and retain original diagnostic objects. Scenario-specific variation: Size mismatch.
- **Expected Result:** Only a fully selected verified read enters decoding once; FAILED/INCOMPLETE status persists and no partial loaded set is emitted. Named requirement: Size mismatch.
- **Expected Diagnostics:** RUN-006 plus original CMP-069/070/073/074 etc. as appropriate; missing digest preflight RUN-007 with CMP-075; reader warnings/info remain ordered causes.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** E. CMP-09 Reader Integration; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T032 — Digest mismatch

- **Test ID:** RUN-01-T032
- **Scenario:** Digest mismatch.
- **Objective:** Establish the digest mismatch requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP-09 source bridge.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use the injected existing CMP reader under forced DIGEST_VERIFIED; supply the named read status, filesystem failure or measured integrity condition and retain original diagnostic objects. Scenario-specific variation: Digest mismatch.
- **Expected Result:** Only a fully selected verified read enters decoding once; FAILED/INCOMPLETE status persists and no partial loaded set is emitted. Named requirement: Digest mismatch.
- **Expected Diagnostics:** RUN-006 plus original CMP-069/070/073/074 etc. as appropriate; missing digest preflight RUN-007 with CMP-075; reader warnings/info remain ordered causes.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** E. CMP-09 Reader Integration; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T033 — Insufficient integrity evidence

- **Test ID:** RUN-01-T033
- **Scenario:** Insufficient integrity evidence.
- **Objective:** Establish the insufficient integrity evidence requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP-09 source bridge.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use an otherwise valid size-only committed receipt with verified_digest=None, even if a successful size-only read could exist.
- **Expected Result:** INCOMPLETE in pure preflight; no digest generated, downgrade or load success.
- **Expected Diagnostics:** RUN-007 wrapping original CMP-075.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** E. CMP-09 Reader Integration; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T034 — No duplicate filesystem reads

- **Test ID:** RUN-01-T034
- **Scenario:** No duplicate filesystem reads.
- **Objective:** Establish the no duplicate filesystem reads requirement without weakening authority, integrity or runtime boundaries.
- **Component:** CMP-09 source bridge.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use a fully authorized supported complete package and record CMP-09 calls when execution is later authorized.
- **Expected Result:** One reader.read for the full ALL set, no per-item source reopening/rehashing from RUN-01.
- **Expected Diagnostics:** None for accepted read; original read diagnostics retained.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** E. CMP-09 Reader Integration; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## F. Artifact Kind and Format

### RUN-01-T035 — Supported artifact kind

- **Test ID:** RUN-01-T035
- **Scenario:** Supported artifact kind.
- **Objective:** Establish the supported artifact kind requirement without weakening authority, integrity or runtime boundaries.
- **Component:** content declaration / dispatch.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use a genuine approved producer declaration and decoder registration; vary the named kind/format/exact encoding version, filename or substitute a CompiledTypeIR input. Scenario-specific variation: Supported artifact kind.
- **Expected Result:** Exact approved tuple is required; unknown capabilities are INCOMPLETE, IR/untyped input is invalid, no migration or filename inference. Named requirement: Supported artifact kind.
- **Expected Diagnostics:** RUN-008 kind; RUN-009 format; RUN-010 exact version; RUN-001 for IR-as-request.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** F. Artifact Kind and Format; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T036 — Unsupported artifact kind

- **Test ID:** RUN-01-T036
- **Scenario:** Unsupported artifact kind.
- **Objective:** Establish the unsupported artifact kind requirement without weakening authority, integrity or runtime boundaries.
- **Component:** content declaration / dispatch.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use a genuine approved producer declaration and decoder registration; vary the named kind/format/exact encoding version, filename or substitute a CompiledTypeIR input. Scenario-specific variation: Unsupported artifact kind.
- **Expected Result:** Exact approved tuple is required; unknown capabilities are INCOMPLETE, IR/untyped input is invalid, no migration or filename inference. Named requirement: Unsupported artifact kind.
- **Expected Diagnostics:** RUN-008 kind; RUN-009 format; RUN-010 exact version; RUN-001 for IR-as-request.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** F. Artifact Kind and Format; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T037 — Supported content format

- **Test ID:** RUN-01-T037
- **Scenario:** Supported content format.
- **Objective:** Establish the supported content format requirement without weakening authority, integrity or runtime boundaries.
- **Component:** content declaration / dispatch.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use a genuine approved producer declaration and decoder registration; vary the named kind/format/exact encoding version, filename or substitute a CompiledTypeIR input. Scenario-specific variation: Supported content format.
- **Expected Result:** Exact approved tuple is required; unknown capabilities are INCOMPLETE, IR/untyped input is invalid, no migration or filename inference. Named requirement: Supported content format.
- **Expected Diagnostics:** RUN-008 kind; RUN-009 format; RUN-010 exact version; RUN-001 for IR-as-request.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** F. Artifact Kind and Format; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T038 — Unsupported format

- **Test ID:** RUN-01-T038
- **Scenario:** Unsupported format.
- **Objective:** Establish the unsupported format requirement without weakening authority, integrity or runtime boundaries.
- **Component:** content declaration / dispatch.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use a genuine approved producer declaration and decoder registration; vary the named kind/format/exact encoding version, filename or substitute a CompiledTypeIR input. Scenario-specific variation: Unsupported format.
- **Expected Result:** Exact approved tuple is required; unknown capabilities are INCOMPLETE, IR/untyped input is invalid, no migration or filename inference. Named requirement: Unsupported format.
- **Expected Diagnostics:** RUN-008 kind; RUN-009 format; RUN-010 exact version; RUN-001 for IR-as-request.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** F. Artifact Kind and Format; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T039 — Valid format version

- **Test ID:** RUN-01-T039
- **Scenario:** Valid format version.
- **Objective:** Establish the valid format version requirement without weakening authority, integrity or runtime boundaries.
- **Component:** content declaration / dispatch.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use a genuine approved producer declaration and decoder registration; vary the named kind/format/exact encoding version, filename or substitute a CompiledTypeIR input. Scenario-specific variation: Valid format version.
- **Expected Result:** Exact approved tuple is required; unknown capabilities are INCOMPLETE, IR/untyped input is invalid, no migration or filename inference. Named requirement: Valid format version.
- **Expected Diagnostics:** RUN-008 kind; RUN-009 format; RUN-010 exact version; RUN-001 for IR-as-request.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** F. Artifact Kind and Format; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T040 — Unsupported future version

- **Test ID:** RUN-01-T040
- **Scenario:** Unsupported future version.
- **Objective:** Establish the unsupported future version requirement without weakening authority, integrity or runtime boundaries.
- **Component:** content declaration / dispatch.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use a genuine approved producer declaration and decoder registration; vary the named kind/format/exact encoding version, filename or substitute a CompiledTypeIR input. Scenario-specific variation: Unsupported future version.
- **Expected Result:** Exact approved tuple is required; unknown capabilities are INCOMPLETE, IR/untyped input is invalid, no migration or filename inference. Named requirement: Unsupported future version.
- **Expected Diagnostics:** RUN-008 kind; RUN-009 format; RUN-010 exact version; RUN-001 for IR-as-request.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** F. Artifact Kind and Format; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T041 — No filename-based format inference

- **Test ID:** RUN-01-T041
- **Scenario:** No filename-based format inference.
- **Objective:** Establish the no filename-based format inference requirement without weakening authority, integrity or runtime boundaries.
- **Component:** content declaration / dispatch.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use a genuine approved producer declaration and decoder registration; vary the named kind/format/exact encoding version, filename or substitute a CompiledTypeIR input. Scenario-specific variation: No filename-based format inference.
- **Expected Result:** Exact approved tuple is required; unknown capabilities are INCOMPLETE, IR/untyped input is invalid, no migration or filename inference. Named requirement: No filename-based format inference.
- **Expected Diagnostics:** RUN-008 kind; RUN-009 format; RUN-010 exact version; RUN-001 for IR-as-request.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** F. Artifact Kind and Format; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T042 — No semantic IR-as-runtime-artifact substitution

- **Test ID:** RUN-01-T042
- **Scenario:** No semantic IR-as-runtime-artifact substitution.
- **Objective:** Establish the no semantic ir-as-runtime-artifact substitution requirement without weakening authority, integrity or runtime boundaries.
- **Component:** content declaration / dispatch.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use a genuine approved producer declaration and decoder registration; vary the named kind/format/exact encoding version, filename or substitute a CompiledTypeIR input. Scenario-specific variation: No semantic IR-as-runtime-artifact substitution.
- **Expected Result:** Exact approved tuple is required; unknown capabilities are INCOMPLETE, IR/untyped input is invalid, no migration or filename inference. Named requirement: No semantic IR-as-runtime-artifact substitution.
- **Expected Diagnostics:** RUN-008 kind; RUN-009 format; RUN-010 exact version; RUN-001 for IR-as-request.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** F. Artifact Kind and Format; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## G. Decoder Dispatch

### RUN-01-T043 — Explicit supported decoder

- **Test ID:** RUN-01-T043
- **Scenario:** Explicit supported decoder.
- **Objective:** Establish the explicit supported decoder requirement without weakening authority, integrity or runtime boundaries.
- **Component:** trusted decoder catalog.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use constructor-injected catalog entries for genuine approved owned format implementations; vary registration pairing, omit implementation or place a module/class name in artifact data. Scenario-specific variation: Explicit supported decoder.
- **Expected Result:** Only the approved kind/format/version/runtime tuple dispatches; no discovery/reflection fallback or data-controlled code loading. Named requirement: Explicit supported decoder.
- **Expected Diagnostics:** RUN-011 recognized kind without implementation; RUN-008/009/010 unsupported dispatch; duplicate catalog ValueError.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** G. Decoder Dispatch; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T044 — Missing decoder

- **Test ID:** RUN-01-T044
- **Scenario:** Missing decoder.
- **Objective:** Establish the missing decoder requirement without weakening authority, integrity or runtime boundaries.
- **Component:** trusted decoder catalog.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Trust-recognize a real producer kind with actual content declaration but zero approved decoder registrations.
- **Expected Result:** INCOMPLETE before byte access with no representation.
- **Expected Diagnostics:** RUN-011.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** G. Decoder Dispatch; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T045 — Wrong kind/decoder pairing

- **Test ID:** RUN-01-T045
- **Scenario:** Wrong kind/decoder pairing.
- **Objective:** Establish the wrong kind/decoder pairing requirement without weakening authority, integrity or runtime boundaries.
- **Component:** trusted decoder catalog.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Keep format/version equal but select a descriptor kind with no matching explicit registration.
- **Expected Result:** INCOMPLETE; never dispatch another kind’s decoder.
- **Expected Diagnostics:** RUN-008, or RUN-011 if trusted kind recognition exists without decoder.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** G. Decoder Dispatch; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T046 — Wrong version/decoder pairing

- **Test ID:** RUN-01-T046
- **Scenario:** Wrong version/decoder pairing.
- **Objective:** Establish the wrong version/decoder pairing requirement without weakening authority, integrity or runtime boundaries.
- **Component:** trusted decoder catalog.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Declare an exact future numeric format version not in the same-kind/format registrations.
- **Expected Result:** INCOMPLETE; no latest fallback or migration.
- **Expected Diagnostics:** RUN-010.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** G. Decoder Dispatch; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T047 — No dynamic module imports

- **Test ID:** RUN-01-T047
- **Scenario:** No dynamic module imports.
- **Objective:** Establish the no dynamic module imports requirement without weakening authority, integrity or runtime boundaries.
- **Component:** trusted decoder catalog.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use constructor-injected catalog entries for genuine approved owned format implementations; vary registration pairing, omit implementation or place a module/class name in artifact data. Scenario-specific variation: No dynamic module imports.
- **Expected Result:** Only the approved kind/format/version/runtime tuple dispatches; no discovery/reflection fallback or data-controlled code loading. Named requirement: No dynamic module imports.
- **Expected Diagnostics:** RUN-011 recognized kind without implementation; RUN-008/009/010 unsupported dispatch; duplicate catalog ValueError.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** G. Decoder Dispatch; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T048 — No arbitrary reflection

- **Test ID:** RUN-01-T048
- **Scenario:** No arbitrary reflection.
- **Objective:** Establish the no arbitrary reflection requirement without weakening authority, integrity or runtime boundaries.
- **Component:** trusted decoder catalog.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use constructor-injected catalog entries for genuine approved owned format implementations; vary registration pairing, omit implementation or place a module/class name in artifact data. Scenario-specific variation: No arbitrary reflection.
- **Expected Result:** Only the approved kind/format/version/runtime tuple dispatches; no discovery/reflection fallback or data-controlled code loading. Named requirement: No arbitrary reflection.
- **Expected Diagnostics:** RUN-011 recognized kind without implementation; RUN-008/009/010 unsupported dispatch; duplicate catalog ValueError.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** G. Decoder Dispatch; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T049 — No unsafe fallback decoding

- **Test ID:** RUN-01-T049
- **Scenario:** No unsafe fallback decoding.
- **Objective:** Establish the no unsafe fallback decoding requirement without weakening authority, integrity or runtime boundaries.
- **Component:** trusted decoder catalog.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use constructor-injected catalog entries for genuine approved owned format implementations; vary registration pairing, omit implementation or place a module/class name in artifact data. Scenario-specific variation: No unsafe fallback decoding.
- **Expected Result:** Only the approved kind/format/version/runtime tuple dispatches; no discovery/reflection fallback or data-controlled code loading. Named requirement: No unsafe fallback decoding.
- **Expected Diagnostics:** RUN-011 recognized kind without implementation; RUN-008/009/010 unsupported dispatch; duplicate catalog ValueError.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** G. Decoder Dispatch; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## H. Decoder Structural Integrity

### RUN-01-T050 — Valid approved artifact payload

- **Test ID:** RUN-01-T050
- **Scenario:** Valid approved artifact payload.
- **Objective:** Establish the valid approved artifact payload requirement without weakening authority, integrity or runtime boundaries.
- **Component:** approved decoder / graph guard.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Once a genuine owned format exists, alter its encoded required field/discriminator/nesting/primitive or depth/element budget under that decoder’s actual documented schema. Scenario-specific variation: Valid approved artifact payload.
- **Expected Result:** Expected structural errors are typed failures with no representation; budget violations fail without partial output or unsafe deserialization. Named requirement: Valid approved artifact payload.
- **Expected Diagnostics:** RUN-012 expected decode errors or format-specific structured diagnostics; RUN-018 budget; RUN-020 invalid representation.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** H. Decoder Structural Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T051 — Missing required encoded field

- **Test ID:** RUN-01-T051
- **Scenario:** Missing required encoded field.
- **Objective:** Establish the missing required encoded field requirement without weakening authority, integrity or runtime boundaries.
- **Component:** approved decoder / graph guard.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Once a genuine owned format exists, alter its encoded required field/discriminator/nesting/primitive or depth/element budget under that decoder’s actual documented schema. Scenario-specific variation: Missing required encoded field.
- **Expected Result:** Expected structural errors are typed failures with no representation; budget violations fail without partial output or unsafe deserialization. Named requirement: Missing required encoded field.
- **Expected Diagnostics:** RUN-012 expected decode errors or format-specific structured diagnostics; RUN-018 budget; RUN-020 invalid representation.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** H. Decoder Structural Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T052 — Incorrect discriminator

- **Test ID:** RUN-01-T052
- **Scenario:** Incorrect discriminator.
- **Objective:** Establish the incorrect discriminator requirement without weakening authority, integrity or runtime boundaries.
- **Component:** approved decoder / graph guard.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Once a genuine owned format exists, alter its encoded required field/discriminator/nesting/primitive or depth/element budget under that decoder’s actual documented schema. Scenario-specific variation: Incorrect discriminator.
- **Expected Result:** Expected structural errors are typed failures with no representation; budget violations fail without partial output or unsafe deserialization. Named requirement: Incorrect discriminator.
- **Expected Diagnostics:** RUN-012 expected decode errors or format-specific structured diagnostics; RUN-018 budget; RUN-020 invalid representation.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** H. Decoder Structural Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T053 — Invalid nested structure

- **Test ID:** RUN-01-T053
- **Scenario:** Invalid nested structure.
- **Objective:** Establish the invalid nested structure requirement without weakening authority, integrity or runtime boundaries.
- **Component:** approved decoder / graph guard.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Once a genuine owned format exists, alter its encoded required field/discriminator/nesting/primitive or depth/element budget under that decoder’s actual documented schema. Scenario-specific variation: Invalid nested structure.
- **Expected Result:** Expected structural errors are typed failures with no representation; budget violations fail without partial output or unsafe deserialization. Named requirement: Invalid nested structure.
- **Expected Diagnostics:** RUN-012 expected decode errors or format-specific structured diagnostics; RUN-018 budget; RUN-020 invalid representation.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** H. Decoder Structural Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T054 — Unsupported encoded primitive

- **Test ID:** RUN-01-T054
- **Scenario:** Unsupported encoded primitive.
- **Objective:** Establish the unsupported encoded primitive requirement without weakening authority, integrity or runtime boundaries.
- **Component:** approved decoder / graph guard.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Once a genuine owned format exists, alter its encoded required field/discriminator/nesting/primitive or depth/element budget under that decoder’s actual documented schema. Scenario-specific variation: Unsupported encoded primitive.
- **Expected Result:** Expected structural errors are typed failures with no representation; budget violations fail without partial output or unsafe deserialization. Named requirement: Unsupported encoded primitive.
- **Expected Diagnostics:** RUN-012 expected decode errors or format-specific structured diagnostics; RUN-018 budget; RUN-020 invalid representation.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** H. Decoder Structural Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T055 — Decoder limit exceeded

- **Test ID:** RUN-01-T055
- **Scenario:** Decoder limit exceeded.
- **Objective:** Establish the decoder limit exceeded requirement without weakening authority, integrity or runtime boundaries.
- **Component:** approved decoder / graph guard.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Once a genuine owned format exists, alter its encoded required field/discriminator/nesting/primitive or depth/element budget under that decoder’s actual documented schema. Scenario-specific variation: Decoder limit exceeded.
- **Expected Result:** Expected structural errors are typed failures with no representation; budget violations fail without partial output or unsafe deserialization. Named requirement: Decoder limit exceeded.
- **Expected Diagnostics:** RUN-012 expected decode errors or format-specific structured diagnostics; RUN-018 budget; RUN-020 invalid representation.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** H. Decoder Structural Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T056 — No arbitrary executable deserialization

- **Test ID:** RUN-01-T056
- **Scenario:** No arbitrary executable deserialization.
- **Objective:** Establish the no arbitrary executable deserialization requirement without weakening authority, integrity or runtime boundaries.
- **Component:** approved decoder / graph guard.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Once a genuine owned format exists, alter its encoded required field/discriminator/nesting/primitive or depth/element budget under that decoder’s actual documented schema. Scenario-specific variation: No arbitrary executable deserialization.
- **Expected Result:** Expected structural errors are typed failures with no representation; budget violations fail without partial output or unsafe deserialization. Named requirement: No arbitrary executable deserialization.
- **Expected Diagnostics:** RUN-012 expected decode errors or format-specific structured diagnostics; RUN-018 budget; RUN-020 invalid representation.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** H. Decoder Structural Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## I. Runtime Representation

### RUN-01-T057 — Immutable LoadedRuntimeArtifact

- **Test ID:** RUN-01-T057
- **Scenario:** Immutable LoadedRuntimeArtifact.
- **Objective:** Establish the immutable loadedruntimeartifact requirement without weakening authority, integrity or runtime boundaries.
- **Component:** loaded artifact.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Return an approved frozen root containing a mutable list/dict/set or a slotted class inheriting an instance dictionary.
- **Expected Result:** Registration/graph inspection rejects hidden mutability; outer frozen wrapper is insufficient.
- **Expected Diagnostics:** Registration TypeError or RUN-020.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** I. Runtime Representation; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T058 — Exact artifact identity preserved

- **Test ID:** RUN-01-T058
- **Scenario:** Exact artifact identity preserved.
- **Objective:** Establish the exact artifact identity preserved requirement without weakening authority, integrity or runtime boundaries.
- **Component:** loaded artifact.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Construct through the approved decoder a concrete frozen slotted representation with the actual descriptor identity/exact origins/scope; vary one named output invariant. Scenario-specific variation: Exact artifact identity preserved.
- **Expected Result:** Only closed deeply immutable approved values with exact metadata are accepted; no new business instance or semantic ID. Named requirement: Exact artifact identity preserved.
- **Expected Diagnostics:** RUN-020 unapproved/mutable/origin mismatch; RUN-014 context mismatch; constructor rejection for invalid evidence.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** I. Runtime Representation; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T059 — Semantic origin preserved

- **Test ID:** RUN-01-T059
- **Scenario:** Semantic origin preserved.
- **Objective:** Establish the semantic origin preserved requirement without weakening authority, integrity or runtime boundaries.
- **Component:** loaded artifact.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Compare decoded exact ElementVersionRef tuple/model_wide to descriptor metadata; alter version, order, omit one origin or fabricate a new origin.
- **Expected Result:** FAILED on every nonmatching origin declaration; preserve model-wide case when explicitly declared.
- **Expected Diagnostics:** RUN-020 with current artifact and original semantic origins.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** I. Runtime Representation; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T060 — Context preserved

- **Test ID:** RUN-01-T060
- **Scenario:** Context preserved.
- **Objective:** Establish the context preserved requirement without weakening authority, integrity or runtime boundaries.
- **Component:** loaded artifact.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Return an approved representation with a different actual SemanticContextRef or raw string scope.
- **Expected Result:** FAILED; no context rewriting.
- **Expected Diagnostics:** RUN-014.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** I. Runtime Representation; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T061 — Typed runtime representation

- **Test ID:** RUN-01-T061
- **Scenario:** Typed runtime representation.
- **Objective:** Establish the typed runtime representation requirement without weakening authority, integrity or runtime boundaries.
- **Component:** loaded artifact.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Approved decoder returns a dict, list, arbitrary object, subclass or a different frozen class instead of its exact representation_type.
- **Expected Result:** FAILED without public partial set.
- **Expected Diagnostics:** RUN-020.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** I. Runtime Representation; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T062 — No semantic element identity fabrication

- **Test ID:** RUN-01-T062
- **Scenario:** No semantic element identity fabrication.
- **Objective:** Establish the no semantic element identity fabrication requirement without weakening authority, integrity or runtime boundaries.
- **Component:** loaded artifact.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Construct through the approved decoder a concrete frozen slotted representation with the actual descriptor identity/exact origins/scope; vary one named output invariant. Scenario-specific variation: No semantic element identity fabrication.
- **Expected Result:** Only closed deeply immutable approved values with exact metadata are accepted; no new business instance or semantic ID. Named requirement: No semantic element identity fabrication.
- **Expected Diagnostics:** RUN-020 unapproved/mutable/origin mismatch; RUN-014 context mismatch; constructor rejection for invalid evidence.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** I. Runtime Representation; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T063 — No runtime business instance construction

- **Test ID:** RUN-01-T063
- **Scenario:** No runtime business instance construction.
- **Objective:** Establish the no runtime business instance construction requirement without weakening authority, integrity or runtime boundaries.
- **Component:** loaded artifact.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Construct through the approved decoder a concrete frozen slotted representation with the actual descriptor identity/exact origins/scope; vary one named output invariant. Scenario-specific variation: No runtime business instance construction.
- **Expected Result:** Only closed deeply immutable approved values with exact metadata are accepted; no new business instance or semantic ID. Named requirement: No runtime business instance construction.
- **Expected Diagnostics:** RUN-020 unapproved/mutable/origin mismatch; RUN-014 context mismatch; constructor rejection for invalid evidence.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** I. Runtime Representation; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## J. Dependency Integrity

### RUN-01-T064 — Valid internal dependencies

- **Test ID:** RUN-01-T064
- **Scenario:** Valid internal dependencies.
- **Objective:** Establish the valid internal dependencies requirement without weakening authority, integrity or runtime boundaries.
- **Component:** dependency/completeness preflight.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Prepare a complete ALL manifest with explicit internal artifact keys; remove the named dependency, request subset, introduce unsupported external dependency or declared self/mutual key cycle. Scenario-specific variation: Valid internal dependencies.
- **Expected Result:** Known full internal dependencies stay in manifest order; incomplete/external scopes fail without closure; independently decoded cycles are allowed. Named requirement: Valid internal dependencies.
- **Expected Diagnostics:** RUN-016 missing/unsupported dependency, RUN-019 subset; original CMP-040 for malformed manifest; no cycle error for valid internal references.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** J. Dependency Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T065 — Missing required dependency

- **Test ID:** RUN-01-T065
- **Scenario:** Missing required dependency.
- **Objective:** Establish the missing required dependency requirement without weakening authority, integrity or runtime boundaries.
- **Component:** dependency/completeness preflight.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Prepare a complete ALL manifest with explicit internal artifact keys; remove the named dependency, request subset, introduce unsupported external dependency or declared self/mutual key cycle. Scenario-specific variation: Missing required dependency.
- **Expected Result:** Known full internal dependencies stay in manifest order; incomplete/external scopes fail without closure; independently decoded cycles are allowed. Named requirement: Missing required dependency.
- **Expected Diagnostics:** RUN-016 missing/unsupported dependency, RUN-019 subset; original CMP-040 for malformed manifest; no cycle error for valid internal references.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** J. Dependency Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T066 — Unsupported external dependency

- **Test ID:** RUN-01-T066
- **Scenario:** Unsupported external dependency.
- **Objective:** Establish the unsupported external dependency requirement without weakening authority, integrity or runtime boundaries.
- **Component:** dependency/completeness preflight.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Prepare a complete ALL manifest with explicit internal artifact keys; remove the named dependency, request subset, introduce unsupported external dependency or declared self/mutual key cycle. Scenario-specific variation: Unsupported external dependency.
- **Expected Result:** Known full internal dependencies stay in manifest order; incomplete/external scopes fail without closure; independently decoded cycles are allowed. Named requirement: Unsupported external dependency.
- **Expected Diagnostics:** RUN-016 missing/unsupported dependency, RUN-019 subset; original CMP-040 for malformed manifest; no cycle error for valid internal references.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** J. Dependency Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T067 — Selected subset omits a required dependency

- **Test ID:** RUN-01-T067
- **Scenario:** Selected subset omits a required dependency.
- **Objective:** Establish the selected subset omits a required dependency requirement without weakening authority, integrity or runtime boundaries.
- **Component:** dependency/completeness preflight.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use CMP ONE or EXPLICIT_SET selection that excludes a descriptor dependency, even if selected bytes could be read.
- **Expected Result:** FAILED at runtime completeness preflight before source access; no implicit expansion.
- **Expected Diagnostics:** RUN-019; CMP-040 if the complete manifest itself has an unknown dependency.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** J. Dependency Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T068 — Multiple artifact versions

- **Test ID:** RUN-01-T068
- **Scenario:** Multiple artifact versions.
- **Objective:** Establish the multiple artifact versions requirement without weakening authority, integrity or runtime boundaries.
- **Component:** dependency/completeness preflight.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Prepare a complete ALL manifest with explicit internal artifact keys; remove the named dependency, request subset, introduce unsupported external dependency or declared self/mutual key cycle. Scenario-specific variation: Multiple artifact versions.
- **Expected Result:** Known full internal dependencies stay in manifest order; incomplete/external scopes fail without closure; independently decoded cycles are allowed. Named requirement: Multiple artifact versions.
- **Expected Diagnostics:** RUN-016 missing/unsupported dependency, RUN-019 subset; original CMP-040 for malformed manifest; no cycle error for valid internal references.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** J. Dependency Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T069 — Valid reference cycle under supported policy

- **Test ID:** RUN-01-T069
- **Scenario:** Valid reference cycle under supported policy.
- **Objective:** Establish the valid reference cycle under supported policy requirement without weakening authority, integrity or runtime boundaries.
- **Component:** dependency/completeness preflight.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use a valid full ALL manifest with A→A and A↔B internal artifact keys and independently decodable approved formats.
- **Expected Result:** Dependency integrity accepts known keys; manifest order preserved, no topological sort or cycle rejection.
- **Expected Diagnostics:** No dependency diagnostic; business/activation execution remains absent.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** J. Dependency Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T070 — No automatic semantic dependency closure

- **Test ID:** RUN-01-T070
- **Scenario:** No automatic semantic dependency closure.
- **Objective:** Establish the no automatic semantic dependency closure requirement without weakening authority, integrity or runtime boundaries.
- **Component:** dependency/completeness preflight.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Prepare a complete ALL manifest with explicit internal artifact keys; remove the named dependency, request subset, introduce unsupported external dependency or declared self/mutual key cycle. Scenario-specific variation: No automatic semantic dependency closure.
- **Expected Result:** Known full internal dependencies stay in manifest order; incomplete/external scopes fail without closure; independently decoded cycles are allowed. Named requirement: No automatic semantic dependency closure.
- **Expected Diagnostics:** RUN-016 missing/unsupported dependency, RUN-019 subset; original CMP-040 for malformed manifest; no cycle error for valid internal references.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** J. Dependency Integrity; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## K. Compatibility

### RUN-01-T071 — Supported runtime target

- **Test ID:** RUN-01-T071
- **Scenario:** Supported runtime target.
- **Objective:** Establish the supported runtime target requirement without weakening authority, integrity or runtime boundaries.
- **Component:** compatibility dispatch.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Keep kind/format exact and vary explicit runtime target, required capability set or format/runtime compatibility version in producer metadata and trusted registration. Scenario-specific variation: Supported runtime target.
- **Expected Result:** Only the exact approved target/version with every mandatory feature accepted; unknown support is INCOMPLETE, target inconsistency FAILED. Named requirement: Supported runtime target.
- **Expected Diagnostics:** RUN-013 target, RUN-015 feature, RUN-010 format version, RUN-021 runtime compatibility version.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** K. Compatibility; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T072 — Incompatible runtime target

- **Test ID:** RUN-01-T072
- **Scenario:** Incompatible runtime target.
- **Objective:** Establish the incompatible runtime target requirement without weakening authority, integrity or runtime boundaries.
- **Component:** compatibility dispatch.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Keep kind/format exact and vary explicit runtime target, required capability set or format/runtime compatibility version in producer metadata and trusted registration. Scenario-specific variation: Incompatible runtime target.
- **Expected Result:** Only the exact approved target/version with every mandatory feature accepted; unknown support is INCOMPLETE, target inconsistency FAILED. Named requirement: Incompatible runtime target.
- **Expected Diagnostics:** RUN-013 target, RUN-015 feature, RUN-010 format version, RUN-021 runtime compatibility version.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** K. Compatibility; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T073 — Supported feature requirements

- **Test ID:** RUN-01-T073
- **Scenario:** Supported feature requirements.
- **Objective:** Establish the supported feature requirements requirement without weakening authority, integrity or runtime boundaries.
- **Component:** compatibility dispatch.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Keep kind/format exact and vary explicit runtime target, required capability set or format/runtime compatibility version in producer metadata and trusted registration. Scenario-specific variation: Supported feature requirements.
- **Expected Result:** Only the exact approved target/version with every mandatory feature accepted; unknown support is INCOMPLETE, target inconsistency FAILED. Named requirement: Supported feature requirements.
- **Expected Diagnostics:** RUN-013 target, RUN-015 feature, RUN-010 format version, RUN-021 runtime compatibility version.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** K. Compatibility; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T074 — Unknown mandatory runtime capability

- **Test ID:** RUN-01-T074
- **Scenario:** Unknown mandatory runtime capability.
- **Objective:** Establish the unknown mandatory runtime capability requirement without weakening authority, integrity or runtime boundaries.
- **Component:** compatibility dispatch.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Keep kind/format exact and vary explicit runtime target, required capability set or format/runtime compatibility version in producer metadata and trusted registration. Scenario-specific variation: Unknown mandatory runtime capability.
- **Expected Result:** Only the exact approved target/version with every mandatory feature accepted; unknown support is INCOMPLETE, target inconsistency FAILED. Named requirement: Unknown mandatory runtime capability.
- **Expected Diagnostics:** RUN-013 target, RUN-015 feature, RUN-010 format version, RUN-021 runtime compatibility version.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** K. Compatibility; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T075 — Supported format version

- **Test ID:** RUN-01-T075
- **Scenario:** Supported format version.
- **Objective:** Establish the supported format version requirement without weakening authority, integrity or runtime boundaries.
- **Component:** compatibility dispatch.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Keep kind/format exact and vary explicit runtime target, required capability set or format/runtime compatibility version in producer metadata and trusted registration. Scenario-specific variation: Supported format version.
- **Expected Result:** Only the exact approved target/version with every mandatory feature accepted; unknown support is INCOMPLETE, target inconsistency FAILED. Named requirement: Supported format version.
- **Expected Diagnostics:** RUN-013 target, RUN-015 feature, RUN-010 format version, RUN-021 runtime compatibility version.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** K. Compatibility; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T076 — Unsupported format version

- **Test ID:** RUN-01-T076
- **Scenario:** Unsupported format version.
- **Objective:** Establish the unsupported format version requirement without weakening authority, integrity or runtime boundaries.
- **Component:** compatibility dispatch.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Keep kind/format exact and vary explicit runtime target, required capability set or format/runtime compatibility version in producer metadata and trusted registration. Scenario-specific variation: Unsupported format version.
- **Expected Result:** Only the exact approved target/version with every mandatory feature accepted; unknown support is INCOMPLETE, target inconsistency FAILED. Named requirement: Unsupported format version.
- **Expected Diagnostics:** RUN-013 target, RUN-015 feature, RUN-010 format version, RUN-021 runtime compatibility version.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** K. Compatibility; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T077 — No implicit migration

- **Test ID:** RUN-01-T077
- **Scenario:** No implicit migration.
- **Objective:** Establish the no implicit migration requirement without weakening authority, integrity or runtime boundaries.
- **Component:** compatibility dispatch.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Keep kind/format exact and vary explicit runtime target, required capability set or format/runtime compatibility version in producer metadata and trusted registration. Scenario-specific variation: No implicit migration.
- **Expected Result:** Only the exact approved target/version with every mandatory feature accepted; unknown support is INCOMPLETE, target inconsistency FAILED. Named requirement: No implicit migration.
- **Expected Diagnostics:** RUN-013 target, RUN-015 feature, RUN-010 format version, RUN-021 runtime compatibility version.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** K. Compatibility; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## L. Atomic Loading

### RUN-01-T078 — All artifacts load successfully

- **Test ID:** RUN-01-T078
- **Scenario:** All artifacts load successfully.
- **Objective:** Establish the all artifacts load successfully requirement without weakening authority, integrity or runtime boundaries.
- **Component:** atomic coordinator/result.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use at least two actually approved artifacts; arrange the named first/later mandatory read/decode/compatibility failure while all other prerequisites remain valid. Scenario-specific variation: All artifacts load successfully.
- **Expected Result:** Success contains all manifest members; any mandatory failure yields no public loaded_set and no active registry side effect. Named requirement: All artifacts load successfully.
- **Expected Diagnostics:** Original reader/decode cause plus corresponding RUN-006/011/012/013; non-success invariant ValueError if partial output is manually attempted.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** L. Atomic Loading; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T079 — First artifact fails

- **Test ID:** RUN-01-T079
- **Scenario:** First artifact fails.
- **Objective:** Establish the first artifact fails requirement without weakening authority, integrity or runtime boundaries.
- **Component:** atomic coordinator/result.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use at least two actually approved artifacts; arrange the named first/later mandatory read/decode/compatibility failure while all other prerequisites remain valid. Scenario-specific variation: First artifact fails.
- **Expected Result:** Success contains all manifest members; any mandatory failure yields no public loaded_set and no active registry side effect. Named requirement: First artifact fails.
- **Expected Diagnostics:** Original reader/decode cause plus corresponding RUN-006/011/012/013; non-success invariant ValueError if partial output is manually attempted.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** L. Atomic Loading; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T080 — Later artifact fails

- **Test ID:** RUN-01-T080
- **Scenario:** Later artifact fails.
- **Objective:** Establish the later artifact fails requirement without weakening authority, integrity or runtime boundaries.
- **Component:** atomic coordinator/result.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use at least two actually approved artifacts; arrange the named first/later mandatory read/decode/compatibility failure while all other prerequisites remain valid. Scenario-specific variation: Later artifact fails.
- **Expected Result:** Success contains all manifest members; any mandatory failure yields no public loaded_set and no active registry side effect. Named requirement: Later artifact fails.
- **Expected Diagnostics:** Original reader/decode cause plus corresponding RUN-006/011/012/013; non-success invariant ValueError if partial output is manually attempted.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** L. Atomic Loading; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T081 — Decoder unavailable

- **Test ID:** RUN-01-T081
- **Scenario:** Decoder unavailable.
- **Objective:** Establish the decoder unavailable requirement without weakening authority, integrity or runtime boundaries.
- **Component:** atomic coordinator/result.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use at least two actually approved artifacts; arrange the named first/later mandatory read/decode/compatibility failure while all other prerequisites remain valid. Scenario-specific variation: Decoder unavailable.
- **Expected Result:** Success contains all manifest members; any mandatory failure yields no public loaded_set and no active registry side effect. Named requirement: Decoder unavailable.
- **Expected Diagnostics:** Original reader/decode cause plus corresponding RUN-006/011/012/013; non-success invariant ValueError if partial output is manually attempted.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** L. Atomic Loading; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T082 — One incompatible artifact

- **Test ID:** RUN-01-T082
- **Scenario:** One incompatible artifact.
- **Objective:** Establish the one incompatible artifact requirement without weakening authority, integrity or runtime boundaries.
- **Component:** atomic coordinator/result.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use at least two actually approved artifacts; arrange the named first/later mandatory read/decode/compatibility failure while all other prerequisites remain valid. Scenario-specific variation: One incompatible artifact.
- **Expected Result:** Success contains all manifest members; any mandatory failure yields no public loaded_set and no active registry side effect. Named requirement: One incompatible artifact.
- **Expected Diagnostics:** Original reader/decode cause plus corresponding RUN-006/011/012/013; non-success invariant ValueError if partial output is manually attempted.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** L. Atomic Loading; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T083 — No partial complete-set success

- **Test ID:** RUN-01-T083
- **Scenario:** No partial complete-set success.
- **Objective:** Establish the no partial complete-set success requirement without weakening authority, integrity or runtime boundaries.
- **Component:** atomic coordinator/result.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use at least two actually approved artifacts; arrange the named first/later mandatory read/decode/compatibility failure while all other prerequisites remain valid. Scenario-specific variation: No partial complete-set success.
- **Expected Result:** Success contains all manifest members; any mandatory failure yields no public loaded_set and no active registry side effect. Named requirement: No partial complete-set success.
- **Expected Diagnostics:** Original reader/decode cause plus corresponding RUN-006/011/012/013; non-success invariant ValueError if partial output is manually attempted.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** L. Atomic Loading; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T084 — No active runtime registry mutation

- **Test ID:** RUN-01-T084
- **Scenario:** No active runtime registry mutation.
- **Objective:** Establish the no active runtime registry mutation requirement without weakening authority, integrity or runtime boundaries.
- **Component:** atomic coordinator/result.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use at least two actually approved artifacts; arrange the named first/later mandatory read/decode/compatibility failure while all other prerequisites remain valid. Scenario-specific variation: No active runtime registry mutation.
- **Expected Result:** Success contains all manifest members; any mandatory failure yields no public loaded_set and no active registry side effect. Named requirement: No active runtime registry mutation.
- **Expected Diagnostics:** Original reader/decode cause plus corresponding RUN-006/011/012/013; non-success invariant ValueError if partial output is manually attempted.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** L. Atomic Loading; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## M. Determinism

### RUN-01-T085 — Stable artifact load order

- **Test ID:** RUN-01-T085
- **Scenario:** Stable artifact load order.
- **Objective:** Establish the stable artifact load order requirement without weakening authority, integrity or runtime boundaries.
- **Component:** deterministic loading/comparison.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** At a future fixed revision, use the same trusted binding, verified bytes, authority references, policy and exact decoder classes/options; vary only the named ordering/configuration concern. Scenario-specific variation: Stable artifact load order.
- **Expected Result:** Manifest order and diagnostic associations are stable; equivalent supported observations compare equal without rerun or timestamp/global state. Named requirement: Stable artifact load order.
- **Expected Diagnostics:** No diagnostic for equivalent supported observations; ValueError for cross-binding successful comparison; changed decoder/value returns unequal.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** M. Determinism; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T086 — Stable decoder selection

- **Test ID:** RUN-01-T086
- **Scenario:** Stable decoder selection.
- **Objective:** Establish the stable decoder selection requirement without weakening authority, integrity or runtime boundaries.
- **Component:** deterministic loading/comparison.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** At a future fixed revision, use the same trusted binding, verified bytes, authority references, policy and exact decoder classes/options; vary only the named ordering/configuration concern. Scenario-specific variation: Stable decoder selection.
- **Expected Result:** Manifest order and diagnostic associations are stable; equivalent supported observations compare equal without rerun or timestamp/global state. Named requirement: Stable decoder selection.
- **Expected Diagnostics:** No diagnostic for equivalent supported observations; ValueError for cross-binding successful comparison; changed decoder/value returns unequal.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** M. Determinism; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T087 — Equivalent immutable load results

- **Test ID:** RUN-01-T087
- **Scenario:** Equivalent immutable load results.
- **Objective:** Establish the equivalent immutable load results requirement without weakening authority, integrity or runtime boundaries.
- **Component:** deterministic loading/comparison.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Compare two actual outcomes with the same original binding, authority scope, policy, verified source evidence, concrete decoder classes/options and representation values.
- **Expected Result:** RuntimeArtifactLoadEquivalence reports equivalent supported observations; no rerun or authenticity claim.
- **Expected Diagnostics:** None; different successful binding is explicitly unsupported ValueError.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** M. Determinism; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T088 — Stable diagnostics

- **Test ID:** RUN-01-T088
- **Scenario:** Stable diagnostics.
- **Objective:** Establish the stable diagnostics requirement without weakening authority, integrity or runtime boundaries.
- **Component:** deterministic loading/comparison.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** At a future fixed revision, use the same trusted binding, verified bytes, authority references, policy and exact decoder classes/options; vary only the named ordering/configuration concern. Scenario-specific variation: Stable diagnostics.
- **Expected Result:** Manifest order and diagnostic associations are stable; equivalent supported observations compare equal without rerun or timestamp/global state. Named requirement: Stable diagnostics.
- **Expected Diagnostics:** No diagnostic for equivalent supported observations; ValueError for cross-binding successful comparison; changed decoder/value returns unequal.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** M. Determinism; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T089 — No timestamp dependency

- **Test ID:** RUN-01-T089
- **Scenario:** No timestamp dependency.
- **Objective:** Establish the no timestamp dependency requirement without weakening authority, integrity or runtime boundaries.
- **Component:** deterministic loading/comparison.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** At a future fixed revision, use the same trusted binding, verified bytes, authority references, policy and exact decoder classes/options; vary only the named ordering/configuration concern. Scenario-specific variation: No timestamp dependency.
- **Expected Result:** Manifest order and diagnostic associations are stable; equivalent supported observations compare equal without rerun or timestamp/global state. Named requirement: No timestamp dependency.
- **Expected Diagnostics:** No diagnostic for equivalent supported observations; ValueError for cross-binding successful comparison; changed decoder/value returns unequal.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** M. Determinism; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T090 — No global mutable state

- **Test ID:** RUN-01-T090
- **Scenario:** No global mutable state.
- **Objective:** Establish the no global mutable state requirement without weakening authority, integrity or runtime boundaries.
- **Component:** deterministic loading/comparison.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** At a future fixed revision, use the same trusted binding, verified bytes, authority references, policy and exact decoder classes/options; vary only the named ordering/configuration concern. Scenario-specific variation: No global mutable state.
- **Expected Result:** Manifest order and diagnostic associations are stable; equivalent supported observations compare equal without rerun or timestamp/global state. Named requirement: No global mutable state.
- **Expected Diagnostics:** No diagnostic for equivalent supported observations; ValueError for cross-binding successful comparison; changed decoder/value returns unequal.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** M. Determinism; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## N. Resource Limits

### RUN-01-T091 — Maximum artifact count

- **Test ID:** RUN-01-T091
- **Scenario:** Maximum artifact count.
- **Objective:** Establish the maximum artifact count requirement without weakening authority, integrity or runtime boundaries.
- **Component:** effective resource policy.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use actual integer limits and inspect declared count/bytes plus decoder depth/elements/scalars at limit-1, limit and limit+1; vary invalid Boolean/zero/negative and client/server ceilings. Scenario-specific variation: Maximum artifact count.
- **Expected Result:** Trusted minima are enforced before reads and during approved parsing/inspection; exceeding any mandatory limit fails with no output. Named requirement: Maximum artifact count.
- **Expected Diagnostics:** RUN-018 runtime bounds; original CMP-072 byte/count preflight; policy ValueError for invalid limits.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** N. Resource Limits; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T092 — Maximum artifact bytes

- **Test ID:** RUN-01-T092
- **Scenario:** Maximum artifact bytes.
- **Objective:** Establish the maximum artifact bytes requirement without weakening authority, integrity or runtime boundaries.
- **Component:** effective resource policy.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use actual integer limits and inspect declared count/bytes plus decoder depth/elements/scalars at limit-1, limit and limit+1; vary invalid Boolean/zero/negative and client/server ceilings. Scenario-specific variation: Maximum artifact bytes.
- **Expected Result:** Trusted minima are enforced before reads and during approved parsing/inspection; exceeding any mandatory limit fails with no output. Named requirement: Maximum artifact bytes.
- **Expected Diagnostics:** RUN-018 runtime bounds; original CMP-072 byte/count preflight; policy ValueError for invalid limits.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** N. Resource Limits; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T093 — Maximum aggregate bytes

- **Test ID:** RUN-01-T093
- **Scenario:** Maximum aggregate bytes.
- **Objective:** Establish the maximum aggregate bytes requirement without weakening authority, integrity or runtime boundaries.
- **Component:** effective resource policy.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use actual integer limits and inspect declared count/bytes plus decoder depth/elements/scalars at limit-1, limit and limit+1; vary invalid Boolean/zero/negative and client/server ceilings. Scenario-specific variation: Maximum aggregate bytes.
- **Expected Result:** Trusted minima are enforced before reads and during approved parsing/inspection; exceeding any mandatory limit fails with no output. Named requirement: Maximum aggregate bytes.
- **Expected Diagnostics:** RUN-018 runtime bounds; original CMP-072 byte/count preflight; policy ValueError for invalid limits.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** N. Resource Limits; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T094 — Maximum decoded structure depth

- **Test ID:** RUN-01-T094
- **Scenario:** Maximum decoded structure depth.
- **Objective:** Establish the maximum decoded structure depth requirement without weakening authority, integrity or runtime boundaries.
- **Component:** effective resource policy.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** With an approved bounded parser, use graph depth D-1, D, D+1 with root depth 1 and every tuple/dataclass/scalar occurrence counted.
- **Expected Result:** Within-depth graphs accepted if other budgets allow; D+1 rejected before successful output.
- **Expected Diagnostics:** RUN-018.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** N. Resource Limits; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T095 — Maximum decoded element count

- **Test ID:** RUN-01-T095
- **Scenario:** Maximum decoded element count.
- **Objective:** Establish the maximum decoded element count requirement without weakening authority, integrity or runtime boundaries.
- **Component:** effective resource policy.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use aggregate occurrence counts N-1, N, N+1 across multiple artifacts and a wide pending frontier.
- **Expected Result:** Per-parser remaining budget plus final aggregate guard prevents extra allocation/output; repeated leaves count each occurrence.
- **Expected Diagnostics:** RUN-018.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** N. Resource Limits; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T096 — Invalid limits

- **Test ID:** RUN-01-T096
- **Scenario:** Invalid limits.
- **Objective:** Establish the invalid limits requirement without weakening authority, integrity or runtime boundaries.
- **Component:** effective resource policy.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use actual integer limits and inspect declared count/bytes plus decoder depth/elements/scalars at limit-1, limit and limit+1; vary invalid Boolean/zero/negative and client/server ceilings. Scenario-specific variation: Invalid limits.
- **Expected Result:** Trusted minima are enforced before reads and during approved parsing/inspection; exceeding any mandatory limit fails with no output. Named requirement: Invalid limits.
- **Expected Diagnostics:** RUN-018 runtime bounds; original CMP-072 byte/count preflight; policy ValueError for invalid limits.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** N. Resource Limits; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T097 — No unbounded recursive decoding

- **Test ID:** RUN-01-T097
- **Scenario:** No unbounded recursive decoding.
- **Objective:** Establish the no unbounded recursive decoding requirement without weakening authority, integrity or runtime boundaries.
- **Component:** effective resource policy.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use actual integer limits and inspect declared count/bytes plus decoder depth/elements/scalars at limit-1, limit and limit+1; vary invalid Boolean/zero/negative and client/server ceilings. Scenario-specific variation: No unbounded recursive decoding.
- **Expected Result:** Trusted minima are enforced before reads and during approved parsing/inspection; exceeding any mandatory limit fails with no output. Named requirement: No unbounded recursive decoding.
- **Expected Diagnostics:** RUN-018 runtime bounds; original CMP-072 byte/count preflight; policy ValueError for invalid limits.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** N. Resource Limits; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## O. Diagnostics

### RUN-01-T098 — Invalid request

- **Test ID:** RUN-01-T098
- **Scenario:** Invalid request.
- **Objective:** Establish the invalid request requirement without weakening authority, integrity or runtime boundaries.
- **Component:** structured diagnostics.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Pass None, dict, bool and SemanticIREnvelope as the loader/application request root.
- **Expected Result:** FAILED with no read/decoder invocation or loaded set.
- **Expected Diagnostics:** RUN-001.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** O. Diagnostics; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T099 — Missing authorization

- **Test ID:** RUN-01-T099
- **Scenario:** Missing authorization.
- **Objective:** Establish the missing authorization requirement without weakening authority, integrity or runtime boundaries.
- **Component:** structured diagnostics.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Trigger the named failure through an otherwise valid actual bound request; retain manifest/key/kind/context/target/origins/stage and original reader objects. Scenario-specific variation: Missing authorization.
- **Expected Result:** Exact stage/category/association and original severity/order survive; no bytes, credentials, absolute paths or fabricated locations are disclosed. Named requirement: Missing authorization.
- **Expected Diagnostics:** Corresponding RUN-001 through RUN-021 as documented; original CMP cause code/message/association preserved in application result.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** O. Diagnostics; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T100 — Manifest mismatch

- **Test ID:** RUN-01-T100
- **Scenario:** Manifest mismatch.
- **Objective:** Establish the manifest mismatch requirement without weakening authority, integrity or runtime boundaries.
- **Component:** structured diagnostics.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Trigger the named failure through an otherwise valid actual bound request; retain manifest/key/kind/context/target/origins/stage and original reader objects. Scenario-specific variation: Manifest mismatch.
- **Expected Result:** Exact stage/category/association and original severity/order survive; no bytes, credentials, absolute paths or fabricated locations are disclosed. Named requirement: Manifest mismatch.
- **Expected Diagnostics:** Corresponding RUN-001 through RUN-021 as documented; original CMP cause code/message/association preserved in application result.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** O. Diagnostics; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T101 — Receipt mismatch

- **Test ID:** RUN-01-T101
- **Scenario:** Receipt mismatch.
- **Objective:** Establish the receipt mismatch requirement without weakening authority, integrity or runtime boundaries.
- **Component:** structured diagnostics.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Trigger the named failure through an otherwise valid actual bound request; retain manifest/key/kind/context/target/origins/stage and original reader objects. Scenario-specific variation: Receipt mismatch.
- **Expected Result:** Exact stage/category/association and original severity/order survive; no bytes, credentials, absolute paths or fabricated locations are disclosed. Named requirement: Receipt mismatch.
- **Expected Diagnostics:** Corresponding RUN-001 through RUN-021 as documented; original CMP cause code/message/association preserved in application result.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** O. Diagnostics; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T102 — Reader failure

- **Test ID:** RUN-01-T102
- **Scenario:** Reader failure.
- **Objective:** Establish the reader failure requirement without weakening authority, integrity or runtime boundaries.
- **Component:** structured diagnostics.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Trigger the named failure through an otherwise valid actual bound request; retain manifest/key/kind/context/target/origins/stage and original reader objects. Scenario-specific variation: Reader failure.
- **Expected Result:** Exact stage/category/association and original severity/order survive; no bytes, credentials, absolute paths or fabricated locations are disclosed. Named requirement: Reader failure.
- **Expected Diagnostics:** Corresponding RUN-001 through RUN-021 as documented; original CMP cause code/message/association preserved in application result.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** O. Diagnostics; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T103 — Unsupported artifact kind

- **Test ID:** RUN-01-T103
- **Scenario:** Unsupported artifact kind.
- **Objective:** Establish the unsupported artifact kind requirement without weakening authority, integrity or runtime boundaries.
- **Component:** structured diagnostics.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Trigger the named failure through an otherwise valid actual bound request; retain manifest/key/kind/context/target/origins/stage and original reader objects. Scenario-specific variation: Unsupported artifact kind.
- **Expected Result:** Exact stage/category/association and original severity/order survive; no bytes, credentials, absolute paths or fabricated locations are disclosed. Named requirement: Unsupported artifact kind.
- **Expected Diagnostics:** Corresponding RUN-001 through RUN-021 as documented; original CMP cause code/message/association preserved in application result.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** O. Diagnostics; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T104 — Unsupported format version

- **Test ID:** RUN-01-T104
- **Scenario:** Unsupported format version.
- **Objective:** Establish the unsupported format version requirement without weakening authority, integrity or runtime boundaries.
- **Component:** structured diagnostics.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Trigger the named failure through an otherwise valid actual bound request; retain manifest/key/kind/context/target/origins/stage and original reader objects. Scenario-specific variation: Unsupported format version.
- **Expected Result:** Exact stage/category/association and original severity/order survive; no bytes, credentials, absolute paths or fabricated locations are disclosed. Named requirement: Unsupported format version.
- **Expected Diagnostics:** Corresponding RUN-001 through RUN-021 as documented; original CMP cause code/message/association preserved in application result.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** O. Diagnostics; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T105 — Decoder unavailable

- **Test ID:** RUN-01-T105
- **Scenario:** Decoder unavailable.
- **Objective:** Establish the decoder unavailable requirement without weakening authority, integrity or runtime boundaries.
- **Component:** structured diagnostics.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Trigger the named failure through an otherwise valid actual bound request; retain manifest/key/kind/context/target/origins/stage and original reader objects. Scenario-specific variation: Decoder unavailable.
- **Expected Result:** Exact stage/category/association and original severity/order survive; no bytes, credentials, absolute paths or fabricated locations are disclosed. Named requirement: Decoder unavailable.
- **Expected Diagnostics:** Corresponding RUN-001 through RUN-021 as documented; original CMP cause code/message/association preserved in application result.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** O. Diagnostics; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T106 — Decoding failure

- **Test ID:** RUN-01-T106
- **Scenario:** Decoding failure.
- **Objective:** Establish the decoding failure requirement without weakening authority, integrity or runtime boundaries.
- **Component:** structured diagnostics.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Trigger the named failure through an otherwise valid actual bound request; retain manifest/key/kind/context/target/origins/stage and original reader objects. Scenario-specific variation: Decoding failure.
- **Expected Result:** Exact stage/category/association and original severity/order survive; no bytes, credentials, absolute paths or fabricated locations are disclosed. Named requirement: Decoding failure.
- **Expected Diagnostics:** Corresponding RUN-001 through RUN-021 as documented; original CMP cause code/message/association preserved in application result.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** O. Diagnostics; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T107 — Dependency mismatch

- **Test ID:** RUN-01-T107
- **Scenario:** Dependency mismatch.
- **Objective:** Establish the dependency mismatch requirement without weakening authority, integrity or runtime boundaries.
- **Component:** structured diagnostics.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Trigger the named failure through an otherwise valid actual bound request; retain manifest/key/kind/context/target/origins/stage and original reader objects. Scenario-specific variation: Dependency mismatch.
- **Expected Result:** Exact stage/category/association and original severity/order survive; no bytes, credentials, absolute paths or fabricated locations are disclosed. Named requirement: Dependency mismatch.
- **Expected Diagnostics:** Corresponding RUN-001 through RUN-021 as documented; original CMP cause code/message/association preserved in application result.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** O. Diagnostics; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T108 — Context mismatch

- **Test ID:** RUN-01-T108
- **Scenario:** Context mismatch.
- **Objective:** Establish the context mismatch requirement without weakening authority, integrity or runtime boundaries.
- **Component:** structured diagnostics.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Trigger the named failure through an otherwise valid actual bound request; retain manifest/key/kind/context/target/origins/stage and original reader objects. Scenario-specific variation: Context mismatch.
- **Expected Result:** Exact stage/category/association and original severity/order survive; no bytes, credentials, absolute paths or fabricated locations are disclosed. Named requirement: Context mismatch.
- **Expected Diagnostics:** Corresponding RUN-001 through RUN-021 as documented; original CMP cause code/message/association preserved in application result.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** O. Diagnostics; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T109 — Compatibility failure

- **Test ID:** RUN-01-T109
- **Scenario:** Compatibility failure.
- **Objective:** Establish the compatibility failure requirement without weakening authority, integrity or runtime boundaries.
- **Component:** structured diagnostics.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Trigger the named failure through an otherwise valid actual bound request; retain manifest/key/kind/context/target/origins/stage and original reader objects. Scenario-specific variation: Compatibility failure.
- **Expected Result:** Exact stage/category/association and original severity/order survive; no bytes, credentials, absolute paths or fabricated locations are disclosed. Named requirement: Compatibility failure.
- **Expected Diagnostics:** Corresponding RUN-001 through RUN-021 as documented; original CMP cause code/message/association preserved in application result.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** O. Diagnostics; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T110 — Original reader diagnostic preservation

- **Test ID:** RUN-01-T110
- **Scenario:** Original reader diagnostic preservation.
- **Objective:** Establish the original reader diagnostic preservation requirement without weakening authority, integrity or runtime boundaries.
- **Component:** structured diagnostics.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Supply CMP read FAILED/INCOMPLETE or successful INFO/WARNING with concrete original diagnostic objects and associations.
- **Expected Result:** Application wrapper retains the identical original objects in order; neutral projection keeps code/message/severity/stage without relabeling semantic failure.
- **Expected Diagnostics:** RUN-006 wrapper for read non-success; original CMP codes and severities unchanged.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** O. Diagnostics; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## P. Security

### RUN-01-T111 — No arbitrary file access

- **Test ID:** RUN-01-T111
- **Scenario:** No arbitrary file access.
- **Objective:** Establish the no arbitrary file access requirement without weakening authority, integrity or runtime boundaries.
- **Component:** security boundary.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review source and, only with later execution permission, exercise artifact-controlled path/module/code/URL or unauthorized input against the real owned format and authenticated boundary. Scenario-specific variation: No arbitrary file access.
- **Expected Result:** No arbitrary file/network/import/code effect, unsafe object deserialization, secret disclosure or authority bypass; fail closed before unsupported access. Named requirement: No arbitrary file access.
- **Expected Diagnostics:** RUN-001/002/003/008/009/012/020 depending boundary; no success for unsupported malicious input.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** P. Security; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T112 — No pickle execution

- **Test ID:** RUN-01-T112
- **Scenario:** No pickle execution.
- **Objective:** Establish the no pickle execution requirement without weakening authority, integrity or runtime boundaries.
- **Component:** security boundary.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review source and, only with later execution permission, exercise artifact-controlled path/module/code/URL or unauthorized input against the real owned format and authenticated boundary. Scenario-specific variation: No pickle execution.
- **Expected Result:** No arbitrary file/network/import/code effect, unsafe object deserialization, secret disclosure or authority bypass; fail closed before unsupported access. Named requirement: No pickle execution.
- **Expected Diagnostics:** RUN-001/002/003/008/009/012/020 depending boundary; no success for unsupported malicious input.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** P. Security; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T113 — No dynamic import from artifact metadata

- **Test ID:** RUN-01-T113
- **Scenario:** No dynamic import from artifact metadata.
- **Objective:** Establish the no dynamic import from artifact metadata requirement without weakening authority, integrity or runtime boundaries.
- **Component:** security boundary.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review source and, only with later execution permission, exercise artifact-controlled path/module/code/URL or unauthorized input against the real owned format and authenticated boundary. Scenario-specific variation: No dynamic import from artifact metadata.
- **Expected Result:** No arbitrary file/network/import/code effect, unsafe object deserialization, secret disclosure or authority bypass; fail closed before unsupported access. Named requirement: No dynamic import from artifact metadata.
- **Expected Diagnostics:** RUN-001/002/003/008/009/012/020 depending boundary; no success for unsupported malicious input.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** P. Security; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T114 — No `eval()` or `exec()`

- **Test ID:** RUN-01-T114
- **Scenario:** No `eval()` or `exec()`.
- **Objective:** Establish the no `eval()` or `exec()` requirement without weakening authority, integrity or runtime boundaries.
- **Component:** security boundary.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review source and, only with later execution permission, exercise artifact-controlled path/module/code/URL or unauthorized input against the real owned format and authenticated boundary. Scenario-specific variation: No `eval()` or `exec()`.
- **Expected Result:** No arbitrary file/network/import/code effect, unsafe object deserialization, secret disclosure or authority bypass; fail closed before unsupported access. Named requirement: No `eval()` or `exec()`.
- **Expected Diagnostics:** RUN-001/002/003/008/009/012/020 depending boundary; no success for unsupported malicious input.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** P. Security; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T115 — No embedded-code execution

- **Test ID:** RUN-01-T115
- **Scenario:** No embedded-code execution.
- **Objective:** Establish the no embedded-code execution requirement without weakening authority, integrity or runtime boundaries.
- **Component:** security boundary.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review source and, only with later execution permission, exercise artifact-controlled path/module/code/URL or unauthorized input against the real owned format and authenticated boundary. Scenario-specific variation: No embedded-code execution.
- **Expected Result:** No arbitrary file/network/import/code effect, unsafe object deserialization, secret disclosure or authority bypass; fail closed before unsupported access. Named requirement: No embedded-code execution.
- **Expected Diagnostics:** RUN-001/002/003/008/009/012/020 depending boundary; no success for unsupported malicious input.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** P. Security; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T116 — No unapproved network access

- **Test ID:** RUN-01-T116
- **Scenario:** No unapproved network access.
- **Objective:** Establish the no unapproved network access requirement without weakening authority, integrity or runtime boundaries.
- **Component:** security boundary.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review source and, only with later execution permission, exercise artifact-controlled path/module/code/URL or unauthorized input against the real owned format and authenticated boundary. Scenario-specific variation: No unapproved network access.
- **Expected Result:** No arbitrary file/network/import/code effect, unsafe object deserialization, secret disclosure or authority bypass; fail closed before unsupported access. Named requirement: No unapproved network access.
- **Expected Diagnostics:** RUN-001/002/003/008/009/012/020 depending boundary; no success for unsupported malicious input.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** P. Security; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T117 — No leaked credentials

- **Test ID:** RUN-01-T117
- **Scenario:** No leaked credentials.
- **Objective:** Establish the no leaked credentials requirement without weakening authority, integrity or runtime boundaries.
- **Component:** security boundary.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review source and, only with later execution permission, exercise artifact-controlled path/module/code/URL or unauthorized input against the real owned format and authenticated boundary. Scenario-specific variation: No leaked credentials.
- **Expected Result:** No arbitrary file/network/import/code effect, unsafe object deserialization, secret disclosure or authority bypass; fail closed before unsupported access. Named requirement: No leaked credentials.
- **Expected Diagnostics:** RUN-001/002/003/008/009/012/020 depending boundary; no success for unsupported malicious input.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** P. Security; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T118 — No bypass of application authorization

- **Test ID:** RUN-01-T118
- **Scenario:** No bypass of application authorization.
- **Objective:** Establish the no bypass of application authorization requirement without weakening authority, integrity or runtime boundaries.
- **Component:** security boundary.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review source and, only with later execution permission, exercise artifact-controlled path/module/code/URL or unauthorized input against the real owned format and authenticated boundary. Scenario-specific variation: No bypass of application authorization.
- **Expected Result:** No arbitrary file/network/import/code effect, unsafe object deserialization, secret disclosure or authority bypass; fail closed before unsupported access. Named requirement: No bypass of application authorization.
- **Expected Diagnostics:** RUN-001/002/003/008/009/012/020 depending boundary; no success for unsupported malicious input.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** P. Security; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## Q. Django / DRF

### RUN-01-T119 — Pure Python runtime domain

- **Test ID:** RUN-01-T119
- **Scenario:** Pure Python runtime domain.
- **Objective:** Establish the pure python runtime domain requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Django/DRF integration ownership.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Inspect pure runtime and constrained tooling declarations; future authorized HTTP integration must use actual installed Django/DRF authentication/permissions and server ceilings. Scenario-specific variation: Pure Python runtime domain.
- **Expected Result:** No framework/ORM import in Runtime, migrations or unnecessary endpoint; future adapter delegates typed service outcomes and does not disclose bytes. Named requirement: Pure Python runtime domain.
- **Expected Diagnostics:** No HTTP success claim while adapter/auth is unavailable; architecture rule failure if forbidden imports are introduced; RUN-002 for unavailable authority.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** Q. Django / DRF; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T120 — No Django ORM coupling

- **Test ID:** RUN-01-T120
- **Scenario:** No Django ORM coupling.
- **Objective:** Establish the no django orm coupling requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Django/DRF integration ownership.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Inspect pure runtime and constrained tooling declarations; future authorized HTTP integration must use actual installed Django/DRF authentication/permissions and server ceilings. Scenario-specific variation: No Django ORM coupling.
- **Expected Result:** No framework/ORM import in Runtime, migrations or unnecessary endpoint; future adapter delegates typed service outcomes and does not disclose bytes. Named requirement: No Django ORM coupling.
- **Expected Diagnostics:** No HTTP success claim while adapter/auth is unavailable; architecture rule failure if forbidden imports are introduced; RUN-002 for unavailable authority.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** Q. Django / DRF; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T121 — No migrations

- **Test ID:** RUN-01-T121
- **Scenario:** No migrations.
- **Objective:** Establish the no migrations requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Django/DRF integration ownership.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Inspect pure runtime and constrained tooling declarations; future authorized HTTP integration must use actual installed Django/DRF authentication/permissions and server ceilings. Scenario-specific variation: No migrations.
- **Expected Result:** No framework/ORM import in Runtime, migrations or unnecessary endpoint; future adapter delegates typed service outcomes and does not disclose bytes. Named requirement: No migrations.
- **Expected Diagnostics:** No HTTP success claim while adapter/auth is unavailable; architecture rule failure if forbidden imports are introduced; RUN-002 for unavailable authority.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** Q. Django / DRF; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T122 — Existing authorized API integration

- **Test ID:** RUN-01-T122
- **Scenario:** Existing authorized API integration.
- **Objective:** Establish the existing authorized api integration requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Django/DRF integration ownership.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Inspect current adapters/apps: no authenticated API implementation exists; future wiring requires installed Django/DRF and actual permission checks.
- **Expected Result:** No endpoint invented now; internal service and unavailable authorization boundary documented for later approved adapter.
- **Expected Diagnostics:** RUN-002 when authority is absent; not an HTTP success fixture.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** Q. Django / DRF; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T123 — No unnecessary public load endpoint

- **Test ID:** RUN-01-T123
- **Scenario:** No unnecessary public load endpoint.
- **Objective:** Establish the no unnecessary public load endpoint requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Django/DRF integration ownership.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Inspect pure runtime and constrained tooling declarations; future authorized HTTP integration must use actual installed Django/DRF authentication/permissions and server ceilings. Scenario-specific variation: No unnecessary public load endpoint.
- **Expected Result:** No framework/ORM import in Runtime, migrations or unnecessary endpoint; future adapter delegates typed service outcomes and does not disclose bytes. Named requirement: No unnecessary public load endpoint.
- **Expected Diagnostics:** No HTTP success claim while adapter/auth is unavailable; architecture rule failure if forbidden imports are introduced; RUN-002 for unavailable authority.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** Q. Django / DRF; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T124 — Existing authentication and permissions preserved

- **Test ID:** RUN-01-T124
- **Scenario:** Existing authentication and permissions preserved.
- **Objective:** Establish the existing authentication and permissions preserved requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Django/DRF integration ownership.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Inspect pure runtime and constrained tooling declarations; future authorized HTTP integration must use actual installed Django/DRF authentication/permissions and server ceilings. Scenario-specific variation: Existing authentication and permissions preserved.
- **Expected Result:** No framework/ORM import in Runtime, migrations or unnecessary endpoint; future adapter delegates typed service outcomes and does not disclose bytes. Named requirement: Existing authentication and permissions preserved.
- **Expected Diagnostics:** No HTTP success claim while adapter/auth is unavailable; architecture rule failure if forbidden imports are introduced; RUN-002 for unavailable authority.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** Q. Django / DRF; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T125 — No raw artifact content disclosure

- **Test ID:** RUN-01-T125
- **Scenario:** No raw artifact content disclosure.
- **Objective:** Establish the no raw artifact content disclosure requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Django/DRF integration ownership.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Inspect pure runtime and constrained tooling declarations; future authorized HTTP integration must use actual installed Django/DRF authentication/permissions and server ceilings. Scenario-specific variation: No raw artifact content disclosure.
- **Expected Result:** No framework/ORM import in Runtime, migrations or unnecessary endpoint; future adapter delegates typed service outcomes and does not disclose bytes. Named requirement: No raw artifact content disclosure.
- **Expected Diagnostics:** No HTTP success claim while adapter/auth is unavailable; architecture rule failure if forbidden imports are introduced; RUN-002 for unavailable authority.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** Q. Django / DRF; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## R. Mini Sales

### RUN-01-T126 — Customer runtime artifact load

- **Test ID:** RUN-01-T126
- **Scenario:** Customer runtime artifact load.
- **Objective:** Establish the customer runtime artifact load requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Mini Sales conceptual integration.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use Customer’s actual UUIDv4 exact origin only after a real producer/runtime format and decoder have been approved and materialized with digest evidence.
- **Expected Result:** Full inactive loaded Customer definition preserves only encoded metadata; current capability gap must not be fabricated into a successful scenario.
- **Expected Diagnostics:** Default missing authority RUN-002; no approved kind RUN-008; future valid path no errors.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** R. Mini Sales; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T127 — Employee runtime artifact load

- **Test ID:** RUN-01-T127
- **Scenario:** Employee runtime artifact load.
- **Objective:** Establish the employee runtime artifact load requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Mini Sales conceptual integration.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use actual Customer sem_...000001@1.0.0 and Employee sem_...000002@1.0.0 in context sem_...999999999999, only after genuine runtime producer/encoder/decoder/authority exist; vary the named condition. Scenario-specific variation: Employee runtime artifact load.
- **Expected Result:** Preserve encoded exact identity/context/self-reference without constructing business records; full success is inactive and requires all real prerequisites. Named requirement: Employee runtime artifact load.
- **Expected Diagnostics:** RUN-002 authority, RUN-008 unknown kind/RUN-011 recognized missing decoder, RUN-010 version, RUN-006 original missing-file cause, RUN-014 context.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** R. Mini Sales; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T128 — Exact Customer@1.0.0 semantic origin

- **Test ID:** RUN-01-T128
- **Scenario:** Exact Customer@1.0.0 semantic origin.
- **Objective:** Establish the exact customer@1.0.0 semantic origin requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Mini Sales conceptual integration.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use actual Customer sem_...000001@1.0.0 and Employee sem_...000002@1.0.0 in context sem_...999999999999, only after genuine runtime producer/encoder/decoder/authority exist; vary the named condition. Scenario-specific variation: Exact Customer@1.0.0 semantic origin.
- **Expected Result:** Preserve encoded exact identity/context/self-reference without constructing business records; full success is inactive and requires all real prerequisites. Named requirement: Exact Customer@1.0.0 semantic origin.
- **Expected Diagnostics:** RUN-002 authority, RUN-008 unknown kind/RUN-011 recognized missing decoder, RUN-010 version, RUN-006 original missing-file cause, RUN-014 context.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** R. Mini Sales; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T129 — Employee self-reference preservation

- **Test ID:** RUN-01-T129
- **Scenario:** Employee self-reference preservation.
- **Objective:** Establish the employee self-reference preservation requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Mini Sales conceptual integration.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Future approved Employee representation encodes its existing stable semantic self-reference as an immutable value leaf; do not construct an Employee instance graph.
- **Expected Result:** Reference identity retained without recursive business object construction or inferred artifact dependency.
- **Expected Diagnostics:** No cycle error for semantic reference; unapproved representation leaf RUN-020.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** R. Mini Sales; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T130 — Missing Customer decoder

- **Test ID:** RUN-01-T130
- **Scenario:** Missing Customer decoder.
- **Objective:** Establish the missing customer decoder requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Mini Sales conceptual integration.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use actual Customer sem_...000001@1.0.0 and Employee sem_...000002@1.0.0 in context sem_...999999999999, only after genuine runtime producer/encoder/decoder/authority exist; vary the named condition. Scenario-specific variation: Missing Customer decoder.
- **Expected Result:** Preserve encoded exact identity/context/self-reference without constructing business records; full success is inactive and requires all real prerequisites. Named requirement: Missing Customer decoder.
- **Expected Diagnostics:** RUN-002 authority, RUN-008 unknown kind/RUN-011 recognized missing decoder, RUN-010 version, RUN-006 original missing-file cause, RUN-014 context.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** R. Mini Sales; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T131 — Unsupported Employee format version

- **Test ID:** RUN-01-T131
- **Scenario:** Unsupported Employee format version.
- **Objective:** Establish the unsupported employee format version requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Mini Sales conceptual integration.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use actual Customer sem_...000001@1.0.0 and Employee sem_...000002@1.0.0 in context sem_...999999999999, only after genuine runtime producer/encoder/decoder/authority exist; vary the named condition. Scenario-specific variation: Unsupported Employee format version.
- **Expected Result:** Preserve encoded exact identity/context/self-reference without constructing business records; full success is inactive and requires all real prerequisites. Named requirement: Unsupported Employee format version.
- **Expected Diagnostics:** RUN-002 authority, RUN-008 unknown kind/RUN-011 recognized missing decoder, RUN-010 version, RUN-006 original missing-file cause, RUN-014 context.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** R. Mini Sales; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T132 — Missing Employee artifact bytes

- **Test ID:** RUN-01-T132
- **Scenario:** Missing Employee artifact bytes.
- **Objective:** Establish the missing employee artifact bytes requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Mini Sales conceptual integration.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use actual Customer sem_...000001@1.0.0 and Employee sem_...000002@1.0.0 in context sem_...999999999999, only after genuine runtime producer/encoder/decoder/authority exist; vary the named condition. Scenario-specific variation: Missing Employee artifact bytes.
- **Expected Result:** Preserve encoded exact identity/context/self-reference without constructing business records; full success is inactive and requires all real prerequisites. Named requirement: Missing Employee artifact bytes.
- **Expected Diagnostics:** RUN-002 authority, RUN-008 unknown kind/RUN-011 recognized missing decoder, RUN-010 version, RUN-006 original missing-file cause, RUN-014 context.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** R. Mini Sales; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T133 — Semantic context mismatch

- **Test ID:** RUN-01-T133
- **Scenario:** Semantic context mismatch.
- **Objective:** Establish the semantic context mismatch requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Mini Sales conceptual integration.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use actual Customer sem_...000001@1.0.0 and Employee sem_...000002@1.0.0 in context sem_...999999999999, only after genuine runtime producer/encoder/decoder/authority exist; vary the named condition. Scenario-specific variation: Semantic context mismatch.
- **Expected Result:** Preserve encoded exact identity/context/self-reference without constructing business records; full success is inactive and requires all real prerequisites. Named requirement: Semantic context mismatch.
- **Expected Diagnostics:** RUN-002 authority, RUN-008 unknown kind/RUN-011 recognized missing decoder, RUN-010 version, RUN-006 original missing-file cause, RUN-014 context.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** R. Mini Sales; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T134 — Missing trusted authorization

- **Test ID:** RUN-01-T134
- **Scenario:** Missing trusted authorization.
- **Objective:** Establish the missing trusted authorization requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Mini Sales conceptual integration.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use actual Customer sem_...000001@1.0.0 and Employee sem_...000002@1.0.0 in context sem_...999999999999, only after genuine runtime producer/encoder/decoder/authority exist; vary the named condition. Scenario-specific variation: Missing trusted authorization.
- **Expected Result:** Preserve encoded exact identity/context/self-reference without constructing business records; full success is inactive and requires all real prerequisites. Named requirement: Missing trusted authorization.
- **Expected Diagnostics:** RUN-002 authority, RUN-008 unknown kind/RUN-011 recognized missing decoder, RUN-010 version, RUN-006 original missing-file cause, RUN-014 context.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** R. Mini Sales; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T135 — Successful load without activation

- **Test ID:** RUN-01-T135
- **Scenario:** Successful load without activation.
- **Objective:** Establish the successful load without activation requirement without weakening authority, integrity or runtime boundaries.
- **Component:** Mini Sales conceptual integration.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Use actual Customer sem_...000001@1.0.0 and Employee sem_...000002@1.0.0 in context sem_...999999999999, only after genuine runtime producer/encoder/decoder/authority exist; vary the named condition. Scenario-specific variation: Successful load without activation.
- **Expected Result:** Preserve encoded exact identity/context/self-reference without constructing business records; full success is inactive and requires all real prerequisites. Named requirement: Successful load without activation.
- **Expected Diagnostics:** RUN-002 authority, RUN-008 unknown kind/RUN-011 recognized missing decoder, RUN-010 version, RUN-006 original missing-file cause, RUN-014 context.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** R. Mini Sales; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## S. Architectural Boundaries

### RUN-01-T136 — No authoring parsing

- **Test ID:** RUN-01-T136
- **Scenario:** No authoring parsing.
- **Objective:** Establish the no authoring parsing requirement without weakening authority, integrity or runtime boundaries.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review production imports/call sites and future call observations for the named excluded authoring/compiler/storage/publication/activation/execution capability. Scenario-specific variation: No authoring parsing.
- **Expected Result:** RUN-01 performs no named excluded capability and obtains bytes only from existing CMP-09; no next-stage implementation is automatically started. Named requirement: No authoring parsing.
- **Expected Diagnostics:** Architecture rule diagnostics if forbidden edges exist; unsupported input RUN-001/008/009 rather than an invented fallback.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** S. Architectural Boundaries; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T137 — No namespace resolution

- **Test ID:** RUN-01-T137
- **Scenario:** No namespace resolution.
- **Objective:** Establish the no namespace resolution requirement without weakening authority, integrity or runtime boundaries.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review production imports/call sites and future call observations for the named excluded authoring/compiler/storage/publication/activation/execution capability. Scenario-specific variation: No namespace resolution.
- **Expected Result:** RUN-01 performs no named excluded capability and obtains bytes only from existing CMP-09; no next-stage implementation is automatically started. Named requirement: No namespace resolution.
- **Expected Diagnostics:** Architecture rule diagnostics if forbidden edges exist; unsupported input RUN-001/008/009 rather than an invented fallback.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** S. Architectural Boundaries; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T138 — No canonicalization

- **Test ID:** RUN-01-T138
- **Scenario:** No canonicalization.
- **Objective:** Establish the no canonicalization requirement without weakening authority, integrity or runtime boundaries.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review production imports/call sites and future call observations for the named excluded authoring/compiler/storage/publication/activation/execution capability. Scenario-specific variation: No canonicalization.
- **Expected Result:** RUN-01 performs no named excluded capability and obtains bytes only from existing CMP-09; no next-stage implementation is automatically started. Named requirement: No canonicalization.
- **Expected Diagnostics:** Architecture rule diagnostics if forbidden edges exist; unsupported input RUN-001/008/009 rather than an invented fallback.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** S. Architectural Boundaries; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T139 — No semantic validation reimplementation

- **Test ID:** RUN-01-T139
- **Scenario:** No semantic validation reimplementation.
- **Objective:** Establish the no semantic validation reimplementation requirement without weakening authority, integrity or runtime boundaries.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review production imports/call sites and future call observations for the named excluded authoring/compiler/storage/publication/activation/execution capability. Scenario-specific variation: No semantic validation reimplementation.
- **Expected Result:** RUN-01 performs no named excluded capability and obtains bytes only from existing CMP-09; no next-stage implementation is automatically started. Named requirement: No semantic validation reimplementation.
- **Expected Diagnostics:** Architecture rule diagnostics if forbidden edges exist; unsupported input RUN-001/008/009 rather than an invented fallback.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** S. Architectural Boundaries; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T140 — No Type IR lowering

- **Test ID:** RUN-01-T140
- **Scenario:** No Type IR lowering.
- **Objective:** Establish the no type ir lowering requirement without weakening authority, integrity or runtime boundaries.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review production imports/call sites and future call observations for the named excluded authoring/compiler/storage/publication/activation/execution capability. Scenario-specific variation: No Type IR lowering.
- **Expected Result:** RUN-01 performs no named excluded capability and obtains bytes only from existing CMP-09; no next-stage implementation is automatically started. Named requirement: No Type IR lowering.
- **Expected Diagnostics:** Architecture rule diagnostics if forbidden edges exist; unsupported input RUN-001/008/009 rather than an invented fallback.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** S. Architectural Boundaries; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T141 — No artifact generation

- **Test ID:** RUN-01-T141
- **Scenario:** No artifact generation.
- **Objective:** Establish the no artifact generation requirement without weakening authority, integrity or runtime boundaries.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review production imports/call sites and future call observations for the named excluded authoring/compiler/storage/publication/activation/execution capability. Scenario-specific variation: No artifact generation.
- **Expected Result:** RUN-01 performs no named excluded capability and obtains bytes only from existing CMP-09; no next-stage implementation is automatically started. Named requirement: No artifact generation.
- **Expected Diagnostics:** Architecture rule diagnostics if forbidden edges exist; unsupported input RUN-001/008/009 rather than an invented fallback.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** S. Architectural Boundaries; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T142 — No artifact writing

- **Test ID:** RUN-01-T142
- **Scenario:** No artifact writing.
- **Objective:** Establish the no artifact writing requirement without weakening authority, integrity or runtime boundaries.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review production imports/call sites and future call observations for the named excluded authoring/compiler/storage/publication/activation/execution capability. Scenario-specific variation: No artifact writing.
- **Expected Result:** RUN-01 performs no named excluded capability and obtains bytes only from existing CMP-09; no next-stage implementation is automatically started. Named requirement: No artifact writing.
- **Expected Diagnostics:** Architecture rule diagnostics if forbidden edges exist; unsupported input RUN-001/008/009 rather than an invented fallback.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** S. Architectural Boundaries; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T143 — No direct filesystem reader duplication

- **Test ID:** RUN-01-T143
- **Scenario:** No direct filesystem reader duplication.
- **Objective:** Establish the no direct filesystem reader duplication requirement without weakening authority, integrity or runtime boundaries.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review production imports/call sites and future call observations for the named excluded authoring/compiler/storage/publication/activation/execution capability. Scenario-specific variation: No direct filesystem reader duplication.
- **Expected Result:** RUN-01 performs no named excluded capability and obtains bytes only from existing CMP-09; no next-stage implementation is automatically started. Named requirement: No direct filesystem reader duplication.
- **Expected Diagnostics:** Architecture rule diagnostics if forbidden edges exist; unsupported input RUN-001/008/009 rather than an invented fallback.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** S. Architectural Boundaries; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T144 — No artifact publication

- **Test ID:** RUN-01-T144
- **Scenario:** No artifact publication.
- **Objective:** Establish the no artifact publication requirement without weakening authority, integrity or runtime boundaries.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review production imports/call sites and future call observations for the named excluded authoring/compiler/storage/publication/activation/execution capability. Scenario-specific variation: No artifact publication.
- **Expected Result:** RUN-01 performs no named excluded capability and obtains bytes only from existing CMP-09; no next-stage implementation is automatically started. Named requirement: No artifact publication.
- **Expected Diagnostics:** Architecture rule diagnostics if forbidden edges exist; unsupported input RUN-001/008/009 rather than an invented fallback.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** S. Architectural Boundaries; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T145 — No runtime registry activation

- **Test ID:** RUN-01-T145
- **Scenario:** No runtime registry activation.
- **Objective:** Establish the no runtime registry activation requirement without weakening authority, integrity or runtime boundaries.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review production imports/call sites and future call observations for the named excluded authoring/compiler/storage/publication/activation/execution capability. Scenario-specific variation: No runtime registry activation.
- **Expected Result:** RUN-01 performs no named excluded capability and obtains bytes only from existing CMP-09; no next-stage implementation is automatically started. Named requirement: No runtime registry activation.
- **Expected Diagnostics:** Architecture rule diagnostics if forbidden edges exist; unsupported input RUN-001/008/009 rather than an invented fallback.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** S. Architectural Boundaries; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T146 — No business execution

- **Test ID:** RUN-01-T146
- **Scenario:** No business execution.
- **Objective:** Establish the no business execution requirement without weakening authority, integrity or runtime boundaries.
- **Component:** architectural non-goals.
- **Prerequisites:** Fixed revision and explicit future execution permission; baseline P or the deliberately absent named prerequisite. Actual approved format/decoder required for any successful decode assertion.
- **Input / Setup:** Review production imports/call sites and future call observations for the named excluded authoring/compiler/storage/publication/activation/execution capability. Scenario-specific variation: No business execution.
- **Expected Result:** RUN-01 performs no named excluded capability and obtains bytes only from existing CMP-09; no next-stage implementation is automatically started. Named requirement: No business execution.
- **Expected Diagnostics:** Architecture rule diagnostics if forbidden edges exist; unsupported input RUN-001/008/009 rather than an invented fallback.
- **Boundary / Edge Cases:** Repeat the named invariant with one versus multiple mandatory artifacts; absent/malformed/exact/mismatched coordinates, first/later failures and limit-1/limit/limit+1 where applicable. Same-looking identity never grants another source scope.
- **Integration Dependencies:** S. Architectural Boundaries; Kernel coordinates, CMP-07/08/09 original evidence, trusted authorizer/reader/decoder ports and pure runtime/application result contracts.
- **Acceptance Criteria:** Exact expected status/construction rejection and diagnostics; complete ordered immutable output only if every prerequisite succeeds; no partial public set, authority expansion, IR fallback or activation. Record actual future execution evidence separately.
- **Execution Status:** NOT_RUN — DEFERRED

## T. Additional implementation-specific boundaries

### RUN-01-T147 — Policy Boolean rejection

- **Test ID:** RUN-01-T147
- **Scenario:** Policy Boolean rejection.
- **Objective:** Verify policy boolean rejection against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Use True/False for each of the six integer policy fields.
- **Expected Result:** Construction rejects each Boolean.
- **Expected Diagnostics:** ValueError.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T148 — Policy zero and negative rejection

- **Test ID:** RUN-01-T148
- **Scenario:** Policy zero and negative rejection.
- **Objective:** Verify policy zero and negative rejection against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Use 0 and -1 for each resource limit.
- **Expected Result:** Construction rejects invalid limits before access.
- **Expected Diagnostics:** ValueError.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T149 — Trusted minima cannot be raised

- **Test ID:** RUN-01-T149
- **Scenario:** Trusted minima cannot be raised.
- **Objective:** Verify trusted minima cannot be raised against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Request each ceiling above server value; retain an even lower original CMP read policy.
- **Expected Result:** Effective runtime and reader ceilings never increase; DIGEST_VERIFIED mandatory.
- **Expected Diagnostics:** RUN-018/CMP-072 on attempted over-limit package.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T150 — Aggregate decoded scalar budget

- **Test ID:** RUN-01-T150
- **Scenario:** Aggregate decoded scalar budget.
- **Objective:** Verify aggregate decoded scalar budget against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Use bytes/text/int leaves whose conservative sum is S-1, S and S+1 across two artifacts.
- **Expected Result:** Only within aggregate scalar budget may return success; second parser gets remaining budget.
- **Expected Diagnostics:** RUN-018 on excess/exhaustion.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T151 — Scalar text accounting

- **Test ID:** RUN-01-T151
- **Scenario:** Scalar text accounting.
- **Objective:** Verify scalar text accounting against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Use Unicode text with S//4 and S//4+1 characters under scalar budget S.
- **Expected Result:** Counts four bytes per character independent of encoding locale.
- **Expected Diagnostics:** RUN-018 when conservative text budget exceeded.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T152 — Integer bit-size accounting

- **Test ID:** RUN-01-T152
- **Scenario:** Integer bit-size accounting.
- **Objective:** Verify integer bit-size accounting against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Use large exact integers and bool leaves in approved representations.
- **Expected Result:** Integer bit-size and one-byte Boolean accounting remain distinct; no str conversion or float fallback.
- **Expected Diagnostics:** RUN-018 when budget exceeded.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T153 — Actual decoded object cycle

- **Test ID:** RUN-01-T153
- **Scenario:** Actual decoded object cycle.
- **Objective:** Verify actual decoded object cycle against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Supply a maliciously constructed approved object cycle to post-decode inspection after future execution permission.
- **Expected Result:** Iterative ancestor guard rejects actual cycles without recursion/hang.
- **Expected Diagnostics:** RUN-020.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T154 — Repeated shared immutable subtree

- **Test ID:** RUN-01-T154
- **Scenario:** Repeated shared immutable subtree.
- **Objective:** Verify repeated shared immutable subtree against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Use the same immutable leaf/subtree multiple times without ancestor cycle.
- **Expected Result:** Occurrences counted individually; sharing is allowed within budgets.
- **Expected Diagnostics:** RUN-018 only when occurrence budget exceeded.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T155 — Pending frontier resource bound

- **Test ID:** RUN-01-T155
- **Scenario:** Pending frontier resource bound.
- **Objective:** Verify pending frontier resource bound against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Use nested wide tuples with total pending nodes exceeding remaining elements before traversing children.
- **Expected Result:** Reject before a large unbounded pending stack is built.
- **Expected Diagnostics:** RUN-018.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T156 — Inherited mutable instance dictionary

- **Test ID:** RUN-01-T156
- **Scenario:** Inherited mutable instance dictionary.
- **Objective:** Verify inherited mutable instance dictionary against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Register a frozen slotted representation inheriting a __dict__-bearing base.
- **Expected Result:** Class approval rejects hidden instance mutability.
- **Expected Diagnostics:** TypeError.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T157 — Mutable decoder configuration

- **Test ID:** RUN-01-T157
- **Scenario:** Mutable decoder configuration.
- **Objective:** Verify mutable decoder configuration against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Register a frozen slotted decoder with list/dict/service/callable configuration fields.
- **Expected Result:** Bounded immutable configuration inspection rejects registration.
- **Expected Diagnostics:** RUN-020 or registration TypeError.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T158 — Decoder parse safety prerequisite

- **Test ID:** RUN-01-T158
- **Scenario:** Decoder parse safety prerequisite.
- **Objective:** Verify decoder parse safety prerequisite against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Attempt registration with enforces_parse_limits=False, None or 1.
- **Expected Result:** Only the actual True trusted safety approval is accepted; no arbitrary sandbox invented.
- **Expected Diagnostics:** ValueError.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T159 — Duplicate decoder dispatch tuple

- **Test ID:** RUN-01-T159
- **Scenario:** Duplicate decoder dispatch tuple.
- **Objective:** Verify duplicate decoder dispatch tuple against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Register two entries with the same kind/format/version/runtime target/compatibility version.
- **Expected Result:** Catalog rejects ambiguous dispatch regardless of equal implementation.
- **Expected Diagnostics:** ValueError.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T160 — Catalog ordering independence

- **Test ID:** RUN-01-T160
- **Scenario:** Catalog ordering independence.
- **Objective:** Verify catalog ordering independence against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Build catalog from the same legitimate entries in reverse order.
- **Expected Result:** Stable dispatch tuple ordering and selected implementation are unchanged.
- **Expected Diagnostics:** No diagnostic.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T161 — Recognized kind without decoder

- **Test ID:** RUN-01-T161
- **Scenario:** Recognized kind without decoder.
- **Objective:** Verify recognized kind without decoder against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Declare a real recognized producer kind with content metadata and no registered decoder.
- **Expected Result:** INCOMPLETE before byte retrieval.
- **Expected Diagnostics:** RUN-011.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T162 — Combined kind inventory ceiling

- **Test ID:** RUN-01-T162
- **Scenario:** Combined kind inventory ceiling.
- **Objective:** Verify combined kind inventory ceiling against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Use registration and recognized-kind inventories whose union exceeds 128.
- **Expected Result:** Catalog construction rejects the combined excess.
- **Expected Diagnostics:** ValueError.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T163 — Legacy content declaration absent

- **Test ID:** RUN-01-T163
- **Scenario:** Legacy content declaration absent.
- **Objective:** Verify legacy content declaration absent against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Use existing RuntimeArtifactMetadata positional construction with no content declaration.
- **Expected Result:** Legacy compiler/manifest contracts remain valid; recognized runtime kind has unavailable format.
- **Expected Diagnostics:** RUN-009, not a fabricated encoding.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T164 — Distinct version namespaces

- **Test ID:** RUN-01-T164
- **Scenario:** Distinct version namespaces.
- **Objective:** Verify distinct version namespaces against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Substitute SemanticVersion or manifest schema Enum for RuntimeArtifactFormatVersion or compatibility version.
- **Expected Result:** Content contract rejects types; no automatic cross-version reinterpretation.
- **Expected Diagnostics:** TypeError.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T165 — Capability normalization and duplicates

- **Test ID:** RUN-01-T165
- **Scenario:** Capability normalization and duplicates.
- **Objective:** Verify capability normalization and duplicates against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Declare unordered distinct requirements, then duplicate/over-128 requirements.
- **Expected Result:** Distinct requirements normalized; duplicates/excess rejected.
- **Expected Diagnostics:** ValueError for invalid inventory.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T166 — Model-wide origin preservation

- **Test ID:** RUN-01-T166
- **Scenario:** Model-wide origin preservation.
- **Objective:** Verify model-wide origin preservation against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Use metadata model_wide=True, origins=(), and matching approved representation; then flip the decoded flag.
- **Expected Result:** Matching origin contract accepted; mismatch rejected without fabricating one-to-one origins.
- **Expected Diagnostics:** RUN-020 on mismatch.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T167 — Multiple exact semantic origins

- **Test ID:** RUN-01-T167
- **Scenario:** Multiple exact semantic origins.
- **Objective:** Verify multiple exact semantic origins against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Use a producer-supported multi-origin artifact with exact sorted ElementVersionRef tuple.
- **Expected Result:** No origin dropped or replaced with QName/latest text.
- **Expected Diagnostics:** RUN-020 on altered origin tuple.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T168 — Declared metadata resource bound

- **Test ID:** RUN-01-T168
- **Scenario:** Declared metadata resource bound.
- **Objective:** Verify declared metadata resource bound against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Supply more than effective element ceiling across explicit origins/dependencies in otherwise typed descriptors.
- **Expected Result:** Reject before authority/read/decoder access.
- **Expected Diagnostics:** RUN-018.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T169 — Exact source binding authority

- **Test ID:** RUN-01-T169
- **Scenario:** Exact source binding authority.
- **Objective:** Verify exact source binding authority against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Return a decision for an equal-looking different RuntimeArtifactLoadBinding object.
- **Expected Result:** Original invocation identity is mandatory; no receipt substitution.
- **Expected Diagnostics:** RUN-003.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T170 — Authority target mismatch

- **Test ID:** RUN-01-T170
- **Scenario:** Authority target mismatch.
- **Objective:** Verify authority target mismatch against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Return decision with same manifest token/keys but other runtime target.
- **Expected Result:** FAILED before reading.
- **Expected Diagnostics:** RUN-003.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T171 — Authority non-secret references

- **Test ID:** RUN-01-T171
- **Scenario:** Authority non-secret references.
- **Objective:** Verify authority non-secret references against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Try empty, path-like, control-containing or over-160-character authority references.
- **Expected Result:** Decision construction rejects; no secret/absolute path exposed.
- **Expected Diagnostics:** ValueError.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T172 — Explicit full subset rejected

- **Test ID:** RUN-01-T172
- **Scenario:** Explicit full subset rejected.
- **Objective:** Verify explicit full subset rejected against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Choose EXPLICIT_ARTIFACT_SET containing every manifest member.
- **Expected Result:** Runtime v0 still requires ALL mode; no implicit package completeness claim.
- **Expected Diagnostics:** RUN-019.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T173 — Reader invalid root result

- **Test ID:** RUN-01-T173
- **Scenario:** Reader invalid root result.
- **Objective:** Verify reader invalid root result against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Inject trusted reader accidentally returning dict/None instead of ArtifactReadResult.
- **Expected Result:** Structured read contract failure; no decoder runs.
- **Expected Diagnostics:** RUN-006.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T174 — Reader different request association

- **Test ID:** RUN-01-T174
- **Scenario:** Reader different request association.
- **Objective:** Verify reader different request association against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Reader returns successful plan associated with another equal request.
- **Expected Result:** Reject because exact authorized read invocation is required.
- **Expected Diagnostics:** RUN-006.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T175 — Reader increased ceilings

- **Test ID:** RUN-01-T175
- **Scenario:** Reader increased ceilings.
- **Objective:** Verify reader increased ceilings against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Return a forged reader plan with limits exceeding the requested runtime policy.
- **Expected Result:** Reject before decoding.
- **Expected Diagnostics:** RUN-018.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T176 — Reader altered source membership

- **Test ID:** RUN-01-T176
- **Scenario:** Reader altered source membership.
- **Objective:** Verify reader altered source membership against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Return read evidence for a substituted receipt descriptor/location or incomplete set.
- **Expected Result:** Existing result invariants or source bridge reject.
- **Expected Diagnostics:** Existing CMP rejection or RUN-005/006.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T177 — Reader size-only outcome

- **Test ID:** RUN-01-T177
- **Scenario:** Reader size-only outcome.
- **Objective:** Verify reader size-only outcome against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Return an invalid purported runtime reader success without original verified SHA-256.
- **Expected Result:** No successful runtime read projection; mandatory digest evidence persists.
- **Expected Diagnostics:** RUN-007/CMP-075 or RUN-006 policy rejection.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T178 — Unexpected programming fault

- **Test ID:** RUN-01-T178
- **Scenario:** Unexpected programming fault.
- **Objective:** Verify unexpected programming fault against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Inject an approved implementation with an unexpected programming exception, separate from documented expected load/decode errors.
- **Expected Result:** Fault propagates; not silently converted into unsupported-capability success/failure.
- **Expected Diagnostics:** Original programming exception; no loaded set.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T179 — Decoder invalid result root

- **Test ID:** RUN-01-T179
- **Scenario:** Decoder invalid result root.
- **Objective:** Verify decoder invalid result root against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Return None/dict/wrong result class from the approved decoder.
- **Expected Result:** FAILED without partial set.
- **Expected Diagnostics:** RUN-012.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T180 — Decoder conflicting diagnostic target

- **Test ID:** RUN-01-T180
- **Scenario:** Decoder conflicting diagnostic target.
- **Objective:** Verify decoder conflicting diagnostic target against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Return typed diagnostic for another artifact, manifest, scope, origin or runtime target.
- **Expected Result:** Reject conflicting association rather than falsely enriching it.
- **Expected Diagnostics:** RUN-012.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T181 — Decoder missing diagnostic association

- **Test ID:** RUN-01-T181
- **Scenario:** Decoder missing diagnostic association.
- **Objective:** Verify decoder missing diagnostic association against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Return a typed expected decode failure with absent optional target association.
- **Expected Result:** Enrich actual manifest/key/kind/context/target/origins while retaining stage/code/severity/order.
- **Expected Diagnostics:** Original structured decoder diagnostic.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T182 — Decoded origin type rejection

- **Test ID:** RUN-01-T182
- **Scenario:** Decoded origin type rejection.
- **Objective:** Verify decoded origin type rejection against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Return plain text origins or SemanticElementId without exact versions in an otherwise approved graph.
- **Expected Result:** Reject malformed origin contract.
- **Expected Diagnostics:** RUN-020.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T183 — Bytes omitted from output repr

- **Test ID:** RUN-01-T183
- **Scenario:** Bytes omitted from output repr.
- **Objective:** Verify bytes omitted from output repr against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Inspect verified input and successful loaded/result repr and public outputs.
- **Expected Result:** Original read buffers are not automatically retained by loaded_set; repr hides content/representations. Explicit approved binary fields remain internal; no default bytes, absolute roots or credentials disclosure.
- **Expected Diagnostics:** No disclosure.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T184 — Inactive load result

- **Test ID:** RUN-01-T184
- **Scenario:** Inactive load result.
- **Objective:** Verify inactive load result against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** After future genuine successful load, inspect registry/action/event/workflow boundaries.
- **Expected Result:** No publication, activation, business record or execution effect.
- **Expected Diagnostics:** No activation/execution diagnostics or fabricated success evidence.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T185 — Cross-binding comparison unsupported

- **Test ID:** RUN-01-T185
- **Scenario:** Cross-binding comparison unsupported.
- **Objective:** Verify cross-binding comparison unsupported against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Compare successful outcomes tied to distinct source binding objects.
- **Expected Result:** Explicit unsupported comparison rather than equality from matching tokens/digests alone.
- **Expected Diagnostics:** ValueError.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T186 — Decoder implementation affects equivalence

- **Test ID:** RUN-01-T186
- **Scenario:** Decoder implementation affects equivalence.
- **Objective:** Verify decoder implementation affects equivalence against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Keep metadata/source facts equal but change decoder concrete class or immutable options.
- **Expected Result:** Results are not asserted equivalent.
- **Expected Diagnostics:** Comparison False.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T187 — Human messages excluded from equivalence

- **Test ID:** RUN-01-T187
- **Scenario:** Human messages excluded from equivalence.
- **Objective:** Verify human messages excluded from equivalence against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Vary only human diagnostic wording with identical code/severity/stage/target/causes.
- **Expected Result:** Supported diagnostic semantics compare equal; original messages still retained for reporting.
- **Expected Diagnostics:** No diagnostic.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

### RUN-01-T188 — No manual smoke verification

- **Test ID:** RUN-01-T188
- **Scenario:** No manual smoke verification.
- **Objective:** Verify no manual smoke verification against the actual RUN-01 production contract.
- **Component:** Runtime contracts/coordinator/catalog or compiler-to-runtime source/application bridge identified by this scenario.
- **Prerequisites:** Fixed revision, explicit future execution permission and actual approved prerequisites from P; use source-only review where the scenario concerns architecture/execution evidence.
- **Input / Setup:** Review work/CI execution evidence at RUN-01 revision.
- **Expected Result:** No load/read/decode/Mini Sales custom script, runtime CLI or deferred case was executed.
- **Expected Diagnostics:** DEFERRED / NOT VERIFIED; 0 deferred tests.
- **Boundary / Edge Cases:** Absent versus exact versus mismatched values; one/multiple members; first/later failure; equality and one-unit overflow of applicable trusted bounds.
- **Integration Dependencies:** Existing Kernel/compiled-contracts, actual CMP-07/08/09 associations, trusted injected source/authorizer/decoder and inactive immutable load result.
- **Acceptance Criteria:** Exact documented behavior, original associations and diagnostic order, no partial successful set or unauthorized side effect; retain real future evidence without marking an unexecuted case passed.
- **Execution Status:** NOT_RUN — DEFERRED

## Documentation summary

Total documented scenarios: **188**. New executable tests: **0**. Tests executed: **0**. Status: **DEFERRED / NOT VERIFIED**. All scenario execution statuses are **NOT_RUN — DEFERRED**. No next architectural task initiated.
