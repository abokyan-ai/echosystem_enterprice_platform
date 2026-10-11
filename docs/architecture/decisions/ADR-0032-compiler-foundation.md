# ADR-0032 — Bound compiler entry and explicit phase foundation

Date: 2026-10-11. Status: accepted implementation decision; behavior unverified.

Registered compiler-core/compiled-contracts were markers. MOD-08 results had no canonical input binding, and SK-11/full TYPE-01 remain unavailable. Compiler admission based on context/count/empty diagnostics would therefore falsely accept unrelated snapshots.

Add an optional original-model association to actual ModelValidationResult, populated by its existing pipeline, and require exact object binding plus VALID/READY at compiler entry. Legacy unbound evidence fails closed. No hash, serializer, new validation run/rules or cross-process certificate is introduced.

Use existing compiler-core for immutable request/context/phase descriptors/state/results and ModelCompiler, with one explicit inward model-authoring API dependency. Mandatory preparation plus injected ordered phases declare prerequisites/capabilities/targets; no generalized scheduler or dynamic discovery. Preparation success is explicitly distinct from artifact-build, which remains incomplete without concrete future generators/output.

Stable artifact metadata/key/kind protocol belongs to compiled-contracts; compiler owns deterministic immutable membership/duplicate conflict checks. No concrete payload, fake artifact, universal IR, persistence or publishing. Final unsuccessful results expose no candidate artifacts/preparation as successful output.

MOD-09 gains an explicit compiler diagnostic extension and presentation projection in model-authoring. Source tooling consumes that contract rather than importing compiler implementation: designated adapter profile remains intact. Actual severities/validation reports/statuses/phase origins remain preserved; general SK-11 is not recreated or claimed complete.

No existing HTTP boundary requires DRF changes, and no endpoint/ORM/dependency upgrade/activation change. Archive future verification and stop CMP-01.
