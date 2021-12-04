
class Board:

    def __init__(self, input_lines):
        self.grid = [[int(i) for i in line.split()] for line in input_lines]
        self.markings = [[0 for _ in range(5)] for _ in range(5)]

    def check_number(self, number):
        if any(number in sublist for sublist in self.grid):
            return self.strike_number(number)
        return False, -1

    def strike_number(self, number):
        for i in range(5):
            for j in range(5):
                if self.grid[i][j] == number:
                    self.markings[i][j] = 1
                    return self.check_won(i, j, number)

    def check_won(self, i, j, number):
        if sum(self.markings[i]) == 5:
            return True, self.won(number)
        elif sum([x[j] for x in self.markings]) == 5:
            return True, self.won(number)
        return False, -1

    def won(self, number):
        for i in range(5):
            for j in range(5):
                if self.markings[i][j] == 1:
                    self.grid[i][j] = 0
        unchecked_markings = sum([sum(x) for x in self.grid])
        return unchecked_markings * number
