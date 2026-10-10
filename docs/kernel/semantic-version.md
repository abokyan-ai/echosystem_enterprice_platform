# SK-07: Semantic Version Reference

## Ownership and minimal strategy

`semantic_kernel.public.SemanticVersion` is a platform-owned immutable value for one semantic definition's declared evolution coordinate. Existing identity, name, context and open kind primitives are reused. The workspace has no trusted version abstraction matching this concern; the CLI's `0.1.0` release string is a tooling/package version, not a semantic definition version. No dependency or module is added.

The v1 contract is deliberately minimal, SemVer-like **major.minor.patch**, not a claim to implement the full SemVer specification. Each component is a plain Python int in `0..9223372036854775807` (the non-negative signed 64-bit range). This portable ceiling avoids arbitrary-precision wire expectations and oversized integer conversion, while remaining far above practical version needs. Booleans, int subclasses, floats, strings and negative/overflowed components are rejected by the structured constructor. The parser checks ASCII grammar and bounds before conversion; it never silently overflows, trims, coerces or repairs.

Canonical syntax is three components matching `0|[1-9][0-9]*`, separated by dots. Accept `0.0.0`, `0.1.0`, `1.0.0`, `1.2.3`, `10.20.30`; reject `v1.0.0`, `01.0.0`, missing/extra components, whitespace, Unicode digits, negative numbers, suffixes and selectors. Zero versions have no automatic experimental policy. Prerelease identifiers and build metadata are deferred: there is no current requirement, and artifact build/provenance data belongs elsewhere. No version increment helpers are provided.

## Public contracts and use

```python
from semantic_kernel.public import SemanticElementId, SemanticVersion, ElementVersionRef

identity = SemanticElementId.parse('sem_550e8400-e29b-41d4-a716-446655440000')
version = SemanticVersion(2, 1, 0)
assert SemanticVersion.parse('2.1.0') == version
assert SemanticVersion.parse('1.9.0') < SemanticVersion.parse('1.10.0')
reference = ElementVersionRef(identity, version)
assert ElementVersionRef.parse(str(reference)) == reference
```

SemanticVersion exposes read-only `major`, `minor`, `patch`; structured construction, `parse`, `try_parse` and `str` all share validation. It stores numeric components, not a raw source string. Frozen slots prevent ordinary mutation. Equality/hash use all three numbers; natural ordering is lexicographic on the numeric tuple, so `1.10.0 > 1.9.0`. Comparisons with strings/tuples are not numeric version comparisons. Ordering is only order; it proves no compatibility, availability or adoption policy.

ElementVersionRef contains exactly two required fields: `element_id: SemanticElementId` and `version: SemanticVersion`. Typed construction preserves these already validated values without reparsing. Equality/hash combine both; a different ID or different version produces a different reference. There is no total ordering of references. Frozen references have no QualifiedName/name hint, context, kind, package or artifact field. No existence/kind validation, loading, resolution, registry or latest lookup occurs. It is an exact coordinate, never a query.

The human text form is `sem_<UUIDv4>@major.minor.patch`. SK-01 forbids `@` inside IDs, so exactly one delimiter is unambiguous. Text parsing delegates both primitives and preserves their diagnostics/cause; ID hex case uses SK-01 canonicalization. JSON should use named fields instead of the composite syntax.

## Identity and root integration

Identity is stable across renames, context moves and versions. Version is never embedded in SemanticElementId or QualifiedName. Two versions can share an ID and name while producing distinct ElementVersionRefs. Renaming an illustrative snapshot without changing ID/version leaves its reference equal; the reference intentionally cannot detect changed content. Production publication governance must prevent republishing changed meaning under the same ID/version. An exact coordinate is not a content hash, existence proof or reproducibility guarantee.

