# MOD-02 — Model Loader

Implementation date: 2026-10-10. Behavioral status: **DEFERRED / NOT VERIFIED**.

## Assessment and ownership

MOD-01 accepts already decoded plain dict/list trees and projects them into immutable AuthoringModelDocument values. Its AuthoringSchemaValidator.validate API is the sole structural authority; MOD-02 supplies source text, format decoding and source associations. No candidate cast or second authoring schema is needed. Original schema diagnostic codes, cause codes, paths and related paths remain nested in loader diagnostics.

Repository-native Python 3.11+ is used, rather than introducing the prompt's illustrative TypeScript stack into a Python-only production analyzer. The existing Kernel/model-core/MOD-01 public contracts remain unchanged. SK-11's general diagnostics/SourceLocation contracts, TYPE-01, TYPE-08 and full SK-09 remain absent/incomplete. The loader has a narrow provisional ModelLoadDiagnostic/SourcePosition seam; it does not claim general SK-11 completion.

`tools/model-loader` owns loading as build/authoring input tooling. Its only module edge is `model-authoring.public`; no compiler/runtime/model registry imports. The narrowly approved model-source-loading technology profile allows only model dependencies. PyYAML is approved exclusively at this tooling path, not inside neutral semantic packages. Public contracts and implementations reside in public.py to respect ARCH-API-002's prohibition on public imports of private implementations. Composition still separates providers, decoders and core orchestration; only the file provider's private read helper touches the filesystem. Internal namespace is reserved under the existing module layout convention, with no duplicate implementation.

CLI registration lists model-loader as an explicit tooling inventory name, without creating a forbidden tooling-to-tooling dependency or a sixth foundation activation marker. Root build imports each manifest public MODULE_NAME independently. Manifest inventory is nine modules; CLI observed module edges remain seven.

## Source and result contracts

ModelSourceId is a dedicated immutable caller-supplied, case-sensitive string: 1..256 Unicode characters, no leading/trailing whitespace, ASCII control characters, DEL or invalid Unicode surrogate values. Invalid programmer-created identities raise ValueError at construction, rather than fabricating a source to carry an input diagnostic. It is not a SemanticElementId and carries no global uniqueness promise.

InMemoryModelSource(id, format, content) takes Unicode source text. FileModelSource(id, format, path) takes an explicit nonempty NUL-free path. Format is explicit, case-sensitive `json` or `yaml` (ModelSourceFormat enum or string). Other nonempty format strings can be submitted and yield MOD-LOAD-003 before acquisition. Paths/extensions never infer format, namespace, semantic identity, context or ownership. Relative file paths use the caller's current working directory. Symlinks to regular files are allowed; access confinement belongs to the calling application's boundary. No discovery, import traversal, network, cache or watcher is implemented.

ModelSourceInformation retains ID, original format and supplied location, without retaining large raw content in successful snapshots. SourceContentResult distinguishes acquired text from errors. SourceDecodeResult carries an untrusted candidate plus optional immutable source-path coordinates; it is not a successful document and may contain mutable parser containers. ModelLoader rechecks resource limits and plain-tree compatibility even for explicitly injected adapters. ModelSourceProvider/ModelDecoder are minimal structural protocols; replace existing provider/decoder slots through constructor injection, with no plugin manager or service locator. Adapter result/association violations and unexpected adapter programming exceptions propagate; anticipated acquisition/parser/input failures are diagnostics.

ModelLoadResult contains either LoadedAuthoringDocument(source, MOD-01 snapshot), with no error diagnostics, or no loaded document plus source-associated errors. `is_success` is derived. Stage is acquisition, decoding, schema or batch. Invalid candidates never become successful loaded snapshots. Parser containers are not retained in the immutable authoring document.

`load_many` takes a list/tuple and copies its input sequence. Entries follow caller order; each entry retains its own source. Derived status is EMPTY, ALL_LOADED, PARTIAL or ALL_FAILED; no ambiguous batch success boolean. Derived successful_documents, failed_sources and diagnostics preserve entry/diagnostic ordering. All occurrences of a duplicate source ID are rejected before acquisition, with MOD-LOAD-011 and the zero-based first input index. Unique sources still load. Duplicate IDs are case-sensitive; different IDs pointing to the same file are distinct submissions. No cross-document semantic collision check or merge occurs. Loading a source separately has no remembered batch state.

## Resource and decoder policies

ModelLoadOptions defaults: max_source_bytes=1,048,576 UTF-8 bytes; max_depth=64 tree levels; max_nodes=100,000 values/containers/mapping keys. Positive exact integers only; max_depth has a documented hard ceiling of 128 to stay within recursive parser/projection bounds. Increase size/node limits explicitly, accepting corresponding resource costs. Tree root counts as level one and scalar child values consume a level. JSON lexical container-depth preflight runs before json.loads; YAML event depth/node preflight runs before composition; both candidates receive a bounded iterative plain-tree check. This limits practical resource exposure, not a hard wall-clock/memory quota for custom adapters. There is no streaming framework.

