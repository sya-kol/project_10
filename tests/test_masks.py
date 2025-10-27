import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "numbers, expected",
    [
        (7000792289606361, "7000 79** **** 6361"),
        ("0000000000000000", "0000 00** **** 0000"),
        ("0000000000009999", "0000 00** **** 9999"),
        (8888888888888888, "8888 88** **** 8888"),
    ],
)
def test_mask_card_number(numbers: int, expected: str):
    assert get_mask_card_number(numbers) == expected


@pytest.fixture
def number_card():
    return [70007922896063611, 700079228960636, "", "eeeeeeeeeeeeeeee", "1212ffffffffffff"]


def test_mask_card_number_format():
    with pytest.raises(ValueError):
        get_mask_card_number(number_card)


@pytest.mark.parametrize(
    "number_acc, expected",
    [
        (73654108430135874305, "**4305"),
        ("00000000000000000000", "**0000"),
        ("00000000000000009999", "**9999"),
        (88888888888888888888, "**8888"),
    ],
)
def test_mask_account(number_acc, expected):
    assert get_mask_account(number_acc) == expected


@pytest.fixture
def number_account():
    return [700079220000896063611, 700079228960636, "", "eeeeeeeeeeeeeeeeeeee", "11111111112131dgdfhd"]


def test_mask_account_format():
    with pytest.raises(ValueError):
        get_mask_account(number_account)
