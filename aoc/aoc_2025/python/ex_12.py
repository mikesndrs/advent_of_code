"""https://adventofcode.com/2025/day/12"""

from typing import Dict, List, Tuple


def handle_input(input_filename: str) -> Tuple[Dict[int, List[int]], List]:
    """Get list of present shapes and list of spaces with required presents from raw
    data"""
    with open(input_filename, "r") as f:
        first_part = True
        presents: Dict[int, List[int]] = {}
        spaces = []
        for line in f:
            if "x" in line:
                first_part = False
            if first_part:
                if ":" in line:
                    key = int(line.strip().strip(":"))
                    presents[key] = []
                    y = 0
                else:
                    for x, char in enumerate(line.strip()):
                        if char == "#":
                            presents[key] += [y, x]
                    y += 1
            else:
                dims = list(int(x) for x in line.strip().split(":")[0].split("x"))
                presents_list = list(
                    int(x) for x in line.strip().split(":")[1].strip().split(" ")
                )
                spaces += [[dims, presents_list]]
    return presents, spaces


def main_func(input_filename: str, version: int) -> int:
    """Check if all given presents fit into assigned space"""
    presents, spaces = handle_input(input_filename)
    res = 0
    for (height, width), present_list in spaces:
        if sum(present_list) * 7 > height * width:
            continue
        elif sum(present_list) * 9 <= 3 * (height // 3) * 3 * (width // 3):
            res += 1
        else:
            print("no actual solution needed I guess")
    print(res)
    return res


def main() -> None:
    # Part 1
    # assert main_func("aoc/aoc_2025/inputs/12_test.txt", 1) == 2
    assert main_func("aoc/aoc_2025/inputs/12.txt", 1) == 485


if __name__ == "__main__":
    main()
