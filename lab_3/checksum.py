import json
import hashlib
from typing import List
from pathlib import Path

RESULT_FILE = Path("result.json")


def calculate_checksum(row_numbers: List[int]) -> str:
    row_numbers.sort()
    return hashlib.md5(
        json.dumps(row_numbers).encode("utf-8")
    ).hexdigest()


def serialize_result(variant: int, checksum: str) -> None:
    data = {
        "variant": str(variant),
        "checksum": checksum,
    }

    with RESULT_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
