
def solve():
    lines = open('input.txt').readlines()
    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        horizontal, depth, aim = accept_command(line, horizontal, depth, aim)
    return horizontal, depth


def accept_command(command, horizontal, depth, aim):
    cmd, val = command.split()
    if cmd == "forward":
        horizontal += int(val)
        depth += aim * int(val)
    elif cmd == "down":
        aim += int(val)
    elif cmd == "up":
        aim -= int(val)
    return horizontal, depth, aim


if __name__ == "__main__":
    hor, dep = solve()
    print(hor * dep)
