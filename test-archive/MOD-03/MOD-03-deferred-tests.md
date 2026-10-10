# MOD-03 — Deferred Test Specification

Task: MOD-03 — Source Location Tracking

Backend: Python / Django / Django REST Framework

Status: NOT_RUN — DEFERRED

Tests Implemented: 0

Tests Executed: 0

Dependencies:
- SK-11
- MOD-01
- MOD-02

Documentation date: 2026-10-10 (Asia/Riyadh). Behavioral verification: **DEFERRED / NOT VERIFIED**.
Archived scenarios: **103**, stable MOD-03-T001 through MOD-03-T103.
This is the single detailed scenario Markdown file. README and the standing-name spec link are navigation only.

## Shared prerequisites

Future explicit authorization is required before any execution. Pin source/archive revisions, Python 3.11+ (3.11/3.12/3.13 matrix for stdlib callback compatibility), actual repository module paths, PyYAML==6.0.3 and source acquisition environment. Record exact source text/UTF-8 bytes, source ID, explicit format, options, native newline convention, parser marks and digest. BASE is the existing MOD-01 schemaVersion="1.0", explicit sem_ UUID-v4 context, namespace="sales", definitions=[]. Expanded fixtures use existing [Mini Sales JSON](../../examples/authoring/mini-sales.json) and [YAML](../../examples/authoring/mini-sales.yaml). No canonical type or runtime fixture is needed.

Every expected result is a specification from source inspection, not an observed passing result. Compare exact typed path, key/value span, half-open endpoints, offsets, digest, primary/related source association, original schema codes/causes and deterministic order. No matching-string location search is a valid oracle; use parser metadata and exact lexical fixture token intervals. Coordinates must remain absent when unavailable. General SK-11 is missing: record the provisional loading seam or an explicitly reconciled future contract revision. Django/DRF transport cases are conditional on a later authorized real API; none is added here.

## Execution policy

No test code is created or changed. No unittest/pytest/manage.py test/tox/nox, custom scenario runner, parser/loader examples or deferred methods are executed. Static syntax/build/dependency/Fitness/document inspection is separate and cannot establish these cases. All cases remain NOT_RUN — DEFERRED. Future PASSED/FAILED requires actual execution command/date/revisions/expected-versus-observed evidence. Preserve stable IDs and prior scenario history. Stop at MOD-03.

## MOD-03-T001 — One-based coordinates

- **Test ID:** MOD-03-T001.
- **Scenario:** One-based coordinates.
- **Category:** Position.
- **Objective:** Verify the specified one-based coordinates behavior while preserving source/semantic separation.
- **Component:** SourcePosition.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Construct line=1,column=1,offset=0 and valid later coordinates.
- **Expected result:** Retain exact immutable coordinates.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Offset units are Python characters, not bytes or UTF-16 units.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T002 — Invalid line and column

- **Test ID:** MOD-03-T002.
- **Scenario:** Invalid line and column.
- **Category:** Position.
- **Objective:** Verify the specified invalid line and column behavior while preserving source/semantic separation.
- **Component:** SourcePosition.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use zero, negative, bool, float and non-int line/column values.
- **Expected result:** Reject exact-integer coordinate misuse.
- **Expected diagnostics:** ValueError.
- **Boundary / edge cases:** One is minimum; no normalization or clamping.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T003 — Optional offset compatibility

- **Test ID:** MOD-03-T003.
- **Scenario:** Optional offset compatibility.
- **Category:** Position.
- **Objective:** Verify the specified optional offset compatibility behavior while preserving source/semantic separation.
- **Component:** SourcePosition.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Construct legacy SourcePosition(line,column) with two arguments.
- **Expected result:** offset=None; existing line/column access remains compatible.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Absence must never be replaced by a guessed offset.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T004 — Invalid offsets

- **Test ID:** MOD-03-T004.
- **Scenario:** Invalid offsets.
- **Category:** Position.
- **Objective:** Verify the specified invalid offsets behavior while preserving source/semantic separation.
- **Component:** SourcePosition.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use negative, bool, float and coordinate-impossible offset values.
- **Expected result:** Reject invalid known offset.
- **Expected diagnostics:** ValueError.
- **Boundary / edge cases:** Offset must be at least line+column-2, the minimum possible character prefix.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T005 — Supplementary Unicode and combining text

- **Test ID:** MOD-03-T005.
- **Scenario:** Supplementary Unicode and combining text.
- **Category:** Position.
- **Objective:** Verify the specified supplementary unicode and combining text behavior while preserving source/semantic separation.
- **Component:** Parser coordinate adapters.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Parse supported documents containing non-ASCII, supplementary and combining characters before tracked nodes.
- **Expected result:** Use Python character offsets and parser-native character columns.
- **Expected diagnostics:** None if source structurally valid.
- **Boundary / edge cases:** Do not mix UTF-8 bytes, grapheme count or UTF-16 units.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T006 — Native newline conventions

- **Test ID:** MOD-03-T006.
- **Scenario:** Native newline conventions.
- **Category:** Position.
- **Objective:** Verify the specified native newline conventions behavior while preserving source/semantic separation.
- **Component:** JSON/YAML adapters.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use LF, CRLF and standalone CR in both formats.
- **Expected result:** JSON follows stdlib LF line counting; YAML follows native YAML marks; offsets index unchanged text.
- **Expected diagnostics:** Syntax/schema errors preserve their native parser convention.
- **Boundary / edge cases:** CRLF retains both source characters; file acquisition performs no newline translation.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T007 — Valid half-open span

- **Test ID:** MOD-03-T007.
- **Scenario:** Valid half-open span.
- **Category:** Span.
- **Objective:** Verify the specified valid half-open span behavior while preserving source/semantic separation.
- **Component:** SourceSpan.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Construct ordered endpoints with optional consistent offsets.
- **Expected result:** Retain [start,end) interval without guessing token length.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** End-exclusive coordinates may lie at next-line start.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T008 — Zero-width span

- **Test ID:** MOD-03-T008.
- **Scenario:** Zero-width span.
- **Category:** Span.
- **Objective:** Verify the specified zero-width span behavior while preserving source/semantic separation.
- **Component:** SourceSpan.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use identical coordinates/offsets at a real parser insertion point.
- **Expected result:** Accept empty [p,p) span.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** EOF point remains a valid span.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T009 — Reversed coordinate span

- **Test ID:** MOD-03-T009.
- **Scenario:** Reversed coordinate span.
- **Category:** Span.
- **Objective:** Verify the specified reversed coordinate span behavior while preserving source/semantic separation.
- **Component:** SourceSpan.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use later start line/column than end.
- **Expected result:** Reject span before index insertion.
- **Expected diagnostics:** ValueError.
- **Boundary / edge cases:** Same-line reversal and cross-line reversal both fail.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T010 — Reversed offset span

- **Test ID:** MOD-03-T010.
- **Scenario:** Reversed offset span.
- **Category:** Span.
- **Objective:** Verify the specified reversed offset span behavior while preserving source/semantic separation.
- **Component:** SourceSpan.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use ordered coordinates but start.offset>end.offset.
- **Expected result:** Reject inconsistent offset order.
- **Expected diagnostics:** ValueError.
- **Boundary / edge cases:** Neither endpoint is silently swapped.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T011 — Offset equality/order consistency

