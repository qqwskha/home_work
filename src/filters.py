import re
from collections import Counter
from typing import List, Dict, Any


def filter_transactions_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций, возвращая только те, где описание содержит указанную строку.

    :param transactions: Список транзакций в виде словарей.
    :param search_string: Строка для поиска в описании.
    :return: Список отфильтрованных транзакций.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [t for t in transactions if pattern.search(t.get("description", ""))]


def count_transaction_categories(transactions: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям.

    :param transactions: Список транзакций.
    :return: Словарь: ключ — категория, значение — количество операций.
    """
    descriptions = [t.get("description", "Неизвестная категория").strip() for t in transactions]
    return dict(Counter(descriptions))
