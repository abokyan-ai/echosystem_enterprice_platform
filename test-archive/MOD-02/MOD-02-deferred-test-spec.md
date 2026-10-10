# MOD-02 — Model Loader: deferred test specification

Date: 2026-10-10 (UTC). Status: **DEFERRED / NOT VERIFIED**. Deferred tests executed: **0**.
Total documented cases: **109**; stable IDs MOD-02-T001 through MOD-02-T109.

## Shared prerequisites and exact fixture vocabulary

Future explicit execution authorization is required. Pin source/archive revisions, Python 3.11+ interpreter, module paths from architecture.json, PyYAML==6.0.3 when YAML is tested, effective filesystem user and platform capabilities. These cases are written specifications based on inspection, not recorded behavioral results. No new executable test infrastructure is introduced.

BASE is source text encoding the MOD-01 object with schemaVersion="1.0", context="sem_550e8400-e29b-41d4-a716-999999999999", namespace="sales", definitions=[]. TYPE/FIELD fixtures use the actual [Mini Sales JSON](../../examples/authoring/mini-sales.json) and [equivalent YAML](../../examples/authoring/mini-sales.yaml). Use valid distinct sem_/fld_ UUID-v4 values when creating new declarations; use the actual closed expression object and ordered constraint-array syntax. Source IDs are independent caller strings. Cases change only specified coordinates unless otherwise stated.

Construct sources with dedicated ModelSourceId and explicit json/yaml format; use ModelLoader.load/load_many. Assert source association, exact stage/code, original nested schema diagnostic/path/cause/related_path, position conventions, result shape and deterministic order. Anticipated errors yield no successful snapshot. Programmer configuration/contract misuse raises documented exceptions. Built-in decoders never execute source text.

Every case requires current provisional loading/authoring diagnostics or an explicitly reconciled future SK-11 revision to be recorded. Missing TYPE-01/TYPE-08/full SK-09 do not license mocked successful canonical behavior. File permissions must be exercised under an actually restricted effective user. No network is needed for loading; dependency setup uses approved package provisioning. Source resource limits and current YAML 1.1 policy must be recorded.

## Evidence policy

Every scenario initially has **NOT_RUN — DEFERRED**. Do not execute these cases, examples, comprehensive tests or CLI/runtime smoke cases during MOD-02. Future PASSED/FAILED requires actual command, date, revision, expected/observed behavior and evidence; preserve stable IDs/history. Static syntax/build/dependency/Fitness checks are separate and do not prove these scenarios. No next architecture stage starts automatically.

## MOD-02-T001 — Valid explicit memory source

- **Test ID / name:** MOD-02-T001 — Valid explicit memory source.
- **Category:** Sources.
- **Component / contract:** InMemoryModelSource/InMemorySourceProvider.
- **Objective:** Establish the specified valid explicit memory source behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Wrap BASE JSON text in source ID mini-sales, format json.
- **Expected behavior:** Acquire unchanged text and load one MOD-01 snapshot, with original ID.
- **Expected diagnostics for invalid cases:** None.
- **Boundary / edge cases:** Minimal empty definitions is valid; no filesystem calls.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T002 — Valid explicit file source

- **Test ID / name:** MOD-02-T002 — Valid explicit file source.
- **Category:** Sources.
- **Component / contract:** FileModelSource/LocalFileSourceProvider.
- **Objective:** Establish the specified valid explicit file source behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Write BASE UTF-8 JSON into a regular file; pass its exact path and ID.
- **Expected behavior:** Read text and retain original supplied path in result metadata.
- **Expected diagnostics for invalid cases:** None.
- **Boundary / edge cases:** Relative and absolute paths; caller working directory is explicit.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T003 — Missing source file

- **Test ID / name:** MOD-02-T003 — Missing source file.
- **Category:** Sources.
- **Component / contract:** LocalFileSourceProvider.
- **Objective:** Establish the specified missing source file behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Supply a nonexistent explicit regular-file path.
- **Expected behavior:** Return acquisition failure, no loaded document.
- **Expected diagnostics for invalid cases:** MOD-LOAD-001, stage acquisition.
- **Boundary / edge cases:** Missing parent directory also produces source-associated failure.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T004 — Unreadable source file

- **Test ID / name:** MOD-02-T004 — Unreadable source file.
- **Category:** Sources.
- **Component / contract:** LocalFileSourceProvider.
- **Objective:** Establish the specified unreadable source file behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use an effective user that lacks read permission on a real file.
- **Expected behavior:** Return acquisition failure and close any acquired descriptor.
- **Expected diagnostics for invalid cases:** MOD-LOAD-002.
- **Boundary / edge cases:** A root user may bypass permission modes; fixture must enforce effective denial.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T005 — Directory is not a document

- **Test ID / name:** MOD-02-T005 — Directory is not a document.
- **Category:** Sources.
- **Component / contract:** LocalFileSourceProvider.
- **Objective:** Establish the specified directory is not a document behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Supply an existing directory path.
- **Expected behavior:** Reject without treating it as empty authoring content.
- **Expected diagnostics for invalid cases:** MOD-LOAD-002.
- **Boundary / edge cases:** Platform open may fail before regular-file inspection.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T006 — FIFO does not block

- **Test ID / name:** MOD-02-T006 — FIFO does not block.
- **Category:** Sources.
- **Component / contract:** LocalFileSourceProvider.
- **Objective:** Establish the specified fifo does not block behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Create a FIFO without a writer and submit it on an O_NONBLOCK-capable OS.
- **Expected behavior:** Reject as nonregular source without waiting for a writer.
- **Expected diagnostics for invalid cases:** MOD-LOAD-002.
- **Boundary / edge cases:** Document platform capability; no FIFO fixture on unsupported systems.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T007 — Symlink to regular file

- **Test ID / name:** MOD-02-T007 — Symlink to regular file.
- **Category:** Sources.
- **Component / contract:** LocalFileSourceProvider.
- **Objective:** Establish the specified symlink to regular file behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit a symlink path pointing to BASE regular file.
- **Expected behavior:** Read target while retaining supplied link path, with no semantic inference.
- **Expected diagnostics for invalid cases:** None.
- **Boundary / edge cases:** Broken link returns MOD-LOAD-001; access confinement belongs to caller.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T008 — Empty source

- **Test ID / name:** MOD-02-T008 — Empty source.
- **Category:** Sources.
- **Component / contract:** check_text.
- **Objective:** Establish the specified empty source behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit empty memory text and separately a zero-byte file.
- **Expected behavior:** Fail acquisition; do not return an empty model.
- **Expected diagnostics for invalid cases:** MOD-LOAD-004.
- **Boundary / edge cases:** Distinguish empty content from valid definitions=[].
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T009 — Whitespace-only source

- **Test ID / name:** MOD-02-T009 — Whitespace-only source.
- **Category:** Sources.
- **Component / contract:** check_text.
- **Objective:** Establish the specified whitespace-only source behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit spaces, tabs and newlines only.
- **Expected behavior:** Fail acquisition before either parser.
- **Expected diagnostics for invalid cases:** MOD-LOAD-004.
- **Boundary / edge cases:** At-size-boundary whitespace still cannot become success.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T010 — Dedicated source identity syntax

- **Test ID / name:** MOD-02-T010 — Dedicated source identity syntax.
- **Category:** Sources.
- **Component / contract:** ModelSourceId.
- **Objective:** Establish the specified dedicated source identity syntax behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Construct IDs with empty text, outer whitespace, control/DEL, nontext or >256 characters.
- **Expected behavior:** Reject invalid constructor inputs with ValueError; no generated identity.
- **Expected diagnostics for invalid cases:** ValueError before any source-associated result exists.
- **Boundary / edge cases:** One and 256 characters accepted; 257 rejected; internal spaces and Unicode allowed.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T011 — Case-sensitive operation identity

