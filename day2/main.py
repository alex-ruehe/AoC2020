from collections import Counter
from typing import List, Tuple

from common.read import read_input


def parse_password_row(row: str) -> Tuple[int, int, str, str]:
    policy, password = row.split(":")
    count, character = policy.split(" ")
    minimum, maximum = count.split("-")
    password = password.strip()

    return int(minimum), int(maximum), character, password


def part_1():
    passwords = read_input(2, 1)
    valid = []
    for password in passwords:
        minimum, maximum, character, p = parse_password_row(password)

        letter_counts = Counter(p)
        if int(minimum) <= letter_counts[character] <= int(maximum):
            valid.append(password)

    print(len(valid))


def part_2():
    """
    Note: For this task, pos1 and pos2 are not 0-based position in the string, that's why the -1
    """
    passwords = read_input(2, 1)
    valid = []
    for password in passwords:
        pos1, pos2, character, p = parse_password_row(password)
        # pos1 and pos2 are not allowed to be identical according to password policy
        if (p[pos1 - 1] != p[pos2 - 1]) and (
            # either pos1 or pos2 needs to be the character
            p[pos1 - 1] == character
            or p[pos2 - 1] == character
        ):
            valid.append(password)

    print(len(valid))


part_1()
part_2()