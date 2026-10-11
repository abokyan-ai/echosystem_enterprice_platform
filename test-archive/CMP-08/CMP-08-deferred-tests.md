# CMP-08 — Deferred Test Specification

Task: CMP-08 — Artifact Writer

Backend: Python / Django / Django REST Framework

Status: NOT_RUN — DEFERRED

New Tests Implemented: 0

Tests Executed: 0

Dependencies:
- SK-11 (general contract absent; existing CMP-02 narrow seam retained)
- MOD-04
- MOD-08
- CMP-01
- CMP-02
- CMP-06
- CMP-07

Documentation date: 2026-10-11. Testing status: **DEFERRED / NOT VERIFIED**.

This is the sole CMP-08 archive document, as required by section 37 of the latest task attachment. Its explicit prohibition of an additional README/spec document supersedes the generic earlier archive layout for this task. Existing archives/history are preserved.

Scope: pure immutable contracts, original-result/manifest byte-source preflight, deterministic flat layout, explicit root configuration, Linux local infrastructure, isolated staging, exact-byte/inode/inventory verification, exclusive complete-directory commit, synchronization policy, immutable receipt and CMP-02 diagnostics. No producer/encoder/publication/runtime/API additions.

Execution conditions: explicit later user permission; fixed source revision; genuine approved final artifact producer/byte fields and original successful evidence; controlled disposable Linux local filesystem with trusted ancestry, libc/kernel/filesystem renameat2 NOREPLACE; independent subprocess/fault fixtures supplied at future verification time. No executable tests, fixtures or test infrastructure are created now. Generic scenario descriptions are specifications, not runtime evidence.

Known limitations: no current final byte producer or encoder; empty capability catalogs fail closed. Strict flat lower ASCII filenames only, no atomic replacement, cloud or remote mounts. Application administrator must approve actual local filesystem semantics and root ancestry. Root and ancestors must be controlled (no group/world write, approved owners); root belongs to writer UID. Privileged/hostile same-UID actors are outside containment guarantees. Startup/staging-name crash debris and cleanup failures need explicit operator handling, no sweeper. fsync requests filesystem synchronization, not universal power-loss durability. Failure after rename may leave visible complete output but no success receipt. Current provenance is trusted in-process object binding, not anti-forgery/portable authentication. Full SK-11/TYPE-01/HTTP integration unavailable. The new tooling module may require historical module-count fixtures to be updated when testing is authorized; existing tests are untouched.

Each scenario below starts **NOT_RUN — DEFERRED**. No passed/failed behavior is asserted.

Total documented scenarios: **158**.

## CMP-08-T001 — Valid writer invocation

- **Scenario:** Writer Contracts: Valid writer invocation.
- **Objective:** Establish the declared valid writer invocation behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriter / immutable ArtifactWriteRequest.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Typed original result, successful CMP-07 assembly, actual content sources and approved logical destination.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Supported exact inputs are planned; wrong roots reject CMP-044/049, unsupported policy CMP-052 INCOMPLETE. Interface constructs without frameworks.
- **Expected Diagnostics:** Supported exact inputs are planned; wrong roots reject CMP-044/049, unsupported policy CMP-052 INCOMPLETE. Interface constructs without frameworks. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriter / immutable ArtifactWriteRequest; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T002 — Invalid request

- **Scenario:** Writer Contracts: Invalid request.
- **Objective:** Establish the declared invalid request behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriter / immutable ArtifactWriteRequest.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Typed original result, successful CMP-07 assembly, actual content sources and approved logical destination.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Supported exact inputs are planned; wrong roots reject CMP-044/049, unsupported policy CMP-052 INCOMPLETE. Interface constructs without frameworks.
- **Expected Diagnostics:** Supported exact inputs are planned; wrong roots reject CMP-044/049, unsupported policy CMP-052 INCOMPLETE. Interface constructs without frameworks. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriter / immutable ArtifactWriteRequest; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T003 — Missing destination

- **Scenario:** Writer Contracts: Missing destination.
- **Objective:** Establish the declared missing destination behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriter / immutable ArtifactWriteRequest.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Typed original result, successful CMP-07 assembly, actual content sources and approved logical destination.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Supported exact inputs are planned; wrong roots reject CMP-044/049, unsupported policy CMP-052 INCOMPLETE. Interface constructs without frameworks.
- **Expected Diagnostics:** Supported exact inputs are planned; wrong roots reject CMP-044/049, unsupported policy CMP-052 INCOMPLETE. Interface constructs without frameworks. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriter / immutable ArtifactWriteRequest; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T004 — Unsupported write policy

- **Scenario:** Writer Contracts: Unsupported write policy.
- **Objective:** Establish the declared unsupported write policy behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriter / immutable ArtifactWriteRequest.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Typed original result, successful CMP-07 assembly, actual content sources and approved logical destination.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Supported exact inputs are planned; wrong roots reject CMP-044/049, unsupported policy CMP-052 INCOMPLETE. Interface constructs without frameworks.
- **Expected Diagnostics:** Supported exact inputs are planned; wrong roots reject CMP-044/049, unsupported policy CMP-052 INCOMPLETE. Interface constructs without frameworks. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriter / immutable ArtifactWriteRequest; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T005 — Framework-independent interface

- **Scenario:** Writer Contracts: Framework-independent interface.
- **Objective:** Establish the declared framework-independent interface behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriter / immutable ArtifactWriteRequest.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Typed original result, successful CMP-07 assembly, actual content sources and approved logical destination.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Supported exact inputs are planned; wrong roots reject CMP-044/049, unsupported policy CMP-052 INCOMPLETE. Interface constructs without frameworks.
- **Expected Diagnostics:** Supported exact inputs are planned; wrong roots reject CMP-044/049, unsupported policy CMP-052 INCOMPLETE. Interface constructs without frameworks. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriter / immutable ArtifactWriteRequest; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T006 — SUCCEEDED compilation

- **Scenario:** Compilation Prerequisites: SUCCEEDED compilation.
- **Objective:** Establish the declared succeeded compilation behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWritePlanner compilation gate.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original BUILD_TARGET result, original VALID/READY evidence, canonical object, scope, compiler configuration and output_origin.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun.
- **Expected Diagnostics:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWritePlanner compilation gate; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T007 — FAILED compilation

- **Scenario:** Compilation Prerequisites: FAILED compilation.
- **Objective:** Establish the declared failed compilation behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWritePlanner compilation gate.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original BUILD_TARGET result, original VALID/READY evidence, canonical object, scope, compiler configuration and output_origin.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun.
- **Expected Diagnostics:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWritePlanner compilation gate; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T008 — INCOMPLETE compilation

- **Scenario:** Compilation Prerequisites: INCOMPLETE compilation.
- **Objective:** Establish the declared incomplete compilation behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWritePlanner compilation gate.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original BUILD_TARGET result, original VALID/READY evidence, canonical object, scope, compiler configuration and output_origin.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun.
- **Expected Diagnostics:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWritePlanner compilation gate; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T009 — Missing validation evidence

- **Scenario:** Compilation Prerequisites: Missing validation evidence.
- **Objective:** Establish the declared missing validation evidence behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWritePlanner compilation gate.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original BUILD_TARGET result, original VALID/READY evidence, canonical object, scope, compiler configuration and output_origin.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun.
- **Expected Diagnostics:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWritePlanner compilation gate; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T010 — Canonical snapshot mismatch

- **Scenario:** Compilation Prerequisites: Canonical snapshot mismatch.
- **Objective:** Establish the declared canonical snapshot mismatch behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWritePlanner compilation gate.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original BUILD_TARGET result, original VALID/READY evidence, canonical object, scope, compiler configuration and output_origin.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun.
- **Expected Diagnostics:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWritePlanner compilation gate; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T011 — Compilation target mismatch

- **Scenario:** Compilation Prerequisites: Compilation target mismatch.
- **Objective:** Establish the declared compilation target mismatch behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWritePlanner compilation gate.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original BUILD_TARGET result, original VALID/READY evidence, canonical object, scope, compiler configuration and output_origin.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun.
- **Expected Diagnostics:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWritePlanner compilation gate; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T012 — Valid CMP-07 manifest

- **Scenario:** Manifest Integrity: Valid CMP-07 manifest.
- **Objective:** Establish the declared valid cmp-07 manifest behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CMP-07 prerequisite / descriptor inventory.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original successful assembly and matching result; preserve full descriptor metadata and internal dependency membership.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Revalidate original binding and whole inventory. Non-success/missing/partial assembly or another invocation rejects CMP-046; preserve CMP-031..043/030 evidence. IR cannot substitute for final artifacts.
- **Expected Diagnostics:** Revalidate original binding and whole inventory. Non-success/missing/partial assembly or another invocation rejects CMP-046; preserve CMP-031..043/030 evidence. IR cannot substitute for final artifacts. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CMP-07 prerequisite / descriptor inventory; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T013 — Missing manifest

- **Scenario:** Manifest Integrity: Missing manifest.
- **Objective:** Establish the declared missing manifest behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CMP-07 prerequisite / descriptor inventory.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original successful assembly and matching result; preserve full descriptor metadata and internal dependency membership.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Revalidate original binding and whole inventory. Non-success/missing/partial assembly or another invocation rejects CMP-046; preserve CMP-031..043/030 evidence. IR cannot substitute for final artifacts.
- **Expected Diagnostics:** Revalidate original binding and whole inventory. Non-success/missing/partial assembly or another invocation rejects CMP-046; preserve CMP-031..043/030 evidence. IR cannot substitute for final artifacts. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CMP-07 prerequisite / descriptor inventory; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T014 — Manifest assembly not successful

- **Scenario:** Manifest Integrity: Manifest assembly not successful.
- **Objective:** Establish the declared manifest assembly not successful behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CMP-07 prerequisite / descriptor inventory.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original successful assembly and matching result; preserve full descriptor metadata and internal dependency membership.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Revalidate original binding and whole inventory. Non-success/missing/partial assembly or another invocation rejects CMP-046; preserve CMP-031..043/030 evidence. IR cannot substitute for final artifacts.
- **Expected Diagnostics:** Revalidate original binding and whole inventory. Non-success/missing/partial assembly or another invocation rejects CMP-046; preserve CMP-031..043/030 evidence. IR cannot substitute for final artifacts. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CMP-07 prerequisite / descriptor inventory; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T015 — Duplicate artifact descriptors