- **Test ID:** MOD-03-T011.
- **Scenario:** Offset equality/order consistency.
- **Category:** Span.
- **Objective:** Verify the specified offset equality/order consistency behavior while preserving source/semantic separation.
- **Component:** SourceSpan.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use equal coordinates with different offsets and different coordinates with equal offsets.
- **Expected result:** Reject inconsistent coordinate/offset ordering.
- **Expected diagnostics:** ValueError.
- **Boundary / edge cases:** Unknown offsets are not invented for comparison.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T012 — Same-line distance consistency

- **Test ID:** MOD-03-T012.
- **Scenario:** Same-line distance consistency.
- **Category:** Span.
- **Objective:** Verify the specified same-line distance consistency behavior while preserving source/semantic separation.
- **Component:** SourceSpan.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use same-line endpoints with offset distance unlike column distance.
- **Expected result:** Reject inconsistent Unicode character distances.
- **Expected diagnostics:** ValueError.
- **Boundary / edge cases:** Cross-line source lengths cannot be fully certified without source text.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T013 — Partial offset absence

- **Test ID:** MOD-03-T013.
- **Scenario:** Partial offset absence.
- **Category:** Span.
- **Objective:** Verify the specified partial offset absence behavior while preserving source/semantic separation.
- **Component:** SourceSpan.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use one known endpoint offset and one absent offset with ordered coordinates.
- **Expected result:** Accept coordinate-ordered span; retain absent offset.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** No inferred end/start offset or decoded-text-length arithmetic.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T014 — Typed endpoints only

- **Test ID:** MOD-03-T014.
- **Scenario:** Typed endpoints only.
- **Category:** Span.
- **Objective:** Verify the specified typed endpoints only behavior while preserving source/semantic separation.
- **Component:** SourceSpan.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Pass tuples, arbitrary objects or SourcePosition subclasses.
- **Expected result:** Reject noncanonical endpoint contracts.
- **Expected diagnostics:** TypeError.
- **Boundary / edge cases:** No duck-typed mutable endpoint accepted.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T015 — Dedicated source identity

- **Test ID:** MOD-03-T015.
- **Scenario:** Dedicated source identity.
- **Category:** Location.
- **Objective:** Verify the specified dedicated source identity behavior while preserving source/semantic separation.
- **Component:** SourceLocation.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Associate span with actual ModelSourceId.
- **Expected result:** Preserve source identity independently of semantic IDs.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** SemanticElementId/FieldId/QualifiedName are not acceptable substitutes.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T016 — Invalid location types

- **Test ID:** MOD-03-T016.
- **Scenario:** Invalid location types.
- **Category:** Location.
- **Objective:** Verify the specified invalid location types behavior while preserving source/semantic separation.
- **Component:** SourceLocation.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Pass semantic ID or mutable span-like object.
- **Expected result:** Reject invalid source/span contracts.
- **Expected diagnostics:** TypeError.
- **Boundary / edge cases:** No source identity inferred from coordinates.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T017 — Multiple declarations in one source

- **Test ID:** MOD-03-T017.
- **Scenario:** Multiple declarations in one source.
- **Category:** Location.
- **Objective:** Verify the specified multiple declarations in one source behavior while preserving source/semantic separation.
- **Component:** LoadedAuthoringDocument.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Load Mini Sales and inspect definition/facet/field/constraint locations.
- **Expected result:** All locations retain one supplied source ID with distinct physical spans.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Do not create separate semantic source IDs for each declaration.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T018 — Multiple source documents

- **Test ID:** MOD-03-T018.
- **Scenario:** Multiple source documents.
- **Category:** Location.
- **Objective:** Verify the specified multiple source documents behavior while preserving source/semantic separation.
- **Component:** Batch loading.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Load equivalent documents under two source IDs.
- **Expected result:** Each immutable index belongs to its own source snapshot.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Equal semantics never merge physical source associations.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T019 — Unavailable physical origin

- **Test ID:** MOD-03-T019.
- **Scenario:** Unavailable physical origin.
- **Category:** Location.
- **Objective:** Verify the specified unavailable physical origin behavior while preserving source/semantic separation.
- **Component:** SourceLocationTracker.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use index=None and separately empty generated index.
- **Expected result:** Return None for absent coordinates; no source/semantic error solely for absence.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Never substitute 1:1 or fabricated offsets.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T020 — Unambiguous root pointer

- **Test ID:** MOD-03-T020.
- **Scenario:** Unambiguous root pointer.
- **Category:** Path.
- **Objective:** Verify the specified unambiguous root pointer behavior while preserving source/semantic separation.
- **Component:** SourceNodePath.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Parse empty string and slash separately.
- **Expected result:** Empty string is root; slash identifies an empty-string property.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Root pointer is not the illustrative slash convention.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T021 — Pointer escaping round trip

- **Test ID:** MOD-03-T021.
- **Scenario:** Pointer escaping round trip.
- **Category:** Path.
- **Objective:** Verify the specified pointer escaping round trip behavior while preserving source/semantic separation.
- **Component:** SourceNodePath.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use tokens containing tilde, slash, empty text and Unicode.
- **Expected result:** Render ~0/~1 and parse back equivalent tokens.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Decode ~1 before ~0; do not percent-decode.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T022 — Invalid pointer escapes

- **Test ID:** MOD-03-T022.
- **Scenario:** Invalid pointer escapes.
- **Category:** Path.
- **Objective:** Verify the specified invalid pointer escapes behavior while preserving source/semantic separation.
- **Component:** SourceNodePath.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Submit pointer without slash, terminal tilde and ~2 escapes.
- **Expected result:** Reject invalid pointer grammar.
- **Expected diagnostics:** ValueError.
- **Boundary / edge cases:** URI fragment syntax is not accepted as a pointer.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T023 — Snapshot-scoped declaration paths

- **Test ID:** MOD-03-T023.
- **Scenario:** Snapshot-scoped declaration paths.
- **Category:** Path.
- **Objective:** Verify the specified snapshot-scoped declaration paths behavior while preserving source/semantic separation.
- **Component:** SourceNodePath.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Address actual definition/facet/field nodes in Mini Sales.
- **Expected result:** Resolve typed pointers according to current ordered authoring arrays.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Moving declarations may change paths; no stable semantic identity promise.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T024 — Constraint declaration array paths

- **Test ID:** MOD-03-T024.
- **Scenario:** Constraint declaration array paths.
- **Category:** Path.
- **Objective:** Verify the specified constraint declaration array paths behavior while preserving source/semantic separation.
- **Component:** SourceNodePath.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Address precision via values/1 and literal via values/1/value.
- **Expected result:** Locate actual MOD-01 ordered declaration syntax.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Do not reinterpret illustrative values/precision map as current schema.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T025 — Numeric object keys and array tokens

