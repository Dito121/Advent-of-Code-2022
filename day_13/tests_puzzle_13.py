import unittest
from puzzle_13 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_13(self):
        answer = Solution("day_13/puzzle_13_sample_data.txt")

        self.assertEqual(answer.solve_part_1(), 13)
        # self.assertEqual(answer.solve_part_2(), )


if __name__ == "__main__":
    unittest.main()
