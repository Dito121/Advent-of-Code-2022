class Solution:
    def __init__(self, file: str) -> None:
        """
        Reads the given file and returns the answer to Puzzle 3 from Advent of Code 2022.
        """
        if type(file) is not str or not file:
            raise TypeError("file must be a string.")

        self.file = file
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.key = {letters[i]: i + 1 for i in range(len(letters))}
        self._read_file()

    def _read_file(self) -> None:
        """
        Reads the file and strips each line as it is added to data.
        """
        with open(self.file, "r") as file:
            self.data = [line.strip() for line in file]

    def solve_part_1(self) -> int:
        """
        Iterates through the left half of data line by line and checks if each character is in the right half. Keeps track of associated value of characters that are found to be in both halves, break once found.
        """
        result = 0
        for i in range(len(self.data)):
            midpoint = len(self.data[i]) // 2
            left = self.data[i][:midpoint]
            right = set(self.data[i][midpoint:])

            for char in left:
                if char in right:
                    result += self.key[char]
                    break

        return result

    def solve_part_2(self) -> int:
        """
        For every three lines in self.data, finds the letter in all three by iterating through ith line and checking if each letter is in both i+1th line and i+2th line.
        """
        result = 0
        for line1, line2, line3 in zip(
            self.data[::3], self.data[1::3], self.data[2::3]
        ):
            for char in line1:
                if char in line2 and char in line3:
                    result += self.key[char]
                    break

        return result


if __name__ == "__main__":
    answer = Solution("day_03/puzzle_3_data.txt")
    print("Solution to Puzzle 3 Part 1: ", answer.solve_part_1())
    print("Solution to Puzzle 3 Part 2: ", answer.solve_part_2())
