import logging
from functools import wraps
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, логирующий выполнение функции.

    :param filename: str | None
        Имя файла для записи логов. Если не указано, логи выводятся в консоль.
    :return: Callable
        Декорированная функция.
    """
    logger = logging.getLogger("function_logger")
    logger.setLevel(logging.INFO)

    # Настройка обработчика
    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler()

    # Формат логов
    handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    logger.addHandler(handler)

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                logger.info(f"Function '{func.__name__}' started with args={args}, kwargs={kwargs}")
                result = func(*args, **kwargs)
                logger.info(f"Function '{func.__name__}' finished successfully with result={result}")
                return result
            except Exception as e:
                logger.error(f"Function '{func.__name__}' raised {type(e).__name__} with args={args}, kwargs={kwargs}")
                raise

        return wrapper

    return decorator
