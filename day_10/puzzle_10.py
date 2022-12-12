class Solution:
    def __init__(self, file: str):
        self.file = file
        self.x = 1
        self.total = 0

        with open(self.file, "r") as file:
            self.data = [line.strip().split() for line in file]

    def solve_part_1(self):
        cycle = 1

        for i in range(len(self.data)):
            if (cycle - 20) % 40 == 0:
                self.total += self.x * cycle

            if self.data[i][0] == "noop":
                cycle += 1
                continue

            cycle += 2

            if self.data[i][1][0] == "-":
                self.x -= int(self.data[i][1][1:])
            else:
                self.x += int(self.data[i][1])

        return self.total

    def solve_part_2(self):
        return


# answer = Solution("day_10/puzzle_10_data.txt")
# print("Solution to Puzzle 10 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 10 Part 2: ", answer.solve_part_2())
