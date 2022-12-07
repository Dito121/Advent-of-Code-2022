import unittest
from puzzle_7 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_7(self):
        answer = Solution("day_7/puzzle_7_sample_data.txt")

        self.assertEqual(answer.solve_part_1(), 95437)
        # self.assertEqual(answer.solve_part_2(), "")


if __name__ == "__main__":
    unittest.main()
