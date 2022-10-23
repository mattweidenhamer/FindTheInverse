import pytest
from FindInverse import find_inverse



testSets = [
    (101, 4260, 1601),
    (3, 7, 1),
]

@pytest.parametrize("number", "mod", "result", testSets)
def test_find_inverse(number, mod, result):
    assert find_inverse(number, mod) == result