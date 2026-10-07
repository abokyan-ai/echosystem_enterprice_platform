# Dependency rules

| Consumer | Permitted module dependencies |
| --- | --- |
| semantic-kernel | None |
| model-core | semantic-kernel |
| compiled-contracts | semantic-kernel |
| compiler-core | semantic-kernel, model-core, compiled-contracts |
| runtime-core | semantic-kernel, compiled-contracts |
| platform-cli | No feature dependencies; metadata/public registration inspection only |
| Future adapters | Explicitly approved platform public contracts |
| Future apps | Explicitly approved platform and adapter public APIs |

`architecture.json` defines module registration and allowlists. `scripts/check_architecture.py` validates registered source ownership, imports via Python AST (including imports nested inside functions), public entry points, external imports and cycles in the full permitted graph. Standard-library imports do not create architectural edges. Platform dynamic import helpers and direct dynamic code evaluation are rejected. Imports into another module must use `package.public`; namespace/internal imports are rejected.

Independent invariants also prevent manifest edits from authorizing kernel → model/compiler/runtime/artifacts, model → compiler/runtime, compiled-contracts → model/compiler/runtime, compiler → runtime, runtime → model/compiler, or platform → tools/adapters/apps. Frontend/database/YAML packages are denied by the external import allowlist. Registered new adapter/app imports are also blocked from platform by family ownership. Unregistered code in platform/adapters/apps/tools fails checking.

AT-001 through AT-006 use negative fixtures: kernel/runtime, kernel/compiler, platform/adapters, platform/apps, model/frontend and circular graphs. Additional fixtures cover private imports, valid public imports, dynamic imports, unregistered source, runtime authoring imports and invariant changes.

## Enforcement limits

This is static Python source policy, not a security boundary or cross-language analyzer. Reflection, computed attribute access, shell execution and file reads cannot all be proven safe by an AST import checker. Module-local test files and repository scripts are outside production module import enforcement. New languages, generated code, external dependencies and contract packaging need explicit ARC-02/ARC-03 extensions; do not claim enforcement for them yet. Python modules remain contract-disciplined, not language-independent wire schemas.
