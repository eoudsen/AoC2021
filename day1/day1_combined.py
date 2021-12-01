
def solve_part2(window_size):
    windows = []
    lines = open('input.txt').readlines()
    num_lines = [int(x) for x in lines]
    for i in range(len(num_lines) - (window_size - 1)):
        windows.append(sum(num_lines[i:i+window_size]))
    return solve_part1(windows)


def solve_part1(lines):
    last = lines[0]
    counter = 0
    for line in lines[1:]:
        counter = counter + 1 if int(line) > last else counter
        last = int(line)
    return counter


if __name__ == "__main__":
    print("Part 1:", solve_part1([int(x) for x in open('input.txt').readlines()]))
    print("Part 2:", solve_part2(3))
