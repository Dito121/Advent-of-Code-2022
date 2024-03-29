import unittest
from puzzle_4 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_4(self):
        answer = Solution("day_04/puzzle_4_sample_data.txt")

        self.assertEqual(answer.solve_part_1(), 2)
        self.assertEqual(answer.solve_part_2(), 4)


if __name__ == "__main__":
    unittest.main()
