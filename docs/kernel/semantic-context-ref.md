# SK-04: SemanticContextRef

`semantic_kernel.public.SemanticContextRef` is a typed reference to the semantic meaning context intended to own/interpret a definition. It wraps one stable `SemanticElementId`, without embedding or resolving a Context Definition. It is a frozen Value Object in the existing Kernel, not a service, registry, runtime scope or lifecycle module.

## Identity strategy and concept separation

The current repository has no dedicated context identity contract or decision requiring contexts to use a separate ID model. SK-04 therefore uses the supplied default: a future context has stable SemanticElementId identity, and SemanticContextRef adds explicit target intent to that identity. It does not yet require Context Definition to be a particular class/subtype. No second identity scheme or `ctx_` prefix is introduced.

| Primitive/concept | Meaning |
| --- | --- |
| SemanticElementId | Stable opaque semantic identity |
| Namespace | Naming scope, not meaning ownership |
| QualifiedName | Canonical semantic name, which can evolve |
| SemanticContextRef | Stable typed reference to an intended meaning context |
| Domain / DDD Bounded Context | Future models/mappings; no equality assumption with Semantic Context |
| Tenant / organization | Separate isolation/organizational concepts |
| Package / application | Distribution/composition concepts, not Context identity |

Namespaces organize names; semantic contexts own meaning. Namespace-to-Context mapping and cardinality remain undecided and must later be explicit. The reference neither derives a context from a naming prefix nor carries names, name hints, display metadata, tenancy, permissions, package, deployment or runtime state. A context rename or move does not intrinsically change its stable identity reference. This value grants no authority or access.

## Public contract and validation

```python
from semantic_kernel.public import SemanticElementId, SemanticContextRef

identity = SemanticElementId.parse("sem_550e8400-e29b-41d4-a716-446655440000")
ref = SemanticContextRef.from_id(identity)
assert ref.context_id is identity
assert SemanticContextRef(identity) == ref
assert str(ref) == str(identity)
assert SemanticContextRef.parse(str(ref)) == ref
assert SemanticContextRef.try_parse("not-a-semantic-id") is None
```

Public API: `SemanticContextRef(context_id: SemanticElementId)`, `from_id(context_id)`, `parse(value)`, `try_parse(value)`, frozen `context_id`, `str`, value equality and hashing. A typed ID is required by constructor/factory; raw strings and other primitives require explicit parsing/construction rather than automatic coercion. Already validated identity values are retained without reparsing. Text parsing calls `SemanticElementId.parse`, reusing its prefix, UUIDv4/RFC variant, whitespace, case and representation rules exactly. Canonical reference text is the canonical `sem_<UUIDv4>` string, with lowercase hexadecimal; no alternate syntax or silent repair is added.

**Syntactic validity is not semantic resolution.** A valid identity can be wrapped with no model loaded. The value does not check target existence, whether the target is a Context, activity, accessibility or ownership. A valid ID notionally used for another semantic kind cannot be distinguished here; later resolution must check the actual target. There are no resolve/load/fetch/exists/owns methods, service lookup, definition caches, hierarchy, mappings or imports.

SemanticContextRefError is a ValueError exposing `code`, `message` and optional `identity_code` for a delegated parsing failure. It retains the underlying error cause/reason without retaining or echoing rejected input. `try_parse` catches only this expected reference diagnostic; unexpected implementation failures propagate.

| Code | Rejection |
| --- | --- |
| SEM-CTXREF-001 | Missing structural identity, or parsed None/empty/entirely whitespace input |
| SEM-CTXREF-002 | Constructor/factory input is not SemanticElementId, or parsed representation is not a string |
| SEM-CTXREF-003 | Parsed identity string violates SK-01 syntax |

Parser mapping is SEM-ID-001 -> SEM-CTXREF-001, SEM-ID-003 -> SEM-CTXREF-002, and SEM-ID-002 -> SEM-CTXREF-003. `identity_code` preserves the original code; structural errors have no delegated code. No unknown-context or wrong-target-kind diagnostic is claimed by the value object.

## Equality, hashing and rename safety

References are equal when their wrapped typed identities are equal; equal references have equal hashes and work as dictionary/set keys. A reference is not equal/interchangeable with a bare SemanticElementId, string, Namespace or QualifiedName. Python hashes are in-process collection hashes, not persistent wire fingerprints. There is no ordering contract. Copies preserve the value, and dataclass replacement revalidates the typed component.

```python
from semantic_kernel.public import QualifiedName
illustration = {"id": identity, "name": QualifiedName.parse("commerce.Sales")}
illustration["name"] = QualifiedName.parse("commerce.Ordering")
assert SemanticContextRef.from_id(illustration["id"]) == ref
```

This dictionary illustration is not Context Definition, Namespace ownership or rename migration implementation. The stored reference is independent of both name and namespace changes.

## Serialization and demo

External compact contracts map explicitly to a scalar string outside Kernel:

```python
import json
encoded = json.dumps({"context": str(ref)})
assert encoded == '{"context": "sem_550e8400-e29b-41d4-a716-446655440000"}'
restored = SemanticContextRef.parse(json.loads(encoded)["context"])
assert restored == ref
```

`json.dumps(ref)` requires explicit mapping; nested type/contextId/value object shapes are not accepted by parse. Serialization contract tests verify scalar/field JSON round trips, case canonicalization and invalid scalar/object inputs. No serializer framework, adapter module or authoring schema is added.

The executable contract demo creates the typed reference, verifies canonical text, round trip/equality, and checks not-a-semantic-id -> SEM-CTXREF-003. A separate inline verification demo prints that existence/target-kind checks are NOT PERFORMED HERE. Placeholder IDs from the prompt are conceptual examples; actual tests use valid SK-01 UUIDv4 strings.

## Architecture, risks and next work

The reference depends on SemanticElementId and the existing dataclass facility only, with no Namespace/QualifiedName use in its implementation. Kernel production imports remain dataclasses/re, with no observed cross-module dependency. ARCH-SK-CTX-001 checks statically declared SemanticContextRef classes in registered production sources are Kernel-owned, using existing single-pass AST discovery. Existing ARCH-SK-002/003 and ARC-03 rules protect non-Kernel dependencies and forbidden public imports; redundant context infrastructure rules are not added. Ownership analysis does not infer dynamically generated classes or aliases and is not full annotation/resolution analysis.

The context identity assumption must be revisited if a future formal model requires a distinct context ID or establishes that contexts cannot use SemanticElementId. Any change then needs compatibility/migration decisions; speculative dual identity models are deferred. Resolution must eventually validate existence, kind, visibility/activity and authorization as appropriate outside this value.

See [ADR-0011](../architecture/decisions/ADR-0011-semantic-context-reference-identity.md). SemanticContextDefinition, Context Registry/Resolver, hierarchy, ownership graphs, mapping, imports/aliases, Domain/Bounded Context models, policies, versioning and cross-context translation remain deferred. Next: SK-05 SemanticElement Base Contract, composing SemanticElementId, QualifiedName and SemanticContextRef as distinct typed properties.
