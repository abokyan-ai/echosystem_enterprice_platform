# MOD-01 — Authoring Model Schema v0

Status: implementation present; deferred-suite execution **0**; **DEFERRED / NOT VERIFIED**. Examples and documented outcomes are expected contracts, not claims of executed behavioral validation.

## Repository assessment and ownership

This repository has a Python 3.11+ stdlib contract/toolchain, despite conceptual prompts using TypeScript examples. MOD-01 follows that actual architecture instead of creating a parallel TypeScript semantic foundation unable to reuse current Python value objects. No TypeScript implementation is claimed.

A new model-authoring module owns the authoring contracts and structural validator in `model_authoring.public`. It depends only on `semantic_kernel.public` and `model_core.public` for existing value syntax and constraint vocabulary. Model-core and Kernel do not depend on authoring. Compiler/runtime/compiled artifacts do not acquire authoring dependencies. The manifest now contains eight modules. CLI has a development-only public MODULE_NAME import for inventory consistency; authoring is not added to the five-module activation composition.

Existing production TYPE-01, SK-11 and TYPE-08 are absent; full SK-09 remains incomplete beyond the existing seven-token vocabulary. MOD-01 does not regenerate these foundations or modify TYPE-01..07 abstractions. Its schema is useful independently of a Semantic Instance Contract. Full SK-11 integration is an open dependency, not claimed complete. Current AuthoringSchemaDiagnostic reuses existing ERROR severity and provides a narrow source-tree path/cause-code seam; it is not a general replacement diagnostics framework.

## One representation boundary

The wire-shaped abstract document is composed of decoded plain dict/list/str/int JSON-compatible values. It is independent of a YAML/JSON parser. `AuthoringSchemaValidator.validate(source: object)` checks this tree and returns an immutable typed AuthoringModelDocument on structural success, or ordered diagnostics and no document on failure. It never reads files, parses source text or creates a canonical semantic model. Producing the typed authoring snapshot is schema projection, not semantic canonicalization.

The validator accepts the decoded abstract tree, not JSON text or previously constructed dataclasses. Direct declaration constructors enforce representation value shapes/immutability; direct construction is not a full schema-validation certificate. This is one schema represented as decoded input and typed snapshot, not competing YAML and JSON authoring models. No generic decoder framework, JSON Schema generator or serializer/content hash is introduced.

The public snapshot contracts are:

| Contract | Fields / role |
| --- | --- |
| AuthoringModelDocument | schema_version, typed context reference, namespace authoring text, ordered definitions |
| AuthoringTypeDeclaration | original ID/name/version text, ordered facet declarations; fixed kind type |
| AuthoringDataFacetDeclaration | ordered field declarations; fixed kind data |
| AuthoringFieldDeclaration | separate original FieldId/FieldName text, explicit authoring expression, constraint declaration |
| AuthoringConstraintDeclaration | separate FieldPresence/FieldNullability, ordered authored values |
| AuthoringValueConstraintDeclaration | existing ConstraintKind and original plain integer/text literal |
| AuthoringSchemaValidationResult | document or None, immutable diagnostics; derived is_valid |
| AuthoringSchemaDiagnostic | stable MOD code/message/path, optional delegated cause_code and related_path |
| AuthoringSchemaPath | immutable property/index segments in the source tree; not identity or physical location |

## Format, context and naming

Root properties are exactly `schemaVersion`, `context`, `namespace`, `definitions`, all required. Only format token **"1.0"** is accepted for the initial v0 schema. It is not a SemanticVersion, compiler/package/runtime revision, or instance version. Unknown versions fail closed.

Context is a scalar semantic identity string validated by SemanticContextRef.parse and retained as the existing typed reference. Symbolic `sales-context` is not supported; no context lookup/declaration registry exists. Namespace is original authoring text checked by Namespace.parse. A definition name is a local ASCII name using the repository's existing local-name grammar. The namespace and local name remain distinct authoring components; no definition QualifiedName is generated or stored.

