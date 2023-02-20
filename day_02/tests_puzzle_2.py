import unittest
from puzzle_2 import Puzzle2


class test_problems(unittest.TestCase):
    def test_puzzle_2(self):
        answer = Puzzle2("day_02/puzzle_2_sample_data.txt")

        self.assertEqual(answer.solve_part_1(), 15)
        self.assertEqual(answer.solve_part_2(), 12)


if __name__ == "__main__":
    unittest.main()
