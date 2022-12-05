import pathlib
import unittest

from advent2022.day5.part1 import compute_part1
from advent2022.day5.part2 import compute_part2

class Day5Test(unittest.TestCase):
    inputpath = pathlib.Path(__file__).parent\
        .joinpath("data", "test_input").absolute()

    def test_part1(self):
        """Test the part 1 computation on the example data."""
        result = compute_part1(self.inputpath)
        self.assertEqual("CMZ", result)

    def test_part2(self):
        """Test the part 2 computation on the example data."""
        result = compute_part2(self.inputpath)
        self.assertEqual("MCD", result)

if __name__ == '__main__':
    unittest.main()