- **Scenario:** Manifest Integrity: Duplicate artifact descriptors.
- **Objective:** Establish the declared duplicate artifact descriptors behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CMP-07 prerequisite / descriptor inventory.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original successful assembly and matching result; preserve full descriptor metadata and internal dependency membership.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Revalidate original binding and whole inventory. Non-success/missing/partial assembly or another invocation rejects CMP-046; preserve CMP-031..043/030 evidence. IR cannot substitute for final artifacts.
- **Expected Diagnostics:** Revalidate original binding and whole inventory. Non-success/missing/partial assembly or another invocation rejects CMP-046; preserve CMP-031..043/030 evidence. IR cannot substitute for final artifacts. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CMP-07 prerequisite / descriptor inventory; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T016 — Incomplete artifact set

- **Scenario:** Manifest Integrity: Incomplete artifact set.
- **Objective:** Establish the declared incomplete artifact set behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CMP-07 prerequisite / descriptor inventory.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original successful assembly and matching result; preserve full descriptor metadata and internal dependency membership.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Revalidate original binding and whole inventory. Non-success/missing/partial assembly or another invocation rejects CMP-046; preserve CMP-031..043/030 evidence. IR cannot substitute for final artifacts.
- **Expected Diagnostics:** Revalidate original binding and whole inventory. Non-success/missing/partial assembly or another invocation rejects CMP-046; preserve CMP-031..043/030 evidence. IR cannot substitute for final artifacts. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CMP-07 prerequisite / descriptor inventory; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T017 — Invalid artifact kind

- **Scenario:** Manifest Integrity: Invalid artifact kind.
- **Objective:** Establish the declared invalid artifact kind behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CMP-07 prerequisite / descriptor inventory.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original successful assembly and matching result; preserve full descriptor metadata and internal dependency membership.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Revalidate original binding and whole inventory. Non-success/missing/partial assembly or another invocation rejects CMP-046; preserve CMP-031..043/030 evidence. IR cannot substitute for final artifacts.
- **Expected Diagnostics:** Revalidate original binding and whole inventory. Non-success/missing/partial assembly or another invocation rejects CMP-046; preserve CMP-031..043/030 evidence. IR cannot substitute for final artifacts. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CMP-07 prerequisite / descriptor inventory; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T018 — No IR-as-artifact substitution

- **Scenario:** Manifest Integrity: No IR-as-artifact substitution.
- **Objective:** Establish the declared no ir-as-artifact substitution behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CMP-07 prerequisite / descriptor inventory.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original successful assembly and matching result; preserve full descriptor metadata and internal dependency membership.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Revalidate original binding and whole inventory. Non-success/missing/partial assembly or another invocation rejects CMP-046; preserve CMP-031..043/030 evidence. IR cannot substitute for final artifacts.
- **Expected Diagnostics:** Revalidate original binding and whole inventory. Non-success/missing/partial assembly or another invocation rejects CMP-046; preserve CMP-031..043/030 evidence. IR cannot substitute for final artifacts. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CMP-07 prerequisite / descriptor inventory; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T019 — Complete descriptor-to-payload matching

- **Scenario:** Content Mapping: Complete descriptor-to-payload matching.
- **Objective:** Establish the declared complete descriptor-to-payload matching behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactContentSource / ArtifactByteContentSupport.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future genuinely approved frozen artifact class produced by an authorized final phase, CMP-07 exact kind approval and immutable bytes field; no current producer exists.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output.
- **Expected Diagnostics:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactContentSource / ArtifactByteContentSupport; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T020 — Missing payload

- **Scenario:** Content Mapping: Missing payload.
- **Objective:** Establish the declared missing payload behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactContentSource / ArtifactByteContentSupport.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future genuinely approved frozen artifact class produced by an authorized final phase, CMP-07 exact kind approval and immutable bytes field; no current producer exists.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output.
- **Expected Diagnostics:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactContentSource / ArtifactByteContentSupport; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T021 — Extra undeclared payload

- **Scenario:** Content Mapping: Extra undeclared payload.
- **Objective:** Establish the declared extra undeclared payload behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactContentSource / ArtifactByteContentSupport.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future genuinely approved frozen artifact class produced by an authorized final phase, CMP-07 exact kind approval and immutable bytes field; no current producer exists.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output.
- **Expected Diagnostics:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactContentSource / ArtifactByteContentSupport; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T022 — Duplicate artifact identity

- **Scenario:** Content Mapping: Duplicate artifact identity.
- **Objective:** Establish the declared duplicate artifact identity behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactContentSource / ArtifactByteContentSupport.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future genuinely approved frozen artifact class produced by an authorized final phase, CMP-07 exact kind approval and immutable bytes field; no current producer exists.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output.
- **Expected Diagnostics:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactContentSource / ArtifactByteContentSupport; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T023 — Artifact kind mismatch

- **Scenario:** Content Mapping: Artifact kind mismatch.
- **Objective:** Establish the declared artifact kind mismatch behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactContentSource / ArtifactByteContentSupport.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future genuinely approved frozen artifact class produced by an authorized final phase, CMP-07 exact kind approval and immutable bytes field; no current producer exists.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output.
- **Expected Diagnostics:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactContentSource / ArtifactByteContentSupport; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T024 — Unsupported content encoding

- **Scenario:** Content Mapping: Unsupported content encoding.
- **Objective:** Establish the declared unsupported content encoding behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactContentSource / ArtifactByteContentSupport.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future genuinely approved frozen artifact class produced by an authorized final phase, CMP-07 exact kind approval and immutable bytes field; no current producer exists.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output.
- **Expected Diagnostics:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactContentSource / ArtifactByteContentSupport; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T025 — No fabricated content

- **Scenario:** Content Mapping: No fabricated content.
- **Objective:** Establish the declared no fabricated content behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactContentSource / ArtifactByteContentSupport.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future genuinely approved frozen artifact class produced by an authorized final phase, CMP-07 exact kind approval and immutable bytes field; no current producer exists.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output.
- **Expected Diagnostics:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactContentSource / ArtifactByteContentSupport; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T026 — Valid relative location

- **Scenario:** Path Safety: Valid relative location.
- **Objective:** Establish the declared valid relative location behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactRelativeLocation / fd-based root traversal.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Explicit trusted Linux local root with controlled ancestors, no-follow directory/file handles, flat portable ASCII layout.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape.
- **Expected Diagnostics:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactRelativeLocation / fd-based root traversal; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T027 — Parent traversal

- **Scenario:** Path Safety: Parent traversal.
- **Objective:** Establish the declared parent traversal behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactRelativeLocation / fd-based root traversal.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Explicit trusted Linux local root with controlled ancestors, no-follow directory/file handles, flat portable ASCII layout.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape.
- **Expected Diagnostics:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactRelativeLocation / fd-based root traversal; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T028 — Absolute path

- **Scenario:** Path Safety: Absolute path.
- **Objective:** Establish the declared absolute path behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactRelativeLocation / fd-based root traversal.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Explicit trusted Linux local root with controlled ancestors, no-follow directory/file handles, flat portable ASCII layout.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape.
- **Expected Diagnostics:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactRelativeLocation / fd-based root traversal; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T029 — NUL byte

- **Scenario:** Path Safety: NUL byte.
- **Objective:** Establish the declared nul byte behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactRelativeLocation / fd-based root traversal.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Explicit trusted Linux local root with controlled ancestors, no-follow directory/file handles, flat portable ASCII layout.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape.
- **Expected Diagnostics:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactRelativeLocation / fd-based root traversal; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T030 — Empty component

- **Scenario:** Path Safety: Empty component.
- **Objective:** Establish the declared empty component behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactRelativeLocation / fd-based root traversal.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Explicit trusted Linux local root with controlled ancestors, no-follow directory/file handles, flat portable ASCII layout.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape.
- **Expected Diagnostics:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactRelativeLocation / fd-based root traversal; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T031 — Symlink escape

- **Scenario:** Path Safety: Symlink escape.
- **Objective:** Establish the declared symlink escape behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactRelativeLocation / fd-based root traversal.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Explicit trusted Linux local root with controlled ancestors, no-follow directory/file handles, flat portable ASCII layout.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape.
- **Expected Diagnostics:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactRelativeLocation / fd-based root traversal; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T032 — Unsafe normalized path

- **Scenario:** Path Safety: Unsafe normalized path.
- **Objective:** Establish the declared unsafe normalized path behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactRelativeLocation / fd-based root traversal.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Explicit trusted Linux local root with controlled ancestors, no-follow directory/file handles, flat portable ASCII layout.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape.
- **Expected Diagnostics:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactRelativeLocation / fd-based root traversal; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T033 — Cross-platform path ambiguity

- **Scenario:** Path Safety: Cross-platform path ambiguity.
- **Objective:** Establish the declared cross-platform path ambiguity behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactRelativeLocation / fd-based root traversal.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Explicit trusted Linux local root with controlled ancestors, no-follow directory/file handles, flat portable ASCII layout.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape.
- **Expected Diagnostics:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactRelativeLocation / fd-based root traversal; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T034 — Destination containment

- **Scenario:** Path Safety: Destination containment.
- **Objective:** Establish the declared destination containment behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactRelativeLocation / fd-based root traversal.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Explicit trusted Linux local root with controlled ancestors, no-follow directory/file handles, flat portable ASCII layout.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape.
- **Expected Diagnostics:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactRelativeLocation / fd-based root traversal; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T035 — Stable artifact order

- **Scenario:** Deterministic Planning: Stable artifact order.
- **Objective:** Establish the declared stable artifact order behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactOutputLayout / ArtifactWritePlan.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Identical manifest bytes and approved kind layout, arbitrary source input order, explicit complete mapping when supplied.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Plan orders existing artifact keys, retains bytes/source identity and stable relative locations. Duplicates/missing/wrong-kind layout reject CMP-051, plan mismatch CMP-046. Default kind__key.bin is deterministic; no suffix/time/PID/random final names.
- **Expected Diagnostics:** Plan orders existing artifact keys, retains bytes/source identity and stable relative locations. Duplicates/missing/wrong-kind layout reject CMP-051, plan mismatch CMP-046. Default kind__key.bin is deterministic; no suffix/time/PID/random final names. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactOutputLayout / ArtifactWritePlan; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T036 — Stable relative paths

- **Scenario:** Deterministic Planning: Stable relative paths.
- **Objective:** Establish the declared stable relative paths behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactOutputLayout / ArtifactWritePlan.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Identical manifest bytes and approved kind layout, arbitrary source input order, explicit complete mapping when supplied.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Plan orders existing artifact keys, retains bytes/source identity and stable relative locations. Duplicates/missing/wrong-kind layout reject CMP-051, plan mismatch CMP-046. Default kind__key.bin is deterministic; no suffix/time/PID/random final names.
- **Expected Diagnostics:** Plan orders existing artifact keys, retains bytes/source identity and stable relative locations. Duplicates/missing/wrong-kind layout reject CMP-051, plan mismatch CMP-046. Default kind__key.bin is deterministic; no suffix/time/PID/random final names. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactOutputLayout / ArtifactWritePlan; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T037 — Duplicate normalized location

