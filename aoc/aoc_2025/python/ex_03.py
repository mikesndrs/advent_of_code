"""https://adventofcode.com/2025/day/03"""

from typing import List


def handle_input(input_filename: str) -> List[List[int]]:
    """Get list of banks with joltages"""
    input = []
    with open(input_filename, "r") as f:
        for line in f:
            input.append([int(x) for x in line.strip()])
    return input


def calc_max_joltage(bank: List[int], n: int) -> int:
    "Calculate highest possible joltage for given bank"
    if len(bank) < n:
        raise ValueError("n too big for input")
    num_str = ""
    idx = -1
    for i in range(n - 1, -1, -1):
        new_val = max(bank[idx + 1 : len(bank) - i])
        idx += bank[idx + 1 : len(bank) - i].index(new_val) + 1
        num_str += str(new_val)
    return int(num_str)


def main_func(input_filename: str, version: int) -> int:
    """Calculate sum of highest joltages"""
    if version == 1:
        n = 2
    else:
        n = 12
    banks = handle_input(input_filename)
    res = 0
    for bank in banks:
        res += calc_max_joltage(bank, n)
    print(res)
    return res


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2025/inputs/03_test.txt", 1) == 357
    assert main_func("aoc/aoc_2025/inputs/03.txt", 1) == 17432
    # # Part 2
    assert main_func("aoc/aoc_2025/inputs/03_test.txt", 2) == 3121910778619
    assert main_func("aoc/aoc_2025/inputs/03.txt", 2) == 173065202451341


if __name__ == "__main__":
    main()
