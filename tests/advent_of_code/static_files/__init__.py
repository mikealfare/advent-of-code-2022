from typing import List
from pathlib import Path

from advent_of_code import static_files


def get(file_name: str) -> List[str]:
    return static_files.get(file_name, Path(__file__).parent)
