# MOD-03 — Source Location Tracking

Date: 2026-10-10 (Asia/Riyadh). Implementation uses Python. Behavioral status: **NOT_RUN — DEFERRED / NOT VERIFIED**. No test code or parser/loader examples were executed.

## Existing contracts and stack assessment

MOD-01 is the existing immutable authoring schema/structural validator. MOD-02 owns dedicated ModelSourceId, explicit sources, providers/decoders and ordered loading. Its SourcePosition(line,column) and source-associated loading diagnostic are reused, not replaced. General SK-11 diagnostics/SourceLocation have not been implemented in this repository; integration uses the actual provisional ModelLoadDiagnostic seam and preserves nested AuthoringSchemaDiagnostic code/cause/path/related_path. This is not a claim that SK-11 is complete. TYPE-01/TYPE-08/full SK-09 also remain incomplete and are not fabricated for source tracking.

The repository requires Python 3.11+; the current local interpreter metadata is Python 3.12.14. Dependency inspection found PyYAML 6.0.3 and no installed Django/djangorestframework. There is no existing Django project, HTTP model-loading endpoint, view or serializer to extend. No Django/DRF package upgrade, HTTP endpoint, API transport, ORM model, database, authentication or filesystem-download capability is added. Future HTTP exposure must use the approved Django/DRF adapter boundary. All value objects remain pure Python.

Core location values and existing loader contracts share model_loader.public because they reuse its source identity. No separate competing identity, reverse domain-to-tooling dependency, new module or manifest/profile relaxation is introduced. Parser integration remains in input tooling, approved only for PyYAML at this path. No semantic element/type/reference gains physical source fields.

## Coordinates, spans and source identity

SourcePosition is frozen/slotted with line>=1, column>=1 and optional offset>=0. Offset is a zero-based **Python Unicode string character index**, not a UTF-8 byte count, grapheme index or JavaScript UTF-16 unit. A supplementary character occupies one offset/column character; combining characters remain separate. Exact integer checks reject bool and invalid scalars. Coordinates with known offsets must satisfy the minimum possible preceding character count. Old two-argument construction remains valid with offset=None.

JSON coordinates follow the stdlib parser's newline convention: LF advances the line; CRLF contains both source characters and advances at LF; a standalone CR is whitespace on the same line. YAML coordinates retain pure-Python SafeLoader marks, including its native YAML line-break rules. Formats are explicitly identified by source metadata; do not conflate differing native newline conventions. Offsets in both adapters are Python string indexes into the unchanged acquired text. No universal newline translation is performed by file acquisition.

SourceSpan is half-open [start,end): punctuation/quotes belong to the parser's actual token/node span; end is exclusive. Zero-width spans are valid for syntax/insertion positions. Endpoints must be canonical SourcePosition values and have nondecreasing line/column order. When both offsets exist they must be nondecreasing, agree with coordinate equality/inequality and, on the same line, have exactly the column distance. Unknown endpoint offsets remain absent; they are never calculated by guessing. A standalone span cannot certify coordinates against unavailable raw text.

SourceLocation is the existing ModelSourceId plus span. It conveys physical authorship position, not semantic identity, context, authority, ownership or a provenance graph. Sources remain caller-identified. No filesystem mtime, random ID or semantic ID is used for location identity.

## Node paths and immutable indexing

SourceNodePath stores a defensive tuple of string tokens, with RFC 6901-style pointer rendering/parsing:

| Meaning | Pointer |
| --- | --- |
| Document root | empty string `""` |
| Empty-string property | `/` |
| Literal slash in key | `~1` inside token |
| Literal tilde in key | `~0` inside token |
| Definition declaration | `/definitions/0` |
| Field declaration | `/definitions/0/facets/0/fields/2` |
| Exact precision literal in current Mini Sales | `/definitions/0/facets/0/fields/2/constraints/values/1/value` |

