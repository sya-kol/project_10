from .masks import get_mask_account, get_mask_card_number


def mask_account_card(name_type_number: str) -> str:
    """Функция, которая умеет обрабатывать информацию о картах и о счетах"""
    card_info = name_type_number.rsplit(" ", 1)
    if "Счет" in name_type_number:
        return f"{card_info[0]} {get_mask_account(int(card_info[1]))}"
    else:
        return f"{card_info[0]} {get_mask_card_number(int(card_info[1]))}"


def get_date(data: str) -> str:
    """Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ"""
    data_slice = data[:10]
    data_new = data_slice.split("-")
    return f"{data_new[2]}.{data_new[1]}.{data_new[0]}"