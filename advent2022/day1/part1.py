import functools
import pathlib
import typing

from advent2022 import compute

def parse(lines: typing.Iterator[str]) -> typing.Iterator[int]:
    """Compute the calories of the elements carried by each elf."""
    partial_sum = 0
    for line in lines:
        try:
            partial_sum += int(line)
        except ValueError:
            yield partial_sum
            partial_sum = 0

    if partial_sum > 0:
        yield partial_sum

compute_part1 = functools.partial(compute, parse=parse, process=max)

def main():
    inputpath = pathlib.Path(__file__).parent\
        .joinpath("data", "input").absolute()
    result = compute_part1(inputpath)

    print("Result", result)


if __name__ == "__main__":
    main()
