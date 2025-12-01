from pathlib import Path

PARENT_DIR = Path(__file__).parent.parent.parent.resolve()

def locate_file(path_from_main: Path | str) -> Path:
    path = PARENT_DIR / path_from_main
    if not path.exists():
        raise FileNotFoundError(f"There's no such file as `{path}`")
    return path