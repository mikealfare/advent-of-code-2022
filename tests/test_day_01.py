import pytest

from advent_of_code import day_01


LEDGER = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".strip().split("\n")


def test_parse_ledger():
    assert day_01.parse_ledger(LEDGER) == [6000, 4000, 11000, 24000, 10000]


@pytest.mark.parametrize("number_of_elves,expected", [
    (1, 24000),
    (3, 45000),
    (None, 24000),
])
def test_max_calories(number_of_elves, expected):
    assert day_01.max_calories(LEDGER, number_of_elves) == expected
