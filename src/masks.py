def get_mask_card_number(number_cart: int) -> str:
    """Функция принимает номер карты в виде числа и
    возвращает маску номера XXXX XX** **** XXXX"""
    number_cart_str = str(number_cart)
    return f"{number_cart_str[:4]} {number_cart_str[4:6]}** **** {number_cart_str[-4:]}"


def get_mask_account(number_account: int) -> str:
    """Функция принимает номер счета в виде числа и
    возвращает маску номера **XXXX"""
    number_account_str = str(number_account)
    return f"**{number_account_str[-4:]}"