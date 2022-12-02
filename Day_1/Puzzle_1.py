class Solution:
    def __init__(self, file: str, n: int = 3):
        self.count = 0
        self.n = n
        self.max = []
        self.file = file

        with open(self.file, "r") as file:
            for line in file:
                if line.strip() != "":
                    self.count += int(line)
                    continue

                self.max.append(self.count)
                self.count = 0
            self.max.append(self.count)

        self.max.sort(reverse=True)

    def solve_part_1(self) -> int:
        return self.max[0]

    def solve_part_2(self) -> int:
        return sum(self.max[: self.n])


# answer = Solution("Day_1/Puzzle_1_Data.txt")
# print(answer.solve_part_1())
# print(answer.solve_part_2())
