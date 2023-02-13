class Solution:
    def __init__(self, file: str):
        self.file = file
        self.hand = {
            "A": "rock",
            "B": "paper",
            "C": "scissors",
            "X": "rock",
            "Y": "paper",
            "Z": "scissors",
        }
        self.key = {
            "rock": 1,
            "paper": 2,
            "scissors": 3,
            "lost": 0,
            "draw": 3,
            "won": 6,
        }
        self.end = {
            "X": "lost",
            "Y": "draw",
            "Z": "won",
        }
        self.won = {
            "paper": "scissors",
            "rock": "paper",
            "scissors": "rock",
        }
        self.lost = {
            "paper": "rock",
            "rock": "scissors",
            "scissors": "paper",
        }
        self.read_file()

    def read_file(self):
        self.data = []
        """
        read file line by line and append split line into self.data
        """
        with open(self.file) as file:
            self.data.extend(line.strip().split() for line in file)

    def solve_part_1(self) -> int:
        my_points = 0
        """
        this function interprets the first column of self.data as the hand
        the opponent will play, and the second column as the hand you should
        play in response.
        my_points will track the total number of points the player will
        accumulate if they follow this plan.
        """
        for line in self.data:
            you = self.hand[line[0]]
            me = self.hand[line[-1]]

            if me == you:
                my_points += self.key["draw"] + self.key[me]
            elif me == "rock":
                if you == "paper":
                    my_points += self.key[me] + self.key["lost"]
                else:
                    my_points += self.key[me] + self.key["won"]
            elif me == "paper":
                if you == "scissors":
                    my_points += self.key[me] + self.key["lost"]
                else:
                    my_points += self.key[me] + self.key["won"]
            else:
                if you == "rock":
                    my_points += self.key[me] + self.key["lost"]
                else:
                    my_points += self.key[me] + self.key["won"]

        return my_points

    def solve_part_2(self) -> int:
        my_points = 0
        """
        this function interprets the first column of self.data as the hand
        the opponent will play, and the second column as the outcome.
        my_points will track the total number of points the player will
        accumulate if they follow this plan.
        """
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


answer = Solution("day_02/puzzle_2_data.txt")
print("Solution to Puzzle 2 Part 1: ", answer.solve_part_1())
print("Solution to Puzzle 2 Part 2: ", answer.solve_part_2())
