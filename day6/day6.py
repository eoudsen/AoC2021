from fish import Fish


def solve():
    lines = open('input.txt').readlines()
    counters = [int(x) for x in lines[0].split(",")]
    fish_list = [Fish(x) for x in counters]
    for i in range(80):
        temp_fish_list = []
        for fish in fish_list:
            if fish.pass_day():
                temp_fish_list.append(Fish())
        for temp_fish in temp_fish_list:
            fish_list.append(temp_fish)
    return len(fish_list)


if __name__ == "__main__":
    print(solve())
