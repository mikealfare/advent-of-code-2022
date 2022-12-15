from pathlib import Path
from typing import List


def get(file_name: str, static_root: Path = None) -> List[str]:
    if not static_root:
        static_root = Path(__file__).parent
    file = static_root / file_name
    contents = file.read_text()
    return contents.split('\n')
