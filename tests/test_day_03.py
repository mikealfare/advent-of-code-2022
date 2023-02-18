import pytest

from advent_of_code import day_03


@pytest.mark.parametrize("rucksack,expected", [
    ("vJrwpWtwJgWrhcsFMMfFFhFp", "p"),
    ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "L"),
    ("PmmdzqPrVvPwwTWBwg", "P"),
    ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "v"),
    ("ttgJtRGJQctTZtZT", "t"),
    ("CrZsJsPPZsGzwwsLwLmpwMDw", "s"),
])
def test_find_error(rucksack, expected):
    assert day_03.find_error(rucksack) == expected


@pytest.mark.parametrize("rucksack,expected", [
    ("vJrwpWtwJgWrhcsFMMfFFhFp", 16),
    ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", 38),
    ("PmmdzqPrVvPwwTWBwg", 42),
    ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", 22),
    ("ttgJtRGJQctTZtZT", 20),
    ("CrZsJsPPZsGzwwsLwLmpwMDw", 19),
])
def test_get_error_priority(rucksack, expected):
    assert day_03.get_error_priority(rucksack) == expected


@pytest.mark.parametrize("badge_group,expected", [
    ((
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
    ), "r"),
    ((
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ), "Z"),
])
def test_find_badge(badge_group, expected):
    assert day_03.find_badge(badge_group) == expected


@pytest.mark.parametrize("rucksacks,expected", [
    ([
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ], 70)
])
def test_total_badge_priority(rucksacks, expected):
    assert day_03.total_badge_priority(rucksacks) == expected
