# CMP-09 — Deferred Test Specification

Task: CMP-09 — Artifact Reader

Backend: Python / Django / Django REST Framework

Status: NOT_RUN — DEFERRED

New Tests Implemented: 0

Tests Executed: 0

Dependencies:
- SK-11 (general contract unavailable; retain existing CMP-02 narrow diagnostics)
- MOD-04
- MOD-08
- CMP-01
- CMP-02
- CMP-06
- CMP-07
- CMP-08

Documentation date: 2026-10-11. Testing: **DEFERRED / NOT VERIFIED**.

This is the sole CMP-09 archive document. Latest task section 45 prohibits README/additional archive files and overrides generic earlier archive layout for CMP-09 only; existing archives/scenarios/genuine execution history are preserved.

Scope: pure reader contracts, manifest/original receipt binding, explicit bounded identity selection and manifest ordering; trusted root configuration reuse; read-only Linux fd traversal/file-type checks; exact bounded byte/length/declared-digest checks; typed actual verification and atomic result payloads; CMP-02 diagnostics. No write/repair/decode/generate/runtime/HTTP features.

Future execution prerequisites: explicit later permission, fixed source revision, genuine approved final producer and valid original manifest/materialization receipt; disposable trusted Linux local roots with controlled ancestry/UID/no-follow/NONBLOCK/NOATIME capabilities; future fault/concurrency fixtures and recorded evidence. No executable scenarios, fixtures, scaffolds or manual write/read experiments are supplied or executed now.

Limitations: current final producer absent; no real receipt/materialization/read demonstration. Only existing flat portable filenames and original same-UID trusted Linux local root model supported; remote/other OS/alternate locator paths unsupported. Receipt and compiler association are trusted in-process metadata, not authentication/portable proof. Length always present; size-only cannot detect same-size corruption; available declared SHA-256 verifies bytes, not authority. Metadata/name-binding checks cannot prove immutable concurrent snapshots. Complete-set reads cover declared selected files, not directory exclusivity. Read-only app code uses O_NOATIME for files; underlying filesystem/access side effects are outside a universal no-state-change claim. Finite payload limits bound byte buffers, not exact total interpreter/RSS overhead or disk latency; conversion may transiently duplicate an individual bounded byte buffer. Hostile same-UID/privileged actors/root moves are outside approved isolation. No general SK-11/TYPE-01/HTTP interface added.

Total documented scenarios: **173**.

## CMP-09-T001 — Valid reader invocation

- **Scenario:** Reader Contract: Valid reader invocation.
- **Objective:** Establish the exact valid reader invocation behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReader / ArtifactReadRequest.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual immutable CMP-07 manifest, CMP-08 receipt, selected identities, logical source and bounded policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Typed supported requests plan/read; wrong root request CMP-062; missing manifest CMP-063, receipt CMP-064, selection CMP-066, source CMP-067, policy CMP-080. Pure contracts require no framework initialization.
- **Expected Diagnostics:** Typed supported requests plan/read; wrong root request CMP-062; missing manifest CMP-063, receipt CMP-064, selection CMP-066, source CMP-067, policy CMP-080. Pure contracts require no framework initialization. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReader / ArtifactReadRequest; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T002 — Invalid request

- **Scenario:** Reader Contract: Invalid request.
- **Objective:** Establish the exact invalid request behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReader / ArtifactReadRequest.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual immutable CMP-07 manifest, CMP-08 receipt, selected identities, logical source and bounded policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Typed supported requests plan/read; wrong root request CMP-062; missing manifest CMP-063, receipt CMP-064, selection CMP-066, source CMP-067, policy CMP-080. Pure contracts require no framework initialization.
- **Expected Diagnostics:** Typed supported requests plan/read; wrong root request CMP-062; missing manifest CMP-063, receipt CMP-064, selection CMP-066, source CMP-067, policy CMP-080. Pure contracts require no framework initialization. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReader / ArtifactReadRequest; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T003 — Missing read source

- **Scenario:** Reader Contract: Missing read source.
- **Objective:** Establish the exact missing read source behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReader / ArtifactReadRequest.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual immutable CMP-07 manifest, CMP-08 receipt, selected identities, logical source and bounded policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Typed supported requests plan/read; wrong root request CMP-062; missing manifest CMP-063, receipt CMP-064, selection CMP-066, source CMP-067, policy CMP-080. Pure contracts require no framework initialization.
- **Expected Diagnostics:** Typed supported requests plan/read; wrong root request CMP-062; missing manifest CMP-063, receipt CMP-064, selection CMP-066, source CMP-067, policy CMP-080. Pure contracts require no framework initialization. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReader / ArtifactReadRequest; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T004 — Unsupported read policy

- **Scenario:** Reader Contract: Unsupported read policy.
- **Objective:** Establish the exact unsupported read policy behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReader / ArtifactReadRequest.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual immutable CMP-07 manifest, CMP-08 receipt, selected identities, logical source and bounded policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Typed supported requests plan/read; wrong root request CMP-062; missing manifest CMP-063, receipt CMP-064, selection CMP-066, source CMP-067, policy CMP-080. Pure contracts require no framework initialization.
- **Expected Diagnostics:** Typed supported requests plan/read; wrong root request CMP-062; missing manifest CMP-063, receipt CMP-064, selection CMP-066, source CMP-067, policy CMP-080. Pure contracts require no framework initialization. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReader / ArtifactReadRequest; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T005 — Framework-independent interface

- **Scenario:** Reader Contract: Framework-independent interface.
- **Objective:** Establish the exact framework-independent interface behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReader / ArtifactReadRequest.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual immutable CMP-07 manifest, CMP-08 receipt, selected identities, logical source and bounded policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Typed supported requests plan/read; wrong root request CMP-062; missing manifest CMP-063, receipt CMP-064, selection CMP-066, source CMP-067, policy CMP-080. Pure contracts require no framework initialization.
- **Expected Diagnostics:** Typed supported requests plan/read; wrong root request CMP-062; missing manifest CMP-063, receipt CMP-064, selection CMP-066, source CMP-067, policy CMP-080. Pure contracts require no framework initialization. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReader / ArtifactReadRequest; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T006 — Valid CMP-07 manifest

- **Scenario:** Manifest Prerequisites: Valid CMP-07 manifest.
- **Objective:** Establish the exact valid cmp-07 manifest behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPlanner manifest gate.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Original complete V0 manifest, bound canonical/VALID-READY evidence, context/target/output_origin and completed final artifact outcomes.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Revalidate existing manifest structure/input/output association before filesystem access. Invalid/missing declaration CMP-063, retain existing CMP-07 causes. Unknown selected key CMP-065. Never reconstruct a manifest from disk or treat IR as final artifacts. Live compiler configuration is not rerun/audited as a new compilation.
- **Expected Diagnostics:** Revalidate existing manifest structure/input/output association before filesystem access. Invalid/missing declaration CMP-063, retain existing CMP-07 causes. Unknown selected key CMP-065. Never reconstruct a manifest from disk or treat IR as final artifacts. Live compiler configuration is not rerun/audited as a new compilation. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPlanner manifest gate; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T007 — Missing manifest

- **Scenario:** Manifest Prerequisites: Missing manifest.
- **Objective:** Establish the exact missing manifest behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPlanner manifest gate.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Original complete V0 manifest, bound canonical/VALID-READY evidence, context/target/output_origin and completed final artifact outcomes.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Revalidate existing manifest structure/input/output association before filesystem access. Invalid/missing declaration CMP-063, retain existing CMP-07 causes. Unknown selected key CMP-065. Never reconstruct a manifest from disk or treat IR as final artifacts. Live compiler configuration is not rerun/audited as a new compilation.
- **Expected Diagnostics:** Revalidate existing manifest structure/input/output association before filesystem access. Invalid/missing declaration CMP-063, retain existing CMP-07 causes. Unknown selected key CMP-065. Never reconstruct a manifest from disk or treat IR as final artifacts. Live compiler configuration is not rerun/audited as a new compilation. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPlanner manifest gate; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T008 — Unsupported schema

- **Scenario:** Manifest Prerequisites: Unsupported schema.
- **Objective:** Establish the exact unsupported schema behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPlanner manifest gate.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Original complete V0 manifest, bound canonical/VALID-READY evidence, context/target/output_origin and completed final artifact outcomes.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Revalidate existing manifest structure/input/output association before filesystem access. Invalid/missing declaration CMP-063, retain existing CMP-07 causes. Unknown selected key CMP-065. Never reconstruct a manifest from disk or treat IR as final artifacts. Live compiler configuration is not rerun/audited as a new compilation.
- **Expected Diagnostics:** Revalidate existing manifest structure/input/output association before filesystem access. Invalid/missing declaration CMP-063, retain existing CMP-07 causes. Unknown selected key CMP-065. Never reconstruct a manifest from disk or treat IR as final artifacts. Live compiler configuration is not rerun/audited as a new compilation. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPlanner manifest gate; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T009 — Unknown artifact identity

- **Scenario:** Manifest Prerequisites: Unknown artifact identity.
- **Objective:** Establish the exact unknown artifact identity behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPlanner manifest gate.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Original complete V0 manifest, bound canonical/VALID-READY evidence, context/target/output_origin and completed final artifact outcomes.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Revalidate existing manifest structure/input/output association before filesystem access. Invalid/missing declaration CMP-063, retain existing CMP-07 causes. Unknown selected key CMP-065. Never reconstruct a manifest from disk or treat IR as final artifacts. Live compiler configuration is not rerun/audited as a new compilation.
- **Expected Diagnostics:** Revalidate existing manifest structure/input/output association before filesystem access. Invalid/missing declaration CMP-063, retain existing CMP-07 causes. Unknown selected key CMP-065. Never reconstruct a manifest from disk or treat IR as final artifacts. Live compiler configuration is not rerun/audited as a new compilation. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPlanner manifest gate; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T010 — Incomplete descriptor

- **Scenario:** Manifest Prerequisites: Incomplete descriptor.
- **Objective:** Establish the exact incomplete descriptor behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPlanner manifest gate.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Original complete V0 manifest, bound canonical/VALID-READY evidence, context/target/output_origin and completed final artifact outcomes.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Revalidate existing manifest structure/input/output association before filesystem access. Invalid/missing declaration CMP-063, retain existing CMP-07 causes. Unknown selected key CMP-065. Never reconstruct a manifest from disk or treat IR as final artifacts. Live compiler configuration is not rerun/audited as a new compilation.
- **Expected Diagnostics:** Revalidate existing manifest structure/input/output association before filesystem access. Invalid/missing declaration CMP-063, retain existing CMP-07 causes. Unknown selected key CMP-065. Never reconstruct a manifest from disk or treat IR as final artifacts. Live compiler configuration is not rerun/audited as a new compilation. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPlanner manifest gate; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T011 — No manifest reconstructed from directory listing

- **Scenario:** Manifest Prerequisites: No manifest reconstructed from directory listing.
- **Objective:** Establish the exact no manifest reconstructed from directory listing behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPlanner manifest gate.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Original complete V0 manifest, bound canonical/VALID-READY evidence, context/target/output_origin and completed final artifact outcomes.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Revalidate existing manifest structure/input/output association before filesystem access. Invalid/missing declaration CMP-063, retain existing CMP-07 causes. Unknown selected key CMP-065. Never reconstruct a manifest from disk or treat IR as final artifacts. Live compiler configuration is not rerun/audited as a new compilation.
- **Expected Diagnostics:** Revalidate existing manifest structure/input/output association before filesystem access. Invalid/missing declaration CMP-063, retain existing CMP-07 causes. Unknown selected key CMP-065. Never reconstruct a manifest from disk or treat IR as final artifacts. Live compiler configuration is not rerun/audited as a new compilation. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPlanner manifest gate; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T012 — Valid CMP-08 receipt

- **Scenario:** Receipt Prerequisites: Valid CMP-08 receipt.
- **Objective:** Establish the exact valid cmp-08 receipt behavior without broadening read scope, evidence or authority.
- **Component:** Receipt consistency preflight.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual CMP-08 ArtifactMaterializationReceipt with exact declaration and same original compilation_association object, full ordered descriptors, distinct safe locations and source destination.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists.
- **Expected Diagnostics:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt consistency preflight; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T013 — Missing required receipt

- **Scenario:** Receipt Prerequisites: Missing required receipt.
- **Objective:** Establish the exact missing required receipt behavior without broadening read scope, evidence or authority.
- **Component:** Receipt consistency preflight.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual CMP-08 ArtifactMaterializationReceipt with exact declaration and same original compilation_association object, full ordered descriptors, distinct safe locations and source destination.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists.
- **Expected Diagnostics:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt consistency preflight; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T014 — Receipt/manifest identity mismatch

- **Scenario:** Receipt Prerequisites: Receipt/manifest identity mismatch.
- **Objective:** Establish the exact receipt/manifest identity mismatch behavior without broadening read scope, evidence or authority.
- **Component:** Receipt consistency preflight.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual CMP-08 ArtifactMaterializationReceipt with exact declaration and same original compilation_association object, full ordered descriptors, distinct safe locations and source destination.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists.
- **Expected Diagnostics:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt consistency preflight; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T015 — Compilation association mismatch

