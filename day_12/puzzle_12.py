class Solution:
    def __init__(self, file: str):
        self.file = file
        self.data = []
        values = "abcdefghijklmnopqrstuvwxyz"
        self.values = {values[i]: i for i in range(len(values))}
        self.read_file()

    def read_file(self):
        with open(self.file) as file:
            file = list(file.readlines())

            for i in range(len(file)):
                file[i] = file[i].strip()

                if "S" in file[i]:
                    self.start = [i, file[i].index("S")]
                    file[i] = file[i].replace("S", "a")

                if "E" in file[i]:
                    self.end = [i, file[i].index("E")]
                    file[i] = file[i].replace("E", "z")

                self.data.append(file[i])

    def find_value(self, row: int, col: int) -> int:
        if (
            row < 0
            or row >= len(self.data)
            or col < 0
            or col >= len(self.data)
            or (row, col) in self.path
        ):
            return -1
        self.path[(row, col)] = 1
        return self.values[self.data[row][col]]

    def find_diffs(self):
        curr = self.find_value(self.p_curr[0], self.p_curr[1])
        left = self.find_value(self.p_curr[0], self.p_curr[1] - 1)
        right = self.find_value(self.p_curr[0], self.p_curr[1] + 1)
        up = self.find_value(self.p_curr[0] - 1, self.p_curr[1])
        down = self.find_value(self.p_curr[0] + 1, self.p_curr[1])

        diffs = {}
        if left != -1:
            diffs["left"] = left - curr
        if right != -1:
            diffs["right"] = right - curr
        if up != -1:
            diffs["up"] = up - curr
        if down != -1:
            diffs["down"] = down - curr

        return dict(filter(lambda item: item[1] <= 1, diffs.items()))

    def assign_next_p_curr(self):
        diffs = self.find_diffs()
        print(diffs)
        nxt = max(diffs, key=diffs.get)

        if nxt == "left":
            self.p_curr[1] -= 1
        elif nxt == "right":
            self.p_curr[1] += 1
        elif nxt == "up":
            self.p_curr[0] -= 1
        elif nxt == "down":
            self.p_curr[0] += 1

    def solve_part_1(self):
        self.p_curr = self.start
        self.path = {}
        count = 0

        while self.p_curr != self.end:
            self.assign_next_p_curr()
            count += 1
            print("COUNT: ", count)

        return count