- **Test ID:** MOD-03-T025.
- **Scenario:** Numeric object keys and array tokens.
- **Category:** Path.
- **Objective:** Verify the specified numeric object keys and array tokens behavior while preserving source/semantic separation.
- **Component:** SourceNodePath.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Parse supported candidate containing string key 0 and array member index 0 at distinct parents.
- **Expected result:** Address per actual container kind without integer-key coercion.
- **Expected diagnostics:** Schema unknown keys may yield MOD-LOAD-010, but tracking remains precise.
- **Boundary / edge cases:** Pointer tokens are strings; AuthoringSchemaPath ints convert explicitly.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T026 — Typed MOD-01 path conversion

- **Test ID:** MOD-03-T026.
- **Scenario:** Typed MOD-01 path conversion.
- **Category:** Path.
- **Objective:** Verify the specified typed mod-01 path conversion behavior while preserving source/semantic separation.
- **Component:** SourceNodePath.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Convert existing AuthoringSchemaPath with property/index segments.
- **Expected result:** Produce equivalent string-token pointer without semantic interpretation.
- **Expected diagnostics:** TypeError for non-AuthoringSchemaPath input.
- **Boundary / edge cases:** Root conversion yields empty pointer.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T027 — Constructor defensive token copy

- **Test ID:** MOD-03-T027.
- **Scenario:** Constructor defensive token copy.
- **Category:** Path.
- **Objective:** Verify the specified constructor defensive token copy behavior while preserving source/semantic separation.
- **Component:** SourceNodePath.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Build from caller list and mutate retained list.
- **Expected result:** Path tokens remain unchanged immutable tuple.
- **Expected diagnostics:** TypeError for nonstring/invalid-surrogate tokens.
- **Boundary / edge cases:** No externally mutable addressing state.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T028 — Exact typed lookup

- **Test ID:** MOD-03-T028.
- **Scenario:** Exact typed lookup.
- **Category:** Index.
- **Objective:** Verify the specified exact typed lookup behavior while preserving source/semantic separation.
- **Component:** SourceLocationIndex.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Build index from root/field entries and use find,contains,entry.
- **Expected result:** Return exact typed locations/entry for present paths.
- **Expected diagnostics:** TypeError for wrong lookup path contract.
- **Boundary / edge cases:** O(1) private map lookup does not expose mutable map.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T029 — Explicit missing result

- **Test ID:** MOD-03-T029.
- **Scenario:** Explicit missing result.
- **Category:** Index.
- **Objective:** Verify the specified explicit missing result behavior while preserving source/semantic separation.
- **Component:** SourceLocationIndex.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Lookup path not registered.
- **Expected result:** find/entry return None; contains returns False.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** find_key returns None when node has no property key.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T030 — Deterministic enumeration

- **Test ID:** MOD-03-T030.
- **Scenario:** Deterministic enumeration.
- **Category:** Index.
- **Objective:** Verify the specified deterministic enumeration behavior while preserving source/semantic separation.
- **Component:** SourceLocationIndex.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Build same entry set in different input orders.
- **Expected result:** Equal canonical entries and lexicographic escaped-pointer enumeration.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Root first; /10 before /2; enumeration is not authoring order.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T031 — Conflicting duplicate path

- **Test ID:** MOD-03-T031.
- **Scenario:** Conflicting duplicate path.
- **Category:** Index.
- **Objective:** Verify the specified conflicting duplicate path behavior while preserving source/semantic separation.
- **Component:** SourceLocationIndex.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Register same path with differing span, kind or key location.
- **Expected result:** Reject conflicting registrations.
- **Expected diagnostics:** ValueError.
- **Boundary / edge cases:** No first/last-write-wins.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T032 — Identical duplicate idempotence

- **Test ID:** MOD-03-T032.
- **Scenario:** Identical duplicate idempotence.
- **Category:** Index.
- **Objective:** Verify the specified identical duplicate idempotence behavior while preserving source/semantic separation.
- **Component:** SourceLocationIndex.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Register same exact immutable entry more than once.
- **Expected result:** Retain one entry in canonical index.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Conflict rejection remains separate from idempotence.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T033 — Cross-source entry rejection

- **Test ID:** MOD-03-T033.
- **Scenario:** Cross-source entry rejection.
- **Category:** Index.
- **Objective:** Verify the specified cross-source entry rejection behavior while preserving source/semantic separation.
- **Component:** SourceLocationIndex.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Construct index with entry belonging to another source ID.
- **Expected result:** Reject mismatched physical ownership.
- **Expected diagnostics:** ValueError.
- **Boundary / edge cases:** Related diagnostic locations may separately reference other sources.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T034 — Property key and value separation

- **Test ID:** MOD-03-T034.
- **Scenario:** Property key and value separation.
- **Category:** Index.
- **Objective:** Verify the specified property key and value separation behavior while preserving source/semantic separation.
- **Component:** SourceLocationEntry.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Construct a property entry with distinct same-source key/value spans.
- **Expected result:** find gives value; find_key gives key.
- **Expected diagnostics:** ValueError for root key or mismatched source key.
- **Boundary / edge cases:** Root/array children have no fabricated key location.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T035 — Known parent kind enforcement

- **Test ID:** MOD-03-T035.
- **Scenario:** Known parent kind enforcement.
- **Category:** Index.
- **Objective:** Verify the specified known parent kind enforcement behavior while preserving source/semantic separation.
- **Component:** SourceLocationIndex.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Attach key_location to entry under a registered array/scalar parent.
- **Expected result:** Reject non-object property-key association.
- **Expected diagnostics:** ValueError.
- **Boundary / edge cases:** Partial generated indexes may omit parent entries without inventing them.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T036 — Deep collection immutability

- **Test ID:** MOD-03-T036.
- **Scenario:** Deep collection immutability.
- **Category:** Index.
- **Objective:** Verify the specified deep collection immutability behavior while preserving source/semantic separation.
- **Component:** SourceLocationIndex.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Retain input list, mutate it and attempt returned tuple/private proxy mutation.
- **Expected result:** Owned entries/map remain unchanged; mutation is rejected.
- **Expected diagnostics:** TypeError/attribute mutation failure as appropriate.
- **Boundary / edge cases:** Frozen dataclass alone must not expose a mutable dict.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T037 — Value equality and hashing

- **Test ID:** MOD-03-T037.
- **Scenario:** Value equality and hashing.
- **Category:** Index.
- **Objective:** Verify the specified value equality and hashing behavior while preserving source/semantic separation.
- **Component:** SourceLocationIndex.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Build independently equivalent frozen positions/spans/paths/entries/indexes.
- **Expected result:** Equality depends on canonical values and digest, not object addresses or construction order.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Private MappingProxyType is excluded from comparison/hash.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T038 — Snapshot digest contract

- **Test ID:** MOD-03-T038.
- **Scenario:** Snapshot digest contract.
- **Category:** Index.
- **Objective:** Verify the specified snapshot digest contract behavior while preserving source/semantic separation.
- **Component:** SourceLocationIndex.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use valid lowercase SHA-256 hex and invalid/nontext/uppercase/short digests.
- **Expected result:** Accept valid/None digest; reject malformed digest.
- **Expected diagnostics:** ValueError for invalid known digest.
- **Boundary / edge cases:** Digest is content association, not provenance authority.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T039 — Parser metadata coordination

