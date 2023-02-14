import unittest
from puzzle_12 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_11(self):
        answer = Solution("day_12/puzzle_12_sample_data.txt")

        self.assertEqual(answer.solve_part_1(), 31)
        self.assertEqual(answer.solve_part_2(), 29)


if __name__ == "__main__":
    unittest.main()