Only ~0/~1 escapes are accepted; no percent-decoding, URI fragment, dot traversal or implicit root `/` interpretation. Array indices render decimal string tokens according to the actual decoded array; numeric object keys remain object keys. Paths address one source snapshot, not stable semantic identity across edits. Conversion from AuthoringSchemaPath is explicit and preserves the existing array/property coordinates; it does not reinterpret authoring meaning.

SourceLocationEntry holds a node path, value/container location, OBJECT/ARRAY/SCALAR kind and optional separate property key location. Root/array members have no key location. Property key/value spans remain distinct. No mutable parser AST node is retained.

SourceLocationIndex belongs to one source ID and optionally identifies exact acquired text with lowercase SHA-256 of UTF-8 text. It defensively copies entries into an immutable sorted tuple and a private MappingProxyType over an owned map. Duplicate identical entries are idempotent; conflicting duplicate paths, different source IDs and key locations on known non-object parents are rejected. Enumeration is lexicographic by escaped pointer (root first; `/10` before `/2`); it is deterministic rather than claimed to be author order. Lookup is keyed by typed SourceNodePath:

- `find(path)` returns value/container location or None.
- `find_key(path)` returns property key location or None.
- `contains(path)` and `entry(path)` provide typed presence/full entry.
- `list_locations()` returns immutable entry tuples.

SourceLocationTracker.build consumes explicit typed parser metadata and optionally original source text for its digest. It does not parse, validate types or resolve names. locate returns exact key/value location; with containing=True it may return a reliable nearest parent object/array when the requested node is absent. Parent fallback is an actual broader authored span, not a synthesized insertion token. None index or missing node with no authorized fallback yields None, never an artificial 1:1 coordinate. A generated document can omit location metadata or use an empty index with no digest.

## JSON location adapter

The existing JsonModelDecoder is now location-aware while keeping strict JSON vocabulary and MOD-02 failures. A private narrow adapter instruments **stdlib json.JSONDecoder**, **json.scanner.py_make_scanner**, **json.decoder.JSONObject/JSONArray** and **scanstring**. The existing stdlib parser remains responsible for grammar, escaping, numeric decoding, whitespace, punctuation and syntax failures. Each parser value scan supplies exact start/returned-end offsets; container callbacks retain ordered child records. Property keys use stdlib scanstring at the member coordinates bounded by those already parsed children. No raw matching-string search, generic manual JSON grammar, second differently configured document parser or dependency is added.

Parsed values and spans come from the same scan. Projection converts parser metadata to typed paths, locations and the retained legacy positions tuple. It covers root, all containers, array members, property values and property keys, including repeated names in distinct nested objects and escaped equivalent spellings. Duplicate keys fail at the conflicting key token with the first key as related location. Syntax failures preserve stdlib error offsets as zero-width spans, including EOF. No synthetic full malformed-document index is promised.

Depth preflight and parser-time node/key limits remain explicit; decoded tree limits still apply. Non-finite numbers and invalid Unicode strings/keys fail with available token spans. Comments, trailing commas, multiple values and executable expressions remain invalid; no YAML fallback occurs. The adapter relies on stdlib parser callback interfaces beyond the public JSONDecoder surface: supported Python 3.11/3.12/3.13 behavior remains a deferred compatibility requirement. Unexpected implementation defects are not swallowed as valid inputs. This risk is documented rather than hidden by a new parser dependency.

## YAML location adapter

Keep pinned PyYAML 6.0.3, pure-Python SafeLoader and the approved strict YAML 1.1 policy unchanged. The existing event preflight and node projection now preserve native start_mark/end_mark line/column/index for containers, scalars and property keys. The exact projection supplying candidate values supplies the index, so no separately read source or incompatible parse is used. Key spans are distinct from associated value-node spans; quotes, block scalar indicators/content, flow/block collections and comment/whitespace boundaries follow the parser's original node marks. Semantic scalar values can differ from lexical text length; spans always use marks, not decoded string lengths.

All explicit tags, anchors, aliases, merge keys and multiple documents remain rejected. Event errors retain event spans; duplicate key errors retain second/first key spans; syntax errors with problem_mark retain a zero-width parser point. Unsupported implicit scalars/keys retain actual node spans where available. Rejected aliases never acquire fabricated expansion locations. No YAML native AST escapes the adapter. A comment-only stream without a root node has no invented root location. Loader disposal/preflight generator cleanup remain intact.

