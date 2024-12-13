import json
import logging
from typing import Dict, List

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Логирование в файл
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_file(file_path: str) -> List[Dict]:
    """
    Читает JSON-файл и возвращает список словарей с данными.

    :param file_path: Путь до JSON-файла.
    :return: Список словарей или пустой список, если файл пуст, содержит не список или не найден.
    """
    try:
        logger.debug(f"Attempting to read JSON file: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Successfully read JSON file: {file_path}")
                return data
            logger.error(f"Invalid JSON format in file: {file_path}")
            return []
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"JSON decode error in file: {file_path}")
        return []
