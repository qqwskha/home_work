import os
from typing import Dict, Any
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из .env
load_dotenv()

API_KEY: str = os.getenv("EXCHANGE_API_KEY")
BASE_URL: str = "https://api.apilayer.com/exchangerates_data/convert"

if not API_KEY:
    raise EnvironmentError("API_KEY for currency conversion is missing. Check your .env file.")


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными о транзакции. Ожидаются ключи 'operationAmount.amount' и 'operationAmount.currency.code'.
    :return: Сумма транзакции в рублях (float).
    :raises ValueError: При неверных данных транзакции.
    :raises ConnectionError: При ошибках соединения с API.
    """
    try:
        # Извлечение данных о транзакции
        operation_amount: Dict[str, Any] = transaction.get("operationAmount", {})
        amount: float = float(operation_amount.get("amount", 0.0))
        currency: str = operation_amount.get("currency", {}).get("code", "RUB")

        # Если валюта уже в рублях
        if currency == "RUB":
            return amount

        # Поддерживаются только USD и EUR
        if currency not in {"USD", "EUR"}:
            raise ValueError(f"Unsupported currency: {currency}")

        # Параметры запроса
        params: Dict[str, Any] = {
            "to": "RUB",
            "from": currency,
            "amount": amount,
        }

        headers: Dict[str, str] = {
            "apikey": API_KEY,
        }

        # Запрос к API
        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()  # Поднять исключение, если запрос завершился с ошибкой

        # Обработка ответа
        data: Dict[str, Any] = response.json()
        result = float(data.get("result", 0.0))
        return result
    except requests.RequestException as e:
        raise ConnectionError(f"Error connecting to the currency API: {e}")
    except KeyError as e:
        raise ValueError(f"Missing key in transaction data: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid transaction data: {e}")
