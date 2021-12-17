from queue import PriorityQueue


def solve():
    lines = open('input.txt').readlines()
    grid = [[int(x) for x in line.strip()] for line in lines]
    dijkstra_grid = [[1000000000000 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dijkstra_grid[0][0] = 0
    dijkstraQueueueue(grid, dijkstra_grid)
    return dijkstra_grid[len(dijkstra_grid) - 1][len(dijkstra_grid[0]) - 1]


def dijkstraQueueueue(grid, dijkstra_grid):
    pq = PriorityQueue()
    pq.put((0, (0, 0)))
    visited = set()

    while not pq.empty():
        (dist, (x, y)) = pq.get()
        visited.add((x, y))

        for neighbour in retrieve_neighbours(x, y, grid):
            distance = grid[neighbour[0]][neighbour[1]]
            if (neighbour[0], neighbour[1]) not in visited:
                old_cost = dijkstra_grid[neighbour[0]][neighbour[1]]
                new_cost = dijkstra_grid[x][y] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbour))
                    dijkstra_grid[neighbour[0]][neighbour[1]] = new_cost


def retrieve_neighbours(x, y, grid):
    neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    vals = []
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid[0]) and 0 <= nx < len(grid):
            vals.append((nx, ny))
    return vals


def update_grid(some_grid):
    for x in range(len(some_grid)):
        for y in range(len(some_grid[x])):
            some_grid[x][y] += 1
            if some_grid[x][y] > 9:
                some_grid[x][y] = 1


def solve2():
    data = [list(map(int, line.strip())) for line in open('input.txt').readlines()]
    grid = [None] * (5 * len(data))
    for i in range(len(data)):
        for j in range(5):
            grid[len(data) * j + i] = data[i] * 5

    for i in range(5):
        for j in range(5):
            if i == j == 0:
                continue

            for k in range(len(data)):
                for l in range(len(data)):
                    x, y = i * len(data) + k, j * len(data) + l
                    grid[y][x] += (i + j)
                    if grid[y][x] > 9:
                        grid[y][x] -= 9

    dijkstra_grid = [[1000000000000 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dijkstra_grid[0][0] = 0
    dijkstraQueueueue(grid, dijkstra_grid)
    return dijkstra_grid[len(dijkstra_grid) - 1][len(dijkstra_grid[0]) - 1]


if __name__ == "__main__":
    print(solve())
    print(solve2())
