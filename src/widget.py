from src.masks import get_mask_card_number, get_mask_account

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
    if "Счет" in data:
        account_number = data.split()[1]
        masked_number = get_mask_account(int(account_number))
        return f"Счет {masked_number}"
    else:
        card_number = data.split()[1]
        masked_number = get_mask_card_number(int(card_number))
        return f"{data.split()[0]} {data.split()[1][:2]}** **** {masked_number[-4:]}"


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
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"