- **Scenario:** Deterministic Planning: Duplicate normalized location.
- **Objective:** Establish the declared duplicate normalized location behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactOutputLayout / ArtifactWritePlan.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Identical manifest bytes and approved kind layout, arbitrary source input order, explicit complete mapping when supplied.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Plan orders existing artifact keys, retains bytes/source identity and stable relative locations. Duplicates/missing/wrong-kind layout reject CMP-051, plan mismatch CMP-046. Default kind__key.bin is deterministic; no suffix/time/PID/random final names.
- **Expected Diagnostics:** Plan orders existing artifact keys, retains bytes/source identity and stable relative locations. Duplicates/missing/wrong-kind layout reject CMP-051, plan mismatch CMP-046. Default kind__key.bin is deterministic; no suffix/time/PID/random final names. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactOutputLayout / ArtifactWritePlan; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T038 — No timestamp-derived output path

- **Scenario:** Deterministic Planning: No timestamp-derived output path.
- **Objective:** Establish the declared no timestamp-derived output path behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactOutputLayout / ArtifactWritePlan.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Identical manifest bytes and approved kind layout, arbitrary source input order, explicit complete mapping when supplied.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Plan orders existing artifact keys, retains bytes/source identity and stable relative locations. Duplicates/missing/wrong-kind layout reject CMP-051, plan mismatch CMP-046. Default kind__key.bin is deterministic; no suffix/time/PID/random final names.
- **Expected Diagnostics:** Plan orders existing artifact keys, retains bytes/source identity and stable relative locations. Duplicates/missing/wrong-kind layout reject CMP-051, plan mismatch CMP-046. Default kind__key.bin is deterministic; no suffix/time/PID/random final names. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactOutputLayout / ArtifactWritePlan; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T039 — No random committed filename

- **Scenario:** Deterministic Planning: No random committed filename.
- **Objective:** Establish the declared no random committed filename behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactOutputLayout / ArtifactWritePlan.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Identical manifest bytes and approved kind layout, arbitrary source input order, explicit complete mapping when supplied.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Plan orders existing artifact keys, retains bytes/source identity and stable relative locations. Duplicates/missing/wrong-kind layout reject CMP-051, plan mismatch CMP-046. Default kind__key.bin is deterministic; no suffix/time/PID/random final names.
- **Expected Diagnostics:** Plan orders existing artifact keys, retains bytes/source identity and stable relative locations. Duplicates/missing/wrong-kind layout reject CMP-051, plan mismatch CMP-046. Default kind__key.bin is deterministic; no suffix/time/PID/random final names. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactOutputLayout / ArtifactWritePlan; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T040 — Deterministic immutable plan

- **Scenario:** Deterministic Planning: Deterministic immutable plan.
- **Objective:** Establish the declared deterministic immutable plan behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactOutputLayout / ArtifactWritePlan.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Identical manifest bytes and approved kind layout, arbitrary source input order, explicit complete mapping when supplied.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Plan orders existing artifact keys, retains bytes/source identity and stable relative locations. Duplicates/missing/wrong-kind layout reject CMP-051, plan mismatch CMP-046. Default kind__key.bin is deterministic; no suffix/time/PID/random final names.
- **Expected Diagnostics:** Plan orders existing artifact keys, retains bytes/source identity and stable relative locations. Duplicates/missing/wrong-kind layout reject CMP-051, plan mismatch CMP-046. Default kind__key.bin is deterministic; no suffix/time/PID/random final names. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactOutputLayout / ArtifactWritePlan; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T041 — FAIL_IF_EXISTS

- **Scenario:** Write Policy: FAIL_IF_EXISTS.
- **Objective:** Establish the declared fail_if_exists behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWritePolicy / exclusive destination.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; FAIL_IF_EXISTS; existing directories, empty directories, regular files and symlinks at final name.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Existing or racing destination rejects CMP-053 FAILED without overwrite. Repeated equal/different requests are conflicts, not successful replays. Replacement unsupported CMP-052 INCOMPLETE; no removal or merge.
- **Expected Diagnostics:** Existing or racing destination rejects CMP-053 FAILED without overwrite. Repeated equal/different requests are conflicts, not successful replays. Replacement unsupported CMP-052 INCOMPLETE; no removal or merge. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWritePolicy / exclusive destination; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T042 — Existing destination

- **Scenario:** Write Policy: Existing destination.
- **Objective:** Establish the declared existing destination behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWritePolicy / exclusive destination.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; FAIL_IF_EXISTS; existing directories, empty directories, regular files and symlinks at final name.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Existing or racing destination rejects CMP-053 FAILED without overwrite. Repeated equal/different requests are conflicts, not successful replays. Replacement unsupported CMP-052 INCOMPLETE; no removal or merge.
- **Expected Diagnostics:** Existing or racing destination rejects CMP-053 FAILED without overwrite. Repeated equal/different requests are conflicts, not successful replays. Replacement unsupported CMP-052 INCOMPLETE; no removal or merge. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWritePolicy / exclusive destination; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T043 — Repeated identical request

- **Scenario:** Write Policy: Repeated identical request.
- **Objective:** Establish the declared repeated identical request behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWritePolicy / exclusive destination.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; FAIL_IF_EXISTS; existing directories, empty directories, regular files and symlinks at final name.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Existing or racing destination rejects CMP-053 FAILED without overwrite. Repeated equal/different requests are conflicts, not successful replays. Replacement unsupported CMP-052 INCOMPLETE; no removal or merge.
- **Expected Diagnostics:** Existing or racing destination rejects CMP-053 FAILED without overwrite. Repeated equal/different requests are conflicts, not successful replays. Replacement unsupported CMP-052 INCOMPLETE; no removal or merge. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWritePolicy / exclusive destination; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T044 — Repeated different request

- **Scenario:** Write Policy: Repeated different request.
- **Objective:** Establish the declared repeated different request behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWritePolicy / exclusive destination.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; FAIL_IF_EXISTS; existing directories, empty directories, regular files and symlinks at final name.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Existing or racing destination rejects CMP-053 FAILED without overwrite. Repeated equal/different requests are conflicts, not successful replays. Replacement unsupported CMP-052 INCOMPLETE; no removal or merge.
- **Expected Diagnostics:** Existing or racing destination rejects CMP-053 FAILED without overwrite. Repeated equal/different requests are conflicts, not successful replays. Replacement unsupported CMP-052 INCOMPLETE; no removal or merge. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWritePolicy / exclusive destination; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T045 — Unsupported replacement

- **Scenario:** Write Policy: Unsupported replacement.
- **Objective:** Establish the declared unsupported replacement behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWritePolicy / exclusive destination.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; FAIL_IF_EXISTS; existing directories, empty directories, regular files and symlinks at final name.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Existing or racing destination rejects CMP-053 FAILED without overwrite. Repeated equal/different requests are conflicts, not successful replays. Replacement unsupported CMP-052 INCOMPLETE; no removal or merge.
- **Expected Diagnostics:** Existing or racing destination rejects CMP-053 FAILED without overwrite. Repeated equal/different requests are conflicts, not successful replays. Replacement unsupported CMP-052 INCOMPLETE; no removal or merge. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWritePolicy / exclusive destination; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T046 — No silent overwrite

- **Scenario:** Write Policy: No silent overwrite.
- **Objective:** Establish the declared no silent overwrite behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWritePolicy / exclusive destination.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; FAIL_IF_EXISTS; existing directories, empty directories, regular files and symlinks at final name.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Existing or racing destination rejects CMP-053 FAILED without overwrite. Repeated equal/different requests are conflicts, not successful replays. Replacement unsupported CMP-052 INCOMPLETE; no removal or merge.
- **Expected Diagnostics:** Existing or racing destination rejects CMP-053 FAILED without overwrite. Repeated equal/different requests are conflicts, not successful replays. Replacement unsupported CMP-052 INCOMPLETE; no removal or merge. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWritePolicy / exclusive destination; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T047 — Successful private staging

- **Scenario:** Staging: Successful private staging.
- **Objective:** Establish the declared successful private staging behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** LocalFilesystemArtifactWriter private staging.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future controlled filesystem fixtures, root fd, exclusively allocated random writer-owned staging and tracked exclusive file inodes.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** 0700 staging under root on same filesystem; exclusive 0600 files. CMP-054 for staging failure. Any earlier/later error prevents commit; cleanup only owned identities and preserves primary evidence. Random staging never appears in receipt.
- **Expected Diagnostics:** 0700 staging under root on same filesystem; exclusive 0600 files. CMP-054 for staging failure. Any earlier/later error prevents commit; cleanup only owned identities and preserves primary evidence. Random staging never appears in receipt. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** LocalFilesystemArtifactWriter private staging; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T048 — Same-filesystem staging

- **Scenario:** Staging: Same-filesystem staging.
- **Objective:** Establish the declared same-filesystem staging behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** LocalFilesystemArtifactWriter private staging.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future controlled filesystem fixtures, root fd, exclusively allocated random writer-owned staging and tracked exclusive file inodes.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** 0700 staging under root on same filesystem; exclusive 0600 files. CMP-054 for staging failure. Any earlier/later error prevents commit; cleanup only owned identities and preserves primary evidence. Random staging never appears in receipt.
- **Expected Diagnostics:** 0700 staging under root on same filesystem; exclusive 0600 files. CMP-054 for staging failure. Any earlier/later error prevents commit; cleanup only owned identities and preserves primary evidence. Random staging never appears in receipt. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** LocalFilesystemArtifactWriter private staging; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T049 — Partial staging failure

- **Scenario:** Staging: Partial staging failure.
- **Objective:** Establish the declared partial staging failure behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** LocalFilesystemArtifactWriter private staging.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future controlled filesystem fixtures, root fd, exclusively allocated random writer-owned staging and tracked exclusive file inodes.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** 0700 staging under root on same filesystem; exclusive 0600 files. CMP-054 for staging failure. Any earlier/later error prevents commit; cleanup only owned identities and preserves primary evidence. Random staging never appears in receipt.
- **Expected Diagnostics:** 0700 staging under root on same filesystem; exclusive 0600 files. CMP-054 for staging failure. Any earlier/later error prevents commit; cleanup only owned identities and preserves primary evidence. Random staging never appears in receipt. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** LocalFilesystemArtifactWriter private staging; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T050 — Cleanup of owned staging

