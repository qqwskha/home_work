from pathlib import Path
from unittest.mock import MagicMock, patch

from src.utils import read_json_file


def test_read_json_file_existing_file(tmp_path: Path) -> None:
    """Тест успешного чтения JSON-файла."""
    test_file = tmp_path / "test.json"
    test_file.write_text('[{"id": 1, "name": "test"}]')

    result = read_json_file(str(test_file))
    assert result == [{"id": 1, "name": "test"}]


def test_read_json_file_empty_file(tmp_path: Path) -> None:
    """Тест чтения пустого JSON-файла."""
    test_file = tmp_path / "empty.json"
    test_file.write_text("")

    result = read_json_file(str(test_file))
    assert result == []


def test_read_json_file_invalid_format(tmp_path: Path) -> None:
    """Тест чтения JSON-файла с некорректным содержимым."""
    test_file = tmp_path / "invalid.json"
    test_file.write_text('{"invalid": "json"}')  # Некорректный формат, должен быть список

    result = read_json_file(str(test_file))
    assert result == []


def test_read_json_file_non_existing_file() -> None:
    """Тест обработки отсутствующего JSON-файла."""
    result = read_json_file("non_existing.json")
    assert result == []


@patch("src.utils.logger")
def test_read_json_file_logging_success(mock_logger: MagicMock, tmp_path: Path) -> None:
    """Тест логгирования успешного чтения JSON-файла."""
    test_file = tmp_path / "test.json"
    test_file.write_text('[{"id": 1, "name": "test"}]')

    read_json_file(str(test_file))
    mock_logger.debug.assert_called_with(f"Attempting to read JSON file: {test_file}")
    mock_logger.info.assert_called_with(f"Successfully read JSON file: {test_file}")


@patch("src.utils.logger")
def test_read_json_file_logging_file_not_found(mock_logger: MagicMock) -> None:
    """Тест логгирования отсутствующего JSON-файла."""
    read_json_file("non_existing.json")
    mock_logger.error.assert_called_with("File not found: non_existing.json")


@patch("src.utils.logger")
def test_read_json_file_logging_invalid_format(mock_logger: MagicMock, tmp_path: Path) -> None:
    """Тест логгирования некорректного формата JSON."""
    test_file = tmp_path / "invalid.json"
    test_file.write_text('{"invalid": "json"}')

    read_json_file(str(test_file))
    mock_logger.error.assert_called_with(f"Invalid JSON format in file: {test_file}")


@patch("src.utils.logger")
def test_read_json_file_logging_json_decode_error(mock_logger: MagicMock, tmp_path: Path) -> None:
    """Тест логгирования ошибки JSONDecodeError."""
    test_file = tmp_path / "decode_error.json"
    test_file.write_text('{"invalid": ')  # Некорректный JSON

    read_json_file(str(test_file))
    mock_logger.error.assert_called_with(f"JSON decode error in file: {test_file}")
