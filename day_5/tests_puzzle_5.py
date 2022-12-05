import unittest
from puzzle_5 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_5(self):
        answer = Solution("day_5/puzzle_5_sample_data.txt")

        self.assertEqual(answer.solve_part_1(), "CMZ")
        # self.assertEqual(answer.solve_part_2(), )


if __name__ == "__main__":
    unittest.main()