- **Test ID / name:** MOD-02-T011 — Case-sensitive operation identity.
- **Category:** Sources.
- **Component / contract:** ModelSourceId.
- **Objective:** Establish the specified case-sensitive operation identity behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit sources named Sales and sales in one batch.
- **Expected behavior:** Treat IDs as distinct and preserve both in input order.
- **Expected diagnostics for invalid cases:** None if both documents valid.
- **Boundary / edge cases:** No normalization, UUID generation or global uniqueness promise.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T012 — Explicit format overrides filename

- **Test ID / name:** MOD-02-T012 — Explicit format overrides filename.
- **Category:** Sources.
- **Component / contract:** ModelSourceFormat/ModelLoader.
- **Objective:** Establish the specified explicit format overrides filename behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Put JSON BASE in a .yaml file and submit explicit json.
- **Expected behavior:** Decode using JSON and retain original path.
- **Expected diagnostics for invalid cases:** None.
- **Boundary / edge cases:** Conversely select yaml explicitly; extension never determines dispatch.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T013 — Unsupported explicit format

- **Test ID / name:** MOD-02-T013 — Unsupported explicit format.
- **Category:** Sources.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified unsupported explicit format behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit formats xml, JSON, yml and unknown against a nonexistent file.
- **Expected behavior:** Reject before opening file; never guess a parser.
- **Expected diagnostics for invalid cases:** MOD-LOAD-003, stage decoding.
- **Boundary / edge cases:** Nonempty format accepted by source contract but closed loader dispatch.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T014 — Filename never creates semantics

- **Test ID / name:** MOD-02-T014 — Filename never creates semantics.
- **Category:** Sources.
- **Component / contract:** FileModelSource.
- **Objective:** Establish the specified filename never creates semantics behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Load BASE through misleading tenant/org/namespace/customer path names.
- **Expected behavior:** Only explicit document context/namespace/IDs define authoring values.
- **Expected diagnostics for invalid cases:** None.
- **Boundary / edge cases:** Different paths yield same authoring values and distinct source metadata.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T015 — Source contract misuse

- **Test ID / name:** MOD-02-T015 — Source contract misuse.
- **Category:** Sources.
- **Component / contract:** FileModelSource/InMemoryModelSource.
- **Objective:** Establish the specified source contract misuse behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use NUL path, blank path, parsed tree as content or non-source object with load.
- **Expected behavior:** Reject caller contract misuse before acquisition.
- **Expected diagnostics for invalid cases:** ValueError for NUL; TypeError for invalid metadata/content/source kind.
- **Boundary / edge cases:** Unsupported nonempty format remains a structured failure, not constructor misuse.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T016 — Explicit byte ceiling

- **Test ID / name:** MOD-02-T016 — Explicit byte ceiling.
- **Category:** Sources.
- **Component / contract:** ModelLoadOptions.
- **Objective:** Establish the specified explicit byte ceiling behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Supply ASCII source at byte limit and one byte over, with a valid schema padded by whitespace.
- **Expected behavior:** Boundary source may load; over-limit source fails before decode.
- **Expected diagnostics for invalid cases:** Over limit MOD-LOAD-012, stage acquisition.
- **Boundary / edge cases:** File read max is limit plus one, never unbounded.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T017 — UTF-8 multibyte accounting

- **Test ID / name:** MOD-02-T017 — UTF-8 multibyte accounting.
- **Category:** Sources.
- **Component / contract:** check_text.
- **Objective:** Establish the specified utf-8 multibyte accounting behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use non-ASCII source text with character length below limit but encoded length above.
- **Expected behavior:** Reject based on UTF-8 bytes.
- **Expected diagnostics for invalid cases:** MOD-LOAD-012.
- **Boundary / edge cases:** Exact encoded boundary accepted subject to schema validity.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T018 — File grows during bounded read

- **Test ID / name:** MOD-02-T018 — File grows during bounded read.
- **Category:** Sources.
- **Component / contract:** LocalFileSourceProvider.
- **Objective:** Establish the specified file grows during bounded read behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Arrange a file to grow after descriptor metadata check.
- **Expected behavior:** Read at most max_source_bytes+1 and reject over-limit content.
- **Expected diagnostics for invalid cases:** MOD-LOAD-012.
- **Boundary / edge cases:** No atomic source revision or external checksum is promised.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T019 — Limit configuration rejects invalid values

- **Test ID / name:** MOD-02-T019 — Limit configuration rejects invalid values.
- **Category:** Sources.
- **Component / contract:** ModelLoadOptions.
- **Objective:** Establish the specified limit configuration rejects invalid values behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Construct options with zero, negative, bool, float and max_depth=129.
- **Expected behavior:** Reject configuration with ValueError.
- **Expected diagnostics for invalid cases:** No source diagnostic for programmer options misuse.
- **Boundary / edge cases:** Depth 128 accepted; positive custom size/node ceilings explicit.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T020 — Descriptor cleanup on all branches

- **Test ID / name:** MOD-02-T020 — Descriptor cleanup on all branches.
- **Category:** Sources.
- **Component / contract:** LocalFileSourceProvider.
- **Objective:** Establish the specified descriptor cleanup on all branches behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Instrument descriptor lifetime for success, too-large, nonregular, invalid encoding and read error.
- **Expected behavior:** No owned descriptor leak after any outcome.
- **Expected diagnostics for invalid cases:** Original source failure category retained.
- **Boundary / edge cases:** Ownership transfer to fdopen must not double-close.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T021 — Strict JSON Mini Sales

- **Test ID / name:** MOD-02-T021 — Strict JSON Mini Sales.
- **Category:** JSON.
- **Component / contract:** JsonModelDecoder.
- **Objective:** Establish the specified strict json mini sales behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use existing mini-sales.json as explicit memory or file JSON source.
- **Expected behavior:** Produce one typed authoring document preserving authored order and literals.
- **Expected diagnostics for invalid cases:** None.
- **Boundary / edge cases:** Do not compare or execute this example during implementation.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T022 — Malformed syntax coordinates

- **Test ID / name:** MOD-02-T022 — Malformed syntax coordinates.
- **Category:** JSON.
- **Component / contract:** JsonModelDecoder.
- **Objective:** Establish the specified malformed syntax coordinates behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use missing value/comma and malformed escaping on a known line.
- **Expected behavior:** Return decode failure with genuine one-based parser coordinates.
- **Expected diagnostics for invalid cases:** MOD-LOAD-005, stage decoding.
- **Boundary / edge cases:** Unicode preceding position counts characters rather than bytes.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T023 — Non-object roots

- **Test ID / name:** MOD-02-T023 — Non-object roots.
- **Category:** JSON.
- **Component / contract:** JsonModelDecoder.
- **Objective:** Establish the specified non-object roots behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit null, [], string, number and true as complete JSON texts.
- **Expected behavior:** Reject decoded root without constructing authoring snapshot.
- **Expected diagnostics for invalid cases:** MOD-LOAD-009.
- **Boundary / edge cases:** Empty object is object-shaped and proceeds to MOD-01 missing properties.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T024 — JSON comments and trailing commas

- **Test ID / name:** MOD-02-T024 — JSON comments and trailing commas.
- **Category:** JSON.
- **Component / contract:** JsonModelDecoder.
- **Objective:** Establish the specified json comments and trailing commas behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit commented JSON and trailing comma in root/nested arrays.
- **Expected behavior:** Strict parser rejects each source without YAML fallback.
- **Expected diagnostics for invalid cases:** MOD-LOAD-005.
- **Boundary / edge cases:** Comment-like characters inside quoted strings remain normal text.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T025 — Duplicate root object keys

