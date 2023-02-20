HAND = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}
KEY = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "lost": 0,
    "draw": 3,
    "won": 6,
}
END = {
    "X": "lost",
    "Y": "draw",
    "Z": "won",
}
WON = {
    "paper": "scissors",
    "rock": "paper",
    "scissors": "rock",
}
LOST = {
    "paper": "rock",
    "rock": "scissors",
    "scissors": "paper",
}


class Puzzle2:
    def __init__(
        self,
        file: str,
        hand: dict = HAND,
        key: dict = KEY,
        end: dict = END,
        won: dict = WON,
        lost: dict = LOST,
    ) -> None:
        self.file = file
        self.hand = hand
        self.key = key
        self.end = end
        self.won = won
        self.lost = lost
        self.data = []
        self._read_file()

    def _read_file(self) -> None:
        """
        Reads file and parses data.
        """
        with open(self.file) as file:
            self.data.extend(line.strip().split() for line in file)

    def _get_result(self, me: str, you: str) -> int:
        """
        Returns points won during each game for part 1 only.
        """
        result = 0
        if me == you:
            result += self.key["draw"] + self.key[me]
        elif me == "rock":
            if you == "paper":
                result += self.key[me] + self.key["lost"]
            else:
                result += self.key[me] + self.key["won"]
        elif me == "paper":
            if you == "scissors":
                result += self.key[me] + self.key["lost"]
            else:
                result += self.key[me] + self.key["won"]
        else:
            if you == "rock":
                result += self.key[me] + self.key["lost"]
            else:
                result += self.key[me] + self.key["won"]
        return result

    def solve_part_1(self) -> int:
        """
        Interprets the first column of data as the hand the opponent will play, and the second column as the hand you should play in response. Returns the total number of points the player will accumulate if they follow this plan.
        """
        my_points = 0
        for line in self.data:
            you = self.hand[line[0]]
            me = self.hand[line[-1]]
            my_points += self._get_result(me, you)

        return my_points

    def solve_part_2(self) -> int:
        """
        Interprets the first column of data as the hand the opponent will play, and the second column as the outcome. Returns the total number of points the player will accumulate if they follow this plan.
        """
        my_points = 0
        for line in self.data:
            you = self.hand[line[0]]
            end = self.end[line[-1]]

            if end == "draw":
                my_points += self.key[end] + self.key[you]
            elif end == "lost":
                my_points += self.key[self.lost[you]] + self.key[end]
            else:
                my_points += self.key[self.won[you]] + self.key[end]

        return my_points


if __name__ == "__main__":
    answer = Puzzle2("day_02/puzzle_2_data.txt")
    print("Solution to Puzzle 2 Part 1: ", answer.solve_part_1())
    print("Solution to Puzzle 2 Part 2: ", answer.solve_part_2())
