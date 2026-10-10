# SK-08: Semantic References

## Existing state and reference taxonomy

SK-01..07 supply stable identity, Namespace, QualifiedName, specialized SemanticContextRef, open Kind, numeric SemanticVersion, the five-property SemanticElement Protocol and exact ElementVersionRef. Production source inspection found no temporary raw string/name target-reference APIs in other modules to migrate: those modules still expose foundation boundary contracts. Their module/dependency identifiers and CLI release strings are not semantic element references. No unrelated refactor is needed.

Reference intent is explicit in the public type rather than guessed from arbitrary text:

| Concept | Contract | State and meaning |
| --- | --- | --- |
| Identity value | SemanticElementId | Existing stable identity value |
| Identity reference | ElementRef | SK-08: points to a semantic definition by stable identity, no version pinned |
| Exact version reference | ElementVersionRef | Existing SK-07: identity plus one required exact SemanticVersion |
| Meaning-context reference | SemanticContextRef | Existing specialized intent; not an alias for ElementRef |
| Symbolic authoring reference | Future Authoring/Canonical contract | Deferred; may carry a QualifiedName or relative source spelling |
| Resolved reference/result | Future Compiler/Resolution contract | Deferred; may associate a typed coordinate with a loaded definition and diagnostics |

There is no base reference hierarchy, optional version field or generic Reference<T>. Runtime class types do not define semantic categories or wire contracts.

## ElementRef public contract

`semantic_kernel.public.ElementRef` is a frozen slots dataclass with exactly one required field, `element_id: SemanticElementId`. Construction/from_id retain an already validated identity without reparsing, loading or selecting a version. `parse` delegates all scalar syntax/canonicalization to SemanticElementId; `try_parse` returns None only for expected ElementRefError diagnostics. `str` returns the canonical ID. Typed equality/hash depend on the ID; references with different IDs differ. No ordering is defined.

```python
from semantic_kernel.public import SemanticElementId, ElementRef, ElementVersionRef, SemanticVersion

identity = SemanticElementId.parse('sem_550e8400-e29b-41d4-a716-446655440000')
logical_target = ElementRef.from_id(identity)
assert logical_target.element_id is identity
assert ElementRef.parse(str(logical_target)) == logical_target
exact_target = ElementVersionRef(identity, SemanticVersion.parse('2.1.0'))
assert logical_target != exact_target
```

Identity-pinned means **which stable semantic definition**, not an instruction to choose latest/current/compatible. There is no version, range, selector, expected kind, name hint, context, namespace, import/alias environment, tenant, source location, permission, registry or loaded object in ElementRef. A syntactically valid unknown identity is still a valid value; construction proves neither existence nor access nor target category.

ElementVersionRef remains unchanged: two required typed fields, equality/hash across ID and version, human ID@version text and structured JSON. It is the coordinate to prefer for future exact application locks, artifact manifests, migration endpoints and provenance. Exact pinning alone proves no content integrity, existence, compatibility or reproducibility; immutable publication and compiler governance are future work. No implicit conversion chooses a version or drops one. A caller deliberately discarding the pin can explicitly construct `ElementRef.from_id(exact_target.element_id)`; no new projection helper is needed today.

SemanticContextRef is retained unchanged. Its context intent is distinct, even where it shares ID syntax with ElementRef; neither validates loaded target kind. The root SemanticElement still has only id, qualified_name, context, kind and version. SK-08 adds no collection or reference property to the root.

## Names, evolution and resolution boundary

QualifiedName is a canonical name, not a stable reference and not automatically an identity. `sales.Customer`, `Customer`, aliases, relative names and name@version spellings are rejected by ElementRef parsing; there is no namespace interpretation or hidden lookup. A rename from sales.Customer to crm.Customer, context move or version evolution leaves the identity reference unchanged while exact version references differ when version changes. Test-only immutable definition snapshots demonstrate this without any registry.

Future source authoring may retain symbolic spelling/source location. External parsing then namespace/import/alias resolution and symbol lookup can produce a typed ElementRef. External version selection, when required, can produce ElementVersionRef for canonical models, semantic IR or artifacts. These are separate stages and contracts; an identity coordinate is not itself a loaded/resolved definition. SK-08 implements only the stable reference value, not that pipeline. Compiler/runtime consumers should eventually use explicit typed canonical references rather than reinterpret raw authoring names.

Definition references are not business/runtime instance references: ElementRef does not denote Customer ACME, SalesOrder 1001, WorkflowRun or AgentRun. It is not an ORM navigation/FK, URL, runtime pointer/service locator, authorization token or tenant key. Projection layers may represent it differently without changing identity semantics. A reference is also not a RelationshipDefinition, import or package dependency; relationship direction/cardinality/ownership and dependency semantics belong to their own future contracts.

## Wire convention and diagnostics

Explicit ElementRef JSON mapping follows existing scalar identity/context conventions:

```json
{"target":"sem_550e8400-e29b-41d4-a716-446655440000"}
```

Exact target mapping retains SK-07 without redesign:

```json
{"target":{"elementId":"sem_550e8400-e29b-41d4-a716-446655440000","version":"2.1.0"}}
```

JSON scalar fields cannot themselves distinguish ElementRef, SemanticElementId and SemanticContextRef. The containing API/schema must declare the field's intent and explicitly invoke the corresponding parser. No generic string decoder guesses type, no serializer framework enters Kernel, and automatic json.dumps of an unmapped reference raises TypeError. Test-only boundary mappings exercise scalar/nested round trips, invalid data and exact structured regression.

| Code | Meaning |
| --- | --- |
| SEM-REF-001 | Missing typed ID, or missing/empty/all-whitespace parsed scalar |
| SEM-REF-002 | Wrong typed ID value or wrong parsed scalar type |
| SEM-REF-003 | Malformed semantic identity syntax, including names and versioned/selecting text |

ElementRefError exposes code/message and, for delegated parse errors, identity_code with the original exception cause. Diagnostics retain no rejected input and explain the expected SK-01 UUIDv4 syntax. Missing positional constructor arguments use ordinary TypeError. Unknown targets/permissions are future resolver/policy errors, never value-object diagnostics. Unexpected implementation errors propagate through try_parse.

## Architecture, verification and future work

Kernel remains stdlib-only and has zero observed module dependencies. ARCH-SK-002/003 and existing public API/import/dependency Fitness rules protect resolver/registry/runtime/compiler independence. No new duplicate Fitness rules are added; targeted actual shape/ownership/source-use tests protect the single ID field, distinct exact fields without defaults, small public API, identity-only primitive use and absence of resolution state. Tests do not claim arbitrary alias/generated-source inference or full static type checking; no external type checker was run.

Executable `SemanticReferenceContractTests.test_demo_identity_pinned_version_pinned_and_name_without_resolution` demonstrates identity reference with no pinned version, exact 2.1.0 reference and the independent sales.Customer name with no resolution. See [ADR-0015](../architecture/decisions/ADR-0015-semantic-reference-model.md), [verification](../architecture/sk08-verification.md) and [SK-07](semantic-version.md).

Deferred: SymbolicElementRef, UnresolvedReference, ResolvedReference/ResolutionResult, namespace/import/alias resolution, ReferenceResolver, version selection/ranges, TypeRef/ActionRef/EventRef, InstanceRef, registries, loaded model lookup, graph/relationship/dependency semantics and serialization frameworks. Future publishers/resolvers must preserve immutable exact coordinates and handle visibility/collisions/authorization. ContextDefinition bootstrap ownership remains the ADR-0012 gate. Next: SK-09 Primitive Type System, then SK-10 Facet Base Contract and SK-11 Diagnostics Model.
