def read_input():
    data = []
    with open("input_day_1_puzzle_1.txt") as puzzle_input:
        for line in puzzle_input:
            data.append(line.strip())

    return data


if __name__ == "__main__":

    puzzle_input = read_input()
    puzzle_input = [int(e) for e in puzzle_input]

    # Puzzle 1 - The sum is supposed to be 2020, which means one of the numbers needs to be >= 1010

    upper = set([e for e in puzzle_input if e >= 1010])
    counter_part = [(2020 - e) for e in puzzle_input if e <= 1010]

    for e in counter_part:
        if e in upper:
            print(f"{e} + {2020-e} = 2020 - {e} * {2020-e} = {e * (2020-e)}")

    # Puzzle 2 - naive approach

    year = 2020
    parts = 3

    # at least one number needs to bee larger than 2020/3 = 673,3 = 674 (when talking about integers)
    first_number = set([e for e in puzzle_input if e >= int(year / 3)])
    # remainders contain the sum of the two missing numbers
    remainders = set([(year - e) for e in first_number])

    # for each of the remainders repeat the same procedure and try to find two numbers from
    # puzzle input that give the sum. Basically reiterate the approach from part 1
    for r in remainders:
        second_number = set([e for e in puzzle_input if e >= int(r / 2)])
        counter_part_3 = set([r - e for e in second_number])
        for e in counter_part_3:
            if e in puzzle_input:
                s1, s2 = e, r - e
                s3 = year - s1 - s2
                print(s1, s2, s3)
                print(s1 * s2 * s3)
                exit()