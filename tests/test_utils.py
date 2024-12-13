from pathlib import Path

import pytest

from src.utils import read_json_file


def test_read_json_file_existing_file(tmp_path: Path) -> None:
    test_file = tmp_path / "test.json"
    test_file.write_text('[{"id": 1, "amount": 100}]')

    result = read_json_file(str(test_file))
    assert result == [{"id": 1, "amount": 100}]


def test_read_json_file_non_existing_file() -> None:
    result = read_json_file("non_existing.json")
    assert result == []


def test_read_json_file_invalid_json(tmp_path: Path) -> None:
    test_file = tmp_path / "invalid.json"
    test_file.write_text('{"invalid": "json"}')

    result = read_json_file(str(test_file))
    assert result == []