- **Test ID / name:** MOD-02-T025 — Duplicate root object keys.
- **Category:** JSON.
- **Component / contract:** JsonModelDecoder.
- **Objective:** Establish the specified duplicate root object keys behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit two schemaVersion properties with equal and different values.
- **Expected behavior:** Reject both duplicates; never silently pick first/last.
- **Expected diagnostics for invalid cases:** MOD-LOAD-006; no invented key line/column.
- **Boundary / edge cases:** Escaped equivalent key spellings count as duplicates after decoding.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T026 — Duplicate nested object keys

- **Test ID / name:** MOD-02-T026 — Duplicate nested object keys.
- **Category:** JSON.
- **Component / contract:** JsonModelDecoder.
- **Objective:** Establish the specified duplicate nested object keys behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Repeat name in a field or kind in a type-expression object.
- **Expected behavior:** Reject during decoding before structural judgment.
- **Expected diagnostics for invalid cases:** MOD-LOAD-006.
- **Boundary / edge cases:** Repeated values in arrays remain MOD-01 or later-boundary concerns.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T027 — No executable expressions

- **Test ID / name:** MOD-02-T027 — No executable expressions.
- **Category:** JSON.
- **Component / contract:** JsonModelDecoder.
- **Objective:** Establish the specified no executable expressions behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Supply JavaScript expressions/function literals instead of JSON values.
- **Expected behavior:** Fail syntax; no eval/object deserialization runs.
- **Expected diagnostics for invalid cases:** MOD-LOAD-005.
- **Boundary / edge cases:** Executable-looking text inside a string remains inert and schema-governed.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T028 — Nonstandard numeric constants

- **Test ID / name:** MOD-02-T028 — Nonstandard numeric constants.
- **Category:** JSON.
- **Component / contract:** JsonModelDecoder.
- **Objective:** Establish the specified nonstandard numeric constants behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use NaN, Infinity and -Infinity in nested values.
- **Expected behavior:** Reject nonstandard constants, even if schema would otherwise reject them.
- **Expected diagnostics for invalid cases:** MOD-LOAD-008.
- **Boundary / edge cases:** Quoted versions are inert strings and proceed to MOD-01.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T029 — JSON float overflow

- **Test ID / name:** MOD-02-T029 — JSON float overflow.
- **Category:** JSON.
- **Component / contract:** inspect_tree.
- **Objective:** Establish the specified json float overflow behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use a JSON numeric literal such as 1e9999 inside a candidate.
- **Expected behavior:** Reject non-finite decoded float.
- **Expected diagnostics for invalid cases:** MOD-LOAD-008.
- **Boundary / edge cases:** Finite floats are JSON-compatible but may fail MOD-01 exact-int constraints.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T030 — JSON depth limits before parse

- **Test ID / name:** MOD-02-T030 — JSON depth limits before parse.
- **Category:** JSON.
- **Component / contract:** json_depth/inspect_tree.
- **Objective:** Establish the specified json depth limits before parse behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Construct nested arrays/objects at and beyond configured depth.
- **Expected behavior:** Reject exceeding container preflight or full-tree levels.
- **Expected diagnostics for invalid cases:** MOD-LOAD-014.
- **Boundary / edge cases:** Braces and escaped quotes inside strings must not affect preflight nesting.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T031 — JSON node and key budget

- **Test ID / name:** MOD-02-T031 — JSON node and key budget.
- **Category:** JSON.
- **Component / contract:** inspect_tree.
- **Objective:** Establish the specified json node and key budget behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use a wide plain object/array exceeding max_nodes.
- **Expected behavior:** Reject with node complexity diagnostic before schema projection.
- **Expected diagnostics for invalid cases:** MOD-LOAD-014.
- **Boundary / edge cases:** Mapping keys count in addition to values/containers; root level is one.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T032 — Interpreter integer conversion limit

- **Test ID / name:** MOD-02-T032 — Interpreter integer conversion limit.
- **Category:** JSON.
- **Component / contract:** JsonModelDecoder.
- **Objective:** Establish the specified interpreter integer conversion limit behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit an integer literal beyond configured interpreter conversion ceiling.
- **Expected behavior:** Contain ValueError as parser numeric-resource failure.
- **Expected diagnostics for invalid cases:** MOD-LOAD-014.
- **Boundary / edge cases:** Record Python integer limit; do not change global interpreter configuration.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T033 — Multiple JSON values

- **Test ID / name:** MOD-02-T033 — Multiple JSON values.
- **Category:** JSON.
- **Component / contract:** JsonModelDecoder.
- **Objective:** Establish the specified multiple json values behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit two consecutive JSON documents in one source.
- **Expected behavior:** Fail strict extra-data parsing rather than returning first document.
- **Expected diagnostics for invalid cases:** MOD-LOAD-005.
- **Boundary / edge cases:** Whitespace after a single document is allowed.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T034 — Escaped surrogate Unicode

- **Test ID / name:** MOD-02-T034 — Escaped surrogate Unicode.
- **Category:** JSON.
- **Component / contract:** inspect_tree.
- **Objective:** Establish the specified escaped surrogate unicode behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit unpaired escaped high/low surrogate in a string/key.
- **Expected behavior:** Reject invalid Unicode scalar values after JSON decode.
- **Expected diagnostics for invalid cases:** MOD-LOAD-013 for string values; MOD-LOAD-008 for invalid object keys.
- **Boundary / edge cases:** A valid paired supplementary character remains compatible.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T035 — SafeLoader Mini Sales

- **Test ID / name:** MOD-02-T035 — SafeLoader Mini Sales.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified safeloader mini sales behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use mini-sales.yaml with pinned PyYAML available.
- **Expected behavior:** Project only plain values and construct MOD-01 authoring snapshot.
- **Expected diagnostics for invalid cases:** None.
- **Boundary / edge cases:** Quoted minimum "0" and schemaVersion "1.0" remain strings.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T036 — Malformed YAML coordinates

- **Test ID / name:** MOD-02-T036 — Malformed YAML coordinates.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified malformed yaml coordinates behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit broken indentation/flow syntax with known source marks.
- **Expected behavior:** Fail decoding and preserve available parser problem_mark.
- **Expected diagnostics for invalid cases:** MOD-LOAD-005.
- **Boundary / edge cases:** If parser has no problem_mark, position remains None.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T037 — Duplicate YAML mapping keys

- **Test ID / name:** MOD-02-T037 — Duplicate YAML mapping keys.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified duplicate yaml mapping keys behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Repeat root schemaVersion and separately nested field name.
- **Expected behavior:** Reject decoded duplicate string keys during projection.
- **Expected diagnostics for invalid cases:** MOD-LOAD-006 with second key mark.
- **Boundary / edge cases:** Equal repeated values still fail; quoted/unquoted equivalent strings collide.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T038 — Multiple YAML documents

- **Test ID / name:** MOD-02-T038 — Multiple YAML documents.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified multiple yaml documents behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit two documents separated by --- including empty second document.
- **Expected behavior:** Reject the source as one decode failure.
- **Expected diagnostics for invalid cases:** MOD-LOAD-007 at second document start.
- **Boundary / edge cases:** One document with optional start/end markers remains allowed.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T039 — Unsafe/custom tags

- **Test ID / name:** MOD-02-T039 — Unsafe/custom tags.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified unsafe/custom tags behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit !!python/object, !custom and executable tag examples.
- **Expected behavior:** Reject event tag before any construction.
- **Expected diagnostics for invalid cases:** MOD-LOAD-008 with event mark.
- **Boundary / edge cases:** No application class construction or arbitrary Python object allowed.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T040 — Explicit standard tags rejected

