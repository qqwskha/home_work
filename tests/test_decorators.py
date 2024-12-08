import pytest
from src.decorators import log
import os


# Функции для тестирования
@log()
def func_success(a: int, b: int) -> int:
    return a + b


@log(filename="test_log.txt")
def func_error(a: int, b: int) -> int:
    return a / b


# Тесты
def test_success_logging(capsys):
    """Тест успешного выполнения функции и логирования в консоль."""
    result = func_success(1, 2)
    assert result == 3

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "Function 'func_success' started" in captured.out
    assert "Function 'func_success' finished successfully with result=3" in captured.out


def test_error_logging():
    """Тест обработки исключений и логирования в файл."""
    log_file = "test_log.txt"

    # Удаляем файл, если он существует
    if os.path.exists(log_file):
        os.remove(log_file)

    # Проверка логирования ошибки
    with pytest.raises(ZeroDivisionError):
        func_error(1, 0)

    # Убедимся, что файл логов создан
    assert os.path.exists(log_file), "Log file was not created"

    # Проверяем содержимое файла
    with open(log_file, "r") as file:
        logs = file.read()
    assert "Function 'func_error' started with args=(1, 0)" in logs
    assert "Function 'func_error' raised ZeroDivisionError" in logs

    # Удаляем файл после теста
    os.remove(log_file)
