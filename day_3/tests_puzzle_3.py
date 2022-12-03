import unittest
from puzzle_3 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_3(self):
        answer = Solution("day_3/puzzle_3_sample_data.txt")

        self.assertEqual(answer.solve_part_1(), 157)
        # self.assertEqual(answer.solve_part_2(), )


if __name__ == "__main__":
    unittest.main()
