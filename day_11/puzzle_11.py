from puzzle_11_models import Monkey


class Solution:
    def __init__(self, file: str):
        self.file = file
        self.data = []
        self.monkeys = []
        self.read_file()

    def read_file(self):
        with open(self.file, "r") as file:
            self.data.extend(
                line.translate(
                    str.maketrans("", "", "newmonkeyoldbythrowSaigOpaisivisiuasIf,=:\n")
                )
                .strip()
                .split()
                for line in file
            )
        print(self.data)

    def play_round(self):
        for monkey in self.monkeys:
            monkey.inspect_items()
            throw_to = monkey.test_items()

            for i in range(len(monkey.items)):
                self.monkeys[throw_to[i]].items.append(monkey.items[i])
            monkey.items = []

    def solve_part_1(self):
        for i in range(0, len(self.data), 7):
            self.monkeys.append(Monkey(self.data[i : i + 7]))

        # for monkey in self.monkeys:
        #     print(monkey)
        # print("\n")

        for _ in range(1, 21):
            self.play_round()

            # for monkey in self.monkeys:
            #     print(monkey)
            # print("\n")

        return [monkey.inspections for monkey in self.monkeys]

    def solve_part_2(self):
        return


# answer = Solution("day_11/puzzle_11_data.txt")
# print("Solution to Puzzle 11 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 11 Part 2: ", answer.solve_part_2())
