class Solution:
    def __init__(self, file: str):
        self.sum = 0
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.key = {letters[i]: i + 1 for i in range(len(letters))}
        with open(file, "r") as file:
            self.lines = [line.strip() for line in file]

    def solve_part_1(self) -> int:
        self.sum = 0

        for i in range(len(self.lines)):
            midpoint = len(self.lines[i]) // 2
            right = self.lines[i][midpoint:]

            for j in range(midpoint):
                if self.lines[i][j] in right:
                    self.sum += self.key[self.lines[i][j]]
                    break

        return self.sum

    def solve_part_2(self) -> int:
        self.sum = 0

        for i in range(0, len(self.lines), 3):
            third = self.lines[i + 2]

            for j in range(len(self.lines[i])):
                if (
                    self.lines[i][j] in self.lines[i + 1]
                    and self.lines[i][j] in self.lines[i + 2]
                ):
                    self.sum += self.key[self.lines[i][j]]
                    break

        return self.sum


answer = Solution("day_3/puzzle_3_data.txt")
print("Solution to Puzzle 3 Part 1: ", answer.solve_part_1())
print("Solution to Puzzle 3 Part 2: ", answer.solve_part_2())
