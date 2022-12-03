class Solution:
    def __init__(self, file: str):
        self.left = ""
        self.right = ""
        self.sum = 0
        self.key = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
            "i": 9,
            "j": 10,
            "k": 11,
            "l": 12,
            "m": 13,
            "n": 14,
            "o": 15,
            "p": 16,
            "q": 17,
            "r": 18,
            "s": 19,
            "t": 20,
            "u": 21,
            "v": 22,
            "w": 23,
            "x": 24,
            "y": 25,
            "z": 26,
            "A": 27,
            "B": 28,
            "C": 29,
            "D": 30,
            "E": 31,
            "F": 32,
            "G": 33,
            "H": 34,
            "I": 35,
            "J": 36,
            "K": 37,
            "L": 38,
            "M": 39,
            "N": 40,
            "O": 41,
            "P": 42,
            "Q": 43,
            "R": 44,
            "S": 45,
            "T": 46,
            "U": 47,
            "V": 48,
            "W": 49,
            "X": 50,
            "Y": 51,
            "Z": 52,
        }

        with open(file, "r") as file:
            self.lines = [line.strip() for line in file]

    def solve_part_1(self) -> int:
        for i in range(len(self.lines)):
            midpoint = len(self.lines[i]) // 2
            right = self.lines[i][midpoint:]

            for j in range(midpoint):
                if self.lines[i][j] in right:
                    self.sum += self.key[self.lines[i][j]]
                    break

        return self.sum

    def solve_part_2(self) -> int:
        pass


# answer = Solution("day_3/puzzle_3_data.txt")
# print("Solution to Puzzle 3 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 3 Part 2: ", answer.solve_part_2())
