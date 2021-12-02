
def solve():
    lines = open('input.txt').readlines()
    horizontal = 0
    depth = 0
    for line in lines:
        horizontal, depth = accept_command(line, horizontal, depth)
    return horizontal, depth


def accept_command(command, horizontal, depth):
    if command.startswith("forward"):
        horizontal += int(command.split(" ")[1])
    elif command.startswith("down"):
        depth += int(command.split(" ")[1])
    elif command.startswith("up"):
        depth -= int(command.split(" ")[1])
    return horizontal, depth


if __name__ == "__main__":
    hor, dep = solve()
    print(hor * dep)
