
def solve():
    lines = open('input.txt').readlines()
    horizontal = 0
    depth = 0
    for line in lines:
        horizontal, depth = accept_command(line, horizontal, depth)
    return horizontal, depth


def accept_command(command, horizontal, depth):
    cmd, val = command.split()
    if cmd == "forward":
        horizontal += int(val)
    elif cmd == "down":
        depth += int(val)
    elif cmd == "up":
        depth -= int(val)
    return horizontal, depth


if __name__ == "__main__":
    hor, dep = solve()
    print(hor * dep)
