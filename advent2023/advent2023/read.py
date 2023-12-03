from pathlib import Path


def read_file(file_name) -> list[str]:
    path = Path(file_name)
    with path.open() as f:
        content = f.readlines()
    return [line.strip() for line in content]
