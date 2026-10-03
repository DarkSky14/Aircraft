import os


class PathUrlFix:
    def __init__(self):
        self.path = os.path.join( #type: ignore
            os.path.abspath(__file__).removesuffix("\\config\\__init__.py"), "library"
        )

    def get(self):
        return self.path


LIBRARY_ROOT = PathUrlFix()


def url_fixer(part: str) -> str:
    """Absolute way"""
    return os.path.join(LIBRARY_ROOT.get(), part)
