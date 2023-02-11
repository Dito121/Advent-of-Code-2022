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

    def calculate_distance(self, curr, adj):
        distance = self.data[adj[0]][adj[1]] - self.data[curr[0]][curr[1]]

        if distance > 1:
            return

        if self.distances[adj[0]][adj[1]] is None:
            self.distances[adj[0]][adj[1]] = self.distances[curr[0]][curr[1]] + 1
            return

        self.distances[adj[0]][adj[1]] = min(
            self.distances[adj[0]][adj[1]], self.distances[curr[0]][curr[1]] + 1
        )

    def check_all_adjacent(self, row, col):
        if (row - 1, col) in self.unvisited:
            self.calculate_distance((row, col), (row - 1, col))

        if (row + 1, col) in self.unvisited:
            self.calculate_distance((row, col), (row + 1, col))

        if (row, col - 1) in self.unvisited:
            self.calculate_distance((row, col), (row, col - 1))

        if (row, col + 1) in self.unvisited:
            self.calculate_distance((row, col), (row, col + 1))

        self.unvisited.remove((row, col))

    def solve_part_1(self):
        self.distances = [[None] * len(self.data[0])] * len(self.data)
        self.distances[self.start[0]][self.start[1]] = 0

        for row in range(len(self.data)):
            for col in range(len(self.data)):
                self.check_all_adjacent(row, col)

        return self.distances[self.end[0]][self.end[1]]
