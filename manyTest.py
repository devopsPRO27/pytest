import math

import pytest


# @pytest.mark.parametrize("x",[(14),(5 ),(8)])
# def test_t1(x):
#     assert math.sqrt(x) > 10

def nums(x, y):
    return x % y == 0


@pytest.mark.parametrize('x,y',
                         [(5, 2), (5, 2), (5, 2), (5, 2), (5, 3), (4, 2), (10, 5), (12, 6), (8, 1), (10855, 5432),
                          (12, 4)])
def test_nums(x, y):
    expected=nums(x, y)
    assert expected == True
