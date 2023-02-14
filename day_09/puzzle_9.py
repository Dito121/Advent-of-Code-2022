import numpy as np


class Solution:
    def __init__(self, file: str):
        self.file = file
        self.data = []
        self.read_file()

    def read_file(self):
        with open(self.file) as file:
            for line in file:
                line = line.strip().split()
                self.data.append([line[0], int(line[1])])

    def are_touching(self, p1: list[int, int], p2: list[int, int]) -> bool:
        return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) < 1.9

    def shift_right(self):
        self.points[0][1] += 1
        for j in range(1, len(self.points)):
            if not self.are_touching(self.points[j], self.points[j - 1]):
                if self.points[j][0] != self.points[j - 1][0]:
                    self.points[j][0] = self.points[j - 1][0]
                self.points[j][1] += 1

    def shift_left(self):
        self.points[0][1] -= 1
        for j in range(1, len(self.points)):
            if not self.are_touching(self.points[j], self.points[j - 1]):
                if self.points[j][0] != self.points[j - 1][0]:
                    self.points[j][0] = self.points[j - 1][0]
                self.points[j][1] -= 1

    def shift_up(self):
        self.points[0][0] -= 1
        for j in range(1, len(self.points)):
            if not self.are_touching(self.points[j], self.points[j - 1]):
                if self.points[j][1] != self.points[j - 1][1]:
                    self.points[j][1] = self.points[j - 1][1]
                self.points[j][0] -= 1

    def shift_down(self):
        self.points[0][0] += 1
        for j in range(1, len(self.points)):
            if not self.are_touching(self.points[j], self.points[j - 1]):
                if self.points[j][1] != self.points[j - 1][1]:
                    self.points[j][1] = self.points[j - 1][1]
                self.points[j][0] += 1

    def shift_tail(self, i):
        if self.data[i][0] == "R":
            self.shift_right()

        elif self.data[i][0] == "L":
            self.shift_left()

        elif self.data[i][0] == "U":
            self.shift_up()

        elif self.data[i][0] == "D":
            self.shift_down()

    def update_path(self):
        if tuple(self.points[-1]) not in self.path:
            self.path[tuple(self.points[-1])] = 1
        else:
            self.path[tuple(self.points[-1])] += 1

    def solve(self, n: int):
        self.points = [[0, 0] for _ in range(n)]
        self.path = {tuple(self.points[-1]): 1}

        for i in range(len(self.data)):
            for _ in range(self.data[i][1]):
                self.shift_tail(i)
                self.update_path()

        return len(self.path)


if __name__ == "__main__":
    answer = Solution("day_09/puzzle_9_data.txt")
    print("Solution to Puzzle 9 Part 1: ", answer.solve(2))
    print("Solution to Puzzle 9 Part 2: ", answer.solve(10))
