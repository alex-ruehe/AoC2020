from common.read import read_input

from itertools import islice


def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def check(nums, total):
    # print(f"Check if {sum} can be created by adding two out of {nums}")
    cleaned = sorted([n for n in nums if n < total])
    # print(f"Cleaned: {cleaned}")
    for n in cleaned:
        if (total - n) in cleaned:
            return
    print(f"Cannot find sum of {total} in {nums}")


def part_1():
    raw_input = read_input(9, 1)
    conv_input = [int(e) for e in raw_input]
    for sub in window(conv_input, 26):
        check(sub[:-1], sub[-1])


def part_2():
    total = 57195069
    raw_input = read_input(9, 1)
    conv_input = [int(e) for e in raw_input]

    for window_size in range(2, len(conv_input)):
        for w in window(conv_input, window_size):
            if sum(w) == total:
                print(min(w) + max(w))


if __name__ == "__main__":
    part_1()
    part_2()