- **Scenario:** Receipt Prerequisites: Compilation association mismatch.
- **Objective:** Establish the exact compilation association mismatch behavior without broadening read scope, evidence or authority.
- **Component:** Receipt consistency preflight.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual CMP-08 ArtifactMaterializationReceipt with exact declaration and same original compilation_association object, full ordered descriptors, distinct safe locations and source destination.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists.
- **Expected Diagnostics:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt consistency preflight; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T016 — Missing receipt entry

- **Scenario:** Receipt Prerequisites: Missing receipt entry.
- **Objective:** Establish the exact missing receipt entry behavior without broadening read scope, evidence or authority.
- **Component:** Receipt consistency preflight.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual CMP-08 ArtifactMaterializationReceipt with exact declaration and same original compilation_association object, full ordered descriptors, distinct safe locations and source destination.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists.
- **Expected Diagnostics:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt consistency preflight; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T017 — Extra receipt entry

- **Scenario:** Receipt Prerequisites: Extra receipt entry.
- **Objective:** Establish the exact extra receipt entry behavior without broadening read scope, evidence or authority.
- **Component:** Receipt consistency preflight.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual CMP-08 ArtifactMaterializationReceipt with exact declaration and same original compilation_association object, full ordered descriptors, distinct safe locations and source destination.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists.
- **Expected Diagnostics:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt consistency preflight; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T018 — Duplicate receipt entry

- **Scenario:** Receipt Prerequisites: Duplicate receipt entry.
- **Objective:** Establish the exact duplicate receipt entry behavior without broadening read scope, evidence or authority.
- **Component:** Receipt consistency preflight.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual CMP-08 ArtifactMaterializationReceipt with exact declaration and same original compilation_association object, full ordered descriptors, distinct safe locations and source destination.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists.
- **Expected Diagnostics:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt consistency preflight; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T019 — Destination mismatch

- **Scenario:** Receipt Prerequisites: Destination mismatch.
- **Objective:** Establish the exact destination mismatch behavior without broadening read scope, evidence or authority.
- **Component:** Receipt consistency preflight.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual CMP-08 ArtifactMaterializationReceipt with exact declaration and same original compilation_association object, full ordered descriptors, distinct safe locations and source destination.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists.
- **Expected Diagnostics:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt consistency preflight; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T020 — Single artifact

- **Scenario:** Artifact Selection: Single artifact.
- **Objective:** Establish the exact single artifact behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadSelection / selected plan.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; ONE with exactly one key, nonempty distinct explicit SET or ALL with no overrides; keys are existing CompilationArtifactKey values.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope.
- **Expected Diagnostics:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadSelection / selected plan; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T021 — Explicit subset

- **Scenario:** Artifact Selection: Explicit subset.
- **Objective:** Establish the exact explicit subset behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadSelection / selected plan.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; ONE with exactly one key, nonempty distinct explicit SET or ALL with no overrides; keys are existing CompilationArtifactKey values.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope.
- **Expected Diagnostics:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadSelection / selected plan; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T022 — Complete artifact set

- **Scenario:** Artifact Selection: Complete artifact set.
- **Objective:** Establish the exact complete artifact set behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadSelection / selected plan.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; ONE with exactly one key, nonempty distinct explicit SET or ALL with no overrides; keys are existing CompilationArtifactKey values.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope.
- **Expected Diagnostics:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadSelection / selected plan; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T023 — Unknown ID

- **Scenario:** Artifact Selection: Unknown ID.
- **Objective:** Establish the exact unknown id behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadSelection / selected plan.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; ONE with exactly one key, nonempty distinct explicit SET or ALL with no overrides; keys are existing CompilationArtifactKey values.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope.
- **Expected Diagnostics:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadSelection / selected plan; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T024 — Duplicate selected IDs

- **Scenario:** Artifact Selection: Duplicate selected IDs.
- **Objective:** Establish the exact duplicate selected ids behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadSelection / selected plan.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; ONE with exactly one key, nonempty distinct explicit SET or ALL with no overrides; keys are existing CompilationArtifactKey values.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope.
- **Expected Diagnostics:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadSelection / selected plan; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T025 — Empty selection

- **Scenario:** Artifact Selection: Empty selection.
- **Objective:** Establish the exact empty selection behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadSelection / selected plan.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; ONE with exactly one key, nonempty distinct explicit SET or ALL with no overrides; keys are existing CompilationArtifactKey values.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope.
- **Expected Diagnostics:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadSelection / selected plan; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T026 — No implicit dependency closure

- **Scenario:** Artifact Selection: No implicit dependency closure.
- **Objective:** Establish the exact no implicit dependency closure behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadSelection / selected plan.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; ONE with exactly one key, nonempty distinct explicit SET or ALL with no overrides; keys are existing CompilationArtifactKey values.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope.
- **Expected Diagnostics:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadSelection / selected plan; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T027 — No filename-based fallback

- **Scenario:** Artifact Selection: No filename-based fallback.
- **Objective:** Establish the exact no filename-based fallback behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadSelection / selected plan.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; ONE with exactly one key, nonempty distinct explicit SET or ALL with no overrides; keys are existing CompilationArtifactKey values.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope.
- **Expected Diagnostics:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadSelection / selected plan; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T028 — Valid committed relative path

- **Scenario:** Path Safety: Valid committed relative path.
- **Objective:** Establish the exact valid committed relative path behavior without broadening read scope, evidence or authority.
- **Component:** Receipt locator / Linux fd containment.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactRelativeLocation flat lowercase portable ASCII grammar, server root/output tokens and trusted ApprovedLocalArtifactRoot.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened.
- **Expected Diagnostics:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt locator / Linux fd containment; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T029 — Absolute path

- **Scenario:** Path Safety: Absolute path.
- **Objective:** Establish the exact absolute path behavior without broadening read scope, evidence or authority.
- **Component:** Receipt locator / Linux fd containment.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactRelativeLocation flat lowercase portable ASCII grammar, server root/output tokens and trusted ApprovedLocalArtifactRoot.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened.
- **Expected Diagnostics:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt locator / Linux fd containment; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T030 — Parent traversal

- **Scenario:** Path Safety: Parent traversal.
- **Objective:** Establish the exact parent traversal behavior without broadening read scope, evidence or authority.
- **Component:** Receipt locator / Linux fd containment.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactRelativeLocation flat lowercase portable ASCII grammar, server root/output tokens and trusted ApprovedLocalArtifactRoot.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened.
- **Expected Diagnostics:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt locator / Linux fd containment; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T031 — NUL byte

- **Scenario:** Path Safety: NUL byte.
- **Objective:** Establish the exact nul byte behavior without broadening read scope, evidence or authority.
- **Component:** Receipt locator / Linux fd containment.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactRelativeLocation flat lowercase portable ASCII grammar, server root/output tokens and trusted ApprovedLocalArtifactRoot.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened.
- **Expected Diagnostics:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt locator / Linux fd containment; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T032 — Unsupported separator

- **Scenario:** Path Safety: Unsupported separator.
- **Objective:** Establish the exact unsupported separator behavior without broadening read scope, evidence or authority.
- **Component:** Receipt locator / Linux fd containment.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactRelativeLocation flat lowercase portable ASCII grammar, server root/output tokens and trusted ApprovedLocalArtifactRoot.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened.
- **Expected Diagnostics:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt locator / Linux fd containment; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T033 — Ambiguous normalized path

- **Scenario:** Path Safety: Ambiguous normalized path.
- **Objective:** Establish the exact ambiguous normalized path behavior without broadening read scope, evidence or authority.
- **Component:** Receipt locator / Linux fd containment.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactRelativeLocation flat lowercase portable ASCII grammar, server root/output tokens and trusted ApprovedLocalArtifactRoot.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened.
- **Expected Diagnostics:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt locator / Linux fd containment; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T034 — Symlinked file

- **Scenario:** Path Safety: Symlinked file.
- **Objective:** Establish the exact symlinked file behavior without broadening read scope, evidence or authority.
- **Component:** Receipt locator / Linux fd containment.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactRelativeLocation flat lowercase portable ASCII grammar, server root/output tokens and trusted ApprovedLocalArtifactRoot.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened.
- **Expected Diagnostics:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt locator / Linux fd containment; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T035 — Symlinked parent

- **Scenario:** Path Safety: Symlinked parent.
- **Objective:** Establish the exact symlinked parent behavior without broadening read scope, evidence or authority.
- **Component:** Receipt locator / Linux fd containment.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactRelativeLocation flat lowercase portable ASCII grammar, server root/output tokens and trusted ApprovedLocalArtifactRoot.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened.
- **Expected Diagnostics:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt locator / Linux fd containment; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T036 — Escape from approved root

- **Scenario:** Path Safety: Escape from approved root.
- **Objective:** Establish the exact escape from approved root behavior without broadening read scope, evidence or authority.
- **Component:** Receipt locator / Linux fd containment.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactRelativeLocation flat lowercase portable ASCII grammar, server root/output tokens and trusted ApprovedLocalArtifactRoot.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened.
- **Expected Diagnostics:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt locator / Linux fd containment; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T037 — Regular file

- **Scenario:** File-Type Security: Regular file.
- **Objective:** Establish the exact regular file behavior without broadening read scope, evidence or authority.
- **Component:** Opened file-type and identity checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled future Linux local fixtures, lstat before open, O_RDONLY|O_NOFOLLOW|O_NONBLOCK|O_NOATIME handles and fstat.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects.
- **Expected Diagnostics:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Opened file-type and identity checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T038 — Directory

- **Scenario:** File-Type Security: Directory.
- **Objective:** Establish the exact directory behavior without broadening read scope, evidence or authority.
- **Component:** Opened file-type and identity checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled future Linux local fixtures, lstat before open, O_RDONLY|O_NOFOLLOW|O_NONBLOCK|O_NOATIME handles and fstat.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects.
- **Expected Diagnostics:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Opened file-type and identity checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T039 — FIFO

- **Scenario:** File-Type Security: FIFO.
- **Objective:** Establish the exact fifo behavior without broadening read scope, evidence or authority.
- **Component:** Opened file-type and identity checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled future Linux local fixtures, lstat before open, O_RDONLY|O_NOFOLLOW|O_NONBLOCK|O_NOATIME handles and fstat.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects.
- **Expected Diagnostics:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Opened file-type and identity checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T040 — Socket

- **Scenario:** File-Type Security: Socket.
- **Objective:** Establish the exact socket behavior without broadening read scope, evidence or authority.
- **Component:** Opened file-type and identity checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled future Linux local fixtures, lstat before open, O_RDONLY|O_NOFOLLOW|O_NONBLOCK|O_NOATIME handles and fstat.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects.
- **Expected Diagnostics:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Opened file-type and identity checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T041 — Device file

- **Scenario:** File-Type Security: Device file.
- **Objective:** Establish the exact device file behavior without broadening read scope, evidence or authority.
- **Component:** Opened file-type and identity checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled future Linux local fixtures, lstat before open, O_RDONLY|O_NOFOLLOW|O_NONBLOCK|O_NOATIME handles and fstat.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects.
- **Expected Diagnostics:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Opened file-type and identity checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T042 — Symlink

- **Scenario:** File-Type Security: Symlink.
- **Objective:** Establish the exact symlink behavior without broadening read scope, evidence or authority.
- **Component:** Opened file-type and identity checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled future Linux local fixtures, lstat before open, O_RDONLY|O_NOFOLLOW|O_NONBLOCK|O_NOATIME handles and fstat.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects.
- **Expected Diagnostics:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Opened file-type and identity checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T043 — Unsupported special file

- **Scenario:** File-Type Security: Unsupported special file.
- **Objective:** Establish the exact unsupported special file behavior without broadening read scope, evidence or authority.
- **Component:** Opened file-type and identity checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled future Linux local fixtures, lstat before open, O_RDONLY|O_NOFOLLOW|O_NONBLOCK|O_NOATIME handles and fstat.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects.
- **Expected Diagnostics:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Opened file-type and identity checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T044 — Safe opening behavior

- **Scenario:** File-Type Security: Safe opening behavior.
- **Objective:** Establish the exact safe opening behavior behavior without broadening read scope, evidence or authority.
- **Component:** Opened file-type and identity checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled future Linux local fixtures, lstat before open, O_RDONLY|O_NOFOLLOW|O_NONBLOCK|O_NOATIME handles and fstat.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects.
- **Expected Diagnostics:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Opened file-type and identity checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T045 — Exact bytes

