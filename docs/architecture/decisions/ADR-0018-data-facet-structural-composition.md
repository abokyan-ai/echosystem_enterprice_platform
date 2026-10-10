# ADR-0018 — DataFacet Structural Composition Strategy

Status: Accepted (host wrapper provisional pending production TYPE-01)
Date: 2026-10-10

## Context and alternatives

Fields must compose structural data semantics without turning TypeDefinition into a fields bag or physical schema. TYPE-02 fields and SK-10 facet contracts exist; TYPE-01, SK-09 and SK-11 do not. A full generic FacetSet/Host framework would require unsupported payload immutability and applicability policies. Direct fields on type, duplicate field storage, untyped maps, mutable lists and automatic merging are rejected. Use the next actual ADR number 0018, not illustrative 0019.

## Decision

Add model-owned frozen DataFacet with ordered typed field tuple and read-only fixed kind=FacetKinds.DATA, structurally satisfying FacetDefinition. Accept explicit ordered list/tuple, copy to tuple, allow empty structure and reject invalid/null entries, duplicate FieldIds/exact names and ASCII case-only collisions. Preserve input order without ordinals/sorting. Exact typed find_by_id/name return field or None. Snapshot equality/hash includes order; neither ordering nor equality classifies semantic compatibility. Containment establishes ownership; no owner pointers/global registry.

Declare immutable DATA_FACET_APPLICABILITY for type-definition only. Add the smallest first-concern association TypeDataComposition(type_definition: SemanticElement, data: DataFacet|None). Validate the five typed root properties and actual applicability. Single typed slot enforces at most one data facet; lists/duplicates/other objects cannot be silently merged. None and explicit empty DataFacet remain distinct. Retain the host reference without copying identity or fields; concrete hosts own immutable snapshot invariants. A wrapper does not deep-freeze arbitrary host implementations.

TYPE-01 is missing, so composition is proved using the existing immutable test-only TypeDefinition fixture. No production TypeDefinition or general host framework is invented. This association is provisional and must be adopted/reviewed with production TYPE-01. Future multi-concern hosting needs a small typed container design rather than optional-property accumulation; the current root and fields remain unchanged.

Use existing local error/code conventions with deterministic first-error indices while SK-11 is missing. Demonstrate only a specific test-only internal/evolving kind/ordered-fields JSON mapping outside model-core; no final authoring schema or generic polymorphic loader. No type/constraints placeholder, physical projection, instance values, compiler/runtime dependency or automatic migration/merge semantics.

## Consequences and future seams

DataFacet now owns structural membership; host retains type identity; fields retain rename/reorder-independent IDs. Local duplicate/case rules support portability without changing FieldName case-sensitive equality. Cross-host ownership, extension augmentation, generic facet dependencies/conflicts and compatibility remain external future validation.

Existing 44 Fitness rules and actual shape/direction/behavior tests suffice. Complete missing SK-09/SK-11/TYPE-01 before production integrated type readiness, then TYPE-04/05/06. Revisit the provisional wrapper when a second concrete facet/real TypeDefinition provides requirements; preserve one-facet-per-kind, explicit applicability and missing/empty distinction. Revisit wire stability only after field type/constraint contracts mature.
