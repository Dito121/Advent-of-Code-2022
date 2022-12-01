import unittest
from Puzzle_1 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_1(self):
        puzzle1 = Solution("Day_1/Puzzle_1_Sample_Data.txt")

        self.assertEqual(puzzle1.solve_part_1(), 24000)
        self.assertEqual(puzzle1.solve_part_2(), 45000)


if __name__ == "__main__":
    unittest.main()
