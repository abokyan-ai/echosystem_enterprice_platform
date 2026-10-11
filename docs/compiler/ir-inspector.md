# CMP-10 — IR Inspector

Date: 2026-10-11. Status: **DEFERRED / NOT VERIFIED**. Tests created/executed: **0**. [179 deferred scenarios](../../test-archive/CMP-10/CMP-10-deferred-tests.md).

## Ownership, contracts and source boundary

Pure `compiler_core.public` owns IRInspector and SemanticIRInspector, IRInspectionRequest/Selection/Options/Limits/Result, immutable envelope/type/field/reference/constraint projections, supported view equivalence and optional bounded developer text. No new module, import edge, dependency exception, framework or filesystem capability. Existing CompilationState/CompilationResult/phase outcomes/readiness and all IR contracts remain unchanged.

Sources are one actual SemanticIREnvelope, an explicit **tuple** of actual envelopes, actual CompilationState.ir_envelopes or actual CompilationPhaseResult.ir_envelopes (the CMP-05 output boundary). No raw JSON/YAML/pickle/paths/arbitrary objects/list/generator, parser, implicit decoding/fetch/registry lookup, cache or private-state introspection. Empty explicit output means source unavailable INCOMPLETE; no empty fake successful view. Do not require a separate CanonicalModel, Manifest, receipt or artifact file.

A collection belongs to **one original canonical-input request**; duplicate IR IDs always fail, including equal envelopes. Mixing request scopes with reused IDs is unsupported rather than selecting ambiguous identities. Envelopes normalize to existing CMP-03 committed collection order by representation ID; source tuples/state/phase outputs are never changed. Candidate PhaseResult output can be structurally inspected without claiming it was committed.

Final CompilationResult currently exports no internal IR/state. Failed/incomplete compilation can coexist with successful inspection only when real envelopes/state/phase outputs were separately explicitly made available. Inspector does not extract unpublished partial internals, rerun compilation or fabricate missing IR. Existing completed intermediate IR is inspectable regardless of later final artifact generation status.

## Selection and limits

ALL_ENVELOPES, BY_IR_IDENTITY, BY_PAYLOAD_KIND and BY_SEMANTIC_ORIGIN use an explicit matching typed selector. Origin selectors are exact ElementVersionRef, never latest version/display-name lookup. No match is FAILED CMP-087; no unrelated fallback/empty success/query language/dependency graph. Source count is bounded before traversal even when selecting one envelope; selected type fields are bounded before projecting, unselected fields are not traversed.

Defaults: **128 supplied envelopes**, **1024 fields per selected type**, **8192 total selected fields**, **262144 text characters**, **8192 requested source associations**. All limits are positive actual integers, not bool/float. Effective maxima are caller/server minima, so caller cannot raise trusted ceilings. Source count/selected field/source-association excess returns INCOMPLETE CMP-089 without partial successful views. The renderer separately takes the minimum of effective text limit and its trusted configured maximum. No silent structured/text truncation.

These are structural/presentation bounds, not an exact interpreter RSS or worst-case execution-time guarantee. Existing immutable pattern/scalar/input association data may be shared without copying a source graph. Text values are length-checked before escaping; escaped expansion is checked again. Integer conversion is bounded and can return INCOMPLETE if interpreter conversion limits prevent complete display; process-global settings are never changed.

## Supported handler and compatibility checks

v0 explicitly supports only **SemanticIRPayloadKind.COMPILED_TYPE_IR / actual CompiledTypeIR**. The existing valid FOUNDATION_COORDINATES kind has no payload inspection handler and returns INCOMPLETE CMP-083. Future Action/Event/Policy/Capability/Relationship/Workflow/Experience kinds are unsupported; extend by intentional compiler-owned typed dispatch, never dynamic import/reflection/filesystem discovery.

