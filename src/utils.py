import json
from typing import Dict, List


def read_json_file(file_path: str) -> List[Dict]:
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь до JSON-файла.
    :return: Список словарей или пустой список, если файл пуст, содержит не список или не найден.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
