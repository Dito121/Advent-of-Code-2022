import operator


class Monkey:
    def __init__(self, info):
        self.info = info
        self.name = int(self.info[0][1])
        self.items = list(map(int, self.info[1]))
        self.operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

        if len(self.info[2]) == 1:
            self.operation = [self.info[2][0]]
        else:
            self.operation = [self.info[2][0], int(self.info[2][1])]

        self.test = int(self.info[3][1])
        self.monkey_if_true = int(self.info[4][0])
        self.monkey_if_false = int(self.info[5][0])
        self.inspections = 0

    def __repr__(self):
        return f"Monkey{self.name}, items: {self.items}"

    def __str__(self):
        return f"Monkey{self.name}, items: {self.items}"

    def inspect_items(self):
        for x in range(len(self.items)):
            if len(self.operation) == 1:
                self.items[x] = (
                    self.operators[self.operation[0]](self.items[x], self.items[x]) // 3
                )
            else:
                self.items[x] = (
                    self.operators[self.operation[0]](self.items[x], self.operation[1])
                    // 3
                )
            self.inspections += 1

    def test_items(self):
        throw_to = []
        for x in range(len(self.items)):
            divisible = self.items[x] // self.test == 0
            throw_to.append(self.monkey_if_true if divisible else self.monkey_if_false)
        return throw_to
