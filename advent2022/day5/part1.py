import collections
import functools
import pathlib
import re
import typing

from advent2022 import compute

CratesType = typing.Dict[int, list]
MoveType = typing.Tuple[int, int, int]
ParsedType = typing.Union[CratesType, MoveType]

exp = re.compile("^move (?P<amount>\d+) from (?P<from>\d+) to (?P<to>\d+)$")

def parse_stacks(lines: typing.Iterator[str]) -> CratesType:
    stacks = collections.defaultdict(collections.deque)
    for line in lines:
        if line == "":
            break

        for i in range(1, len(line), 4):
            c = line[i]
            j = (i - 1) // 4 + 1
            if c >= 'A' and c <= 'Z':
                stacks[j].appendleft(c)

    return {key: list(stacks[key]) for key in stacks}

def parse(lines: typing.Iterator[str]) -> typing.Iterator[ParsedType]:
    # First parse the initial stack
    yield parse_stacks(lines)

    # Then parse the moves
    for line in lines:
        m = exp.match(line)
        if m:
            yield (
                int(m.group("amount")),
                int(m.group("from")),
                int(m.group("to"))
            )


def process(data: typing.Iterator[ParsedType]) -> str:
    stacks: CratesType = next(data)

    for (amount, fromm, to) in data:
        stacks[to].extend(reversed(stacks[fromm][-amount:]))
        del stacks[fromm][-amount:]

    result = "".join(stacks[key].pop() for key in sorted(stacks.keys()))
    return result

compute_part1 = functools.partial(compute, parse=parse, process=process)

def main():
    inputpath = pathlib.Path(__file__).parent\
        .joinpath("data", "input").absolute()
    result = compute_part1(inputpath)

    print("Result", result)


if __name__ == "__main__":
    main()
