from functools import reduce
from timeit import default_timer as timer

from common.read import read_input


def part_1(step_x=3, step_y=1):
    raw_input = read_input(3, 1)

    x = 0
    y = 0

    pos_x = 0
    pos_y = 0

    trees = 0

    mod = len(raw_input[0])

    while pos_y < len(raw_input):
        row = raw_input[pos_y]
        field = row[pos_x % len(row)]

        if field == "#":
            trees += 1

        pos_x += step_x
        pos_y += step_y

    return trees


def part_2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    counts = []
    start = timer()

    for slope in slopes:
        x, y = slope
        counts.append(part_1(x, y))
    print(timer() - start)
    return reduce(lambda x, y: x * y, counts)


if __name__ == "__main__":
    print(part_1())
    print(part_2())