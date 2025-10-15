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

banking_operation = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

print(filter_by_state(banking_operation))
print(sort_by_date(banking_operation))
