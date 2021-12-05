import re


def solve(part=1):
    lines = open('input.txt').readlines()
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in lines:
        groups = re.search(r"(?P<x1>\d+),(?P<y1>\d+)\s*->\s*(?P<x2>\d+),(?P<y2>\d+)", line)
        x1 = int(groups.group("x1"))
        x2 = int(groups.group("x2"))
        y1 = int(groups.group("y1"))
        y2 = int(groups.group("y2"))
        if x1 == x2:
            direction = range(y1, y2 + 1)
            if y1 > y2:
                direction = range(y2, y1 + 1)
            for i in direction:
                grid[x1][i] += 1
        elif y1 == y2:
            direction = range(x1, x2 + 1)
            if x1 > x2:
                direction = range(x2, x1 + 1)
            for i in direction:
                grid[i][y1] += 1
        elif part == 2:
            xiter = range(x1, x2 + 1)
            yiter = range(y1, y2 + 1)
            if y1 > y2:
                yiter = reversed(range(y2, y1 + 1))
            if x1 > x2:
                xiter = reversed(range(x2, x1 + 1))
            for i, j in zip(xiter, yiter):
                grid[i][j] += 1

    count_list = [sum(map(lambda x: x > 1, y)) for y in grid]
    return sum(count_list)


if __name__ == "__main__":
    print(solve())
    print(solve(2))
