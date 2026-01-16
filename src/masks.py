import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_cart: int|str) -> str:
    """Функция принимает номер карты в виде числа и
    возвращает маску номера XXXX XX** **** XXXX"""
    logger.info("Начало работы функции get_mask_card_number")
    number_cart_str = str(number_cart)
    if len(number_cart_str) != 16 or not number_cart_str.isdigit():
        logger.error("Не тот формат номера карты")
        raise ValueError("Не тот формат номера карты")
    number_cart_mask = (
        number_cart_str[:4] + " " + number_cart_str[4:6] + "**" + " " + "****" + " " + number_cart_str[-4:]
    )
    logger.info(f"Окончание работы функции с возратом маски карты: {number_cart_mask}")
    return number_cart_mask


def get_mask_account(number_account: int|str) -> str:
    """Функция принимает номер счета в виде числа и
    возвращает маску номера **XXXX"""
    logger.info("Начало работы функции get_mask_account")
    number_account_str = str(number_account)
    if len(number_account_str) != 20 or not number_account_str.isdigit():
        # logger.error("Не тот формат номера счета")
        raise ValueError("Не тот формат номера счета")
    number_account_mask = "**" + number_account_str[-4:]
    logger.info(f"Окончание работы функции с возратом маски счета: {number_account_mask}")
    return number_account_mask


# if __name__ == '__main__':
#     print(get_mask_card_number("7000792289606361"))
#     print(get_mask_account("73654108430135874305"))