# Test ownership

Module-local tests check registration markers. Root unit tests validate parsing/cycles/diagnostics; architecture tests cover AT-DEP-001..012 and negative fixtures. Contract tests import the actual public surface. Integration tests execute real root graph/validation commands. E2E tests cover doctor success and actionable failure. Compatibility/migration behavior remains deferred. Synthetic adapter/experience fixtures exist only in isolated temporary repositories and are never production modules.
