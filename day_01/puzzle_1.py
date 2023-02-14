class Solution:
    def __init__(self, file: str, n: int = 3):
        self.file = file
        self.n = n
        self.count = 0
        self.read_file()

    def read_file(self):
        self.elves = []

        with open(self.file, "r") as file:
            """
            open the text file that contains the data of calories each elf has
            """
            for line in file:
                """
                each line that is not representing the end of an elf's snacks
                (using an empty line) is added to the current elf's count
                """
                if line.strip() != "":
                    self.count += int(line)
                    continue
                """
                add this elf's total calorie count to self.elves
                and reset count for next elf
                """
                self.elves.append(self.count)
                self.count = 0
            self.elves.append(self.count)
        """
        sort list of elves' calorie counts in descending order
        """
        self.elves.sort(reverse=True)

    def max_calories(self) -> int:
        """
        return no. of calories of elf with the most calories
        """
        return self.elves[0]

    def max_n_calories(self) -> int:
        """
        return total no. of calories of the n elves with the most calories
        """
        return sum(self.elves[: self.n])


if __name__ == "__main__":
    answer = Solution("day_01/puzzle_1_data.txt")
    print(answer.max_calories())
    print(answer.max_n_calories())
