import unittest
from puzzle_9 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_9(self):
        answer = Solution("day_9/puzzle_9_sample_data_part_1.txt")

        self.assertEqual(answer.solve_part_1(), 13)
        # self.assertEqual(answer.solve_part_2(), )


if __name__ == "__main__":
    unittest.main()
