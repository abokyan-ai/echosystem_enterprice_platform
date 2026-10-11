# ADR-0030 — Explicit validation orchestration

Date: 2026-10-11. Status: accepted implementation decision; behavioral verification deferred.

The supplied immutable MOD-04 model already guarantees canonical membership. TYPE-06 already owns structural, constraint and direct reference judgments; general SK-11/full TYPE-01 remain absent. Reimplementing these rules or claiming unsupported-kind coverage would hide actual contract gaps.

Model-authoring owns two mandatory ordered stages: canonical scope compatibility and full TYPE-06 semantic validation with explicit stable TYPE-07 lookup capture. The latter includes existing reference rules exactly once. Additional stages are explicitly injected after the core; none may replace core checks. No generic rule/profile engine, automatic authoring processing or model consistency semantics.

Lookup must explicitly contain canonical identities at matching selected metadata/version coordinates. No auto registration, model fallback, latest selection or graph traversal. Missing/ambiguous infrastructure yields incomplete evidence; mismatched environments block unsafe later validation. None for external targets remains TYPE-06's missing-target error. Five-value lookup metadata cannot certify full facet equality; caller provides a stable pure view.

Reports preserve complete original TYPE-06 diagnostics with stage and exact owner provenance; only narrow orchestration failures use new task-local codes pending SK-11. Source paths come from actual MOD-05 associations, with physical MOD-03 enrichment external in model-loader. Constraint locations use actual broader field/definition nodes instead of fabricated coordinates.

All mandatory outcomes must complete without errors (and according to explicit warning policy) to claim VALID/READY under supported contracts. Readiness is not compilation success, full missing TYPE-01 validation or runtime authority. Unsupported kinds remain constructor-rejected, not silently excluded.

No Django/DRF interface currently needs extension; no endpoint/ORM/dependency change. No tests or examples are executed. Archive future verification and stop MOD-08.
