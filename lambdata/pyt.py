import pytest
import pandas

def func(x):
    return x + 0


def test_answer():
    assert func(5) == 5