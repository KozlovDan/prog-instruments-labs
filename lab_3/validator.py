"""
Модуль для валидации CSV-файла с данными студентов.

Читает CSV-файл, валидирует каждую строку с использованием
регулярных выражений, собирает номера невалидных строк и
вычисляет контрольную сумму для проверки через GitHub Actions.
"""

import csv
import re
from pathlib import Path
from typing import List

from checksum import calculate_checksum, serialize_result



CSV_FILE = Path("46.csv")


VARIANT = 46


VALIDATORS = [
    re.compile(r"^[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"),

    re.compile(r"^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$"),

    re.compile(r"^\d{3} [A-Za-z ]+$"),

    re.compile(r"^(0\.[5-9]\d|[1-2]\.\d{2})$"),

    re.compile(r"^\d{11}$"),

    re.compile(r"^\d{12}$"),

    re.compile(r"^\d{2} \d{2} \d{6}$"),

    re.compile(r"^\d{2}-\d{2}/\d{2}$"),

    re.compile(
        r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
        r"(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$"
    ),

    re.compile(r"^[A-Za-zА-Яа-яЁё\- ]+$"),
]


def is_row_valid(row: List[str]) -> bool:
    """
    Проверяет одну строку CSV-файла на валидность.

    Строка считается валидной, если:
    - количество полей совпадает с количеством валидаторов
    - каждое поле полностью соответствует своему регулярному выражению

    :param row: список значений полей одной строки CSV
    :return: True, если строка валидна, иначе False
    """
    if len(row) != len(VALIDATORS):
        return False

    for value, pattern in zip(row, VALIDATORS):
        if not pattern.fullmatch(value.strip()):
            return False

    return True


def find_invalid_rows(csv_path: Path) -> List[int]:
    """
    Находит номера невалидных строк в CSV-файле.

    Первая строка CSV содержит заголовки и пропускается.
    Нумерация строк с данными начинается с 0
    (в соответствии с требованиями checksum.py).

    :param csv_path: путь к CSV-файлу
    :return: список номеров строк с ошибками валидации
    """
    invalid_rows: List[int] = []

    with csv_path.open(encoding="utf-16", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row_number, row in enumerate(reader):
            if not is_row_valid(row):
                invalid_rows.append(row_number)

    return invalid_rows


def main() -> None:
    """
    Точка входа в программу.

    Выполняет валидацию CSV-файла, вычисляет контрольную сумму
    по номерам невалидных строк и сериализует результат в result.json.
    """
    invalid_rows = find_invalid_rows(CSV_FILE)
    checksum = calculate_checksum(invalid_rows)
    serialize_result(VARIANT, checksum)


if __name__ == "__main__":
    main()
