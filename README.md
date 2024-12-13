# Data Processing Project

## Этот проект предоставляет функции для работы с банковскими операциями и данными. Основные модули и функции включают:

### Маскирование данных:
- `get_mask_card_number`: маскирование номера карты.
- `get_mask_account`: маскирование номера счета.
### Фильтрация и сортировка операций:
- `filter_by_state`: фильтрация списка операций по заданному состоянию.
- `sort_by_date`: сортировка списка операций по дате.
### Обработка данных с генераторами:
- `filter_by_currency`: итератор для фильтрации транзакций по заданной валюте.
- `transaction_descriptions`: генератор, возвращающий описание транзакций.
- `card_number_generator`: генератор, создающий номера карт в формате `XXXX XXXX XXXX XXXX`.
- `mask_account_card`: выборочное маскирование данных (карта или счет).
- `get_date`: преобразование даты в читаемый формат.
- 
### Проект ориентирован на упрощение работы с банковскими операциями, автоматизацию обработки данных и обеспечение безопасности.

## Установка

1. Склонируйте репозиторий:
   ```bash
   git clone <git@github.com:qqwskha/home_work.git>
   
## Проверка покрытия тестами

Для проверки покрытия кода тестами выполните команду:
- `pytest --cov`

# Использование

### Маскирование номеров карт и счетов

`from src.masks import get_mask_card_number, get_mask_account`

### Маскирование карты
`print(get_mask_card_number(7000792289606361))  # '7000 79** **** 6361'`

### Маскирование счета
`print(get_mask_account(73654108430135874305))  # '**4305'`

## Фильтрация и сортировка операций

`from src.processing import filter_by_state, sort_by_date`

`data = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-11-01T12:00:00'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-11-02T13:00:00'}
]`

### Фильтрация по состоянию
`filtered = filter_by_state(data, state='EXECUTED')`
`print(filtered)  # [{'id': 1, 'state': 'EXECUTED', 'date': '2023-11-01T12:00:00'}]`

### Сортировка по дате
`sorted_data = sort_by_date(data)
print(sorted_data)
 [{'id': 2, 'state': 'CANCELED', 'date': '2023-11-02T13:00:00'},
 {'id': 1, 'state': 'EXECUTED', 'date': '2023-11-01T12:00:00'}]`

## Маскирование и преобразование данных

`from src.widget import mask_account_card, get_date`

### Маскирование карты/счета
`print(mask_account_card("Visa Platinum 7000792289606361"))  # 'Visa Platinum 7000 79** **** 6361'`
`print(mask_account_card("Счет 73654108430135874305"))       # 'Счет **4305'`

### Преобразование даты
`print(get_date("2024-03-11T02:26:18.671407"))  # '11.03.2024'`

### Декоратор `log`

`from src.decorators import log`

`@log(filename="mylog.txt")`
`def add(a, b):
    return a + b`

`add(1, 2)`

## Чтение данных из JSON

### Функция для чтения данных о транзакциях из JSON-файла:

`from src.utils import read_json_file`

`transactions = read_json_file("data/operations.json")
print(transactions)`

Если файл пустой, содержит некорректные данные или не найден, возвращается пустой список.

## Конвертация валюты

### Функция для конвертации суммы транзакции в рубли:

`from src.external_api import convert_to_rub`

`transaction = {"currency": "USD", "amount": 100.0}
amount_in_rub = convert_to_rub(transaction)
print(f"Сумма в рублях: {amount_in_rub}")`



