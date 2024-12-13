import os
from typing import Dict, Union
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из .env
load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(transaction: Dict[str, Union[str, float]]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными о транзакции. Ожидаются ключи 'currency' и 'amount'.
    :return: Сумма транзакции в рублях (float).
    """
    currency = transaction.get('currency', 'RUB')
    amount = transaction.get('amount', 0.0)

    if currency == 'RUB':
        return float(amount)

    if currency not in {'USD', 'EUR'}:
        raise ValueError(f"Unsupported currency: {currency}")

    params = {
        'to': 'RUB',
        'from': currency,
        'amount': amount
    }

    headers = {
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    if response.status_code != 200:
        raise ConnectionError(f"Failed to fetch exchange rate: {response.status_code}")

    data = response.json()
    return float(data.get('result', 0.0))
