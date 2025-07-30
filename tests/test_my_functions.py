import pytest
from src import my_functions
import time


def test_add():
    result = my_functions.add(1, 2)
    assert result == 3

@pytest.mark.skip(reason="observing, how skipping tests work")
def test_add_skipping_function():
    result = my_functions.add(1, 2)
    assert result == 3

def test_add_strings():
    result = my_functions.add("I Like ", "Tea")
    assert result == "I Like Tea"


def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    """
    It says expect 'ZeroDivisionError' (as we are dividing by 0), 
    and when it raises that err, output is what is expected, so test passes
    """
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(num1=100, num2=25)
    assert result == 4


@pytest.mark.xfail(reason="We cannot dovide by zero")
def test_divide_by_zero_broken():
    my_functions.divide(num1=10, num2=0)
