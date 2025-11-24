from src.decorators import log


def test_log_in_console(capsys):
    @log()
    def add_numbers(a, b):
        return a + b

    result = add_numbers(2, 3)
    assert result == 5
    capture = capsys.readouterr()
    assert "add_numbers ok" in capture.out
    assert "Результат: 5" in capture.out


def test_log_exception(capsys):
    @log()
    def divide(x, y):
        return x / y

    divide(10, 0)
    capture = capsys.readouterr()
    assert "divide" in capture.out
    assert "ZeroDivisionError" in capture.out