Check schema V0, selected payload existence/actual type, exact compiled identity/name/context and fields tuple, one exact matching envelope origin, model-wide false and input-context agreement. Check actual field ID/name/reference/constraint leaves and duplicate ID/portable name compatibility. These are intrinsic inspection shape checks; **no IR-versus-CanonicalModel comparison, semantic constraint applicability, validation pipeline, DataFacet regeneration, lowerer or field-value evaluation**. Existing IR constructors already own their creation invariants and can reject malformed data before inspection.

Unknown/malformed source/request fails; schema/handler unavailable INCOMPLETE; selected kind/payload/origin/scope/field incompatibility FAILED. No generic fallback. Ordinary unexpected programming defects are not disguised as expected inspection outcomes.

## Immutable views and exact values

IREnvelopeInspectionView always exposes actual representation identity, payload kind, semantic context and typed compiled-type projection. Optional IREnvelopeMetadataInspectionView contains actual schema, original immutable SemanticIRCanonicalInput association and optional producer phase. It does not fabricate a canonical fingerprint/compiler version/producer or copy the full envelope merely to rename it. Original association is shared readonly; generic metadata equality retains original request identity. Inspection views are not portable/authenticated proof or artifact serialization.

CompiledTypeInspectionView preserves exact ElementVersionRef (including all numeric version parts), QualifiedName, scope and declaration-ordered fields. No alphabetical reordering, semantic-ID creation, TypeDefinition reconstruction, table/endpoint/runtime names.

CompiledFieldInspectionView retains owned FieldId and FieldName separately, explicit primitive/semantic reference projection, independent FieldPresence/FieldNullability and optional constraint projections. All collections are tuples; no mutable view containers/setters.

IRPrimitiveReferenceInspectionView preserves Kernel String/Boolean/Integer/Decimal/Date/DateTime/UUID. IRSemanticReferenceInspectionView preserves identity-only ElementRef; current TYPE-05 semantic references are **versionless**. Self/mutual references stay leaf values, no latest resolution/registry/query/dependency expansion or invented exact-version form. No target SQL/JSON/ORM/DRF/Python type mapping.

IRConstraintInspectionView preserves actual ConstraintKind and exact supported scalar from the seven existing classes: min/max-length, minimum/maximum, pattern, precision, scale. Numeric bounds share NumericConstraintValue exact fixed-point text, never binary float or Decimal context rounding. Presence/nullability are always retained, even if optional value constraints are omitted. Patterns are reported, never compiled/evaluated. No default/minimum/regex semantics invented or TYPE-06/instance constraints applied.

## Options, source data and diagnostics

Four actual booleans: metadata/origins/constraints enabled by default, source associations disabled. Metadata option controls schema/input/producer projection; core identity/kind/context remains. Disabled optional group is **None**; requested source data can be **empty tuple**. Requested missing source produces CMP-090 WARNING and semantic inspection may SUCCEED. Empty actual IR output produces CMP-090 INCOMPLETE. No guessed field/file/line coordinates.

Source projection reuses CanonicalSourceAssociation/AuthoringSchemaPath, bounded in count and coordinate representation. These are authoring **schema-tree** coordinates, not physical file paths. Reject path-like slash/backslash/control segments when exposing source data; no source file read or physical-location loader. Preserve original sidecar order and exact origin; field error uses the first reliable existing field coordinate in established order when source data is requested. Full original source collection remains in the projected view. No unrestricted absolute path in public output.

CMP-081..092 extend the existing compiler diagnostic family: invalid request, unsupported schema, unsupported payload, payload mismatch, invalid envelope, duplicate identity, unknown selection, invalid field, structural limit, source unavailable, invalid options, text limit. RESULT origin with original IR identity, exact type/FieldId/producer/reliable requested source path where available. Missing optional producer stays absent; no phase failure is fabricated. Full SK-11 remains unavailable; retain existing CMP-02 narrow seam. These inspection diagnostics are never appended to the original CompilationResult or used to change compilation readiness/outcomes.

