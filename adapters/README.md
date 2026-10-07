# Infrastructure adapters

Future persistence/memory, persistence/postgres, messaging/in-process, frontend/react (or Angular/Flutter), and observability/console implementations belong here. Create a physical module only with the first needed adapter. Adapters implement platform-owned ports and import public contracts; platform code never imports adapters. Applications perform explicit in-process wiring. No database, broker or UI dependency is installed in ARC-01.
