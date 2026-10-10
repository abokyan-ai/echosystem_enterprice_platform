# MOD-02 — Model Loader: repository test archive

Task ID: **MOD-02**. Title: **Model Loader**. Documentation date: **2026-10-10 (UTC)**.
Testing status: **DEFERRED / NOT VERIFIED**. Deferred tests executed: **0**.
Scenarios: **109**, stable IDs MOD-02-T001 through MOD-02-T109.
Specification: [MOD-02-deferred-test-spec.md](MOD-02-deferred-test-spec.md).

## Implementation scope and affected sources

[model_loader.public](../../tools/model-loader/src/model_loader/public.py) contains dedicated source ID/format/metadata/options, immutable result/diagnostic/position/batch contracts, minimal provider/decoder protocols, memory/read-only local-file providers, strict JSON and PyYAML SafeLoader 1.1 decoder adapters, ModelLoader.load and deterministic load_many. It delegates all authoring structural judgment to MOD-01 and returns immutable authoring snapshots associated with sources. Every duplicate source-ID occurrence is rejected; unique sources retain input order. No semantic resolution/registry/canonicalization/compiler/runtime behavior.

Other changes: architecture.json module declaration; architecture-policy.json narrow parser profile/approval; pinned requirements-model-loader.txt; scripts/dev.py install dependency setup; CLI explicit inventory name without a loader import/activation edge; two existing inventory test-source count updates (not executed); README/CONTRIBUTING/repository structure documentation; new Mini Sales YAML and module test README. Full file list/static activities are in [mod02-verification.md](../../docs/architecture/mod02-verification.md).

## Architectural dependencies and future execution conditions

Only model-authoring public module dependency, reusing its existing Kernel/model-core contracts transitively. YAML parser is PyYAML==6.0.3, narrowly approved only at tools/model-loader. Built-in JSON is stdlib; file acquisition is read-only UTF-8 with explicit supplied paths. Root build imports MODULE_NAME without loading examples. Nine modules, seven observed CLI edges, five foundation activation markers.

Future execution requires explicit user authorization, fixed source/archive revisions, Python 3.11+, repository module paths, pinned YAML dependency for YAML cases, OS/effective user fixtures for real permission errors and FIFO/symlink cases, recorded expected/actual diagnostics and immutable-source checks. Reconcile or explicitly target the provisional SK-11 seam. Record date, revision, commands and evidence before changing a test status; preserve previous scenarios/history. No executable deferred test infrastructure is added merely to document these cases.

## Known limitations and open architectural decisions

Implementation adapts conceptual TypeScript to existing Python analyzer/contracts. General SK-11 diagnostics are missing; loading SourcePosition/ModelLoadDiagnostic is a narrow provisional seam retaining original MOD-01 errors. TYPE-01/TYPE-08/full SK-09 remain incomplete. YAML is 1.1, not 1.2: quoting is required to avoid implicit scalar conversions; all explicit tags, anchors/aliases, merge keys and multiple documents are rejected. JSON schema/duplicate-key positions are unavailable; no physical location is invented. Missing YAML properties likewise have no node mark. No end span, checksum, filesystem confinement, atomic external file revision, hard time quota or semantic provenance graph is claimed.

Configured byte/depth/node bounds mitigate practical parser exposure. Injected adapters are trusted code and unexpected programming failures propagate; successful returned trees still receive compatibility/limit checks. File symlinks to regular files are allowed; caller owns path authorization. Future parser/format providers and unified diagnostics need explicit decisions. All example loading, snapshot equivalence, semantic-side-effect and robustness scenarios remain unverified.

See [loading contract](../../docs/model/model-loader.md) and [ADR-0024](../../docs/architecture/decisions/ADR-0024-model-source-loading-boundary.md). Stop at MOD-02; no subsequent stage implemented.

## Subsequent MOD-03 compatibility note (2026-10-10)

MOD-03 adds reliable physical spans/indexes and related locations without executing or deleting any of these archived cases. JSON schema/duplicate-key locations and YAML missing-property containing-object spans now have new expectations at the MOD-03 revision, documented in its [single detailed specification](../MOD-03/MOD-03-deferred-tests.md). Preserve these MOD-02 baseline cases/statuses and record which source/archive revision future execution targets. No prior results are reclassified.
