# ADR-0001 — Modular Monolith and Explicit Module Boundaries

Status: Accepted. Date: 2026-10-07.

## Context

An empty repository must support a long-lived semantic, model-driven platform while avoiding early distributed systems and framework coupling.

## Decision

Start as a modular monolith. Use explicit public contracts, independent compiled-contract ownership, static dependency allowlists and isolated internal implementations. Keep infrastructure behind platform-owned ports and adapters. Use in-process composition first. Extract services only when operational evidence justifies it.

## Alternatives considered

A single undifferentiated package hides ownership and permits coupling. Microservices add transport/deployment costs before a vertical slice exists. Dozens of empty modules add management without meaningful contracts.

## Consequences

Six current modules establish five platform boundaries plus tooling. No DB, UI or transport is required. Independent contracts permit future replacement/extraction, but distributed transactions and serialization remain future work. Discipline and automated negative tests protect boundaries; public API markers do not implement platform behavior.

## Future revisit conditions

Measured scaling/isolation demands, independent team release cadence, compliance requirements, or public contracts requiring separate distribution. Record evidence and failure semantics before service extraction.
