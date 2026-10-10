# ADR-0013 — Open Semantic Element Kind Strategy

Status: Accepted
Date: 2026-10-10

## Context and options

SK-05 planned a typed classification addition to the minimal root. Ecosystem packages/partners may introduce new categories without rewriting Kernel. A closed enum makes current vocabulary an exhaustive universe and encourages ordinal wire contracts/closed dispatch. An unchecked string cannot enforce lexical rules or nominal type distinctions. Choose a frozen strongly typed open value set instead. ADR numbers through 0012 are occupied, so this decision uses 0013.

## Decision

SemanticElementKind stores exact canonical ASCII lowercase dot-separated kebab-case segments, each `[a-z][a-z0-9]*(?:-[a-z0-9]+)*`. Reject noncanonical case, malformed separators, whitespace and other syntax without repair. Use typed equality/hash and scalar text; never numeric ordinals or Unknown/Other fallback values. Parsing is local and independent of Core membership, support registries or implementation classes.

Publish only the agreed twelve Core values as short unqualified identifiers in an immutable SemanticElementKinds catalog, with ALL/is_core for inspection. Canonical literals have one code source. Custom publishers should use scoped values; unqualified publication is reserved for platform vocabulary under future registration governance. Parsing accepts unknown unqualified lexical values too, so future Core values can survive older inspection tools. Enforcing ownership/reservation at publication is separate from parsing; no registry is implemented now. All-namespaced Core identifiers were considered but add a wire prefix without sufficient current benefit over the requested short values.

Add only required read-only kind: SemanticElementKind to SemanticElement. This planned early contract evolution means structural implementations must add the property; all current fixtures/consumers are migrated. No default kind, version, facets or metadata is introduced. The value has no compiler/type/ID/name/context/package coupling.

## Consequences and forward compatibility

Unknown syntactically valid values remain exact through parse/string/JSON mapping, display, compare and storage. Unsupported semantics are a Compiler/Application result, not lexical invalidity. JSON conversion remains explicit outside Kernel. Polymorphic loading, handler dispatch, schemas, package registration, versioning and concrete definitions are deferred.

Published canonical Core values are long-lived wire contracts: never silently repurpose them or rename them without migration. Future extension publication must govern reservations, scoped ownership and collisions; a scope alone proves no publisher identity or permissions. Contract/version semantics remain independent. Existing kernel dependency rules and targeted open-value/root-type tests suffice; no redundant infrastructure rule or broad enum detection is added.

Revisit only with evidence of a permanently platform-owned closed vocabulary or a separate external numeric protocol, while retaining semantic identifiers as canonical meaning. Context-definition ownership remains the ADR-0012 decision gate. Next: SK-07 then SK-08.
