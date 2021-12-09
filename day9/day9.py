from math import prod


def retrieve_neighbors(x, y, grid):
    neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    vals = []
    for dx, dy in neighbors:
        nx, ny = x+dx, y+dy
        if 0 <= ny < len(grid[0]) and 0 <= nx < len(grid):
            vals.append((nx, ny))
    return vals


def breadth_first_search(x, y, grid, visited):
    visited.add((x, y))
    for dx, dy in set(retrieve_neighbors(x, y, grid)) - visited:
        if grid[dx][dy] == 9:
            continue
        visited.add((dx, dy))
        visited |= breadth_first_search(dx, dy, grid, visited)
    return visited


def solve():
    lines = open('input.txt').readlines()
    risk = 0
    grid = [[int(x) for x in line.strip()] for line in lines]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            curr_val = grid[i][j]
            if i < len(grid) - 1 and grid[i+1][j] <= curr_val:
                continue
            if i > 0 and grid[i-1][j] <= curr_val:
                continue
            if j > 0 and grid[i][j-1] <= curr_val:
                continue
            if j < len(grid[i]) - 1 and grid[i][j+1] <= curr_val:
                continue
            risk += curr_val + 1
    return risk


def solve2():
    lines = open('input.txt').readlines()
    grid = [[int(x) for x in line.strip()] for line in lines]
    visited = set()
    basins = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 9 or (i, j) in visited:
                continue
            basin = breadth_first_search(i, j, grid, set())
            visited |= basin
            basins.add(tuple(sorted(basin)))
    return prod(sorted([len(x) for x in basins])[::-1][:3])


if __name__ == "__main__":
    print(solve())
    print(solve2())
