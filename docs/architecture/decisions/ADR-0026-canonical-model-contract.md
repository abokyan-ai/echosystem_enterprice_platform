# ADR-0026: Selected exact canonical definition snapshots

Date: 2026-10-10 (Asia/Riyadh). Status: implemented against actual provisional semantic contracts; **NOT_RUN — DEFERRED / NOT VERIFIED**.

## Context

TYPE-07 is a context-aware version catalog; authoring/loading/source locations are separate upstream concerns. Consumers need selected immutable semantic membership without interpreting authoring syntax. Full TYPE-01 and general SK-11 are missing; current TypeDataComposition plus TYPE-07 frozen host capture is the actual usable seam. No existing Django canonical API needs extension.

## Decision

Own CanonicalModel/factory/results/intrinsic diagnostics in existing model-core public API, with no new module/dependency/profile. Reuse Kernel exact IDs/versions/context/names and current field/facet/reference/constraint definitions. V0's explicit supported CanonicalDefinition alias is the existing TypeDataComposition; future kinds require real owned contracts and explicit support extension. Do not invent a TypeDefinition class or accept arbitrary SemanticElement-shaped objects. Reuse existing TYPE-07 defensive capture/deep-value admission helpers without constructing, inheriting or wrapping a concrete TypeRegistry.

One model has one explicit context and caller-selected exact versions; allow multiple versions of one ID without choosing latest/default. Exact lookup uses ElementVersionRef only. Sort by stable ID scalar and numeric SemanticVersion. Deduplicate equal supported content idempotently; reject exact conflicting content, cross-context members and ambiguous name ownership among selected members. Preserve version-specific renames. Unselected registry historical name reservations are not imported because a canonical snapshot is selected membership, not the complete catalog.

Copy input collections, reuse existing frozen host snapshot and immutable nested values, own a private read-only exact map and return no partial model on intrinsic conflicts. No registration API or graph closure. Existing TYPE-05 identity-only field references remain unchanged; future exact target binding is explicitly separate. Dataclass equality/current-content comparison covers only the declared provisional host/data seam; membership comparison is separate. Disable model hash and add no model ID/version/serialized format or content digest.

General SK-11 cannot be reused before it exists. Use the established severity/path convention and narrow intrinsic diagnostics analogous to TYPE-07, with exact/related candidate coordinates and no invented source location. This is an explicit unresolved integration seam, not a competing generic diagnostic framework. Full TYPE-01/TYPE-08/SK-09 reconciliation remains visible.

Source locations/provenance are external associations; do not add metadata/tenancy or reverse tooling dependencies to semantic values. No authoring-to-canonical transform, parser, resolver, validator orchestration, registry registration, compiler/runtime/ORM/API behavior is implemented. No endpoint/serializer/Django model is added. Django/DRF remain the prescribed future HTTP stack but are absent from this domain task and are not upgraded.

## Consequences

Current construction is complete for actual typed host/data membership, not a claim of missing full semantic contracts. Unknown host attributes/future facets are outside the existing seam and cannot be advertised as preserved complete semantic content. Caller input diagnostics retain input indices, while successful membership is order-independent. A capture is not a synchronized read of a concurrently changing arbitrary host. Static checks do not prove factory/collision/immutability behavior; no test code or example execution is introduced. Detailed future scenarios are archived in one Markdown file, with navigation files preserving standing naming conventions. Stop at MOD-04.
