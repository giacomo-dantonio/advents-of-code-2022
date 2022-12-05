import functools
import pathlib
import typing

from advent2022 import compute
from advent2022.day5.part1 import CratesType, ParsedType, parse


def process(data: typing.Iterator[ParsedType]) -> str:
    stacks: CratesType = next(data)

    for (amount, fromm, to) in data:
        stacks[to].extend(stacks[fromm][-amount:])
        del stacks[fromm][-amount:]

    result = "".join(stacks[key].pop() for key in sorted(stacks.keys()))
    return result

compute_part2 = functools.partial(compute, parse=parse, process=process)

def main():
    inputpath = pathlib.Path(__file__).parent\
        .joinpath("data", "input").absolute()
    result = compute_part2(inputpath)

    print("Result", result)


if __name__ == "__main__":
    main()