- **Test ID:** MOD-03-T039.
- **Scenario:** Parser metadata coordination.
- **Category:** Tracker.
- **Objective:** Verify the specified parser metadata coordination behavior while preserving source/semantic separation.
- **Component:** SourceLocationTracker.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Build index from reliable typed parser entries and original source text.
- **Expected result:** Copy/index metadata and compute exact UTF-8 SHA-256 digest.
- **Expected diagnostics:** TypeError for nontext source_text.
- **Boundary / edge cases:** Tracker performs no parsing, filesystem acquisition or semantic judging.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T040 — Reliable containing-node fallback

- **Test ID:** MOD-03-T040.
- **Scenario:** Reliable containing-node fallback.
- **Category:** Tracker.
- **Objective:** Verify the specified reliable containing-node fallback behavior while preserving source/semantic separation.
- **Component:** SourceLocationTracker.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Lookup missing required property with containing=True.
- **Expected result:** Return nearest registered object/array parent span.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Broader authored span is not a fabricated missing token.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T041 — Exact lookup without fallback

- **Test ID:** MOD-03-T041.
- **Scenario:** Exact lookup without fallback.
- **Category:** Tracker.
- **Objective:** Verify the specified exact lookup without fallback behavior while preserving source/semantic separation.
- **Component:** SourceLocationTracker.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Lookup nonexistent path with containing=False.
- **Expected result:** Return None even if root/parent exists.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Unknown origin does not turn into root automatically.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T042 — Key lookup mode

- **Test ID:** MOD-03-T042.
- **Scenario:** Key lookup mode.
- **Category:** Tracker.
- **Objective:** Verify the specified key lookup mode behavior while preserving source/semantic separation.
- **Component:** SourceLocationTracker.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Lookup existing property with key=True and absent property key without containing fallback.
- **Expected result:** Return key span only when parser supplied it.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Never substitute value span for missing key unless explicitly choosing a parent fallback.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T043 — Nested containers and declarations

- **Test ID:** MOD-03-T043.
- **Scenario:** Nested containers and declarations.
- **Category:** JSON.
- **Objective:** Verify the specified nested containers and declarations behavior while preserving source/semantic separation.
- **Component:** JsonModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Load actual nested Mini Sales JSON.
- **Expected result:** Track root, definitions, facets, fields, expressions and constraints from one parse.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Every valid node value/container span has parser-derived offsets.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T044 — Repeated nested property names

- **Test ID:** MOD-03-T044.
- **Scenario:** Repeated nested property names.
- **Category:** JSON.
- **Objective:** Verify the specified repeated nested property names behavior while preserving source/semantic separation.
- **Component:** JsonModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use name/value/kind repeatedly in distinct nested objects.
- **Expected result:** Index distinct correct paths/spans without matching-string searches.
- **Expected diagnostics:** None if schema valid.
- **Boundary / edge cases:** Equal scalar contents in different declarations retain different spans.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T045 — Escaped JSON strings and keys

- **Test ID:** MOD-03-T045.
- **Scenario:** Escaped JSON strings and keys.
- **Category:** JSON.
- **Objective:** Verify the specified escaped json strings and keys behavior while preserving source/semantic separation.
- **Component:** JsonModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use escaped quotes/backslashes, Unicode escapes and escaped equivalent key spellings.
- **Expected result:** Track lexical quoted token boundaries while retaining decoded values.
- **Expected diagnostics:** Duplicate equivalent keys MOD-LOAD-006.
- **Boundary / edge cases:** Decoded string length is not lexical span length.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T046 — Arrays and empty containers

- **Test ID:** MOD-03-T046.
- **Scenario:** Arrays and empty containers.
- **Category:** JSON.
- **Objective:** Verify the specified arrays and empty containers behavior while preserving source/semantic separation.
- **Component:** JsonModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use empty definitions, empty facets/fields/values and populated arrays.
- **Expected result:** Track exact container/member spans and no invented array key location.
- **Expected diagnostics:** None if schema valid.
- **Boundary / edge cases:** Empty object/array parser callbacks retain start/end punctuation.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T047 — Whitespace and formatting independence

- **Test ID:** MOD-03-T047.
- **Scenario:** Whitespace and formatting independence.
- **Category:** JSON.
- **Objective:** Verify the specified whitespace and formatting independence behavior while preserving source/semantic separation.
- **Component:** JsonModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use compact/indented source with spaces/newlines around member delimiters.
- **Expected result:** Track actual parser coordinates for each formatting, preserving semantic values.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Do not claim spans identical across different formatting.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T048 — Duplicate JSON keys with related spans

- **Test ID:** MOD-03-T048.
- **Scenario:** Duplicate JSON keys with related spans.
- **Category:** JSON.
- **Objective:** Verify the specified duplicate json keys with related spans behavior while preserving source/semantic separation.
- **Component:** JsonModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Repeat key in one object using equal and unequal values.
- **Expected result:** Reject at second key with first key as related location.
- **Expected diagnostics:** MOD-LOAD-006, stage decoding.
- **Boundary / edge cases:** Escaped equivalent names collide after parser decoding.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T049 — Malformed syntax parser point

- **Test ID:** MOD-03-T049.
- **Scenario:** Malformed syntax parser point.
- **Category:** JSON.
- **Objective:** Verify the specified malformed syntax parser point behavior while preserving source/semantic separation.
- **Component:** JsonModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use missing value/comma, trailing comma and malformed escape.
- **Expected result:** Retain reliable stdlib parser offset as zero-width error span.
- **Expected diagnostics:** MOD-LOAD-005.
- **Boundary / edge cases:** No partial loaded authoring document or fabricated enclosing syntax span.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T050 — EOF insertion point

- **Test ID:** MOD-03-T050.
- **Scenario:** EOF insertion point.
- **Category:** JSON.
- **Objective:** Verify the specified eof insertion point behavior while preserving source/semantic separation.
- **Component:** JsonModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Truncate JSON at known end-of-source parser failure.
- **Expected result:** Error span may be [len(text),len(text)) with genuine coordinates.
- **Expected diagnostics:** MOD-LOAD-005.
- **Boundary / edge cases:** Do not require token text beyond EOF.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T051 — Invalid decoded root location

- **Test ID:** MOD-03-T051.
- **Scenario:** Invalid decoded root location.
- **Category:** JSON.
- **Objective:** Verify the specified invalid decoded root location behavior while preserving source/semantic separation.
- **Component:** JsonModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use scalar, null and array roots.
- **Expected result:** Retain actual root span and return no successful document.
- **Expected diagnostics:** MOD-LOAD-009.
- **Boundary / edge cases:** Root text can be valid JSON but not a MOD-01 document.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T052 — Strict existing decode policy

- **Test ID:** MOD-03-T052.
- **Scenario:** Strict existing decode policy.
- **Category:** JSON.
- **Objective:** Verify the specified strict existing decode policy behavior while preserving source/semantic separation.
- **Component:** JsonModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Submit comments, nonstandard constants, multiple values and executable expressions.
- **Expected result:** Reject as MOD-02 decoding failure; no heuristic YAML retry.
- **Expected diagnostics:** MOD-LOAD-005 or MOD-LOAD-008 per original category.
- **Boundary / edge cases:** Quoted executable-looking text remains inert and schema-governed.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T053 — Non-finite overflow token span

