# SK-02: Namespace

`semantic_kernel.public.Namespace` is an immutable semantic naming scope, a peer of `SemanticElementId` in the existing Kernel. It carries no identity, local element name, context, package, version, tenant, persistence or security semantics. Renaming a namespace produces a different naming value without changing an element's ID. QualifiedName will pair a Namespace with a local name in SK-03; neither QualifiedName nor a local-name primitive is implemented here.

## Syntax and contract

The canonical separator is `.`. Each canonical segment matches ASCII `[a-z][a-z0-9_-]*`. ASCII uppercase input is accepted and converted to lowercase; this is the only normalization. Examples: `Sales.Orders` becomes `sales.orders`; `sales-orders.accounts_payable` remains unchanged. Spaces, Unicode, controls, slashes, backslashes, colons, quotes, wildcards and URL syntax are rejected. Leading/trailing/double dots create invalid empty segments. No trimming, replacement or separator repair occurs.

Empty/root namespaces are forbidden. `platform`, `system`, `internal`, `class`, `namespace`, `module` and `package` are ordinary valid segments: reservations and technology escaping belong to higher layers. No arbitrary length or depth cap is imposed by the value object; input-size budgets belong at untrusted ingress boundaries. Parsing is linear in input length with a compiled segment regex.

```python
from semantic_kernel.public import Namespace, NamespaceError

scope = Namespace.parse("Sales.Orders")
assert str(scope) == "sales.orders"
assert scope.value == "sales.orders"
assert scope.segments == ("sales", "orders")
assert Namespace.parse(str(scope)) == scope
assert scope.parent() == Namespace("sales")
assert Namespace("sales").parent() is None
assert Namespace("sales").child("Orders") == scope
assert Namespace.try_parse("sales..orders") is None
```

Constructor and `parse(value)` share validation. `try_parse(value)` returns None for NamespaceError only; unexpected failures propagate. `value` is the canonical scalar; `segments` returns the cached immutable tuple. Equality and hashing use the canonical typed value, so mixed-case input gives equal Namespace keys, while strings and SemanticElementId values remain different types. There is no ordering contract; callers may sort by `str(scope)` for presentation. Frozen state and copies preserve the value.

`parent()` removes one naming segment and returns None for a single segment, without manufacturing an empty root. `child(segment)` validates exactly one segment, canonicalizes case, and returns a new Namespace. Dotted children are rejected. These helpers support simple naming navigation/composition; hierarchy implies no policy, type inheritance, context ownership or authorization. There is no ancestor engine, registry or resolution behavior. `from_segments` and a public NamespaceSegment are deferred because the scalar constructor and immutable tuple suffice.

## Diagnostics

| Code | Rejection |
| --- | --- |
| SEM-NS-001 | None, empty or entirely whitespace input |
| SEM-NS-002 | Non-string representation; no coercion |
| SEM-NS-003 | Segment violates the ASCII grammar, or child argument has multiple segments |
| SEM-NS-004 | Empty segment caused by leading, trailing or repeated dot |

NamespaceError is a ValueError with `code`, `message` and optional zero-based `segment_index`. Segment diagnostics explain the required grammar and failing position without retaining or echoing rejected input. Validation reports the first invalid segment from left to right. `child` first validates its standalone argument; errors there use argument-relative indexes. A multi-segment child error points to the append position in the parent.

## Serialization and demo

JSON mapping stays outside Kernel and follows SK-01's explicit scalar boundary:

```python
import json
scope = Namespace.parse("sales.orders")
encoded = json.dumps({"namespace": str(scope)})
assert encoded == '{"namespace": "sales.orders"}'
assert Namespace.parse(json.loads(encoded)["namespace"]) == scope
try:
    Namespace.parse("sales..orders")
except NamespaceError as error:
    assert error.code == "SEM-NS-004"
```

`json.dumps(scope)` requires explicit mapping; a segments-object wire shape is not accepted. Contract tests verify scalar/field round trips, case normalization and invalid JSON values. No serialization adapter module or framework is necessary for this primitive. The executable demo is `NamespaceSerializationTests.test_demo`.

## Architecture and evolution

Production imports remain `dataclasses` and `re`; there is no module dependency, new module, CLI command or bootstrap registration. ARCH-SK-NS-001 checks statically declared classes named Namespace in registered production sources belong to semantic-kernel, using the existing single AST pass. It cannot infer dynamically generated classes or aliases. Existing ARCH-SK-002 protects declared/observed dependency independence, and ARCH-SK-003 plus ARC-03 governance reject forbidden infrastructure/internal imports. These rules check dependencies, not arbitrary annotation semantics; redundant namespace infrastructure rules are not added.

See [ADR-0009](../architecture/decisions/ADR-0009-semantic-namespace-naming.md) for the long-term syntax decision. QualifiedName, SemanticContext, BoundedContext, aliases, imports, wildcard resolution, registries, cross-context mapping, tenancy, package mappings and evolution/migration services remain deferred. Case folding merges spelling variants by design; changes to grammar or case policy require an explicit compatibility decision. Namespace validity alone is never authorization. Next: SK-03 QualifiedName.