- **Test ID / name:** MOD-02-T040 — Explicit standard tags rejected.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified explicit standard tags rejected behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit !!str, !!int and !!map explicit safe tags.
- **Expected behavior:** Reject according to stricter v0 no-explicit-tags policy.
- **Expected diagnostics for invalid cases:** MOD-LOAD-008.
- **Boundary / edge cases:** Implicit safe node tags remain supported.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T041 — Anchors and aliases rejected

- **Test ID / name:** MOD-02-T041 — Anchors and aliases rejected.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified anchors and aliases rejected behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit an anchor alone and separately alias reuse.
- **Expected behavior:** Reject all anchored/alias constructs before composition.
- **Expected diagnostics for invalid cases:** MOD-LOAD-008.
- **Boundary / edge cases:** No expansion, shared object tree or implicit copy semantics.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T042 — Recursive alias rejection

- **Test ID / name:** MOD-02-T042 — Recursive alias rejection.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified recursive alias rejection behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit root anchor referencing itself and multi-anchor cycles.
- **Expected behavior:** Reject safely before recursive projection.
- **Expected diagnostics for invalid cases:** MOD-LOAD-008.
- **Boundary / edge cases:** No RecursionError should escape anticipated alias handling.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T043 — Alias amplification rejection

- **Test ID / name:** MOD-02-T043 — Alias amplification rejection.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified alias amplification rejection behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit an alias expansion bomb with many references.
- **Expected behavior:** Reject first anchor/alias instead of expanding.
- **Expected diagnostics for invalid cases:** MOD-LOAD-008.
- **Boundary / edge cases:** Keep input under byte limit to isolate construct handling.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T044 — Merge keys unsupported

- **Test ID / name:** MOD-02-T044 — Merge keys unsupported.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified merge keys unsupported behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit << mapping key with a mapping value and no anchors.
- **Expected behavior:** Reject non-string merge-tagged key.
- **Expected diagnostics for invalid cases:** MOD-LOAD-008.
- **Boundary / edge cases:** Quoted "<<" is a plain unknown property handled by MOD-01.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T045 — Implicit timestamp not a native object

- **Test ID / name:** MOD-02-T045 — Implicit timestamp not a native object.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified implicit timestamp not a native object behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit unquoted YAML date/timestamp scalar in candidate.
- **Expected behavior:** Reject unsupported scalar node before construction.
- **Expected diagnostics for invalid cases:** MOD-LOAD-008; quote dates to preserve text.
- **Boundary / edge cases:** Quoted dates can reach schema rules as strings.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T046 — Sets and binary unsupported

- **Test ID / name:** MOD-02-T046 — Sets and binary unsupported.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified sets and binary unsupported behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit YAML set/binary node syntax.
- **Expected behavior:** Reject explicit tag or unsupported collection/scalar.
- **Expected diagnostics for invalid cases:** MOD-LOAD-008.
- **Boundary / edge cases:** No bytes/set/native object may reach MOD-01.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T047 — Non-string mapping keys

- **Test ID / name:** MOD-02-T047 — Non-string mapping keys.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified non-string mapping keys behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use numeric, boolean, null and complex sequence keys.
- **Expected behavior:** Reject keys instead of coercing or overwriting.
- **Expected diagnostics for invalid cases:** MOD-LOAD-008.
- **Boundary / edge cases:** Quoted string keys remain plain strings and schema-governed.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T048 — YAML 1.1 scalar policy

- **Test ID / name:** MOD-02-T048 — YAML 1.1 scalar policy.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified yaml 1.1 scalar policy behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use unquoted yes/no/on/off, leading-zero integer and quoted equivalents.
- **Expected behavior:** Follow documented SafeLoader 1.1 resolution, then MOD-01 exact scalar judgment.
- **Expected diagnostics for invalid cases:** Schema mismatches MOD-LOAD-010 with original MOD-SCHEMA code.
- **Boundary / edge cases:** Do not claim YAML 1.2 behavior; authoring strings require quoting.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T049 — YAML version/tag directives

- **Test ID / name:** MOD-02-T049 — YAML version/tag directives.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified yaml version/tag directives behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit %YAML 1.1; separately %YAML 1.2 and %TAG directive.
- **Expected behavior:** Allow 1.1 only; reject other version/tag directives.
- **Expected diagnostics for invalid cases:** Unsupported directives MOD-LOAD-008.
- **Boundary / edge cases:** No directive defaults to documented 1.1 resolution.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T050 — Non-finite YAML floats

- **Test ID / name:** MOD-02-T050 — Non-finite YAML floats.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified non-finite yaml floats behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit .nan, .inf and -.inf as unquoted scalar values.
- **Expected behavior:** Reject after compatible scalar projection.
- **Expected diagnostics for invalid cases:** MOD-LOAD-008.
- **Boundary / edge cases:** Quoted tokens are inert strings judged by schema.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T051 — YAML excessive nesting

- **Test ID / name:** MOD-02-T051 — YAML excessive nesting.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified yaml excessive nesting behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Build a no-alias nested mapping/sequence beyond max_depth.
- **Expected behavior:** Event preflight rejects before composition/project recursion.
- **Expected diagnostics for invalid cases:** MOD-LOAD-014 at actual event mark.
- **Boundary / edge cases:** Full-tree scalar depth is checked after projection as well.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T052 — YAML excessive node count

- **Test ID / name:** MOD-02-T052 — YAML excessive node count.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified yaml excessive node count behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use a wide mapping/sequence beyond max_nodes.
- **Expected behavior:** Reject event count or full plain-tree complexity.
- **Expected diagnostics for invalid cases:** MOD-LOAD-014.
- **Boundary / edge cases:** Mapping key scalar events consume budget too.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T053 — YAML scalar/array/null roots

- **Test ID / name:** MOD-02-T053 — YAML scalar/array/null roots.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified yaml scalar/array/null roots behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Supply a single string, sequence or null YAML document.
- **Expected behavior:** Reject root as non-object.
- **Expected diagnostics for invalid cases:** MOD-LOAD-009.
- **Boundary / edge cases:** A comment-only stream is not a successful empty authoring document.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T054 — Missing parser dependency

- **Test ID / name:** MOD-02-T054 — Missing parser dependency.
- **Category:** YAML.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified missing parser dependency behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Arrange an isolated environment without PyYAML and request YAML.
- **Expected behavior:** Return explicit dependency-unavailable decode failure; JSON still works.
- **Expected diagnostics for invalid cases:** MOD-LOAD-003.
- **Boundary / edge cases:** Contract/public import remains possible; no automatic pip install inside loader.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T055 — Valid minimal document

- **Test ID / name:** MOD-02-T055 — Valid minimal document.
- **Category:** Schema.
- **Component / contract:** ModelLoader/AuthoringSchemaValidator.
- **Objective:** Establish the specified valid minimal document behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Load BASE in both explicit formats.
- **Expected behavior:** Delegate once and return AuthoringModelDocument with empty definitions.
- **Expected diagnostics for invalid cases:** None.
- **Boundary / edge cases:** No canonical TypeDefinition construction.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T056 — Missing schema version

- **Test ID / name:** MOD-02-T056 — Missing schema version.
- **Category:** Schema.
- **Component / contract:** AuthoringSchemaValidator integration.
- **Objective:** Establish the specified missing schema version behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Remove schemaVersion from BASE.
- **Expected behavior:** No loaded snapshot; retain original structural error/path.
- **Expected diagnostics for invalid cases:** MOD-LOAD-010 wrapping MOD-SCHEMA-002.
- **Boundary / edge cases:** Missing property has no fabricated YAML node location.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T057 — Unsupported schema version

