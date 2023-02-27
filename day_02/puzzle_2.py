KEY_PART1 = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}
KEY_PART2 = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "lost",
    "Y": "draw",
    "Z": "won",
}
RESULTS_PART1 = {
    ("rock", "rock"): 4,  # draw
    ("rock", "paper"): 1,  # lost
    ("rock", "scissors"): 7,  # won
    ("paper", "rock"): 8,  # won
    ("paper", "paper"): 5,  # draw
    ("paper", "scissors"): 2,  # lost
    ("scissors", "rock"): 3,  # lost
    ("scissors", "paper"): 9,  # won
    ("scissors", "scissors"): 6,  # draw
}
RESULTS_PART2 = {
    ("rock", "draw"): 4,
    ("paper", "lost"): 1,
    ("scissors", "won"): 7,
    ("rock", "won"): 8,
    ("paper", "draw"): 5,
    ("scissors", "lost"): 2,
    ("rock", "lost"): 3,
    ("paper", "won"): 9,
    ("scissors", "draw"): 6,
}


class Puzzle2:
    def __init__(self, file: str) -> None:
        if type(file) != str or not file:
            raise TypeError("file must be a string.")

        self.file = file
        self.KEY_PART1 = KEY_PART1
        self.KEY_PART2 = KEY_PART2
        self.RESULTS_PART1 = RESULTS_PART1
        self.RESULTS_PART2 = RESULTS_PART2
        self.data = []
        self._read_file()

    def _read_file(self) -> None:
        """
        Reads file and parses data.
        """
        with open(self.file) as file:
            self.data.extend(line.strip().split() for line in file)

    def solve_part_1(self) -> int:
        """
        Interprets the first column of data as the hand the opponent will play, and the second column as the hand you should play in response. Returns the total number of points the player will accumulate if they follow this plan.
        """
        my_points = 0
        for line in self.data:
            you = self.KEY_PART1[line[0]]
            me = self.KEY_PART1[line[-1]]
            my_points += self.RESULTS_PART1[(me, you)]

        return my_points

    def solve_part_2(self) -> int:
        """
        Interprets the first column of data as the hand the opponent will play, and the second column as the outcome. Returns the total number of points the player will accumulate if they follow this plan.
        """
        my_points = 0
        for line in self.data:
            you = self.KEY_PART2[line[0]]
            end = self.KEY_PART2[line[-1]]
            my_points += self.RESULTS_PART2[(you, end)]

        return my_points


if __name__ == "__main__":
    answer = Puzzle2("day_02/puzzle_2_data.txt")
    print("Solution to Puzzle 2 Part 1: ", answer.solve_part_1())
    print("Solution to Puzzle 2 Part 2: ", answer.solve_part_2())
