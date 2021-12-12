from graph import Graph


def solve():
    lines = open('input.txt').readlines()
    graph = Graph()
    for line in lines:
        cave1, cave2 = line.strip().split("-")
        if cave1 not in graph.get_caves():
            graph.add_cave(cave1)
        if cave2 not in graph.get_caves():
            graph.add_cave(cave2)
        graph.add_neighbour(cave1, cave2)
        graph.add_neighbour(cave2, cave1)

    result_set = set()
    path_search(graph, "start", [], result_set, True)
    return len(result_set)


def path_search(graph, curr_cave, path, paths, duplicate_small):
    path.append(curr_cave)
    if curr_cave == "end":
        paths.add(tuple(path))
        return
    for cave in graph.get_neighbours(curr_cave):
        if cave not in path and cave != "start":
            path_search(graph, cave, [x for x in path], paths, duplicate_small)
        elif not cave.islower():
            path_search(graph, cave, [x for x in path], paths, duplicate_small)
        elif not duplicate_small and cave != "start":
            path_search(graph, cave, [x for x in path], paths, True)


def solve2():
    lines = open('input.txt').readlines()
    graph = Graph()
    for line in lines:
        cave1, cave2 = line.strip().split("-")
        if cave1 not in graph.get_caves():
            graph.add_cave(cave1)
        if cave2 not in graph.get_caves():
            graph.add_cave(cave2)
        graph.add_neighbour(cave1, cave2)
        graph.add_neighbour(cave2, cave1)

    result_set = set()
    path_search(graph, "start", [], result_set, False)
    return len(result_set)


if __name__ == "__main__":
    print(solve())
    print(solve2())
