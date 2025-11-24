transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions, currency):
    """Функция, которая принимает на вход список словарей, представляющих транзакции.
    Возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).
    Если структура транзакции не содержит нужных ключей,
    такая транзакция пропускается"""
    for transaction in transactions:
        try:
            # Проверяем, есть ли в транзакции валюта и совпадает ли её код с currency
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except KeyError:
            # Если нужных ключей нет — пропускаем эту транзакцию
            continue


def transaction_descriptions(transactions):
    """Функция генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        try:
            # Проверяем, есть ли в транзакции описание операции
            if transaction["description"]:
                yield transaction["description"]
        except KeyError:
            # Если описания операции нет — пропускаем эту транзакцию
            continue


def card_number_generator(start, end):
    """Функция генератор, который выдает номера банковских карт
    в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты.
    Генератор может сгенерировать номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров"""
    start_card = 1
    end_card = 9999999999999999
    if start < start_card:
        raise ValueError("Начальное значение не может быть меньше 1")
    if end > end_card:
        raise ValueError("Конечное значение не может быть больше 9999999999999999")
    if start > end:
        raise ValueError("Начальное значение не может быть больше конечного")

    for num in range(start, end + 1):
        num_card = str(num).zfill(16)
        yield f"{num_card[:4]} {num_card[4:8]} {num_card[8:12]} {num_card[12:]}"


usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))


for card_number in card_number_generator(1, 5):
    print(card_number)
