class Puzzle1:
    def __init__(self, file: str, n: int = 1) -> None:
        """
        Reads a given file and returns an integer which represents the sum of n elves with most calories.
        """
        if type(file) != str:
            raise TypeError("filename must be a string")
        elif type(n) != int or n <= 0:
            raise TypeError("argument, n, must be a positive integer")

        self.file = file
        self.n = n
        self.read_file()

    def update_elves(self, count: int) -> None:
        """
        Assesses whether or not the current elf's count belongs to the max n seen thus far, then adds it if necessary.
        """
        if count > self.elves[-1]:
            self.elves.append(count)
            self.elves.sort(reverse=True)
            del self.elves[-1]

    def read_file(self) -> None:
        """
        Parses the data from text file to n elves with most total calories.
        """
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
            """
            add final elf's total calorie count to self.elves
            """
            self.update_elves(count)
        self.answer = sum(self.elves)


if __name__ == "__main__":
    print("Solution to Puzzle 1 Part 1: ", Puzzle1("day_01/puzzle_1_data.txt").answer)
    print(
        "Solution to Puzzle 1 Part 2: ", Puzzle1("day_01/puzzle_1_data.txt", 3).answer
    )
