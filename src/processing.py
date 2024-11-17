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


# Тестовые данные
if __name__ == "__main__":
    data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    # Пример работы filter_by_state
    print("Фильтрация по состоянию 'EXECUTED':")
    print(filter_by_state(data))

    print("\nФильтрация по состоянию 'CANCELED':")
    print(filter_by_state(data, state='CANCELED'))

    # Пример работы sort_by_date
    print("\nСортировка по дате (по убыванию):")
    print(sort_by_date(data))

    print("\nСортировка по дате (по возрастанию):")
    print(sort_by_date(data, descending=False))
