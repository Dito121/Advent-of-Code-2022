class Solution:
    def __init__(self, file: str):
        self.file = file
        self.data = []
        self.answer = 0

        with open(self.file, "r") as file:
            for line in file:
                data = line.strip().split(",")
                self.data.extend(
                    list(map(int, data[i].split("-"))) for i in range(len(data))
                )

    def solve_part_1(self) -> int:
        self.answer = 0

        for i in range(0, len(self.data), 2):
            if (
                self.data[i][0] <= self.data[i + 1][0]
                and self.data[i][1] >= self.data[i + 1][1]
            ):
                self.answer += 1
            elif (
                self.data[i][0] >= self.data[i + 1][0]
                and self.data[i][1] <= self.data[i + 1][1]
            ):
                self.answer += 1

        return self.answer

    def solve_part_2(self) -> int:
        self.answer = 0

        for i in range(0, len(self.data), 2):
            if (
                (self.data[i][0] <= self.data[i + 1][0] <= self.data[i][1])
                or (self.data[i][0] <= self.data[i + 1][1] <= self.data[i][1])
                or (self.data[i + 1][0] <= self.data[i][0] <= self.data[i + 1][1])
                or (self.data[i + 1][0] <= self.data[i][1] <= self.data[i + 1][1])
            ):
                self.answer += 1

        return self.answer


answer = Solution("day_4/puzzle_4_data.txt")
print("Solution to Puzzle 4 Part 1: ", answer.solve_part_1())
print("Solution to Puzzle 4 Part 2: ", answer.solve_part_2())
