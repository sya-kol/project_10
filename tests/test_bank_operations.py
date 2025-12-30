import pytest


from src.bank_operations import process_bank_operations_count, process_bank_search


@pytest.mark.parametrize(
    "data, search, expected",
    [
        (
            [
                {"description": "Перевод со счета на счет", "amount": 100},
                {"description": "Открытие вклада", "amount": 200},
                {"description": "Перевод организации", "amount": 50},
            ],
            "Перевод",
            [
                {"description": "Перевод со счета на счет", "amount": 100},
                {"description": "Перевод организации", "amount": 50},
            ],
        ),
        (
            [
                {"description": "Перевод со счета на счет", "amount": 200},
                {"description": "Перевод организации", "amount": 250},
            ],
            "Открытие",
            [],
        ),
        ([], "Перевод", []),
    ],
)
def test_process_bank_search(data, search, expected):
    # Проверяем, что функция правильно находит все операции, содержащие "Перевод" в их описании.
    result = process_bank_search(data, search)
    assert result == expected


# def test_process_bank_search_basic():
#     # Проверяем, что функция правильно находит все операции, содержащие "Перевод" в их описании.
#     data = [
#         {"description": "Перевод со счета на счет", "amount": 100},
#         {"description": "Открытие вклада", "amount": 200},
#         {"description": "Перевод организации", "amount": 50},
#     ]
#     search = "Перевод"
#     expected = [
#         {"description": "Перевод со счета на счет", "amount": 100},
#         {"description": "Перевод организации", "amount": 50},
#     ]
#     result = process_bank_search(data, search)
#     assert result == expected


def test_process_bank_search_no_match():
    # Проверяем случай, когда ни одна из операций не содержит "Открытие".
    data = [
        {"description": "Перевод со счета на счет", "amount": 200},
        {"description": "Перевод организации", "amount": 250},
    ]
    search = "Открытие"
    expected = []
    result = process_bank_search(data, search)
    assert result == expected


def test_process_bank_search_empty_data():
    # Проверяем случай, когда список операций пустой
    data = []
    search = "Перевод"
    expected = []
    result = process_bank_search(data, search)
    assert result == expected


@pytest.mark.parametrize(
    "data, categories, expected",
    [
        (
            [
                {"description": "Перевод организации", "amount": 100},
                {"description": "Перевод со счета на счет", "amount": 50},
                {"description": "Открытие вклада", "amount": 150},
                {"description": "Перевод с карты на карту", "amount": 200},
            ],
            ["Перевод", "Открытие"],
            {"Перевод": 3, "Открытие": 1},
        ),
        (
            [
                {"description": "Перевод организации", "amount": 500},
                {"description": "Перевод со счета на счет", "amount": 150},
            ],
            ["Открытие вклада", "Перевод с карты на карту"],
            {},
        ),
        ([], ["Открытие вклада", "Перевод с карты на карту"], {}),
    ],
)
def test_process_bank_operations_count(data, categories, expected):
    # Проверяем, что функция правильно считает количество операций для каждой категории из списка.
    result = process_bank_operations_count(data, categories)
    assert result == expected


# def test_process_bank_operations_count_basic():
#     # Проверяем, что функция правильно считает количество операций для каждой категории из списка.
#     data = [
#         {"description": "Перевод организации", "amount": 100},
#         {"description": "Перевод со счета на счет", "amount": 50},
#         {"description": "Открытие вклада", "amount": 150},
#         {"description": "Перевод с карты на карту", "amount": 200},
#     ]
#     categories = ["Перевод", "Открытие"]
#     expected = {"Перевод": 3, "Открытие": 1}
#     result = process_bank_operations_count(data, categories)
#     assert result == expected


def test_process_bank_operations_count_no_category_match():
    # Проверяем случай, когда ни одна из категорий операций не совпадает с данными.
    data = [
        {"description": "Перевод организации", "amount": 500},
        {"description": "Перевод со счета на счет", "amount": 150},
    ]
    categories = ["Открытие вклада", "Перевод с карты на карту"]
    expected = {}
    result = process_bank_operations_count(data, categories)
    assert result == expected


def test_process_bank_operations_count_empty_data():
    # Проверяет случай, когда список операций пустой.
    data = []
    categories = ["Открытие вклада", "Перевод с карты на карту"]
    expected = {}
    result = process_bank_operations_count(data, categories)
    assert result == expected
