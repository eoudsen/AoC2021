from display import Display


def solve():
    lines = open('input.txt').readlines()
    answer = 0
    for line in lines:
        output = line.split("|")[1]
        output_digits = output.split()
        for digit in output_digits:
            if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                answer += 1
    return answer


def solve2():
    lines = open('input.txt').readlines()
    total = 0
    for line in lines:
        left_break, right_break = line.split("|")
        left_digits = left_break.split()
        right_digits = right_break.split()
        dis = Display(left_digits, right_digits)
        total += dis.result_number
    return total


if __name__ == "__main__":
    print(solve())
    print(solve2())
