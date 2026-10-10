# SK-05: SemanticElement Base Contract

`semantic_kernel.public.SemanticElement` is the smallest root contract shared by first-class semantic **definitions**. It is broader than SemanticType: future Type, Relationship, Action, Event, Policy and other definitions may satisfy the same contract through composition. It is not a customer/order business instance, agent identity, workflow run or runtime execution, and it is not a transport DTO or database row.

## Public contract

SemanticElement is a Python structural `typing.Protocol` with five read-only property contracts after SK-07:

| Property | Required type | Meaning |
| --- | --- | --- |
| id | SemanticElementId | Stable semantic identity |
| qualified_name | QualifiedName | Canonical name for the definition snapshot |
| context | SemanticContextRef | Explicit intended meaning-context reference |
| kind | SemanticElementKind | Explicit open semantic classification |
| version | SemanticVersion | Exact definition evolution coordinate |

```python
from semantic_kernel.public import SemanticElement

def read_definition(element: SemanticElement):
    return element.id, element.qualified_name, element.context, element.kind, element.version
```

Implementations need not inherit the protocol or share implementation behavior. This avoids a mandatory base class, template methods or deep hierarchy. Protocol getter types are non-optional, use the existing primitives and provide a read-only static consumer surface. There is no root constructor, builder, runtime validator or generic production implementation. Python annotations/Protocol do not themselves enforce runtime value types or freeze implementations: concrete definitions must protect their construction invariants and immutable snapshot state. The protocol is intentionally not runtime_checkable; `isinstance` would only inspect member presence, not validate their semantic types.

Test-only frozen TestTypeDefinition and TestActionDefinition fixtures in `tests/contracts/test_semantic_element.py` demonstrate structural consumption, typed values, immutable snapshots and local construction validation. They are not production Type/Action definitions and do not introduce subtype semantics. No external static type checker was added or executed; contract tests exercise real consumers and inspect public return annotations, without claiming a compile-time type-checking run.

## Identity, naming, context and equality

Identity is supplied as SemanticElementId, never computed from a name/context hash. Naming is supplied as QualifiedName; namespace/local name remain accessible through that value without duplicate root fields. Context is supplied explicitly as SemanticContextRef and is never inferred from the naming prefix. Namespace remains naming scope, while Context identifies an intended meaning boundary without resolving its existence/kind.

Rename or context move can create a new snapshot with the same stable ID. The root does not override equality/hash or assert that same ID implies identical fields. Identity comparisons explicitly compare `.id`; concrete immutable definitions may separately define snapshot equality. Test dataclasses use structural snapshot equality as an illustration only, not a root requirement. SK-07 distinguishes stable identity from exact version coordinates through ElementVersionRef; changing version leaves identity intact.

## Required context and meta-circular ownership decision

Every implementation of this contract must expose a non-optional SemanticContextRef. There is no nullable context, omitted binding or hidden default in SK-05. This is workable because the protocol is a contract and ContextDefinition is not implemented yet.

If a future SemanticContextDefinition also satisfies SemanticElement, the question remains: **which context owns a context definition?** No existing formal root/context ownership strategy resolves this question. Considered options are an explicit kernel/system context, a precisely scoped root exception, or modeling context definitions outside the ordinary root. None is selected arbitrarily here. In particular, SK-05 does not create a system Context Definition/ID, infer `platform.semantic-contexts`, or assume self-reference.

Before a production ContextDefinition is introduced, an architecture decision must establish its ownership/bootstrap binding and resolution rules. The ordinary root remains required-context meanwhile. If a root exception is eventually necessary, it must have a separately documented exact contract and compatibility impact; null must not mean unknown/unbound/root interchangeably. Test fixtures use explicit syntactically valid context identities, without claiming loaded or resolved context definitions. This deferral and gate are recorded in ADR-0012.

## Minimal root and future evolution

The current contract contains only id, qualified_name, context, typed kind and typed version. SK-06 adds open classification and SK-07 adds the planned required exact SemanticVersion; neither uses temporary strings or defaults. Facets wait for SK-10; metadata/annotations require explicit composed contracts rather than an ungoverned dictionary/object extension bag. There are no tags, description/display fields, source locations, relationship collections, parent/children, type fields, action handlers, event payloads, persistence, UI/API, tenancy, security, package or deployment fields.

There are no validate/compile/persist/render/authorize/to_json/visitor/clone/register/lifecycle methods. Subsystem behavior belongs to external consumers, and local invariants belong to concrete construction. Polymorphic serialization is deferred until concrete definitions and typed Kind contracts exist; no discriminator/type registry or root serialization requirement is added.

**Adding a field to SemanticElement requires architecture review.** A proposed field must be universal to first-class definitions, technology-neutral, stable across representations, infrastructure-independent, natural for all element kinds, avoid widespread optional/null semantics, and belong here more clearly than in a facet/composed contract. This is an architectural decision, not a convenience refactor. Future root evolution must remain typed and explicitly reviewed.

## Architecture and executable demo

The root uses the existing SemanticElementId, QualifiedName, SemanticContextRef, SemanticElementKind and SemanticVersion in the same public surface, plus the standard-library typing.Protocol. Kernel production imports are dataclasses, re and typing; no non-Kernel dependency is introduced. No new module or bootstrap/CLI registration is needed.

ARCH-SK-ELEM-001 checks statically declared SemanticElement classes in registered production sources are Kernel-owned using the existing single AST pass. Existing ARCH-SK-002/003 and ARC-03 rules protect dependency independence and prohibited public imports. Negative fixtures demonstrate rejection of hypothetical runtime/compiler/ORM/UI imports. A source-level architecture test checks the current root declares only the five typed property contracts, alongside functional two-implementation consumer tests. No additional behavior rule is advertised as full semantic analysis. Static ownership does not infer generated classes/aliases.

The executable `SemanticElementContractTests.test_demo` reads the same contract from test Type/Action definitions with explicit ID, name, context, kind and version. Full fitness proves zero observed Kernel module dependencies; infrastructure/runtime/compiler dependencies are absent. Literal placeholder IDs in the prompt are replaced by valid SK-01 UUIDv4 values in actual tests.

See [ADR-0012](../architecture/decisions/ADR-0012-minimal-semantic-element-root.md) and [verification](../architecture/sk05-verification.md). Deferred: version ranges/compatibility, semantic references, facets, metadata/annotations, concrete definitions, registries, resolution and context bootstrap ownership. See [SK-06 kind contract](semantic-element-kind.md) and [ADR-0013](../architecture/decisions/ADR-0013-open-semantic-element-kind.md) for the planned kind addition. See [SK-07 version contract](semantic-version.md) and [ADR-0014](../architecture/decisions/ADR-0014-exact-semantic-version-reference.md) for exact versions. Next: SK-08 Semantic References, then SK-09 Primitive Type System.
