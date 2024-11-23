from datetime import datetime
from typing import List, Dict


def filter_by_state(data_list: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по заданному состоянию.

    :param data_list: List[Dict]
        Список словарей, каждый из которых содержит ключ 'state'.
    :param state: str, optional
        Состояние для фильтрации. По умолчанию 'EXECUTED'.
    :return: List[Dict]
        Отфильтрованный список словарей.

    Примеры использования:
    >>> data = [
    ...     {'id': 1, 'state': 'EXECUTED', 'date': '2023-11-01T12:00:00'},
    ...     {'id': 2, 'state': 'CANCELED', 'date': '2023-11-02T13:00:00'}
    ... ]
    >>> filter_by_state(data)
    [{'id': 1, 'state': 'EXECUTED', 'date': '2023-11-01T12:00:00'}]
    >>> filter_by_state(data, state='CANCELED')
    [{'id': 2, 'state': 'CANCELED', 'date': '2023-11-02T13:00:00'}]
    """
    return [item for item in data_list if item.get('state') == state]


def sort_by_date(data_list: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.

    :param data_list: List[Dict]
        Список словарей, содержащих ключ 'date' в формате ISO 8601.
    :param descending: bool, optional
        Порядок сортировки: True для убывания, False для возрастания. По умолчанию True.
    :return: List[Dict]
        Отсортированный список словарей.

    Примеры использования:
    >>> data = [
    ...     {'id': 1, 'state': 'EXECUTED', 'date': '2023-11-01T12:00:00'},
    ...     {'id': 2, 'state': 'CANCELED', 'date': '2023-11-02T13:00:00'}
    ... ]
    >>> sort_by_date(data)
    [{'id': 2, 'state': 'CANCELED', 'date': '2023-11-02T13:00:00'}, {'id': 1, 'state': 'EXECUTED', 'date': '2023-11-01T12:00:00'}]
    >>> sort_by_date(data, descending=False)
    [{'id': 1, 'state': 'EXECUTED', 'date': '2023-11-01T12:00:00'}, {'id': 2, 'state': 'CANCELED', 'date': '2023-11-02T13:00:00'}]
    """
    return sorted(
        data_list,
        key=lambda x: datetime.fromisoformat(x['date']),
        reverse=descending
    )


if __name__ == "__main__":
    import doctest
    doctest.testmod()
