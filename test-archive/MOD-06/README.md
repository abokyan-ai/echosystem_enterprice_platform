# MOD-06 — Namespace Resolver test archive

Task: MOD-06 — Namespace Resolver. Documentation date: 2026-10-10 (Asia/Riyadh).

Testing status: **DEFERRED / NOT VERIFIED**. All **146** scenarios: **NOT_RUN — DEFERRED**. New automated tests implemented: **0**. Tests executed: **0**.

Scope: explicit typed requests, minimal declared symbol coordinates, immutable single-context visibility, local/exact-qualified/explicit-alias/identity/exact-version resolution, ambiguity/kind safeguards, TYPE-07 read-only selected symbol capture, existing MOD-05 field-binding compatibility, diagnostics and optional actual MOD-03 location presentation.

[Detailed specification](MOD-06-deferred-tests.md). [Standing-name navigation](MOD-06-deferred-test-spec.md). One detailed scenario collection; navigation contains no duplicate cases.

Dependencies: SK-02/03/04/07/08/11, TYPE-07, MOD-01/03/05 actual contracts. Full SK-11/TYPE-01 and other declared architectural gaps are not fabricated. TYPE-05 exact field pins remain incompatible with current canonicalization. No Django/DRF endpoint currently exists and none is created.

Future execution requires explicit authorization, fixed revision, Python 3.11+, registered public source paths/setup, actual approved symbol/lookup/authoring/location inputs and evidence. Current task does not run tests, examples, resolver/capture/bridge/location scenarios or custom runners. Conditional future API cases require actual approved prerequisites first.

Known limits: single-context v0; aliases are resolver-only explicit direct namespace capabilities, without MOD-01 schema extension or recursive chains; minimal symbols do not compare full definition fields; selected visibility does not infer unseen registry history; lookup port purity/stability and original source-document pairing are caller obligations. General SK-11 remains a real missing contract. Static success is not behavioral verification.

See [implementation record](../../docs/architecture/mod06-verification.md) and [resolver contract](../../docs/model/namespace-resolver.md). Existing archives/test code/history are preserved. Stop after MOD-06; no MOD-07.
