import os

SRC_ROOT = os.path.abspath(".")
LIBRARY_ROOT = os.path.join(SRC_ROOT, "library")


def base_absolute_import(part: str) -> str:
    """Absolute way"""
    return os.path.join(LIBRARY_ROOT, part)

def obsessed_absolute_import(*parts: str) -> str:
    """Absolute way"""
    library_status = False
    for part in parts:
        if not library_status:
            way = os.path.join(LIBRARY_ROOT, part)
            library_status = True
        else:
            way = os.path.join(way, part)
    return way