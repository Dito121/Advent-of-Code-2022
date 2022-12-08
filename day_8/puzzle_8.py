class Solution:
    def __init__(self, file: str):
        self.file = file
        self.data = []
        self.part1 = 0

        with open(self.file) as file:
            self.data.extend(list(map(int, line.strip())) for line in file)

    def solve_part_1(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                visible = {"up": True, "down": True, "left": True, "right": True}
                p_up = i - 1
                p_down = i + 1
                p_left = j - 1
                p_right = j + 1

                while p_up >= 0:
                    if self.data[p_up][j] < self.data[i][j]:
                        p_up -= 1
                        continue
                    visible["up"] = False
                    break

                while p_down < len(self.data):
                    if self.data[p_down][j] < self.data[i][j]:
                        p_down += 1
                        continue
                    visible["down"] = False
                    break

                while p_left >= 0:
                    if self.data[i][p_left] < self.data[i][j]:
                        p_left -= 1
                        continue
                    visible["left"] = False
                    break

                while p_right < len(self.data[i]):
                    if self.data[i][p_right] < self.data[i][j]:
                        p_right += 1
                        continue
                    visible["right"] = False
                    break

                if True in visible.values():
                    self.part1 += 1
        return self.part1

    def solve_part_2(self):
        pass


answer = Solution("day_8/puzzle_8_data.txt")
print("Solution to Puzzle 8 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 8 Part 2: ", answer.solve_part_2())
