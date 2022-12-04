import functools
import pathlib
import re
import typing

from advent2022 import compute

DataType = typing.Tuple[int, int, int, int]

exp = re.compile("^(?P<A>\d+)-(?P<B>\d+),(?P<C>\d+)-(?P<D>\d+)$")

def parse(lines: typing.Iterator[str]) -> typing.Iterator[DataType]:
    for line in lines:
        m = exp.match(line)
        if m:
            yield (int(m.group("A")), int(m.group("B")), int(m.group("C")), int(m.group("D")))

def process(data: typing.Iterator[DataType]) -> int:
    def condition(item):
        (A, B, C, D) = item
        return (A <= C and B >= D)\
            or (C <= A and D >= B)

    return sum(1 for item in data if condition(item))

compute_part1 = functools.partial(compute, parse=parse, process=process)

def main():
    inputpath = pathlib.Path(__file__).parent\
        .joinpath("data", "input").absolute()
    result = compute_part1(inputpath)

    print("Result", result)


if __name__ == "__main__":
    main()