- **Test ID / name:** MOD-02-T057 — Unsupported schema version.
- **Category:** Schema.
- **Component / contract:** AuthoringSchemaValidator integration.
- **Objective:** Establish the specified unsupported schema version behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Set schemaVersion to "999.0" in otherwise valid BASE.
- **Expected behavior:** Reject structure rather than calling it a decoder syntax error.
- **Expected diagnostics for invalid cases:** MOD-LOAD-010 wrapping MOD-SCHEMA-004.
- **Boundary / edge cases:** No automatic schema upgrade/correction.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T058 — Invalid type declaration

- **Test ID / name:** MOD-02-T058 — Invalid type declaration.
- **Category:** Schema.
- **Component / contract:** AuthoringSchemaValidator integration.
- **Objective:** Establish the specified invalid type declaration behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use a definition kind action or omit required type version.
- **Expected behavior:** Reuse MOD-01 exact kind/shape rules.
- **Expected diagnostics for invalid cases:** MOD-LOAD-010 with MOD-SCHEMA-005 or MOD-SCHEMA-002.
- **Boundary / edge cases:** Do not create a second schema inside loader.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T059 — Duplicate field identity

- **Test ID / name:** MOD-02-T059 — Duplicate field identity.
- **Category:** Schema.
- **Component / contract:** AuthoringSchemaValidator integration.
- **Objective:** Establish the specified duplicate field identity behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Repeat a canonical FieldId within Mini Sales data fields.
- **Expected behavior:** Reject through MOD-01; preserve related first path.
- **Expected diagnostics for invalid cases:** MOD-LOAD-010 wrapping MOD-SCHEMA-013.
- **Boundary / edge cases:** Case-normalized UUID spelling still collides.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T060 — Field name portability collision

- **Test ID / name:** MOD-02-T060 — Field name portability collision.
- **Category:** Schema.
- **Component / contract:** AuthoringSchemaValidator integration.
- **Objective:** Establish the specified field name portability collision behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use same name and separately ASCII case-only field-name variations.
- **Expected behavior:** Reject structural collision via MOD-01.
- **Expected diagnostics for invalid cases:** MOD-LOAD-010 wrapping MOD-SCHEMA-013.
- **Boundary / edge cases:** No loader-specific uniqueness policy.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T061 — Unsupported primitive

- **Test ID / name:** MOD-02-T061 — Unsupported primitive.
- **Category:** Schema.
- **Component / contract:** AuthoringSchemaValidator integration.
- **Objective:** Establish the specified unsupported primitive behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Set primitive expression vocabulary to object.
- **Expected behavior:** Parser succeeds; MOD-01 rejects primitive.
- **Expected diagnostics for invalid cases:** MOD-LOAD-010 wrapping MOD-SCHEMA-009.
- **Boundary / edge cases:** Unknown bare primitive text also fails structural shape.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T062 — Unsupported facet or repeated data facet

- **Test ID / name:** MOD-02-T062 — Unsupported facet or repeated data facet.
- **Category:** Schema.
- **Component / contract:** AuthoringSchemaValidator integration.
- **Objective:** Establish the specified unsupported facet or repeated data facet behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use ui facet; separately two data facets on same declaration.
- **Expected behavior:** Delegate facet vocabulary/multiplicity policy.
- **Expected diagnostics for invalid cases:** MOD-LOAD-010 wrapping MOD-SCHEMA-006 or MOD-SCHEMA-014.
- **Boundary / edge cases:** No future facet extension bag.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T063 — Invalid constraint payload

- **Test ID / name:** MOD-02-T063 — Invalid constraint payload.
- **Category:** Schema.
- **Component / contract:** AuthoringSchemaValidator integration.
- **Objective:** Establish the specified invalid constraint payload behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use boolean precision, duplicate constraint kind, negative max-length or scale above precision.
- **Expected behavior:** Delegate payload/local-consistency rules.
- **Expected diagnostics for invalid cases:** MOD-LOAD-010 wrapping MOD-SCHEMA-011.
- **Boundary / edge cases:** Exact numeric bounds remain quoted strings; no float substitution.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T064 — Unresolved semantic name retained

- **Test ID / name:** MOD-02-T064 — Unresolved semantic name retained.
- **Category:** Schema.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified unresolved semantic name retained behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use semantic-name Employee and qualified hr.Employee with no lookup installed.
- **Expected behavior:** Successful authoring load retaining exact name text.
- **Expected diagnostics for invalid cases:** None if structurally valid.
- **Boundary / edge cases:** No missing-target diagnostic, registry lookup or name binding.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T065 — Explicit identity and version expression retained

- **Test ID / name:** MOD-02-T065 — Explicit identity and version expression retained.
- **Category:** Schema.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified explicit identity and version expression retained behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use semantic-id and semantic-version expressions with valid missing targets.
- **Expected behavior:** Keep existing Kernel reference contract and exact declared version pin.
- **Expected diagnostics for invalid cases:** None if structurally valid.
- **Boundary / edge cases:** No target existence check or latest-version selection.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T066 — Authored identity spelling/order retained

- **Test ID / name:** MOD-02-T066 — Authored identity spelling/order retained.
- **Category:** Schema.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified authored identity spelling/order retained behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use uppercase UUID hex, numeric bound "001.000" and noncanonical declaration order.
- **Expected behavior:** Retain MOD-01 authoring text/literal order and established context semantics.
- **Expected diagnostics for invalid cases:** None subject to current MOD-01 syntax/local consistency.
- **Boundary / edge cases:** Do not claim no canonicalization of Kernel context/reference value constructors.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T067 — Source cannot supply missing semantic declarations

- **Test ID / name:** MOD-02-T067 — Source cannot supply missing semantic declarations.
- **Category:** Schema.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified source cannot supply missing semantic declarations behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Remove namespace/context/ID and use descriptive path names.
- **Expected behavior:** Fail schema; never synthesize values from source metadata.
- **Expected diagnostics for invalid cases:** MOD-LOAD-010 with delegated missing-property diagnostics.
- **Boundary / edge cases:** No tenant/organization inference.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T068 — No TYPE-06 applicability during loading

- **Test ID / name:** MOD-02-T068 — No TYPE-06 applicability during loading.
- **Category:** Schema.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified no type-06 applicability during loading behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use string primitive with positive precision constraint declaration.
- **Expected behavior:** Accept structurally valid authoring data; semantic applicability belongs later.
- **Expected diagnostics for invalid cases:** None under MOD-01 structural contract.
- **Boundary / edge cases:** Do not weaken actual TYPE-06 production rules.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T069 — Unknown/prototype-like keys

- **Test ID / name:** MOD-02-T069 — Unknown/prototype-like keys.
- **Category:** Schema.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified unknown/prototype-like keys behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Add __proto__, constructor, prototype and tenantId at root/nested known objects.
- **Expected behavior:** Plain parser maps remain safe; MOD-01 rejects unknown properties.
- **Expected diagnostics for invalid cases:** MOD-LOAD-010 wrapping MOD-SCHEMA-003.
- **Boundary / edge cases:** No dynamic object spread, attribute assignment or prototype mutation.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T070 — Deterministic aggregate schema diagnostics

- **Test ID / name:** MOD-02-T070 — Deterministic aggregate schema diagnostics.
- **Category:** Schema.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified deterministic aggregate schema diagnostics behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Combine missing required root keys, sorted unknown keys and invalid ordered declarations.
- **Expected behavior:** Preserve MOD-01 diagnostic sequence, causes and related paths.
- **Expected diagnostics for invalid cases:** Ordered MOD-LOAD-010 wrappers, original schema diagnostics unchanged.
- **Boundary / edge cases:** Source association added without rewriting semantic diagnostic codes.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T071 — Multiple valid sources

