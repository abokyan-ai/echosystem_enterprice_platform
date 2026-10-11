# ADR-0038 — Assemble checked immutable runtime artifact declarations after successful final builds

Date: 2026-10-11. Status: implemented contracts/assembler; no final producer, DEFERRED / NOT VERIFIED.

## Context

CMP-01 has artifact metadata/key/kind contracts and authoritative final collection but no concrete generator; CMP-05 emits intermediate Type IR only. Original result did not bind original request/compiler invocation, while CMP-06 can compare semantic declarations but cannot authorize foreign input. Final artifact payload equality/byte/digest/location contracts do not exist.

## Decision

Add shared Kernel-only immutable dependency/producer metadata/descriptor contracts to compiled-contracts. Reuse original artifact key/kind/protocol; optional producer manifest_metadata is separate from semantic dependencies/payload. Approve only explicit real frozen artifact classes/kinds; default approval list empty. No concrete producer/kind generated.

Append optional original request/compiler output origin to CompilationResult; original ModelCompiler attaches invocation-local identity binding without changing statuses/state/artifact protocol/objectives. Checked manifest association validates original successful artifact-build, exact evidence/snapshot/context/configured outcomes and current immutable configuration. Extract descriptor/outcome snapshots with InitVar result so artifact payloads are not retained. Compiler manifest remains an in-process bound description; future portable provenance/publication transport must supply its own real contract.

Manifest uses distinct caller token/V0, complete checked artifact inventory, original scope/target, unique key ordering and explicit exact origins/internal dependencies. Dependencies are membership only; self/cycles allowed, no graph/loading policy. Enforce full inventory/no subset/unknown dependencies/duplicate overwrite. Same-declaration comparison is bounded metadata, not payload/bytes/authority. Use original statuses/diagnostics and trailing typed related artifact/manifest associations.

## Consequences

Current Type IR-only artifact-build cannot yield manifest success. Producer-dependent positive verification blocked until real artifacts/approved contracts exist; no placeholder workaround. In-process bindings trusted rather than authenticated/portable; callers own explicit uniqueness inventory/approvals. No runtime import change/HTTP/ORM/serialization/hash/storage/publish/activate/deploy/execute/authorization. Tests deferred, stop CMP-07.
