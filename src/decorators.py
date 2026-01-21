import functools
import time
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Декоратор для логирования"""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                log_info = (
                    f"{func.__name__} ok\nВремя начала функции: {start_time}\n"
                    f"Результат: {result}\nВремя завершения функции: {end_time}\n"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_info)
                else:
                    print(log_info)
                if result:
                    return result
            except Exception as some_ex:
                log_info = f"{func.__name__} error: {type(some_ex).__name__}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_info)
                else:
                    print(log_info)

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int|float, y: int|float) -> int|float:
    return x + y


my_function(1, 2)


@log(filename="mylog.txt")
def divide(x: int|float, y: int|float) -> int|float:
    return x / y


divide(10, 0)
