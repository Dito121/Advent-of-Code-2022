class Puzzle1:
    def __init__(self, file: str) -> None:
        if type(file) != str:
            raise TypeError("filename must be a string")

        self.file = file
        self.read_file()

    def read_file(self) -> None:
        self.elves = []

        with open(self.file, "r") as file:
            count = 0
            """
            open the text file that contains the data of calories each elf has
            """
            for line in file:
                line = line.strip()
                """
                each line that is not representing the end of an elf's snacks
                (using an empty line) is added to the current elf's count
                """
                if line != "":
                    count += int(line)
                    continue
                """
                add this elf's total calorie count to self.elves
                and reset count for next elf
                """
                self.elves.append(count)
                count = 0
            """
            need to make sure to append the count for the final elf in the
            text file because it would otherwise get overlooked
            """
            self.elves.append(count)
        """
        sort list of elves' calorie counts in descending order
        """
        self.elves.sort(reverse=True)

    def max_calories(self) -> int:
        """
        return number of calories of elf with the most calories
        """
        return self.elves[0]

    def max_n_calories(self, n: int) -> int:
        """
        return total number of calories of the n elves with the most calories
        """
        return sum(self.elves[:n])


if __name__ == "__main__":
    answer = Puzzle1("day_01/puzzle_1_data.txt")
    print("Solution to Puzzle 1 Part 1: ", answer.max_calories())
    print("Solution to Puzzle 1 Part 2: ", answer.max_n_calories(3))
