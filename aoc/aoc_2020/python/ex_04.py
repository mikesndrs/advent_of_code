"""https://adventofcode.com/2020/day/04"""

from typing import Dict, List

PASSPORT = Dict[str, str]

keys = set(
    [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]
)

optional_keys = set(
    [
        "cid",
    ]
)

eye_colors = set(
    [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    ]
)


def handle_input(input_filename: str) -> List[PASSPORT]:
    """Create dictionary objects for passports from raw input"""
    passport_data = []
    with open(input_filename, "r") as f:
        for line in f.read().split("\n\n"):
            passport = line.strip().replace("\n", " ")
            passport_dict = {
                x.split(":")[0]: x.split(":")[1] for x in passport.split(" ")
            }
            passport_data.append(passport_dict)
    return passport_data


def main_func(input_filename: str, version: int) -> int:
    """Count number of valid passports"""
    passport_data = handle_input(input_filename)
    res = 0
    for passport in passport_data:
        my_bool = check_validations(passport, version)
        if my_bool:
            res += 1
    print(res)
    return res


def check_validations(passport: PASSPORT, version: int) -> bool:
    """Check if given passport adheres to validation rules"""
    validations = [
        len(keys - set(passport.keys())) == 0,
    ]
    if not all(validations):
        return False
    if version == 1:
        return True

    try:
        byr = int(passport["byr"])
        iyr = int(passport["iyr"])
        eyr = int(passport["eyr"])
        hgt = passport["hgt"]
        hcl = passport["hcl"]
        ecl = passport["ecl"]
        pid = passport["pid"]
    except (KeyError, ValueError):
        return False

    validations += [
        1920 <= byr <= 2002,
        2010 <= iyr <= 2020,
        2020 <= eyr <= 2030,
    ]
    if hgt.endswith("cm"):
        validations += [
            150 <= int(hgt[:-2]) <= 193,
        ]
    elif hgt.endswith("in"):
        validations += [
            59 <= int(hgt[:-2]) <= 76,
        ]
    else:
        return False

    validations += [
        hcl.startswith("#"),
        len(hcl) == 7,
        all(
            [
                (ord(x) >= 48 and ord(x) <= 57) or (ord(x) >= 97 and ord(x) <= 102)
                for x in hcl[1:]
            ]
        ),
        ecl in eye_colors,
        len(pid) == 9,
        pid.isnumeric(),
    ]
    return all(validations)


def main() -> None:
    """Main function"""
    # Part 1
    assert main_func("aoc/aoc_2020/inputs/04_test.txt", 1) == 2
    assert main_func("aoc/aoc_2020/inputs/04.txt", 1) == 245
    # # Part 2
    assert main_func("aoc/aoc_2020/inputs/04_test.txt", 2) == 2
    assert main_func("aoc/aoc_2020/inputs/04_test_valid.txt", 2) == 4
    assert main_func("aoc/aoc_2020/inputs/04_test_invalid.txt", 2) == 0
    assert main_func("aoc/aoc_2020/inputs/04.txt", 2) == 133


if __name__ == "__main__":
    main()
