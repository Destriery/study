# pytest algorithms/test_lc.py -sv
from .leetcode import get_valid_sum


def test__get_valid_sum():
    assert get_valid_sum([50, 57, 53, 56, 58, 51, 81], 163, 3) == 163
    assert get_valid_sum([], 163, 3) == None
    assert get_valid_sum([3, 4, 5, 5, 5], 10, 2) == 10
    assert get_valid_sum([50], 10, 2) == None
