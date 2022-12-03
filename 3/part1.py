import typing


def priority(item: chr) -> int:
    if item >= 'a' and item <= 'z':
        return ord(item) - ord('a') + 1
    elif item >= 'A' and item <= 'Z':
        return ord(item) - ord('A') + 27
    else:
        assert False

def priorities(items: set[chr]) -> int:
    return sum(priority(item) for item in items)

def parse(lines: typing.Iterator[str]) -> set[chr]:
    for line in lines:
        l = len(line)
        assert l % 2 == 0
        yield set(line[:(l//2)]).intersection(line[(l//2):])

def main():
    with open("input") as f:
        lines = (line.rstrip("\r\n") for line in f)

        total_priorities = 0
        for items in parse(lines):
            total_priorities += priorities(items)

    print("Total priorities", total_priorities)


if __name__ == "__main__":
    main()
