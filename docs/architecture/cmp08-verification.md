# CMP-08 — Implementation and static inspection record

Date: 2026-10-11. Task: Artifact Writer. Status: **DEFERRED / NOT VERIFIED**. Tests implemented/executed: **0**. Deferred scenarios: **158**, all **NOT_RUN — DEFERRED**.

## Components and source files

Modified production source:
- `platform/compiler/compiler-core/src/compiler_core/public.py`: ArtifactWriter, immutable write request/destination/policies, approved byte-source contracts, layout/planner/plan, result/materialization receipt, CMP-044..061 diagnostics and typed associations; pure application/domain, no filesystem/framework import.

Created production source:
- `tools/artifact-writer/src/artifact_writer/__init__.py`: owned package namespace.
- `tools/artifact-writer/src/artifact_writer/public.py`: ApprovedLocalArtifactRoot, LocalFilesystemArtifactWriter facade and secure local Linux infrastructure (root-fd traversal, private staging, short-write handling, exact byte/inode/inventory/declared digest verification, fsync policy, single NOREPLACE commit, owned cleanup).

Architecture config modified: `architecture.json`, `architecture-policy.json`; add the constrained tooling module/profile and compiler-public API edge, no compiler capabilities or dependency exceptions weakened. Existing runtime/activation edges preserved. No test or CI changes.

Documentation created: `docs/compiler/artifact-writer.md`, `docs/architecture/decisions/ADR-0039-artifact-writer.md`, this record and the sole `test-archive/CMP-08/CMP-08-deferred-tests.md`. Related repository/compiler/diagnostic/determinism/manifest indexes are updated. Latest task section 37 explicitly prohibits archive README/extra spec files; previous archive history remains intact.

## Static evidence, separate from deferred tests

Syntax/whitespace/architecture lint, source compilation/build with public MODULE_NAME imports, architecture fitness, dependency graph and diff checks are permitted static checks. No archive cases, runtime materialization, Mini Sales, CLI smoke or automated suites execute. Initial inspection caught a compiler-to-filesystem placement violation; final ownership was corrected into tooling rather than adding an exception.

Final local static checks: lint/build completed successfully; architecture fitness HEALTHY, **44 rules**, **10 modules**, **47 production Python sources**, **0** failures/warnings/exceptions/suppression/cycles; dependency graph and diff formatting clean. Public imports construct no writer/request and touch no output destination. Django/DRF package metadata: NOT_INSTALLED; no applicable HTTP boundary, endpoint/ORM/migration added.

CI retains DEFER_COMPREHENSIVE_TESTS=true. Merge is conditioned on six successful push/PR static jobs (Python 3.11/3.12/3.13) and verification that each skips all nine comprehensive/runtime/smoke steps (54 skips). Their green state does not verify this implementation's behavior. Remote commit/PR evidence is reported after actual checks, not treated as test success here.

## Risks and readiness

No current real final artifact byte producer/kind/encoder, so empty default approvals cannot produce a successful manifest/materialization. Current IR-only artifact-build remains INCOMPLETE. The real adapter is implemented, but no output operation has been executed during this task. Future success/fault/concurrency fixtures require explicit verification authorization and actual approved producer contracts.

Linux libc/kernel/local-filesystem support and administrator-controlled roots/ancestry are required. Flat safe filenames only; oversized default layouts need explicit complete shorter mapping. Other OS/remote storage/atomic replacement unsupported. fsync establishes requested synchronization operations subject to storage semantics, not universal crash durability. Post-rename failure may leave visible complete output and no receipt; callers inspect committed_destination. Cleanup can fail safely and process crashes can leave staging; no sweeper. Privileged/hostile same-UID actors or administrator path moves are outside v0 isolation. Trusted in-process provenance is not authentication/portable anti-forgery proof. Full SK-11/TYPE-01 and applicable Django HTTP API remain absent. Added module may affect existing module-count expectations; historical tests are preserved and remain deferred.

[Contract and conceptual Mini Sales](../compiler/artifact-writer.md), [decision](decisions/ADR-0039-artifact-writer.md), [158 deferred cases](../../test-archive/CMP-08/CMP-08-deferred-tests.md). Implementation is ready for authorized review/future verification and downstream planning subject to these prerequisites. Stop CMP-08; CMP-09 is not started.
