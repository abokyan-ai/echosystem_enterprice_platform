# TYPE-07: Type Registry

## Existing architecture and scope

The repository is a Python 3.11+ standard-library workspace, not a TypeScript project. TYPE-07 therefore uses its established frozen dataclass, snake_case and public.py conventions rather than introducing a second language/toolchain. Registry contracts live in model_core.public; model-core depends only on semantic_kernel.public. No module, third-party package, CLI command or adapter is added.

Kernel supplies distinct value equality/hash for SemanticElementId, QualifiedName, SemanticContextRef and ElementVersionRef. SemanticVersion already has numeric major/minor/patch ordering (`order=True`); registry enumeration reuses it. ElementRef is identity-only, whereas ElementVersionRef pins exactly one version. Namespace and name case remain unchanged. The registry is not a global namespace authority.

Production TYPE-01 and SK-11 remain absent. Actual input/output is the existing TypeDataComposition(host, data) seam, not an invented TypeDefinition interface. The known definition consists of five typed root properties and optional canonical DataFacet, with ordered fields, TypeRef and constraints. Additional host members are outside this provisional registration contract; equality is complete for the supported seam, not a promise about future facets. Reconcile full TYPE-01 before registering a richer definition. The TYPE-05 primitive prerequisite does not complete the full unseen SK-09 specification.

One TypeRegistry snapshot belongs to one explicit SemanticContextRef. Registration rejects a different context, even for an equal ID. Within that scope, a name is owned by one ID across all registered versions. Separate registries may use the same name in distinct contexts. Name uniqueness per context is a local registry policy, not a newly defined universal Kernel rule.

## Actual API

| Operation | Result / semantics |
| --- | --- |
| `TypeRegistry(context)` | Empty immutable context-scoped snapshot |
| `register(TypeDataComposition)` | TypeRegistrationResult containing a new snapshot on insertion; same snapshot on duplicate/failure |
| `find_by_id(SemanticElementId)` | Tuple of all versions, ascending SemanticVersion order |
| `find_by_version(ElementVersionRef)` | Exact TypeDataComposition or None; no fallback |
| `find_by_qualified_name(QualifiedName)` | Tuple of entries recorded under exactly that name, ascending version order |
| `list_versions(SemanticElementId)` | Immutable ordered tuple of SemanticVersion values |
| `contains(ElementVersionRef)` | Whether that exact identity/version is registered |
| `entries` | Immutable tuple ordered by canonical ID scalar, then numeric version |
| `find(ElementRef)` | Existing TypeLookup contract: root SemanticElement or None when zero/one version exists; explicit ambiguity exception for several |
| `bind_versions(tuple/list[ElementVersionRef])` | TypeRegistryLookup implementing the unchanged TypeLookup with one explicitly selected version per visible identity |

Queries require canonical typed values; invalid raw strings/None/wrong reference variants raise TypeError as API programming errors. Missing exact/broad lookups return None/empty tuple. No latest/highest/default/active version selection exists.

## Registration and collisions

Registration performs only registry structural/index invariants. It does not invoke TypeValidator or require semantic references to be resolved. Registering a structurally valid declaration with an inapplicable field constraint is allowed; TYPE-06 judges it separately.

The outcome is REGISTERED, ALREADY_REGISTERED or REJECTED. `is_success` is derived; successful results have no failure diagnostics. Failures are atomic and return the original registry. Checks run in deterministic order: contract/root shape, kind, scope, canonical facet snapshot, exact duplicate/conflict, name ownership.

| Case | Behavior |
| --- | --- |
| Equal ID/version and equal complete supported registration content | ALREADY_REGISTERED, same snapshot |
| Equal ID/version but different name, data presence, field ID/name/order/type or constraints | DUPLICATE_CONFLICT; never overwrite |
| Equal ID, different version | New entry, subject to scope/name ownership |
| Different ID, same exact name in one scope, even at different versions | QUALIFIED_NAME_COLLISION |
| Same ID, another name at another version | Allowed explicit historical evolution; each version keeps its name |
| Missing exact version | None; never use another version or name |
| Non-type element | UNSUPPORTED_ELEMENT_KIND |
| Different context | SCOPE_MISMATCH |

Reliable equality comes from a frozen five-property registry host capture and existing canonical dataclass equality for DataFacet/FieldDefinition/TypeRef/constraints. Separately constructed equal inputs are idempotent; object identity, JSON serialization and canonical hashes are not used. None data differs from DataFacet(()). Field order remains content; constraint input order is already normalized by FieldConstraintSet.

Rename rules are independent of registration order: historical versions may be backfilled after a newer renamed version. This does not infer the current name or enforce a chronological migration policy. A former name stays owned while its historical entry remains in this snapshot. It never becomes an alias for the renamed version, and cannot be reused by another ID here. No redirects, alias chains, migration or removal operation exists.

## Real snapshot immutability and indexes

Three private mapping proxies index the same canonical entries: exact reference, ID -> version tuple, and name -> version tuple. A successful registration builds/sorts all indexes locally and publishes a fresh snapshot; old snapshots share only immutable entries, not mutable maps. Failed registration cannot partially change an index.

