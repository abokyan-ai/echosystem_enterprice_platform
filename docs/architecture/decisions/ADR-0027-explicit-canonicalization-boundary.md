# ADR-0027 — Explicit resolved authoring canonicalization

Date: 2026-10-10. Status: accepted for the current supported contracts; runtime verification deferred.

## Context

MOD-01 retains authoring expressions and ordering. MOD-04 represents exact canonical membership. No general resolver, full TYPE-01 or general SK-11 exists. TYPE-05 has only identity-pinned semantic references. MOD-03 source types live in tooling, which domain modules must not depend on.

## Decision

Implement a separate stateless Canonicalizer operation in the existing model-authoring domain. Frozen resolution bindings make declaration identity, exact definition version, name, context, field identity and semantic target explicit. Intrinsic binding checks compare supplied coordinates/values against one immutable document; no namespace search, identity generation or registry lookup occurs.

Reuse existing field, reference, constraint and DataFacet constructors, and MOD-04 factory assembly. Expose a model-core-owned construction function for its existing five-value frozen host; do not duplicate TypeDefinition or import a private cross-module class. Multiple exact member versions remain selected explicitly. Exact field reference pins fail rather than weakening TYPE-05. Unknown schema content remains rejected upstream.

Preserve field order and TYPE-04 constraint ordering; MOD-04 owns definition ordering and collisions. Any failure returns no model or successful sidecar. Preserve delegated diagnostics and source paths through a narrow provisional diagnostic contract; no substitute general SK-11 is advertised.

Core sidecars identify exact owner references and stable FieldIds with original authoring paths. An optional model-loader presentation helper attaches existing MOD-03 physical locations through the existing inward dependency. It performs no loading/parsing/transformation. The caller must pair the exact original document; no stronger provenance certificate is claimed.

## Consequences

No new module, architecture-policy exception, dependency, Django API/ORM/serializer, mutable registry, canonical hash or runtime behavior. Current supported transformation is implemented, but full TYPE-01/SK-11 and exact-version field reference representation are separate real gaps. Deferred tests are documented only, static checks provide limited evidence, and the next task does not begin automatically.
