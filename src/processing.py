from datetime import datetime
from typing import Dict, List


def get_filter_by_state(banking_operation: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция принимает список словарей и значение для ключа state и
    возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    filtered_operations = []
    for operation in banking_operation:
        if operation.get("state") == state:
            filtered_operations.append(operation)
    if filtered_operations == []:
        raise ValueError("Нет такого статуса")
    return filtered_operations


def get_sort_by_date(banking_operation: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция принимает список словарей и параметр,
    задающий порядок сортировки (по умолчанию — убывание),
    возвращает новый список, отсортированный по дате"""
    def is_valid_date(date_str):
        try:
            # Используем strptime для проверки корректности даты
            datetime.fromisoformat(date_str)
            return True
        except ValueError:
            raise ValueError("Некорректная дата: {}".format(date_str))
    # Отфильтруем только корректные даты
    valid_operations = []
    for op in banking_operation:
        if is_valid_date(op.get("date", "")):
            valid_operations.append(op)
    return sorted(valid_operations, key=lambda x: x.get("date"), reverse=reverse)
