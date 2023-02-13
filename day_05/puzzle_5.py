class Solution:
    def __init__(self, file: str):
        """
        1. Read the file using read_file() method.
        2. Reorganize data in self.data using create_stacks() method into self.stacks.
        3. Prepare instructions using clean_instructions() method.
        """
        self.file = file
        self.read_file()
        self.create_stacks()
        self.clean_instructions()

    def read_file(self):
        self.p_i = 0
        """
        1. Find where the separation between stacks and instructions are in
            the text file and use that to create self.data, self.stacks, and
            self.instructions.
        2. Initiate self.stacks as a list of empty strings of length self.n.
        3. self.data is the information about the stacks but needs to be
            reorganized into self.stacks.
        4. self.instructions will need to be cleaned using clean_instructions()
            method.
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
            self.instructions[i] = list(
                map(
                    int,
                    self.instructions[i]
                    .translate(str.maketrans("", "", "abcdefghijklmnopqrstuvwxyz\n"))
                    .split(),
                )
            )

    def get_stacks(self) -> list:
        """
        solve_part1() and solve_part2() methods manipulate the stacks and thus need
        to be able to reset the stacks as initially read from the file.
        """
        return self.stacks.copy()

    def move_item_n_times(
        self, stacks: list, n: int, stack_initial: list, stack_final: list
    ):
        """
        moves n items from stack_initial to stack_final.
        """
        for _ in range(n):
            stacks[stack_final] += stacks[stack_initial][-1]
            stacks[stack_initial] = stacks[stack_initial][:-1]

    def move_n_items(
        self, stacks: list, n: int, stack_initial: list, stack_final: list
    ):
        """
        moves n items from stack_initial to stack_final.
        """
        stacks[stack_final] += stacks[stack_initial][-n:]
        stacks[stack_initial] = stacks[stack_initial][:-n]

    def solve_part_1(self) -> int:
        stacks = self.get_stacks()
        """
        implement self.instructions to move one item at a time, n times.
        """
        for i in range(len(self.instructions)):
            self.move_item_n_times(
                stacks,
                self.instructions[i][0],
                self.instructions[i][1] - 1,
                self.instructions[i][2] - 1,
            )

        self.part1 = ""
        for i in range(len(stacks)):
            self.part1 += stacks[i][-1]

        return self.part1

    def solve_part_2(self) -> int:
        stacks = self.get_stacks()
        """
        implement self.instructions to move n items.
        """
        for i in range(len(self.instructions)):
            self.move_n_items(
                stacks,
                self.instructions[i][0],
                self.instructions[i][1] - 1,
                self.instructions[i][2] - 1,
            )

        self.part2 = ""
        for i in range(len(stacks)):
            self.part2 += stacks[i][-1]

        return self.part2


answer = Solution("day_05/puzzle_5_data.txt")
print("Solution to Puzzle 5 Part 1: ", answer.solve_part_1())
print("Solution to Puzzle 5 Part 2: ", answer.solve_part_2())
