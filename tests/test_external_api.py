from typing import Dict, Union
from unittest.mock import MagicMock, patch

import pytest

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get: MagicMock) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 75.0}

    transaction: Dict[str, Union[str, float]] = {"currency": "USD", "amount": 1.0}
    result = convert_to_rub(transaction)
    assert result == 75.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_eur(mock_get: MagicMock) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 85.0}

    transaction: Dict[str, Union[str, float]] = {"currency": "EUR", "amount": 1.0}
    result = convert_to_rub(transaction)
    assert result == 85.0


def test_convert_to_rub_rub() -> None:
    transaction: Dict[str, Union[str, float]] = {"currency": "RUB", "amount": 100.0}
    result = convert_to_rub(transaction)
    assert result == 100.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_invalid_currency(mock_get: MagicMock) -> None:
    transaction: Dict[str, Union[str, float]] = {"currency": "GBP", "amount": 1.0}
    with pytest.raises(ValueError):
        convert_to_rub(transaction)
