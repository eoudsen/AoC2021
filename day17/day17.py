import re


def solve():
    # print(abs(ymin) * abs(ymin + 1) // 2)
    xmin, xmax, ymin, ymax = map(int, re.findall(r"[-\d]+", open("input.txt").read()))
    total = 0
    for i in range(-xmin, xmax + 1):
        for j in range(ymin, -ymin + 1):
            found = False
            increase_x, increase_y = i, j
            x = y = 0
            max_y = 0
            while x < xmax and y > ymin:
                x += max(increase_x, 0)
                y += increase_y
                increase_x -= 1
                increase_y -= 1
                max_y = max(max_y, y)
                found = xmin <= x <= xmax and ymax >= y >= ymin
            if found:
                total = max(total, max_y)
    return total


def solve2():
    xmin, xmax, ymin, ymax = map(int, re.findall(r"[-\d]+", open("input.txt").read()))
    memo = set()
    for i in range(-xmin, xmax + 1):
        for j in range(ymin, -ymin + 1):
            increase_x, increase_y = i, j
            x = y = 0
            while x < xmax and y > ymin:
                x += max(increase_x, 0)
                y += increase_y
                increase_x -= 1
                increase_y -= 1
                if xmin <= x <= xmax and ymax >= y >= ymin:
                    memo.add((i, j))
    return len(memo)


if __name__ == "__main__":
    print(solve())
    print(solve2())
