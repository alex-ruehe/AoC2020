from common.read import read_input
import functools


def partition_input(raw_input):
    total = []
    current = []
    for row in raw_input:
        if row:
            current += list(row)
        else:
            total.append(current)
            current = []
    total.append(current)

    return total


def group_partition(raw_input):
    total = []
    current = []
    for row in raw_input:
        if row:
            current.append(set(row))
        else:
            common = functools.reduce(lambda x, y: x.intersection(y), current)
            total.append(common)
            current = []
    common = functools.reduce(lambda x, y: x.intersection(y), current)
    total.append(common)

    return total


def part_1():
    raw_input = read_input(6, 1)
    partitioned = partition_input(raw_input)
    count = 0
    for partition in partitioned:
        p_set = set(partition)
        count += len(p_set)
    print(count)


def part_2():
    raw_input = read_input(6, 1)
    grouped = group_partition(raw_input)
    total = 0
    for g in grouped:
        total += len(g)
    print(total)


if __name__ == "__main__":
    part_1()
    part_2()