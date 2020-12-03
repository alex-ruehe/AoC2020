from typing import List

RESOURCES_FOLDER = "../resources/"


def read_input(day: int, puzzle: int) -> List[str]:
    filename = f"{RESOURCES_FOLDER}/input_day_{day}_puzzle_{puzzle}.txt"
    data = []
    with open(filename) as puzzle_input:
        for line in puzzle_input:
            data.append(line.strip())

    return data
