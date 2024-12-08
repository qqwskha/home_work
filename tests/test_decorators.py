import pytest
from src.decorators import log
from typing import Optional


@log()
def test_func_success(a: int, b: int) -> int:
    return a + b


@log(filename="test_log.txt")
def test_func_error(a: int, b: int) -> int:
    return a / b


def test_success_logging(capsys):
    result = test_func_success(1, 2)
    assert result == 3

    captured = capsys.readouterr()
    assert "Function 'test_func_success' started" in captured.out
    assert "Function 'test_func_success' finished successfully with result=3" in captured.out


def test_error_logging():
    with pytest.raises(ZeroDivisionError):
        test_func_error(1, 0)

    with open("test_log.txt", "r") as file:
        logs = file.read()
    assert "Function 'test_func_error' started with args=(1, 0)" in logs
    assert "Function 'test_func_error' raised ZeroDivisionError" in logs
