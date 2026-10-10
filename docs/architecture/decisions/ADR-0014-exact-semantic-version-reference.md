# ADR-0014 — Exact Semantic Version Reference

Status: Accepted
Date: 2026-10-10

## Context and options

Stable ID, canonical name, context and open kind cannot select an exact evolved definition. The existing CLI/package release string describes another concern. Reusing a package version library, raw strings, full SemVer prerelease/build syntax and a compatibility engine were considered. None matches the minimal current requirement better than a small Kernel-owned exact coordinate. ADR-0012/0013 are occupied; use 0014.

## Decision

Add frozen SemanticVersion(major, minor, patch), canonical ASCII major.minor.patch only. Plain integer components use 0..9223372036854775807, the non-negative signed 64-bit range, for a portable wire expectation and deterministic bounded parsing. Reject bool/int subclasses, non-integers, negative/overflowed components, leading zeros, Unicode digits, whitespace, v prefixes, prerelease/build suffixes, ranges and selectors. All-zero is valid; zero implies no policy. Equality/hash use the numeric triple; ordering uses numeric components, never serialized text. Store structured numbers and generate canonical text; no increments.

Add frozen ElementVersionRef(element_id: SemanticElementId, version: SemanticVersion), no duplicated name/context/kind. Identity is stable across version changes. Equality/hash include both fields. The human ID@version syntax is safe because IDs prohibit @; parsing delegates both primitives. Structured JSON with elementId/version fields and scalar version strings is preferred; explicit converters belong outside Kernel.

Add only required read-only version: SemanticVersion to the existing root Protocol, completing five properties. All current test implementations/consumers migrate explicitly. This early planned contract addition is breaking for external structural implementations with only four properties; they must provide a typed version, with no automatic default. No production concrete definitions currently exist. Context ownership remains gated by ADR-0012.

## Consequences and future governance

The value is SemVer-like, not full SemVer or a compatibility claim. Numbers are author-declared coordinates; actual compatibility requires future semantic diff/contract rules. Package, artifact, model, deployment, API/event schema and migration versioning remain separate concerns. No registry, resolution, publication checking, ranges/selectors, migration or latest lookup is introduced. Publication must eventually guarantee immutable meaning for each ID/version; a coordinate alone proves neither content integrity nor existence/reproducibility.

Existing 44 dependency/import/public Fitness rules suffice; actual type/shape/root and behavior tests add focused coverage. No redundant Fitness rule is invented, no module/framework/bootstrap command is introduced. Revisit prerelease or component range only for a concrete interoperability requirement with a documented wire compatibility decision. Next: SK-08 then SK-09.
