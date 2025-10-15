from typing import List, Dict


def filter_by_state(banking_operations: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]:
    """Функция принимает список словарей и значение для ключа state и
    возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    filtered_operations = []
    for operation in banking_operations:
        if operation.get('state') == state:
            filtered_operations.append(operation)
    return filtered_operations
