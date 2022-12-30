class Solution:
    def __init__(self, file: str):
        self.file = file
        self.data = []
        self.part1 = 0
        self.part2 = 0
        self.read_file()

    def read_file(self):
        with open(self.file) as file:
            self.data.extend(list(map(int, line.strip())) for line in file)

    def scan_up_part1(self, i, j, p_up, visible):
        while p_up >= 0:
            if self.data[p_up][j] < self.data[i][j]:
                p_up -= 1
                continue
            visible["up"] = False
            break
        return visible

    def scan_down_part1(self, i, j, p_down, visible):
        while p_down < len(self.data):
            if self.data[p_down][j] < self.data[i][j]:
                p_down += 1
                continue
            visible["down"] = False
            break
        return visible

    def scan_left_part1(self, i, j, p_left, visible):
        while p_left >= 0:
            if self.data[i][p_left] < self.data[i][j]:
                p_left -= 1
                continue
            visible["left"] = False
            break
        return visible

    def scan_right_part1(self, i, j, p_right, visible):
        while p_right < len(self.data[i]):
            if self.data[i][p_right] < self.data[i][j]:
                p_right += 1
                continue
            visible["right"] = False
            break
        return visible

    def scan_four_directions_part1(self, i, j):
        visible = {"up": True, "down": True, "left": True, "right": True}

        visible = self.scan_up_part1(i, j, i - 1, visible)
        visible = self.scan_down_part1(i, j, i + 1, visible)
        visible = self.scan_left_part1(i, j, j - 1, visible)
        visible = self.scan_right_part1(i, j, j + 1, visible)

        if True in visible.values():
            self.part1 += 1

    def solve_part_1(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.scan_four_directions_part1(i, j)
        return self.part1

    def scan_up_part2(self, i, j, p_up, visible):
        while p_up >= 0:
            if self.data[p_up][j] >= self.data[i][j]:
                visible["up"] += 1
                break
            p_up -= 1
            visible["up"] += 1
        return visible

    def scan_down_part2(self, i, j, p_down, visible):
        while p_down < len(self.data):
            if self.data[p_down][j] >= self.data[i][j]:
                visible["down"] += 1
                break
            p_down += 1
            visible["down"] += 1
        return visible

    def scan_left_part2(self, i, j, p_left, visible):
        while p_left >= 0:
            if self.data[i][p_left] >= self.data[i][j]:
                visible["left"] += 1
                break
            p_left -= 1
            visible["left"] += 1
        return visible

    def scan_right_part2(self, i, j, p_right, visible):
        while p_right < len(self.data[i]):
            if self.data[i][p_right] >= self.data[i][j]:
                visible["right"] += 1
                break
            p_right += 1
            visible["right"] += 1
        return visible

    def scan_four_directions_part2(self, i, j):
        visible = {"up": 0, "down": 0, "left": 0, "right": 0}

        visible = self.scan_up_part2(i, j, i - 1, visible)
        visible = self.scan_down_part2(i, j, i + 1, visible)
        visible = self.scan_left_part2(i, j, j - 1, visible)
        visible = self.scan_right_part2(i, j, j + 1, visible)

        product = 1
        for num in list(visible.values()):
            product *= num
        self.part2 = max(product, self.part2)

    def solve_part_2(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.scan_four_directions_part2(i, j)

        return self.part2


answer = Solution("day_8/puzzle_8_data.txt")
print("Solution to Puzzle 8 Part 1: ", answer.solve_part_1())
print("Solution to Puzzle 8 Part 2: ", answer.solve_part_2())
