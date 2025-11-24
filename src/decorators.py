import functools
import time


def log(filename=None):
    """Декоратор для логирования"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                log_info = f"{func.__name__} ok\nВремя начала функции: {start_time}\nРезультат: {result}\nВремя завершения функции: {end_time}"
                if filename:
                    with open(filename, 'a', encoding="utf-8") as file:
                        file.write(log_info)
                else:
                    print(log_info)
                if result:
                    return result
            except Exception as some_ex:
                log_info = f"{func.__name__}\nВремя начала функции: {start_time}\nРезультат: Работа преждевременно завершена с ошибкой: {type(some_ex).__name__}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_info)
                else:
                    print(log_info)
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
# Ожидаемый вывод в лог-файл
# mylog.txt
#  при успешном выполнении:
# my_function ok
# Ожидаемый вывод при ошибке:
# my_function error: тип ошибки. Inputs: (1, 2), {}
# Где
# тип ошибки
#  заменяется на текст ошибки.


