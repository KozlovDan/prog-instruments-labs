"""
Модуль для валидации CSV-файла с данными студентов.
"""

import csv
import re
from pathlib import Path
from typing import List

from checksum import calculate_checksum, serialize_result

CSV_FILE = Path("46.csv")
VARIANT = 46

VALIDATORS = [
    re.compile(r"^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$"),
    re.compile(r"^\d{3} [A-Z][A-Za-z]*(?: [A-Z][A-Za-z]*)*$"),
    re.compile(r"^\d{12}$"),
    re.compile(r"^\d{2}-\d{2}/\d{2}$"),
    re.compile(
        r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
        r"(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$"
    ),
    re.compile(r"^-?(?:[0-8]?\d(?:\.\d+)?|90(?:\.0+)?)$"),
    re.compile(r"^(A|B|AB|O)[+\u2212]$"),
    re.compile(
        r"^(?:\d-\d{5}-\d{3}-[\dX]|\d{3}-\d-\d{5}-\d{3}-[\dX])$"
    ),
    re.compile(
        r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    ),
    re.compile(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$")
]


def is_row_valid(row: List[str]) -> bool:
    if len(row) != len(VALIDATORS):
        return False

    for value, pattern in zip(row, VALIDATORS):
        if not pattern.fullmatch(value.strip()):
            return False

    return True


def find_invalid_rows(csv_path: Path) -> List[int]:
    invalid_rows: List[int] = []

    with csv_path.open(encoding="utf-16", newline="") as file:
        reader = csv.reader(file, delimiter=";")  # ← КЛЮЧЕВО
        next(reader)  # пропускаем заголовок

        for row_number, row in enumerate(reader):
            if not is_row_valid(row):
                invalid_rows.append(row_number)

    return invalid_rows


def main() -> None:
    invalid_rows = find_invalid_rows(CSV_FILE)
    checksum = calculate_checksum(invalid_rows)
    serialize_result(VARIANT, checksum)
    print(len(invalid_rows))
    print(invalid_rows[:20])


if __name__ == "__main__":
    main()
