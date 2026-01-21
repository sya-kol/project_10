from src.decorators import log

from typing import Any


def test_log_in_console(capsys: Any) -> None:
    @log()
    def add_numbers(a: int|float, b: int|float) -> int|float:
        return a + b

    result = add_numbers(2, 3)
    assert result == 5
    capture = capsys.readouterr()
    assert "add_numbers ok" in capture.out
    assert "Результат: 5" in capture.out


def test_log_exception(capsys: Any) -> None:
    @log()
    def divide(x: int|float, y: int|float) -> int|float:
        return x / y

    divide(10, 0)
    capture = capsys.readouterr()
    assert "divide" in capture.out
    assert "ZeroDivisionError" in capture.out
