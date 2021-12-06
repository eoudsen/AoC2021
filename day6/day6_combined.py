from collections import Counter


def solve(timers, days):
    counts = Counter(timers)

    for _ in range(days):
        sixes = 0
        eights = 0

        for i in range(9):
            if counts[i] == 0:
                continue

            if i == 0:
                sixes += counts[i]
                eights += counts[i]
            else:
                counts[i - 1] += counts[i]

            counts[i] = 0

        counts[6] += sixes
        counts[8] += eights

    return sum(counts.values())


if __name__ == "__main__":
    input_list = [int(x) for x in open("input.txt").readline().split(',')]
    print(solve(input_list, 80))
    print(solve(input_list, 256))
