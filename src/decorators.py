import logging
import sys
from functools import wraps
from typing import Any, Callable, Optional, Union


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, логирующий выполнение функции.

    :param filename: Optional[str]
        Имя файла для записи логов. Если не указано, логи выводятся в консоль.
    :return: Callable
        Декорированная функция.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            # Удаление старых обработчиков
            if logger.hasHandlers():
                logger.handlers.clear()

            # Логирование в файл или консоль
            handler: Union[logging.FileHandler, logging.StreamHandler]
            if filename:
                handler = logging.FileHandler(filename)
            else:
                handler = logging.StreamHandler(sys.stdout)

            formatter = logging.Formatter('%(asctime)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            try:
                logger.info(f"Function '{func.__name__}' started with args={args}, kwargs={kwargs}")
                result = func(*args, **kwargs)
                logger.info(f"Function '{func.__name__}' finished successfully with result={result}")
                return result
            except Exception as e:
                logger.error(f"Function '{func.__name__}' raised {type(e).__name__} with args={args}, kwargs={kwargs}")
                raise
            finally:
                logger.removeHandler(handler)  # Удаление обработчика

        return wrapper

    return decorator
