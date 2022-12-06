import unittest
from puzzle_6 import Solution


class test_problems(unittest.TestCase):
    def test_1_puzzle_6(self):
        answer1 = Solution("day_6/sample_data/puzzle_6_sample_data_1.txt")
        self.assertEqual(answer1.solve_part_1(), 7)
        self.assertEqual(answer1.solve_part_2(), 19)

    def test_2_puzzle_6(self):
        answer2 = Solution("day_6/sample_data/puzzle_6_sample_data_2.txt")
        self.assertEqual(answer2.solve_part_1(), 5)
        self.assertEqual(answer2.solve_part_2(), 23)

    def test_3_puzzle_6(self):
        answer3 = Solution("day_6/sample_data/puzzle_6_sample_data_3.txt")
        self.assertEqual(answer3.solve_part_1(), 6)
        self.assertEqual(answer3.solve_part_2(), 23)

    def test_4_puzzle_6(self):
        answer4 = Solution("day_6/sample_data/puzzle_6_sample_data_4.txt")
        self.assertEqual(answer4.solve_part_1(), 10)
        self.assertEqual(answer4.solve_part_2(), 29)

    def test_5_puzzle_6(self):
        answer5 = Solution("day_6/sample_data/puzzle_6_sample_data_5.txt")
        self.assertEqual(answer5.solve_part_1(), 11)
        self.assertEqual(answer5.solve_part_2(), 26)


if __name__ == "__main__":
    unittest.main()
