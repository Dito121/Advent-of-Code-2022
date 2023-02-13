class Solution:
    def __init__(self, file: str):
        """
        Read the file using read_file() method.
        """
        self.file = file
        self.read_file()

    def read_file(self):
        """
        Read the file.
        """
        self.data = ""
        with open(self.file) as file:
            for line in file:
                self.data += line.strip()

    def start_of_packet_marker(self, n: int):
        seen = ""
        """
        Find index where previous n letters are unique.
        """
        for i in range(len(self.data)):
            if self.data[i] not in seen:
                seen += self.data[i]
                if len(seen) == n:
                    return i + 1
                continue

            j = seen.index(self.data[i])
            seen = seen[j + 1 :] + self.data[i]

    def solve_part_1(self) -> int:
        return self.start_of_packet_marker(4)

    def solve_part_2(self) -> int:
        return self.start_of_packet_marker(14)


answer = Solution("day_06/puzzle_6_data.txt")
print("Solution to Puzzle 6 Part 1: ", answer.solve_part_1())
print("Solution to Puzzle 6 Part 2: ", answer.solve_part_2())
