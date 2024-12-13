from unittest.mock import MagicMock, patch

import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тесты для функции get_mask_card_number
def test_get_mask_card_number_success() -> None:
    """Тест успешного маскирования номера карты."""
    card_number = 7000792289606361
    result = get_mask_card_number(card_number)
    assert result == "7000 79** **** 6361"


def test_get_mask_card_number_invalid_number() -> None:
    """Тест ошибки при неверном номере карты."""
    card_number = 12345  # Меньше 16 цифр
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@patch("src.masks.logger")
def test_get_mask_card_number_logging_success(mock_logger: MagicMock) -> None:
    """Тест логгирования успешного маскирования номера карты."""
    card_number = 7000792289606361
    result = get_mask_card_number(card_number)
    assert result == "7000 79** **** 6361"
    mock_logger.debug.assert_called_with(f"Masking card number: {card_number}")
    mock_logger.info.assert_called_with("Successfully masked card number: 7000 79** **** 6361")


@patch("src.masks.logger")
def test_get_mask_card_number_logging_error(mock_logger: MagicMock) -> None:
    """Тест логгирования ошибки при неверном номере карты."""
    card_number = 12345  # Меньше 16 цифр
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)
    mock_logger.debug.assert_called_with(f"Masking card number: {card_number}")
    mock_logger.error.assert_called()


# Тесты для функции get_mask_account
def test_get_mask_account_success() -> None:
    """Тест успешного маскирования номера счета."""
    account_number = 73654108430135874305
    result = get_mask_account(account_number)
    assert result == "**4305"


def test_get_mask_account_invalid_number() -> None:
    """Тест ошибки при неверном номере счета."""
    account_number = -12345  # Номер счета не может быть отрицательным
    with pytest.raises(ValueError):
        get_mask_account(account_number)


@patch("src.masks.logger")
def test_get_mask_account_logging_success(mock_logger: MagicMock) -> None:
    """Тест логгирования успешного маскирования номера счета."""
    account_number = 73654108430135874305
    result = get_mask_account(account_number)
    assert result == "**4305"
    mock_logger.debug.assert_called_with(f"Masking account number: {account_number}")
    mock_logger.info.assert_called_with("Successfully masked account number: **4305")


@patch("src.masks.logger")
def test_get_mask_account_logging_error(mock_logger: MagicMock) -> None:
    """Тест логгирования ошибки при неверном номере счета."""
    account_number = -12345  # Номер счета не может быть отрицательным
    with pytest.raises(ValueError):
        get_mask_account(account_number)
    mock_logger.debug.assert_called_with(f"Masking account number: {account_number}")
    mock_logger.error.assert_called()