- **Scenario:** Byte Retrieval: Exact bytes.
- **Objective:** Establish the exact exact bytes behavior without broadening read scope, evidence or authority.
- **Component:** RetrievedArtifact / exact byte retrieval.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Future real previously materialized approved producer bytes; actual receipt lengths, optional declared digest.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Return immutable exact bytes including empty/binary/non-UTF8/line endings/whitespace. No decoding/normalization/import/pickle/eval/exec or writes. RetrievedArtifact is separate from original CompilationArtifact. Empty genuine file with length 0 is valid.
- **Expected Diagnostics:** Return immutable exact bytes including empty/binary/non-UTF8/line endings/whitespace. No decoding/normalization/import/pickle/eval/exec or writes. RetrievedArtifact is separate from original CompilationArtifact. Empty genuine file with length 0 is valid. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** RetrievedArtifact / exact byte retrieval; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T046 — Empty permitted artifact

- **Scenario:** Byte Retrieval: Empty permitted artifact.
- **Objective:** Establish the exact empty permitted artifact behavior without broadening read scope, evidence or authority.
- **Component:** RetrievedArtifact / exact byte retrieval.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Future real previously materialized approved producer bytes; actual receipt lengths, optional declared digest.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Return immutable exact bytes including empty/binary/non-UTF8/line endings/whitespace. No decoding/normalization/import/pickle/eval/exec or writes. RetrievedArtifact is separate from original CompilationArtifact. Empty genuine file with length 0 is valid.
- **Expected Diagnostics:** Return immutable exact bytes including empty/binary/non-UTF8/line endings/whitespace. No decoding/normalization/import/pickle/eval/exec or writes. RetrievedArtifact is separate from original CompilationArtifact. Empty genuine file with length 0 is valid. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** RetrievedArtifact / exact byte retrieval; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T047 — Binary content

- **Scenario:** Byte Retrieval: Binary content.
- **Objective:** Establish the exact binary content behavior without broadening read scope, evidence or authority.
- **Component:** RetrievedArtifact / exact byte retrieval.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Future real previously materialized approved producer bytes; actual receipt lengths, optional declared digest.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Return immutable exact bytes including empty/binary/non-UTF8/line endings/whitespace. No decoding/normalization/import/pickle/eval/exec or writes. RetrievedArtifact is separate from original CompilationArtifact. Empty genuine file with length 0 is valid.
- **Expected Diagnostics:** Return immutable exact bytes including empty/binary/non-UTF8/line endings/whitespace. No decoding/normalization/import/pickle/eval/exec or writes. RetrievedArtifact is separate from original CompilationArtifact. Empty genuine file with length 0 is valid. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** RetrievedArtifact / exact byte retrieval; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T048 — Non-UTF-8 bytes

- **Scenario:** Byte Retrieval: Non-UTF-8 bytes.
- **Objective:** Establish the exact non-utf-8 bytes behavior without broadening read scope, evidence or authority.
- **Component:** RetrievedArtifact / exact byte retrieval.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Future real previously materialized approved producer bytes; actual receipt lengths, optional declared digest.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Return immutable exact bytes including empty/binary/non-UTF8/line endings/whitespace. No decoding/normalization/import/pickle/eval/exec or writes. RetrievedArtifact is separate from original CompilationArtifact. Empty genuine file with length 0 is valid.
- **Expected Diagnostics:** Return immutable exact bytes including empty/binary/non-UTF8/line endings/whitespace. No decoding/normalization/import/pickle/eval/exec or writes. RetrievedArtifact is separate from original CompilationArtifact. Empty genuine file with length 0 is valid. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** RetrievedArtifact / exact byte retrieval; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T049 — No text normalization

- **Scenario:** Byte Retrieval: No text normalization.
- **Objective:** Establish the exact no text normalization behavior without broadening read scope, evidence or authority.
- **Component:** RetrievedArtifact / exact byte retrieval.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Future real previously materialized approved producer bytes; actual receipt lengths, optional declared digest.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Return immutable exact bytes including empty/binary/non-UTF8/line endings/whitespace. No decoding/normalization/import/pickle/eval/exec or writes. RetrievedArtifact is separate from original CompilationArtifact. Empty genuine file with length 0 is valid.
- **Expected Diagnostics:** Return immutable exact bytes including empty/binary/non-UTF8/line endings/whitespace. No decoding/normalization/import/pickle/eval/exec or writes. RetrievedArtifact is separate from original CompilationArtifact. Empty genuine file with length 0 is valid. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** RetrievedArtifact / exact byte retrieval; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T050 — No deserialization

- **Scenario:** Byte Retrieval: No deserialization.
- **Objective:** Establish the exact no deserialization behavior without broadening read scope, evidence or authority.
- **Component:** RetrievedArtifact / exact byte retrieval.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Future real previously materialized approved producer bytes; actual receipt lengths, optional declared digest.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Return immutable exact bytes including empty/binary/non-UTF8/line endings/whitespace. No decoding/normalization/import/pickle/eval/exec or writes. RetrievedArtifact is separate from original CompilationArtifact. Empty genuine file with length 0 is valid.
- **Expected Diagnostics:** Return immutable exact bytes including empty/binary/non-UTF8/line endings/whitespace. No decoding/normalization/import/pickle/eval/exec or writes. RetrievedArtifact is separate from original CompilationArtifact. Empty genuine file with length 0 is valid. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** RetrievedArtifact / exact byte retrieval; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T051 — No artifact mutation

- **Scenario:** Byte Retrieval: No artifact mutation.
- **Objective:** Establish the exact no artifact mutation behavior without broadening read scope, evidence or authority.
- **Component:** RetrievedArtifact / exact byte retrieval.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Future real previously materialized approved producer bytes; actual receipt lengths, optional declared digest.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Return immutable exact bytes including empty/binary/non-UTF8/line endings/whitespace. No decoding/normalization/import/pickle/eval/exec or writes. RetrievedArtifact is separate from original CompilationArtifact. Empty genuine file with length 0 is valid.
- **Expected Diagnostics:** Return immutable exact bytes including empty/binary/non-UTF8/line endings/whitespace. No decoding/normalization/import/pickle/eval/exec or writes. RetrievedArtifact is separate from original CompilationArtifact. Empty genuine file with length 0 is valid. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** RetrievedArtifact / exact byte retrieval; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T052 — Maximum artifact size

- **Scenario:** Resource Bounds: Maximum artifact size.
- **Objective:** Establish the exact maximum artifact size behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPolicy / effective bounded plan / chunk reads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Caller and trusted server policy; defaults 32 MiB/artifact, 128 MiB aggregate, 128 artifacts; positive actual ints and size/digest enum.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails.
- **Expected Diagnostics:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPolicy / effective bounded plan / chunk reads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T053 — Maximum aggregate size

- **Scenario:** Resource Bounds: Maximum aggregate size.
- **Objective:** Establish the exact maximum aggregate size behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPolicy / effective bounded plan / chunk reads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Caller and trusted server policy; defaults 32 MiB/artifact, 128 MiB aggregate, 128 artifacts; positive actual ints and size/digest enum.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails.
- **Expected Diagnostics:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPolicy / effective bounded plan / chunk reads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T054 — Maximum artifact count

- **Scenario:** Resource Bounds: Maximum artifact count.
- **Objective:** Establish the exact maximum artifact count behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPolicy / effective bounded plan / chunk reads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Caller and trusted server policy; defaults 32 MiB/artifact, 128 MiB aggregate, 128 artifacts; positive actual ints and size/digest enum.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails.
- **Expected Diagnostics:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPolicy / effective bounded plan / chunk reads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T055 — Invalid limit

- **Scenario:** Resource Bounds: Invalid limit.
- **Objective:** Establish the exact invalid limit behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPolicy / effective bounded plan / chunk reads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Caller and trusted server policy; defaults 32 MiB/artifact, 128 MiB aggregate, 128 artifacts; positive actual ints and size/digest enum.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails.
- **Expected Diagnostics:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPolicy / effective bounded plan / chunk reads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T056 — Oversized actual file

- **Scenario:** Resource Bounds: Oversized actual file.
- **Objective:** Establish the exact oversized actual file behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPolicy / effective bounded plan / chunk reads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Caller and trusted server policy; defaults 32 MiB/artifact, 128 MiB aggregate, 128 artifacts; positive actual ints and size/digest enum.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails.
- **Expected Diagnostics:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPolicy / effective bounded plan / chunk reads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T057 — Oversized declared file

- **Scenario:** Resource Bounds: Oversized declared file.
- **Objective:** Establish the exact oversized declared file behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPolicy / effective bounded plan / chunk reads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Caller and trusted server policy; defaults 32 MiB/artifact, 128 MiB aggregate, 128 artifacts; positive actual ints and size/digest enum.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails.
- **Expected Diagnostics:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPolicy / effective bounded plan / chunk reads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T058 — Early read abort

- **Scenario:** Resource Bounds: Early read abort.
- **Objective:** Establish the exact early read abort behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPolicy / effective bounded plan / chunk reads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Caller and trusted server policy; defaults 32 MiB/artifact, 128 MiB aggregate, 128 artifacts; positive actual ints and size/digest enum.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails.
- **Expected Diagnostics:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPolicy / effective bounded plan / chunk reads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T059 — No unbounded memory allocation

- **Scenario:** Resource Bounds: No unbounded memory allocation.
- **Objective:** Establish the exact no unbounded memory allocation behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPolicy / effective bounded plan / chunk reads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Caller and trusted server policy; defaults 32 MiB/artifact, 128 MiB aggregate, 128 artifacts; positive actual ints and size/digest enum.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails.
- **Expected Diagnostics:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPolicy / effective bounded plan / chunk reads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T060 — Matching expected size

- **Scenario:** Byte Length Verification: Matching expected size.
- **Objective:** Establish the exact matching expected size behavior without broadening read scope, evidence or authority.
- **Component:** Expected/actual length evidence.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing receipt always supplies nonnegative byte_length; exact known expected length and opened regular file.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Stored or read length mismatch CMP-073 (larger file beyond limits may first CMP-072). Matching bytes record equal measured expected/actual lengths. No missing-size path supported: malformed/missing receipt length CMP-064. Same-size corruption without digest is not detectable cryptographically.
- **Expected Diagnostics:** Stored or read length mismatch CMP-073 (larger file beyond limits may first CMP-072). Matching bytes record equal measured expected/actual lengths. No missing-size path supported: malformed/missing receipt length CMP-064. Same-size corruption without digest is not detectable cryptographically. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Expected/actual length evidence; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T061 — Smaller stored file

- **Scenario:** Byte Length Verification: Smaller stored file.
- **Objective:** Establish the exact smaller stored file behavior without broadening read scope, evidence or authority.
- **Component:** Expected/actual length evidence.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing receipt always supplies nonnegative byte_length; exact known expected length and opened regular file.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Stored or read length mismatch CMP-073 (larger file beyond limits may first CMP-072). Matching bytes record equal measured expected/actual lengths. No missing-size path supported: malformed/missing receipt length CMP-064. Same-size corruption without digest is not detectable cryptographically.
- **Expected Diagnostics:** Stored or read length mismatch CMP-073 (larger file beyond limits may first CMP-072). Matching bytes record equal measured expected/actual lengths. No missing-size path supported: malformed/missing receipt length CMP-064. Same-size corruption without digest is not detectable cryptographically. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Expected/actual length evidence; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T062 — Larger stored file

- **Scenario:** Byte Length Verification: Larger stored file.
- **Objective:** Establish the exact larger stored file behavior without broadening read scope, evidence or authority.
- **Component:** Expected/actual length evidence.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing receipt always supplies nonnegative byte_length; exact known expected length and opened regular file.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Stored or read length mismatch CMP-073 (larger file beyond limits may first CMP-072). Matching bytes record equal measured expected/actual lengths. No missing-size path supported: malformed/missing receipt length CMP-064. Same-size corruption without digest is not detectable cryptographically.
- **Expected Diagnostics:** Stored or read length mismatch CMP-073 (larger file beyond limits may first CMP-072). Matching bytes record equal measured expected/actual lengths. No missing-size path supported: malformed/missing receipt length CMP-064. Same-size corruption without digest is not detectable cryptographically. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Expected/actual length evidence; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T063 — Missing expected size where permitted

- **Scenario:** Byte Length Verification: Missing expected size where permitted.
- **Objective:** Establish the exact missing expected size where permitted behavior without broadening read scope, evidence or authority.
- **Component:** Expected/actual length evidence.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing receipt always supplies nonnegative byte_length; exact known expected length and opened regular file.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Stored or read length mismatch CMP-073 (larger file beyond limits may first CMP-072). Matching bytes record equal measured expected/actual lengths. No missing-size path supported: malformed/missing receipt length CMP-064. Same-size corruption without digest is not detectable cryptographically.
- **Expected Diagnostics:** Stored or read length mismatch CMP-073 (larger file beyond limits may first CMP-072). Matching bytes record equal measured expected/actual lengths. No missing-size path supported: malformed/missing receipt length CMP-064. Same-size corruption without digest is not detectable cryptographically. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Expected/actual length evidence; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T064 — Size-only evidence limitations

