import logging

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Логирование в файл
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


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
    try:
        logger.debug(f"Masking card number: {card_number}")
        if not isinstance(card_number, int) or card_number < 1000000000000000:
            raise ValueError("Invalid card number: must be a positive integer with at least 16 digits.")
        card_str = str(card_number)
        masked_number = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
        logger.info(f"Successfully masked card number: {masked_number}")
        return masked_number
    except ValueError as e:
        logger.error(f"Error masking card number: {e}")
        raise


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
    try:
        logger.debug(f"Masking account number: {account_number}")
        if not isinstance(account_number, int) or account_number < 1:
            raise ValueError("Invalid account number: must be a positive integer.")
        account_str = str(account_number)
        masked_account = f"**{account_str[-4:]}"
        logger.info(f"Successfully masked account number: {masked_account}")
        return masked_account
    except ValueError as e:
        logger.error(f"Error masking account number: {e}")
        raise
