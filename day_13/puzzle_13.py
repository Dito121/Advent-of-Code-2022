class Solution:
    def __init__(self, file: str):
        self.file = file
        self.read_file()

    def read_file(self):
        with open(self.file, "r") as file:
            file = file.readlines()

    def solve_part_1(self):
        return


if __name__ == "__main__":
    answer = Solution("day_13/puzzle_13_data.txt")
