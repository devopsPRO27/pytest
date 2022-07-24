import math
import pytest

def func1(x):
    return x*2

def hodisqrt(x):
    return math.sqrt(x)


def first_char(st):
    return st[0]




@pytest.mark.first
def test_first_char():
    expected='m' # from sql
    input1="moooo"
    actual=first_char(input1)

    assert actual == expected

@pytest.mark.skip
def test_hodisqrt():
    assert hodisqrt(4) == 2

@pytest.mark.first
def test_func1():
    assert func1(12) == 20