Definitions require `kind: type`, stable semantic `id`, local `name`, and exact semantic `version`. Facets may be omitted (no facets) or an explicit list (including empty). Definitions may be an empty list. No identities/default versions are generated. Identity/version text is preserved, including accepted ID hex case; temporary typed parsing supports syntax and duplicate comparisons, never name binding.

Within this one context/namespace document, duplicate exact (ID, version) declarations and different identities claiming the same exact local name are structural errors. Multiple versions of one ID are allowed; names may change across versions. No registry lookup, version selection, compatibility/chronology policy or global ownership assertion is made. Definition names remain case-sensitive. Field names additionally follow the existing DataFacet ASCII case portability policy.

## Facet and field schema

Only `kind: data` is supported; at most one such facet per definition. Its `fields` list is required and may be empty. Fields remain under facets, never directly under definitions. Unknown facet/definition kinds are not extension objects.

A field requires `id`, `name`, `type` and `constraints`; no defaults or inference. Field ID is not derived from name, position, host name or physical representation. Duplicate canonical FieldId, duplicate exact FieldName and case-portability collisions are diagnosed with related paths to the first declaration. Valid duplicate coordinates are still considered when another property in the field is invalid.

All declaration arrays retain authored order. They are copied into tuple snapshots; original dict/list aliases cannot mutate a returned document. All leaf authoring text and constraint payloads are plain immutable values; domain value objects are existing canonical frozen contracts. No internal writable collection is exposed.

## Explicit authoring type expressions

| kind | Required properties | Meaning |
| --- | --- | --- |
| primitive | primitive | Existing seven-token Kernel primitive vocabulary |
| semantic-name | name | Unresolved local or qualified name syntax; no ElementRef fabricated |
| semantic-id | id | Explicit authored stable identity, retained as ElementRef; no selected version |
| semantic-version | id, version | Explicit exact identity/version retained as ElementVersionRef |

Each expression must be an object with its exact discriminator/keys. Bare `"string"`, ambiguous optional reference properties and compact `type: Customer` syntax are not supported in this initial schema. Primitive tokens are exactly string, boolean, integer, decimal, date, datetime, uuid; object/any/arrays/maps/runtime classes fail closed. Named references check local or QualifiedName syntax only, with no namespace prefixing, alias/import handling, existence checks or symbol binding.

Explicit identities are syntax-validated but do not certify target existence/kind. `latest`, `current`, `*`, ranges and malformed exact versions are rejected by existing syntax. Exact authored pins cannot currently be copied blindly into TYPE-05's identity-only SemanticTypeRef: future resolution/canonicalization must define pin reconciliation rather than discard it. MOD-01 preserves that distinction and performs no conversion.

## Constraint declarations

`constraints` requires all three properties: `presence`, `nullability`, `values`. Presence is required/optional; nullability is nullable/non-null; values is an explicit ordered array, including empty. All four presence/nullability combinations remain distinct. There are no implicit defaults, optional-to-nullable inference or value coercions.

Values are objects with exactly `kind` and `value`:

| Constraint kind | Authored payload |
| --- | --- |
| min-length, max-length | Plain int >= 0; bool/float/string rejected |
| precision | Plain int > 0 |
| scale | Plain int >= 0 |
| minimum, maximum | Exact fixed-point numeric text under NumericConstraintValue's existing grammar/digit limit; no JSON float/int coercion |
| pattern | Nonempty exact text; no regex compilation or execution |

Original numeric text, including accepted leading/trailing zeros, stays in the authoring snapshot. Temporary existing TYPE-04 value objects and FieldConstraintSet enforce payload validity, duplicate kinds and min/max/scale/precision consistency; no conflicting algorithm is duplicated. Value declarations retain original author order instead of adopting FieldConstraintSet's canonical kind sorting.

Structural validity is not applicability: string+precision is representable and structurally accepted; TYPE-06 must judge it later after explicit transformation. MOD-01 never calls TypeValidator, imports a concrete TypeRegistry, constructs FieldDefinition/DataFacet/TypeRef/TypeDefinition, resolves a graph or validates instance values.

## Structural diagnostics and extension policy

