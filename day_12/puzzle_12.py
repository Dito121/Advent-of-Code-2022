import igraph as ig


class Solution:
    def __init__(self, file: str):
        self.file = file
        letters = "abcdefghijklmnopqrstuvwxyz"
        self.values = {letters[i]: i for i in range(len(letters))}
        self.values["S"] = 0
        self.values["E"] = 25
        self.read_file()

    def read_file(self):
        names, values, edges = [], [], []

        with open(self.file) as file:
            file = list(file.readlines())
            p_curr = 0
            vertices = len(file) * len(file[-1])

            for row in range(len(file)):
                file[row] = file[row].strip()

                for col in range(len(file[row])):
                    if file[row][col] == "S":
                        self.start = (row, col)

                    elif file[row][col] == "E":
                        self.end = (row, col)

                    if row != 0:
                        edges.append([p_curr, p_curr - len(file[row])])
                    if row != len(file) - 1:
                        edges.append([p_curr, p_curr + len(file[row])])
                    if col != 0:
                        edges.append([p_curr, p_curr - 1])
                    if col != len(file[row]) - 1:
                        edges.append([p_curr, p_curr + 1])

                    names.append(f"{row}, {col}")
                    values.append(self.values[file[row][col]])
                    p_curr += 1

        self.data = ig.Graph(n=vertices, edges=edges)
        self.data.vs["name"] = names
        self.data.vs["value"] = values

    def solve_part_1(self):
        print(self.data)
        return
