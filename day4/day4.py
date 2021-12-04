from board import Board


def solve():
    lines = open('input.txt').readlines()
    numbers = [int(x) for x in lines[0].split(",")]
    boards = []
    line_counter = 2
    while True:
        boards.append(Board(lines[line_counter:line_counter+5]))
        line_counter += 6
        if line_counter >= len(lines):
            break

    for number in numbers:
        for board in boards:
            won, result = board.check_number(number)
            if won:
                return result


if __name__ == "__main__":
    print(solve())