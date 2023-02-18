from typing import List

from advent_of_code import static_files


def max_calories(ledger: List[str], number_of_elves: int = None):
    elves = parse_ledger(ledger)
    calories = sorted(elves, reverse=True)
    number_of_elves = number_of_elves or 1
    return sum(calories[:number_of_elves])


def parse_ledger(ledger: List[str]) -> List[int]:
    elves = [0]
    for entry in ledger:
        if len(entry) == 0:
            elves.append(0)
        else:
            elves[-1] += int(entry)
    return elves


if __name__ == "__main__":
    ledger = static_files.get("day_01.txt")
    print(f"The top elf has :{max_calories(ledger)}")
    print(f"The top three elves have :{max_calories(ledger, 3)}")
