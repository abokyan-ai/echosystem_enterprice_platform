# ADR-0024: Explicit model-source loading boundary

Date: 2026-10-10. Status: implemented for MOD-02; behavior **DEFERRED / NOT VERIFIED**.

## Context

MOD-01's pure validator already accepts decoded trees and constructs immutable authoring snapshots. The model zone excludes JSON, filesystem infrastructure and external parsers. A caller needs explicit input acquisition/decoding, source traceability and separate acquisition/decoding/schema errors. General SK-11 diagnostics are absent; adding an unseen full diagnostic framework would expand scope.

## Decision

Own the loader in tools/model-loader (tooling zone) with a single public model-authoring dependency. Approve PyYAML==6.0.3 only at that source-loading profile/path. Keep the existing neutral-zone dependency policy unchanged. No tooling-to-tooling CLI import is added: CLI uses an explicit inventory name and root build checks manifest public entry points independently. Keep five foundation activation markers unchanged.

Use Python public value contracts consistent with the repository's analyzer, explicitly adapting the conceptual TypeScript prompt. Define frozen source IDs/metadata/options/result/diagnostic/snapshot/batch contracts; mutable parser candidates never become the successful result. Define contracts and concrete operation classes in public.py, complying with the existing no-public-private-import rule. Private functions separate file I/O and each established parser from orchestration; provider and decoder slots are injectable, not globally registered. Anticipated errors are source-associated diagnostics; programmer contract violations propagate.

Require caller source IDs and formats. Read explicit regular files as bounded strict UTF-8 without BOM; no path-derived semantics. JSON is strict with duplicate-key/non-finite rejection. YAML is SafeLoader 1.1 with event limits, rejecting all explicit tags, anchors/aliases, merge keys and multiple documents, then projecting only JSON-compatible nodes. Do not implement a custom YAML parser. YAML dependency is lazy and explicit requirements setup is reproducible.

Delegate structure to MOD-01 and retain its full original diagnostic. Provisional narrow loading diagnostics use one-based marks or original schema paths; no made-up positions, unified SK-11 claim or semantic provenance graph. Retain authored semantic values and unresolved expressions.

Batch results preserve input order and represent empty/all/partial/failure states distinctly. Reject every occurrence of duplicate source identity before acquisition; distinct sources may retain the same semantic identity for later governed processing. No implicit merge, resolution, registry interaction, canonical model creation, compiler behavior or runtime dependency.

## Consequences and open decisions

A real parser dependency now exists in tooling; semantic packages remain stdlib-only. YAML 1.1 coercions require documented quoting; YAML 1.2 is not advertised. Source limits offer practical bounds, not isolated quotas; filesystem confinement/checksums/external version stability belong to later governed calling boundaries. General SK-11 integration must preserve current source associations/schema causes, and any future parser/format expansion requires an explicit decision. TYPE-01/TYPE-08/full SK-09 remain incomplete but are not prerequisites for authoring loading.

All loading scenarios and Mini Sales demonstrations are deferred. Syntax/build/governance checks do not prove loader behavior. See [contract](../../model/model-loader.md) and [deferred specification](../../../test-archive/MOD-02/MOD-02-deferred-test-spec.md). Stop at MOD-02.
