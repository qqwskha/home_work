import os
from typing import Dict, Union

import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из .env
load_dotenv()

API_KEY: str = os.getenv("EXCHANGE_API_KEY", "8QIKOjxqRyV6OktSA8fT0PEVHobGS7kz")
BASE_URL: str = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(transaction: Dict[str, Union[str, float]]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными о транзакции. Ожидаются ключи 'currency' и 'amount'.
    :return: Сумма транзакции в рублях (float).
    """
    currency: str = str(transaction.get('currency', 'RUB'))
    amount: float = float(transaction.get('amount', 0.0))

    if currency == 'RUB':
        return amount

    if currency not in {'USD', 'EUR'}:
        raise ValueError(f"Unsupported currency: {currency}")

    params: Dict[str, Union[str, float]] = {
        'to': 'RUB',
        'from': currency,
        'amount': amount
    }

    headers: Dict[str, str] = {
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    if response.status_code != 200:
        raise ConnectionError(f"Failed to fetch exchange rate: {response.status_code}")

    data: Dict[str, Union[str, float]] = response.json()
    return float(data.get('result', 0.0))
