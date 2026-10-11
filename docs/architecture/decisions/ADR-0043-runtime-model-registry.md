# ADR-0043 — Scoped exact runtime registry with atomic local membership

Date: 2026-10-11. Status: accepted for implementation; behavioral/concurrency verification deferred.

RUN-01 exposes immutable loaded artifacts but has no approved concrete runtime decoder or model definition format. TYPE-07 stores upstream semantic definitions and cannot become a runtime fallback. Runtime registry membership must preserve exact identity and provenance without granting activation or execution.

Implement inside existing runtime-core, keeping Kernel/compiled-contracts as its only public dependencies. Extend existing runtime diagnostic codes/stages with registry-specific associations, not a second generic diagnostic framework. Add runtime stdlib threading solely for a private Lock; no Thread/worker, infrastructure/ORM imports, module or dependency exception.

Application owners create an explicit local instance with a bounded immutable scope allowlist and policy. Keys combine semantic context/runtime target with existing ElementVersionRef. Multiple versions and human-name candidates coexist; exact lookup never falls back to latest/name/TypeRegistry/loading. Versionless references require explicit selection; enumeration is a separately authorized read.

Registration consumes only actual successful original RUN-01 evidence. Explicit trusted extraction support binds the same decoder approval and selects actual immutable nodes already encoded in its closed representation graph. Original node/artifact/load association is retained; no canonical/IR reconstruction or guessed one-artifact-one-definition mapping. Default extractor/kind catalog is empty and unsupported capabilities are incomplete. Model-wide artifacts can have explicitly approved zero definitions; a zero-entry registration additionally needs trusted ALLOW_VERIFIED_NO_CHANGE policy and authority.

Registration and every inspection need their own trusted instance/scope/operation/selector/source-bound authorizer decision. Default authority is unavailable. Mutation results reveal only the submitted committed IDs; a full post-state snapshot requires separate inspection authority. Load possession/checksum is not registration permission. These are trusted in-process composition contracts, not cryptographic authority tokens or an arbitrary Python sandbox.

REJECT_CONFLICTS rejects duplicate batch/existing exact keys including equal entries, because approved idempotent content/provenance equivalence is unavailable. Preflight stages whole immutable entries outside the lock; a private lock checks current conflicts/capacity and publishes one fully built copy-on-write state/result. Readers capture coherent immutable state under the same lock. Old snapshots are stable; thread scheduling does not establish a deterministic winner. No overwrite, merge, activation pointer, rollback, persistence or distributed synchronization.

Django/DRF remain selected backend technologies but are not installed and have no applicable authenticated HTTP workflow. No endpoint/serializer/ORM/migration is introduced. Actual future composition must supply real decoders/extractors and authenticated authority before registry membership can be produced.

Consequences: functional locally thread-safe registry source, bounded snapshots/indexes and exact-version semantics; per-instance/process isolation and copy-on-write/graph traversal costs. Original loaded evidence may retain other decoded members of its source set; no duplicated read buffers or artifact store. Count limits are not exact heap/latency guarantees. No registration/lookup/concurrency scenario was run.

[Contract and conditional Mini Sales](../../runtime/runtime-model-registry.md), [sole deferred archive](../../../test-archive/RUN-02/RUN-02-deferred-tests.md), [static record](../run02-verification.md). Tests created/executed: **0**; **DEFERRED / NOT VERIFIED**. Stop RUN-02.
