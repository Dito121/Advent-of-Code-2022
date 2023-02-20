import unittest
from puzzle_1 import Puzzle1


class test_day_01(unittest.TestCase):
    def test_puzzle_1(self):
        puzzle1 = Puzzle1("day_01/puzzle_1_sample_data.txt")

        self.assertEqual(puzzle1.max_calories(), 24_000)
        self.assertEqual(puzzle1.max_n_calories(3), 45_000)


if __name__ == "__main__":
    unittest.main()