- **Scenario:** Staging: Cleanup of owned staging.
- **Objective:** Establish the declared cleanup of owned staging behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** LocalFilesystemArtifactWriter private staging.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future controlled filesystem fixtures, root fd, exclusively allocated random writer-owned staging and tracked exclusive file inodes.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** 0700 staging under root on same filesystem; exclusive 0600 files. CMP-054 for staging failure. Any earlier/later error prevents commit; cleanup only owned identities and preserves primary evidence. Random staging never appears in receipt.
- **Expected Diagnostics:** 0700 staging under root on same filesystem; exclusive 0600 files. CMP-054 for staging failure. Any earlier/later error prevents commit; cleanup only owned identities and preserves primary evidence. Random staging never appears in receipt. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** LocalFilesystemArtifactWriter private staging; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T051 — No staging exposure as final destination

- **Scenario:** Staging: No staging exposure as final destination.
- **Objective:** Establish the declared no staging exposure as final destination behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** LocalFilesystemArtifactWriter private staging.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future controlled filesystem fixtures, root fd, exclusively allocated random writer-owned staging and tracked exclusive file inodes.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** 0700 staging under root on same filesystem; exclusive 0600 files. CMP-054 for staging failure. Any earlier/later error prevents commit; cleanup only owned identities and preserves primary evidence. Random staging never appears in receipt.
- **Expected Diagnostics:** 0700 staging under root on same filesystem; exclusive 0600 files. CMP-054 for staging failure. Any earlier/later error prevents commit; cleanup only owned identities and preserves primary evidence. Random staging never appears in receipt. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** LocalFilesystemArtifactWriter private staging; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T052 — Complete successful commit

- **Scenario:** Atomic Commit: Complete successful commit.
- **Objective:** Establish the declared complete successful commit behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Linux renameat2 RENAME_NOREPLACE commit.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual Linux/libc/kernel/filesystem support; all planned bytes verified in one staged directory.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback.
- **Expected Diagnostics:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Linux renameat2 RENAME_NOREPLACE commit; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T053 — Commit conflict

- **Scenario:** Atomic Commit: Commit conflict.
- **Objective:** Establish the declared commit conflict behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Linux renameat2 RENAME_NOREPLACE commit.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual Linux/libc/kernel/filesystem support; all planned bytes verified in one staged directory.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback.
- **Expected Diagnostics:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Linux renameat2 RENAME_NOREPLACE commit; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T054 — Atomic rename behavior

- **Scenario:** Atomic Commit: Atomic rename behavior.
- **Objective:** Establish the declared atomic rename behavior behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Linux renameat2 RENAME_NOREPLACE commit.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual Linux/libc/kernel/filesystem support; all planned bytes verified in one staged directory.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback.
- **Expected Diagnostics:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Linux renameat2 RENAME_NOREPLACE commit; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T055 — Unsupported atomicity

- **Scenario:** Atomic Commit: Unsupported atomicity.
- **Objective:** Establish the declared unsupported atomicity behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Linux renameat2 RENAME_NOREPLACE commit.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual Linux/libc/kernel/filesystem support; all planned bytes verified in one staged directory.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback.
- **Expected Diagnostics:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Linux renameat2 RENAME_NOREPLACE commit; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T056 — Previous output preservation

- **Scenario:** Atomic Commit: Previous output preservation.
- **Objective:** Establish the declared previous output preservation behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Linux renameat2 RENAME_NOREPLACE commit.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual Linux/libc/kernel/filesystem support; all planned bytes verified in one staged directory.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback.
- **Expected Diagnostics:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Linux renameat2 RENAME_NOREPLACE commit; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T057 — No partial committed artifact set

- **Scenario:** Atomic Commit: No partial committed artifact set.
- **Objective:** Establish the declared no partial committed artifact set behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Linux renameat2 RENAME_NOREPLACE commit.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual Linux/libc/kernel/filesystem support; all planned bytes verified in one staged directory.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback.
- **Expected Diagnostics:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Linux renameat2 RENAME_NOREPLACE commit; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T058 — Same destination concurrent writes

- **Scenario:** Concurrent Writers: Same destination concurrent writes.
- **Objective:** Establish the declared same destination concurrent writes behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Cross-process exclusive commit.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Independent writer processes and separate private staging, same approved root/output token; no in-process lock relied upon.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** At most one succeeds; loser CMP-053 with no receipt and only its own staging removed. Winner unchanged. Independent destinations may succeed. No LWW/distributed lock/global mutable collector.
- **Expected Diagnostics:** At most one succeeds; loser CMP-053 with no receipt and only its own staging removed. Winner unchanged. Independent destinations may succeed. No LWW/distributed lock/global mutable collector. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Cross-process exclusive commit; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T059 — Cross-process conflict

- **Scenario:** Concurrent Writers: Cross-process conflict.
- **Objective:** Establish the declared cross-process conflict behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Cross-process exclusive commit.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Independent writer processes and separate private staging, same approved root/output token; no in-process lock relied upon.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** At most one succeeds; loser CMP-053 with no receipt and only its own staging removed. Winner unchanged. Independent destinations may succeed. No LWW/distributed lock/global mutable collector.
- **Expected Diagnostics:** At most one succeeds; loser CMP-053 with no receipt and only its own staging removed. Winner unchanged. Independent destinations may succeed. No LWW/distributed lock/global mutable collector. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Cross-process exclusive commit; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T060 — Exclusive commit

- **Scenario:** Concurrent Writers: Exclusive commit.
- **Objective:** Establish the declared exclusive commit behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Cross-process exclusive commit.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Independent writer processes and separate private staging, same approved root/output token; no in-process lock relied upon.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** At most one succeeds; loser CMP-053 with no receipt and only its own staging removed. Winner unchanged. Independent destinations may succeed. No LWW/distributed lock/global mutable collector.
- **Expected Diagnostics:** At most one succeeds; loser CMP-053 with no receipt and only its own staging removed. Winner unchanged. Independent destinations may succeed. No LWW/distributed lock/global mutable collector. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Cross-process exclusive commit; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T061 — No last-write-wins

- **Scenario:** Concurrent Writers: No last-write-wins.
- **Objective:** Establish the declared no last-write-wins behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Cross-process exclusive commit.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Independent writer processes and separate private staging, same approved root/output token; no in-process lock relied upon.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** At most one succeeds; loser CMP-053 with no receipt and only its own staging removed. Winner unchanged. Independent destinations may succeed. No LWW/distributed lock/global mutable collector.
- **Expected Diagnostics:** At most one succeeds; loser CMP-053 with no receipt and only its own staging removed. Winner unchanged. Independent destinations may succeed. No LWW/distributed lock/global mutable collector. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Cross-process exclusive commit; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T062 — No shared mutable staging collector

- **Scenario:** Concurrent Writers: No shared mutable staging collector.
- **Objective:** Establish the declared no shared mutable staging collector behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Cross-process exclusive commit.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Independent writer processes and separate private staging, same approved root/output token; no in-process lock relied upon.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** At most one succeeds; loser CMP-053 with no receipt and only its own staging removed. Winner unchanged. Independent destinations may succeed. No LWW/distributed lock/global mutable collector.
- **Expected Diagnostics:** At most one succeeds; loser CMP-053 with no receipt and only its own staging removed. Winner unchanged. Independent destinations may succeed. No LWW/distributed lock/global mutable collector. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Cross-process exclusive commit; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T063 — Exact byte preservation

- **Scenario:** Integrity: Exact byte preservation.
- **Objective:** Establish the declared exact byte preservation behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Staged exact byte / length / optional digest verification.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original immutable bytes, bounded chunk writes/reads, owned normal file with same inode/nlink=1 and optional producer-declared SHA-256.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature.
- **Expected Diagnostics:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Staged exact byte / length / optional digest verification; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T064 — Expected byte length

- **Scenario:** Integrity: Expected byte length.
- **Objective:** Establish the declared expected byte length behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Staged exact byte / length / optional digest verification.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original immutable bytes, bounded chunk writes/reads, owned normal file with same inode/nlink=1 and optional producer-declared SHA-256.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature.
- **Expected Diagnostics:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Staged exact byte / length / optional digest verification; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T065 — Incomplete write

- **Scenario:** Integrity: Incomplete write.
- **Objective:** Establish the declared incomplete write behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Staged exact byte / length / optional digest verification.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original immutable bytes, bounded chunk writes/reads, owned normal file with same inode/nlink=1 and optional producer-declared SHA-256.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature.
- **Expected Diagnostics:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Staged exact byte / length / optional digest verification; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T066 — Staged artifact missing

- **Scenario:** Integrity: Staged artifact missing.
- **Objective:** Establish the declared staged artifact missing behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Staged exact byte / length / optional digest verification.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original immutable bytes, bounded chunk writes/reads, owned normal file with same inode/nlink=1 and optional producer-declared SHA-256.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature.
- **Expected Diagnostics:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Staged exact byte / length / optional digest verification; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T067 — Existing declared digest verification

- **Scenario:** Integrity: Existing declared digest verification.
- **Objective:** Establish the declared existing declared digest verification behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Staged exact byte / length / optional digest verification.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original immutable bytes, bounded chunk writes/reads, owned normal file with same inode/nlink=1 and optional producer-declared SHA-256.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature.
- **Expected Diagnostics:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Staged exact byte / length / optional digest verification; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T068 — Digest mismatch

- **Scenario:** Integrity: Digest mismatch.
- **Objective:** Establish the declared digest mismatch behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Staged exact byte / length / optional digest verification.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original immutable bytes, bounded chunk writes/reads, owned normal file with same inode/nlink=1 and optional producer-declared SHA-256.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature.
- **Expected Diagnostics:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Staged exact byte / length / optional digest verification; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T069 — No fabricated digest

- **Scenario:** Integrity: No fabricated digest.
- **Objective:** Establish the declared no fabricated digest behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Staged exact byte / length / optional digest verification.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original immutable bytes, bounded chunk writes/reads, owned normal file with same inode/nlink=1 and optional producer-declared SHA-256.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature.
- **Expected Diagnostics:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Staged exact byte / length / optional digest verification; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T070 — Visible commit

- **Scenario:** Durability: Visible commit.
- **Objective:** Establish the declared visible commit behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactDurabilityPolicy / fsync boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; VISIBLE_COMMIT or SYNCHRONIZED_COMMIT on supported local filesystem; controlled synchronization fault fixtures.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee.
- **Expected Diagnostics:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactDurabilityPolicy / fsync boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T071 — Crash durability when supported

- **Scenario:** Durability: Crash durability when supported.
- **Objective:** Establish the declared crash durability when supported behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactDurabilityPolicy / fsync boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; VISIBLE_COMMIT or SYNCHRONIZED_COMMIT on supported local filesystem; controlled synchronization fault fixtures.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee.
- **Expected Diagnostics:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactDurabilityPolicy / fsync boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T072 — File synchronization

