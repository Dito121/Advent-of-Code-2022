class Solution:
    def __init__(self, file: str):
        self.file = file
        self.data = []
        self.unvisited = set()
        self.read_file()

    def read_file(self):
        letters = "abcdefghijklmnopqrstuvwxyz"
        values = {letters[i]: i for i in range(len(letters))}

        with open(self.file) as file:
            file = list(file.readlines())

            for row in range(len(file)):
                file[row] = file[row].strip()
                self.data.append([])

                if "S" in file[row]:
                    self.start = (row, file[row].index("S"))
                    file[row] = file[row].replace("S", "a")

                elif "E" in file[row]:
                    self.end = (row, file[row].index("E"))
                    file[row] = file[row].replace("E", "z")

                for col in range(len(file[row])):
                    self.unvisited.add((row, col))
                    self.data[row].append(values[file[row][col]])

    def calculate_distance(self):
        return

    def check_all_adjacent(self, row, col):
        unvisited = []

        if (row - 1, col) in self.unvisited:
            unvisited.append((row - 1, col))

        if (row + 1, col) in self.unvisited:
            unvisited.append((row + 1, col))

        if (row, col - 1) in self.unvisited:
            unvisited.append((row, col - 1))

        if (row, col + 1) in self.unvisited:
            unvisited.append((row, col + 1))

        for curr in unvisited:
            self.calculate_distance((row, col), curr)

    def solve_part_1(self):
        self.distances = [[None] * len(self.data[0])] * len(self.data)
        self.distances[self.start[0]][self.start[1]] = 0

        self.check_all_adjacent(self.start[0], self.start[1])

        return
