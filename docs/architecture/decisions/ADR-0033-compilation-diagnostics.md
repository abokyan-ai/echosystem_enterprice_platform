# ADR-0033 — Compose compiler diagnostics through existing MOD-09 projection

Date: 2026-10-11. Status: implemented within existing bounded contracts; behavior unverified.

## Context

CMP-01 supplies original immutable compiler diagnostic/result/outcome and atomic artifact metadata contracts. MOD-09 already owns the shared domain diagnostic envelope and inward tooling projection. General SK-11/factory is absent; there is no compiler HTTP route. Replacing these contracts or adding outward tooling edges would violate current ownership.

## Decision

Keep scalar semantics on original diagnostics and reuse current severity. Compiler-core owns typed association/wrapper/reporter and independent actual artifact identifiers. Extend the existing authoring-owned presentation seam with explicit responsibility, artifact token projection, semantic scope, summary, phase prerequisites and execution evidence. Model-loader reuses source enrichment and explicit transport through its existing inward edge. No dependency/profile exception is needed.

Use producer diagnostic occurrence identity/counts rather than set membership/equality deduplication. Fixed legacy code ownership plus original outcome association is bounded compatibility; new producers can provide explicit association. Preserve original validation origins and original compilation status. Report compiler-only derived summary separately from unified model diagnostics. Retain authoritative CMP-01 diagnostic emission order.

Record actual execution evidence in the existing producer, not inferred status. Enrich the existing conflict exception with actual key and related candidate semantic dependencies without changing collision algorithm. Never fabricate phase execution, artifact instances, source coordinates, facet identity or SK-11 compatibility.

Reuse MOD-03 source machinery at tooling boundary. Source mappings can be absent/ambiguous; original explicitly located evidence wins. Default presentation excludes message/source/semantic/artifact details; caller authorizes opt-in details through actual future API policy.

## Consequences

Manual result constructors must retain original phase diagnostic object occurrences. Evidence is in-process and not transferable automatically across serialization. Source selection and optional detail redaction remain caller obligations. Artifact metadata views do not grant publishability. General SK-11 and applicable DRF integration remain blocked by absent upstream contracts. No new phase/generator/validator/runtime/API/persistence is introduced. 137 scenarios remain NOT_RUN — DEFERRED, tests executed 0; static checks are not behavioral verification. Stop CMP-02.
