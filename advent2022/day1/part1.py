import typing


def calories(lines : typing.Iterator[str]) -> typing.Iterator[int]:
    """Compute the calories sum of the elements carried by each elf."""
    partial_sum = 0
    for line in lines:
        try:
            partial_sum += int(line)
        except ValueError:
            yield partial_sum
            partial_sum = 0

def main():
    with open("input") as f:
        lines = (line.rstrip("\r\n") for line in f)
        max_calories = max(calories(lines))

    print("Max calories:", max_calories)


if __name__ == "__main__":
    main()
