import os


class PathUrlFix:
    def __init__(self):
        main_root = os.path.abspath(".")
        reserve_root = os.path.abspath(__file__).removesuffix("\\config\\__init__.py")

        if main_root == reserve_root or "AppData\\Local\\Temp" in reserve_root:
            root = main_root
        else:
            root = reserve_root

        self.path = os.path.join( #type: ignore
            root, "library"
        )

        self._debug_ = (
            f"[path: {self.path}] "
            f"[main_root: {main_root}] "
            f"[reserve_root: {reserve_root}] "
        )

    def get(self):
        return self.path

    def debug(self):
        return self._debug_


LIBRARY_ROOT = PathUrlFix()


def url_fixer(part: str) -> str:
    """Absolute way"""
    return os.path.join(LIBRARY_ROOT.get(), part)
