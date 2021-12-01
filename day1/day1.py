
def solve():
    lines = open('input.txt').readlines()
    last = int(lines[0])
    counter = 0
    for line in lines[1:]:
        counter = counter + 1 if int(line) > last else counter
        last = int(line)
    return counter


if __name__ == "__main__":
    print(solve())
