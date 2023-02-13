import unittest
from puzzle_2 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_2(self):
        answer = Solution("day_02/puzzle_2_sample_data.txt")

        self.assertEqual(answer.solve_part_1(), 15)
        self.assertEqual(answer.solve_part_2(), 12)


if __name__ == "__main__":
    unittest.main()