- **Scenario:** Durability: File synchronization.
- **Objective:** Establish the declared file synchronization behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactDurabilityPolicy / fsync boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; VISIBLE_COMMIT or SYNCHRONIZED_COMMIT on supported local filesystem; controlled synchronization fault fixtures.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee.
- **Expected Diagnostics:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactDurabilityPolicy / fsync boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T073 — Directory synchronization

- **Scenario:** Durability: Directory synchronization.
- **Objective:** Establish the declared directory synchronization behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactDurabilityPolicy / fsync boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; VISIBLE_COMMIT or SYNCHRONIZED_COMMIT on supported local filesystem; controlled synchronization fault fixtures.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee.
- **Expected Diagnostics:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactDurabilityPolicy / fsync boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T074 — Unsupported durability policy

- **Scenario:** Durability: Unsupported durability policy.
- **Objective:** Establish the declared unsupported durability policy behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactDurabilityPolicy / fsync boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; VISIBLE_COMMIT or SYNCHRONIZED_COMMIT on supported local filesystem; controlled synchronization fault fixtures.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee.
- **Expected Diagnostics:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactDurabilityPolicy / fsync boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T075 — No unsupported replication claim

- **Scenario:** Durability: No unsupported replication claim.
- **Objective:** Establish the declared no unsupported replication claim behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactDurabilityPolicy / fsync boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; VISIBLE_COMMIT or SYNCHRONIZED_COMMIT on supported local filesystem; controlled synchronization fault fixtures.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee.
- **Expected Diagnostics:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactDurabilityPolicy / fsync boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T076 — Preflight failure

- **Scenario:** Failure Handling: Preflight failure.
- **Objective:** Establish the declared preflight failure behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Failure containment / cleanup / result.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Controlled fault at each named mandatory stage; preserve old destination, owned inode map and primary diagnostic.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output.
- **Expected Diagnostics:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Failure containment / cleanup / result; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T077 — First artifact write failure

- **Scenario:** Failure Handling: First artifact write failure.
- **Objective:** Establish the declared first artifact write failure behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Failure containment / cleanup / result.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Controlled fault at each named mandatory stage; preserve old destination, owned inode map and primary diagnostic.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output.
- **Expected Diagnostics:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Failure containment / cleanup / result; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T078 — Later artifact write failure

- **Scenario:** Failure Handling: Later artifact write failure.
- **Objective:** Establish the declared later artifact write failure behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Failure containment / cleanup / result.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Controlled fault at each named mandatory stage; preserve old destination, owned inode map and primary diagnostic.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output.
- **Expected Diagnostics:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Failure containment / cleanup / result; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T079 — Verification failure

- **Scenario:** Failure Handling: Verification failure.
- **Objective:** Establish the declared verification failure behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Failure containment / cleanup / result.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Controlled fault at each named mandatory stage; preserve old destination, owned inode map and primary diagnostic.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output.
- **Expected Diagnostics:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Failure containment / cleanup / result; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T080 — Commit failure

- **Scenario:** Failure Handling: Commit failure.
- **Objective:** Establish the declared commit failure behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Failure containment / cleanup / result.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Controlled fault at each named mandatory stage; preserve old destination, owned inode map and primary diagnostic.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output.
- **Expected Diagnostics:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Failure containment / cleanup / result; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T081 — Cleanup failure

- **Scenario:** Failure Handling: Cleanup failure.
- **Objective:** Establish the declared cleanup failure behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Failure containment / cleanup / result.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Controlled fault at each named mandatory stage; preserve old destination, owned inode map and primary diagnostic.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output.
- **Expected Diagnostics:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Failure containment / cleanup / result; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T082 — Previous committed output preserved

- **Scenario:** Failure Handling: Previous committed output preserved.
- **Objective:** Establish the declared previous committed output preserved behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Failure containment / cleanup / result.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Controlled fault at each named mandatory stage; preserve old destination, owned inode map and primary diagnostic.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output.
- **Expected Diagnostics:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Failure containment / cleanup / result; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T083 — No false successful receipt

- **Scenario:** Failure Handling: No false successful receipt.
- **Objective:** Establish the declared no false successful receipt behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Failure containment / cleanup / result.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Controlled fault at each named mandatory stage; preserve old destination, owned inode map and primary diagnostic.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output.
- **Expected Diagnostics:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Failure containment / cleanup / result; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T084 — SUCCEEDED

- **Scenario:** Result and Receipt: SUCCEEDED.
- **Objective:** Establish the declared succeeded behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriteResult / ArtifactMaterializationReceipt.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Verified committed set, exact manifest and logical destination; immutable ordered entries.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none.
- **Expected Diagnostics:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriteResult / ArtifactMaterializationReceipt; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T085 — FAILED

- **Scenario:** Result and Receipt: FAILED.
- **Objective:** Establish the declared failed behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriteResult / ArtifactMaterializationReceipt.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Verified committed set, exact manifest and logical destination; immutable ordered entries.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none.
- **Expected Diagnostics:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriteResult / ArtifactMaterializationReceipt; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T086 — INCOMPLETE

- **Scenario:** Result and Receipt: INCOMPLETE.
- **Objective:** Establish the declared incomplete behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriteResult / ArtifactMaterializationReceipt.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Verified committed set, exact manifest and logical destination; immutable ordered entries.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none.
- **Expected Diagnostics:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriteResult / ArtifactMaterializationReceipt; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T087 — Immutable result

- **Scenario:** Result and Receipt: Immutable result.
- **Objective:** Establish the declared immutable result behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriteResult / ArtifactMaterializationReceipt.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Verified committed set, exact manifest and logical destination; immutable ordered entries.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none.
- **Expected Diagnostics:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriteResult / ArtifactMaterializationReceipt; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T088 — Immutable receipt

- **Scenario:** Result and Receipt: Immutable receipt.
- **Objective:** Establish the declared immutable receipt behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriteResult / ArtifactMaterializationReceipt.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Verified committed set, exact manifest and logical destination; immutable ordered entries.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none.
- **Expected Diagnostics:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriteResult / ArtifactMaterializationReceipt; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T089 — Correct manifest identity

- **Scenario:** Result and Receipt: Correct manifest identity.
- **Objective:** Establish the declared correct manifest identity behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriteResult / ArtifactMaterializationReceipt.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Verified committed set, exact manifest and logical destination; immutable ordered entries.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none.
- **Expected Diagnostics:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriteResult / ArtifactMaterializationReceipt; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T090 — Correct artifact IDs

- **Scenario:** Result and Receipt: Correct artifact IDs.
- **Objective:** Establish the declared correct artifact ids behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriteResult / ArtifactMaterializationReceipt.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Verified committed set, exact manifest and logical destination; immutable ordered entries.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none.
- **Expected Diagnostics:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriteResult / ArtifactMaterializationReceipt; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T091 — Actual committed paths

- **Scenario:** Result and Receipt: Actual committed paths.
- **Objective:** Establish the declared actual committed paths behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriteResult / ArtifactMaterializationReceipt.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Verified committed set, exact manifest and logical destination; immutable ordered entries.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none.
- **Expected Diagnostics:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriteResult / ArtifactMaterializationReceipt; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T092 — Correct byte lengths

- **Scenario:** Result and Receipt: Correct byte lengths.
- **Objective:** Establish the declared correct byte lengths behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriteResult / ArtifactMaterializationReceipt.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Verified committed set, exact manifest and logical destination; immutable ordered entries.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none.
- **Expected Diagnostics:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriteResult / ArtifactMaterializationReceipt; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T093 — No staging-path leakage

- **Scenario:** Result and Receipt: No staging-path leakage.
- **Objective:** Establish the declared no staging-path leakage behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriteResult / ArtifactMaterializationReceipt.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Verified committed set, exact manifest and logical destination; immutable ordered entries.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none.
- **Expected Diagnostics:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriteResult / ArtifactMaterializationReceipt; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T094 — Invalid request

- **Scenario:** Diagnostics: Invalid request.
- **Objective:** Establish the declared invalid request behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CompilationDiagnostic / ArtifactWriteDiagnostics.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Existing CMP-02 enums and original diagnostics, writer stage and independent artifact/manifest identities.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame.
- **Expected Diagnostics:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CompilationDiagnostic / ArtifactWriteDiagnostics; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T095 — Missing payload

- **Scenario:** Diagnostics: Missing payload.
- **Objective:** Establish the declared missing payload behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CompilationDiagnostic / ArtifactWriteDiagnostics.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Existing CMP-02 enums and original diagnostics, writer stage and independent artifact/manifest identities.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame.
- **Expected Diagnostics:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CompilationDiagnostic / ArtifactWriteDiagnostics; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T096 — Unsafe path

- **Scenario:** Diagnostics: Unsafe path.
- **Objective:** Establish the declared unsafe path behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CompilationDiagnostic / ArtifactWriteDiagnostics.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Existing CMP-02 enums and original diagnostics, writer stage and independent artifact/manifest identities.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame.
- **Expected Diagnostics:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CompilationDiagnostic / ArtifactWriteDiagnostics; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T097 — Location collision

- **Scenario:** Diagnostics: Location collision.
- **Objective:** Establish the declared location collision behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CompilationDiagnostic / ArtifactWriteDiagnostics.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Existing CMP-02 enums and original diagnostics, writer stage and independent artifact/manifest identities.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame.
- **Expected Diagnostics:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CompilationDiagnostic / ArtifactWriteDiagnostics; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T098 — Destination conflict

- **Scenario:** Diagnostics: Destination conflict.
- **Objective:** Establish the declared destination conflict behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CompilationDiagnostic / ArtifactWriteDiagnostics.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Existing CMP-02 enums and original diagnostics, writer stage and independent artifact/manifest identities.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame.
- **Expected Diagnostics:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CompilationDiagnostic / ArtifactWriteDiagnostics; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T099 — Staging failure

- **Scenario:** Diagnostics: Staging failure.
- **Objective:** Establish the declared staging failure behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CompilationDiagnostic / ArtifactWriteDiagnostics.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Existing CMP-02 enums and original diagnostics, writer stage and independent artifact/manifest identities.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame.
- **Expected Diagnostics:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CompilationDiagnostic / ArtifactWriteDiagnostics; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T100 — Integrity mismatch

- **Scenario:** Diagnostics: Integrity mismatch.
- **Objective:** Establish the declared integrity mismatch behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CompilationDiagnostic / ArtifactWriteDiagnostics.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Existing CMP-02 enums and original diagnostics, writer stage and independent artifact/manifest identities.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame.
- **Expected Diagnostics:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CompilationDiagnostic / ArtifactWriteDiagnostics; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T101 — Commit failure

