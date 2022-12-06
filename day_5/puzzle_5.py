import itertools


class Solution:
    def __init__(self, file: str):
        self.file = file
        self.data = []

        with open(self.file) as file:
            for line in file:
                self.data.append(
                    line.translate(
                        str.maketrans("", "", "abcdefghijklmnopqrstuvwxyz\n")
                    )
                )

        p_i = 0
        while self.data[p_i] != "":
            p_i += 1

        self.instructions = self.data[p_i + 1 :]
        self.n = int(self.data[p_i - 1][-2])
        self.data = self.data[: p_i - 1]

        for i in range(len(self.instructions)):
            self.instructions[i] = self.instructions[i].strip().split()

        stacks = [""] * (p_i - 1)
        for i in range(len(self.data) - 1, -1, -1):
            for j in range(1, len(self.data[i]), 4):
                stacks[i] += self.data[i][j]

        self.data = [""] * self.n
        for i in range(len(stacks) - 1, -1, -1):
            for j in range(len(self.data)):
                if stacks[i][j] == " ":
                    continue
                self.data[j] += stacks[i][j]

    def solve_part_1(self) -> int:
        for i in range(len(self.instructions)):
            for _ in range(int(self.instructions[i][0])):
                self.data[int(self.instructions[i][-1]) - 1] += self.data[
                    int(self.instructions[i][1]) - 1
                ][-1]
                self.data[int(self.instructions[i][1]) - 1] = self.data[
                    int(self.instructions[i][1]) - 1
                ][:-1]

        self.part1 = ""
        for i in range(len(self.data)):
            self.part1 += self.data[i][-1]

        return self.part1

    def solve_part_2(self) -> int:
        pass


# answer = Solution("day_5/puzzle_5_data.txt")
# print("Solution to Puzzle 5 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 5 Part 2: ", answer.solve_part_2())
