"""
Модуль с функциями для вычисления и сериализации контрольной суммы.
Используется для автоматической проверки результатов лабораторной
работы через GitHub Actions.
"""

import json
import hashlib
from typing import List
from pathlib import Path

RESULT_FILE = Path("result.json")


def calculate_checksum(row_numbers: List[int]) -> str:
    """
    Вычисляет MD5-хеш от списка номеров строк.
    Перед вычислением список сортируется (для стабильного результата).
    Нумерация строк должна начинаться с 0.

    :param row_numbers: список номеров строк с ошибками валидации
    :return: строка с MD5-хешем
    """
    normalized = sorted(int(x) for x in row_numbers)

    # Важно: компактный JSON без пробелов, иначе MD5 будет отличаться
    payload = json.dumps(normalized, separators=(",", ":"), ensure_ascii=False)

    return hashlib.md5(payload.encode("utf-8")).hexdigest()


def serialize_result(variant: int, checksum: str) -> None:
    """
    Сериализует результат выполнения лабораторной работы в JSON-файл.
    Файл result.json содержит номер варианта и вычисленную
    контрольную сумму. Структура файла не должна изменяться,
    так как используется GitHub Actions для проверки.

    :param variant: номер варианта лабораторной работы
    :param checksum: контрольная сумма
    """
    data = {
        "variant": str(variant),
        "checksum": checksum,
    }

    with RESULT_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


if name == "__main__":
    print(calculate_checksum([1, 2, 3]))
    print(calculate_checksum([3, 2, 1]))