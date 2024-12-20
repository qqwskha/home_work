from src.filters import count_transaction_categories, filter_transactions_by_description


def test_filter_transactions_by_description() -> None:
    transactions = [
        {"description": "Открытие вклада"},
        {"description": "Перевод организации"},
        {"description": "Открытие счета"}
    ]
    result = filter_transactions_by_description(transactions, "открытие")
    assert len(result) == 2
    assert all("открытие" in t["description"].lower() for t in result)


def test_count_transaction_categories() -> None:
    transactions = [
        {"description": "Открытие вклада"},
        {"description": "Открытие вклада"},
        {"description": "Перевод организации"}
    ]
    result = count_transaction_categories(transactions)
    assert result == {
        "Открытие вклада": 2,
        "Перевод организации": 1
    }
