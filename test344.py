import pytest

@pytest.fixture
def bank1():
    numbers = ('hodi',2,2,2)
    return numbers

def test_1(numbers):
    assert numbers[0]==10
def test_2(numbers):
    assert numbers[1] == 10
def test_3(numbers):
    assert numbers[3] == 'avi'










