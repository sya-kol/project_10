import requests
import os
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()
api_key = os.getenv('API_KEY')
transaction={
     "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }

def get_exchange(transaction):
    """Функция конвертации валюты"""
    # Доступ к первому элементу списка
    if transaction["operationAmount"]["currency"]["code"] in ["USD", "EUR"]:
        money_to = 'RUB'
        money_from = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/currency_data/convert?to={money_to}&from={money_from}&amount={amount}"

        headers = {
            "apikey": api_key
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise ValueError(f"Failed to get currency rate")
        result = response.json()
        return result["result"]
    elif transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    else:
        return 'Некорректная валюта'

print(get_exchange(transaction))