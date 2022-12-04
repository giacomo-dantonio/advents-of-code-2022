import functools
import heapq
import pathlib
import typing

from advent2022 import compute
from advent2022.day1.part1 import parse

def process(data: typing.Iterator[int]) -> int:
    three_largest = heapq.nlargest(3, data)
    return sum(three_largest)

compute_part2 = functools.partial(compute, parse=parse, process=process)

def main():
    inputpath = pathlib.Path(__file__).parent\
        .joinpath("data", "input").absolute()
    result = compute_part2(inputpath)

    print("Result", result)


if __name__ == "__main__":
    main()
