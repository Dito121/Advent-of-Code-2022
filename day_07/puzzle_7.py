from anytree import Node, RenderTree


class Solution:
    def __init__(
        self,
        file: str,
        max_space: int = 70_000_000,
        space_needed: int = 30_000_000,
    ):
        self.file = file
        self.data = []
        self.max_space = max_space
        self.space_needed = space_needed
        self.part1 = 0

        self.read_file()
        self.create_tree()

    def read_file(self):
        with open(self.file) as file:
            self.data.extend(line.strip().split() for line in file)

    def show_tree(self):
        print(RenderTree(self.root))

    def create_children(self, p_right: int, p_current: Node) -> int:
        """
        Create a window from p_left to p_right that contains all files and
        directories in p_current.
        """
        p_right += 1
        p_left = p_right
        while self.data[p_right][0] != "$" and p_right < len(self.data) - 1:
            p_right += 1
        """
        Create nodes for each listed file and directory, set them as
        children of p_current.
        """
        for data in self.data[p_left:p_right]:
            if data[0] == "dir":
                Node(
                    data[1],
                    parent=p_current,
                    type="dir",
                    size=0,
                )
            else:
                node = Node(
                    data[1],
                    parent=p_current,
                    type="file",
                    size=int(data[0]),
                )
        return p_right  # return p_right or else won't register changes.

    def cd_to_child(self, p_right: int, p_current: Node):
        """
        Create list of names of all child nodes and find index within
        p_current.children so that we can cd into the correct child node.
        """
        children = [
            child.name[: len(self.data[p_right][2])] for child in p_current.children
        ]
        index = children.index(self.data[p_right][2])
        p_current = p_current.children[index]
        return p_current  # return p_current or else won't register changes.

    def create_tree(self):
        """
        Creates a tree using anytree library for Node creation and populates it when listing files and directories within the current directory pointer (p_current). Creates a window using a left pointer (p_left) and right pointer (p_right).
        """
        self.root = Node("root", type="dir", size=0)
        p_current = self.root
        p_right = 1

        while p_right < len(self.data):
            if self.data[p_right][0] == "break":
                break
            elif self.data[p_right][1] == "ls":
                p_right = self.create_children(p_right, p_current)

            elif self.data[p_right][1] == "cd":
                if self.data[p_right][2] == "..":
                    p_current = p_current.parent
                else:
                    p_current = self.cd_to_child(p_right, p_current)
                p_right += 1

    def solve_part_1(self, node: Node) -> int:
        dir_size = 0

        for child in node.children:
            if child.type == "dir":
                dir_size += self.solve_part_1(child)
            else:
                dir_size += child.size

        node.size = dir_size
        if dir_size <= 100000:
            self.part1 += dir_size
        return dir_size

    def solve_part_2(self) -> int:
        unused_space = self.max_space - self.root.size
        space_needed = self.space_needed - unused_space
        self.file_to_delete = self.root.size

        def traverse_tree(node: Node):
            for child in node.children:
                if child.type == "dir" and child.size >= space_needed:
                    self.file_to_delete = min(self.file_to_delete, child.size)
                    traverse_tree(child)

        traverse_tree(self.root)

        return self.file_to_delete


if __name__ == "__main__":
    answer = Solution("day_07/puzzle_7_data.txt")
    answer.solve_part_1(answer.root)
    print("Solution to Puzzle 7 Part 1: ", answer.part1)
    print("Solution to Puzzle 7 Part 2: ", answer.solve_part_2())
