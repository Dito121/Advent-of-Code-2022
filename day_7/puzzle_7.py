from anytree import Node, RenderTree


class Solution:
    def __init__(self, file: str):
        self.file = file
        self.data = []
        self.size = 0

        with open(self.file) as file:
            self.data.extend(line.strip().split() for line in file)
        self.root = Node(self.data[0][2], type="dir")
        p_current = self.root

        p_right = 1
        while p_right < len(self.data):
            print(p_right, p_current)
            if self.data[p_right][0] == "$":
                if self.data[p_right][1] == "ls":
                    p_right += 1
                    p_left = p_right
                    while self.data[p_right][0] != "$" and p_right < len(self.data):
                        p_right += 1

                    for data in self.data[p_left:p_right]:
                        if data[0] == "dir":
                            node = Node(data[1], parent=p_current, type="dir")
                        else:
                            Node(
                                data[1],
                                parent=p_current,
                                type="file",
                                size=int(data[0]),
                            )
                            self.size += int(data[0])

                elif self.data[p_right][1] == "cd":
                    if self.data[p_right][2] == "..":
                        p_current = p_current.parent
                        p_right += 1
                        continue

                    p_current = filter(
                        lambda node: node.name[-len(p_current.name) :]
                        == self.data[p_right][2],
                        p_current.children,
                    )

            p_right += 1

            # for pre, fill, node in RenderTree(self.root):
            #     print(f"{pre}{node.name}")

    def solve_part_1(self):
        return self.size

    def solve_part_2(self):
        pass


# answer = Solution("day_7/puzzle_7_data.txt")
# print("Solution to Puzzle 7 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 7 Part 2: ", answer.solve_part_2())


"""
class Dir:
    def __init__(self, name: str):
        if files is None:
            files = []

        self.name = name

    def __str__(self):
        return f"{self.name} (dir)"


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.name} (file, size={self.size})"
"""
