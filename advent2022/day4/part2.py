import functools
import pathlib
import typing

from advent2022 import compute
from advent2022.day4.part1 import DataType, parse

def process(data: typing.Iterator[DataType]) -> int:
    def condition(item):
        (A, B, C, D) = item
        return (B >= C and A <= D)\
            or (D >= A and C <= A)
    return sum(1 for item in data if condition(item))

compute_part2 = functools.partial(compute, parse=parse, process=process)

def main():
    inputpath = pathlib.Path(__file__).parent\
        .joinpath("data", "input").absolute()
    result = compute_part2(inputpath)

    print("Result", result)


if __name__ == "__main__":
    main()
