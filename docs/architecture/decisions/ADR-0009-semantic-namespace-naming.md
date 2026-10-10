# ADR-0009 — Semantic Namespace Naming Strategy

Status: Accepted
Date: 2026-10-10

## Context and requirements

SK-01 established identity independent of naming. SK-02 needs a pure, typed naming scope that can later form one component of QualifiedName, with stable cross-language equality and scalar serialization. The existing semantic-kernel module and public surface already provide the appropriate ownership and dependency boundary. ADR-0007 and ADR-0008 are occupied; this decision uses the next available number.

## Options

Considered dot versus slash separation, exact-case versus lowercase canonicalization, a letters/digits-only grammar versus letters/digits plus underscores/hyphens, and a separate public segment primitive. Slash invites path interpretation; exact case introduces avoidable cross-platform differences; a stricter grammar unnecessarily rejects the requested sales-orders/accounts_payable examples; a new segment type has no current independent use.

## Decision

Use dot-separated hierarchical namespaces. Canonical segments match ASCII `[a-z][a-z0-9_-]*`, accepting ASCII uppercase input and normalizing to lowercase. All other malformed input is rejected without repair or trimming. Empty root and empty segments are invalid. No reserved keywords or arbitrary length/depth cap are introduced. Boundary layers may impose resource budgets independently.

Namespace is a frozen Value Object in semantic_kernel.public, independently validated from SemanticElementId. Keep cached immutable segments and canonical scalar value; equality/hash are typed canonical value semantics, without ordering. Expose constructor, parse, try_parse, value, segments, parent and single-segment child. Single-segment parent is None. Hierarchy is naming only: it conveys no inheritance, context, tenant, package or security meaning.

## Consequences and future evolution

JSON boundaries explicitly map to a scalar string and parse on ingress, outside Kernel. ASCII case variants intentionally collapse to one key. Non-ASCII display names can live in later metadata; compiler and technology adapters handle escaping/mappings. A namespace rename changes its naming value without requiring an identity change; migration behavior is deferred. Any grammar/case change must address compatibility and existing keys. SK-03 may compose Namespace and a local name without extending this primitive with identity/context fields.

ARCH-SK-NS-001 adds static Namespace ownership protection; existing kernel independence/public dependency rules cover infrastructure constraints. No registry, aliases, imports, wildcard resolver or framework dependency is introduced.
