
def create_windows(window_size):
    windows = []
    lines = open('input.txt').readlines()
    num_lines = [int(x) for x in lines]
    for i in range(len(num_lines) - (window_size - 1)):
        windows.append(sum(num_lines[i:i+window_size]))
    return windows


def solve(windows):
    last = windows[0]
    counter = 0
    for line in windows[1:]:
        counter = counter + 1 if int(line) > last else counter
        last = int(line)
    return counter


if __name__ == "__main__":
    wins = create_windows(3)
    print(solve(wins))
