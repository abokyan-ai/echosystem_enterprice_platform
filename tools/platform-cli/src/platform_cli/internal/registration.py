"""Explicit development-only public imports for doctor registration checks."""
from semantic_kernel.public import MODULE_NAME as KERNEL
from model_core.public import MODULE_NAME as MODEL
from model_authoring.public import MODULE_NAME as AUTHORING
from compiled_contracts.public import MODULE_NAME as CONTRACTS
from compiler_core.public import MODULE_NAME as COMPILER
from runtime_core.public import MODULE_NAME as RUNTIME

from bootstrap_contracts.public import MODULE_NAME as BOOTSTRAP_CONTRACTS

CORE_MODULE_IDENTITIES = (KERNEL, MODEL, CONTRACTS, COMPILER, RUNTIME)
# Explicit tooling inventory name; a tooling-to-tooling import is forbidden.
# Root build independently verifies the loader public MODULE_NAME from the manifest.
REGISTERED_PLATFORM_MODULES = {*CORE_MODULE_IDENTITIES, BOOTSTRAP_CONTRACTS, AUTHORING, "model-loader"}
