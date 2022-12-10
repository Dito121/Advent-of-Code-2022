import numpy as np


class Solution:
    def __init__(self, file: str):
        self.file = file
        self.data = []

        with open(self.file) as file:
            for line in file:
                line = line.strip().split()
                self.data.append([line[0], int(line[1])])

    def are_touching(self) -> bool:
        return (
            np.sqrt(
                (self.p_head[0] - self.p_tail[0]) ** 2
                + (self.p_head[1] - self.p_tail[1]) ** 2
            )
            < 2
        )

    def track_tail(self):
        if tuple(self.p_tail) not in self.path:
            self.path[tuple(self.p_tail)] = 1
        else:
            self.path[tuple(self.p_tail)] += 1

    def shift_tail(self, i):
        if self.data[i][0] == "R":
            self.p_head[1] += 1

            if not self.are_touching():
                if self.p_tail[0] != self.p_head[0]:
                    self.p_tail[0] = self.p_head[0]
                self.p_tail[1] += 1

        elif self.data[i][0] == "L":
            self.p_head[1] -= 1

            if not self.are_touching():
                if self.p_tail[0] != self.p_head[0]:
                    self.p_tail[0] = self.p_head[0]
                self.p_tail[1] -= 1

        elif self.data[i][0] == "U":
            self.p_head[0] -= 1

            if not self.are_touching():
                if self.p_tail[1] != self.p_head[1]:
                    self.p_tail[1] = self.p_head[1]
                self.p_tail[0] -= 1

        elif self.data[i][0] == "D":
            self.p_head[0] += 1

            if not self.are_touching():
                if self.p_tail[1] != self.p_head[1]:
                    self.p_tail[1] = self.p_head[1]
                self.p_tail[0] += 1

    def solve_part_1(self):
        self.p_head = [len(self.data) - 1, 0]
        self.p_tail = [len(self.data) - 1, 0]
        self.path = {tuple(self.p_tail): 1}

        for i in range(len(self.data)):
            for _ in range(self.data[i][1]):
                self.shift_tail(i)
                self.track_tail()

        return len(self.path)

    def solve_part_2(self):
        pass


answer = Solution("day_9/puzzle_9_data.txt")
print("Solution to Puzzle 9 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 9 Part 2: ", answer.solve_part_2())