In-memory input is never read from a file. Source text must contain valid Unicode scalar values and have no leading BOM; empty/whitespace-only content is acquisition failure. File acquisition opens read-only, checks the opened descriptor is a regular file, and reads at most the byte limit plus one, avoiding an unbounded read if a file grows. Nonblocking open prevents FIFO blocking on platforms supporting O_NONBLOCK. UTF-8 is strict; malformed encoding and BOM are rejected. Files are not rewritten, corrected or upgraded. File content may change externally during reading; there is no atomic external version pin/checksum or OS-level sandbox. Permission errors depend on the actual effective OS user.

JSON uses Python's established json decoder, with duplicate object keys rejected at every level, nonstandard NaN/Infinity constants rejected and finite JSON-compatible values required. Comments, trailing commas, executable expressions, extra documents, invalid escaping and invalid Unicode scalar values fail. No YAML retry occurs. String/primitive roots are rejected as decoded-root errors. Float overflow is rejected; interpreter integer conversion ceilings are reported as parser resource failures. Prototype-like keys are plain dict strings and subsequently rejected by MOD-01 as unknown properties; no executable object construction occurs.

YAML uses pinned **PyYAML 6.0.3**, pure Python **SafeLoader**, **YAML 1.1 implicit scalar resolution**, with strict event preflight and explicit node projection. `%YAML 1.1` is allowed; other version directives and tag directives are rejected. This is not a claim of YAML 1.2 support. Unquoted yes/no/on/off resolve to booleans; quote string-valued tokens such as names, dates and schema versions where necessary. Standard numeric spellings follow SafeLoader 1.1; authoring constraints still require MOD-01's exact types (e.g. numeric-bound values must be quoted strings).

Reject all explicit tags (including safe standard explicit tags), custom/unsafe object tags, anchors, aliases (including recursive aliases), merge keys, non-string mapping keys, duplicate decoded string keys and more than one document. Only map, sequence, string, integer, finite float, boolean and null node types are projected; implicit dates/timestamps, sets/binary/objects and non-finite floats fail. Parsing uses the established parser; MOD-02 does not implement a YAML grammar. YAML is imported lazily; if unavailable, YAML requests return an explicit unsupported/unavailable decoder diagnostic, while JSON and contract imports remain usable. `scripts/dev.py install` installs the pinned requirements; CI performs dependency setup without loading archived examples.

## Diagnostic categories and source positions

| Code | Boundary | Meaning |
| --- | --- | --- |
| MOD-LOAD-001 | acquisition | Missing file |
| MOD-LOAD-002 | acquisition | Unreadable/nonregular file |
| MOD-LOAD-003 | decoding | Unsupported explicit format or unavailable YAML dependency |
| MOD-LOAD-004 | acquisition | Empty/whitespace-only source |
| MOD-LOAD-005 | decoding | JSON/YAML syntax failure |
| MOD-LOAD-006 | decoding | Duplicate mapping key |
| MOD-LOAD-007 | decoding | Multiple YAML documents |
| MOD-LOAD-008 | decoding | Unsupported/unsafe/non-JSON-compatible construct |
| MOD-LOAD-009 | decoding | Non-object root |
| MOD-LOAD-010 | schema | Delegated MOD-01 failure; original diagnostic retained |
| MOD-LOAD-011 | batch | Duplicate source ID; all occurrences rejected |
| MOD-LOAD-012 | acquisition | Source exceeds byte limit |
| MOD-LOAD-013 | acquisition/decoding | Invalid Unicode/UTF-8/BOM |
| MOD-LOAD-014 | decoding | Depth/node/numeric/parser resource limit |

Source positions are one-based Unicode character line/column coordinates. JSON syntax errors retain json.JSONDecodeError coordinates; duplicate-key/tree/schema errors have no invented JSON location. YAML parser/event/node errors retain marks. YAML schema diagnostics use an exact matching authoring path's value-node start mark. Missing-property paths have no node and no position. Original related_path remains in schema diagnostics without an invented related physical span. Byte spans, end positions and a semantic provenance graph are not implemented.

## Mini Sales loading usage (documented, NOT RUN)

Existing [JSON](../../examples/authoring/mini-sales.json) and new equivalent [YAML](../../examples/authoring/mini-sales.yaml) use actual MOD-01 IDs, expression objects, explicit presence/nullability and ordered constraint declarations. No example loading or comparison was executed.

```python
from model_loader.public import ModelLoader, ModelSourceId, FileModelSource
loader = ModelLoader()
result = loader.load(FileModelSource(
    ModelSourceId('mini-sales'), 'yaml', 'examples/authoring/mini-sales.yaml'))
# Consume result.loaded only if result.is_success.
# Keep schema diagnostics separate from acquisition/decoding diagnostics.
```

Do not run this example until deferred execution is explicitly authorized. A minimal memory source can contain `{"schemaVersion":"1.0","context":"sem_550e8400-e29b-41d4-a716-999999999999","namespace":"sales","definitions":[]}` as source text. Unresolved semantic-name expressions stay unresolved; no target lookup, registration, canonicalization, compilation, tenant inference or instance execution occurs.

See [ADR-0024](../architecture/decisions/ADR-0024-model-source-loading-boundary.md), [static record](../architecture/mod02-verification.md) and [mandatory archive](../../test-archive/MOD-02/README.md). Implementation stops at MOD-02.

Parser references: [PyYAML documentation](https://pyyaml.org/wiki/PyYAMLDocumentation), [project release metadata](https://pypi.org/project/PyYAML/6.0.3/). These references informed parser API/configuration decisions; they are not execution evidence.
