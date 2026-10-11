# CMP-09 — Implementation and static inspection record

Date: 2026-10-11. Artifact Reader. Status: **DEFERRED / NOT VERIFIED**. Tests created/executed: **0**. **173** future scenarios, all **NOT_RUN — DEFERRED**.

## Production source files modified (2)

- `platform/compiler/compiler-core/src/compiler_core/public.py`: pure ArtifactReader protocol, request/source alias/explicit selection/policy, planner/plan, actual verification/RetrievedArtifact/result, CMP-062..080 diagnostics and trailing typed read associations; CMP-06 diagnostic comparison. Existing CompilationResult/ArtifactWriteResult unchanged.
- `tools/artifact-writer/src/artifact_writer/public.py`: independent LocalFilesystemArtifactReader and safe read-only Linux adapter, reusing existing ApprovedLocalArtifactRoot/root-fd helpers. No writer/staging/rename/repair/cleanup calls in reader flow.

No production files created, no module/dependency/policy/CI/test changes. Existing tooling compiler-public edge/profile retained; 10 modules/47 production sources unchanged. No HTTP/ORM/migration/framework/activation/runtime dependency.

Documentation created: reader contract, ADR-0040, this record and sole `test-archive/CMP-09/CMP-09-deferred-tests.md`. Related repository/compiler/manifest/writer/diagnostic/determinism indexes updated, and AGENTS notes latest section 45 single-archive exception. Historical tests/scenarios/evidence untouched.

## Static inspection and permitted checks

No automated suite, manual reader/writer experiment, Mini Sales, runtime or CLI smoke is executed. Permitted lint/build compile source and import public MODULE_NAME only; static fitness/dependency/diff/document inspection is distinct from testing.

Final local syntax/whitespace/architecture lint and build/public imports completed successfully. Architecture fitness HEALTHY: **44 rules**, **10 modules**, **47 production source files**, **0** failures/warnings/exceptions/suppression/cycles. Dependency graph and diff formatting clean. Documentation links and 173 stable IDs/status records inspected. Django/DRF package metadata remains NOT_INSTALLED; no applicable HTTP boundary modified or endpoint added.

CI retains DEFER_COMPREHENSIVE_TESTS=true. Auto-merge requires six completed successful static push/PR jobs on Python 3.11/3.12/3.13 and actual verification of nine skipped comprehensive/runtime/smoke steps per job (54 skips). This is never a passed deferred suite. Actual PR/main/tree evidence is reported after checks/merge, not preasserted here.

## Readiness and risks

Real final producer/encoder/current successful receipt absent; no runtime read success was demonstrated. Future integration requires genuine original manifest/materialization evidence and explicit permission to verify deferred cases. No full SK-11/TYPE-01/portable authenticated provenance/HTTP API implemented. Receipt has expected length and optional explicit SHA-256; missing mandatory digest INCOMPLETE, size-only cannot detect equal-length corruption.

Only existing trusted same-UID Linux local storage and portable flat paths supported. Root ancestry/mounts must remain controlled; privileged/hostile same-UID actors and administrator moves are outside containment. Nonblocking/type checks prevent FIFO hangs within supported open behavior; no disk latency bound or universal special-device/platform guarantee. Metadata/path binding detects obvious modifications but does not establish immutable/cross-file snapshot. Complete selected success verifies declared entries, not directory exclusivity. Read-only code makes no writes; O_NOATIME used for files, no universal underlying filesystem side-effect claim. Finite payload limits may incur bounded conversion/interpreter overhead, not exact RSS. No cloud/remote/streaming/repair/decoder/writer/publisher/runtime authority.

Ready for authorized review/future verification and next-stage planning subject to prerequisites. [Contract and conceptual Mini Sales](../compiler/artifact-reader.md), [decision](decisions/ADR-0040-artifact-reader.md), [sole deferred specification](../../test-archive/CMP-09/CMP-09-deferred-tests.md). Stop CMP-09; CMP-10 not started.
