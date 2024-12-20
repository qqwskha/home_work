import pandas as pd
from typing import List, Dict


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла и возвращает список словарей.

    :param file_path: Путь к CSV-файлу.
    :return: Список транзакций в виде словарей.
    """
    try:
        data = pd.read_csv(file_path)
        transactions = data.to_dict(orient="records")
        return transactions
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    except pd.errors.EmptyDataError:
        raise ValueError(f"CSV file is empty or invalid: {file_path}")


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла и возвращает список словарей.

    :param file_path: Путь к Excel-файлу.
    :return: Список транзакций в виде словарей.
    """
    try:
        data = pd.read_excel(file_path)
        transactions = data.to_dict(orient="records")
        return transactions
    except FileNotFoundError:
        raise FileNotFoundError(f"Excel file not found: {file_path}")
    except ValueError:
        raise ValueError(f"Excel file is empty or invalid: {file_path}")