- **Test ID:** MOD-03-T053.
- **Scenario:** Non-finite overflow token span.
- **Category:** JSON.
- **Objective:** Verify the specified non-finite overflow token span behavior while preserving source/semantic separation.
- **Component:** JsonModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Place 1e9999 in a nested candidate property.
- **Expected result:** Reject non-finite value with exact numeric token span.
- **Expected diagnostics:** MOD-LOAD-008.
- **Boundary / edge cases:** Do not silently accept a native infinity.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T054 — Malformed decoded Unicode token span

- **Test ID:** MOD-03-T054.
- **Scenario:** Malformed decoded Unicode token span.
- **Category:** JSON.
- **Objective:** Verify the specified malformed decoded unicode token span behavior while preserving source/semantic separation.
- **Component:** JsonModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use escaped lone surrogate in a key and separately scalar value.
- **Expected result:** Reject with key/value token span without constructing invalid pointer.
- **Expected diagnostics:** MOD-LOAD-008 for key; MOD-LOAD-013 for value.
- **Boundary / edge cases:** Valid supplementary pair remains Unicode-compatible.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T055 — Depth/node limits retained

- **Test ID:** MOD-03-T055.
- **Scenario:** Depth/node limits retained.
- **Category:** JSON.
- **Objective:** Verify the specified depth/node limits retained behavior while preserving source/semantic separation.
- **Component:** JsonModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use deep/wide documents exceeding configured limits.
- **Expected result:** Reject before unbounded index creation; keep original resource boundary.
- **Expected diagnostics:** MOD-LOAD-014.
- **Boundary / edge cases:** Mapping keys count alongside values; supported depth still subject to interpreter recursion limits.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T056 — Supported Python matrix

- **Test ID:** MOD-03-T056.
- **Scenario:** Supported Python matrix.
- **Category:** JSON.
- **Objective:** Verify the specified supported python matrix behavior while preserving source/semantic separation.
- **Component:** Stdlib parser callback compatibility.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Under future authorization, load representative source on Python 3.11/3.12/3.13.
- **Expected result:** Established scanner/object/array/scanstring callback contracts produce equivalent mappings.
- **Expected diagnostics:** No unexpected implementation exception for supported valid source.
- **Boundary / edge cases:** Static public imports do not execute this callback compatibility case.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T057 — No second incompatible parse

- **Test ID:** MOD-03-T057.
- **Scenario:** No second incompatible parse.
- **Category:** JSON.
- **Objective:** Verify the specified no second incompatible parse behavior while preserving source/semantic separation.
- **Component:** JsonModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Instrument decoder calls and source read operations.
- **Expected result:** One stdlib document parse creates both candidate and span ledger; key scanstring uses bounded parsed member coordinates.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** No raw declaration-text search or full manual JSON grammar.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T058 — Block collections

- **Test ID:** MOD-03-T058.
- **Scenario:** Block collections.
- **Category:** YAML.
- **Objective:** Verify the specified block collections behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Load existing Mini Sales YAML block maps/sequences.
- **Expected result:** Index real node/container/key/value start/end marks.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Document root span follows parser node boundaries, not file-wide guessed text.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T059 — Flow collections

- **Test ID:** MOD-03-T059.
- **Scenario:** Flow collections.
- **Category:** YAML.
- **Objective:** Verify the specified flow collections behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use supported flow maps/arrays equivalent to authoring values.
- **Expected result:** Track brace/bracket/member spans from native nodes.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** No assumption that block and flow span punctuation is identical.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T060 — Quoted scalars

- **Test ID:** MOD-03-T060.
- **Scenario:** Quoted scalars.
- **Category:** YAML.
- **Objective:** Verify the specified quoted scalars behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use single/double quoted source strings with escapes.
- **Expected result:** Track original lexical marks instead of decoded value lengths.
- **Expected diagnostics:** None if schema valid.
- **Boundary / edge cases:** Key quoted spans remain separate from value spans.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T061 — Block scalar values

- **Test ID:** MOD-03-T061.
- **Scenario:** Block scalar values.
- **Category:** YAML.
- **Objective:** Verify the specified block scalar values behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use literal/folded block scalar for a supported string constraint value.
- **Expected result:** Track full parser scalar node span and retain decoded text.
- **Expected diagnostics:** Schema may reject invalid payload; wrapper keeps exact span.
- **Boundary / edge cases:** Chomping/folding changes values but never drives guessed span lengths.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T062 — Comments and whitespace

- **Test ID:** MOD-03-T062.
- **Scenario:** Comments and whitespace.
- **Category:** YAML.
- **Objective:** Verify the specified comments and whitespace behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Place comments and blank lines between declarations.
- **Expected result:** Coordinates account for original text; node marks control included/excluded trivia.
- **Expected diagnostics:** None if schema valid.
- **Boundary / edge cases:** No stripping source before tracking.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T063 — Duplicate YAML keys with related spans

- **Test ID:** MOD-03-T063.
- **Scenario:** Duplicate YAML keys with related spans.
- **Category:** YAML.
- **Objective:** Verify the specified duplicate yaml keys with related spans behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Repeat root/nested string key with distinct original key marks.
- **Expected result:** Reject second key and retain first key as related location.
- **Expected diagnostics:** MOD-LOAD-006.
- **Boundary / edge cases:** No native mapping overwrite before conflict diagnosis.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T064 — Anchor rejection preserved

- **Test ID:** MOD-03-T064.
- **Scenario:** Anchor rejection preserved.
- **Category:** YAML.
- **Objective:** Verify the specified anchor rejection preserved behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Supply anchor without alias.
- **Expected result:** Reject at original event span; no anchor expansion index.
- **Expected diagnostics:** MOD-LOAD-008.
- **Boundary / edge cases:** MOD-03 does not enable previously unsupported constructs.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T065 — Alias and recursive alias rejection

- **Test ID:** MOD-03-T065.
- **Scenario:** Alias and recursive alias rejection.
- **Category:** YAML.
- **Objective:** Verify the specified alias and recursive alias rejection behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Supply alias reuse and recursive expansion source.
- **Expected result:** Reject actual alias/anchor event without fabricated expanded-node spans.
- **Expected diagnostics:** MOD-LOAD-008.
- **Boundary / edge cases:** Alias usage is not confused with definition location; neither is supported in v0.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T066 — Explicit/custom tag rejection

- **Test ID:** MOD-03-T066.
- **Scenario:** Explicit/custom tag rejection.
- **Category:** YAML.
- **Objective:** Verify the specified explicit/custom tag rejection behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use safe standard explicit tag and unsafe/custom object tag.
- **Expected result:** Reject at actual event span before object construction.
- **Expected diagnostics:** MOD-LOAD-008.
- **Boundary / edge cases:** No arbitrary application class or YAML object executes.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T067 — Multiple documents rejection

- **Test ID:** MOD-03-T067.
- **Scenario:** Multiple documents rejection.
- **Category:** YAML.
- **Objective:** Verify the specified multiple documents rejection behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Supply two YAML documents including an empty second.
- **Expected result:** Return original decode failure with second document event location.
- **Expected diagnostics:** MOD-LOAD-007.
- **Boundary / edge cases:** One source still maps to one authoring document.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T068 — Malformed syntax point

