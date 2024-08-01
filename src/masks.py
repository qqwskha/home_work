def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маскированный номер банковской карты.

    Маска скрывает цифры номера карты, оставляя видимыми только первые 6 и последние 4 цифры.
    Формат маски: XXXX XX** **** XXXX.

    Параметры:
    card_number (int): Номер банковской карты.

    Возвращает:
    str: Маскированный номер карты.

    Пример:
    >>> get_mask_card_number(7000792289606361)
    '7000 79** **** 6361'
    """
    card_str = str(card_number)
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Возвращает маскированный номер банковского счета.

    Маска скрывает цифры номера счета, оставляя видимыми только последние 4 цифры.
    Формат маски: **XXXX.

    Параметры:
    account_number (int): Номер банковского счета.

    Возвращает:
    str: Маскированный номер счета.

    Пример:
    >>> get_mask_account(73654108430135874305)
    '**4305'
    """
    account_str = str(account_number)
    if len(account_str) < 4:
        raise ValueError("Номер счета должен содержать не менее 4 цифр.")
    return f"**{account_str[-4:]}"
