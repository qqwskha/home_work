import os
from typing import Dict, Union
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из .env
load_dotenv()

API_KEY: str = os.getenv("EXCHANGE_API_KEY", "8QIKOjxqRyV6OktSA8fT0PEVHobGS7kz")
BASE_URL: str = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(transaction: Dict[str, Union[str, Dict[str, Union[float, Dict[str, str]]]]]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными о транзакции. Ожидаются ключи 'operationAmount.amount' и 'operationAmount.currency.code'.
    :return: Сумма транзакции в рублях (float).
    """
    try:
        # Извлечение суммы и валюты
        amount: float = float(transaction.get("operationAmount", {}).get("amount", 0.0))
        currency: str = transaction.get("operationAmount", {}).get("currency", {}).get("code", "RUB")

        if currency == "RUB":
            return amount

        if currency not in {"USD", "EUR"}:
            raise ValueError(f"Unsupported currency: {currency}")

        params: Dict[str, Union[str, float]] = {
            "to": "RUB",
            "from": currency,
            "amount": amount,
        }

        headers: Dict[str, str] = {
            "apikey": "8QIKOjxqRyV6OktSA8fT0PEVHobGS7kz",
        }

        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()  # Поднимает исключение при неудачном запросе

        data: Dict[str, Union[str, float]] = response.json()
        return float(data.get("result", 0.0))
    except requests.RequestException as e:
        raise ConnectionError(f"Error connecting to the currency API: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid transaction data: {e}")
