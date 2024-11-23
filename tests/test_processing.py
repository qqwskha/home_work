import pytest
from typing import List, Dict
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def transaction_data() -> List[Dict]:
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-11-01T12:00:00'},
        {'id': 2, 'state': 'CANCELED', 'date': '2023-11-02T13:00:00'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-11-01T15:00:00'},
    ]


def test_filter_by_state(transaction_data: List[Dict]) -> None:
    result = filter_by_state(transaction_data, 'EXECUTED')
    assert len(result) == 2
    assert all(item['state'] == 'EXECUTED' for item in result)


def test_filter_by_state_empty(transaction_data: List[Dict]) -> None:
    result = filter_by_state(transaction_data, 'PENDING')
    assert len(result) == 0


@pytest.mark.parametrize("descending,expected_ids", [
    (True, [2, 3, 1]),
    (False, [1, 3, 2]),
])
def test_sort_by_date(transaction_data: List[Dict], descending: bool, expected_ids: List[int]) -> None:
    result = sort_by_date(transaction_data, descending)
    assert [item['id'] for item in result] == expected_ids


def test_sort_by_date_invalid(transaction_data: List[Dict]) -> None:
    transaction_data[0]['date'] = "Некорректная дата"
    with pytest.raises(ValueError):
        sort_by_date(transaction_data)
