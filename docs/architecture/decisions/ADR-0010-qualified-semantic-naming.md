# ADR-0010 — Qualified Semantic Naming Strategy

Status: Accepted
Date: 2026-10-10

## Context and requirements

SK-01 supplies stable opaque identity, and SK-02 supplies Namespace naming scope. The next primitive must name an element explicitly within that scope, preserve identity/name separation, support pure structural equality/hash and scalar round trips, and remain neutral to frameworks and deployment technologies. Namespace ADR-0009 does not decide local-name grammar or case. Existing ADR numbers 0008/0009 are occupied, so this decision uses 0010.

## Options

Considered an unchecked concatenated string versus structured Namespace/local name, case-insensitive versus exact-case local naming, and a new public SemanticLocalName type versus an internal validated string. Structured composition prevents unchecked state and reuses Namespace validation. Exact case preserves authored semantic names without guessing naming style. A separate local-name primitive has no current independent use and would expand the early public contract unnecessarily.

## Decision

QualifiedName is a frozen Value Object in semantic_kernel.public with Namespace and plain-string local_name. Local grammar is ASCII `[A-Za-z][A-Za-z0-9_]*`, with exact case preserved and no semantic-kind style enforcement. Namespace keeps SK-02 normalization. Canonical text is namespace + dot + local name, parsed at the final dot with Namespace.parse. An explicit namespace is mandatory; no relative names or default root are inferred.

Constructor/create accept a validated typed Namespace without reparsing. parse/try_parse accept scalar text; validation failures use SEM-QN codes and preserve delegated namespace diagnostics. No whitespace trimming, repair, escaping or local-case conversion occurs. Equality/hash are structural and pure; there is no ordering, registry lookup or I/O. Wire boundaries explicitly map to scalar strings outside Kernel.

## Identity separation and consequences

A rename or namespace move changes the name value independently of SemanticElementId. QualifiedName carries no context ownership, version, kind, tenant, package, source location or display name. Exact-case local names can collide on case-insensitive platforms; later model validation/projection adapters must address portability. Python hashes support in-process collections, not persistent identity or cross-process hashing.

Changing grammar/case rules requires explicit compatibility/migration decisions. Rich display names can be later metadata, while adapters map semantic names to technology syntax. SK-04/SK-05 can compose these contracts without adding context/element behavior here. Imports, aliases, resolution, registries, references, versions and rename migration remain deferred.

ARCH-SK-QN-001 adds static class ownership protection. Existing kernel independence and public dependency rules continue to guard infrastructure boundaries; no redundant rule or framework dependency is added.
