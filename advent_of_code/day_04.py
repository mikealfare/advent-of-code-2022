from typing import List

from advent_of_code import static_files


class Section:

    def __init__(self, raw_section: str):
        lower_bound, upper_bound = raw_section.split("-")
        self.start = int(lower_bound)
        self.end = int(upper_bound)

    def __contains__(self, other) -> bool:
        return all([
            self.start <= other.start,
            self.end >= other.end
        ])

    def __gt__(self, other) -> bool:
        return all([
            self.start < other.start,
            other.start <= self.end,
            self.end < other.end,
        ])


class SectionPair:

    def __init__(self, raw_section_pair: str):
        section_1, section_2 = raw_section_pair.split(",")
        self.section_1 = Section(section_1)
        self.section_2 = Section(section_2)

    @property
    def is_full_overlap(self):
        return any([
            self.section_1 in self.section_2,
            self.section_2 in self.section_1
        ])

    @property
    def is_partial_overlap(self):
        return any([
            self.section_1 > self.section_2,
            self.section_2 > self.section_1
        ])


def get_full_overlaps(section_pairs: List[SectionPair]) -> int:
    return len([
        section_pair
        for section_pair in section_pairs
        if section_pair.is_full_overlap
    ])


def get_partial_overlaps(section_pairs: List[SectionPair]) -> int:
    return len([
        section_pair
        for section_pair in section_pairs
        if section_pair.is_partial_overlap or section_pair.is_full_overlap
    ])


def parse_raw_section_pairs(section_pairs: List[str]) -> List[SectionPair]:
    return [SectionPair(pair) for pair in section_pairs]


if __name__ == "__main__":
    my_section_pairs = parse_raw_section_pairs(static_files.get("day_04.txt"))
    print(f"Number of full section overlaps: {get_full_overlaps(my_section_pairs)}")
    print(f"Number of partial section overlaps: {get_partial_overlaps(my_section_pairs)}")
