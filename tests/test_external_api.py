import pytest
from unittest.mock import patch
from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 75.0}

    transaction = {"currency": "USD", "amount": 1.0}
    result = convert_to_rub(transaction)
    assert result == 75.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_eur(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 85.0}

    transaction = {"currency": "EUR", "amount": 1.0}
    result = convert_to_rub(transaction)
    assert result == 85.0


def test_convert_to_rub_rub():
    transaction = {"currency": "RUB", "amount": 100.0}
    result = convert_to_rub(transaction)
    assert result == 100.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_invalid_currency(mock_get):
    transaction = {"currency": "GBP", "amount": 1.0}
    with pytest.raises(ValueError):
        convert_to_rub(transaction)