SK-07 adds only required read-only `version: SemanticVersion` to SemanticElement, giving five properties: id, qualified_name, context, kind, version. There is no optional version, implicit `1.0.0`, raw string or generic production definition. All test-only Type/Action implementations and shared consumers explicitly supply/read the fifth field. Python Protocol annotations do not enforce runtime types or immutability; concrete definitions own construction invariants and snapshot validation. No external static type checker was added or run. The existing ADR-0012 gate for ContextDefinition ownership still applies.

## Distinct version concerns and compatibility boundary

A SemanticVersion describes an individual semantic definition. Package/library/application/compiler releases, compiled artifact builds/provenance, deployment rollout versions, model-wide versions, API `/v1` projections, event envelopes/schema registries, database migrations and tenant configuration versions have different scopes. No implicit conversions or forced numerical correspondence exist. A future ContractDefinition/EventDefinition may itself have a SemanticVersion without equating it to transport protocol/schema registry numbering. These other abstractions are not implemented here.

A version number is a declared evolution coordinate, not proof of compatibility. Future model diff and contract analysis must inspect actual semantic changes. Major/minor/patch do not trigger automatic breaking/compatible/fix classification. No is_compatible_with, VersionRange, VersionSelector, migration plan, dependency selection, nearest/highest/latest lookup, package registry or runtime reproducibility engine is provided.

## Wire convention outside Kernel

SemanticVersion maps explicitly to the JSON scalar `"2.1.0"`. ElementVersionRef maps to:

```json
{"elementId":"sem_550e8400-e29b-41d4-a716-446655440000","version":"2.1.0"}
```

Callers parse both named fields through their own Kernel primitives and construct the typed reference. Missing fields are invalid, with no defaults. JSON converters are demonstrated by test-only boundary code in `tests/contracts/test_semantic_version_serialization.py`; no production serializer/framework is added to Kernel. That illustrative strict mapper rejects extra keys and preserves delegated primitive errors for invalid field values. Automatic json.dumps of either value fails until the caller explicitly maps it. Future adapters can adopt this wire contract with transport-specific diagnostics; object-level SemanticElement polymorphic serialization remains deferred.

## Diagnostics

| Code | Meaning |
| --- | --- |
| SEM-VER-001 | Missing/empty/all-whitespace parsed version |
| SEM-VER-002 | Wrong scalar type or noncanonical format; expected major.minor.patch, e.g. 1.0.0 |
| SEM-VER-003 | Invalid structured component or parsed overflow; zero-based component_index |
| SEM-VREF-001 | Missing typed element ID or empty ID in textual reference |
| SEM-VREF-002 | Missing typed version or empty version in textual reference |
| SEM-VREF-003 | Wrong typed components, malformed composite text or invalid delegated primitive |

Errors expose code/message; parsed reference errors additionally expose primitive_code and exception cause. Rejected input is not retained/echoed. Missing positional Python constructor arguments use ordinary TypeError. `try_parse` returns None only for its own expected diagnostics; unexpected implementation errors propagate.

## Architecture and demo

Existing ARCH-SK-002/003 and public/import/dependency Fitness rules protect Kernel infrastructure independence; all 44 rules remain unchanged. Targeted real architecture tests protect public ownership, exactly two typed reference fields, three numeric version fields, five root getters, the SemanticVersion return type and absence of resolution/compatibility helpers. These complement functional/negative tests, not a claim to infer arbitrary aliasing or semantic compatibility through AST analysis. No bootstrap/CLI registration or UI is needed for value primitives.

Executable demos are `ElementVersionRefTests.test_demo_exact_coordinate_numeric_order_and_diagnostic` and the updated `SemanticElementContractTests.test_demo`. They cover a 2.1.0 reference, numeric 1.9.0 < 1.10.0 and v1.0 -> SEM-VER-002. All prior behavior remains covered. See [ADR-0014](../architecture/decisions/ADR-0014-exact-semantic-version-reference.md), [verification](../architecture/sk07-verification.md). Next: SK-08 Semantic References, then SK-09 Primitive Type System.
