from typing import Dict, List, Tuple

from advent_of_code import static_files


Crate = str
Stack = List[Crate]
Stacks = Dict[int, Stack]


Move = Tuple[int, int, int]


def top_boxes_after_moves(stacks: Stacks, moves: List[Move]) -> str:
    for move in moves:
        stacks = update_stacks(stacks, move)
    return "".join([stack[-1] if len(stack) > 0 else " " for stack in stacks.values()])


def update_stacks(stacks: Stacks, move: Move) -> Stacks:
    number_of_crates, from_stack, to_stack = move
    stacks[from_stack], crates_to_move = stacks[from_stack][:-number_of_crates], stacks[from_stack][-number_of_crates:]
    stacks[to_stack].extend(crates_to_move[::-1])
    return stacks


def parse_input_file(lines: List[str]) -> Tuple[Stacks, List[Move]]:
    null_index = lines.index("")
    stacks, moves = get_stacks(lines[:null_index]), get_moves(lines[null_index + 1:])
    return stacks, moves


def get_stacks(raw_stacks: List[str]) -> Stacks:
    number_of_stacks = int(raw_stacks[-1].split(" ")[-1])
    stacks = {stack + 1: [] for stack in range(number_of_stacks)}
    for tier in raw_stacks[:-1:-1]:
        crates = tier[1::4]
        for stack in range(number_of_stacks):
            if crates[stack] != " ":
                stacks[stack + 1].append(crates[stack])
    return stacks


def get_moves(raw_moves: List[str]) -> List[Move]:
    moves = []
    for move in raw_moves:
        _, crates, _, from_stack, _, to_stack = move.split(" ")
        moves.append((int(crates), int(from_stack), int(to_stack)))
    return moves


if __name__ == "__main__":
    my_stacks, my_moves = parse_input_file(static_files.get("day_05.txt"))
    print(f"The top boxes are: '{top_boxes_after_moves(my_stacks, my_moves)}'")