- **Test ID / name:** MOD-02-T071 — Multiple valid sources.
- **Category:** Batch.
- **Component / contract:** ModelLoader.load_many.
- **Objective:** Establish the specified multiple valid sources behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit three distinct IDs with valid documents in specified order.
- **Expected behavior:** ALL_LOADED; entries and successful_documents keep source order.
- **Expected diagnostics for invalid cases:** None.
- **Boundary / edge cases:** Synchronous operation has no asynchronous completion ordering.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T072 — Mixed success and failure

- **Test ID / name:** MOD-02-T072 — Mixed success and failure.
- **Category:** Batch.
- **Component / contract:** ModelLoader.load_many.
- **Objective:** Establish the specified mixed success and failure behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit valid, malformed, valid sources in that order.
- **Expected behavior:** PARTIAL; two snapshots plus one failed source; three ordered entries.
- **Expected diagnostics for invalid cases:** Middle source MOD-LOAD-005 only.
- **Boundary / edge cases:** Partial success cannot be mistaken for complete success.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T073 — All sources fail

- **Test ID / name:** MOD-02-T073 — All sources fail.
- **Category:** Batch.
- **Component / contract:** ModelLoader.load_many.
- **Objective:** Establish the specified all sources fail behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit missing file, malformed JSON and invalid schema with distinct IDs.
- **Expected behavior:** ALL_FAILED; no successful documents, failures remain ordered.
- **Expected diagnostics for invalid cases:** Acquisition, decoding and schema categories preserved by entry.
- **Boundary / edge cases:** Failures do not collapse into one generic semantic error.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T074 — Empty batch

- **Test ID / name:** MOD-02-T074 — Empty batch.
- **Category:** Batch.
- **Component / contract:** ModelLoader.load_many.
- **Objective:** Establish the specified empty batch behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit empty tuple and empty list.
- **Expected behavior:** EMPTY with no entries/documents/failures/diagnostics.
- **Expected diagnostics for invalid cases:** None.
- **Boundary / edge cases:** No vacuous ALL_LOADED or generated document.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T075 — All duplicate submissions rejected

- **Test ID / name:** MOD-02-T075 — All duplicate submissions rejected.
- **Category:** Batch.
- **Component / contract:** ModelLoader.load_many.
- **Objective:** Establish the specified all duplicate submissions rejected behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit two equal IDs with different content and a third unique valid source.
- **Expected behavior:** Both duplicates fail before provider invocation; unique source loads; PARTIAL.
- **Expected diagnostics for invalid cases:** MOD-LOAD-011 for each duplicate, first related_input_index=0.
- **Boundary / edge cases:** No first/last-write-wins; repeated identical object also rejected.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T076 — Multiple duplicate groups

- **Test ID / name:** MOD-02-T076 — Multiple duplicate groups.
- **Category:** Batch.
- **Component / contract:** ModelLoader.load_many.
- **Objective:** Establish the specified multiple duplicate groups behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Interleave repeated A/B IDs with a unique source.
- **Expected behavior:** Reject each group occurrence, preserve all input entries.
- **Expected diagnostics for invalid cases:** MOD-LOAD-011 related index points to first occurrence in its group.
- **Boundary / edge cases:** Indices are zero-based caller input positions.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T077 — Duplicate missing/unreadable file ID

- **Test ID / name:** MOD-02-T077 — Duplicate missing/unreadable file ID.
- **Category:** Batch.
- **Component / contract:** ModelLoader.load_many.
- **Objective:** Establish the specified duplicate missing/unreadable file id behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Repeat same ID across nonexistent file and valid memory source.
- **Expected behavior:** Reject both as batch duplicates without source acquisition.
- **Expected diagnostics for invalid cases:** MOD-LOAD-011 takes precedence over per-source failures.
- **Boundary / edge cases:** Pre-scan performed before any acquisition in the duplicate groups.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T078 — No cross-document semantic merge

- **Test ID / name:** MOD-02-T078 — No cross-document semantic merge.
- **Category:** Batch.
- **Component / contract:** ModelLoader.load_many.
- **Objective:** Establish the specified no cross-document semantic merge behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Load Customer and Employee declarations in two distinct sources.
- **Expected behavior:** Return two separately associated authoring documents.
- **Expected diagnostics for invalid cases:** None if both structurally valid.
- **Boundary / edge cases:** No canonical world or definition concatenation result.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T079 — Same semantic identity in distinct sources

- **Test ID / name:** MOD-02-T079 — Same semantic identity in distinct sources.
- **Category:** Batch.
- **Component / contract:** ModelLoader.load_many.
- **Objective:** Establish the specified same semantic identity in distinct sources behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Load equal/conflicting type ID/version in two documents with different source IDs.
- **Expected behavior:** Keep both snapshots without cross-document registry collision judgment.
- **Expected diagnostics for invalid cases:** None if each MOD-01 document is structurally valid.
- **Boundary / edge cases:** Within-document MOD-01 duplicates still fail independently.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T080 — Same file under different source IDs

- **Test ID / name:** MOD-02-T080 — Same file under different source IDs.
- **Category:** Batch.
- **Component / contract:** ModelLoader.load_many.
- **Objective:** Establish the specified same file under different source ids behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit same explicit path twice with distinct source IDs.
- **Expected behavior:** Load two independent snapshots preserving separate source identities.
- **Expected diagnostics for invalid cases:** None if file valid.
- **Boundary / edge cases:** No path-based deduplication or persistent cache.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T081 — No persistent batch identity cache

- **Test ID / name:** MOD-02-T081 — No persistent batch identity cache.
- **Category:** Batch.
- **Component / contract:** ModelLoader.load_many.
- **Objective:** Establish the specified no persistent batch identity cache behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Load an ID successfully, then reuse it in a separate single/batch operation.
- **Expected behavior:** Independent operation succeeds; duplicate policy is per batch only.
- **Expected diagnostics for invalid cases:** None for structurally valid source.
- **Boundary / edge cases:** Loader is frozen; no hidden registration state.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T082 — Ordered sequence API misuse

- **Test ID / name:** MOD-02-T082 — Ordered sequence API misuse.
- **Category:** Batch.
- **Component / contract:** ModelLoader.load_many.
- **Objective:** Establish the specified ordered sequence api misuse behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Supply set, generator and list containing a non-source object.
- **Expected behavior:** Reject unsupported sequence/source contracts before partial work.
- **Expected diagnostics for invalid cases:** TypeError programmer misuse.
- **Boundary / edge cases:** List/tuple order is copied into immutable entries.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T083 — Correct acquisition/decoding/schema association

- **Test ID / name:** MOD-02-T083 — Correct acquisition/decoding/schema association.
- **Category:** Diagnostics.
- **Component / contract:** ModelLoadDiagnostic.
- **Objective:** Establish the specified correct acquisition/decoding/schema association behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit same content under distinct source IDs/paths that fail at each stage.
- **Expected behavior:** Every diagnostic retains exact source metadata and correct stage.
- **Expected diagnostics for invalid cases:** Original stage-specific MOD-LOAD codes.
- **Boundary / edge cases:** No source path becomes namespace or semantic context.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T084 — JSON character positions

- **Test ID / name:** MOD-02-T084 — JSON character positions.
- **Category:** Diagnostics.
- **Component / contract:** SourcePosition/JsonModelDecoder.
- **Objective:** Establish the specified json character positions behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Place non-ASCII text before known malformed token on multiple lines.
- **Expected behavior:** Retain genuine one-based JSONDecodeError line/column.
- **Expected diagnostics for invalid cases:** MOD-LOAD-005.
- **Boundary / edge cases:** No byte-offset or zero-based mislabeling.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T085 — YAML schema value-node positions

