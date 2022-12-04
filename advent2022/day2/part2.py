import functools
import pathlib
import typing

from advent2022 import compute
from advent2022.day2.part1 import ROCK, PAPER, SCISSORS, parse_choice, process


LOOSE = "X"
DRAW = "Y"
WIN = "Z"

win_move = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK
}

loose_move = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER
}

def compute_move(opponent_move, expected_outcome):
    if expected_outcome == WIN:
        return win_move.get(opponent_move)
    elif expected_outcome == DRAW:
        return opponent_move
    else:
        return loose_move.get(opponent_move)

def parse(lines: typing.Iterator[str]) -> typing.Iterator[dict[str, str]]:
    for line in lines:
        if len(line) < 3:
            continue

        opponent_move = parse_choice(line[0])
        expected_outcome = line[2]
        move = {
            "opponent": opponent_move,
            "me": compute_move(opponent_move, expected_outcome),
        }

        yield move

compute_part2 = functools.partial(compute, parse=parse, process=process)

def main():
    inputpath = pathlib.Path(__file__).parent\
        .joinpath("data", "input").absolute()
    result = compute_part2(inputpath)

    print("Result", result)


if __name__ == "__main__":
    main()
