from common.read import read_input
from typing import List, Dict


def part_1() -> List[Dict]:
    passports = []

    puzzle_input_raw = read_input(4, 1)
    current = dict()
    for l in puzzle_input_raw:
        if l:
            entries = l.split(" ")
            for e in entries:
                k, v = e.split(":")
                current[k] = v
        else:
            passports.append(current)
            current = dict()
    passports.append(current)

    valid = [p for p in passports if len(p.keys()) == 8]

    missing_only_one = [p for p in passports if len(p.keys()) == 7]
    missing_only_cid = [p for p in missing_only_one if "cid" not in p]

    return valid + missing_only_cid


def is_valid(passport: Dict) -> bool:
    valid_fields = 0

    try:
        if 1920 <= int(passport["byr"]) <= 2002:
            valid_fields += 1
        if 2010 <= int(passport["iyr"]) <= 2020:
            valid_fields += 1
        if 2020 <= int(passport["eyr"]) <= 2030:
            valid_fields += 1
        if passport["hgt"].endswith("in"):
            if 59 <= int(passport["hgt"][:-2]) <= 76:
                valid_fields += 1
        elif passport["hgt"].endswith("cm"):
            if 150 <= int(passport["hgt"][:-2]) <= 193:
                valid_fields += 1
        if len(passport["pid"]) == 9:
            valid_fields += 1
        if passport["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
            valid_fields += 1
        if passport["hcl"].startswith("#"):
            if len(passport["hcl"]) == 7:
                valid_fields += 1

    except Exception as e:
        print(passport)
        print(e)
        return False
    if valid_fields == 7:
        return True
    return False


def part_2(passport_list: List[Dict]) -> List[Dict]:
    valid = []
    for passport in passport_list:
        if is_valid(passport):
            valid.append(passport)

    return valid


if __name__ == "__main__":
    valid = part_1()
    print(len(valid))
    cleaned_valid = part_2(valid)
    print(len(cleaned_valid))