# SK-06: Semantic Element Kinds

`semantic_kernel.public.SemanticElementKind` is an immutable, strongly typed open identifier for the semantic category of a first-class definition. It is not a closed enum, unchecked string, runtime class, identity, qualified name, meaning context, version or serializer implementation. Kernel validates lexical form and preserves the value without knowing compiler support, handlers, schemas, ownership or permissions.

## Canonical syntax and scope

Each ASCII lowercase kebab-case segment matches `[a-z][a-z0-9]*(?:-[a-z0-9]+)*`. A value has one or more segments separated by `.`. Examples: `action-definition`, `acme.route-definition`, `industry.healthcare.protocol-definition`. Digits may follow the initial letter; every hyphen must separate nonempty groups. Uppercase, underscores, whitespace, Unicode/control characters, leading/trailing/repeated hyphens, empty dot segments, slashes, colons, wildcards, quotes and version suffix syntax are rejected. No trim, case folding, spelling repair or numeric ordinal conversion occurs. No arbitrary length/depth limit is added.

Core values use the agreed short unqualified identifiers. Extension publishers should use scoped identifiers such as `acme.route-definition`; their registration/ownership governance must enforce this later. The lexical parser deliberately also preserves unknown unqualified identifiers for future platform vocabulary. Reserving the unqualified publication scope for the platform is a governance rule, not a Core allowlist in parse. This separates lexical validity from known/supported membership and permits older inspection tooling to retain future values. No publisher registration API exists here, and scopes do not prove publisher/package identity or authority.

## Public contract and constants

```python
from semantic_kernel.public import SemanticElementKind, SemanticElementKinds

core = SemanticElementKind.parse("action-definition")
assert core == SemanticElementKinds.ACTION_DEFINITION
assert SemanticElementKinds.is_core(core)
custom = SemanticElementKind.parse("acme.route-definition")
assert not SemanticElementKinds.is_core(custom)
assert str(custom) == "acme.route-definition"
assert SemanticElementKind.parse(str(custom)) == custom
assert SemanticElementKind.try_parse("Action Definition") is None
```

Public value API: constructor, `parse`, `try_parse`, frozen `value`, `str`, typed equality and hash. Equal values have equal hashes and work as collection keys; raw strings remain distinct. There is no ordering, class discovery, dispatch, registry lookup or I/O. Safe parsing catches only SemanticElementKindError; unexpected implementation failures propagate. Canonical values are preserved exactly, including unknown kinds, never collapsed to Unknown/Other/Custom. Python collection hashes are process-local, not stable wire fingerprints.

`SemanticElementKinds` is an immutable catalog instance exposing typed uppercase constants, immutable `ALL` tuple and `is_core(kind)`. The private catalog implementation is not another public primitive or registry. Canonical Core literals occur once in its typed fields; `ALL` references those fields rather than duplicating strings. Membership answers only whether the value is in the currently published Core set, not validity, compiler support or authorization.

| Typed constant | Canonical value |
| --- | --- |
| TYPE_DEFINITION | type-definition |
| RELATIONSHIP_DEFINITION | relationship-definition |
| BEHAVIOR_DEFINITION | behavior-definition |
| CAPABILITY_DEFINITION | capability-definition |
| ACTION_DEFINITION | action-definition |
| EVENT_DEFINITION | event-definition |
| PROCESS_DEFINITION | process-definition |
| RULE_DEFINITION | rule-definition |
| POLICY_DEFINITION | policy-definition |
| CONTRACT_DEFINITION | contract-definition |
| COMPOSITION_DEFINITION | composition-definition |
| EXTENSION_DEFINITION | extension-definition |

No SemanticType/DocType/business/persistence/UI/transport/AI shortcuts are added to this Core list. A scoped future value may be lexically valid without having defined or supported semantics here. Published canonical values are long-lived wire contracts: do not silently repurpose them or rename them without an explicit migration strategy. Contract versioning is independent of the identifier; a lexically valid `v2` segment/suffix is not assigned version semantics by Kernel.

## Diagnostics, validity and support

SemanticElementKindError is a ValueError with code, message and optional zero-based `segment_index`, without retaining or echoing rejected input. SEM-KIND-001 means None/empty/entirely whitespace input. SEM-KIND-002 means a non-string representation or malformed segment. A malformed segment diagnostic explains the grammar and failing index. The compact error vocabulary uses these two codes; no unknown-kind error is emitted.

`Action Definition` is invalid -> SEM-KIND-002. `acme.route-definition` is valid and preserved, even when an eventual compiler has no handler. An unsupported-kind diagnostic belongs to Compiler/Application support validation, not the value constructor. Parsing never calls Core membership, so the known catalog cannot become a closed-world gate.

## SemanticElement integration

The root now has four required read-only typed properties: id, qualified_name, context and kind. Only kind is added by SK-06; no default, optional kind, version, metadata or facets are added. All test fixtures and typed consumers are updated to pass/preserve it explicitly. Missing/raw kinds are rejected by test fixture construction, while the Protocol itself remains a static contract rather than a runtime validator. Old structural implementations must provide the new property; this planned early API change is explicit in ADR-0013.

Both Core and custom kinds can use the same test definition class. Classification is not inferred from class/package names, semantic names, ID prefixes or contexts. No actual production Type/Action/custom definition, factory, dispatcher or registry is introduced.

## Serialization, forward compatibility and demo

External wire mapping remains scalar text outside Kernel:

```python
import json
encoded = json.dumps({"kind": str(custom)})
assert encoded == '{"kind": "acme.route-definition"}'
assert SemanticElementKind.parse(json.loads(encoded)["kind"]) == custom
```

Default JSON serialization requires explicit mapping. Numeric enum ordinals and object-shaped wrappers are rejected by parse. Contract tests round-trip all Core values and explicitly preserve unknown scoped and future unqualified values through deserialize/store/display/compare/reserialize. This models inspection-tool preservation without claiming compiler support or implementing a polymorphic model loader.

`SemanticElementKindSerializationTests.test_demo_core_custom_and_invalid_kind` checks Core membership, custom preservation and Action Definition -> SEM-KIND-002. Root consumer tests demonstrate typed Core/custom kinds in test-only definitions. An inline verification demo prints compiler support NOT EVALUATED BY KERNEL.

## Architecture and deferred work

The Kind primitive uses only existing dataclasses/re facilities and is independent of the ID, naming and context peers. Root contract composes the value. Kernel still imports only dataclasses/re/typing and has no observed non-Kernel module dependency, new module or lifecycle registration. Existing ARCH-SK-002/003 and ARC-03 rules suffice for infrastructure neutrality. Targeted contract tests verify Kind is not an Enum, valid unknown values survive and SemanticElement.kind returns SemanticElementKind; no broad enum regex or artificial duplicate Fitness rule is added.

See [ADR-0013](../architecture/decisions/ADR-0013-open-semantic-element-kind.md) and [verification](../architecture/sk06-verification.md). Future registration must govern Core reservations, scoped publishers/collisions and support handlers. Deferred: Kind Registry, compiler dispatch, polymorphic model loading, package-provided registration, kind-specific schemas, versioning and concrete definitions. Context-definition ownership remains the SK-05 decision gate. Next: SK-07 Semantic Version Reference, then SK-08 Semantic References.