- **Test ID / name:** MOD-02-T085 — YAML schema value-node positions.
- **Category:** Diagnostics.
- **Component / contract:** YamlModelDecoder/ModelLoader.
- **Objective:** Establish the specified yaml schema value-node positions behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Put unsupported primitive and invalid scalar at known YAML node coordinates.
- **Expected behavior:** Attach matching exact path value-node start marks to schema wrappers.
- **Expected diagnostics for invalid cases:** MOD-LOAD-010 plus original MOD-SCHEMA code/path/cause.
- **Boundary / edge cases:** Node mark is a value start, not a key or arbitrary enclosing position.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T086 — No fabricated missing-property positions

- **Test ID / name:** MOD-02-T086 — No fabricated missing-property positions.
- **Category:** Diagnostics.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified no fabricated missing-property positions behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Remove YAML required property and inspect schema wrapper.
- **Expected behavior:** Position None; original authoring missing-property path retained.
- **Expected diagnostics for invalid cases:** MOD-LOAD-010.
- **Boundary / edge cases:** Missing node has no physical coordinates; no enclosing fallback invented.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T087 — JSON schema and duplicate locations unavailable

- **Test ID / name:** MOD-02-T087 — JSON schema and duplicate locations unavailable.
- **Category:** Diagnostics.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified json schema and duplicate locations unavailable behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit duplicate JSON keys and separately invalid schema JSON.
- **Expected behavior:** Retain source-level/schema paths without guessed line/column.
- **Expected diagnostics for invalid cases:** MOD-LOAD-006 or MOD-LOAD-010, position None.
- **Boundary / edge cases:** JSON syntax coordinates remain available only from parser.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T088 — Deterministic diagnostic flattening

- **Test ID / name:** MOD-02-T088 — Deterministic diagnostic flattening.
- **Category:** Diagnostics.
- **Component / contract:** ModelLoader/ModelLoadBatchResult.
- **Objective:** Establish the specified deterministic diagnostic flattening behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Repeat an ordered mixed batch with multiple schema diagnostics.
- **Expected behavior:** Flatten errors by entry then original structural order.
- **Expected diagnostics for invalid cases:** Exact stable source/stage/code/path sequences match fixed input.
- **Boundary / edge cases:** No sorting by source ID or mutable map overwrite.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T089 — Result invariants reject ambiguous success

- **Test ID / name:** MOD-02-T089 — Result invariants reject ambiguous success.
- **Category:** Diagnostics.
- **Component / contract:** ModelLoadResult.
- **Objective:** Establish the specified result invariants reject ambiguous success behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Construct loaded+errors, no loaded+no errors and mismatched source results.
- **Expected behavior:** Reject invalid result contracts with ValueError.
- **Expected diagnostics for invalid cases:** Programmer exception, not fabricated source failure.
- **Boundary / edge cases:** Valid failure has at least one associated diagnostic; valid success has none.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T090 — Adapter result invariants

- **Test ID / name:** MOD-02-T090 — Adapter result invariants.
- **Category:** Diagnostics.
- **Component / contract:** SourceContentResult/SourceDecodeResult.
- **Objective:** Establish the specified adapter result invariants behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Construct acquisition/decode result with absent content/value and no errors or mismatched diagnostic source.
- **Expected behavior:** Reject invalid port contract.
- **Expected diagnostics for invalid cases:** ValueError.
- **Boundary / edge cases:** Decoded null roots must already be decode failure, not a success candidate.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T091 — Coordinate/schema invariant enforcement

- **Test ID / name:** MOD-02-T091 — Coordinate/schema invariant enforcement.
- **Category:** Diagnostics.
- **Component / contract:** ModelLoadDiagnostic/SourcePosition.
- **Objective:** Establish the specified coordinate/schema invariant enforcement behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Construct zero/bool coordinates, illegal codes and wrong schema attachment/stage.
- **Expected behavior:** Reject invalid diagnostic value objects.
- **Expected diagnostics for invalid cases:** ValueError/TypeError per public contract.
- **Boundary / edge cases:** Only schema stage has original AuthoringSchemaDiagnostic; related index nonnegative.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T092 — Immutable authoring snapshot

- **Test ID / name:** MOD-02-T092 — Immutable authoring snapshot.
- **Category:** Safety.
- **Component / contract:** LoadedAuthoringDocument.
- **Objective:** Establish the specified immutable authoring snapshot behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Keep parsed candidate through an injected decoder; load and then mutate candidate containers.
- **Expected behavior:** Loaded frozen MOD-01 document remains unchanged.
- **Expected diagnostics for invalid cases:** None during valid load; frozen assignments reject mutation.
- **Boundary / edge cases:** Nested declarations/lists projected to existing immutable authoring values.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T093 — Source text and files unchanged

- **Test ID / name:** MOD-02-T093 — Source text and files unchanged.
- **Category:** Safety.
- **Component / contract:** ModelLoader/Source contracts.
- **Objective:** Establish the specified source text and files unchanged behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Capture source text/file bytes and metadata before loading valid and invalid sources.
- **Expected behavior:** No rewrite, schema upgrade, ID generation or version correction.
- **Expected diagnostics for invalid cases:** Failures retain original categories.
- **Boundary / edge cases:** Read-only access may update filesystem access time under OS policy.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T094 — Immutable batch and diagnostics

- **Test ID / name:** MOD-02-T094 — Immutable batch and diagnostics.
- **Category:** Safety.
- **Component / contract:** ModelLoadBatchResult.
- **Objective:** Establish the specified immutable batch and diagnostics behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Build from caller list then mutate list; try assigning frozen fields.
- **Expected behavior:** Entries/derived results retain immutable tuple order and snapshots.
- **Expected diagnostics for invalid cases:** TypeError/attribute assignment failure on invalid mutation.
- **Boundary / edge cases:** Candidate decoder value intentionally remains untrusted, not advertised immutable.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T095 — Explicit memory provider injection

- **Test ID / name:** MOD-02-T095 — Explicit memory provider injection.
- **Category:** Safety.
- **Component / contract:** ModelSourceProvider/ModelLoader.
- **Objective:** Establish the specified explicit memory provider injection behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Inject a source-aware provider returning BASE without filesystem access.
- **Expected behavior:** Use injected operation, retain source identity and delegate schema validation.
- **Expected diagnostics for invalid cases:** None.
- **Boundary / edge cases:** No global service locator or dynamic registry.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T096 — Injected provider cannot bypass limits

- **Test ID / name:** MOD-02-T096 — Injected provider cannot bypass limits.
- **Category:** Safety.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified injected provider cannot bypass limits behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Inject provider returning oversized/empty/invalid-Unicode source text.
- **Expected behavior:** Shared acquisition boundary rejects before decoder.
- **Expected diagnostics for invalid cases:** MOD-LOAD-012/004/013 respectively.
- **Boundary / edge cases:** Provider-produced successful content is checked again by orchestrator.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T097 — Injected decoder cycle/shared object safety

- **Test ID / name:** MOD-02-T097 — Injected decoder cycle/shared object safety.
- **Category:** Safety.
- **Component / contract:** ModelLoader/inspect_tree.
- **Objective:** Establish the specified injected decoder cycle/shared object safety behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Inject a plain candidate with self-cycle and separately repeated shared list.
- **Expected behavior:** Reject cyclic/shared containers before MOD-01 recursion.
- **Expected diagnostics for invalid cases:** MOD-LOAD-008.
- **Boundary / edge cases:** No automatic alias cloning; only a plain tree accepted.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T098 — Injected decoder native object safety

