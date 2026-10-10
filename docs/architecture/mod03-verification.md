# MOD-03 — implementation and static-check record

Date: 2026-10-10 (Asia/Riyadh). Implementation: source tracking and loader integration complete within actual repository contracts. Behavior: **NOT_RUN — DEFERRED / NOT VERIFIED**. Scenarios documented: **103**. Test code implemented: **0**. Tests executed: **0**.

## Implemented components and contract extensions

Existing SourcePosition gains optional Unicode character offset. Added frozen SourceSpan, SourceLocation, SourceNodePath, SourceNodeKind, SourceLocationEntry, SourceLocationIndex and SourceLocationTracker. The immutable index supports typed value/key lookup, absence, deterministic enumeration, idempotent duplicate entry handling and conflicting registration rejection. Exact-text snapshot digest is optional for generated/legacy inputs and always supplied by built-in text decoders.

Existing JSON decoder now instruments the stdlib scanner/object/array callbacks and scanstring to retain exact key/value/container intervals from the same parse. Existing YAML projection retains native node/key/event marks under unchanged SafeLoader 1.1 restrictions. SourceDecodeResult/LoadedAuthoringDocument carry defaulted optional indexes. ModelLoadDiagnostic adds primary and immutable related locations, retaining original structural diagnostics and position compatibility. Loader checks declared digest alignment with exact acquired text. No semantic contracts or source IDs are recreated; no semantic validation/resolution/registration/compilation/runtime work is added.

General SK-11 is absent, so full integration is blocked by that missing prerequisite; the actual provisional loading/authoring diagnostic seam is extended and explicitly documented. No competing generic Diagnostics model is invented. Existing TYPE-01/TYPE-08/full SK-09 limitations remain visible.

## Stack and Django/DRF boundary

Read-only interpreter/distribution metadata inspection reported local Python 3.12.14, PyYAML 6.0.3, Django absent and djangorestframework absent. Source inspection found no current Django project/model-loading HTTP endpoint/view/serializer. Therefore no API is extended, no serializer/HTTP endpoint/Django model/database is added, and no dependency version is upgraded. Domain value contracts remain framework-independent; future HTTP exposure must use the approved DRF boundary.

## Actual separately executed static activities

- `python3 scripts/dev.py lint`: syntax/whitespace/source ownership/architecture checks succeeded.
- `python3 scripts/dev.py build`: source syntax/boundaries and all manifest public MODULE_NAME imports succeeded; generated ignored bytecode and build/platform-workspace.zip. This does not invoke source decoding/tracking/lookup scenarios.
- `python3 scripts/dev.py fitness:json --output build/mod03-fitness.json`: 44 static architecture rules satisfied, nine modules, 45 production sources parsed, one shared scan; no failures/cycles/warnings/exceptions/suppression.
- `python3 scripts/dev.py dependencies:json`: static dependency report, no violations/cycles; existing module/profile inventory unchanged.
- `git diff --check`: whitespace patch clean.
- Documentation inventory: 103 stable scenario headings and 103 NOT_RUN — DEFERRED execution statuses in the single detailed file; scenario text only, no case execution.
- Local stdlib JSON callback source was read for compatibility design; installed distribution metadata was read to assess framework/parser versions. Neither activity executed a tracked-source case.

No test source is created or modified. No unit/comprehensive/architecture behavioral tests, parser/loader/tracker examples, Mini Sales location/equivalence operations, CLI/runtime/doctor smoke commands or custom deferred scenario runners were executed. Existing CI deferral stays true; publishing checks only static/setup jobs and requires comprehensive/runtime steps to remain skipped. Green static jobs do not certify source-span behavior.

## Created and modified files

Modified production source:

- tools/model-loader/src/model_loader/public.py

Created documentation:

- docs/model/source-location-tracking.md
- docs/architecture/decisions/ADR-0025-source-location-tracking.md
- docs/architecture/mod03-verification.md
- test-archive/MOD-03/README.md
- test-archive/MOD-03/MOD-03-deferred-tests.md (single detailed specification)
- test-archive/MOD-03/MOD-03-deferred-test-spec.md (standing-name navigation only)

Modified documentation:

- README.md
- docs/model/model-loader.md
- docs/architecture/repository-structure.md
- test-archive/MOD-02/README.md (append-only compatibility note; no prior scenario deleted or execution status changed)

## Decisions, risks and next-stage readiness

Coordinates are one-based; offsets count zero-based Python Unicode source characters. Spans are half-open, including zero-width parser points. Node addressing is snapshot-scoped pointer tokens with empty root and ~0/~1 escaping. Index owns read-only copied collections and lexical pointer enumeration. Key/value spans remain separate. Missing-property fallback uses a reliable existing parent span, not a guessed absent token; syntax uses parser positions; related structural declarations retain precise original spans where available. Physical positions remain auxiliary to semantic identities.

Stdlib JSON scanner/callback methods are implementation interfaces; supported Python matrix behavior remains deferred, and static import success does not prove parser callback execution. JSON/YAML native newline conventions differ and are documented; no byte/UTF-16/grapheme offsets are advertised. Unknown offsets/marks remain absent. Standalone spans cannot certify arbitrary raw text, and undigested custom adapters remain trusted protocol metadata. Parser resource limits are practical bounds, not a new isolation framework. YAML anchors/aliases/tags/multiple documents remain rejected. No AST leakage, source rewriting, provenance graph or unrestricted source API is introduced.

Implementation and Markdown documentation are ready for review/consumption by the next authoring stage, with missing unified SK-11 and behavioral verification limitations explicit. Stop at MOD-03; no MOD-04 automatically started.
