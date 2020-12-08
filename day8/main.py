from common.read import read_input


def get_instructions(raw_data):
    instructions = []
    for row in raw_data:
        operation, argument = row.split(" ")
        instructions.append((operation, int(argument)))
    return instructions


def parse_instructions(instructions):
    total = 0
    pos = 0
    executed = set()
    while True:
        try:
            current = instructions[pos]
            # print(f"Executing {current}")
            if pos in executed:
                print(f"Beginning of infinite loop at pos {pos}, acc: {total}")
                break
            executed.add(pos)
            if current[0] == "jmp":
                pos += current[1]
            elif current[0] == "acc":
                total += current[1]
                pos += 1
            else:
                pos += 1
        except IndexError as ierr:
            print(f"Finished with acc: {total}")
            return total, True
    return total, False


def part_1():
    raw_input = read_input(8, 1)
    instructions = get_instructions(raw_input)
    total, finished = parse_instructions(instructions)
    print(f"Finished: {finished}. Acc: {total}")


def part_2():
    raw_input = read_input(8, 1)
    instructions = get_instructions(raw_input)
    for i in range(0, len(instructions)):
        current = instructions[i]
        if current[0] == "jmp":
            tmp = ("nop", current[1])
        elif current[0] == "nop":
            tmp = ("jmp", current[1])
        else:
            continue

        instructions[i] = tmp
        total, finished = parse_instructions(instructions)
        if finished:
            print(total)
            exit(0)
        instructions[i] = current


if __name__ == "__main__":
    part_1()
    part_2()