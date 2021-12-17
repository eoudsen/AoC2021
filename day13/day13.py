import matplotlib.pyplot as plt


def solve():
    lines = open('input.txt').readlines()
    points = set()
    counter = 0
    while len(lines[counter]) > 1:
        x, y = lines[counter].strip().split(",")
        points.add((int(x), int(y)))
        counter += 1

    counter += 1

    folds = []
    while len(lines[counter]) > 1 and counter < len(lines) - 1:
        axis, line = lines[counter].split("=")
        axis = axis.split()[-1]
        line = int(line)
        folds.append((axis, line))
        counter += 1

    fold(folds[0], points)
    return len(points)


def fold(the_fold, points):
    if the_fold[0] == "x":
        fold_x(the_fold, points)
    else:
        fold_y(the_fold, points)


def fold_x(the_fold, points):
    iterate_set = set()
    for point in points:
        iterate_set.add(point)
    for point in iterate_set:
        if point[0] > the_fold[1]:
            new_point = (point[0] - ((point[0] - the_fold[1]) * 2), point[1])
            points.remove(point)
            points.add(new_point)


def fold_y(the_fold, points):
    iterate_set = set()
    for point in points:
        iterate_set.add(point)
    for point in iterate_set:
        if point[1] > the_fold[1]:
            new_point = (point[0], point[1] - ((point[1] - the_fold[1]) * 2))
            points.remove(point)
            points.add(new_point)


def solve2():
    lines = open('input.txt').readlines()
    points = set()
    counter = 0
    while len(lines[counter]) > 1:
        x, y = lines[counter].strip().split(",")
        points.add((int(x), int(y)))
        counter += 1
    counter += 1

    folds = []
    while counter < len(lines) and len(lines[counter]) > 1:
        axis, line = lines[counter].split("=")
        axis = axis.split()[-1]
        line = int(line)
        folds.append((axis, line))
        counter += 1
    for foldi in folds:
        fold(foldi, points)

    point_list = []
    for point in points:
        point_list.append(point)

    xs, ys = zip(*point_list)
    ys = [-1 * y for y in ys]
    plt.scatter(xs, ys)
    plt.show()


if __name__ == "__main__":
    print(solve())
    print(solve2())
