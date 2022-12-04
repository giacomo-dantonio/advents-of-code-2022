import functools
import pathlib
import typing

from advent2022 import compute


def priority(item: chr) -> int:
    if item >= 'a' and item <= 'z':
        return ord(item) - ord('a') + 1
    elif item >= 'A' and item <= 'Z':
        return ord(item) - ord('A') + 27
    else:
        assert False

def priorities(items: set[chr]) -> int:
    return sum(priority(item) for item in items)

def parse(lines: typing.Iterator[str]) -> typing.Iterator[set[chr]]:
    for line in lines:
        l = len(line)
        assert l % 2 == 0
        yield set(line[:(l//2)]).intersection(line[(l//2):])

def process(data: typing.Iterator[set[chr]]) -> int:
    return sum(priorities(items) for items in data)

compute_part1 = functools.partial(compute, parse=parse, process=process)

def main():
    inputpath = pathlib.Path(__file__).parent\
        .joinpath("data", "input").absolute()
    result = compute_part1(inputpath)

    print("Result", result)


if __name__ == "__main__":
    main()
