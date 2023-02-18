import pytest

from advent_of_code import day_02


@pytest.mark.parametrize("play,expected", [
    (("A", "Y"), 4),
    (("B", "X"), 1),
    (("C", "Z"), 7),
])
def test_round_score(play, expected):
    assert day_02.round_score(play) == expected
