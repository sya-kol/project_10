import pytest

from src.widget import get_date, get_mask_account_card


@pytest.mark.parametrize(
    "info_numbers, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card(info_numbers, expected):
    assert get_mask_account_card(info_numbers) == expected


@pytest.mark.parametrize(
    "number_card_account, expected",
    [
        ("maestro 1596837868705199", "maestro 1596 83** **** 5199"),
        ("счет 73654108430135874305", "счет **4305"),
        ("СЧЕТ 35383033474447895560", "СЧЕТ **5560"),
        ("Банковский счет 35383033474447895560", "Банковский счет **5560"),
    ],
)
def test_mask_account_card_register(number_card_account, expected):
    assert get_mask_account_card(number_card_account) == expected


def test_mask_account_card_empty_list():
    with pytest.raises(ValueError):
        get_mask_account_card("")


def test_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_date_card_empty_list():
    with pytest.raises(ValueError):
        get_date("")


@pytest.mark.parametrize(
    "data_info, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-03-11T02:26:18", "11.03.2024")]
)
def test_mask_account_card_format(data_info, expected):
    assert get_date(data_info) == expected
