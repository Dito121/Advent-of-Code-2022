import unittest
from puzzle_1 import Puzzle1


class test_day_01(unittest.TestCase):
    def test_puzzle_1(self):
        part1 = Puzzle1("day_01/puzzle_1_sample_data.txt")
        self.assertEqual(part1.max_n_calories(), 24_000)

        part2 = Puzzle1("day_01/puzzle_1_sample_data.txt", 3)
        self.assertEqual(part2.max_n_calories(), 45_000)


if __name__ == "__main__":
    unittest.main()
