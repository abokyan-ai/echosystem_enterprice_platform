"""Explicit development-only public imports for doctor registration checks."""
from semantic_kernel.public import MODULE_NAME as KERNEL
from model_core.public import MODULE_NAME as MODEL
from compiled_contracts.public import MODULE_NAME as CONTRACTS
from compiler_core.public import MODULE_NAME as COMPILER
from runtime_core.public import MODULE_NAME as RUNTIME

REGISTERED_PLATFORM_MODULES = {KERNEL, MODEL, CONTRACTS, COMPILER, RUNTIME}
