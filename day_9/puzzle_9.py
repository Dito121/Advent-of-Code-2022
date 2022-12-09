import numpy as np


class Solution:
    def __init__(self, file: str):
        self.file = file
        self.data = []
        with open(self.file) as file:
            for line in file:
                line = line.strip().split()
                self.data.append([line[0], int(line[1])])

    def are_touching(self, p1: tuple, p2: tuple) -> bool:
        return int(np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)) < 2

    def solve_part_1(self):
        self.path = {}

        return

    def solve_part_2(self):
        pass


# answer = Solution("day_9/puzzle_9_data.txt")
# print("Solution to Puzzle 9 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 9 Part 2: ", answer.solve_part_2())