## Compatible loader and diagnostic extensions

All added fields have defaults and are appended to existing contracts:

- SourcePosition.offset defaults None, retaining line/column callers.
- SourceDecodeResult.locations defaults None, retaining legacy positions/decoder constructors.
- LoadedAuthoringDocument.locations defaults None, retaining two-argument generated/legacy construction.
- ModelLoadDiagnostic.source_location and related_locations default None/empty; original source, stage, code, position, schema diagnostic and related input index remain.

The loader passes a decoder's index to the successful immutable document. An index must have the exact source ID; when it declares a digest, the loader verifies it against the exact bounded acquired text. Built-in adapters always digest their own parsed text. Injected adapters without an index/digest remain compatible but cannot claim certified physical alignment; the application owns their contract. No location cache or reparsing file read is introduced.

Diagnostic precision is deterministic:

| Concern | Location policy |
| --- | --- |
| Invalid expression/literal/facet kind | Exact MOD-01 path value span |
| Duplicate ID/name/constraint | Conflicting declaration value span plus original related_path span |
| Unknown property | Exact property key span |
| Missing property | Nearest actual containing object/array span |
| Invalid decoded root | Actual parsed root span |
| JSON/YAML syntax | Reliable parser point, represented by zero-width span |
| Source acquisition or generated origin without marks | Explicit absence |

The legacy position is populated from source_location.span.start when available and validated for consistency if supplied. Existing MOD-01 diagnostic codes, cause codes, path and related_path are retained unchanged. Legacy decoders with only positions use those exact coordinates without inventing spans. Related locations are immutable and may identify a different source for a future explicitly governed diagnostic; primary location must match its source. No competing generic Diagnostic model, semantic validator or full SK-11 framework is implemented.

## Mini Sales usage (documented, NOT RUN)

Reuse existing JSON/YAML without changing identities, constraints or examples. Current MOD-01 constraints are ordered declarations rather than the illustrative keyed precision map:

| Construct | SourceNodePath pointer |
| --- | --- |
| Customer | `/definitions/0` |
| Customer DataFacet | `/definitions/0/facets/0` |
| name field | `/definitions/0/facets/0/fields/0` |
| active expression | `/definitions/0/facets/0/fields/1/type` |
| creditLimit field | `/definitions/0/facets/0/fields/2` |
| minimum declaration | `/definitions/0/facets/0/fields/2/constraints/values/0` |
| precision declaration | `/definitions/0/facets/0/fields/2/constraints/values/1` |
| scale declaration | `/definitions/0/facets/0/fields/2/constraints/values/2` |

```python
# Illustration only: do not execute while testing is deferred.
from model_loader.public import ModelLoader, ModelSourceId, FileModelSource, SourceNodePath
result = ModelLoader().load(FileModelSource(
    ModelSourceId('mini-sales'), 'yaml', 'examples/authoring/mini-sales.yaml'))
if result.loaded is not None and result.loaded.locations is not None:
    precision = result.loaded.locations.find(SourceNodePath.parse(
        '/definitions/0/facets/0/fields/2/constraints/values/1/value'))
    # Coordinates are obtained from the actual parser, never hardcoded.
```

See [ADR-0025](../architecture/decisions/ADR-0025-source-location-tracking.md), [deferred specification](../../test-archive/MOD-03/MOD-03-deferred-tests.md), and [static record](../architecture/mod03-verification.md). Stop at MOD-03; no MOD-04 or semantic applicability operation is introduced.

Implementation references inspected, not executed as tests: [CPython JSON decoder](https://github.com/python/cpython/blob/3.12/Lib/json/decoder.py), [CPython scanner](https://github.com/python/cpython/blob/3.12/Lib/json/scanner.py), [PyYAML marks/nodes](https://pyyaml.org/wiki/PyYAMLDocumentation). Current source files and local stdlib source are the implementation authority.