A Protocol host may be externally mutable at the TYPE-03 seam. Registry registration captures its five properties once into a private frozen root, rather than retaining that mutable host or claiming full TYPE-01 implementation. Known canonical immutable facets are safely shared. Mutable/noncanonical facet, field, reference and constraint subclasses are rejected; nested namespace/context identity subclasses are also rejected. No arbitrary deep-clone framework is added. As with all frozen Python contracts, deliberate object.__setattr__ bypasses are outside supported use.

Public collections are tuples and mapping proxies never escape as writable maps. Caller-retained list inputs cannot mutate facets or bound-view selections. Registry equality compares context and exact supported contents, not insertion order. Enumeration never relies on incidental dict order: maps are built after explicit ID/version sorting. Rebuild cost is O(n log n) per insertion; this intentionally favors correctness over speculative persistent-index machinery.

## Unchanged TYPE-06 TypeLookup integration

TypeLookup declares only `find(ElementRef) -> SemanticElement | None`. It cannot represent ambiguity or an exact-version request; this is the precise existing boundary limitation. It must remain an unambiguous read-only view.

A zero/one-version registry can be passed directly. Calling its find for a multiversion identity raises TypeRegistryAmbiguityError (TYPE-REG-006), retaining all exact references in numeric order. It never misreports ambiguity as missing, and the validator propagates this orchestration error rather than choosing a version.

For multiversion snapshots, explicitly bind a TypeRegistryLookup. Each selection is an existing ElementVersionRef, at most one per ID; duplicates, unknown versions and malformed selections are programming errors at binding. The view is selected-only: unselected identities are absent, even if the backing registry has one version. There is no hidden fallback. Selections are copied and ordered by ID. Old views remain bound to their immutable old snapshot when another snapshot is created.

This is a concrete implementation of the existing Protocol, not a competing lookup abstraction. No TYPE-06 signature is changed, no competing reference type is introduced, and no backward-compatible extension is required for the selected-view solution. A future explicit ambiguity result on the generic lookup would require a separately agreed contract change.

Self/mutual references are finite ID lookup operations. Registration neither traverses references nor recursively validates targets; invalid target constraints do not cause validation of another definition to recurse.

## Diagnostics

SK-11 does not exist to import. TypeRegistrationDiagnostic is a narrow provisional registration result, reusing TypeValidationSeverity.ERROR and TypeValidationPath instead of creating a general diagnostic framework. It preserves exact ElementVersionRef, QualifiedName and SemanticContextRef when root coordinates are valid. It contains no rejected raw object, infrastructure details or instance data.

| Code | Category |
| --- | --- |
| TYPE-REG-001 | INVALID_REGISTRY_ENTRY |
| TYPE-REG-002 | UNSUPPORTED_ELEMENT_KIND |
| TYPE-REG-003 | SCOPE_MISMATCH |
| TYPE-REG-004 | DUPLICATE_CONFLICT |
| TYPE-REG-005 | QUALIFIED_NAME_COLLISION |
| TYPE-REG-006 | Ambiguous direct TypeLookup call; use explicit bound view |

Each registration failure has one first-applicable diagnostic in documented precedence. Existing Kernel constructors and typed query guards handle invalid references; no new reference parser or INVALID_REFERENCE result hierarchy is added. Unified Diagnostic/SemanticPath/SourceLocation integration remains pending SK-11.

## Executed Mini Sales contract example

The contract test reuses the existing typed_customer fixture: Customer name:string/max-length 200, active:boolean, creditLimit:decimal/minimum 0/precision 18/scale 2, with explicit presence/nullability.

```python
old = typed_customer()  # existing test fixture, Customer@1.0.0
new = TypeDataComposition(
    replace(old.type_definition, version=SemanticVersion(1, 1, 0)), old.data)
a = TypeRegistry(old.type_definition.context)
b = a.register(old).registry
c = b.register(new).registry
old_ref = ElementVersionRef(old.type_definition.id, SemanticVersion(1, 0, 0))
new_ref = ElementVersionRef(old.type_definition.id, SemanticVersion(1, 1, 0))
assert c.find_by_version(old_ref).type_definition.version == old_ref.version
assert c.find_by_version(new_ref).type_definition.version == new_ref.version
assert len(c.find_by_id(old.type_definition.id)) == 2
assert a.entries == ()
lookup = c.bind_versions([old_ref])  # explicit choice by caller, never inferred
```

Sales/Address integration, Employee.manager self reference and A.b/B.a mutual references are executable tests. They use production TypeRegistry and TypeRegistryLookup with the provisional current composition seam; test hosts are not claimed to be full production TYPE-01.

## Deferred work

TYPE-08 Semantic Instance Contract is the next requested stage; it is not implemented here. Full TYPE-01/SK-11/SK-09 reconciliation, instance storage/validation, persistence, APIs/UI, authoring parsing/imports/aliases, compiler/runtime, latest/version preferences, compatibility/migrations, inheritance, ValueType propagation, relationship traversal, tenant authorization and remote/global registries remain separate.

See [ADR-0022](../architecture/decisions/ADR-0022-context-scoped-immutable-type-registry.md) and [verification](../architecture/type07-verification.md).
