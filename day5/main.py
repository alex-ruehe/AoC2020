from common.read import read_input
import math
from typing import Tuple, Union


def new_upper(lower: int, upper: int) -> int:
    diff = upper - lower
    half = math.floor(diff / 2)
    return lower + half


def new_lower(lower: int, upper: int) -> int:
    diff = upper - lower
    half = math.ceil(diff / 2)
    return lower + half


def search(sequence: str, lower: int, upper: int) -> Union[Tuple[str, int, int], int]:
    # print(f"Sequence: {sequence} - lower: {lower} - upper: {upper}")
    if len(sequence) > 1:
        if sequence[0] == "F" or sequence[0] == "L":
            return search(sequence[1:], lower, new_upper(lower, upper))
        return search(sequence[1:], new_lower(lower, upper), upper)
    if sequence == "F" or sequence == "L":
        return lower
    else:
        return upper


def part_1():
    puzzle_input_raw = read_input(5, 1)

    highest = 0
    pass_str = ""
    seat_ids = []
    for boarding_pass in puzzle_input_raw:
        row, column = boarding_pass[:-3], boarding_pass[-3:]
        row_number = search(row, 0, 127)
        column_number = search(column, 0, 7)

        seat_id = row_number * 8 + column_number
        seat_ids.append(seat_id)

        # print(
        #     f"{boarding_pass}: row {row_number}, column {column_number}, seat id {seat_id}"
        # )
        if seat_id > highest:
            highest = seat_id
            pass_str = boarding_pass

    print(f"{pass_str}: {highest}")

    return sorted(seat_ids)


if __name__ == "__main__":

    id_list = part_1()

    for i in range(1, len(id_list)):
        # print(id_list[i])
        diff = id_list[i] - id_list[i - 1]
        if diff > 1:
            print(f"{id_list[i-1]} - {id_list[i]}")
