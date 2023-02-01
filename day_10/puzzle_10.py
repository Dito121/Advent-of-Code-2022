class Solution:
    def __init__(self, file: str):
        self.file = file
        self.x = 1
        self.total = 0
        self.read_file()

    def read_file(self):
        with open(self.file, "r") as file:
            self.data = [line.strip().split() for line in file]

    def update_total(self):
        if (self.cycle - 20) % 40 == 0:
            self.total += self.x * self.cycle

    def process_x(self, i):
        if self.data[i][0] == "noop":
            self.cycle += 1
            self.update_total()
            return

        self.cycle += 1
        self.update_total()

        if self.data[i][1][0] == "-":
            self.x -= int(self.data[i][1][1:])
        else:
            self.x += int(self.data[i][1])

        self.cycle += 1
        self.update_total()

    def solve_part_1(self) -> int:
        self.cycle = 1

        for i in range(len(self.data)):
            self.process_x(i)

        return self.total

    def solve_part_2(self) -> list[str]:
        return


# answer = Solution("day_10/puzzle_10_data.txt")
# print("Solution to Puzzle 10 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 10 Part 2: ", answer.solve_part_2())
