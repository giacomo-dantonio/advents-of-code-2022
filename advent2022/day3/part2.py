import itertools
import typing

from part1 import priority


def parse(lines: typing.Iterator[str]) -> typing.Iterator[chr]:
    while True:
        try:
            rs1, rs2, rs3 = itertools.islice(lines, 3)

            badges = set(rs1)\
                .intersection(rs2)\
                .intersection(rs3)

            assert len(badges) == 1
            badge = badges.pop()

            yield badge
        except ValueError:
            break

def main():
    with open("input") as f:
        lines = (line.rstrip("\r\n") for line in f)

        total_priorities = 0
        for badge in parse(lines):
            total_priorities += priority(badge)

    print("Total priorities", total_priorities)


if __name__ == "__main__":
    main()
