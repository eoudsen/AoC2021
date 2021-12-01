file = None

def import_file():
    return open('input.txt')

def solve(file):
    print(file)


if __name__ == "__main__":
    file = import_file()
    solve(file)