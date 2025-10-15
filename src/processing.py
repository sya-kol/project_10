from typing import List, Dict


def filter_by_state(banking_operation: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Функция принимает список словарей и значение для ключа state и
    возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    filtered_operations = []
    for operation in banking_operation:
        if operation.get('state') == state:
            filtered_operations.append(operation)
    return filtered_operations


def sort_by_date(banking_operation: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция принимает список словарей и параметр,
    задающий порядок сортировки (по умолчанию — убывание),
    возвращает новый список, отсортированный по дате"""
    return sorted(banking_operation, key=lambda x: x.get('date'), reverse=reverse)
