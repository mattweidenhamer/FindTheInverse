import pytest
from library.src.inverse_finder.FindInverse import find_inverse


testSets = [
    (101, 4620, 1601),
    (3, 7, -2),
    (5, 10, None),
    (7, 26, -11),
    (13, 2436, 937),
]


@pytest.mark.parametrize("num1, num2, expected", testSets)
def test_find_inverse(num1, num2, expected):
    assert find_inverse(num1, num2) == expected
