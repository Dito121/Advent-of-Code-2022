import unittest
from puzzle_9 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_9_part_1(self):
        answer1 = Solution("day_9/puzzle_9_sample_data_part_1.txt")
        self.assertEqual(answer1.solve(2), 13)

    def test_puzzle_9_part_2(self):
        answer2 = Solution("day_9/puzzle_9_sample_data_part_2.txt")
        self.assertEqual(answer2.solve(10), 36)


if __name__ == "__main__":
    unittest.main()
