"""https://adventofcode.com/2025/day/06"""

from functools import reduce
from typing import Callable, List, Tuple

MY_NUMS = List[List[int]]
MY_OPS = List[Callable]


op_dict = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
}


def read_inputs_human(input_filename: str) -> Tuple[MY_NUMS, MY_OPS]:
    """Get numbers and operators through human way"""
    nums_list: MY_NUMS = []
    op_list: MY_OPS = []
    with open(input_filename, "r") as f:
        for line in f:
            if line.strip()[0].isdigit():
                nums_list.append([int(x) for x in line.strip().split(" ") if x])
            else:
                op_list = [op_dict[x] for x in line.strip().split(" ") if x]
        nums_list = list(map(list, zip(*nums_list)))
    return nums_list, op_list


def read_inputs_cephalopod(input_filename: str) -> Tuple[MY_NUMS, MY_OPS]:
    """Get numbers and operators through cephalopod way"""
    nums_list: MY_NUMS = []
    op_list: MY_OPS = []
    new_nums = []
    with open(input_filename, "r") as f:
        lines = f.readlines()
        for i in reversed(range(len(lines[-1].strip("\n")))):
            char = lines[-1].strip("\n")[i]
            nums_str = "".join(line.strip("\n")[i] for line in lines[:-1])
            if nums_str.strip():
                new_nums.append(int(nums_str))
            if char != " ":
                nums_list.append(new_nums)
                op_list.append(op_dict[char])
                new_nums = []
    return nums_list, op_list


def handle_input(input_filename: str, version: int) -> Tuple[MY_NUMS, MY_OPS]:
    """Get numbers and operators from raw input data"""
    if version == 1:
        return read_inputs_human(input_filename)
    else:
        return read_inputs_cephalopod(input_filename)


def main_func(input_filename: str, version: int) -> int:
    """Calculate sum for cephalopod math"""
    nums_list, op_list = handle_input(input_filename, version)
    res = 0
    for i, op in enumerate(op_list):
        nums = nums_list[i]
        res += reduce(op, nums)
    print(res)
    return res


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2025/inputs/06_test.txt", 1) == 4277556
    assert main_func("aoc/aoc_2025/inputs/06.txt", 1) == 6295830249262
    # # Part 2
    assert main_func("aoc/aoc_2025/inputs/06_test.txt", 2) == 3263827
    assert main_func("aoc/aoc_2025/inputs/06.txt", 2) == 9194682052782


if __name__ == "__main__":
    main()
