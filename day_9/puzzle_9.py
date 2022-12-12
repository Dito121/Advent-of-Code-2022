import numpy as np


class Solution:
    def __init__(self, file: str, n: int = 2):
        self.file = file
        self.data = []
        self.n = n

        with open(self.file) as file:
            for line in file:
                line = line.strip().split()
                self.data.append([line[0], int(line[1])])

    def are_touching(self, p1: list[int, int], p2: list[int, int]) -> bool:
        return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) < 1.9

    def track_tail(self):
        if tuple(self.points[-1]) not in self.path:
            self.path[tuple(self.points[-1])] = 1
        else:
            self.path[tuple(self.points[-1])] += 1

    def shift_tail(self, i):
        if self.data[i][0] == "R":
            self.points[0][1] += 1

            for j in range(1, len(self.points)):
                if not self.are_touching(self.points[j], self.points[j - 1]):
                    if self.points[j][0] != self.points[j - 1][0]:
                        self.points[j][0] = self.points[j - 1][0]
                    self.points[j][1] += 1

        elif self.data[i][0] == "L":
            self.points[0][1] -= 1

            for j in range(1, len(self.points)):
                if not self.are_touching(self.points[j], self.points[j - 1]):
                    if self.points[j][0] != self.points[j - 1][0]:
                        self.points[j][0] = self.points[j - 1][0]
                    self.points[j][1] -= 1

        elif self.data[i][0] == "U":
            self.points[0][0] -= 1

            for j in range(1, len(self.points)):
                if not self.are_touching(self.points[j], self.points[j - 1]):
                    if self.points[j][1] != self.points[j - 1][1]:
                        self.points[j][1] = self.points[j - 1][1]
                    self.points[j][0] -= 1

        elif self.data[i][0] == "D":
            self.points[0][0] += 1

            for j in range(1, len(self.points)):
                if not self.are_touching(self.points[j], self.points[j - 1]):
                    if self.points[j][1] != self.points[j - 1][1]:
                        self.points[j][1] = self.points[j - 1][1]
                    self.points[j][0] += 1

    def solve_part_1(self):
        self.points = []
        for i in range(self.n):
            self.points.append([len(self.data) - 1, 0])
        self.path = {tuple(self.points[-1]): 1}

        for i in range(len(self.data)):
            for _ in range(self.data[i][1]):
                self.shift_tail(i)
                self.track_tail()

        return len(self.path)

    def solve_part_2(self):
        pass


# answer = Solution("day_9/puzzle_9_data.txt")
# print("Solution to Puzzle 9 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 9 Part 2: ", answer.solve_part_2())
