# ADR-0023: Authoring schema representation boundary

Status: implemented for MOD-01; behavioral verification DEFERRED; full SK-11/TYPE-01 integration remains open.

## Context

Current semantic contracts are Python frozen values, identity-only TYPE-05 references, TYPE-06 validation and TYPE-07 exact-version registry snapshots. Production TYPE-01, general SK-11 diagnostics, TYPE-08 and full SK-09 remain missing. Authors need explicit syntax without generating canonical objects or fabricating identities from names. The conceptual TypeScript examples cannot be integrated into the existing Python-only analyzer/value-object toolchain without a separate foundation.

## Decision

Create model-authoring in the model zone with only Kernel/model-core public API dependencies. Keep its dependency direction separate from core semantic model ownership. CLI imports MODULE_NAME for static inventory only; no authoring activation marker, compiler/runtime reverse edge or parser/framework dependency is added. Use repository-native Python contracts, explicitly documenting the language adaptation rather than claiming TypeScript implementation.

Validate decoded abstract dict/list trees and return frozen typed authoring snapshots, not canonical semantic definitions. Initial format is explicit 1.0; context is an explicit identity reference; namespace and local type name remain authoring text. Require IDs/versions, allow empty definition collections and absent/empty facets, keep fields under a single data facet and require explicit presence/nullability/value arrays.

Support primitive, unresolved semantic-name, explicit semantic-id and exact semantic-version discriminators. Reuse Kernel syntax without lookup or inference. Preserve authored definition/field ID/name/version text, value literals and declaration order. Exact pins remain distinguishable from TYPE-05 identity-only references; future transformations must reconcile them explicitly.

Reuse TYPE-04 payload/local consistency contracts, never TYPE-06 applicability policy. Support only seven current value constraints and seven primitives; reject unknown kinds/properties, ambiguous variant keys, malformed shapes and duplicate local declarations. Failures aggregate stable source-tree diagnostics without partial document output or mutation. Duplicate checks use normalized typed identity comparisons even while snapshots preserve authored text.

SK-11 cannot be integrated before it exists. Use narrow AuthoringSchemaDiagnostic/Path with current model ERROR severity, delegated cause codes and related source coordinates. Do not implement physical locations, provenance or a competing generic diagnostic framework. Extensions remain closed until explicit versioned contracts are introduced.

## Consequences

Authoring syntax, structural judgment and canonical semantics remain separate. Existing test sources are preserved; three inventory expectations are adjusted to eight modules but not executed. Comprehensive tests and even schema example execution are deferred; static lint/build/Fitness evidence does not prove behavioral correctness. Exact-version conversion, full unified diagnostics, TYPE-01 reconciliation, parsers/resolvers/canonicalizers, compiler/runtime, persistence/UI and provenance remain future work.

See [schema contract](../../model/authoring-schema.md) and [deferred specification](../../../test-archive/MOD-01/MOD-01-deferred-test-spec.md).
