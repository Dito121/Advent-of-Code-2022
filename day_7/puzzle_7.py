from anytree import Node, RenderTree


class Solution:
    def __init__(self, file: str):
        self.file = file
        self.data = []
        self.part1 = 0

        with open(self.file) as file:
            self.data.extend(line.strip().split() for line in file)
        self.root = Node("root", type="dir")
        p_current = self.root

        p_right = 1
        while p_right < len(self.data):
            if self.data[p_right][0] == "break":
                break

            elif self.data[p_right][1] == "ls":
                p_right += 1
                p_left = p_right
                while self.data[p_right][0] != "$" and p_right < len(self.data) - 1:
                    p_right += 1

                for data in self.data[p_left:p_right]:
                    if data[0] == "dir":
                        Node(data[1], parent=p_current, type="dir")
                    else:
                        node = Node(
                            data[1],
                            parent=p_current,
                            type="file",
                            size=int(data[0]),
                        )
                continue

            elif self.data[p_right][1] == "cd":
                if self.data[p_right][2] == "..":
                    p_current = p_current.parent

                else:
                    children = [
                        child.name[: len(self.data[p_right][2])]
                        for child in p_current.children
                    ]
                    index = children.index(self.data[p_right][2])
                    p_current = p_current.children[index]

                p_right += 1

        # print(RenderTree(self.root))  # use this to see tree

    def solve_part_1(self, node):
        part1 = 0

        for child in node.children:
            if child.type == "dir":
                part1 += self.solve_part_1(child)
            else:
                part1 += child.size

        if part1 <= 100000:
            self.part1 += part1

        return part1

    def solve_part_2(self):
        pass


# answer = Solution("day_7/puzzle_7_data.txt")
# print("Solution to Puzzle 7 Part 1: ", answer.solve_part_1(answer.root))
# print("Solution to Puzzle 7 Part 2: ", answer.solve_part_2())
