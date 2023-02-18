from typing import Tuple, List

from advent_of_code import static_files


RawRound = Tuple[str, str]
Play = int
Outcome = int
Score = int
Round = Tuple[Play, Outcome]


ROCK = 1
PAPER = 2
SCISSORS = 3


WIN = 6
LOSE = 0
DRAW = 3


SHAPE_MAP = {
"A": ROCK,
"B": PAPER,
"C": SCISSORS,
}


OUTCOME_MAP = {
"X": LOSE,
"Y": DRAW,
"Z": WIN,
}


def total_score(raw_rounds: List[RawRound]) -> int:
    return sum([round_score(round) for round in raw_rounds])


def round_score(raw_round: RawRound) -> Score:
    round = parse_round(raw_round)
    opponent, _ = round
    player = your_shape(round)
    return shape_score(player) + outcome_score(opponent, player)


def parse_round(round: RawRound) -> Round:
    opponent, outcome = round
    return SHAPE_MAP[opponent], OUTCOME_MAP[outcome]


def your_shape(round: Round) -> Play:
    opponent, outcome = round
    plays = {
        (ROCK, LOSE): SCISSORS,
        (ROCK, DRAW): ROCK,
        (ROCK, WIN): PAPER,
        (PAPER, LOSE): ROCK,
        (PAPER, DRAW): PAPER,
        (PAPER, WIN): SCISSORS,
        (SCISSORS, LOSE): PAPER,
        (SCISSORS, DRAW): SCISSORS,
        (SCISSORS, WIN): ROCK,
    }
    return plays[(opponent, outcome)]


def shape_score(play: Play) -> Score:
    scores = {
        ROCK: 1,
        PAPER: 2,
        SCISSORS: 3,
    }
    return scores[play]


def outcome_score(opponent: Play, player: Play) -> Score:
    scores = {
        (ROCK, ROCK): DRAW,
        (ROCK, PAPER): WIN,
        (ROCK, SCISSORS): LOSE,
        (PAPER, ROCK): LOSE,
        (PAPER, PAPER): DRAW,
        (PAPER, SCISSORS): WIN,
        (SCISSORS, ROCK): WIN,
        (SCISSORS, PAPER): LOSE,
        (SCISSORS, SCISSORS): DRAW,
    }
    return scores[(opponent, player)]


if __name__ == "__main__":
    game = [tuple(play.split(" ")) for play in static_files.get("day_02.txt")]
    print(f"Total score: {total_score(game)}")
