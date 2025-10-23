from curses.ascii import isdigit


def get_mask_card_number(number_cart: str) -> str:
    """Функция принимает номер карты в виде числа и
    возвращает маску номера XXXX XX** **** XXXX"""
    number_cart_str = str(number_cart)
    if len(number_cart_str) != 16 or not number_cart_str.isdigit():
        raise ValueError("Не тот формат номера карты")
    number_cart_mask = number_cart_str[:4] + " " + number_cart_str[4:6] + "**" + " " + "****" + " " + number_cart_str[-4:]
    return number_cart_mask


def get_mask_account(number_account: str) -> str:
    """Функция принимает номер счета в виде числа и
    возвращает маску номера **XXXX"""
    number_account_str = str(number_account)
    if len(number_account_str) != 20 or not number_account_str.isdigit():
        raise ValueError("Не тот формат номера карты")
    number_account_mask = "**" + number_account_str[-4:]
    return number_account_mask
