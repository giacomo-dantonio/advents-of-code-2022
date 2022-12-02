import typing
import re

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

def parse_choice(choice: chr) -> str:
    if choice in ["A", "X"]:
        return ROCK
    if choice in ["B", "Y"]:
        return PAPER
    if choice in ["C", "Z"]:
        return SCISSORS

def parse(lines: typing.Iterator[str]) -> typing.Iterator[dict[str, str]]:
    for line in lines:
        if len(line) < 3:
            continue

        move = {
            "opponent": parse_choice(line[0]),
            "me": parse_choice(line[2]),
        }

        yield move

def wins(lhs, rhs):
    return (lhs == ROCK and rhs == SCISSORS)\
        or (lhs == SCISSORS and rhs == PAPER)\
        or (lhs == PAPER and rhs == ROCK)

def round_score(move: dict[str, str]) -> int:
    choice_score = 1 if move["me"] == ROCK else \
        2 if move["me"] == PAPER else \
        3

    outcome_score = 6 if wins(move["me"], move["opponent"]) else \
        3 if not wins(move["opponent"], move["me"])\
        else 0

    return choice_score + outcome_score


def main():
    with open("input") as f:
        lines = (line.rstrip("\r\n") for line in f)

        total_score = 0
        for move in parse(lines):
            total_score += round_score(move)

    print("Total score", total_score)


if __name__ == "__main__":
    main()