IRInspectionResult reuses established status values for **inspection semantics only**. SUCCEEDED requires every selected supported view and no errors within effective limits. FAILED/INCOMPLETE expose no views, retain diagnostics/selected IDs/effective bounds. Warnings may accompany complete semantic inspection. A later selected failure discards earlier projected views; no partial success mode in v0.

## Determinism and developer text

IRInspectionEquivalence compares actual projection values/order/options plus metadata schema/producer and existing CMP-06 supported original-input comparison. Original identity association is not replaced by equality, authenticity or serialization. The helper never repeats inspection/compilation. Source locations, if requested, remain actual projection data; no text/message-derived ordering.

IRInspectionTextRenderer optionally renders a successful structured result in fixed explicit labels and IR/type/field/constraint/source order. It reports identity/scope/schema/producer/origins, exact type identity/name, field ID/name/primitive or unresolved versionless reference, presence/nullability and exact constraints. Source schema segments are displayed individually; no AuthoringSchemaPath repr or arbitrary dataclass dumping. It displays only that the canonical association is original in-process, never full canonical/request internals.

Scalar strings are JSON-quoted/escaped for developer text only, including untrusted patterns; numeric fixed-point values retain exact text. This is **not** canonical IR JSON/serialization, no round-trip decoder/persisted format/runtime input. Text overflow returns INCOMPLETE CMP-092 with text None, no marker pretending to be complete or partial display contract. Failed structured results cannot render successful text. No CLI command or HTTP presentation endpoint is introduced.

## Django/DRF and Mini Sales

Selected backend is Python/Django/DRF; package metadata reports Django/DRF NOT_INSTALLED and no compiler HTTP adapter exists. Pure inspector imports/constructs without Django. No ORM/migration/serializer/auth/permission/API change. Future authorized HTTP presentation must use explicit serializers/server limits/response-size policy and established permissions; context is not tenant authorization. No generic object inspection/public internal-state endpoint.

Conceptual Mini Sales only: actual Customer `sem_550e8400-e29b-41d4-a716-000000000001@1.0.0`, Employee `sem_550e8400-e29b-41d4-a716-000000000002@1.0.0`, actual schema field UUIDs and explicit request-local `ir-...` tokens. Prompt `typ_customer_123`/`fld_name` are illustrative aliases incompatible with real ID grammar.

Given real already constructed CMP-05 Customer IR, inspection exposes name/active/creditLimit in original order. Name is required/non-null String with max-length 200; active required/non-null Boolean; creditLimit optional/non-null Decimal with exact minimum 0, precision 18, scale 2. Employee.manager's versionless ElementRef self-reference is displayed once, no recursion. Missing selected IR ID fails CMP-087, valid foundation kind CMP-083, absent source maps truthfully remain empty. Later artifact build INCOMPLETE can coexist with successful available IR inspection without changing compilation status or implying runtime artifacts. No example, compiler, inspector or renderer invocation is executed during this task.

## Deferred verification and readiness

[179 future cases](../../test-archive/CMP-10/CMP-10-deferred-tests.md), all NOT_RUN — DEFERRED; tests created/executed **0**. Sole archive file per latest task section 41; no README/test scaffolding. Static source/syntax/build/public MODULE_NAME imports/fitness/dependency/diff/document inspection is separate from behavior and does not verify these scenarios.

Limits: unsupported future/foundation payload handlers, optional missing schema source maps, no final-result internal IR export, trusted in-process associations, general SK-11/full TYPE-01/HTTP absence, bounded complete-only output. No artifact producers/encoders/storage/read/write/publish/deploy/runtime dependency added. Stop CMP-10; CMP-11 not started.

Source coordinate resource note: requested schema-segment counts and aggregate content additionally use the effective maximum_output_characters representation budget (integer segment bit lengths conservatively bound conversion size). Overflow is INCOMPLETE/CMP-089 before unsafe text scanning/projection; no truncated coordinates.
