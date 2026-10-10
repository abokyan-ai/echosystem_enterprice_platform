# ADR-0011 — Semantic Context Reference Identity Strategy

Status: Accepted
Date: 2026-10-10

## Context

SK-01 gives stable semantic identity; SK-02/SK-03 give naming scopes and names. Context owns meaning, and a future element needs an explicit reference to its meaning boundary that survives name changes. No existing dedicated context identity decision requires a second ID model. Prior ADRs through 0010 are occupied, so this decision uses 0011.

## Options and decision

Namespace or QualifiedName references are insufficient because naming can evolve and no namespace/context cardinality or implicit prefix mapping is decided. Passing a bare SemanticElementId fails to communicate target intent. A separate Context ID scheme adds unsupported duplication.

Use a frozen SemanticContextRef wrapper around one SemanticElementId, with constructor/from_id, scalar parse/try_parse, read-only context_id and canonical str. Parsing delegates to SK-01; no new prefix or duplicated validation is introduced. Equality/hash are typed, pure and based on the wrapped identity; there is no ordering or implicit coercion to/from other primitives. Scalar serialization maps explicitly at external boundaries, outside Kernel.

## Resolution boundary

The wrapper expresses an intended Context target, not proof that its identity exists or denotes a Context. Syntactic identity validation is local; target-kind, existence, activity/accessibility, ownership and authorization require future model/resolver/policy layers. No Registry, resolver methods, cached definition or runtime state exists in this primitive.

Namespace is naming scope, QualifiedName is canonical naming, and ContextRef is stable meaning-boundary reference. No name hints, namespace mapping, cardinality, Domain/Bounded Context equivalence, hierarchy, tenancy, package or application relationship is decided here.

## Consequences and revisit conditions

Context renames need not change references. Future Context Definitions can expose SemanticElementId without a prescribed class/subtype, and SK-05 can compose identity, naming and context separately. Static ARCH-SK-CTX-001 ownership protection complements existing kernel independence/public import rules; no redundant infrastructure rule is added.

Revisit if the formal Context model requires a distinct stable identity or cannot use SemanticElementId. That would require explicit wire/API compatibility and migration decisions. A speculative second identity model is not built now. Context Registry/Resolver, mappings, hierarchy, imports, ownership, versioning, policies and cross-context translation remain deferred.
