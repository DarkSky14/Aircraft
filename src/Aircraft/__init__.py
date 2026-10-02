import os
from Aircraft.config import *


class PathUrlFix:
    def __init__(self):
        self.path = os.path.join( #type: ignore
            os.path.abspath(__file__).removesuffix("\\__init__.py"), "library"
        )

    def get(self):
        return self.path


LIBRARY_ROOT = PathUrlFix()


def base_absolute_import(part: str) -> str:
    """Absolute way"""
    return os.path.join(LIBRARY_ROOT.get(), part)


def obsessed_absolute_import(*parts: str) -> str:
    """Absolute way"""
    library_status = False
    way = ""
    for part in parts:
        if not library_status:
            way = os.path.join(LIBRARY_ROOT.get(), part)
            library_status = True
        else:
            way = os.path.join(way, part)
    return way