import pathlib
import unittest

from advent2022.day2.part1 import compute_part1
from advent2022.day2.part2 import compute_part2

class Day1Test(unittest.TestCase):
    inputpath = pathlib.Path(__file__).parent\
        .joinpath("data", "test_input").absolute()

    def test_part1(self):
        """Test the part 1 computation on the example data."""
        result = compute_part1(self.inputpath)
        self.assertEqual(15, result)

    def test_part2(self):
        """Test the part 2 computation on the example data."""
        result = compute_part2(self.inputpath)
        self.assertEqual(12, result)

if __name__ == '__main__':
    unittest.main()
