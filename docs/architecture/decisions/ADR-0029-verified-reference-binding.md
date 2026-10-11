# ADR-0029 — Verified reference binding and complete authoring readiness

Date: 2026-10-11. Status: accepted for actual supported contracts; behavioral verification deferred.

## Context

MOD-06 already interprets names/aliases/identity/exact expressions in explicit single-context visibility. MOD-05 needs existing complete authoring bindings. TYPE-05 field references are identity-only; full TYPE-01/general SK-11/TYPE-08 remain missing.

## Decision

Keep reference requirements separate from target identity: expected kind, identity-only/exact semantics and bounded general-definition/type-field consumer. Delegate all namespace interpretation to the actual MOD-06 service. Verify matching immutable declared/visible symbol evidence and preserve whole delegated diagnostics, context, source paths and explicit pins.

Return existing ElementRef for unpinned identity and ElementVersionRef only for explicit compatible exact intent. An identity-only consumer never discards authored pins, and an exact type-field consumer reports current TYPE-05 incompatibility rather than weakening the reference. Final SemanticTypeRef/field/facet/definition/model construction remains with MOD-05.

Reuse existing local symbol projection and TypeLookupSymbolAdapter. Capture visible external selections through caller-supplied immutable TYPE-07 views; do not invent a registry/lookup/version-selection engine. Evidence categories record local/visible source, not registration authority/provenance. No hidden live lookup or global cache.

Finite batches preserve all occurrence outcomes and distinguish complete/partial/none. Whole-document binding enumerates every field, bypasses primitives, validates explicit local declaration coordinates and exposes the existing ResolvedAuthoringModel only when all required semantic occurrences succeed. Result invariants reject missing/extra/contradictory coverage. Readiness is reference completeness, not full semantic validity.

Physical MOD-03 presentation remains in tooling through existing inward dependency. Caller owns original document pairing; no source position is semantic identity. All verification scenarios remain Markdown-only.

## Consequences

No new module/dependency/framework/API/ORM, canonicalization, recursive graph traversal, compiler/runtime, instance repository or security engine. Current exact general references are supported; exact fields remain a real downstream gap. Full SK-11/TYPE-01 and stronger provenance require separate implementation. Examples are unexecuted; static evidence is separate. Stop after MOD-07.
