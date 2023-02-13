import unittest
from puzzle_8 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_8(self):
        answer = Solution("day_08/puzzle_8_sample_data.txt")

        self.assertEqual(answer.solve_part_1(), 21)
        self.assertEqual(answer.solve_part_2(), 8)


if __name__ == "__main__":
    unittest.main()
