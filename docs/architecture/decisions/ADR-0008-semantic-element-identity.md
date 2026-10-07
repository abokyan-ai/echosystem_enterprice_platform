# ADR-0008: Opaque semantic element identity

Status: Accepted for SK-01

## Context and requirements

Semantic references must survive renaming and changes in deployment, representation and storage. Identity cannot encode qualified names, namespaces, element kinds, semantic versions, tenants or database/runtime instance keys. The kernel is a pure Python 3.11+ foundation with no external dependencies; the representation is a long-lived public contract.

## Options considered

- UUIDv4: established random opaque identity, supported by the Python 3.11 standard library, compact ASCII/hyphen representation; lacks chronological ordering.
- UUIDv7: time-ordered format, but standard-library generation is introduced in Python 3.14, beyond this repository's 3.11–3.13 matrix; a new library/custom generator is unnecessary for the current representation task.
- ULID: compact sortable representation, requiring an additional implementation/dependency and case/alphabet decisions without a demonstrated ordering requirement.
- Name/hash/sequence identities: couple identity to naming or issuance/storage semantics and do not meet the requirements.

## Decision

Represent a SemanticElementId as `sem_` plus a strictly hyphenated UUIDv4 with RFC variant, canonical lowercase hex. The prefix identifies the semantic-element category only. Accept hex case variation, reject all alternate shapes and versions, and validate both constructor and parser. Use one frozen slotted value object, one small ValueError diagnostic and a None-returning safe parse.

SK-01 does not generate IDs or provide a generation service. Callers supply values; future issuance belongs to a separate boundary using an established UUIDv4 implementation. No clock/randomness enters the primitive. Serialization maps the value to a string outside Kernel. Normalized value equality/hashing are Python-idiomatic; hashes are not persisted.

## Consequences and migration

The wire value is 40 URL-safe ASCII characters. Identity remains unchanged across renaming. No chronological ordering is promised and parse validation does not prove uniqueness or entropy. No global registry, serializer framework or new physical module is introduced. Bootstrap and CLI require no semantic lifecycle or command additions.

Any future prefix/layout/version change requires an explicit compatibility/migration decision. Do not silently reinterpret existing UUIDv4 identifiers or rewrite them as UUIDv7. Multi-format support is deferred until an actual compatibility requirement exists. ADR-0006 is already Bootstrap; this decision uses the next free identifier, ADR-0008.

## Primary references

- [Python 3.11 uuid](https://docs.python.org/3.11/library/uuid.html): standard UUIDv4 support.
- [Python 3.14 uuid](https://docs.python.org/3.14/library/uuid.html): addition of UUID versions 6/7/8.
- [RFC 9562 section 5.4](https://www.rfc-editor.org/rfc/rfc9562.html#section-5.4): UUIDv4 version/variant layout and random payload.
