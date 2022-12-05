import re


class Solution:
    def __init__(self, file: str):
        self.file = file
        self.data = []

        with open(self.file) as file:
            for line in file:
                my_str = line.translate(
                    str.maketrans("", "", "abcdefghijklmnopqrstuvwxyz\n[]")
                )
                self.data.append(re.sub(" +", " ", my_str))

        p_i = 0
        while self.data[p_i] != "":
            p_i += 1

        self.instructions = self.data[p_i + 1 :]
        self.data = self.data[:p_i]
        self.data[-1] = self.data[-1].strip()
        self.n = int(self.data[-1][-1])

        for i in range(len(self.instructions)):
            self.instructions[i] = self.instructions[i].strip()

        print(self.data)
        print(self.instructions)

    def solve_part_1(self) -> int:
        pass

    def solve_part_2(self) -> int:
        pass


# answer = Solution("day_5/puzzle_5_data.txt")
# print("Solution to Puzzle 5 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 5 Part 2: ", answer.solve_part_2())
