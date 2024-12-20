from typing import Dict
from unittest.mock import MagicMock, patch

import pytest
import requests

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get: MagicMock) -> None:
    """Тест успешной конвертации из USD в RUB."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 7500.0}

    transaction: Dict[str, Dict] = {
        "operationAmount": {
            "amount": 100.0,
            "currency": {
                "code": "USD"
            }
        }
    }
    result = convert_to_rub(transaction)
    assert result == 7500.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_eur(mock_get: MagicMock) -> None:
    """Тест успешной конвертации из EUR в RUB."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 8500.0}

    transaction: Dict[str, Dict] = {
        "operationAmount": {
            "amount": 100.0,
            "currency": {
                "code": "EUR"
            }
        }
    }
    result = convert_to_rub(transaction)
    assert result == 8500.0


def test_convert_to_rub_rub() -> None:
    """Тест: конвертация из RUB в RUB возвращает ту же сумму."""
    transaction: Dict[str, Dict] = {
        "operationAmount": {
            "amount": 100.0,
            "currency": {
                "code": "RUB"
            }
        }
    }
    result = convert_to_rub(transaction)
    assert result == 100.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_invalid_currency(mock_get: MagicMock) -> None:
    """Тест ошибки при неподдерживаемой валюте."""
    transaction: Dict[str, Dict] = {
        "operationAmount": {
            "amount": 100.0,
            "currency": {
                "code": "GBP"
            }
        }
    }
    with pytest.raises(ValueError):
        convert_to_rub(transaction)


@patch("src.external_api.requests.get")
def test_convert_to_rub_api_error(mock_get: MagicMock) -> None:
    """Тест ошибки API."""
    mock_get.side_effect = requests.RequestException("API Error")
    transaction: Dict[str, Dict] = {
        "operationAmount": {
            "amount": 100.0,
            "currency": {
                "code": "USD"
            }
        }
    }
    with pytest.raises(ConnectionError):
        convert_to_rub(transaction)
