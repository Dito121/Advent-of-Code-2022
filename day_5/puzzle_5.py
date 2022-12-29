class Solution:
    def __init__(self, file: str):
        self.file = file
        self.read_file()
        self.create_stacks()
        self.clean_instructions()

    def read_file(self):
        self.p_i = 0
        """
        this finds where the separation between stacks and instructions are in
        the text file and saves that location as self.p_i
        """
        with open(self.file) as file:
            file = list(file.readlines())
            for line in file:
                if line.strip() != "":
                    self.p_i += 1
                else:
                    self.n = int(file[self.p_i - 1][-3])
                    self.stacks = [""] * self.n
                    self.data = file[: self.p_i - 1]
                    self.instructions = file[self.p_i + 1 :]
                    return

    def create_stacks(self):
        """
        populates self.stacks using self.data
        """
        for i in range(len(self.data) - 1, -1, -1):
            for j in range(1, len(self.data[i]), 4):
                if self.data[i][j] != " ":
                    self.stacks[j // 4] += self.data[i][j]

    def clean_instructions(self):
        for i in range(len(self.instructions)):
            self.instructions[i] = (
                self.instructions[i]
                .translate(str.maketrans("", "", "abcdefghijklmnopqrstuvwxyz\n"))
                .split()
            )

    def get_stacks(self):
        return self.stacks.copy()

    def move_item(self, from_stack, to_stack):
        return

    def solve_part_1(self) -> int:
        stacks = self.get_stacks()

        for i in range(len(self.instructions)):
            for _ in range(int(self.instructions[i][0])):
                stacks[int(self.instructions[i][-1]) - 1] += stacks[
                    int(self.instructions[i][1]) - 1
                ][-1]
                stacks[int(self.instructions[i][1]) - 1] = stacks[
                    int(self.instructions[i][1]) - 1
                ][:-1]

        self.part1 = ""
        for i in range(len(stacks)):
            self.part1 += stacks[i][-1]

        return self.part1

    def solve_part_2(self) -> int:
        stacks = self.get_stacks()

        for i in range(len(self.instructions)):
            stacks[int(self.instructions[i][2]) - 1] += stacks[
                int(self.instructions[i][1]) - 1
            ][-int(self.instructions[i][0]) :]
            stacks[int(self.instructions[i][1]) - 1] = stacks[
                int(self.instructions[i][1]) - 1
            ][: -int(self.instructions[i][0])]

        self.part2 = ""
        for i in range(len(stacks)):
            self.part2 += stacks[i][-1]

        return self.part2


# answer = Solution("day_5/puzzle_5_data.txt")
# print("Solution to Puzzle 5 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 5 Part 2: ", answer.solve_part_2())
