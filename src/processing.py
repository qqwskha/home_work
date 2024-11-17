from datetime import datetime


def filter_by_state(data_list, state='EXECUTED'):
    """
    Фильтрует список словарей по заданному состоянию.

    :param data_list: list, список словарей с ключом 'state'.
    :param state: str, состояние для фильтрации (по умолчанию 'EXECUTED').
    :return: list, отфильтрованный список словарей.
    """
    return [item for item in data_list if item.get('state') == state]


def sort_by_date(data_list, descending=True):
    """
    Сортирует список словарей по дате.

    :param data_list: list, список словарей с ключом 'date'.
    :param descending: bool, порядок сортировки (по умолчанию по убыванию).
    :return: list, отсортированный список.
    """
    return sorted(data_list, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)