- **Scenario:** Byte Length Verification: Size-only evidence limitations.
- **Objective:** Establish the exact size-only evidence limitations behavior without broadening read scope, evidence or authority.
- **Component:** Expected/actual length evidence.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing receipt always supplies nonnegative byte_length; exact known expected length and opened regular file.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Stored or read length mismatch CMP-073 (larger file beyond limits may first CMP-072). Matching bytes record equal measured expected/actual lengths. No missing-size path supported: malformed/missing receipt length CMP-064. Same-size corruption without digest is not detectable cryptographically.
- **Expected Diagnostics:** Stored or read length mismatch CMP-073 (larger file beyond limits may first CMP-072). Matching bytes record equal measured expected/actual lengths. No missing-size path supported: malformed/missing receipt length CMP-064. Same-size corruption without digest is not detectable cryptographically. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Expected/actual length evidence; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T065 — Supported digest algorithm

- **Scenario:** Digest Verification: Supported digest algorithm.
- **Objective:** Establish the exact supported digest algorithm behavior without broadening read scope, evidence or authority.
- **Component:** Receipt digest / actual verification.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactContentDigest explicit sha256/lowercase 64-hex, receipt.verified_digest, policy SIZE_VERIFIED or DIGEST_VERIFIED.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim.
- **Expected Diagnostics:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt digest / actual verification; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T066 — Matching digest

- **Scenario:** Digest Verification: Matching digest.
- **Objective:** Establish the exact matching digest behavior without broadening read scope, evidence or authority.
- **Component:** Receipt digest / actual verification.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactContentDigest explicit sha256/lowercase 64-hex, receipt.verified_digest, policy SIZE_VERIFIED or DIGEST_VERIFIED.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim.
- **Expected Diagnostics:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt digest / actual verification; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T067 — Mismatched digest

- **Scenario:** Digest Verification: Mismatched digest.
- **Objective:** Establish the exact mismatched digest behavior without broadening read scope, evidence or authority.
- **Component:** Receipt digest / actual verification.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactContentDigest explicit sha256/lowercase 64-hex, receipt.verified_digest, policy SIZE_VERIFIED or DIGEST_VERIFIED.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim.
- **Expected Diagnostics:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt digest / actual verification; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T068 — Missing mandatory digest

- **Scenario:** Digest Verification: Missing mandatory digest.
- **Objective:** Establish the exact missing mandatory digest behavior without broadening read scope, evidence or authority.
- **Component:** Receipt digest / actual verification.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactContentDigest explicit sha256/lowercase 64-hex, receipt.verified_digest, policy SIZE_VERIFIED or DIGEST_VERIFIED.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim.
- **Expected Diagnostics:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt digest / actual verification; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T069 — Malformed digest declaration

- **Scenario:** Digest Verification: Malformed digest declaration.
- **Objective:** Establish the exact malformed digest declaration behavior without broadening read scope, evidence or authority.
- **Component:** Receipt digest / actual verification.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactContentDigest explicit sha256/lowercase 64-hex, receipt.verified_digest, policy SIZE_VERIFIED or DIGEST_VERIFIED.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim.
- **Expected Diagnostics:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt digest / actual verification; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T070 — Unknown algorithm

- **Scenario:** Digest Verification: Unknown algorithm.
- **Objective:** Establish the exact unknown algorithm behavior without broadening read scope, evidence or authority.
- **Component:** Receipt digest / actual verification.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactContentDigest explicit sha256/lowercase 64-hex, receipt.verified_digest, policy SIZE_VERIFIED or DIGEST_VERIFIED.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim.
- **Expected Diagnostics:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt digest / actual verification; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T071 — No hash-as-authenticity claim

- **Scenario:** Digest Verification: No hash-as-authenticity claim.
- **Objective:** Establish the exact no hash-as-authenticity claim behavior without broadening read scope, evidence or authority.
- **Component:** Receipt digest / actual verification.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactContentDigest explicit sha256/lowercase 64-hex, receipt.verified_digest, policy SIZE_VERIFIED or DIGEST_VERIFIED.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim.
- **Expected Diagnostics:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt digest / actual verification; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T072 — Identity/location verification

- **Scenario:** Read Integrity: Identity/location verification.
- **Objective:** Establish the exact identity/location verification behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadVerification evidence.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual immutable retrieved bytes with length checks and optional reverified receipt digest.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Evidence reports SIZE_VERIFIED only without digest and DIGEST_VERIFIED only after declared digest matched retrieved bytes. Expected/actual lengths match. Receipt historical verification does not replace current checking; identity/location alone is insufficient success under v0.
- **Expected Diagnostics:** Evidence reports SIZE_VERIFIED only without digest and DIGEST_VERIFIED only after declared digest matched retrieved bytes. Expected/actual lengths match. Receipt historical verification does not replace current checking; identity/location alone is insufficient success under v0. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadVerification evidence; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T073 — Size verification

- **Scenario:** Read Integrity: Size verification.
- **Objective:** Establish the exact size verification behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadVerification evidence.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual immutable retrieved bytes with length checks and optional reverified receipt digest.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Evidence reports SIZE_VERIFIED only without digest and DIGEST_VERIFIED only after declared digest matched retrieved bytes. Expected/actual lengths match. Receipt historical verification does not replace current checking; identity/location alone is insufficient success under v0.
- **Expected Diagnostics:** Evidence reports SIZE_VERIFIED only without digest and DIGEST_VERIFIED only after declared digest matched retrieved bytes. Expected/actual lengths match. Receipt historical verification does not replace current checking; identity/location alone is insufficient success under v0. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadVerification evidence; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T074 — Digest verification

- **Scenario:** Read Integrity: Digest verification.
- **Objective:** Establish the exact digest verification behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadVerification evidence.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual immutable retrieved bytes with length checks and optional reverified receipt digest.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Evidence reports SIZE_VERIFIED only without digest and DIGEST_VERIFIED only after declared digest matched retrieved bytes. Expected/actual lengths match. Receipt historical verification does not replace current checking; identity/location alone is insufficient success under v0.
- **Expected Diagnostics:** Evidence reports SIZE_VERIFIED only without digest and DIGEST_VERIFIED only after declared digest matched retrieved bytes. Expected/actual lengths match. Receipt historical verification does not replace current checking; identity/location alone is insufficient success under v0. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadVerification evidence; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T075 — Actual verification evidence

- **Scenario:** Read Integrity: Actual verification evidence.
- **Objective:** Establish the exact actual verification evidence behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadVerification evidence.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual immutable retrieved bytes with length checks and optional reverified receipt digest.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Evidence reports SIZE_VERIFIED only without digest and DIGEST_VERIFIED only after declared digest matched retrieved bytes. Expected/actual lengths match. Receipt historical verification does not replace current checking; identity/location alone is insufficient success under v0.
- **Expected Diagnostics:** Evidence reports SIZE_VERIFIED only without digest and DIGEST_VERIFIED only after declared digest matched retrieved bytes. Expected/actual lengths match. Receipt historical verification does not replace current checking; identity/location alone is insufficient success under v0. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadVerification evidence; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T076 — No fabricated integrity level

- **Scenario:** Read Integrity: No fabricated integrity level.
- **Objective:** Establish the exact no fabricated integrity level behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadVerification evidence.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual immutable retrieved bytes with length checks and optional reverified receipt digest.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Evidence reports SIZE_VERIFIED only without digest and DIGEST_VERIFIED only after declared digest matched retrieved bytes. Expected/actual lengths match. Receipt historical verification does not replace current checking; identity/location alone is insufficient success under v0.
- **Expected Diagnostics:** Evidence reports SIZE_VERIFIED only without digest and DIGEST_VERIFIED only after declared digest matched retrieved bytes. Expected/actual lengths match. Receipt historical verification does not replace current checking; identity/location alone is insufficient success under v0. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadVerification evidence; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T077 — Receipt evidence versus current bytes

- **Scenario:** Read Integrity: Receipt evidence versus current bytes.
- **Objective:** Establish the exact receipt evidence versus current bytes behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadVerification evidence.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual immutable retrieved bytes with length checks and optional reverified receipt digest.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Evidence reports SIZE_VERIFIED only without digest and DIGEST_VERIFIED only after declared digest matched retrieved bytes. Expected/actual lengths match. Receipt historical verification does not replace current checking; identity/location alone is insufficient success under v0.
- **Expected Diagnostics:** Evidence reports SIZE_VERIFIED only without digest and DIGEST_VERIFIED only after declared digest matched retrieved bytes. Expected/actual lengths match. Receipt historical verification does not replace current checking; identity/location alone is insufficient success under v0. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadVerification evidence; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T078 — Manifest order

- **Scenario:** Deterministic Ordering: Manifest order.
- **Objective:** Establish the exact manifest order behavior without broadening read scope, evidence or authority.
- **Component:** Manifest-order sequential plan / diagnostics.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Identical accepted manifest/receipt/source/policy and unchanged bytes/filesystem state; input selections can be reversed.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Sequential reads and returned selected keys follow existing manifest key order, no directory enumeration/path/time/object-ID/concurrency order. First selected failure deterministic; diagnostics preserve actual stage/location/artifact/manifest. No repeat-read behavior is executed now.
- **Expected Diagnostics:** Sequential reads and returned selected keys follow existing manifest key order, no directory enumeration/path/time/object-ID/concurrency order. First selected failure deterministic; diagnostics preserve actual stage/location/artifact/manifest. No repeat-read behavior is executed now. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Manifest-order sequential plan / diagnostics; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T079 — Explicit subset order policy

- **Scenario:** Deterministic Ordering: Explicit subset order policy.
- **Objective:** Establish the exact explicit subset order policy behavior without broadening read scope, evidence or authority.
- **Component:** Manifest-order sequential plan / diagnostics.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Identical accepted manifest/receipt/source/policy and unchanged bytes/filesystem state; input selections can be reversed.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Sequential reads and returned selected keys follow existing manifest key order, no directory enumeration/path/time/object-ID/concurrency order. First selected failure deterministic; diagnostics preserve actual stage/location/artifact/manifest. No repeat-read behavior is executed now.
- **Expected Diagnostics:** Sequential reads and returned selected keys follow existing manifest key order, no directory enumeration/path/time/object-ID/concurrency order. First selected failure deterministic; diagnostics preserve actual stage/location/artifact/manifest. No repeat-read behavior is executed now. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Manifest-order sequential plan / diagnostics; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T080 — Multiple artifacts

- **Scenario:** Deterministic Ordering: Multiple artifacts.
- **Objective:** Establish the exact multiple artifacts behavior without broadening read scope, evidence or authority.
- **Component:** Manifest-order sequential plan / diagnostics.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Identical accepted manifest/receipt/source/policy and unchanged bytes/filesystem state; input selections can be reversed.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Sequential reads and returned selected keys follow existing manifest key order, no directory enumeration/path/time/object-ID/concurrency order. First selected failure deterministic; diagnostics preserve actual stage/location/artifact/manifest. No repeat-read behavior is executed now.
- **Expected Diagnostics:** Sequential reads and returned selected keys follow existing manifest key order, no directory enumeration/path/time/object-ID/concurrency order. First selected failure deterministic; diagnostics preserve actual stage/location/artifact/manifest. No repeat-read behavior is executed now. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Manifest-order sequential plan / diagnostics; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T081 — No filesystem enumeration order

- **Scenario:** Deterministic Ordering: No filesystem enumeration order.
- **Objective:** Establish the exact no filesystem enumeration order behavior without broadening read scope, evidence or authority.
- **Component:** Manifest-order sequential plan / diagnostics.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Identical accepted manifest/receipt/source/policy and unchanged bytes/filesystem state; input selections can be reversed.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Sequential reads and returned selected keys follow existing manifest key order, no directory enumeration/path/time/object-ID/concurrency order. First selected failure deterministic; diagnostics preserve actual stage/location/artifact/manifest. No repeat-read behavior is executed now.
- **Expected Diagnostics:** Sequential reads and returned selected keys follow existing manifest key order, no directory enumeration/path/time/object-ID/concurrency order. First selected failure deterministic; diagnostics preserve actual stage/location/artifact/manifest. No repeat-read behavior is executed now. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Manifest-order sequential plan / diagnostics; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T082 — Stable diagnostics

- **Scenario:** Deterministic Ordering: Stable diagnostics.
- **Objective:** Establish the exact stable diagnostics behavior without broadening read scope, evidence or authority.
- **Component:** Manifest-order sequential plan / diagnostics.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Identical accepted manifest/receipt/source/policy and unchanged bytes/filesystem state; input selections can be reversed.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Sequential reads and returned selected keys follow existing manifest key order, no directory enumeration/path/time/object-ID/concurrency order. First selected failure deterministic; diagnostics preserve actual stage/location/artifact/manifest. No repeat-read behavior is executed now.
- **Expected Diagnostics:** Sequential reads and returned selected keys follow existing manifest key order, no directory enumeration/path/time/object-ID/concurrency order. First selected failure deterministic; diagnostics preserve actual stage/location/artifact/manifest. No repeat-read behavior is executed now. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Manifest-order sequential plan / diagnostics; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T083 — Stable failure ordering

