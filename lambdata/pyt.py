import pytest
import pandas

def func(x):
    return x + 0


def test_answer():
    assert func(5) == 5

def increment_ten(x):
     return x + 10

def test_increment_ten_int():
    """Testing increment_ten on integers"""
    x0 = 0
    y0 = increment_ten(x0)
    assert y0 == 10