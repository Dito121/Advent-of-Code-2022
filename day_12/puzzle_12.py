import igraph as ig
import matplotlib.pyplot as plt


class Solution:
    def __init__(self, file: str):
        self.file = file
        letters = "abcdefghijklmnopqrstuvwxyz"
        self.values = {letters[i]: i for i in range(len(letters))}
        self.values["S"] = 0
        self.values["E"] = 25
        self.read_file()

    def add_edges(self, row, col, p_curr, width, length):
        new_edges = []

        if row != length - 1:
            new_edges.append([p_curr, p_curr + width])
        if col != width - 1:
            new_edges.append([p_curr, p_curr + 1])

        return new_edges

    def create_graph(self, vertices, edges, names, values):
        self.unvisited = set(names)
        self.data = ig.Graph(n=vertices, edges=edges)
        self.data.vs["name"] = names
        self.data.vs["value"] = values
        self.reset_graph_distances()

    def reset_graph_distances(self):
        self.data.vs["distance"] = [None] * self.data.vcount()

    def read_file(self):
        names, values, edges = [], [], []

        with open(self.file) as file:
            file = list(file.readlines())
            vertices = len(file) * len(file[-1])
            self.all_lowest = []
            p_curr = 0

            for row in range(len(file)):
                file[row] = file[row].strip()

                for col in range(len(file[row])):
                    if file[row][col] == "S":
                        self.start = (row, col)
                        self.all_lowest.append((row, col))
                    elif file[row][col] == "E":
                        self.end = (row, col)
                    elif file[row][col] == "a":
                        self.all_lowest.append((row, col))

                    edges.extend(
                        self.add_edges(row, col, p_curr, len(file[row]), len(file))
                    )

                    names.append((row, col))
                    values.append(self.values[file[row][col]])
                    p_curr += 1

        self.create_graph(vertices, edges, names, values)

    def get_unvisited(self):
        return self.unvisited.copy()

    def plot_data(self):
        layout = self.data.layout("kk")
        fig, ax = plt.subplots()
        self.data.vs["label"] = self.data.vs["name"]
        ig.plot(self.data, layout=layout, target=ax)
        plt.show()

    def solve_part_1(self, start=None):
        if start is None:
            start = self.data.vs.find(name=self.start)
        else:
            start = self.data.vs.find(name=start)

        unvisited = self.get_unvisited()
        start["distance"] = 0
        queue = [start]

        while queue:
            p_curr = queue.pop(0)

            if p_curr["name"] not in unvisited:
                continue
            if p_curr["name"] == self.end:
                return p_curr["distance"]

            neighbors = self.data.neighborhood(p_curr, 1)

            for neighbor in neighbors:
                neighbor = self.data.vs.find(neighbor)

                if (
                    neighbor["name"] not in unvisited
                    or neighbor["value"] - p_curr["value"] > 1
                ):
                    continue

                if neighbor["distance"] is None:
                    neighbor["distance"] = p_curr["distance"] + 1
                else:
                    neighbor["distance"] = min(
                        neighbor["distance"], p_curr["distance"] + 1
                    )

                queue.append(neighbor)

            unvisited.remove(p_curr["name"])

    def solve_part_2(self):
        result = self.data.vs.find(name=self.end)["distance"]

        for lowest in self.all_lowest:
            self.reset_graph_distances()
            if res := self.solve_part_1(start=lowest):
                result = min(result, res)

        return result


if __name__ == "__main__":
    answer = Solution("day_12/puzzle_12_data.txt")
    print("Solution to Puzzle 12 Part 1: ", answer.solve_part_1())
    print("Solution to Puzzle 12 Part 2: ", answer.solve_part_2())
    # answer.plot_data()