- **Scenario:** Deterministic Ordering: Stable failure ordering.
- **Objective:** Establish the exact stable failure ordering behavior without broadening read scope, evidence or authority.
- **Component:** Manifest-order sequential plan / diagnostics.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Identical accepted manifest/receipt/source/policy and unchanged bytes/filesystem state; input selections can be reversed.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Sequential reads and returned selected keys follow existing manifest key order, no directory enumeration/path/time/object-ID/concurrency order. First selected failure deterministic; diagnostics preserve actual stage/location/artifact/manifest. No repeat-read behavior is executed now.
- **Expected Diagnostics:** Sequential reads and returned selected keys follow existing manifest key order, no directory enumeration/path/time/object-ID/concurrency order. First selected failure deterministic; diagnostics preserve actual stage/location/artifact/manifest. No repeat-read behavior is executed now. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Manifest-order sequential plan / diagnostics; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T084 — All selected artifacts succeed

- **Scenario:** Atomic Read Result: All selected artifacts succeed.
- **Objective:** Establish the exact all selected artifacts succeed behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadResult atomic exposed payloads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Selected immutable plan and future per-artifact success/fault setup at each position.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Success requires every selected entry verified and within effective limits. First/later failure returns FAILED/INCOMPLETE with artifacts=(), no partial payload exposure. Plan retains exact selection and complete_set true only for ALL. This is result atomicity, not a multi-file filesystem snapshot.
- **Expected Diagnostics:** Success requires every selected entry verified and within effective limits. First/later failure returns FAILED/INCOMPLETE with artifacts=(), no partial payload exposure. Plan retains exact selection and complete_set true only for ALL. This is result atomicity, not a multi-file filesystem snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadResult atomic exposed payloads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T085 — First artifact fails

- **Scenario:** Atomic Read Result: First artifact fails.
- **Objective:** Establish the exact first artifact fails behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadResult atomic exposed payloads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Selected immutable plan and future per-artifact success/fault setup at each position.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Success requires every selected entry verified and within effective limits. First/later failure returns FAILED/INCOMPLETE with artifacts=(), no partial payload exposure. Plan retains exact selection and complete_set true only for ALL. This is result atomicity, not a multi-file filesystem snapshot.
- **Expected Diagnostics:** Success requires every selected entry verified and within effective limits. First/later failure returns FAILED/INCOMPLETE with artifacts=(), no partial payload exposure. Plan retains exact selection and complete_set true only for ALL. This is result atomicity, not a multi-file filesystem snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadResult atomic exposed payloads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T086 — Later artifact fails

- **Scenario:** Atomic Read Result: Later artifact fails.
- **Objective:** Establish the exact later artifact fails behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadResult atomic exposed payloads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Selected immutable plan and future per-artifact success/fault setup at each position.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Success requires every selected entry verified and within effective limits. First/later failure returns FAILED/INCOMPLETE with artifacts=(), no partial payload exposure. Plan retains exact selection and complete_set true only for ALL. This is result atomicity, not a multi-file filesystem snapshot.
- **Expected Diagnostics:** Success requires every selected entry verified and within effective limits. First/later failure returns FAILED/INCOMPLETE with artifacts=(), no partial payload exposure. Plan retains exact selection and complete_set true only for ALL. This is result atomicity, not a multi-file filesystem snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadResult atomic exposed payloads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T087 — No partial complete-set success

- **Scenario:** Atomic Read Result: No partial complete-set success.
- **Objective:** Establish the exact no partial complete-set success behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadResult atomic exposed payloads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Selected immutable plan and future per-artifact success/fault setup at each position.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Success requires every selected entry verified and within effective limits. First/later failure returns FAILED/INCOMPLETE with artifacts=(), no partial payload exposure. Plan retains exact selection and complete_set true only for ALL. This is result atomicity, not a multi-file filesystem snapshot.
- **Expected Diagnostics:** Success requires every selected entry verified and within effective limits. First/later failure returns FAILED/INCOMPLETE with artifacts=(), no partial payload exposure. Plan retains exact selection and complete_set true only for ALL. This is result atomicity, not a multi-file filesystem snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadResult atomic exposed payloads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T088 — Previous retrieved bytes not exposed as successful complete output

- **Scenario:** Atomic Read Result: Previous retrieved bytes not exposed as successful complete output.
- **Objective:** Establish the exact previous retrieved bytes not exposed as successful complete output behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadResult atomic exposed payloads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Selected immutable plan and future per-artifact success/fault setup at each position.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Success requires every selected entry verified and within effective limits. First/later failure returns FAILED/INCOMPLETE with artifacts=(), no partial payload exposure. Plan retains exact selection and complete_set true only for ALL. This is result atomicity, not a multi-file filesystem snapshot.
- **Expected Diagnostics:** Success requires every selected entry verified and within effective limits. First/later failure returns FAILED/INCOMPLETE with artifacts=(), no partial payload exposure. Plan retains exact selection and complete_set true only for ALL. This is result atomicity, not a multi-file filesystem snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadResult atomic exposed payloads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T089 — Explicit selected-scope success

- **Scenario:** Atomic Read Result: Explicit selected-scope success.
- **Objective:** Establish the exact explicit selected-scope success behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadResult atomic exposed payloads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Selected immutable plan and future per-artifact success/fault setup at each position.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Success requires every selected entry verified and within effective limits. First/later failure returns FAILED/INCOMPLETE with artifacts=(), no partial payload exposure. Plan retains exact selection and complete_set true only for ALL. This is result atomicity, not a multi-file filesystem snapshot.
- **Expected Diagnostics:** Success requires every selected entry verified and within effective limits. First/later failure returns FAILED/INCOMPLETE with artifacts=(), no partial payload exposure. Plan retains exact selection and complete_set true only for ALL. This is result atomicity, not a multi-file filesystem snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadResult atomic exposed payloads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T090 — Missing file

- **Scenario:** Missing and Corrupted Files: Missing file.
- **Objective:** Establish the exact missing file behavior without broadening read scope, evidence or authority.
- **Component:** Filesystem availability / tampering / race checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled missing/unreadable/truncated/modified/replaced selected files, approved fixed root and directory handles.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot.
- **Expected Diagnostics:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Filesystem availability / tampering / race checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T091 — Unreadable file

- **Scenario:** Missing and Corrupted Files: Unreadable file.
- **Objective:** Establish the exact unreadable file behavior without broadening read scope, evidence or authority.
- **Component:** Filesystem availability / tampering / race checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled missing/unreadable/truncated/modified/replaced selected files, approved fixed root and directory handles.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot.
- **Expected Diagnostics:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Filesystem availability / tampering / race checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T092 — Truncated file

- **Scenario:** Missing and Corrupted Files: Truncated file.
- **Objective:** Establish the exact truncated file behavior without broadening read scope, evidence or authority.
- **Component:** Filesystem availability / tampering / race checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled missing/unreadable/truncated/modified/replaced selected files, approved fixed root and directory handles.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot.
- **Expected Diagnostics:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Filesystem availability / tampering / race checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T093 — Modified file

- **Scenario:** Missing and Corrupted Files: Modified file.
- **Objective:** Establish the exact modified file behavior without broadening read scope, evidence or authority.
- **Component:** Filesystem availability / tampering / race checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled missing/unreadable/truncated/modified/replaced selected files, approved fixed root and directory handles.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot.
- **Expected Diagnostics:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Filesystem availability / tampering / race checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T094 — Digest mismatch

- **Scenario:** Missing and Corrupted Files: Digest mismatch.
- **Objective:** Establish the exact digest mismatch behavior without broadening read scope, evidence or authority.
- **Component:** Filesystem availability / tampering / race checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled missing/unreadable/truncated/modified/replaced selected files, approved fixed root and directory handles.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot.
- **Expected Diagnostics:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Filesystem availability / tampering / race checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T095 — Concurrent modification

- **Scenario:** Missing and Corrupted Files: Concurrent modification.
- **Objective:** Establish the exact concurrent modification behavior without broadening read scope, evidence or authority.
- **Component:** Filesystem availability / tampering / race checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled missing/unreadable/truncated/modified/replaced selected files, approved fixed root and directory handles.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot.
- **Expected Diagnostics:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Filesystem availability / tampering / race checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T096 — No automatic repair

- **Scenario:** Missing and Corrupted Files: No automatic repair.
- **Objective:** Establish the exact no automatic repair behavior without broadening read scope, evidence or authority.
- **Component:** Filesystem availability / tampering / race checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled missing/unreadable/truncated/modified/replaced selected files, approved fixed root and directory handles.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot.
- **Expected Diagnostics:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Filesystem availability / tampering / race checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T097 — No recompilation

- **Scenario:** Missing and Corrupted Files: No recompilation.
- **Objective:** Establish the exact no recompilation behavior without broadening read scope, evidence or authority.
- **Component:** Filesystem availability / tampering / race checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled missing/unreadable/truncated/modified/replaced selected files, approved fixed root and directory handles.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot.
- **Expected Diagnostics:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Filesystem availability / tampering / race checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T098 — Immutable request

- **Scenario:** Immutability: Immutable request.
- **Objective:** Establish the exact immutable request behavior without broadening read scope, evidence or authority.
- **Component:** Frozen reader values / local state.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual dataclass requests/policy/selection/plan/retrieved verification/result and immutable byte content.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Input finite lists copied to tuples; actual types/ints/enums enforced; no mutable output/cache/global counter. Returned fields cannot be reassigned and bytes retain exact content. Any non-success result with payload or success with incomplete selected inventory rejects.
- **Expected Diagnostics:** Input finite lists copied to tuples; actual types/ints/enums enforced; no mutable output/cache/global counter. Returned fields cannot be reassigned and bytes retain exact content. Any non-success result with payload or success with incomplete selected inventory rejects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Frozen reader values / local state; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T099 — Immutable policy

- **Scenario:** Immutability: Immutable policy.
- **Objective:** Establish the exact immutable policy behavior without broadening read scope, evidence or authority.
- **Component:** Frozen reader values / local state.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual dataclass requests/policy/selection/plan/retrieved verification/result and immutable byte content.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Input finite lists copied to tuples; actual types/ints/enums enforced; no mutable output/cache/global counter. Returned fields cannot be reassigned and bytes retain exact content. Any non-success result with payload or success with incomplete selected inventory rejects.
- **Expected Diagnostics:** Input finite lists copied to tuples; actual types/ints/enums enforced; no mutable output/cache/global counter. Returned fields cannot be reassigned and bytes retain exact content. Any non-success result with payload or success with incomplete selected inventory rejects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Frozen reader values / local state; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T100 — Immutable RetrievedArtifact

- **Scenario:** Immutability: Immutable RetrievedArtifact.
- **Objective:** Establish the exact immutable retrievedartifact behavior without broadening read scope, evidence or authority.
- **Component:** Frozen reader values / local state.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual dataclass requests/policy/selection/plan/retrieved verification/result and immutable byte content.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Input finite lists copied to tuples; actual types/ints/enums enforced; no mutable output/cache/global counter. Returned fields cannot be reassigned and bytes retain exact content. Any non-success result with payload or success with incomplete selected inventory rejects.
- **Expected Diagnostics:** Input finite lists copied to tuples; actual types/ints/enums enforced; no mutable output/cache/global counter. Returned fields cannot be reassigned and bytes retain exact content. Any non-success result with payload or success with incomplete selected inventory rejects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Frozen reader values / local state; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T101 — Immutable result

- **Scenario:** Immutability: Immutable result.
- **Objective:** Establish the exact immutable result behavior without broadening read scope, evidence or authority.
- **Component:** Frozen reader values / local state.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual dataclass requests/policy/selection/plan/retrieved verification/result and immutable byte content.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Input finite lists copied to tuples; actual types/ints/enums enforced; no mutable output/cache/global counter. Returned fields cannot be reassigned and bytes retain exact content. Any non-success result with payload or success with incomplete selected inventory rejects.
- **Expected Diagnostics:** Input finite lists copied to tuples; actual types/ints/enums enforced; no mutable output/cache/global counter. Returned fields cannot be reassigned and bytes retain exact content. Any non-success result with payload or success with incomplete selected inventory rejects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Frozen reader values / local state; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T102 — Exact bytes retained

- **Scenario:** Immutability: Exact bytes retained.
- **Objective:** Establish the exact exact bytes retained behavior without broadening read scope, evidence or authority.
- **Component:** Frozen reader values / local state.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual dataclass requests/policy/selection/plan/retrieved verification/result and immutable byte content.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Input finite lists copied to tuples; actual types/ints/enums enforced; no mutable output/cache/global counter. Returned fields cannot be reassigned and bytes retain exact content. Any non-success result with payload or success with incomplete selected inventory rejects.
- **Expected Diagnostics:** Input finite lists copied to tuples; actual types/ints/enums enforced; no mutable output/cache/global counter. Returned fields cannot be reassigned and bytes retain exact content. Any non-success result with payload or success with incomplete selected inventory rejects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Frozen reader values / local state; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T103 — No mutable global cache

