class Solution:
    def __init__(self, file: str):
        self.file = file
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.key = {letters[i]: i + 1 for i in range(len(letters))}
        self.read_file()

    def read_file(self):
        """
        read self.file and strip each line as it is added to self.data
        """
        with open(self.file, "r") as file:
            self.data = [line.strip() for line in file]

    def solve_part_1(self) -> int:
        self.sum = 0
        """
        iterate through the left half of self.data line by line and check
        if each character is in the right half.
        keep track of associated value of characters that are found to be
        in both halves, break once found
        """
        for i in range(len(self.data)):
            midpoint = len(self.data[i]) // 2
            right = self.data[i][midpoint:]

            for j in range(midpoint):
                if self.data[i][j] in right:
                    self.sum += self.key[self.data[i][j]]
                    break

        return self.sum

    def solve_part_2(self) -> int:
        self.sum = 0
        """
        for every three lines in self.data, find the letter in all
        three by iterating through line i and checking if letter
        is in both i+1 and i+2
        """
        for i in range(0, len(self.data), 3):
            for j in range(len(self.data[i])):
                if (
                    self.data[i][j] in self.data[i + 1]
                    and self.data[i][j] in self.data[i + 2]
                ):
                    self.sum += self.key[self.data[i][j]]
                    break

        return self.sum


answer = Solution("day_3/puzzle_3_data.txt")
print("Solution to Puzzle 3 Part 1: ", answer.solve_part_1())
print("Solution to Puzzle 3 Part 2: ", answer.solve_part_2())
