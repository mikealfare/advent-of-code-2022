from typing import List, Tuple
from string import ascii_letters

from advent_of_code import static_files


Rucksack = str
BadgeGroup = Tuple[Rucksack, Rucksack, Rucksack]


def total_error_priority(rucksacks: List[Rucksack]) -> int:
    return sum(get_error_priority(rucksack) for rucksack in rucksacks)


def total_badge_priority(rucksacks: List[Rucksack]) -> int:
    badge_groups = get_badge_groups(rucksacks)
    return sum(get_badge_priority(badge_group) for badge_group in badge_groups)


def get_error_priority(rucksack: Rucksack) -> int:
    error = find_error(rucksack)
    return priority(error)


def find_error(rucksack: Rucksack) -> str:
    size = len(rucksack)//2
    compartment_one = rucksack[:size]
    compartment_two = rucksack[size:]
    return set(compartment_one).intersection(set(compartment_two)).pop()


def get_badge_groups(rucksacks: List[Rucksack]) -> List[BadgeGroup]:
    badge_groups = []
    while rucksacks:
        badge_group, rucksacks = rucksacks[:3], rucksacks[3:]
        badge_groups.append(tuple(badge_group))
    return badge_groups


def get_badge_priority(badge_group: BadgeGroup) -> int:
    badge = find_badge(badge_group)
    return priority(badge)


def find_badge(badge_group: BadgeGroup) -> str:
    ruck_1, ruck_2, ruck_3 = badge_group
    return set(ruck_1).intersection(set(ruck_2)).intersection(set(ruck_3)).pop()


def priority(item_type: str) -> int:
    return ascii_letters.index(item_type) + 1


if __name__ == "__main__":
    my_rucksacks = static_files.get("day_03.txt")
    print(f"Total error priority: {total_error_priority(my_rucksacks)}")
    print(f"Total badge priority: {total_badge_priority(my_rucksacks)}")
