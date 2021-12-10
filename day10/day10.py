
def solve():
    lines = open('input.txt').readlines()
    total_value = 0
    for line in lines:
        total_value += run_line(line.strip())
    return total_value


def run_line(line):
    stack = []
    for token in line:
        if token == "<" or token == "{" or token == "[" or token == "(":
            stack.append(token)
        elif token == ">":
            if stack[-1] == "<":
                stack.pop(-1)
            else:
                return 25137
        elif token == "}":
            if stack[-1] == "{":
                stack.pop(-1)
            else:
                return 1197
        elif token == "]":
            if stack[-1] == "[":
                stack.pop(-1)
            else:
                return 57
        elif token == ")":
            if stack[-1] == "(":
                stack.pop(-1)
            else:
                return 3
    return 0


def solve2():
    lines = open('input.txt').readlines()
    score_list = []
    for line in lines:
        return_value = run_line2(line.strip())
        if return_value != 0:
            score_list.append(return_value)
    return sorted(score_list)[int(len(score_list) / 2)]


def run_line2(line):
    stack = []
    for token in line:
        if token == "<" or token == "{" or token == "[" or token == "(":
            stack.append(token)
        elif token == ">":
            if stack[-1] == "<":
                stack.pop(-1)
            else:
                return 0
        elif token == "}":
            if stack[-1] == "{":
                stack.pop(-1)
            else:
                return 0
        elif token == "]":
            if stack[-1] == "[":
                stack.pop(-1)
            else:
                return 0
        elif token == ")":
            if stack[-1] == "(":
                stack.pop(-1)
            else:
                return 0

    score = 0
    for token in stack[::-1]:
        score *= 5
        if token == "<":
            score += 4
        elif token == "{":
            score += 3
        elif token == "[":
            score += 2
        elif token == "(":
            score += 1

    return score


if __name__ == "__main__":
    print(solve())
    print(solve2())
