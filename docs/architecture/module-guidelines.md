# Module guidelines

Each physical module has `src/<package>/public.py`, `src/<package>/internal/` and `tests/`. The namespace initializer is deliberately inert. Public contracts belong to their semantic owner, never an infrastructure project or generic dumping ground. Consumers import `public`, not internal files. Keep external library types out of public contracts unless a documented contract explicitly requires them.

Create a physical module when a meaningful dependency/ownership boundary exists and a real slice or stable shared contract needs it. Add the path/package/allowed edges in `architecture.json`, public entry point, focused tests and responsibility documentation. Root commands discover registered module source and unit tests automatically. New module tests must be importable by standard-library unittest discovery.

Do not introduce wrappers, service locators or network APIs to dissolve a dependency cycle. Redesign ownership or extract a small independently owned contract when justified. Add a port in the owning platform module when behavior requires a replaceable implementation, then implement it in an adapter and wire it in an application.

Extract a module into a separate process only with evidence of independent scaling, release cadence, fault isolation or compliance needs. First define serialization, compatibility, security, transactions, observability and failure behavior; process extraction is more than moving a directory. A possible future extraction does not justify a network hop today.

Generated code belongs outside source directories. Compatibility/migration rules accompany evolving public contracts when actual behavior exists. No semantic entities, persistence interfaces, compiler features or runtime services are created merely to populate ARC-01.
