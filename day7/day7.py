import math
from statistics import median
from statistics import mean

def solve():
    numbers = [int(x) for x in open('input.txt').readline().split(",")]
    middle = median(numbers)
    distances = [abs(x - middle) for x in numbers]
    return sum(distances)


def solve2():
    numbers = [int(x) for x in open('input.txt').readline().split(",")]
    rounded_mean = math.floor(mean(numbers)) if mean(numbers) % 1 < .75 else round(mean(numbers))
    distances = [sum(range(abs(x - rounded_mean) + 1)) for x in numbers]
    return sum(distances)


if __name__ == "__main__":
    print(solve())
    print(solve2())
    