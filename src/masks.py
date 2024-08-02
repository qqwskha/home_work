# src/masks.py


def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты по правилу XXXX XX** **** XXXX.

    Аргумент:
    card_number (int): Номер карты в виде числа.

    Возвращает:
    str: Маскированный номер карты.

    Примеры:
    >>> get_mask_card_number(7000792289606361)
    '7000 79** **** 6361'
    """
    card_str = str(card_number)
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счета по правилу **XXXX.

    Аргумент:
    account_number (int): Номер счета в виде числа.

    Возвращает:
    str: Маскированный номер счета.

    Примеры:
    >>> get_mask_account(73654108430135874305)
    '**4305'
    """
    account_str = str(account_number)
    return f"**{account_str[-4:]}"
