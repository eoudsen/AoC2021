def solve():
    lines = open('input.txt').readlines()
    result = 0
    grid = [[int(x) for x in line.strip()] for line in lines]
    for _ in range(100):
        flashed = set()
        update_grid(grid)
        while any([any(x > 9 for x in grid[i]) for i in range(len(grid))]):
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] > 9 and (i, j) not in flashed:
                        flashed.add((i, j))
                        grid[i][j] = 0
                        for dx, dy in retrieve_neighbours(i, j, grid):
                            if (dx, dy) not in flashed:
                                grid[dx][dy] += 1
        result += len(flashed)
    return result


def retrieve_neighbours(x, y, grid):
    neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
    vals = []
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid[0]) and 0 <= nx < len(grid):
            vals.append((nx, ny))
    return vals


def update_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1


def solve2():
    lines = open('input.txt').readlines()
    counter = 0
    grid = [[int(x) for x in line.strip()] for line in lines]
    while True:
        flashed = set()
        update_grid(grid)
        while any([any(x > 9 for x in grid[i]) for i in range(len(grid))]):
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] > 9 and (i, j) not in flashed:
                        flashed.add((i, j))
                        grid[i][j] = 0
                        for dx, dy in retrieve_neighbours(i, j, grid):
                            if (dx, dy) not in flashed:
                                grid[dx][dy] += 1
        counter += 1
        if len(flashed) == 100:
            return counter


if __name__ == "__main__":
    print(solve())
    print(solve2())