- **Scenario:** Immutability: No mutable global cache.
- **Objective:** Establish the exact no mutable global cache behavior without broadening read scope, evidence or authority.
- **Component:** Frozen reader values / local state.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual dataclass requests/policy/selection/plan/retrieved verification/result and immutable byte content.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Input finite lists copied to tuples; actual types/ints/enums enforced; no mutable output/cache/global counter. Returned fields cannot be reassigned and bytes retain exact content. Any non-success result with payload or success with incomplete selected inventory rejects.
- **Expected Diagnostics:** Input finite lists copied to tuples; actual types/ints/enums enforced; no mutable output/cache/global counter. Returned fields cannot be reassigned and bytes retain exact content. Any non-success result with payload or success with incomplete selected inventory rejects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Frozen reader values / local state; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T104 — Invalid request

- **Scenario:** Diagnostics: Invalid request.
- **Objective:** Establish the exact invalid request behavior without broadening read scope, evidence or authority.
- **Component:** CMP-02 read diagnostic associations.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Stable existing CompilationFailure family extended CMP-062..080; RESULT origin, typed read stage/source type and existing artifact/manifest/context/relative location.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success.
- **Expected Diagnostics:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** CMP-02 read diagnostic associations; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T105 — Manifest mismatch

- **Scenario:** Diagnostics: Manifest mismatch.
- **Objective:** Establish the exact manifest mismatch behavior without broadening read scope, evidence or authority.
- **Component:** CMP-02 read diagnostic associations.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Stable existing CompilationFailure family extended CMP-062..080; RESULT origin, typed read stage/source type and existing artifact/manifest/context/relative location.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success.
- **Expected Diagnostics:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** CMP-02 read diagnostic associations; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T106 — Receipt mismatch

- **Scenario:** Diagnostics: Receipt mismatch.
- **Objective:** Establish the exact receipt mismatch behavior without broadening read scope, evidence or authority.
- **Component:** CMP-02 read diagnostic associations.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Stable existing CompilationFailure family extended CMP-062..080; RESULT origin, typed read stage/source type and existing artifact/manifest/context/relative location.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success.
- **Expected Diagnostics:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** CMP-02 read diagnostic associations; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T107 — Unsafe path

- **Scenario:** Diagnostics: Unsafe path.
- **Objective:** Establish the exact unsafe path behavior without broadening read scope, evidence or authority.
- **Component:** CMP-02 read diagnostic associations.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Stable existing CompilationFailure family extended CMP-062..080; RESULT origin, typed read stage/source type and existing artifact/manifest/context/relative location.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success.
- **Expected Diagnostics:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** CMP-02 read diagnostic associations; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T108 — Unsupported file type

- **Scenario:** Diagnostics: Unsupported file type.
- **Objective:** Establish the exact unsupported file type behavior without broadening read scope, evidence or authority.
- **Component:** CMP-02 read diagnostic associations.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Stable existing CompilationFailure family extended CMP-062..080; RESULT origin, typed read stage/source type and existing artifact/manifest/context/relative location.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success.
- **Expected Diagnostics:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** CMP-02 read diagnostic associations; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T109 — Missing file

- **Scenario:** Diagnostics: Missing file.
- **Objective:** Establish the exact missing file behavior without broadening read scope, evidence or authority.
- **Component:** CMP-02 read diagnostic associations.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Stable existing CompilationFailure family extended CMP-062..080; RESULT origin, typed read stage/source type and existing artifact/manifest/context/relative location.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success.
- **Expected Diagnostics:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** CMP-02 read diagnostic associations; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T110 — Access denied

- **Scenario:** Diagnostics: Access denied.
- **Objective:** Establish the exact access denied behavior without broadening read scope, evidence or authority.
- **Component:** CMP-02 read diagnostic associations.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Stable existing CompilationFailure family extended CMP-062..080; RESULT origin, typed read stage/source type and existing artifact/manifest/context/relative location.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success.
- **Expected Diagnostics:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** CMP-02 read diagnostic associations; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T111 — Size limit

- **Scenario:** Diagnostics: Size limit.
- **Objective:** Establish the exact size limit behavior without broadening read scope, evidence or authority.
- **Component:** CMP-02 read diagnostic associations.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Stable existing CompilationFailure family extended CMP-062..080; RESULT origin, typed read stage/source type and existing artifact/manifest/context/relative location.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success.
- **Expected Diagnostics:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** CMP-02 read diagnostic associations; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T112 — Size mismatch

- **Scenario:** Diagnostics: Size mismatch.
- **Objective:** Establish the exact size mismatch behavior without broadening read scope, evidence or authority.
- **Component:** CMP-02 read diagnostic associations.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Stable existing CompilationFailure family extended CMP-062..080; RESULT origin, typed read stage/source type and existing artifact/manifest/context/relative location.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success.
- **Expected Diagnostics:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** CMP-02 read diagnostic associations; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T113 — Digest mismatch

- **Scenario:** Diagnostics: Digest mismatch.
- **Objective:** Establish the exact digest mismatch behavior without broadening read scope, evidence or authority.
- **Component:** CMP-02 read diagnostic associations.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Stable existing CompilationFailure family extended CMP-062..080; RESULT origin, typed read stage/source type and existing artifact/manifest/context/relative location.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success.
- **Expected Diagnostics:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** CMP-02 read diagnostic associations; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T114 — I/O failure

- **Scenario:** Diagnostics: I/O failure.
- **Objective:** Establish the exact i/o failure behavior without broadening read scope, evidence or authority.
- **Component:** CMP-02 read diagnostic associations.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Stable existing CompilationFailure family extended CMP-062..080; RESULT origin, typed read stage/source type and existing artifact/manifest/context/relative location.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success.
- **Expected Diagnostics:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** CMP-02 read diagnostic associations; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T115 — CMP-02 integration

- **Scenario:** Diagnostics: CMP-02 integration.
- **Objective:** Establish the exact cmp-02 integration behavior without broadening read scope, evidence or authority.
- **Component:** CMP-02 read diagnostic associations.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Stable existing CompilationFailure family extended CMP-062..080; RESULT origin, typed read stage/source type and existing artifact/manifest/context/relative location.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success.
- **Expected Diagnostics:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** CMP-02 read diagnostic associations; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T116 — Pure Python domain

- **Scenario:** Django / DRF: Pure Python domain.
- **Objective:** Establish the exact pure python domain behavior without broadening read scope, evidence or authority.
- **Component:** Framework / trusted application boundary.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Django/DRF selected but not installed; no existing compilation HTTP API; neutral compiler imports no filesystem/framework.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization.
- **Expected Diagnostics:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Framework / trusted application boundary; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T117 — Infrastructure-isolated filesystem access

- **Scenario:** Django / DRF: Infrastructure-isolated filesystem access.
- **Objective:** Establish the exact infrastructure-isolated filesystem access behavior without broadening read scope, evidence or authority.
- **Component:** Framework / trusted application boundary.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Django/DRF selected but not installed; no existing compilation HTTP API; neutral compiler imports no filesystem/framework.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization.
- **Expected Diagnostics:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Framework / trusted application boundary; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T118 — No ORM models

- **Scenario:** Django / DRF: No ORM models.
- **Objective:** Establish the exact no orm models behavior without broadening read scope, evidence or authority.
- **Component:** Framework / trusted application boundary.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Django/DRF selected but not installed; no existing compilation HTTP API; neutral compiler imports no filesystem/framework.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization.
- **Expected Diagnostics:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Framework / trusted application boundary; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T119 — No migrations

- **Scenario:** Django / DRF: No migrations.
- **Objective:** Establish the exact no migrations behavior without broadening read scope, evidence or authority.
- **Component:** Framework / trusted application boundary.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Django/DRF selected but not installed; no existing compilation HTTP API; neutral compiler imports no filesystem/framework.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization.
- **Expected Diagnostics:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Framework / trusted application boundary; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T120 — Existing API authorization

- **Scenario:** Django / DRF: Existing API authorization.
- **Objective:** Establish the exact existing api authorization behavior without broadening read scope, evidence or authority.
- **Component:** Framework / trusted application boundary.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Django/DRF selected but not installed; no existing compilation HTTP API; neutral compiler imports no filesystem/framework.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization.
- **Expected Diagnostics:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Framework / trusted application boundary; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T121 — No arbitrary file-read endpoint

- **Scenario:** Django / DRF: No arbitrary file-read endpoint.
- **Objective:** Establish the exact no arbitrary file-read endpoint behavior without broadening read scope, evidence or authority.
- **Component:** Framework / trusted application boundary.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Django/DRF selected but not installed; no existing compilation HTTP API; neutral compiler imports no filesystem/framework.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization.
- **Expected Diagnostics:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Framework / trusted application boundary; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T122 — No absolute path disclosure

- **Scenario:** Django / DRF: No absolute path disclosure.
- **Objective:** Establish the exact no absolute path disclosure behavior without broadening read scope, evidence or authority.
- **Component:** Framework / trusted application boundary.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Django/DRF selected but not installed; no existing compilation HTTP API; neutral compiler imports no filesystem/framework.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization.
- **Expected Diagnostics:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Framework / trusted application boundary; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T123 — Customer artifact retrieval

- **Scenario:** Mini Sales: Customer artifact retrieval.
- **Objective:** Establish the exact customer artifact retrieval behavior without broadening read scope, evidence or authority.
- **Component:** Conceptual Mini Sales writer/reader compatibility.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual Customer sem_...000000000001@1.0.0 and Employee sem_...000000000002@1.0.0, future genuine producer, successful original CMP-07 and CMP-08 receipt; no current producer exists.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success.
- **Expected Diagnostics:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Conceptual Mini Sales writer/reader compatibility; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T124 — Employee artifact retrieval

- **Scenario:** Mini Sales: Employee artifact retrieval.
- **Objective:** Establish the exact employee artifact retrieval behavior without broadening read scope, evidence or authority.
- **Component:** Conceptual Mini Sales writer/reader compatibility.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual Customer sem_...000000000001@1.0.0 and Employee sem_...000000000002@1.0.0, future genuine producer, successful original CMP-07 and CMP-08 receipt; no current producer exists.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success.
- **Expected Diagnostics:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Conceptual Mini Sales writer/reader compatibility; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T125 — Matching manifest/receipt

- **Scenario:** Mini Sales: Matching manifest/receipt.
- **Objective:** Establish the exact matching manifest/receipt behavior without broadening read scope, evidence or authority.
- **Component:** Conceptual Mini Sales writer/reader compatibility.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual Customer sem_...000000000001@1.0.0 and Employee sem_...000000000002@1.0.0, future genuine producer, successful original CMP-07 and CMP-08 receipt; no current producer exists.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success.
- **Expected Diagnostics:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Conceptual Mini Sales writer/reader compatibility; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T126 — Missing Customer file

- **Scenario:** Mini Sales: Missing Customer file.
- **Objective:** Establish the exact missing customer file behavior without broadening read scope, evidence or authority.
- **Component:** Conceptual Mini Sales writer/reader compatibility.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual Customer sem_...000000000001@1.0.0 and Employee sem_...000000000002@1.0.0, future genuine producer, successful original CMP-07 and CMP-08 receipt; no current producer exists.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success.
- **Expected Diagnostics:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Conceptual Mini Sales writer/reader compatibility; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T127 — Corrupted Employee bytes

- **Scenario:** Mini Sales: Corrupted Employee bytes.
- **Objective:** Establish the exact corrupted employee bytes behavior without broadening read scope, evidence or authority.
- **Component:** Conceptual Mini Sales writer/reader compatibility.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual Customer sem_...000000000001@1.0.0 and Employee sem_...000000000002@1.0.0, future genuine producer, successful original CMP-07 and CMP-08 receipt; no current producer exists.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success.
- **Expected Diagnostics:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Conceptual Mini Sales writer/reader compatibility; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T128 — Unknown artifact identity

- **Scenario:** Mini Sales: Unknown artifact identity.
- **Objective:** Establish the exact unknown artifact identity behavior without broadening read scope, evidence or authority.
- **Component:** Conceptual Mini Sales writer/reader compatibility.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual Customer sem_...000000000001@1.0.0 and Employee sem_...000000000002@1.0.0, future genuine producer, successful original CMP-07 and CMP-08 receipt; no current producer exists.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success.
- **Expected Diagnostics:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Conceptual Mini Sales writer/reader compatibility; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T129 — Unsafe receipt location

- **Scenario:** Mini Sales: Unsafe receipt location.
- **Objective:** Establish the exact unsafe receipt location behavior without broadening read scope, evidence or authority.
- **Component:** Conceptual Mini Sales writer/reader compatibility.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual Customer sem_...000000000001@1.0.0 and Employee sem_...000000000002@1.0.0, future genuine producer, successful original CMP-07 and CMP-08 receipt; no current producer exists.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success.
- **Expected Diagnostics:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Conceptual Mini Sales writer/reader compatibility; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T130 — Failed complete-set read

- **Scenario:** Mini Sales: Failed complete-set read.
- **Objective:** Establish the exact failed complete-set read behavior without broadening read scope, evidence or authority.
- **Component:** Conceptual Mini Sales writer/reader compatibility.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual Customer sem_...000000000001@1.0.0 and Employee sem_...000000000002@1.0.0, future genuine producer, successful original CMP-07 and CMP-08 receipt; no current producer exists.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success.
- **Expected Diagnostics:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Conceptual Mini Sales writer/reader compatibility; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T131 — Successful Customer-only read

