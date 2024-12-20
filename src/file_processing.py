from typing import Any, Dict, Hashable, List

import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict[Hashable, Any]]:
    """
    Считывает финансовые операции из CSV-файла и возвращает список словарей.
    """
    try:
        data: pd.DataFrame = pd.read_csv(file_path)
        transactions: List[Dict[Hashable, Any]] = data.to_dict(orient="records")
        return transactions
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    except pd.errors.EmptyDataError:
        raise ValueError(f"CSV file is empty or invalid: {file_path}")


def read_transactions_from_excel(file_path: str) -> List[Dict[Hashable, Any]]:
    """
    Считывает финансовые операции из Excel-файла и возвращает список словарей.
    """
    try:
        data: pd.DataFrame = pd.read_excel(file_path)
        transactions: List[Dict[Hashable, Any]] = data.to_dict(orient="records")
        return transactions
    except FileNotFoundError:
        raise FileNotFoundError(f"Excel file not found: {file_path}")
    except ValueError:
        raise ValueError(f"Excel file is empty or invalid: {file_path}")
