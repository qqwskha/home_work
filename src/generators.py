from typing import List, Dict, Iterator, Generator


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по заданной валюте.

    :param transactions: список транзакций (каждая транзакция представлена словарем).
    :param currency_code: код валюты для фильтрации (например, "USD").
    :return: итератор с транзакциями в заданной валюте.

    Пример использования:
    >>> transactions = [
    ...     {"operationAmount": {"currency": {"code": "USD"}}},
    ...     {"operationAmount": {"currency": {"code": "RUB"}}},
    ... ]
    >>> list(filter_by_currency(transactions, "USD"))
    [{'operationAmount': {'currency': {'code': 'USD'}}}]
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """
    Генерирует описания транзакций по запросу.

    :param transactions: список транзакций (каждая транзакция представлена словарем).
    :yield: описание каждой транзакции.

    Пример использования:
    >>> transactions = [{"description": "Перевод организации"}, {"description": "Перевод со счета на счет"}]
    >>> desc = transaction_descriptions(transactions)
    >>> next(desc)
    'Перевод организации'
    """
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX.

    :param start: начальное значение для генерации.
    :param stop: конечное значение для генерации.
    :yield: номер карты в формате строки.

    Пример использования:
    >>> list(card_number_generator(1, 3))
    ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003']
    """
    for number in range(start, stop + 1):
        card_number = f"{number:016}"  # Форматируем в строку длиной 16 символов с ведущими нулями
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"