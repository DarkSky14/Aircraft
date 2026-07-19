import os

SRC_ROOT = os.path.abspath(".")
LIBRARY_ROOT = os.path.join(SRC_ROOT, "library")


def absolute_import(*parts: str) -> str:
    """Absolute way"""
    return os.path.join(LIBRARY_ROOT, next(iter(parts)))
