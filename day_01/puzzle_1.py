class Puzzle1:
    def __init__(self, file: str, n: int = 1) -> None:
        """
        Reads a given file and returns an integer which represents the sum of n elves with most calories.
        """
        if type(file) is not str or not file:
            raise TypeError("filename must be a string")
        elif type(n) != int or n <= 0:
            raise TypeError("optional argument, n, must be a positive integer")

        self.file = file
        self.n = n
        self.top_n_elves = [0] * self.n
        self._read_file()

    def _update_top_n_elves(self, calories: int) -> None:
        """
        Assesses whether or not the current elf's count belongs to the max n seen thus far, then adds it if necessary.
        """
        if calories > self.top_n_elves[-1]:
            self.top_n_elves.append(calories)
            self.top_n_elves.sort(reverse=True)
            del self.top_n_elves[-1]

    def _read_file(self) -> None:
        """
        Parses the data from text file to n elves with most total calories.
        """
        with open(self.file, "r") as file:
            calories = 0

            for line in file:
                if line := line.strip():
                    calories += int(line)
                    continue

                self._update_top_n_elves(calories)
                calories = 0

            self._update_top_n_elves(calories)

        self.answer = sum(self.top_n_elves)


if __name__ == "__main__":
    print("Solution to Puzzle 1 Part 1: ", Puzzle1("day_01/puzzle_1_data.txt").answer)
    print(
        "Solution to Puzzle 1 Part 2: ", Puzzle1("day_01/puzzle_1_data.txt", 3).answer
    )
