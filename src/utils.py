import json
import os


path_file_operation = os.path.join('data', 'operations.json')

def get_file_operation(path_file_operation: str) -> list[dict]:
    """Функция, которая принимает на вход путь до JSON-файла
        и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path_file_operation, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    print('Данные в файле не являются списком')
                    return []
                return data
            except json.decoder.JSONDecodeError:
                print('Ошибка чтении файла')
                return []
    except FileNotFoundError:
        print('Файл не найден!')
        return []

print(get_file_operation(path_file_operation))