- **Scenario:** Diagnostics: Commit failure.
- **Objective:** Establish the declared commit failure behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CompilationDiagnostic / ArtifactWriteDiagnostics.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Existing CMP-02 enums and original diagnostics, writer stage and independent artifact/manifest identities.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame.
- **Expected Diagnostics:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CompilationDiagnostic / ArtifactWriteDiagnostics; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T102 — Cleanup failure

- **Scenario:** Diagnostics: Cleanup failure.
- **Objective:** Establish the declared cleanup failure behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CompilationDiagnostic / ArtifactWriteDiagnostics.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Existing CMP-02 enums and original diagnostics, writer stage and independent artifact/manifest identities.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame.
- **Expected Diagnostics:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CompilationDiagnostic / ArtifactWriteDiagnostics; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T103 — CMP-02 compatibility

- **Scenario:** Diagnostics: CMP-02 compatibility.
- **Objective:** Establish the declared cmp-02 compatibility behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CompilationDiagnostic / ArtifactWriteDiagnostics.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Existing CMP-02 enums and original diagnostics, writer stage and independent artifact/manifest identities.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame.
- **Expected Diagnostics:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CompilationDiagnostic / ArtifactWriteDiagnostics; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T104 — Pure Python domain

- **Scenario:** Django / DRF: Pure Python domain.
- **Objective:** Establish the declared pure python domain behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Framework / deployment integration boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Repository selects Django/DRF but neither distribution is installed and no compilation HTTP API exists. Tooling profile depends only on compiler-core public API.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request.
- **Expected Diagnostics:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Framework / deployment integration boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T105 — Filesystem adapter isolation

- **Scenario:** Django / DRF: Filesystem adapter isolation.
- **Objective:** Establish the declared filesystem adapter isolation behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Framework / deployment integration boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Repository selects Django/DRF but neither distribution is installed and no compilation HTTP API exists. Tooling profile depends only on compiler-core public API.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request.
- **Expected Diagnostics:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Framework / deployment integration boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T106 — No ORM models

- **Scenario:** Django / DRF: No ORM models.
- **Objective:** Establish the declared no orm models behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Framework / deployment integration boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Repository selects Django/DRF but neither distribution is installed and no compilation HTTP API exists. Tooling profile depends only on compiler-core public API.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request.
- **Expected Diagnostics:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Framework / deployment integration boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T107 — No migrations

- **Scenario:** Django / DRF: No migrations.
- **Objective:** Establish the declared no migrations behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Framework / deployment integration boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Repository selects Django/DRF but neither distribution is installed and no compilation HTTP API exists. Tooling profile depends only on compiler-core public API.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request.
- **Expected Diagnostics:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Framework / deployment integration boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T108 — Existing API compatibility

- **Scenario:** Django / DRF: Existing API compatibility.
- **Objective:** Establish the declared existing api compatibility behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Framework / deployment integration boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Repository selects Django/DRF but neither distribution is installed and no compilation HTTP API exists. Tooling profile depends only on compiler-core public API.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request.
- **Expected Diagnostics:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Framework / deployment integration boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T109 — No arbitrary remote write endpoint

- **Scenario:** Django / DRF: No arbitrary remote write endpoint.
- **Objective:** Establish the declared no arbitrary remote write endpoint behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Framework / deployment integration boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Repository selects Django/DRF but neither distribution is installed and no compilation HTTP API exists. Tooling profile depends only on compiler-core public API.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request.
- **Expected Diagnostics:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Framework / deployment integration boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T110 — Existing permissions preserved

- **Scenario:** Django / DRF: Existing permissions preserved.
- **Objective:** Establish the declared existing permissions preserved behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Framework / deployment integration boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Repository selects Django/DRF but neither distribution is installed and no compilation HTTP API exists. Tooling profile depends only on compiler-core public API.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request.
- **Expected Diagnostics:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Framework / deployment integration boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T111 — Customer artifact content

- **Scenario:** Mini Sales: Customer artifact content.
- **Objective:** Establish the declared customer artifact content behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Conceptual Mini Sales integration.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Use actual mini-sales canonical IDs/fields and mini-sales-references Employee definitions, future genuine final byte producer and matching original compilation/manifest.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt.
- **Expected Diagnostics:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Conceptual Mini Sales integration; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T112 — Employee artifact content

- **Scenario:** Mini Sales: Employee artifact content.
- **Objective:** Establish the declared employee artifact content behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Conceptual Mini Sales integration.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Use actual mini-sales canonical IDs/fields and mini-sales-references Employee definitions, future genuine final byte producer and matching original compilation/manifest.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt.
- **Expected Diagnostics:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Conceptual Mini Sales integration; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T113 — Matching CMP-07 manifest

- **Scenario:** Mini Sales: Matching CMP-07 manifest.
- **Objective:** Establish the declared matching cmp-07 manifest behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Conceptual Mini Sales integration.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Use actual mini-sales canonical IDs/fields and mini-sales-references Employee definitions, future genuine final byte producer and matching original compilation/manifest.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt.
- **Expected Diagnostics:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Conceptual Mini Sales integration; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T114 — Missing Employee payload

- **Scenario:** Mini Sales: Missing Employee payload.
- **Objective:** Establish the declared missing employee payload behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Conceptual Mini Sales integration.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Use actual mini-sales canonical IDs/fields and mini-sales-references Employee definitions, future genuine final byte producer and matching original compilation/manifest.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt.
- **Expected Diagnostics:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Conceptual Mini Sales integration; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T115 — Unsafe Customer path

- **Scenario:** Mini Sales: Unsafe Customer path.
- **Objective:** Establish the declared unsafe customer path behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Conceptual Mini Sales integration.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Use actual mini-sales canonical IDs/fields and mini-sales-references Employee definitions, future genuine final byte producer and matching original compilation/manifest.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt.
- **Expected Diagnostics:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Conceptual Mini Sales integration; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T116 — Duplicate Customer/Employee location

- **Scenario:** Mini Sales: Duplicate Customer/Employee location.
- **Objective:** Establish the declared duplicate customer/employee location behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Conceptual Mini Sales integration.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Use actual mini-sales canonical IDs/fields and mini-sales-references Employee definitions, future genuine final byte producer and matching original compilation/manifest.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt.
- **Expected Diagnostics:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Conceptual Mini Sales integration; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T117 — Partial staging failure

- **Scenario:** Mini Sales: Partial staging failure.
- **Objective:** Establish the declared partial staging failure behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Conceptual Mini Sales integration.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Use actual mini-sales canonical IDs/fields and mini-sales-references Employee definitions, future genuine final byte producer and matching original compilation/manifest.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt.
- **Expected Diagnostics:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Conceptual Mini Sales integration; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T118 — Successful receipt

- **Scenario:** Mini Sales: Successful receipt.
- **Objective:** Establish the declared successful receipt behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Conceptual Mini Sales integration.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Use actual mini-sales canonical IDs/fields and mini-sales-references Employee definitions, future genuine final byte producer and matching original compilation/manifest.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt.
- **Expected Diagnostics:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Conceptual Mini Sales integration; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T119 — No fabricated runtime artifact from Type IR

- **Scenario:** Mini Sales: No fabricated runtime artifact from Type IR.
- **Objective:** Establish the declared no fabricated runtime artifact from type ir behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Conceptual Mini Sales integration.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Use actual mini-sales canonical IDs/fields and mini-sales-references Employee definitions, future genuine final byte producer and matching original compilation/manifest.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt.
- **Expected Diagnostics:** Customer/Employee exact byte sources materialize only with future final producer. Missing Employee CMP-047, unsafe Customer path CMP-050, shared location CMP-051, staging I/O CMP-055 without partial commit. Type IR-only build remains INCOMPLETE and cannot produce runtime files or success receipt. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Conceptual Mini Sales integration; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T120 — No semantic validation duplication

- **Scenario:** Architectural Boundaries: No semantic validation duplication.
- **Objective:** Establish the declared no semantic validation duplication behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Architectural boundaries / production source inspection.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual module manifest, constrained artifact-materialization tooling profile, current semantic/model/compiler/runtime contracts.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success.
- **Expected Diagnostics:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Architectural boundaries / production source inspection; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T121 — No type lowering

- **Scenario:** Architectural Boundaries: No type lowering.
- **Objective:** Establish the declared no type lowering behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Architectural boundaries / production source inspection.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual module manifest, constrained artifact-materialization tooling profile, current semantic/model/compiler/runtime contracts.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success.
- **Expected Diagnostics:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Architectural boundaries / production source inspection; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T122 — No target-specific artifact encoding

- **Scenario:** Architectural Boundaries: No target-specific artifact encoding.
- **Objective:** Establish the declared no target-specific artifact encoding behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Architectural boundaries / production source inspection.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual module manifest, constrained artifact-materialization tooling profile, current semantic/model/compiler/runtime contracts.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success.
- **Expected Diagnostics:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Architectural boundaries / production source inspection; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T123 — No artifact generation

- **Scenario:** Architectural Boundaries: No artifact generation.
- **Objective:** Establish the declared no artifact generation behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Architectural boundaries / production source inspection.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual module manifest, constrained artifact-materialization tooling profile, current semantic/model/compiler/runtime contracts.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success.
- **Expected Diagnostics:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Architectural boundaries / production source inspection; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T124 — No publication

- **Scenario:** Architectural Boundaries: No publication.
- **Objective:** Establish the declared no publication behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Architectural boundaries / production source inspection.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual module manifest, constrained artifact-materialization tooling profile, current semantic/model/compiler/runtime contracts.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success.
- **Expected Diagnostics:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Architectural boundaries / production source inspection; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T125 — No deployment

- **Scenario:** Architectural Boundaries: No deployment.
- **Objective:** Establish the declared no deployment behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Architectural boundaries / production source inspection.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual module manifest, constrained artifact-materialization tooling profile, current semantic/model/compiler/runtime contracts.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success.
- **Expected Diagnostics:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Architectural boundaries / production source inspection; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T126 — No Control Plane authority

- **Scenario:** Architectural Boundaries: No Control Plane authority.
- **Objective:** Establish the declared no control plane authority behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Architectural boundaries / production source inspection.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual module manifest, constrained artifact-materialization tooling profile, current semantic/model/compiler/runtime contracts.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success.
- **Expected Diagnostics:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Architectural boundaries / production source inspection; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T127 — No runtime execution

- **Scenario:** Architectural Boundaries: No runtime execution.
- **Objective:** Establish the declared no runtime execution behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Architectural boundaries / production source inspection.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual module manifest, constrained artifact-materialization tooling profile, current semantic/model/compiler/runtime contracts.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success.
- **Expected Diagnostics:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Architectural boundaries / production source inspection; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T128 — No cloud storage