- **Scenario:** Mini Sales: Successful Customer-only read.
- **Objective:** Establish the exact successful customer-only read behavior without broadening read scope, evidence or authority.
- **Component:** Conceptual Mini Sales writer/reader compatibility.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual Customer sem_...000000000001@1.0.0 and Employee sem_...000000000002@1.0.0, future genuine producer, successful original CMP-07 and CMP-08 receipt; no current producer exists.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success.
- **Expected Diagnostics:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Conceptual Mini Sales writer/reader compatibility; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T132 — No Type IR-as-runtime-artifact substitution

- **Scenario:** Mini Sales: No Type IR-as-runtime-artifact substitution.
- **Objective:** Establish the exact no type ir-as-runtime-artifact substitution behavior without broadening read scope, evidence or authority.
- **Component:** Conceptual Mini Sales writer/reader compatibility.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual Customer sem_...000000000001@1.0.0 and Employee sem_...000000000002@1.0.0, future genuine producer, successful original CMP-07 and CMP-08 receipt; no current producer exists.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success.
- **Expected Diagnostics:** Original committed Customer/Employee bytes read by receipt locations. Missing Customer CMP-070; corrupted Employee with digest CMP-074; unknown ID CMP-065; unsafe location CMP-068/050 before access; Employee failure exposes no Customer partial result. Customer-only success stays selected scope. Current IR-only build cannot fabricate materialization/read success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Conceptual Mini Sales writer/reader compatibility; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T133 — No parsing

- **Scenario:** Architectural Boundaries: No parsing.
- **Objective:** Establish the exact no parsing behavior without broadening read scope, evidence or authority.
- **Component:** Architectural / read-only source inspection.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual source boundaries, original model/compiler/writer/runtime contracts and deferred policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof.
- **Expected Diagnostics:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Architectural / read-only source inspection; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T134 — No name resolution

- **Scenario:** Architectural Boundaries: No name resolution.
- **Objective:** Establish the exact no name resolution behavior without broadening read scope, evidence or authority.
- **Component:** Architectural / read-only source inspection.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual source boundaries, original model/compiler/writer/runtime contracts and deferred policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof.
- **Expected Diagnostics:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Architectural / read-only source inspection; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T135 — No canonicalization

- **Scenario:** Architectural Boundaries: No canonicalization.
- **Objective:** Establish the exact no canonicalization behavior without broadening read scope, evidence or authority.
- **Component:** Architectural / read-only source inspection.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual source boundaries, original model/compiler/writer/runtime contracts and deferred policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof.
- **Expected Diagnostics:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Architectural / read-only source inspection; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T136 — No semantic validation

- **Scenario:** Architectural Boundaries: No semantic validation.
- **Objective:** Establish the exact no semantic validation behavior without broadening read scope, evidence or authority.
- **Component:** Architectural / read-only source inspection.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual source boundaries, original model/compiler/writer/runtime contracts and deferred policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof.
- **Expected Diagnostics:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Architectural / read-only source inspection; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T137 — No type lowering

- **Scenario:** Architectural Boundaries: No type lowering.
- **Objective:** Establish the exact no type lowering behavior without broadening read scope, evidence or authority.
- **Component:** Architectural / read-only source inspection.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual source boundaries, original model/compiler/writer/runtime contracts and deferred policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof.
- **Expected Diagnostics:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Architectural / read-only source inspection; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T138 — No artifact generation

- **Scenario:** Architectural Boundaries: No artifact generation.
- **Objective:** Establish the exact no artifact generation behavior without broadening read scope, evidence or authority.
- **Component:** Architectural / read-only source inspection.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual source boundaries, original model/compiler/writer/runtime contracts and deferred policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof.
- **Expected Diagnostics:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Architectural / read-only source inspection; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T139 — No artifact writing

- **Scenario:** Architectural Boundaries: No artifact writing.
- **Objective:** Establish the exact no artifact writing behavior without broadening read scope, evidence or authority.
- **Component:** Architectural / read-only source inspection.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual source boundaries, original model/compiler/writer/runtime contracts and deferred policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof.
- **Expected Diagnostics:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Architectural / read-only source inspection; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T140 — No artifact publication

- **Scenario:** Architectural Boundaries: No artifact publication.
- **Objective:** Establish the exact no artifact publication behavior without broadening read scope, evidence or authority.
- **Component:** Architectural / read-only source inspection.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual source boundaries, original model/compiler/writer/runtime contracts and deferred policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof.
- **Expected Diagnostics:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Architectural / read-only source inspection; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T141 — No runtime loading

- **Scenario:** Architectural Boundaries: No runtime loading.
- **Objective:** Establish the exact no runtime loading behavior without broadening read scope, evidence or authority.
- **Component:** Architectural / read-only source inspection.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual source boundaries, original model/compiler/writer/runtime contracts and deferred policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof.
- **Expected Diagnostics:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Architectural / read-only source inspection; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T142 — No execution

- **Scenario:** Architectural Boundaries: No execution.
- **Objective:** Establish the exact no execution behavior without broadening read scope, evidence or authority.
- **Component:** Architectural / read-only source inspection.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual source boundaries, original model/compiler/writer/runtime contracts and deferred policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof.
- **Expected Diagnostics:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Architectural / read-only source inspection; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T143 — No cloud storage

- **Scenario:** Architectural Boundaries: No cloud storage.
- **Objective:** Establish the exact no cloud storage behavior without broadening read scope, evidence or authority.
- **Component:** Architectural / read-only source inspection.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual source boundaries, original model/compiler/writer/runtime contracts and deferred policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof.
- **Expected Diagnostics:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Architectural / read-only source inspection; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T144 — Same manifest ID from another invocation is rejected

- **Scenario:** Receipt Prerequisites: Same manifest ID from another invocation is rejected.
- **Objective:** Establish the exact same manifest id from another invocation is rejected behavior without broadening read scope, evidence or authority.
- **Component:** Receipt consistency preflight.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual CMP-08 ArtifactMaterializationReceipt with exact declaration and same original compilation_association object, full ordered descriptors, distinct safe locations and source destination.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists.
- **Expected Diagnostics:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt consistency preflight; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T145 — Equivalent manifest object must share original association

- **Scenario:** Receipt Prerequisites: Equivalent manifest object must share original association.
- **Objective:** Establish the exact equivalent manifest object must share original association behavior without broadening read scope, evidence or authority.
- **Component:** Receipt consistency preflight.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual CMP-08 ArtifactMaterializationReceipt with exact declaration and same original compilation_association object, full ordered descriptors, distinct safe locations and source destination.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists.
- **Expected Diagnostics:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt consistency preflight; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T146 — All receipt locations validated before subset access

- **Scenario:** Receipt Prerequisites: All receipt locations validated before subset access.
- **Objective:** Establish the exact all receipt locations validated before subset access behavior without broadening read scope, evidence or authority.
- **Component:** Receipt consistency preflight.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual CMP-08 ArtifactMaterializationReceipt with exact declaration and same original compilation_association object, full ordered descriptors, distinct safe locations and source destination.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists.
- **Expected Diagnostics:** Identity/schema/scope/target/membership/kind/association/destination mismatch, missing/extra/duplicate entry CMP-064 before access. Missing receipt fails closed. Every receipt entry is validated even for subset reads; no alternate locator contract exists. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt consistency preflight; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T147 — Explicit set containing all keys retains explicit-set mode

- **Scenario:** Artifact Selection: Explicit set containing all keys retains explicit-set mode.
- **Objective:** Establish the exact explicit set containing all keys retains explicit-set mode behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadSelection / selected plan.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; ONE with exactly one key, nonempty distinct explicit SET or ALL with no overrides; keys are existing CompilationArtifactKey values.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope.
- **Expected Diagnostics:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadSelection / selected plan; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T148 — Selection order reversed from manifest order

- **Scenario:** Artifact Selection: Selection order reversed from manifest order.
- **Objective:** Establish the exact selection order reversed from manifest order behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadSelection / selected plan.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; ONE with exactly one key, nonempty distinct explicit SET or ALL with no overrides; keys are existing CompilationArtifactKey values.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope.
- **Expected Diagnostics:** Unknown key CMP-065; duplicate/empty/wrong-mode keys CMP-066. Results follow manifest order regardless of input key order. Only requested keys are read, no dependency closure, filename or QName fallback. ALL-only complete_set marker preserves scope. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadSelection / selected plan; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T149 — Caller cannot raise server maximum

- **Scenario:** Resource Bounds: Caller cannot raise server maximum.
- **Objective:** Establish the exact caller cannot raise server maximum behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPolicy / effective bounded plan / chunk reads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Caller and trusted server policy; defaults 32 MiB/artifact, 128 MiB aggregate, 128 artifacts; positive actual ints and size/digest enum.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails.
- **Expected Diagnostics:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPolicy / effective bounded plan / chunk reads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T150 — Server mandatory digest cannot be downgraded

- **Scenario:** Resource Bounds: Server mandatory digest cannot be downgraded.
- **Objective:** Establish the exact server mandatory digest cannot be downgraded behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPolicy / effective bounded plan / chunk reads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Caller and trusted server policy; defaults 32 MiB/artifact, 128 MiB aggregate, 128 artifacts; positive actual ints and size/digest enum.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails.
- **Expected Diagnostics:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPolicy / effective bounded plan / chunk reads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T151 — Boolean and float read limits rejected

- **Scenario:** Resource Bounds: Boolean and float read limits rejected.
- **Objective:** Establish the exact boolean and float read limits rejected behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPolicy / effective bounded plan / chunk reads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Caller and trusted server policy; defaults 32 MiB/artifact, 128 MiB aggregate, 128 artifacts; positive actual ints and size/digest enum.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails.
- **Expected Diagnostics:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPolicy / effective bounded plan / chunk reads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T152 — File growth is stopped by one-byte probe

- **Scenario:** Resource Bounds: File growth is stopped by one-byte probe.
- **Objective:** Establish the exact file growth is stopped by one-byte probe behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPolicy / effective bounded plan / chunk reads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Caller and trusted server policy; defaults 32 MiB/artifact, 128 MiB aggregate, 128 artifacts; positive actual ints and size/digest enum.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails.
- **Expected Diagnostics:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPolicy / effective bounded plan / chunk reads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T153 — Aggregate exact boundary and plus-one byte

- **Scenario:** Resource Bounds: Aggregate exact boundary and plus-one byte.
- **Objective:** Establish the exact aggregate exact boundary and plus-one byte behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPolicy / effective bounded plan / chunk reads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Caller and trusted server policy; defaults 32 MiB/artifact, 128 MiB aggregate, 128 artifacts; positive actual ints and size/digest enum.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails.
- **Expected Diagnostics:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPolicy / effective bounded plan / chunk reads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T154 — Regular-file-to-FIFO replacement race

- **Scenario:** File-Type Security: Regular-file-to-FIFO replacement race.
- **Objective:** Establish the exact regular-file-to-fifo replacement race behavior without broadening read scope, evidence or authority.
- **Component:** Opened file-type and identity checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled future Linux local fixtures, lstat before open, O_RDONLY|O_NOFOLLOW|O_NONBLOCK|O_NOATIME handles and fstat.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects.
- **Expected Diagnostics:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Opened file-type and identity checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T155 — Single-link and write-permission restrictions

- **Scenario:** File-Type Security: Single-link and write-permission restrictions.
- **Objective:** Establish the exact single-link and write-permission restrictions behavior without broadening read scope, evidence or authority.
- **Component:** Opened file-type and identity checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled future Linux local fixtures, lstat before open, O_RDONLY|O_NOFOLLOW|O_NONBLOCK|O_NOATIME handles and fstat.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects.
- **Expected Diagnostics:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Opened file-type and identity checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T156 — O_NOATIME capability unavailable

- **Scenario:** File-Type Security: O_NOATIME capability unavailable.
- **Objective:** Establish the exact o_noatime capability unavailable behavior without broadening read scope, evidence or authority.
- **Component:** Opened file-type and identity checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled future Linux local fixtures, lstat before open, O_RDONLY|O_NOFOLLOW|O_NONBLOCK|O_NOATIME handles and fstat.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Required Linux file-open flags unavailable gives CMP-067 INCOMPLETE before access; inability to apply authorized file open gives access/I/O failure, no silent less-safe fallback.
- **Expected Diagnostics:** Only regular single-link writer-owned non-group/world-writable files accepted. Symlinks CMP-068; directories/FIFO/socket/device/special/hardlink CMP-069; unsafe ownership CMP-071. NONBLOCK prevents FIFO replacement race from hanging; opened type always rechecked. No bytes returned from unsafe objects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Opened file-type and identity checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T157 — Path replaced after descriptor open

