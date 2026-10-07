# Infrastructure adapters

Future persistence/memory, persistence/postgres, messaging/in-process, frontend/react (or Angular/Flutter), and observability/console implementations belong here. Create a physical module only with the first needed adapter. Adapters implement platform-owned ports and import public contracts; platform code never imports adapters. Applications perform explicit in-process wiring. No database, broker or UI dependency is installed in ARC-01.

Selected targets: `frontend/angular` with Angular + PrimeNG; `http/django-rest-framework` with Django + DRF; `data/memory` with contract-based production Mock Data and no database. These are documented boundaries, not installed packages or implemented modules. Declare zone/owner/profile/public APIs before introducing source; TypeScript analysis must be added for Angular code.
