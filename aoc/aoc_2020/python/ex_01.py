"""https://adventofcode.com/2020/day/01"""

from typing import List, Optional

TARGET = 2020


def handle_input(input_filename: str) -> List[int]:
    """Get list of inputs from raw data"""
    input_list = []
    with open(input_filename, "r") as f:
        for line in f:
            input_list.append(int(line.strip()))
    return input_list


def main_func(input_filename: str, version: int) -> int:
    """Multiply list of elements that sum to target value"""
    input_list = handle_input(input_filename)
    res = 0
    if version == 1:
        pair = get_pair(TARGET, input_list, 2)
    else:
        pair = get_pair(TARGET, input_list, 3)
    if pair is not None:
        res = 1
        for val in pair:
            res *= val
    print(res)
    return res


def get_pair(
    target: int, input_list: List[int], n: int, i: int = 0
) -> Optional[List[int]]:
    """Recursively get list of values that sum to target value from list"""
    if i == n - 2:
        seen_list = set()
        for val in input_list:
            if target - val in seen_list:
                return [val, target - val]
            seen_list.add(val)
    else:
        for idx, val in enumerate(input_list):
            pair = get_pair(target - val, input_list[idx + 1 :], n, i + 1)
            if pair is not None:
                return pair + [val]
    return None


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2020/inputs/01_test.txt", 1) == 514579
    assert main_func("aoc/aoc_2020/inputs/01.txt", 1) == 542619
    # # Part 2
    assert main_func("aoc/aoc_2020/inputs/01_test.txt", 2) == 241861950
    assert main_func("aoc/aoc_2020/inputs/01.txt", 2) == 32858450


if __name__ == "__main__":
    main()
