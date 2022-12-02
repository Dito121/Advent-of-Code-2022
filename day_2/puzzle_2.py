class Solution:
    def __init__(self, file: str):
        self.file = file
        self.result = 0
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
        self.end = {"X": "lost", "Y": "draw", "Z": "won"}
        self.won = {"paper": "scissors", "rock": "paper", "scissors": "rock"}
        self.lost = {"paper": "rock", "rock": "scissors", "scissors": "paper"}

        with open(file) as file:
            self.lines = file.readlines()

    def solve_part_1(self) -> int:
        self.result = 0

        for line in self.lines:
            you = self.hand[line.strip()[0]]
            me = self.hand[line.strip()[-1]]

            if me == you:
                self.result += self.key["draw"] + self.key[me]
            elif me == "rock":
                if you == "paper":
                    self.result += self.key[me] + self.key["lost"]
                else:
                    self.result += self.key[me] + self.key["won"]
            elif me == "paper":
                if you == "scissors":
                    self.result += self.key[me] + self.key["lost"]
                else:
                    self.result += self.key[me] + self.key["won"]
            else:
                if you == "rock":
                    self.result += self.key[me] + self.key["lost"]
                else:
                    self.result += self.key[me] + self.key["won"]

        return self.result

    def solve_part_2(self) -> int:
        self.result = 0

        for line in self.lines:
            you = self.hand[line.strip()[0]]
            end = self.end[line.strip()[-1]]

            if end == "draw":
                self.result += self.key[end] + self.key[you]
            elif end == "lost":
                self.result += self.key[self.lost[you]] + self.key[end]
            else:
                self.result += self.key[self.won[you]] + self.key[end]

        return self.result


# answer = Solution("day_2/puzzle_2_data.txt")
# print("Solution to Puzzle 2 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 2 Part 2: ", answer.solve_part_2())
