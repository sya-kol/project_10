from src.utils import get_file_operation
from src.file_readers import func_read_csv, func_read_excel
from src.processing import get_filter_by_state, get_sort_by_date
from src.generators import filter_by_currency
from src.bank_operations import process_bank_search, process_bank_operations
from src.widget import get_mask_account_card, get_date


def main():
    """Функция, которая отвечает за основную логику проекта
    и связывает функциональности между собой."""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        # Блок выбора из какого типа файлов будем получать информацию о транзакциях
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        user_choice = input("Выберете нужный вариант: ").strip()
        if user_choice == "1":
            file_json_path = 'data/operations.json'
            transactions = get_file_operation(file_json_path)
            print("Для обработки выбран JSON-файл")
            break
        elif user_choice == "2":
            file_csv_path = 'data/transactions.csv'
            transactions = func_read_csv(file_csv_path)
            print("Для обработки выбран CSV-файл")
            break
        elif user_choice == "3":
            file_excel_path = 'data/transactions_excel.xlsx'
            transactions = func_read_excel(file_excel_path)
            print("Для обработки выбран XLSX-файл")
            break
        else:
            print(f"Данный выбор {user_choice} не доступен")
            continue

    while True:
        # Блок выбора статуса, по которому необходимо выполнить фильтрацию
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status_user_choice = input().upper().strip()
        if status_user_choice in ["EXECUTED", "CANCELED", "PENDING"]:
            final_transactions = get_filter_by_state(transactions, status_user_choice)
            print(f"Операции отфильтрованы по статусу {status_user_choice}")
            break
        else:
            print(f"Статус операции {status_user_choice} недоступен.")
            continue


    while True:
        # Блок выбора нужно ли сортировать операции по дате и если да, то по возрастанию или по убыванию
        print("Отсортировать операции по дате?")
        sort_by_date_choice = input("Да/Нет: ").lower().strip()
        if sort_by_date_choice == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            user_choice_sort = input("возрастанию/убыванию: ").lower().strip()
            if user_choice_sort == "возрастанию":
                user_choice_filter = False
                final_transactions = get_sort_by_date(final_transactions, user_choice_filter)
                break
            elif user_choice_sort == "убыванию":
                final_transactions = get_sort_by_date(final_transactions)
                break
            else:
                print("Не верный формат выбора.")
                continue
        elif sort_by_date_choice == "нет":
            break
        else:
            print("Не верный формат выбора.")
            continue


    while True:
        # Блок выбора в какой валюте выводить транзакции в консоль
        print("Выводить только рублевые транзакции?")
        user_choice_currency = input("Да/Нет: ").lower().strip()
        if user_choice_currency == "да":
            final_transactions = list(filter_by_currency(final_transactions, 'RUB'))
            break
        elif user_choice_currency.lower() == "нет":
            break
        else:
            print("Не верный формат выбора.")
            continue


    while True:
        # Блок выбора по полю "description"
        print("Отфильтровать список транзакций по определенному слову в описании?")
        user_choice_word = input("Да/Нет: ").lower().strip()
        if user_choice_word in ["да", "нет"]:
            if user_choice_word == "да":
                filter_word = input("Введите слово: ")
                final_transactions = process_bank_search(final_transactions, filter_word)
                break
            else:
                break
        else:
            print("Не верный формат выбора.")
            continue


    # Блок печати
    print("Распечатываю итоговый список транзакций...")
    print(f"{process_bank_operations(final_transactions, filter_word)}")
    for trans in final_transactions:
        print(f"{get_date(trans['date'])} {trans['description']}\n"
              f"{get_mask_account_card(trans['from'])} -> {get_mask_account_card(trans['to'])}\n"
              f"Сумма: {trans['operationAmount']['amount']} {trans['operationAmount']['currency']['name']}")


if __name__ == '__main__':
    main()
