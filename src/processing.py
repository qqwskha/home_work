from datetime import datetime


def filter_by_state(data_list, state='EXECUTED'):
    """
    Фильтрует список словарей по заданному состоянию.

    :param data_list: list
        Список словарей, каждый из которых содержит ключ 'state'.
    :param state: str, optional
        Состояние для фильтрации. По умолчанию используется 'EXECUTED'.
    :return: list
        Новый список словарей, отфильтрованный по указанному состоянию.

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


def sort_by_date(data_list, descending=True):
    """
    Сортирует список словарей по ключу 'date'.

    :param data_list: list
        Список словарей, каждый из которых содержит ключ 'date' в формате ISO 8601.
    :param descending: bool, optional
        Если True, сортировка по убыванию (самые последние даты в начале).
        Если False, сортировка по возрастанию. По умолчанию True.
    :return: list
        Новый список словарей, отсортированный по ключу 'date'.

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
    return sorted(data_list, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
