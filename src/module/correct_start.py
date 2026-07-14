from pathlib import Path

SRC_ROOT: Path = Path(__file__).resolve().parent.parent
LIBRARY_ROOT: Path = SRC_ROOT / "library"


def absolute_import(*parts: str) -> str:
    """Absolute way"""
    return str(LIBRARY_ROOT.joinpath(*parts))
