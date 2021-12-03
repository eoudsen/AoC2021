
def solve():
    lines = open('input.txt').readlines()

    gamma_list = [get_most(lines, bit) for bit in range(len(lines[0].strip()))]
    gamma = int("".join([str(int(x)) for x in gamma_list]), 2)
    epsilon = int("".join([str(int(not x)) for x in gamma_list]), 2)

    return gamma * epsilon


def get_most(input_list, index):
    bit_list = [int(bit_number[index]) for bit_number in input_list]
    return sum(bit_list) >= len(input_list) / 2


if __name__ == "__main__":
    print(solve())
