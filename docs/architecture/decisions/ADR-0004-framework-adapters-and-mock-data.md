# ADR-0004 — Angular/PrimeNG, Django REST Framework and Mock Data Adapters

Status: Accepted. Date: 2026-10-07.

## Context

The project owner explicitly selected Angular + PrimeNG frontend, Django + Django REST Framework backend API, and mock-data contracts without a database. ARC-01's Python standard-library choice covers the skeleton/governance tooling; it did not implement or select an HTTP/UI stack.

## Decision

Adopt Angular/PrimeNG for a future frontend target, Django/DRF for a future HTTP adapter, and contract-based in-memory data for the first slice. Keep semantic/compiled/experience contracts framework neutral. Application composition wires concrete adapters. Do not add ORM entities, migrations, a database connection or test fixtures as production storage.

## Alternatives considered

React/Flutter and other HTTP frameworks remain possible replacement implementations at the contract boundaries, but are not the selected stack. A concrete database is unnecessary for the requested mock-data phase.

## Consequences

Angular/PrimeNG dependencies belong in a future frontend module with TypeScript analyzer and package exports. Django/DRF dependencies belong in an explicitly declared HTTP adapter. Runtime depends on owned data contracts and receives mock implementations via composition. HTTP requests, Django models and PrimeNG types do not enter platform contracts. No framework packages, UI, HTTP endpoints or data behavior are added in ARC-02.

## Future revisit conditions

Before implementing the first API/UI slice, pin compatible versions, introduce package manifests/analyzers, specify wire contracts and demonstrate API calls with mock data. Add a DB adapter only if a later requirement needs it, preserving consumers of the data contracts.
