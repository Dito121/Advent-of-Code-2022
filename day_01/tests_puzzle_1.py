import unittest
from puzzle_1 import Puzzle1


class test_day_01(unittest.TestCase):
    def test_puzzle_1(self):
        self.assertEqual(Puzzle1("day_01/puzzle_1_test_data.txt").answer, 24_000)
        self.assertEqual(Puzzle1("day_01/puzzle_1_test_data.txt", 3).answer, 45_000)


if __name__ == "__main__":
    unittest.main()
