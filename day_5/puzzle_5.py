class Solution:
    def __init__(self, file: str):
        self.file = file
        self.data = []

        with open(self.file) as file:
            for line in file:
                self.data.append(
                    line.translate(
                        str.maketrans("", "", "abcdefghijklmnopqrstuvwxyz\n[]")
                    )
                )

        i = 0
        while self.data[i] != "":
            i += 1

        self.instructions = self.data[:i]
        self.data = self.data[i + 1 :]
        for i in range(len(self.data)):
            self.data[i] = self.data[i].strip()

        # print(self.instructions)
        # print(self.data)

    def solve_part_1(self) -> int:
        pass

    def solve_part_2(self) -> int:
        pass


# answer = Solution("day_5/puzzle_5_data.txt")
# print("Solution to Puzzle 5 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 5 Part 2: ", answer.solve_part_2())
