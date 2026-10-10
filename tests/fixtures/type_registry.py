"""Explicit versioned composition fixture; production TYPE-01 remains absent."""
from dataclasses import replace
from semantic_kernel.public import SemanticVersion, QualifiedName, ElementVersionRef
from fixtures.type_validation import host, definition


def entry(number=0, version='1.0.0', name='sales.Customer', fields=(), context=None, absent=False):
    owner = replace(host(number, name), version=SemanticVersion.parse(version))
    if context is not None:
        owner = replace(owner, context=context)
    return definition(*fields, owner=owner, absent=absent)


def exact(model):
    owner = model.type_definition
    return ElementVersionRef(owner.id, owner.version)