- **Scenario:** Architectural Boundaries: No cloud storage.
- **Objective:** Establish the declared no cloud storage behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Architectural boundaries / production source inspection.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual module manifest, constrained artifact-materialization tooling profile, current semantic/model/compiler/runtime contracts.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success.
- **Expected Diagnostics:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Architectural boundaries / production source inspection; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T129 — Filename boundaries and reserved stems

- **Scenario:** Path Safety: Filename boundaries and reserved stems.
- **Objective:** Establish the declared filename boundaries and reserved stems behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactRelativeLocation / fd-based root traversal.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Explicit trusted Linux local root with controlled ancestors, no-follow directory/file handles, flat portable ASCII layout.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape.
- **Expected Diagnostics:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactRelativeLocation / fd-based root traversal; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T130 — Trusted root permission and ancestor replacement assumptions

- **Scenario:** Path Safety: Trusted root permission and ancestor replacement assumptions.
- **Objective:** Establish the declared trusted root permission and ancestor replacement assumptions behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactRelativeLocation / fd-based root traversal.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Explicit trusted Linux local root with controlled ancestors, no-follow directory/file handles, flat portable ASCII layout.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape.
- **Expected Diagnostics:** Traversal, slash/backslash, percent/unicode encoding, NUL, empty/dot components, uppercase, reserved Windows stems, leading/trailing dot and oversized names reject CMP-050. Root symlink/unsafe ownership or writable ancestry rejects CMP-049 before staging; no escape. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactRelativeLocation / fd-based root traversal; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T131 — Default mapping exceeds 240-character bound

- **Scenario:** Deterministic Planning: Default mapping exceeds 240-character bound.
- **Objective:** Establish the declared default mapping exceeds 240-character bound behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactOutputLayout / ArtifactWritePlan.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Identical manifest bytes and approved kind layout, arbitrary source input order, explicit complete mapping when supplied.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. Maximum valid kind/key pair may produce an oversized default filename: CMP-050 before staging; explicit complete shorter safe mapping can be accepted.
- **Expected Result:** Maximum valid kind/key pair may produce an oversized default filename: CMP-050 before staging; explicit complete shorter safe mapping can be accepted.
- **Expected Diagnostics:** Plan orders existing artifact keys, retains bytes/source identity and stable relative locations. Duplicates/missing/wrong-kind layout reject CMP-051, plan mismatch CMP-046. Default kind__key.bin is deterministic; no suffix/time/PID/random final names. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactOutputLayout / ArtifactWritePlan; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T132 — Empty bytes are valid only as real approved producer bytes

- **Scenario:** Content Mapping: Empty bytes are valid only as real approved producer bytes.
- **Objective:** Establish the declared empty bytes are valid only as real approved producer bytes behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactContentSource / ArtifactByteContentSupport.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future genuinely approved frozen artifact class produced by an authorized final phase, CMP-07 exact kind approval and immutable bytes field; no current producer exists.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. An approved real b-empty payload produces a zero-length regular file and measured length 0; absent content is never replaced by empty bytes.
- **Expected Result:** An approved real b-empty payload produces a zero-length regular file and measured length 0; absent content is never replaced by empty bytes.
- **Expected Diagnostics:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactContentSource / ArtifactByteContentSupport; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T133 — Digest capability requires a separate declared field

- **Scenario:** Content Mapping: Digest capability requires a separate declared field.
- **Objective:** Establish the declared digest capability requires a separate declared field behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactContentSource / ArtifactByteContentSupport.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future genuinely approved frozen artifact class produced by an authorized final phase, CMP-07 exact kind approval and immutable bytes field; no current producer exists.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output.
- **Expected Diagnostics:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactContentSource / ArtifactByteContentSupport; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T134 — Hardlink or inode substitution during staging

- **Scenario:** Integrity: Hardlink or inode substitution during staging.
- **Objective:** Establish the declared hardlink or inode substitution during staging behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Staged exact byte / length / optional digest verification.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original immutable bytes, bounded chunk writes/reads, owned normal file with same inode/nlink=1 and optional producer-declared SHA-256.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature.
- **Expected Diagnostics:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Staged exact byte / length / optional digest verification; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T135 — Extra undeclared staging entry

- **Scenario:** Integrity: Extra undeclared staging entry.
- **Objective:** Establish the declared extra undeclared staging entry behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Staged exact byte / length / optional digest verification.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original immutable bytes, bounded chunk writes/reads, owned normal file with same inode/nlink=1 and optional producer-declared SHA-256.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature.
- **Expected Diagnostics:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Staged exact byte / length / optional digest verification; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T136 — Staged file metadata changes while reading

- **Scenario:** Integrity: Staged file metadata changes while reading.
- **Objective:** Establish the declared staged file metadata changes while reading behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Staged exact byte / length / optional digest verification.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original immutable bytes, bounded chunk writes/reads, owned normal file with same inode/nlink=1 and optional producer-declared SHA-256.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature.
- **Expected Diagnostics:** All files exact bytes/actual length, unchanged size/mtime/ctime and exact declared digest before commit. CMP-056 for mismatch/missing/extra/tampered file. Read/write I/O diagnosed; short writes loop, zero progress fails. Digest absent stays None, never fabricate digest/signature. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Staged exact byte / length / optional digest verification; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T137 — Exclusive file open failure must not adopt existing inode

- **Scenario:** Failure Handling: Exclusive file open failure must not adopt existing inode.
- **Objective:** Establish the declared exclusive file open failure must not adopt existing inode behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Failure containment / cleanup / result.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Controlled fault at each named mandatory stage; preserve old destination, owned inode map and primary diagnostic.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. Exclusive open failure adds no existing file to the owned map; cleanup refuses the unowned inventory and retains the primary I/O diagnostic plus CMP-058.
- **Expected Result:** Exclusive open failure adds no existing file to the owned map; cleanup refuses the unowned inventory and retains the primary I/O diagnostic plus CMP-058.
- **Expected Diagnostics:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Failure containment / cleanup / result; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T138 — Staging open failure leaves cleanup limitation diagnostic

- **Scenario:** Failure Handling: Staging open failure leaves cleanup limitation diagnostic.
- **Objective:** Establish the declared staging open failure leaves cleanup limitation diagnostic behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Failure containment / cleanup / result.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Controlled fault at each named mandatory stage; preserve old destination, owned inode map and primary diagnostic.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. No safe staging handle means no blind deletion; primary CMP-054 plus CMP-058, no final directory/receipt.
- **Expected Result:** No safe staging handle means no blind deletion; primary CMP-054 plus CMP-058, no final directory/receipt.
- **Expected Diagnostics:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Failure containment / cleanup / result; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T139 — Unknown or replaced staging resources are preserved

- **Scenario:** Failure Handling: Unknown or replaced staging resources are preserved.
- **Objective:** Establish the declared unknown or replaced staging resources are preserved behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Failure containment / cleanup / result.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Controlled fault at each named mandatory stage; preserve old destination, owned inode map and primary diagnostic.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output.
- **Expected Diagnostics:** No pre-commit failure exposes final output or receipt. Expected OS errors yield stage-associated FAILED/INCOMPLETE. Cleanup refuses unknown/changed inventory and emits CMP-058 in addition to primary; leaves unresolved staging for owner action. Unexpected programmer defects propagate after owned cleanup. Committed failures are explicit and never remove final output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Failure containment / cleanup / result; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T140 — Final parent fsync fails after successful rename

- **Scenario:** Durability: Final parent fsync fails after successful rename.
- **Objective:** Establish the declared final parent fsync fails after successful rename behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactDurabilityPolicy / fsync boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; VISIBLE_COMMIT or SYNCHRONIZED_COMMIT on supported local filesystem; controlled synchronization fault fixtures.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. Full destination may already be visible; failed/unsupported sync returns FAILED/CMP-055 or INCOMPLETE/CMP-060 with committed_destination, receipt None. Final directory remains intact.
- **Expected Result:** Full destination may already be visible; failed/unsupported sync returns FAILED/CMP-055 or INCOMPLETE/CMP-060 with committed_destination, receipt None. Final directory remains intact.
- **Expected Diagnostics:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactDurabilityPolicy / fsync boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T141 — Final directory binding changed after commit

- **Scenario:** Atomic Commit: Final directory binding changed after commit.
- **Objective:** Establish the declared final directory binding changed after commit behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Linux renameat2 RENAME_NOREPLACE commit.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual Linux/libc/kernel/filesystem support; all planned bytes verified in one staged directory.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback.
- **Expected Diagnostics:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Linux renameat2 RENAME_NOREPLACE commit; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T142 — renameat2 symbol exists but filesystem does not support NOREPLACE

- **Scenario:** Atomic Commit: renameat2 symbol exists but filesystem does not support NOREPLACE.
- **Objective:** Establish the declared renameat2 symbol exists but filesystem does not support noreplace behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Linux renameat2 RENAME_NOREPLACE commit.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual Linux/libc/kernel/filesystem support; all planned bytes verified in one staged directory.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback.
- **Expected Diagnostics:** One same-root complete-directory rename provides exclusive atomic visibility. EEXIST/ENOTEMPTY CMP-053; unavailable platform/libc/kernel/filesystem/EXDEV CMP-059 INCOMPLETE; other commit I/O CMP-057. No partial commit or replace fallback. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Linux renameat2 RENAME_NOREPLACE commit; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T143 — Bounded 32 staging-name collisions

- **Scenario:** Staging: Bounded 32 staging-name collisions.
- **Objective:** Establish the declared bounded 32 staging-name collisions behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** LocalFilesystemArtifactWriter private staging.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future controlled filesystem fixtures, root fd, exclusively allocated random writer-owned staging and tracked exclusive file inodes.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** 0700 staging under root on same filesystem; exclusive 0600 files. CMP-054 for staging failure. Any earlier/later error prevents commit; cleanup only owned identities and preserves primary evidence. Random staging never appears in receipt.
- **Expected Diagnostics:** 0700 staging under root on same filesystem; exclusive 0600 files. CMP-054 for staging failure. Any earlier/later error prevents commit; cleanup only owned identities and preserves primary evidence. Random staging never appears in receipt. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** LocalFilesystemArtifactWriter private staging; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T144 — Different destination names do not share collectors