Expected malformed decoded source produces diagnostics with no partial output document. Programming errors in direct typed constructors remain exceptions. Missing properties, wrong shapes, wrong tokens and unsupported properties do not cause auto-repair or identity generation. Unexpected delegated implementation failures are not hidden by blanket exception handling.

| Code | Meaning |
| --- | --- |
| MOD-SCHEMA-001 | Wrong object/array shape or non-string object key |
| MOD-SCHEMA-002 | Missing required property |
| MOD-SCHEMA-003 | Unsupported property, including properties from another expression variant |
| MOD-SCHEMA-004 | Unsupported authoring format version |
| MOD-SCHEMA-005 | Unsupported definition kind |
| MOD-SCHEMA-006 | Unsupported facet kind |
| MOD-SCHEMA-007 | Invalid identity, context, namespace, local name or type version syntax |
| MOD-SCHEMA-008 | Unsupported type-expression discriminator |
| MOD-SCHEMA-009 | Invalid/unsupported primitive token |
| MOD-SCHEMA-010 | Invalid semantic reference expression syntax |
| MOD-SCHEMA-011 | Constraint token, payload, duplicate kind or local consistency failure |
| MOD-SCHEMA-012 | Duplicate exact definition or ambiguous local name ownership |
| MOD-SCHEMA-013 | Duplicate field identity/name or case-portability collision |
| MOD-SCHEMA-014 | Duplicate DataFacet |

Required-property diagnostics follow declared schema property order; unsupported property names are sorted by Python's deterministic string order. Root syntax checks follow context then namespace; definitions/facets/fields/values traverse original array order. Child shape/value errors precede duplicate membership diagnostics at that declaration; related_path identifies the first matching source coordinate. Non-string keys emit one object-shape diagnostic. Unsupported discriminators stop payload interpretation rather than guessing another kind. Dependent local constraint consistency checks occur only after that constraint block's payloads are structurally valid.

Paths are typed source-tree coordinates such as `$['definitions'][0]['facets'][0]['fields'][2]['constraints']['values'][0]['value']`. Array ordinals are source coordinates, not semantic IDs. cause_code preserves delegated SEM/TYPE diagnostic codes without leaking rejected values. No physical file/line/column or provenance contract is implemented while SK-11 is absent. Such fields are unsupported properties, not mutable fields on canonical definitions.

Default extensions are closed: metadata, databaseTable, UI properties, imports, aliases and arbitrary facets/kinds are rejected. Future support requires explicit versioned discriminated contracts, owned validators and architecture review; no generic bag or dynamic extension registration is created.

## Mini Sales and invalid examples

[mini-sales.json](../../examples/authoring/mini-sales.json) adapts all IDs/context to real UUIDv4 value syntax. Customer contains name:string/max-length 200, active:boolean and optional non-null creditLimit:decimal/minimum "0"/precision 18/scale 2, each under one data facet. It is authored data, not generated canonical objects or runtime instances. Its expected structural acceptance is specified and **has not been executed**.

Expected examples (not executed): missing definition id -> MOD-SCHEMA-002; primitive object -> MOD-SCHEMA-009; repeated canonical FieldId -> MOD-SCHEMA-013; databaseTable -> MOD-SCHEMA-003; omitted nullability -> MOD-SCHEMA-002, with no inference; semantic-name Employee remains AuthoringNameExpression without target identity; semantic-version with latest -> MOD-SCHEMA-010 and delegated SEM-VER code. Minimum authored as JSON 0 rather than exact text -> MOD-SCHEMA-011; quoted "0" is the chosen exact literal contract.

## Deferred verification and next boundary

The [MOD-01 test archive](../../test-archive/MOD-01/README.md) documents all positive/negative/edge/integration cases. No schema validation demo, unit test, architecture suite or archived scenario is run during implementation. Essential lint/build/dependency Fitness checks are separate static evidence only. Existing comprehensive/runtime CI steps remain explicitly skipped.

Next requested work can build a parser/resolver boundary against these contracts after reviewing deferred specifications and missing foundations; no MOD-02 or other future task is started. See [ADR-0023](../architecture/decisions/ADR-0023-authoring-schema-representation-boundary.md) and [static-check record](../architecture/mod01-verification.md).
