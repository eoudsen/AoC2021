from collections import Counter, defaultdict
import re


def solve():
    lines = open('input.txt').readlines()
    startingPolymer = lines[0].strip()
    rules = []
    for line in lines[2:]:
        before, between = line.strip().split(" -> ")
        rules.append((before, between))

    for _ in range(10):
        insert_dict = {}
        for rule in rules:
            create_rule = '(?=' + rule[0] + ')'
            fancy_list = [m.start() for m in re.finditer(create_rule, startingPolymer)]
            if len(fancy_list) > 0:
                for i in fancy_list:
                    insert_dict.update({i+1: rule[1]})
        sorted_dict = sorted(insert_dict.items(), reverse=True)
        for key, value in sorted_dict:
            startingPolymer = startingPolymer[:key] + value + startingPolymer[key:]

    counter = Counter(startingPolymer)
    lowest = 1000000000
    highest = 0
    for key, value in counter.items():
        if value < lowest:
            lowest = value
        if value > highest:
            highest = value

    return highest - lowest


def solve2():
    with open('input.txt') as f:
        template, rules = f.read().split('\n\n')
        template = template.strip()
        between = {}

        for rule in rules.split('\n'):
            pair, char = rule.split(' -> ')
            between[pair] = char

    n = len(template)
    pair_counts = defaultdict(int)
    single_counts = Counter(template)

    for i in range(1, n):
        pair_counts[template[i - 1] + template[i]] += 1

    for _ in range(40):
        new_pair_counts = defaultdict(int)

        for pair in list(pair_counts):
            if pair_counts[pair] == 0:
                continue

            if pair in between:
                single_counts[between[pair]] += pair_counts[pair]
                new_pair_counts[pair[0] + between[pair]] += pair_counts[pair]
                new_pair_counts[between[pair] + pair[1]] += pair_counts[pair]

        pair_counts = new_pair_counts

    return max(single_counts.values()) - min(single_counts.values())


if __name__ == "__main__":
    print(solve())
    print(solve2())
