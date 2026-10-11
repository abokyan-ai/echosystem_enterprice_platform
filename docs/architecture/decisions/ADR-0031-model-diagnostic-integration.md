# ADR-0031 — Preserve original diagnostics in immutable reports

Date: 2026-10-11. Status: accepted implementation decision; behavior unverified.

General SK-11 is absent; actual existing diagnostic contracts are the authoritative available seams. MOD-09 retains whole original diagnostics and adds bounded origin/target/source/stage associations, without competing codes/severity, message classification or validation rules. Missing SK-11 is documented rather than fabricated.

Semantic associations live in model-authoring. Physical MOD-03 types and unified loading/domain reports live in existing model-loader tooling, preserving inward dependencies and pure Python values without framework startup. No reverse tooling import/new module/profile is required.

Typed result adapters preserve explicit producer outcome, original emission order and MOD-08 status/readiness/stage outcomes. Fixed phase sorting is stable within each phase. No deduplication by default; counts and filtered/grouped views cannot decide validity. One authoritative validation run per report avoids silently choosing among incompatible model results.

Enrichment uses original physical evidence or explicitly paired exact indexes; ambiguous/missing associations remain unavailable. QName never becomes stable identity; FieldId stays owned-field identity. Constraint reports use actual broader field/definition nodes while exact constraint mapping is absent.

Explicit JSON-ready presentation omits sensitive details by default and uses optional caller-authorized disclosure without creating a permission engine or HTTP-status mapping. No existing DRF endpoint needs modification; no endpoint/ORM/persistence. No diagnostic/model transformation or upstream validation execution. Document all future verification and stop MOD-09.
