import unittest
from puzzle_7 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_7(self):
        answer = Solution("day_07/puzzle_7_sample_data.txt")

        answer.solve_part_1(answer.root)
        self.assertEqual(answer.part1, 95437)
        self.assertEqual(answer.solve_part_2(), 24933642)


if __name__ == "__main__":
    unittest.main()
