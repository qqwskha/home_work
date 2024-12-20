from src.file_processing import read_transactions_from_csv, read_transactions_from_excel
from src.filters import count_transaction_categories, filter_transactions_by_description
from src.processing import filter_by_state, sort_by_date
from src.utils import read_json_file


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ").strip()

    transactions = []
    if choice == "1":
        file_path = input("Введите путь к JSON-файлу: ")
        transactions = read_json_file(file_path)
    elif choice == "2":
        file_path = input("Введите путь к CSV-файлу: ")
        transactions = read_transactions_from_csv(file_path)
    elif choice == "3":
        file_path = input("Введите путь к XLSX-файлу: ")
        transactions = read_transactions_from_excel(file_path)
    else:
        print("Некорректный выбор.")
        return

    if not transactions:
        print("Файл пуст или транзакции отсутствуют.")
        return

    available_statuses = {"executed", "canceled", "pending"}
    while True:
        status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").strip().lower()
        if status in available_statuses:
            break
        print(f"Статус \"{status}\" недоступен.")

    filtered_transactions = filter_by_state(transactions, status.upper())

    if input("Отсортировать операции по дате? (Да/Нет): ").strip().lower() == "да":
        order = input("Отсортировать по возрастанию или убыванию? ").strip().lower()
        filtered_transactions = sort_by_date(filtered_transactions, descending=(order == "по убыванию"))

    if input("Выводить только рублевые транзакции? (Да/Нет): ").strip().lower() == "да":
        filtered_transactions = [t for t in filtered_transactions
                                 if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"]

    if input("Отфильтровать список транзакций по строке в описании? (Да/Нет): ").strip().lower() == "да":
        search = input("Введите строку для поиска в описании: ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search)

    if not filtered_transactions:
        print("Не найдено ни одной транзакции.")
        return

    category_counts = count_transaction_categories(filtered_transactions)

    print("\nРаспечатываю транзакции:")
    for transaction in filtered_transactions:
        print(transaction)

    print("\nКатегории транзакций:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")

    print(f"\nВсего транзакций: {len(filtered_transactions)}")
