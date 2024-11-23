# src/widget.py

from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от переданного типа.

    Аргумент:
    data (str): Строка, содержащая тип и номер карты или счета.

    Возвращает:
    str: Строка с замаскированным номером.

    Примеры:
    >>> mask_account_card("Visa Platinum 7000792289606361")
    'Visa Platinum 7000 79** **** 6361'
    >>> mask_account_card("Счет 73654108430135874305")
    'Счет **4305'
    """
    parts = data.split()
    if not parts:
        raise ValueError("Input data is empty.")

    if "Счет" in data:
        if len(parts) < 2:
            raise ValueError("Account number is missing.")
        account_number = parts[1]
        if not account_number.isdigit():
            raise ValueError("Account number must be numeric.")
        # Маскируем номер счета
        masked_number = get_mask_account(int(account_number))
        return f"Счет {masked_number}"
    else:
        if len(parts) < 2:
            raise ValueError("Card number is missing.")
        card_number = parts[-1]
        if not card_number.isdigit():
            raise ValueError("Card number must be numeric.")
        # Маскируем номер карты
        masked_number = get_mask_card_number(int(card_number))
        # Собираем тип карты и маскированный номер
        card_type = ' '.join(parts[:-1])
        return f"{card_type} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Форматирует строку даты из формата "YYYY-MM-DDTHH:MM:SS.ssssss"
    в формат "ДД.ММ.ГГГГ".

    Аргумент:
    date_str (str): Строка с датой.

    Возвращает:
    str: Отформатированная дата в виде строки.

    Примеры:
    >>> get_date("2024-03-11T02:26:18.671407")
    '11.03.2024'
    """
    try:
        # Проверяем корректность формата даты
        date = datetime.fromisoformat(date_str)
        return date.strftime("%d.%m.%Y")
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid date string: {date_str}") from e
