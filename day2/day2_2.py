
def solve():
    lines = open('input.txt').readlines()
    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        horizontal, depth, aim = accept_command(line, horizontal, depth, aim)
    return horizontal, depth


def accept_command(command, horizontal, depth, aim):
    if command.startswith("forward"):
        horizontal += int(command.split(" ")[1])
        depth += aim * int(command.split(" ")[1])
    elif command.startswith("down"):
        aim += int(command.split(" ")[1])
    elif command.startswith("up"):
        aim -= int(command.split(" ")[1])
    return horizontal, depth, aim


if __name__ == "__main__":
    hor, dep = solve()
    print(hor * dep)