- **Test ID / name:** MOD-02-T098 — Injected decoder native object safety.
- **Category:** Safety.
- **Component / contract:** ModelLoader/inspect_tree.
- **Objective:** Establish the specified injected decoder native object safety behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Inject custom mapping/list subclasses, tuple child, arbitrary class and nonstring key.
- **Expected behavior:** Reject non-plain JSON-compatible output.
- **Expected diagnostics for invalid cases:** Root subclass MOD-LOAD-009; nested/key cases MOD-LOAD-008.
- **Boundary / edge cases:** No unchecked cast or executable domain-object trust.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T099 — Injected decoder depth/node safety

- **Test ID / name:** MOD-02-T099 — Injected decoder depth/node safety.
- **Category:** Safety.
- **Component / contract:** ModelLoader/inspect_tree.
- **Objective:** Establish the specified injected decoder depth/node safety behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Inject huge width/depth candidate despite short acquired source.
- **Expected behavior:** Recheck tree limits before structural validation.
- **Expected diagnostics for invalid cases:** MOD-LOAD-014.
- **Boundary / edge cases:** Precheck collection size before extending traversal stack.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T100 — Adapter association/programming violations

- **Test ID / name:** MOD-02-T100 — Adapter association/programming violations.
- **Category:** Safety.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified adapter association/programming violations behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Inject wrong result type/source and provider/decoder raising unexpected RuntimeError.
- **Expected behavior:** Reject result/association with TypeError; propagate unexpected programming exceptions.
- **Expected diagnostics for invalid cases:** No misleading anticipated-input diagnostic for programmer defects.
- **Boundary / edge cases:** Parser/source anticipated failures remain structured through built-in adapters.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T101 — Malformed encoding and source BOM

- **Test ID / name:** MOD-02-T101 — Malformed encoding and source BOM.
- **Category:** Safety.
- **Component / contract:** check_text/LocalFileSourceProvider.
- **Objective:** Establish the specified malformed encoding and source bom behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Submit invalid UTF-8 file, in-memory lone surrogate and leading BOM in either format.
- **Expected behavior:** Reject acquisition rather than silently correcting encoding.
- **Expected diagnostics for invalid cases:** MOD-LOAD-013.
- **Boundary / edge cases:** Valid supplementary Unicode scalar source text remains permitted.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T102 — Parser lifetime cleanup

- **Test ID / name:** MOD-02-T102 — Parser lifetime cleanup.
- **Category:** Safety.
- **Component / contract:** YamlModelDecoder.
- **Objective:** Establish the specified parser lifetime cleanup behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Instrument SafeLoader dispose on success and syntax/tag/scalar/resource failures.
- **Expected behavior:** No retained loader state or cross-load candidate contamination.
- **Expected diagnostics for invalid cases:** Original failure code and source retained.
- **Boundary / edge cases:** Preflight yaml.parse generator also closes on handled failure.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T103 — Loader public imports remain governed

- **Test ID / name:** MOD-02-T103 — Loader public imports remain governed.
- **Category:** Architecture.
- **Component / contract:** Module dependency graph.
- **Objective:** Establish the specified loader public imports remain governed behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Inspect manifest and production imports at fixed future revision.
- **Expected behavior:** Only model-authoring module edge; approved yaml parser at tooling profile/path.
- **Expected diagnostics for invalid cases:** No ARCH dependency/API/external violation.
- **Boundary / edge cases:** No Kernel/model-core contract changes or relaxed neutral-zone policy.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T104 — No semantic side effects

- **Test ID / name:** MOD-02-T104 — No semantic side effects.
- **Category:** Architecture.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified no semantic side effects behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use spies around registry, resolver, compiler/runtime/network APIs while loading valid references.
- **Expected behavior:** No resolution, canonical types, registry registration, compilation, instance execution or network calls.
- **Expected diagnostics for invalid cases:** None for valid unresolved declarations.
- **Boundary / edge cases:** No tenant/org ownership, provenance graph or package import traversal.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T105 — Nine-module inventory without tooling reverse edge

- **Test ID / name:** MOD-02-T105 — Nine-module inventory without tooling reverse edge.
- **Category:** Architecture.
- **Component / contract:** CLI inventory/root build.
- **Objective:** Establish the specified nine-module inventory without tooling reverse edge behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Inspect CLI repository registration and manifest importability at fixed revision.
- **Expected behavior:** Explicit model-loader inventory name accepted; five activation markers and seven CLI observed edges retained.
- **Expected diagnostics for invalid cases:** No public registration mismatch or architectural tooling-to-tooling edge.
- **Boundary / edge cases:** Inventory check is deferred; current static build only imports MODULE_NAME.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T106 — Pinned YAML dependency setup

- **Test ID / name:** MOD-02-T106 — Pinned YAML dependency setup.
- **Category:** Architecture.
- **Component / contract:** Development setup.
- **Objective:** Establish the specified pinned yaml dependency setup behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use clean supported Python environment and scripts/dev.py install under authorized future verification.
- **Expected behavior:** Install requirements-model-loader.txt PyYAML==6.0.3 without loading examples/tests.
- **Expected diagnostics for invalid cases:** Dependency/setup failures surfaced by root command.
- **Boundary / edge cases:** External parser approval is limited to tools/model-loader, not Django/DRF/semantic packages.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T107 — Equivalent JSON/YAML authoring snapshots

- **Test ID / name:** MOD-02-T107 — Equivalent JSON/YAML authoring snapshots.
- **Category:** Mini Sales.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified equivalent json/yaml authoring snapshots behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Load existing JSON and new YAML through separate source IDs.
- **Expected behavior:** Equivalent document values; different explicit source metadata retained.
- **Expected diagnostics for invalid cases:** None.
- **Boundary / edge cases:** Original creditLimit minimum "0", precision 18 and scale 2 remain authored declarations.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T108 — Mini Sales stable field IDs and axes

- **Test ID / name:** MOD-02-T108 — Mini Sales stable field IDs and axes.
- **Category:** Mini Sales.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified mini sales stable field ids and axes behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Inspect loaded Customer fields from both formats.
- **Expected behavior:** Preserve all three field IDs/order; required/optional and non-null axes; version "1.0.0".
- **Expected diagnostics for invalid cases:** None.
- **Boundary / edge cases:** No nullable default, generated ID or version range introduced.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

## MOD-02-T109 — Mini Sales malformed and unsupported primitive

- **Test ID / name:** MOD-02-T109 — Mini Sales malformed and unsupported primitive.
- **Category:** Mini Sales.
- **Component / contract:** ModelLoader.
- **Objective:** Establish the specified mini sales malformed and unsupported primitive behavior without crossing loading responsibilities.
- **Required prerequisites:** Shared authorized, pinned-revision setup above; required adapter/format and stated fixture capability available.
- **Inputs / setup:** Use malformed JSON copy and separately replace decimal with unsupported object primitive.
- **Expected behavior:** First fails decoding; second fails MOD-01; neither returns partial snapshot.
- **Expected diagnostics for invalid cases:** MOD-LOAD-005 versus MOD-LOAD-010/MOD-SCHEMA-009.
- **Boundary / edge cases:** No canonical Customer registration or instance construction on either branch.
- **Integration dependencies:** model_loader.public and existing model_authoring.public; built-in JSON/PyYAML or explicit injected port as stated. No TypeRegistry/runtime dependency.
- **Acceptance criteria:** Exact expected result, source association, diagnostic/stage/path/position and boundary behavior observed with recorded evidence; no undocumented success, mutation or semantic side effect.
- **Execution status:** NOT_RUN — DEFERRED