- **Test ID:** MOD-03-T068.
- **Scenario:** Malformed syntax point.
- **Category:** YAML.
- **Objective:** Verify the specified malformed syntax point behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use broken flow collection/indentation with problem_mark.
- **Expected result:** Retain genuine parser position as zero-width span.
- **Expected diagnostics:** MOD-LOAD-005.
- **Boundary / edge cases:** No mark means explicit absence, not 1:1.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T069 — Unsupported implicit scalar node

- **Test ID:** MOD-03-T069.
- **Scenario:** Unsupported implicit scalar node.
- **Category:** YAML.
- **Objective:** Verify the specified unsupported implicit scalar node behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use unquoted timestamp or non-finite float.
- **Expected result:** Reject with available native node span.
- **Expected diagnostics:** MOD-LOAD-008.
- **Boundary / edge cases:** YAML 1.1 quoting policy remains unchanged.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T070 — Non-string and merge key rejection

- **Test ID:** MOD-03-T070.
- **Scenario:** Non-string and merge key rejection.
- **Category:** YAML.
- **Objective:** Verify the specified non-string and merge key rejection behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Supply numeric/complex/merge key.
- **Expected result:** Reject with actual offending key node span where available.
- **Expected diagnostics:** MOD-LOAD-008.
- **Boundary / edge cases:** Quoted prototype-like names stay plain keys then MOD-01 rejects unknown properties.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T071 — Comment-only missing root

- **Test ID:** MOD-03-T071.
- **Scenario:** Comment-only missing root.
- **Category:** YAML.
- **Objective:** Verify the specified comment-only missing root behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Supply nonempty comment-only YAML text.
- **Expected result:** No document root snapshot; no invented physical root location.
- **Expected diagnostics:** MOD-LOAD-009.
- **Boundary / edge cases:** Whitespace-only text still fails earlier with MOD-LOAD-004.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T072 — Resource bounds and AST cleanup

- **Test ID:** MOD-03-T072.
- **Scenario:** Resource bounds and AST cleanup.
- **Category:** YAML.
- **Objective:** Verify the specified resource bounds and ast cleanup behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Submit excessive nesting/nodes and inspect disposal/reference ownership.
- **Expected result:** Retain bounded failure and no mutable AST nodes in exported locations.
- **Expected diagnostics:** MOD-LOAD-014.
- **Boundary / edge cases:** Preflight generators and SafeLoader remain closed on handled failures.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T073 — Successful document retains index

- **Test ID:** MOD-03-T073.
- **Scenario:** Successful document retains index.
- **Category:** Loader.
- **Objective:** Verify the specified successful document retains index behavior while preserving source/semantic separation.
- **Component:** ModelLoader.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Load valid JSON/YAML through memory/file providers.
- **Expected result:** Loaded document carries matching source identity, authoring snapshot and immutable index.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Candidate and index originate from same acquired text.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T074 — Exact source snapshot digest

- **Test ID:** MOD-03-T074.
- **Scenario:** Exact source snapshot digest.
- **Category:** Loader.
- **Objective:** Verify the specified exact source snapshot digest behavior while preserving source/semantic separation.
- **Component:** ModelLoader.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use built-in decoder and independently record exact acquired UTF-8 text digest.
- **Expected result:** Index digest matches that source text and loader validates it.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** No file mtime/random source revision used.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T075 — Mismatched decoder digest rejected

- **Test ID:** MOD-03-T075.
- **Scenario:** Mismatched decoder digest rejected.
- **Category:** Loader.
- **Objective:** Verify the specified mismatched decoder digest rejected behavior while preserving source/semantic separation.
- **Component:** ModelLoader.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Inject index with matching source ID but digest of different text.
- **Expected result:** Reject adapter snapshot contract violation before schema success.
- **Expected diagnostics:** TypeError.
- **Boundary / edge cases:** A matching source ID alone cannot certify declared digest alignment.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T076 — Cross-source index contract rejection

- **Test ID:** MOD-03-T076.
- **Scenario:** Cross-source index contract rejection.
- **Category:** Loader.
- **Objective:** Verify the specified cross-source index contract rejection behavior while preserving source/semantic separation.
- **Component:** SourceDecodeResult/LoadedAuthoringDocument.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Attach location index from a different source ID.
- **Expected result:** Reject result/snapshot contract mismatch.
- **Expected diagnostics:** ValueError.
- **Boundary / edge cases:** No silent source rebinding.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T077 — Legacy decoder without locations

- **Test ID:** MOD-03-T077.
- **Scenario:** Legacy decoder without locations.
- **Category:** Loader.
- **Objective:** Verify the specified legacy decoder without locations behavior while preserving source/semantic separation.
- **Component:** SourceDecodeResult.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Inject existing four-field decoder result with legacy positions only.
- **Expected result:** Load remains compatible; locations=None; exact legacy diagnostic position retained.
- **Expected diagnostics:** None for valid schema; existing schema errors retain original categories.
- **Boundary / edge cases:** No span fabricated from start position alone.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T078 — Legacy generated snapshot construction

- **Test ID:** MOD-03-T078.
- **Scenario:** Legacy generated snapshot construction.
- **Category:** Loader.
- **Objective:** Verify the specified legacy generated snapshot construction behavior while preserving source/semantic separation.
- **Component:** LoadedAuthoringDocument.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Construct loaded document with existing source/document arguments.
- **Expected result:** Optional locations defaults None; no new mandatory physical origin.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** This constructor is not a substitute for structural-validation certification.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T079 — Ordered multi-source indexes

- **Test ID:** MOD-03-T079.
- **Scenario:** Ordered multi-source indexes.
- **Category:** Loader.
- **Objective:** Verify the specified ordered multi-source indexes behavior while preserving source/semantic separation.
- **Component:** ModelLoader.load_many.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Load valid/invalid/valid sources in explicit order.
- **Expected result:** Preserve batch status/order; successful indexes and failures retain own source.
- **Expected diagnostics:** Original failure categories and primary/related locations.
- **Boundary / edge cases:** No index merging or semantic collision judgment.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T080 — Duplicate source IDs remain pre-acquisition failures

- **Test ID:** MOD-03-T080.
- **Scenario:** Duplicate source IDs remain pre-acquisition failures.
- **Category:** Loader.
- **Objective:** Verify the specified duplicate source ids remain pre-acquisition failures behavior while preserving source/semantic separation.
- **Component:** ModelLoader.load_many.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Submit same ID multiple times including file/memory variants.
- **Expected result:** Reject all occurrences before reading/parsing; no invented location.
- **Expected diagnostics:** MOD-LOAD-011 with original related input index.
- **Boundary / edge cases:** Physical related locations are not manufactured from batch input positions.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T081 — Missing/unreadable/oversized/encoding source

- **Test ID:** MOD-03-T081.
- **Scenario:** Missing/unreadable/oversized/encoding source.
- **Category:** Loader.
- **Objective:** Verify the specified missing/unreadable/oversized/encoding source behavior while preserving source/semantic separation.
- **Component:** Acquisition boundaries.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Exercise MOD-02 source acquisition failures.
- **Expected result:** Preserve existing failure categories with source metadata and absent unknown physical span.
- **Expected diagnostics:** MOD-LOAD-001/002/012/013 as appropriate.
- **Boundary / edge cases:** No decoder or source rewriting occurs.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T082 — Invalid type expression precise location

