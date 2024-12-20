from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src.file_processing import read_transactions_from_csv, read_transactions_from_excel


@patch("pandas.read_csv")
def test_read_transactions_from_csv_success(mock_read_csv: MagicMock) -> None:
    """Тест успешного чтения CSV-файла."""
    mock_read_csv.return_value = pd.DataFrame([
        {"id": 1, "amount": 100.0, "currency": "USD"},
        {"id": 2, "amount": 200.0, "currency": "EUR"}
    ])
    result = read_transactions_from_csv("transactions.csv")
    expected = [
        {"id": 1, "amount": 100.0, "currency": "USD"},
        {"id": 2, "amount": 200.0, "currency": "EUR"}
    ]
    assert result == expected


@patch("pandas.read_csv")
def test_read_transactions_from_csv_file_not_found(mock_read_csv: MagicMock) -> None:
    """Тест ошибки, если файл CSV не найден."""
    mock_read_csv.side_effect = FileNotFoundError("CSV file not found")
    with pytest.raises(FileNotFoundError):
        read_transactions_from_csv("missing.csv")


@patch("pandas.read_csv")
def test_read_transactions_from_csv_empty_file(mock_read_csv: MagicMock) -> None:
    """Тест ошибки при пустом CSV-файле."""
    mock_read_csv.side_effect = pd.errors.EmptyDataError("CSV file is empty")
    with pytest.raises(ValueError):
        read_transactions_from_csv("empty.csv")


@patch("pandas.read_excel")
def test_read_transactions_from_excel_success(mock_read_excel: MagicMock) -> None:
    """Тест успешного чтения Excel-файла."""
    mock_read_excel.return_value = pd.DataFrame([
        {"id": 1, "amount": 100.0, "currency": "USD"},
        {"id": 2, "amount": 200.0, "currency": "EUR"}
    ])
    result = read_transactions_from_excel("transactions_excel.xlsx")
    expected = [
        {"id": 1, "amount": 100.0, "currency": "USD"},
        {"id": 2, "amount": 200.0, "currency": "EUR"}
    ]
    assert result == expected


@patch("pandas.read_excel")
def test_read_transactions_from_excel_file_not_found(mock_read_excel: MagicMock) -> None:
    """Тест ошибки, если файл Excel не найден."""
    mock_read_excel.side_effect = FileNotFoundError("Excel file not found")
    with pytest.raises(FileNotFoundError):
        read_transactions_from_excel("missing.xlsx")


@patch("pandas.read_excel")
def test_read_transactions_from_excel_empty_file(mock_read_excel: MagicMock) -> None:
    """Тест ошибки при пустом Excel-файле."""
    mock_read_excel.side_effect = ValueError("Excel file is empty")
    with pytest.raises(ValueError):
        read_transactions_from_excel("empty.xlsx")
