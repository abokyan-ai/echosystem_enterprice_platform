# ADR-0012 — Minimal SemanticElement Root Contract

Status: Accepted
Date: 2026-10-10

## Context and problem

SK-01 through SK-04 provide stable identity, naming and a meaning-context reference. First-class semantic definitions need a common root that is broader than SemanticType and can be consumed without infrastructure or subtype knowledge. A behavior-heavy base class would couple unrelated future Type/Action/Event/Policy definitions and invite uncontrolled metadata growth. ADR numbers through 0011 are occupied; this decision uses 0012.

## Decision

Use a structural Python typing.Protocol named SemanticElement in the existing Kernel public surface. It has only three read-only properties: id: SemanticElementId, qualified_name: QualifiedName, context: SemanticContextRef. These are required, non-optional existing primitives. Concrete implementations protect their local invariants and immutable definition snapshots; no runtime-checkable protocol, builder or generic production instance is added.

Identity, naming and context are independent. Identity is not derived from name/context. The root imposes no global equality/hash: explicit ID comparisons express identity equality, while concrete types may decide snapshot equality. Definitions are distinct from business/runtime instances and executions.

Kind/Version are deferred to SK-06/SK-07, facets to SK-10, and metadata/annotations to explicit composed contracts. No temporary strings, dictionaries/object extension bags, subtype fields, source/transport/persistence/UI/API/security/package/runtime fields or subsystem behavior enter the root. Polymorphic serialization is not needed for an interface-only stage.

## Context meta-circularity

Ordinary first-class definitions require explicit context. If a future ContextDefinition implements this root, its ownership remains an unresolved bootstrap modeling question. Considered options: explicit kernel/system context; narrowly specified root exception; separate modeling of context definitions. No existing decision selects one, and SK-05 creates no root identity/definition, self-reference assumption or optional context escape hatch.

A reviewed architecture decision establishing context-definition ownership/bootstrap binding and resolution rules is required before introducing a production ContextDefinition. This deferral does not obstruct the current protocol or test implementations. Any future root exception needs exact semantics and compatibility treatment rather than null meaning multiple states.

## Consequences and evolution rules

Unrelated future definitions can structurally satisfy the root without inheritance behavior. Static property contracts are read-only, but Python Protocol alone does not enforce runtime type validation or immutability; concrete construction must do so. Tests use frozen, locally validated fixtures and functional consumers; no external static checker is claimed.

Adding a field to SemanticElement requires architecture review. It must be universal, technology-neutral, stable across runtime representations, independent from infrastructure, natural for all element kinds without widespread optional/null semantics, and a better fit here than in a facet/composed contract. Kind/Version additions must be typed and explicitly reviewed.

ARCH-SK-ELEM-001 adds static root ownership protection; existing independence/public import rules remain in force. Consumer tests, type contracts, source-shape guard and negative dependency fixtures provide complementary checks without claiming complete arbitrary semantic analysis. Concrete definitions, registries, resolution, references, facets and context bootstrap binding remain deferred.
