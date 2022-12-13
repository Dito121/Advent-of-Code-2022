import unittest
from puzzle_10 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_10_part_1(self):
        answer = Solution("day_10/puzzle_10_sample_data.txt")
        self.assertEqual(answer.solve_part_1(), 13140)

        part2 = [
            ["##..##..##..##..##..##..##..##..##..##.."],
            ["###...###...###...###...###...###...###."],
            ["####....####....####....####....####...."],
            ["#####.....#####.....#####.....#####....."],
            ["######......######......######......####"],
            ["#######.......#######.......#######....."],
        ]
        self.assertEqual(answer.solve_part_2(), part2)


if __name__ == "__main__":
    unittest.main()
