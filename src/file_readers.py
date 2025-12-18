from typing import Any, Dict, List, Hashable

import pandas as pd


def func_read_csv(path: str) -> List[Dict[Hashable, Any]]:
    """Функция чтения csv-файла, выдает список словарей с транзакциями"""
    try:
        df = pd.read_csv(path)
        result = df.to_dict(orient="records")
        return result
    except FileNotFoundError:
        print("Файл не найден")
        return []


def func_read_excel(path: str) -> List[Dict[Hashable, Any]]:
    """Функция чтения excel-файла, выдает список словарей с транзакциями"""
    try:
        df = pd.read_excel(path)
        result = df.to_dict(orient="records")
        return result
    except FileNotFoundError:
        print("Файл не найден")
        return []


# if __name__ == '__main__':
#     rezult = func_read_excel('data/transactions_excel.xlsx')
#     print(rezult)


# if __name__ == '__main__':
#     rezult = func_read_csv('data/transactions.csv')
#     print(rezult)
