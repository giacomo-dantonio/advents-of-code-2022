import typing
from part1 import ROCK, PAPER, SCISSORS, parse_choice, round_score

LOOSE = "X"
DRAW = "Y"
WIN = "Z"

def win_move(opponent_move):
    if opponent_move == ROCK:
        return PAPER
    elif opponent_move == PAPER:
        return SCISSORS
    else:
        return ROCK

def loose_move(opponent_move):
    if opponent_move == ROCK:
        return SCISSORS
    elif opponent_move == PAPER:
        return ROCK
    else:
        return PAPER

def draw_move(opponent_move):
    return opponent_move

def compute_move(opponent_move, expected_outcome):
    if expected_outcome == WIN:
        return win_move(opponent_move)
    elif expected_outcome == DRAW:
        return draw_move(opponent_move)
    else:
        return loose_move(opponent_move)

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

def main():
    with open("input") as f:
        lines = (line.rstrip("\r\n") for line in f)

        total_score = 0
        for move in parse(lines):
            total_score += round_score(move)

    print("Total score", total_score)


if __name__ == "__main__":
    main()
