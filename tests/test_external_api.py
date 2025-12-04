from unittest.mock import patch

import pytest

from src.external_api import get_exchange


@patch("src.external_api.requests.get")
def test_get_exchange_rub(mock_get):
    test_transaction_rub = {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 48223.05}
    result = get_exchange(test_transaction_rub)
    assert result == 48223.05


@patch("src.external_api.requests.get")
def test_get_exchange(mock_get):
    test_transaction_usd = {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 638597.9155}
    result = get_exchange(test_transaction_usd)
    assert result == 638597.9155


@patch("src.external_api.requests.get")
def test_get_exchange_unknown_currency(mock_get):
    test_transaction_us = {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "US", "code": "US"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }

    assert get_exchange(test_transaction_us) == "Некорректная валюта"


@patch("src.external_api.requests.get")
def test_get_exchange_api_error(mock_get):
    test_transaction = {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }

    # Настройка mock для возврата кода ошибки
    mock_get.return_value.status_code = 500

    # Проверка, что вызывается исключение
    with pytest.raises(ValueError, match="Failed to get currency rate"):
        get_exchange(test_transaction)
