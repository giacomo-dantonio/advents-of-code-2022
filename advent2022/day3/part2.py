import functools
import itertools
import pathlib
import typing

from advent2022 import compute
from advent2022.day3.part1 import priority


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

def process(data: typing.Iterator[set[chr]]) -> int:
    return sum(priority(item) for item in data)

compute_part2 = functools.partial(compute, parse=parse, process=process)

def main():
    inputpath = pathlib.Path(__file__).parent\
        .joinpath("data", "input").absolute()
    result = compute_part2(inputpath)

    print("Result", result)


if __name__ == "__main__":
    main()
