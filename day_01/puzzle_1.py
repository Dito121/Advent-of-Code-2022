class Puzzle1:
    def __init__(self, file: str, n: int = 1) -> None:
        if type(file) != str:
            raise TypeError("filename must be a string")
        elif type(n) != int or n <= 0:
            raise TypeError("argument, n, must be a positive integer")

        self.file = file
        self.n = n
        self.read_file()

    def update_elves(self, count):
        if count > self.elves[-1]:
            self.elves.append(count)
            self.elves.sort(reverse=True)
            del self.elves[-1]

    def read_file(self) -> None:
        self.elves = [0] * self.n

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
                self.update_elves(count)
                count = 0
            self.update_elves(count)

    def max_n_calories(self) -> int:
        """
        return total number of calories of the n elves with the most calories
        """
        return sum(self.elves)


if __name__ == "__main__":
    part1 = Puzzle1("day_01/puzzle_1_data.txt")
    print("Solution to Puzzle 1 Part 1: ", part1.max_n_calories())

    part2 = Puzzle1("day_01/puzzle_1_data.txt", 3)
    print("Solution to Puzzle 1 Part 2: ", part2.max_n_calories())