- **Scenario:** Missing and Corrupted Files: Path replaced after descriptor open.
- **Objective:** Establish the exact path replaced after descriptor open behavior without broadening read scope, evidence or authority.
- **Component:** Filesystem availability / tampering / race checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled missing/unreadable/truncated/modified/replaced selected files, approved fixed root and directory handles.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot.
- **Expected Diagnostics:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Filesystem availability / tampering / race checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T158 — Output directory renamed during retrieval

- **Scenario:** Missing and Corrupted Files: Output directory renamed during retrieval.
- **Objective:** Establish the exact output directory renamed during retrieval behavior without broadening read scope, evidence or authority.
- **Component:** Filesystem availability / tampering / race checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled missing/unreadable/truncated/modified/replaced selected files, approved fixed root and directory handles.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot.
- **Expected Diagnostics:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Filesystem availability / tampering / race checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T159 — Same-size corruption under size-only policy

- **Scenario:** Missing and Corrupted Files: Same-size corruption under size-only policy.
- **Objective:** Establish the exact same-size corruption under size-only policy behavior without broadening read scope, evidence or authority.
- **Component:** Filesystem availability / tampering / race checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled missing/unreadable/truncated/modified/replaced selected files, approved fixed root and directory handles.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot.
- **Expected Diagnostics:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Filesystem availability / tampering / race checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T160 — First file changes after its read while second reads

- **Scenario:** Missing and Corrupted Files: First file changes after its read while second reads.
- **Objective:** Establish the exact first file changes after its read while second reads behavior without broadening read scope, evidence or authority.
- **Component:** Filesystem availability / tampering / race checks.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Controlled missing/unreadable/truncated/modified/replaced selected files, approved fixed root and directory handles.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Reader guarantees selected-result atomicity and individual verification only; it does not detect every post-read change or certify a cross-file snapshot. Document the limit without overstating success.
- **Expected Diagnostics:** Missing CMP-070, access CMP-071, size CMP-073, digest CMP-074, metadata/path-binding change CMP-078, other OS I/O CMP-076. No repair/search/recompile/delete. Per-file before/after metadata and name binding plus output-directory identity detect obvious races, not every mutation or a transactional snapshot. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Filesystem availability / tampering / race checks; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T161 — File close failure after verification

- **Scenario:** Diagnostics: File close failure after verification.
- **Objective:** Establish the exact file close failure after verification behavior without broadening read scope, evidence or authority.
- **Component:** CMP-02 read diagnostic associations.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Stable existing CompilationFailure family extended CMP-062..080; RESULT origin, typed read stage/source type and existing artifact/manifest/context/relative location.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success.
- **Expected Diagnostics:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** CMP-02 read diagnostic associations; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T162 — Source close failure after all reads

- **Scenario:** Diagnostics: Source close failure after all reads.
- **Objective:** Establish the exact source close failure after all reads behavior without broadening read scope, evidence or authority.
- **Component:** CMP-02 read diagnostic associations.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Stable existing CompilationFailure family extended CMP-062..080; RESULT origin, typed read stage/source type and existing artifact/manifest/context/relative location.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success.
- **Expected Diagnostics:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** CMP-02 read diagnostic associations; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T163 — Primary read error plus close error retained

- **Scenario:** Diagnostics: Primary read error plus close error retained.
- **Objective:** Establish the exact primary read error plus close error retained behavior without broadening read scope, evidence or authority.
- **Component:** CMP-02 read diagnostic associations.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Stable existing CompilationFailure family extended CMP-062..080; RESULT origin, typed read stage/source type and existing artifact/manifest/context/relative location.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success.
- **Expected Diagnostics:** Preserve bounded category and actual source/stage/artifact/path association. Never absolute roots/raw OS errors/stack traces or semantic-validation blame. CMP-06 comparison includes read stage/source; existing model projection unchanged, raw diagnostic contains full association. Close failure retains primary diagnostics and blocks success. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** CMP-02 read diagnostic associations; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T164 — Unrelated directory files are not enumerated

- **Scenario:** Deterministic Ordering: Unrelated directory files are not enumerated.
- **Objective:** Establish the exact unrelated directory files are not enumerated behavior without broadening read scope, evidence or authority.
- **Component:** Manifest-order sequential plan / diagnostics.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Identical accepted manifest/receipt/source/policy and unchanged bytes/filesystem state; input selections can be reversed.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Extra unrelated files are neither read nor deleted; even ALL success verifies declared membership only, never current directory exclusivity.
- **Expected Diagnostics:** Sequential reads and returned selected keys follow existing manifest key order, no directory enumeration/path/time/object-ID/concurrency order. First selected failure deterministic; diagnostics preserve actual stage/location/artifact/manifest. No repeat-read behavior is executed now. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Manifest-order sequential plan / diagnostics; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T165 — Available digest verified even with size-only requirement

- **Scenario:** Digest Verification: Available digest verified even with size-only requirement.
- **Objective:** Establish the exact available digest verified even with size-only requirement behavior without broadening read scope, evidence or authority.
- **Component:** Receipt digest / actual verification.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactContentDigest explicit sha256/lowercase 64-hex, receipt.verified_digest, policy SIZE_VERIFIED or DIGEST_VERIFIED.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim.
- **Expected Diagnostics:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt digest / actual verification; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T166 — Unsupported digest on unselected receipt entry

- **Scenario:** Digest Verification: Unsupported digest on unselected receipt entry.
- **Objective:** Establish the exact unsupported digest on unselected receipt entry behavior without broadening read scope, evidence or authority.
- **Component:** Receipt digest / actual verification.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactContentDigest explicit sha256/lowercase 64-hex, receipt.verified_digest, policy SIZE_VERIFIED or DIGEST_VERIFIED.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim.
- **Expected Diagnostics:** Every available digest verified, including SIZE policy. Mismatch CMP-074; missing mandatory selected digest CMP-075 INCOMPLETE before access; malformed/unsupported receipt digest CMP-079 INCOMPLETE (constructor also rejects unsupported declaration). No algorithm inference/fabrication/signature/authenticity claim. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt digest / actual verification; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T167 — Previously accepted compiler configuration later changes

- **Scenario:** Manifest Prerequisites: Previously accepted compiler configuration later changes.
- **Objective:** Establish the exact previously accepted compiler configuration later changes behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPlanner manifest gate.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Original complete V0 manifest, bound canonical/VALID-READY evidence, context/target/output_origin and completed final artifact outcomes.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Read uses captured accepted manifest/receipt association; it does not rerun compilation or require current compiler configuration equivalence. Original declaration/evidence binding remains mandatory.
- **Expected Diagnostics:** Revalidate existing manifest structure/input/output association before filesystem access. Invalid/missing declaration CMP-063, retain existing CMP-07 causes. Unknown selected key CMP-065. Never reconstruct a manifest from disk or treat IR as final artifacts. Live compiler configuration is not rerun/audited as a new compilation. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPlanner manifest gate; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T168 — Read deployment uses same trusted UID root model

- **Scenario:** Django / DRF: Read deployment uses same trusted UID root model.
- **Objective:** Establish the exact read deployment uses same trusted uid root model behavior without broadening read scope, evidence or authority.
- **Component:** Framework / trusted application boundary.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Django/DRF selected but not installed; no existing compilation HTTP API; neutral compiler imports no filesystem/framework.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization.
- **Expected Diagnostics:** Read-only infrastructure remains in tooling-owned artifact-writer module with existing compiler public edge. No ORM/migration/API/public arbitrary read endpoint or authentication changes. Trusted server root config/limits, no root from query/user ID possession. Future applicable API must preserve authorization. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Framework / trusted application boundary; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T169 — No manual reader/writer experiments during this task

- **Scenario:** Architectural Boundaries: No manual reader/writer experiments during this task.
- **Objective:** Establish the exact no manual reader/writer experiments during this task behavior without broadening read scope, evidence or authority.
- **Component:** Architectural / read-only source inspection.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual source boundaries, original model/compiler/writer/runtime contracts and deferred policy.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof.
- **Expected Diagnostics:** Reader never parses/models/resolves/validates/lowers/generates/writes/repairs/publishes/activates/loads/executes/cloud-fetches. Reuse receipt/root/location/digest contracts, no competing hierarchy/new permission engine or runtime dependency. Static checks are not deferred test proof. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Architectural / read-only source inspection; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T170 — Result exposes no partial bytes after later failure

- **Scenario:** Immutability: Result exposes no partial bytes after later failure.
- **Objective:** Establish the exact result exposes no partial bytes after later failure behavior without broadening read scope, evidence or authority.
- **Component:** Frozen reader values / local state.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual dataclass requests/policy/selection/plan/retrieved verification/result and immutable byte content.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Input finite lists copied to tuples; actual types/ints/enums enforced; no mutable output/cache/global counter. Returned fields cannot be reassigned and bytes retain exact content. Any non-success result with payload or success with incomplete selected inventory rejects.
- **Expected Diagnostics:** Input finite lists copied to tuples; actual types/ints/enums enforced; no mutable output/cache/global counter. Returned fields cannot be reassigned and bytes retain exact content. Any non-success result with payload or success with incomplete selected inventory rejects. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Frozen reader values / local state; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T171 — No fresh digest when receipt has none

- **Scenario:** Read Integrity: No fresh digest when receipt has none.
- **Objective:** Establish the exact no fresh digest when receipt has none behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadVerification evidence.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Actual immutable retrieved bytes with length checks and optional reverified receipt digest.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Evidence reports SIZE_VERIFIED only without digest and DIGEST_VERIFIED only after declared digest matched retrieved bytes. Expected/actual lengths match. Receipt historical verification does not replace current checking; identity/location alone is insufficient success under v0.
- **Expected Diagnostics:** Evidence reports SIZE_VERIFIED only without digest and DIGEST_VERIFIED only after declared digest matched retrieved bytes. Expected/actual lengths match. Receipt historical verification does not replace current checking; identity/location alone is insufficient success under v0. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadVerification evidence; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T172 — Maximum and reserved flat filename boundaries

- **Scenario:** Path Safety: Maximum and reserved flat filename boundaries.
- **Objective:** Establish the exact maximum and reserved flat filename boundaries behavior without broadening read scope, evidence or authority.
- **Component:** Receipt locator / Linux fd containment.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Existing ArtifactRelativeLocation flat lowercase portable ASCII grammar, server root/output tokens and trusted ApprovedLocalArtifactRoot.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened.
- **Expected Diagnostics:** Receipt paths revalidated before open: unsafe CMP-068, underlying path value constructor CMP-050. Root/output/file symlink or unsafe ancestry fails safely CMP-068/071; no resolve+open/string-prefix containment. Only no-follow handle-relative known names are opened. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** Receipt locator / Linux fd containment; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

## CMP-09-T173 — Bounded transient memory conversion overhead

- **Scenario:** Resource Bounds: Bounded transient memory conversion overhead.
- **Objective:** Establish the exact bounded transient memory conversion overhead behavior without broadening read scope, evidence or authority.
- **Component:** ArtifactReadPolicy / effective bounded plan / chunk reads.
- **Prerequisites:** Explicit later verification authorization and fixed source revision; Caller and trusted server policy; defaults 32 MiB/artifact, 128 MiB aggregate, 128 artifacts; positive actual ints and size/digest enum.
- **Input / Setup:** Start from the named category prerequisites and vary only this scenario's condition. Keep original manifest/receipt/source and record selected keys, safe locations, stored bytes and permissions before/after. For success use complete approved evidence; for invalid/security/fault/concurrency cases introduce that named condition at the specified stage. No fake production producer or guessed semantic IDs.
- **Expected Result:** Payload limits bound retained aggregate bytes and each read buffer; final bytearray-to-bytes conversion can temporarily duplicate the individual buffer plus a bounded chunk. Do not advertise exact RSS ceilings.
- **Expected Diagnostics:** Effective maxima are minima and integrity the stricter requirement. Declared count/length checked before any file access; actual fstat and each chunk checked. Exceeding limit CMP-072, invalid policy CMP-080. At most 1 MiB plus one-byte length/growth probe; no unbounded stream/buffer/cache. Exact limit succeeds; limit+1 fails. Positive valid cases add no errors; negative/unavailable cases preserve the exact bounded category, stage/source type/artifact/manifest/validated location when available. Do not leak absolute paths.
- **Boundary / Edge Cases:** Include relevant empty/single/multiple selected entries, first/last selected failure, exact size/count/name boundary and plus-one; maintain manifest order, explicit versions and selection mode. Where no contract permits a variant, expect explicit rejection rather than fabricated fallback.
- **Integration Dependencies:** ArtifactReadPolicy / effective bounded plan / chunk reads; existing CMP-07/CMP-08/CMP-02/CMP-06 and original Kernel/model evidence; approved local filesystem/producer only where this scenario requires them.
- **Acceptance Criteria:** All named expected observations documented against fixed revision; every selected byte and actual evidence accounted for; no partial successful payload, unbounded lookup, mutation/repair, unsupported integrity level, fake receipt or runtime authority. Static checks cannot satisfy deferred behavioral verification.
- **Execution Status:** NOT_RUN — DEFERRED

