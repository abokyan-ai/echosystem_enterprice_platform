# Configuration and secrets

architecture.json is versioned developer configuration, not tenant/runtime data. Future local overrides belong in ignored config/local.* files; test settings belong to fixtures. Keep secrets in environment variables or a secret provider and never commit .env files. Tenant and runtime configuration contracts will be introduced when their behavior is implemented.


ARC-04 ships `development.json` (all explicitly registered foundation markers) and `test.json` (empty activation). Profiles label environments; choosing a profile does not implicitly change module selection. Defaults < file < PLATFORM_* environment < CLI. See [bootstrap configuration](../docs/architecture/platform-bootstrap.md). Never put secrets in tracked files.
