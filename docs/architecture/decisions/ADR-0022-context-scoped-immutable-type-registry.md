# ADR-0022: Context-scoped immutable type registry

Status: accepted for TYPE-07's supported composition seam; full TYPE-01/SK-11 integration remains provisional.

## Context

TYPE-06 consumes read-only TypeLookup.find(ElementRef)->SemanticElement|None. Kernel distinguishes stable identity, exact version and name; SemanticVersion supplies numeric comparison. Bare identity lookup cannot express several definitions. This repository implements Python contracts, despite the conceptual prompt using TypeScript examples. Production TYPE-01 and general SK-11 diagnostics are absent; TYPE-03 TypeDataComposition and TYPE-06's diagnostic/path seam are actual available foundations.

## Decision

Implement TypeRegistry in model-core using existing frozen Python contracts and Kernel public values. One snapshot belongs to one semantic context. Use private immutable exact/identity/name indexes and atomic copy-on-write registration. Canonical ID then existing SemanticVersion order governs enumeration independently of registration order. Exact version lookup never falls back; broad ID/name lookup returns every matching version.

Capture the five typed Protocol-host values into a private frozen registry root and share only canonical immutable DataFacet/field/constraint objects. This closes mutable host aliasing without introducing a replacement TypeDefinition or deep-clone system. Supported seam structural equality, including data presence and field order, distinguishes idempotent duplicates from exact-entry conflicts. Future unknown facets are not claimed to be compared.

One name has one identity owner per scope across all registered versions. Permit names to vary across versions, including historical backfill. Preserve the name recorded by each version; historical names are not aliases, and cannot be reassigned while retained in this snapshot. Scope/name ownership is an explicit registry-local policy, not a global namespace authority.

Keep registration separate from TypeValidator; only registration invariants are enforced. Return immutable typed success/duplicate/failure results. Use narrow provisional TypeRegistrationDiagnostic with existing severity/path conventions, exact identity/name/context coordinates and stable TYPE-REG codes. Do not claim SK-11 reuse/completion when the dependency is absent.

Keep TYPE-06 unchanged. Registry implements TypeLookup directly for zero/one-version IDs; several versions raise a specific orchestration ambiguity error. Explicit TypeRegistryLookup bound to chosen exact references supplies an unambiguous selected-only view for multiversion snapshots. Unselected identities are absent; no implicit latest/default/single-version fallback exists. Binding unknown/duplicate selections is a programming error. No lookup invokes validation or traverses the semantic reference graph.

## Consequences

The implementation is deterministic, immutable and entirely in memory, with no Kernel reverse dependency or external infrastructure. Index rebuilds cost O(n log n) per insertion, appropriate for the foundational scope. Version preferences remain the caller's decision; direct multiversion TypeLookup cannot safely be used without an explicit view. Future richer TypeDefinition facets and unified diagnostics require deliberate contract reconciliation. Unsupported mutable subclasses are rejected rather than silently weakening snapshot guarantees.

TYPE-08, persistence, instance execution, authoring/aliases, compilation, relationship traversal, compatibility/migration and global/remote registries remain deferred. See [actual contracts and example](../../model/type-registry.md).
