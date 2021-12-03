
def solve():
    lines = open('input.txt').readlines()

    ox_gen_temp_list = [x.strip() for x in lines]
    for bit in range(len(lines[0].strip())):
        ox_gen_temp_list = [x for x in ox_gen_temp_list if int(x[bit]) == get_most(ox_gen_temp_list, bit)]
        if len(ox_gen_temp_list) == 1:
            break
    ox_gen = int(ox_gen_temp_list[0], 2)

    co_scrub_temp_list = [x.strip() for x in lines]
    for bit in range(len(lines[0].strip())):
        co_scrub_temp_list = [x for x in co_scrub_temp_list if int(x[bit]) != get_most(co_scrub_temp_list, bit)]
        if len(co_scrub_temp_list) == 1:
            break

    co_scrub = int(co_scrub_temp_list[0], 2)
    return ox_gen * co_scrub


def get_most(input_list, index):
    bit_list = [int(bit_number[index]) for bit_number in input_list]
    return int(sum(bit_list) >= len(input_list) / 2)


if __name__ == "__main__":
    print(solve())
