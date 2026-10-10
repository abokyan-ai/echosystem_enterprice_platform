# SK-03: QualifiedName

`semantic_kernel.public.QualifiedName` is the canonical semantic name of an element within a Namespace. It stores a validated `Namespace` and a validated plain-string `local_name`, rather than repeatedly splitting an unchecked string. It is a frozen Value Object in the existing Kernel, independent of stable identity, context, element kind, version, package, tenant, application, deployment, storage and execution. It has no source location, display/localization fields, resolution or I/O behavior.

## Naming strategy and public contract

Namespace keeps SK-02's dot-separated ASCII syntax and lowercase canonicalization. A local name matches ASCII `[A-Za-z][A-Za-z0-9_]*`, preserving exact case. Thus `Sales.Orders.SalesOrder` becomes `sales.orders.SalesOrder`, while `sales.Customer` and `sales.customer` are different names. Underscores are permitted after the first letter; hyphens are valid in Namespace segments but not local names. There is no PascalCase, event suffix or action-verb requirement. Keywords such as `class` are lexically valid; adapters can escape them later. Rich display names belong in separate metadata.

```python
from semantic_kernel.public import Namespace, QualifiedName, QualifiedNameError

namespace = Namespace.parse("sales.orders")
name = QualifiedName.create(namespace, "SalesOrder")
assert name.namespace is namespace
assert name.local_name == "SalesOrder"
assert str(name) == "sales.orders.SalesOrder"
assert QualifiedName.parse(str(name)) == name
assert QualifiedName(namespace, "SalesOrder") == name
assert QualifiedName.try_parse("SalesOrder") is None
```

Public API: `QualifiedName(namespace: Namespace, local_name: str)`, `create(namespace, local_name)`, `parse(value)`, `try_parse(value)`, frozen `namespace` and `local_name`, `str`, structural equality and hashing. No separate public LocalName primitive is added because no independent use exists yet. Constructor and factory require a typed, already validated Namespace without reparsing it; raw namespace strings are rejected. Text parsing splits at the final dot and calls `Namespace.parse` on the preceding text. The namespace validator remains the single source of truth.

An explicit namespace is mandatory. `Customer` is rejected, without implicit default/global root. Empty segments, whitespace, slashes, backslashes, Unicode, controls, quotes, wildcards, version suffixes and escaping syntax are rejected. There is no trimming, separator repair or local-name case conversion. Dots supplied in the structural local-name argument are rejected. In parsed text, the last dot always separates namespace and local name: `sales.orders.Customer` is valid with Namespace `sales.orders`.

## Diagnostics

QualifiedNameError is a ValueError with `code`, `message`, optional zero-based `segment_index`, and optional `namespace_code` for a delegated Namespace failure. It does not retain or echo rejected input. Namespace failures retain their reason and cause, permitting precise diagnostics without duplicating grammar. Validation checks the namespace component before the local component.

| Code | Meaning |
| --- | --- |
| SEM-QN-001 | Parsed scalar is None, empty or entirely whitespace |
| SEM-QN-002 | Parsed text has no final dot/explicit namespace, or structural namespace is None |
| SEM-QN-003 | Invalid namespace portion, or structural namespace is not a Namespace |
| SEM-QN-004 | Local name violates the grammar or is not a string |
| SEM-QN-005 | Empty namespace segment or empty local component, including None local input |
| SEM-QN-006 | Parsed representation is not a string; no coercion |

`NamespaceError` SEM-NS-004 maps to SEM-QN-005; other namespace validation failures map to SEM-QN-003, except an empty namespace prefix also maps to SEM-QN-005. For invalid namespace portions, `namespace_code` preserves the original code. Local diagnostics use index `len(namespace.segments)`; a missing parsed namespace or representation error has no index. `try_parse` catches only QualifiedNameError; unexpected failures propagate.

Examples: `sales.Customer` and `finance.accounts.payable.Invoice` pass; `Customer` gives SEM-QN-002, `sales..Customer` gives SEM-QN-005, `sales.Order Management` gives SEM-QN-004, and `9sales.Customer` gives SEM-QN-003 with SEM-NS-003 preserved.

## Equality, identity and evolution

Equality/hash use Namespace equality plus exact-case local-name equality. Equal names can serve as dictionary/set keys; strings, Namespace and SemanticElementId values are different types. Python hashes are process-local collection hashes, not persistent IDs or wire fingerprints. There is no semantic ordering; tooling may externally sort canonical strings. Copies preserve the value, and dataclass replacement revalidates changed components.

```python
from semantic_kernel.public import SemanticElementId
identity = SemanticElementId.parse("sem_550e8400-e29b-41d4-a716-446655440000")
item = {"id": identity, "name": QualifiedName.parse("sales.Customer")}
item["name"] = QualifiedName.parse("crm.Client")
assert item["id"] == identity
```

This dictionary illustration is not a SemanticElement implementation or migration policy. A rename or namespace move creates a new QualifiedName; it does not intrinsically change stable identity. Namespace hierarchy still carries naming only, without inherited policy/type semantics. Segments such as `v2`, `tenantA`, `security` or `package` may be lexically valid names, but encode no version, tenancy, privilege or package semantics in Kernel. No reservation or collision registry is consulted by equality.

## Serialization and executable demo

External compact contracts use scalar strings, explicitly mapped outside Kernel:

```python
import json
encoded = json.dumps({"qualifiedName": str(name)})
assert encoded == '{"qualifiedName": "sales.orders.SalesOrder"}'
restored = QualifiedName.parse(json.loads(encoded)["qualifiedName"])
assert restored == name
```

`json.dumps(name)` intentionally requires explicit mapping. Object-shaped namespace/localName wire values are rejected by parse. The JSON contract tests verify scalar/field round trips, local-case preservation, namespace canonicalization and rejected shapes. No serializer framework, adapter module or authoring schema is introduced.

`QualifiedNameSerializationTests.test_demo` verifies sales.orders.SalesOrder parsing, namespace/local extraction, canonical output and round trip. It also verifies SalesOrder produces SEM-QN-002 and sales.Order Management produces SEM-QN-004.

## Architecture, risks and next work

Production imports remain dataclasses/re. QualifiedName uses Namespace directly in the same public surface, with no SemanticElementId dependency, new module, CLI command or lifecycle registration. ARCH-SK-QN-001 checks statically declared QualifiedName classes in registered production sources belong to Kernel, using existing single-pass AST discovery. Existing ARCH-SK-002/003 and ARC-03 rules protect dependency independence/public imports; no redundant infrastructure rules are added. Static checks do not infer generated classes, aliases or arbitrary annotation semantics.

Exact-case local names can collide in case-insensitive projections; later model validators/adapters must handle portability. No arbitrary length cap is added: ingress boundaries can impose resource budgets. Changes to grammar/case/syntax require compatibility decisions. QualifiedName alone does not resolve uniqueness across models/contexts or grant authorization.

See [ADR-0010](../architecture/decisions/ADR-0010-qualified-semantic-naming.md). SemanticContext, SemanticElement, ElementRef, SemanticVersion, symbol tables, namespace resolution, imports, aliases, registries, package exports, cross-context mapping and rename migration/history remain deferred. Next: SK-04 Semantic Context Reference, then SK-05 SemanticElement Base Contract.