- **Scenario:** Concurrent Writers: Different destination names do not share collectors.
- **Objective:** Establish the declared different destination names do not share collectors behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Cross-process exclusive commit.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Independent writer processes and separate private staging, same approved root/output token; no in-process lock relied upon.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** At most one succeeds; loser CMP-053 with no receipt and only its own staging removed. Winner unchanged. Independent destinations may succeed. No LWW/distributed lock/global mutable collector.
- **Expected Diagnostics:** At most one succeeds; loser CMP-053 with no receipt and only its own staging removed. Winner unchanged. Independent destinations may succeed. No LWW/distributed lock/global mutable collector. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Cross-process exclusive commit; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T145 — Writer associations participate in CMP-06 diagnostic comparison

- **Scenario:** Diagnostics: Writer associations participate in CMP-06 diagnostic comparison.
- **Objective:** Establish the declared writer associations participate in cmp-06 diagnostic comparison behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CompilationDiagnostic / ArtifactWriteDiagnostics.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Existing CMP-02 enums and original diagnostics, writer stage and independent artifact/manifest identities.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame.
- **Expected Diagnostics:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CompilationDiagnostic / ArtifactWriteDiagnostics; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T146 — Original compiler warnings are not duplicated on success

- **Scenario:** Diagnostics: Original compiler warnings are not duplicated on success.
- **Objective:** Establish the declared original compiler warnings are not duplicated on success behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** CompilationDiagnostic / ArtifactWriteDiagnostics.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Existing CMP-02 enums and original diagnostics, writer stage and independent artifact/manifest identities.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. Original compiler diagnostic objects retained once; assembly diagnostics already identical to those objects are not re-added.
- **Expected Result:** Original compiler diagnostic objects retained once; assembly diagnostics already identical to those objects are not re-added.
- **Expected Diagnostics:** Codes CMP-044..061 use RESULT origin with typed stage/artifact/manifest and only validated relative path. Public messages omit absolute roots/OS exception text/secrets. Original evidence retained; raw association includes new fields, legacy model projection unchanged; no invented semantic/source blame. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** CompilationDiagnostic / ArtifactWriteDiagnostics; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T147 — Post-commit failure has visible destination and no receipt

- **Scenario:** Result and Receipt: Post-commit failure has visible destination and no receipt.
- **Objective:** Establish the declared post-commit failure has visible destination and no receipt behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriteResult / ArtifactMaterializationReceipt.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Verified committed set, exact manifest and logical destination; immutable ordered entries.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none.
- **Expected Diagnostics:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriteResult / ArtifactMaterializationReceipt; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T148 — Receipt contains no artifact payload

- **Scenario:** Result and Receipt: Receipt contains no artifact payload.
- **Objective:** Establish the declared receipt contains no artifact payload behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriteResult / ArtifactMaterializationReceipt.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Verified committed set, exact manifest and logical destination; immutable ordered entries.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none.
- **Expected Diagnostics:** Only full committed success creates receipt. It retains manifest identity/association, exact descriptor membership/kind, safe relative locations, measured lengths, optional verified declared digest and durability; no payload or staging path. Invalid status/receipt combination rejects, FAILED/INCOMPLETE has none. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriteResult / ArtifactMaterializationReceipt; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T149 — Same-valued compilation from a different output origin is rejected

- **Scenario:** Compilation Prerequisites: Same-valued compilation from a different output origin is rejected.
- **Objective:** Establish the declared same-valued compilation from a different output origin is rejected behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWritePlanner compilation gate.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original BUILD_TARGET result, original VALID/READY evidence, canonical object, scope, compiler configuration and output_origin.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun.
- **Expected Diagnostics:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWritePlanner compilation gate; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T150 — Compiler configuration drift after manifest assembly

- **Scenario:** Compilation Prerequisites: Compiler configuration drift after manifest assembly.
- **Objective:** Establish the declared compiler configuration drift after manifest assembly behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWritePlanner compilation gate.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Original BUILD_TARGET result, original VALID/READY evidence, canonical object, scope, compiler configuration and output_origin.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun.
- **Expected Diagnostics:** Accept only SUCCEEDED. FAILED/INCOMPLETE reject CMP-045; request/evidence/scope/target/configuration mismatch retains CMP-07/CMP-06 rejection plus CMP-046. No phases or validation rerun. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWritePlanner compilation gate; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T151 — Byte sources in reverse order still bind original artifact identities

- **Scenario:** Content Mapping: Byte sources in reverse order still bind original artifact identities.
- **Objective:** Establish the declared byte sources in reverse order still bind original artifact identities behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactContentSource / ArtifactByteContentSupport.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Future genuinely approved frozen artifact class produced by an authorized final phase, CMP-07 exact kind approval and immutable bytes field; no current producer exists.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output.
- **Expected Diagnostics:** Exactly one supplied source must be the original result artifact object. Missing/extra/repeated/copied sources reject CMP-047. Missing byte approval CMP-048 INCOMPLETE; text/bytearray/memoryview/implicit encoder CMP-061 INCOMPLETE. No invented output. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactContentSource / ArtifactByteContentSupport; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T152 — Explicit mapping must match every descriptor kind

- **Scenario:** Deterministic Planning: Explicit mapping must match every descriptor kind.
- **Objective:** Establish the declared explicit mapping must match every descriptor kind behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactOutputLayout / ArtifactWritePlan.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Identical manifest bytes and approved kind layout, arbitrary source input order, explicit complete mapping when supplied.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Plan orders existing artifact keys, retains bytes/source identity and stable relative locations. Duplicates/missing/wrong-kind layout reject CMP-051, plan mismatch CMP-046. Default kind__key.bin is deterministic; no suffix/time/PID/random final names.
- **Expected Diagnostics:** Plan orders existing artifact keys, retains bytes/source identity and stable relative locations. Duplicates/missing/wrong-kind layout reject CMP-051, plan mismatch CMP-046. Default kind__key.bin is deterministic; no suffix/time/PID/random final names. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactOutputLayout / ArtifactWritePlan; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T153 — Unsupported file fsync capability produces INCOMPLETE

- **Scenario:** Durability: Unsupported file fsync capability produces INCOMPLETE.
- **Objective:** Establish the declared unsupported file fsync capability produces incomplete behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactDurabilityPolicy / fsync boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; VISIBLE_COMMIT or SYNCHRONIZED_COMMIT on supported local filesystem; controlled synchronization fault fixtures.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee.
- **Expected Diagnostics:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactDurabilityPolicy / fsync boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T154 — Cleanup synchronization failure retains primary failure

- **Scenario:** Durability: Cleanup synchronization failure retains primary failure.
- **Objective:** Establish the declared cleanup synchronization failure retains primary failure behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactDurabilityPolicy / fsync boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; VISIBLE_COMMIT or SYNCHRONIZED_COMMIT on supported local filesystem; controlled synchronization fault fixtures.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee.
- **Expected Diagnostics:** Visible mode claims only complete visible rename. Synchronized mode root capability precheck, each file fsync, staged directory fsync, rename then root fsync. Unsupported required sync CMP-060 INCOMPLETE; actual sync I/O CMP-055 FAILED. Post-rename failure records committed_destination, no success receipt; no hardware/replication guarantee. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactDurabilityPolicy / fsync boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T155 — Caller attempts an infinite or unordered inventory

- **Scenario:** Writer Contracts: Caller attempts an infinite or unordered inventory.
- **Objective:** Establish the declared caller attempts an infinite or unordered inventory behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** ArtifactWriter / immutable ArtifactWriteRequest.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Typed original result, successful CMP-07 assembly, actual content sources and approved logical destination.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Supported exact inputs are planned; wrong roots reject CMP-044/049, unsupported policy CMP-052 INCOMPLETE. Interface constructs without frameworks.
- **Expected Diagnostics:** Supported exact inputs are planned; wrong roots reject CMP-044/049, unsupported policy CMP-052 INCOMPLETE. Interface constructs without frameworks. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** ArtifactWriter / immutable ArtifactWriteRequest; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T156 — New tooling module affects historical module-count expectations

- **Scenario:** Django / DRF: New tooling module affects historical module-count expectations.
- **Objective:** Establish the declared new tooling module affects historical module-count expectations behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Framework / deployment integration boundaries.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Repository selects Django/DRF but neither distribution is installed and no compilation HTTP API exists. Tooling profile depends only on compiler-core public API.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request.
- **Expected Diagnostics:** Contracts construct without Django, filesystems remain tooling-owned; no ORM/migration/HTTP endpoint/auth changes. Future server wiring uses approved root references and existing permissions; never raw root from remote request. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Framework / deployment integration boundaries; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T157 — Trusted in-process association is not portable authenticated provenance

- **Scenario:** Architectural Boundaries: Trusted in-process association is not portable authenticated provenance.
- **Objective:** Establish the declared trusted in-process association is not portable authenticated provenance behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Architectural boundaries / production source inspection.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual module manifest, constrained artifact-materialization tooling profile, current semantic/model/compiler/runtime contracts.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success.
- **Expected Diagnostics:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Architectural boundaries / production source inspection; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-08-T158 — No materialization or Mini Sales execution during this task

- **Scenario:** Architectural Boundaries: No materialization or Mini Sales execution during this task.
- **Objective:** Establish the declared no materialization or mini sales execution during this task behavior and ensure it cannot bypass complete-set materialization requirements.
- **Component:** Architectural boundaries / production source inspection.
- **Prerequisites:** Explicit later authorization and fixed implementation revision; Actual module manifest, constrained artifact-materialization tooling profile, current semantic/model/compiler/runtime contracts.
- **Input / Setup:** Start from the category prerequisites; vary only the named scenario condition, retaining original typed evidence and recording destination inventory before/after. For invalid, fault, security or conflict cases introduce that exact condition; for successful cases supply the complete approved set. 
- **Expected Result:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success.
- **Expected Diagnostics:** No semantic validation/type lowering/encoder/generator/publisher/deployer/Control Plane/runtime/cloud behavior is added or executed. No compiler-to-tool edge, neutral filesystem capability relaxation, exception or runtime dependency. Static inspection does not establish deferred suite success. Successful supported cases add no error; invalid/unavailable cases must expose their bounded code, actual stage and typed artifact/manifest association where applicable, without absolute path leakage.
- **Boundary / Edge Cases:** Repeat the specified condition at the first/last artifact and relevant empty/single/multiple-member or minimum/maximum path/byte boundary; preserve exact versions, order and explicit policy. No invented producer or guessed canonical identifiers.
- **Integration Dependencies:** Architectural boundaries / production source inspection; original Kernel/model/validation/CMP-01..07 contracts; approved filesystem and producer capabilities only when the scenario needs them.
- **Acceptance Criteria:** All named observations and expected diagnostics recorded against the fixed revision; no missing/extra artifacts, partial success, overwrite, unsafe cleanup, fake receipt or broadened guarantee. Static checks alone cannot satisfy this case.
- **Execution Status:** NOT_RUN — DEFERRED

