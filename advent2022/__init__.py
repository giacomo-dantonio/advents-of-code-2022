import pathlib
import typing

T = typing.TypeVar("T")
U = typing.TypeVar("U")
ParseType = typing.Callable[[typing.Iterator[str]], typing.Iterator[T]]
ProcessType = typing.Callable[[typing.Iterator[T]], U]

def compute(filepath: pathlib.Path, parse: ParseType, process: ProcessType) -> U:
    with open(filepath) as f:
        lines = (line.rstrip("\r\n") for line in f)
        return process(parse(lines))
