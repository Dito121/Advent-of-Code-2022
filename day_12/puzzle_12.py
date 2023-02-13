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

    def solve_part_1(self):
        return