- **Test ID:** MOD-03-T082.
- **Scenario:** Invalid type expression precise location.
- **Category:** Diagnostic.
- **Objective:** Verify the specified invalid type expression precise location behavior while preserving source/semantic separation.
- **Component:** ModelLoadDiagnostic integration.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Submit an invalid type-expression node or primitive token at a known path.
- **Expected result:** Retain exact expression/token span selected by original MOD-01 diagnostic path.
- **Expected diagnostics:** MOD-LOAD-010 plus original MOD-SCHEMA diagnostic/cause.
- **Boundary / edge cases:** Tracking does not determine semantic type applicability.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T083 — Duplicate field ID related locations

- **Test ID:** MOD-03-T083.
- **Scenario:** Duplicate field ID related locations.
- **Category:** Diagnostic.
- **Objective:** Verify the specified duplicate field id related locations behavior while preserving source/semantic separation.
- **Component:** ModelLoadDiagnostic integration.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Repeat a field ID in one DataFacet.
- **Expected result:** Primary location points to conflicting ID value and related location to original ID value.
- **Expected diagnostics:** MOD-LOAD-010 / MOD-SCHEMA-013.
- **Boundary / edge cases:** Original schema path/related_path remain unchanged.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T084 — Duplicate name and constraint kind

- **Test ID:** MOD-03-T084.
- **Scenario:** Duplicate name and constraint kind.
- **Category:** Diagnostic.
- **Objective:** Verify the specified duplicate name and constraint kind behavior while preserving source/semantic separation.
- **Component:** ModelLoadDiagnostic integration.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Repeat field name/case collision and separately constraint kind.
- **Expected result:** Retain conflicting/original declaration value spans.
- **Expected diagnostics:** MOD-LOAD-010 with MOD-SCHEMA-013 or 011.
- **Boundary / edge cases:** No new uniqueness policy implemented in tracker.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T085 — Invalid constraint literal

- **Test ID:** MOD-03-T085.
- **Scenario:** Invalid constraint literal.
- **Category:** Diagnostic.
- **Objective:** Verify the specified invalid constraint literal behavior while preserving source/semantic separation.
- **Component:** ModelLoadDiagnostic integration.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use invalid exact integer/text or locally inconsistent constraint declaration.
- **Expected result:** Exact value path span or actual enclosing constraints span follows MOD-01 diagnostic.
- **Expected diagnostics:** MOD-LOAD-010 / MOD-SCHEMA-011.
- **Boundary / edge cases:** Precision applicability remains TYPE-06 concern, not MOD-03.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T086 — Unsupported facet kind

- **Test ID:** MOD-03-T086.
- **Scenario:** Unsupported facet kind.
- **Category:** Diagnostic.
- **Objective:** Verify the specified unsupported facet kind behavior while preserving source/semantic separation.
- **Component:** ModelLoadDiagnostic integration.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use unsupported facet kind value.
- **Expected result:** Locate the actual kind value token.
- **Expected diagnostics:** MOD-LOAD-010 / MOD-SCHEMA-006.
- **Boundary / edge cases:** No future facet parser extension enabled.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T087 — Missing required property uses parent

- **Test ID:** MOD-03-T087.
- **Scenario:** Missing required property uses parent.
- **Category:** Diagnostic.
- **Objective:** Verify the specified missing required property uses parent behavior while preserving source/semantic separation.
- **Component:** ModelLoadDiagnostic integration.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Remove required field/root property in otherwise parsed document.
- **Expected result:** Use nearest actual containing object span rather than invented missing token.
- **Expected diagnostics:** MOD-LOAD-010 / MOD-SCHEMA-002.
- **Boundary / edge cases:** This deliberately supersedes MOD-02 absence-only precision at the new revision.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T088 — Unknown property uses key span

- **Test ID:** MOD-03-T088.
- **Scenario:** Unknown property uses key span.
- **Category:** Diagnostic.
- **Objective:** Verify the specified unknown property uses key span behavior while preserving source/semantic separation.
- **Component:** ModelLoadDiagnostic integration.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Add __proto__, constructor or unsupported authoring property.
- **Expected result:** Locate original property key while retaining structural error.
- **Expected diagnostics:** MOD-LOAD-010 / MOD-SCHEMA-003.
- **Boundary / edge cases:** Plain dictionaries remain inert; no dynamic object construction.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T089 — Legacy position/span consistency

- **Test ID:** MOD-03-T089.
- **Scenario:** Legacy position/span consistency.
- **Category:** Diagnostic.
- **Objective:** Verify the specified legacy position/span consistency behavior while preserving source/semantic separation.
- **Component:** ModelLoadDiagnostic.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Supply source_location with no position and separately consistent/inconsistent positions.
- **Expected result:** Derive missing position from span start; reject inconsistent known coordinates/offsets.
- **Expected diagnostics:** ValueError for inconsistency.
- **Boundary / edge cases:** Old offset=None can coexist with same line/column known start offset.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T090 — Primary and related source association

- **Test ID:** MOD-03-T090.
- **Scenario:** Primary and related source association.
- **Category:** Diagnostic.
- **Objective:** Verify the specified primary and related source association behavior while preserving source/semantic separation.
- **Component:** ModelLoadDiagnostic.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use primary same-source location, immutable related locations and a mismatched primary source.
- **Expected result:** Retain related source identities; reject primary mismatch.
- **Expected diagnostics:** ValueError for primary mismatch; TypeError for invalid related objects.
- **Boundary / edge cases:** Future related cross-source diagnostics remain explicit, not index merging.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T091 — Deterministic error order retained

- **Test ID:** MOD-03-T091.
- **Scenario:** Deterministic error order retained.
- **Category:** Diagnostic.
- **Objective:** Verify the specified deterministic error order retained behavior while preserving source/semantic separation.
- **Component:** ModelLoadDiagnostic integration.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Load mixed structural errors and mixed source batch repeatedly.
- **Expected result:** Keep original MOD-01/entry diagnostic order and stable equivalent spans.
- **Expected diagnostics:** Original stable stage/code/path sequence.
- **Boundary / edge cases:** Index lexical enumeration does not reorder diagnostics.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T092 — Missing general SK-11 dependency remains explicit

- **Test ID:** MOD-03-T092.
- **Scenario:** Missing general SK-11 dependency remains explicit.
- **Category:** Diagnostic.
- **Objective:** Verify the specified missing general sk-11 dependency remains explicit behavior while preserving source/semantic separation.
- **Component:** Provisional SK-11 seam.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Inspect actual exported Kernel/authoring/loading contracts at pinned revision.
- **Expected result:** Use existing ModelLoadDiagnostic/AuthoringSchemaDiagnostic rather than invent generic SK-11 model.
- **Expected diagnostics:** No claim of full SK-11 completion.
- **Boundary / edge cases:** Future reconciliation must preserve primary/related locations and causes.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T093 — Immutable values and no parser AST leakage

