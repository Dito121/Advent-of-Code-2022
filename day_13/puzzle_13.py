from ast import literal_eval


class Solution:
    def __init__(self, file: str):
        self.file = file
        self.left = []
        self.right = []
        self.read_file()

    def read_file(self):
        with open(self.file, "r") as file:
            file = file.readlines()

            for i in range(len(file)):
                remainder = i % 3
                if remainder == 0:
                    self.left.append(literal_eval(file[i].strip()))
                elif remainder == 1:
                    self.right.append(literal_eval(file[i].strip()))

    def compare_lists(self, left, right):
        for i in range(len(left)):
            if left[i] > right[i]:
                return False

        return True

    def compare_ints(self, left, right):
        if left < right:
            return True
        return False

    def solve_part_1(self):
        self.right_order = 0

        for i in range(len(self.left)):
            if type(self.left[i]) == type(self.right[i]) == list:
                if not self.compare_lists(self.left[i], self.right[i]):
                    continue
                self.right_order += 1

            elif type(self.left[i]) == type(self.right) == int:
                if not self.compare_ints(self.left[i], self.right[i]):
                    continue
                self.right_order += 1

        return self.right_order

    def solve_part_2(self):
        return


if __name__ == "__main__":
    answer = Solution("day_13/puzzle_13_data.txt")
    print(answer.solve_part_1())
    # print(answer.solve_part_2())
