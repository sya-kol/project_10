import json
import logging
import os

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


path_file_operation = os.path.join("data", "operations.json")


def get_file_operation(path_file_operation: str) -> list[dict]:
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    logger.info("Начало работы функции")
    try:
        with open(path_file_operation, "r", encoding="utf-8") as file:
            logger.info(f"Открываем json файл: {path_file_operation}")
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    logger.error(f"Данные в файле: {path_file_operation}, не являются списком")
                    print("Данные в файле не являются списком")
                    return []
                return data
            except json.decoder.JSONDecodeError as ex:
                logger.error(f"Ошибка: {ex} в файле: {path_file_operation}")
                print("Ошибка чтении файла")
                return []
    except FileNotFoundError:
        logger.error(f"Файл: {path_file_operation}  не найден!")
        print("Файл не найден!")
        return []


# print(get_file_operation(path_file_operation))