- **Test ID:** MOD-03-T093.
- **Scenario:** Immutable values and no parser AST leakage.
- **Category:** Domain.
- **Objective:** Verify the specified immutable values and no parser ast leakage behavior while preserving source/semantic separation.
- **Component:** Frozen location contracts.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Attempt assignments and retained constructor collection mutations for every new value contract.
- **Expected result:** Frozen typed values, owned tuple/proxy collections remain immutable.
- **Expected diagnostics:** Documented mutation/contract errors.
- **Boundary / edge cases:** Private parser frames are mutable implementation state and never public domain data.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T094 — No unnecessary HTTP API or ORM

- **Test ID:** MOD-03-T094.
- **Scenario:** No unnecessary HTTP API or ORM.
- **Category:** Framework.
- **Objective:** Verify the specified no unnecessary http api or orm behavior while preserving source/semantic separation.
- **Component:** Django/DRF boundary.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Inspect production imports/routes after implementation.
- **Expected result:** No added endpoint, serializer, ORM model, source download or framework coupling.
- **Expected diagnostics:** No architectural framework leak.
- **Boundary / edge cases:** Django/DRF absent locally; no existing endpoint is extended in this task.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T095 — Future explicit HTTP exposure prerequisites

- **Test ID:** MOD-03-T095.
- **Scenario:** Future explicit HTTP exposure prerequisites.
- **Category:** Framework.
- **Objective:** Verify the specified future explicit http exposure prerequisites behavior while preserving source/semantic separation.
- **Component:** Future applicable DRF transport.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** If a later authorized endpoint exists, record its DRF Serializer and permission contract before executing transport checks.
- **Expected result:** Explicit optional span/related-location serialization preserving access controls; never ModelSerializer for pure values.
- **Expected diagnostics:** Existing API error conventions only at that future boundary.
- **Boundary / edge cases:** Conditional future scenario, not an implemented/current endpoint or test code.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T096 — No semantic processing or runtime dependency

- **Test ID:** MOD-03-T096.
- **Scenario:** No semantic processing or runtime dependency.
- **Category:** Architecture.
- **Objective:** Verify the specified no semantic processing or runtime dependency behavior while preserving source/semantic separation.
- **Component:** Source tracking dependency graph.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Inspect imports and instrument future authorized loading operation.
- **Expected result:** No lookup/resolver, canonicalizer, TypeRegistry, compiler/runtime execution, network, ORM/persistence or source-derived semantic ID.
- **Expected diagnostics:** No architecture violations or unintended semantic side effects.
- **Boundary / edge cases:** SemanticElement/TypeDefinition contracts are unchanged.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T097 — No ownership inference

- **Test ID:** MOD-03-T097.
- **Scenario:** No ownership inference.
- **Category:** Architecture.
- **Objective:** Verify the specified no ownership inference behavior while preserving source/semantic separation.
- **Component:** Source tracking vs provenance.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Load source with misleading tenant/org names and paths.
- **Expected result:** Location metadata carries source/span/digest only, without authority/approval/audit graph.
- **Expected diagnostics:** None for valid authoring document.
- **Boundary / edge cases:** Digest and source path do not prove semantic provenance or ownership.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T098 — Locate Customer and DataFacet

- **Test ID:** MOD-03-T098.
- **Scenario:** Locate Customer and DataFacet.
- **Category:** Mini Sales.
- **Objective:** Verify the specified locate customer and datafacet behavior while preserving source/semantic separation.
- **Component:** SourceLocationIndex.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Load existing JSON/YAML and lookup /definitions/0 and /definitions/0/facets/0.
- **Expected result:** Return actual parser-derived declaration/container locations.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Never hardcode line/column expectations from illustrative prompt syntax.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T099 — Locate fields and active expression

- **Test ID:** MOD-03-T099.
- **Scenario:** Locate fields and active expression.
- **Category:** Mini Sales.
- **Objective:** Verify the specified locate fields and active expression behavior while preserving source/semantic separation.
- **Component:** SourceLocationIndex.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Lookup name field, active type expression and creditLimit field paths from documented table.
- **Expected result:** Return correct separate lexical node spans with stable authored IDs unchanged.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Path addresses snapshot order, not identity across arbitrary edits.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T100 — Locate minimum precision scale declarations

- **Test ID:** MOD-03-T100.
- **Scenario:** Locate minimum precision scale declarations.
- **Category:** Mini Sales.
- **Objective:** Verify the specified locate minimum precision scale declarations behavior while preserving source/semantic separation.
- **Component:** SourceLocationIndex.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Lookup values/0, values/1, values/2 and each /value literal.
- **Expected result:** Return declaration versus literal spans from actual ordered constraint arrays.
- **Expected diagnostics:** None.
- **Boundary / edge cases:** Numeric minimum is quoted text; decoded literal length is not span length.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T101 — Mini Sales failure mapping

- **Test ID:** MOD-03-T101.
- **Scenario:** Mini Sales failure mapping.
- **Category:** Mini Sales.
- **Objective:** Verify the specified mini sales failure mapping behavior while preserving source/semantic separation.
- **Component:** ModelLoadDiagnostic integration.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Modify primitive or constraint literal and separately duplicate field ID.
- **Expected result:** No loaded snapshot; exact offending/related spans and schema causes retained.
- **Expected diagnostics:** MOD-LOAD-010 with original MOD-SCHEMA codes.
- **Boundary / edge cases:** No applicability judgment, canonical Customer registration or instance created.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T102 — Invalid escaped Unicode mapping key

- **Test ID:** MOD-03-T102.
- **Scenario:** Invalid escaped Unicode mapping key.
- **Category:** YAML.
- **Objective:** Verify the specified invalid escaped unicode mapping key behavior while preserving source/semantic separation.
- **Component:** YamlModelDecoder location adapter.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Use a quoted escaped lone-surrogate YAML property key.
- **Expected result:** Reject at actual key-node span before building invalid SourceNodePath.
- **Expected diagnostics:** MOD-LOAD-008.
- **Boundary / edge cases:** Valid supplementary Unicode keys remain compatible with plain-tree policy.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-03-T103 — Legacy positions and index start conflict

- **Test ID:** MOD-03-T103.
- **Scenario:** Legacy positions and index start conflict.
- **Category:** Loader.
- **Objective:** Verify the specified legacy positions and index start conflict behavior while preserving source/semantic separation.
- **Component:** SourceDecodeResult.
- **Prerequisites:** Shared authorized fixed-revision setup above; format/parser/fixture capabilities stated in this scenario available.
- **Input / setup:** Construct decoder result with same-source index and conflicting known line/column or offset in positions.
- **Expected result:** Reject inconsistent coexisting metadata at construction.
- **Expected diagnostics:** ValueError.
- **Boundary / edge cases:** Position-only results and matching positions with absent offsets remain compatible.
- **Integration dependencies:** Existing model_loader.public, MOD-01 authoring contracts, selected stdlib/PyYAML parser or explicitly stated provisional diagnostic/conditional future API boundary.
- **Acceptance criteria:** Exact stated expected values, span/source/path/diagnostic behavior and edge cases observed with recorded evidence; no fabricated location, mutation, unsupported success or unrelated semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

