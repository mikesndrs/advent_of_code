"""https://adventofcode.com/2020/day/02"""

from typing import Any, Dict, List

ENTRY = Dict[str, Any]


def handle_input(input_filename: str) -> List[ENTRY]:
    """Process input"""
    password_list: List[ENTRY] = []
    with open(input_filename, "r") as f:
        for line in f:
            entry: ENTRY = {}
            a, b, c = line.strip().split(" ")
            entry["min"] = int(a.split("-")[0])
            entry["max"] = int(a.split("-")[1])
            entry["char"] = b.strip(":")
            entry["password"] = c.strip()
            password_list.append(entry)
    return password_list


def main_func(input_filename: str, version: int) -> int:
    """Get number of valid passwords according to policy"""
    password_list = handle_input(input_filename)
    res = 0
    for entry in password_list:
        if version == 1:
            char_count = entry["password"].count(entry["char"])
            if char_count >= entry["min"] and char_count <= entry["max"]:
                res += 1
        else:
            max_eq = entry["password"][entry["max"] - 1] == entry["char"]
            min_eq = entry["password"][entry["min"] - 1] == entry["char"]
            if len([x for x in [max_eq, min_eq] if x]) == 1:
                res += 1
    print(res)
    return res


def main() -> None:
    """Main function"""
    # Part 1
    assert main_func("aoc/aoc_2020/inputs/02_test.txt", 1) == 2
    assert main_func("aoc/aoc_2020/inputs/02.txt", 1) == 467
    # # Part 2
    assert main_func("aoc/aoc_2020/inputs/02_test.txt", 2) == 1
    assert main_func("aoc/aoc_2020/inputs/02.txt", 2) == 441


if __name__ == "__main__":
    main()
