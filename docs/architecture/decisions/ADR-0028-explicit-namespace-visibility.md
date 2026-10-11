# ADR-0028 — Explicit namespace visibility and identity resolution

Date: 2026-10-10. Status: accepted for current supported contracts; behavioral verification deferred.

## Context

MOD-01 distinguishes authoring name/identity/exact-reference expressions but has no alias discriminator. MOD-05 requires explicit stable target bindings. TYPE-07's read-only TypeLookup offers identity lookup and requires external exact binding for ambiguous versions. Full SK-11/TYPE-01 are absent. Physical MOD-03 locations belong to tooling.

## Decision

Use minimal typed versioned SemanticSymbol coordinates in one frozen explicit visibility environment. Local and visible sources have equal standing; current namespace plus explicitly searchable namespaces determine local-name candidates. Qualified lookup is exact; context is never inferred or crossed. Ambiguous identities fail before kind/version safeguards can choose one. Selected qualified-name ownership and exact coordinate/kind integrity are checked when constructing the environment.

Reuse Kernel naming/reference values. Identity resolution returns ElementRef without choosing a version; exact requests/authored pins return only the requested visible ElementVersionRef. Retain all matched names for identity lookups rather than naming an arbitrary current version. Historical aliases are not created.

Implement direct concrete namespace aliases through a resolver-only explicit variant, without changing MOD-01 decoded syntax or reinterpreting ordinary dotted names. Equal targets are idempotent; conflicts fail. Concrete namespace targets are never alias-to-alias references, so no recursive chain engine exists.

Snapshot explicitly selected actual TypeLookup identities through a narrow type-only adapter, then resolve against copied symbols. No live/global lookup, concrete registry creation, mutation or hidden version binding. Caller supplies stable immutable views. Project local declarations before field binding without constructing definitions.

Bridge successful type targets to the existing MOD-05 ResolvedFieldBinding only; preserve exact pins even though current TYPE-05 canonicalization rejects them. Do not implement the complete reference-binding/build pipeline. Keep source paths/domain diagnostics narrow and provisional; attach actual MOD-03 physical coordinates through optional existing tooling presentation.

## Consequences

No new module/dependency/profile/exception, Django API/ORM/serializer, canonicalization/validation/compiler/runtime or authority model. Unseen registry history remains governed by TYPE-07 registration rather than implicit namespace visibility. Callers own semantic visibility, lookup purity and cross-stage document pairing. Deferred specifications are mandatory; static success does not verify resolution behavior. Stop after MOD-06.
