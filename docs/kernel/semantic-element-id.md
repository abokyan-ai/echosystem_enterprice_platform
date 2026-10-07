# SK-01: SemanticElementId

`SemanticElementId` is the identity of a semantic definition, independent of its name, namespace, kind, semantic version, tenant, runtime instance and storage. Create it once, reference it many times and retain it when a definition is renamed. It contains no element business classification and has no repository lookup or lifecycle behavior.

## Canonical contract

The only supported wire format is **`sem_<UUIDv4>`**, exactly 40 ASCII characters:

```text
sem_550e8400-e29b-41d4-a716-446655440000
```

The `sem_` category prefix is mandatory and case-sensitive. UUID hexadecimal digits may arrive in upper, lower or mixed case and always normalize to lowercase. Hyphens must occur in the UUID's 8-4-4-4-12 grouping. The UUID version field must be 4 and its variant nibble must be 8, 9, a or b. The UUID layout version is unrelated to a future semantic model version. Nil/Max UUIDs, other UUID versions, braces, URNs, unprefixed UUIDs, bytes, integer representations, Unicode substitutes, control characters and surrounding whitespace are rejected. Input is never trimmed, coerced or repaired into another identity.

UUIDv4 was selected for portability to the supported Python 3.11/3.12/3.13 stack and standard-library availability. It does not provide chronological sorting. SK-01 represents and validates supplied values; it provides **no generator** and does not allocate randomness, access a clock or prove global uniqueness. A future issuance boundary can use an established UUIDv4 implementation; validation cannot verify the origin or entropy of supplied bytes. No custom random algorithm or distributed identity registry exists here.

## Public API

```python
from semantic_kernel.public import SemanticElementId, SemanticElementIdError

identity = SemanticElementId("sem_550e8400-e29b-41d4-a716-446655440000")
identity = SemanticElementId.parse(str(identity))
assert SemanticElementId.try_parse(str(identity)) == identity
assert SemanticElementId.try_parse("not-an-id") is None
assert identity.value == str(identity)
```

The constructor and `parse` share validation. Invalid input raises the one small `SemanticElementIdError(ValueError)`, carrying `code` and `message`. `try_parse` returns an identity or None for validation failure; it does not swallow unexpected implementation errors. A missing constructor argument remains Python TypeError (programmer misuse).

| Code | Meaning |
| --- | --- |
| SEM-ID-001 | None, empty or whitespace-only input |
| SEM-ID-002 | Invalid textual prefix, length, characters, layout, version or variant |
| SEM-ID-003 | Non-string representation; no implicit coercion |

Diagnostics do not echo/store rejected input. Kernel does not import bootstrap/CLI diagnostics; a future external diagnostic boundary can map these small semantic codes. String subclasses are normalized through built-in string methods so an overridden `lower` cannot produce invalid stored state.

The value object is a frozen slotted dataclass with a canonical string field. Normal assignment/deletion is prohibited and no mutable object graph is stored. Equality requires the same value-object type and canonical value; a raw string/UUID is not equal to the identity. Equal values have equal hashes and work in dictionaries/sets. Python hashes are process-local values, not persistent identifiers or a serialization contract. No ordering or clone-to-new-identity API is supplied. Copy/deepcopy preserve the same identity value.

## Serialization outside Kernel

Use a scalar/string at serializer boundaries:

```python
import json
from semantic_kernel.public import SemanticElementId

identity = SemanticElementId.parse("sem_550e8400-e29b-41d4-a716-446655440000")
encoded = json.dumps({"id": str(identity)})
restored = SemanticElementId.parse(json.loads(encoded)["id"])
assert restored == identity
```

`json.dumps(identity)` intentionally requires explicit mapping; it does not silently create a `{type,value}` DTO. JSON encoding/decoding tests live in `tests/contracts`, outside Kernel production source. No serializer dependency, converter module or general serialization abstraction is added. Future YAML/wire adapters should preserve the same scalar and parse it at input boundaries.

## Rename example

```python
identity = SemanticElementId.parse("sem_550e8400-e29b-41d4-a716-446655440000")
definition = {"id": identity, "name": "sales.Customer"}
definition["name"] = "sales.Client"
assert definition["id"] == identity
```

This example is a dictionary illustration, not an implementation of QualifiedName or SemanticElement. ID validity is not authorization. Prefixes classify the ID category; they do not create tenant/type/version semantics.

## Ownership and verification

The implementation remains in the existing `semantic_kernel.public` surface, with only `dataclasses` and `re` imports. The regex is compiled once at import. No new module, CLI command, bootstrap registration or external package is needed.

ARCH-SK-001 checks ownership of statically declared classes named SemanticElementId. Class names/locations are collected from the existing AST parse, without rescanning files. It does not infer dynamically generated classes or aliases. ARCH-SK-002 protects kernel independence through declared/observed paths even with relaxed allowlists. ARCH-SK-003 guards forbidden infrastructure/internal imports in the kernel public source using existing governance findings; it does not claim full semantic analysis of arbitrary annotations.

Tests cover construction, validation, canonicalization, equality/hash, cross-type rejection, immutability, copies, fixed-length/version/variant boundaries, string-subclass normalization, safe parsing, standard UUIDv4 input compatibility, JSON scalar round trips, invalid JSON values, ownership and forbidden dependencies. The executable contract test `test_demo_valid_round_trip_and_invalid_input` is the SK-01 demo.

SK-01 also renames the source CLI helper to `scripts/platform_cli_launcher.py`: the previous `scripts/platform.py` shadowed Python's standard `platform` module when scripts was on PYTHONPATH, breaking standard `uuid` imports. Source launchers also put the standard-library path ahead of tooling helper paths, preventing helper files from shadowing foundational imports. `bin/platform`, `python -m platform_cli` and root development aliases are preserved; the helper path and its documentation/tests are updated.

Generation/registries, Namespace, QualifiedName, SemanticElement, semantic versions, references, persistence/compiler/runtime behavior and multi-format compatibility remain deferred. This early contract requires an explicit migration decision before changing prefix/layout/accepted versions. Next: SK-02 Namespace, then SK-03 QualifiedName.
