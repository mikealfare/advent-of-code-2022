import pytest

from advent_of_code import day_04


SECTION_PAIRS = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip().split("\n")


@pytest.mark.parametrize("section_pair,expected", [
    ("2-4,6-8", False),
    ("5-7,7-9", False),
    ("6-6,4-6", True),
    ("2-8,3-7", True)
])
def test_is_overlap(section_pair, expected):
    assert day_04.SectionPair(section_pair).is_full_overlap == expected


def test_get_full_overlaps():
    section_pairs = day_04.parse_raw_section_pairs(SECTION_PAIRS)
    assert day_04.get_full_overlaps(section_pairs) == 2


def test_get_partial_overlaps():
    section_pairs = day_04.parse_raw_section_pairs(SECTION_PAIRS)
    assert day_04.get_partial_overlaps(section_pairs) == 4
