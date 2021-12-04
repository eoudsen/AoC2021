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

    marked_boards = [1 for _ in boards]
    for number in numbers:
        for i in range(len(boards)):
            if marked_boards[i] == 0:
                continue
            won, result = boards[i].check_number(number)
            if won:
                if sum(marked_boards) == 1:
                    return result
                marked_boards[i] = 0


if __name__ == "__main__":
    print(solve())
