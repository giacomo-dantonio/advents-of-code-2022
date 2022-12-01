import typing
from part1 import calories


def maxn(n : int, collection : typing.Iterator[int]) -> list[int]:
    """Return the n biggest elements in collection."""
    acc = [0] * n

    for el in collection:
        acc.append(el)
        acc.remove(min(acc))

    return acc

def main():
    with open("input") as f:
        lines = (line.rstrip("\r\n") for line in f)
        max_calories = maxn(3, calories(lines))

    print("Max calories:", sum(max_calories))


if __name__ == "__main__":
    main()
