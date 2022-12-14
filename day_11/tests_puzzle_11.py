import unittest
from puzzle_11 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_11(self):
        answer = Solution("day_11/puzzle_11_sample_data.txt")

        self.assertEqual(answer.solve_part_1(), 10605)
        # self.assertEqual(answer.solve_part_2(), )


if __name__ == "__main__":
    unittest.main()
