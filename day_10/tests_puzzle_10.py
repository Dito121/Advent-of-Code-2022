import unittest
from puzzle_10 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_10(self):
        answer = Solution("day_10/puzzle_10_data.txt")

        # self.assertEqual(answer.solve_part_1(), )
        # self.assertEqual(answer.solve_part_2(), )


if __name__ == "__main__":
    unittest.main()
