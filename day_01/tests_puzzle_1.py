import unittest
from puzzle_1 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_1(self):
        puzzle1 = Solution("day_01/puzzle_1_sample_data.txt")

        self.assertEqual(puzzle1.max_calories(), 24000)
        self.assertEqual(puzzle1.max_n_calories(3), 45000)


if __name__ == "__main__":
    unittest.main()
