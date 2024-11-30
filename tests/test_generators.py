import pytest
from typing import List, Dict
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def transactions() -> List[Dict]:
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод с карты на карту",
        },
    ]


def test_filter_by_currency(transactions: List[Dict]) -> None:
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)


def test_filter_by_currency_empty(transactions: List[Dict]) -> None:
    result = list(filter_by_currency(transactions, "EUR"))
    assert len(result) == 0


def test_transaction_descriptions(transactions: List[Dict]) -> None:
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"


def test_transaction_descriptions_empty() -> None:
    descriptions = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(descriptions)


@pytest.mark.parametrize("start, stop, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
])
def test_card_number_generator(start: int, stop: int, expected: List[str]) -> None:
    assert list(card_number_generator(start, stop)) == expected


def test_card_number_generator_format() -> None:
    result = list(card_number_generator(1, 5))
    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
