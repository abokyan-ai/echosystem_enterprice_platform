# ADR-0016 — Composable Semantic Facet Model

Status: Accepted
Date: 2026-10-10

## Context and alternatives

Enterprise definitions accumulate orthogonal data, policy, persistence, API and experience concerns. Deep inheritance and optional-field God Objects couple every concern to a single root; an untyped metadata bag hides contracts rather than expressing composition. Existing Kernel kinds/reference primitives support a small independent base. SK-09 PrimitiveType is absent in the inspected main; SK-10 does not use it and proceeds independently without claiming Minimum Kernel completion. ADR-0015 is occupied; use 0016.

## Decision

Introduce a minimal structural FacetDefinition Protocol with only read-only kind: FacetKind. Facets are composed definition concerns, not automatically SemanticElements with their own IDs/names/context/version. Concrete snapshots own typed invariants; no generic payload bag or production GenericFacet exists. Keep SemanticElement unchanged and defer FacetHost until concrete hosts need it.

FacetKind is a strongly typed immutable open canonical value, sharing only lexical validation with SemanticElementKind. Canonical dot-separated lowercase ASCII kebab segments are strict, without normalization. Publish the fourteen typed Core kinds data/behavior/lifecycle/workflow/rule/policy/security/api/event/persistence/experience/search/audit/integration in a frozen catalog. Unknown valid identifiers survive, including future unqualified vocabulary; custom publication should be scoped under future ownership governance. No public Enum, mutable registry or parser Core allowlist.

Represent applicability separately as frozen FacetApplicability(facet_kind, allowed_element_kinds: frozenset[SemanticElementKind]). Require explicit typed frozen sets; empty means nowhere, not wildcard. Equality/hash use the unordered set and facet kind. Allow custom host kinds without runtime class/registry coupling. No final Core matrix, required/present semantics, conflicts/dependencies/multiplicity resolver or validation engine is implemented. Document at most one facet per kind as the default future host invariant without encoding speculative fields.

Keep compiler/runtime/serializer/security/framework behavior outside facets. Explicit FacetKind scalar JSON follows existing kind boundaries; polymorphic payload loading and applicability wire formats wait for concrete contracts. No service locator, parent pointer, tenant overlay, enabled/priority flags, extension hooks or last-write-wins semantics.

## Consequences and revisit conditions

Future DataFacet/PolicyFacet/PersistenceFacet can contribute typed concerns without root bloat, and external validators/compilers interpret them. Facet does not equate to Capability, Extension, Annotation, language mixin or UI component. Independent facet identity/versioning or a host container requires a separately justified design. Existing 44 Fitness rules plus actual type/shape/behavior tests protect neutrality; no redundant engine/rules or external static checker is introduced.

Publication must eventually govern scoped ownership/collisions and compiler support. Concrete facets must define applicability/dependencies/conflicts and immutable payloads; base values do not certify support or safety. Complete SK-09 then SK-11 before declaring Minimum Kernel ready for TYPE-01/02/03. ContextDefinition bootstrap ownership remains gated by ADR-0012.
