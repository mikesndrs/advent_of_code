"""https://adventofcode.com/2024/day/02"""

from typing import Callable


def handle_input(input_filename: str) -> list[list[int]]:
    """Make list with separate reports from inputs"""
    reports: list[list[int]] = []
    with open(input_filename, "r") as f:
        for line in f:
            report = [int(x) for x in line.strip().split(" ")]
            reports.append(report)
    return reports


def is_safe(arr: list, version: int) -> bool:
    """Check whether report is safe"""
    for op in [lambda x, y: x < y, lambda x, y: x > y]:
        if check_array(arr, op, version):
            return True
    return False


def check_array(arr: list, op: Callable, version: int) -> bool:
    """Check whether array is valid for given operation"""
    if version == 1:
        safety_cutoff = 0
    else:
        safety_cutoff = 1
    old_val = None
    skip_next = False
    for i, x in enumerate(arr):
        if skip_next:
            skip_next = False
            continue
        if old_val is not None:
            shallow = 1 <= abs(x - old_val) <= 3
            increasing = op(x, old_val)
            if not (shallow and increasing):
                if safety_cutoff == 0:
                    return False
                else:
                    safety_cutoff -= 1
                    if i == len(arr) - 1:
                        continue
                    elif (1 <= abs(arr[i + 1] - old_val) <= 3) and op(
                        arr[i + 1], old_val
                    ):
                        continue
                    elif (1 <= abs(arr[i + 1] - x) <= 3) and op(arr[i + 1], x):
                        if i == 1:
                            old_val = x
                        elif (1 <= abs(x - arr[i - 2]) <= 3) and op(x, arr[i - 2]):
                            old_val = x
                        else:
                            return False
                        continue
                    else:
                        return False
        old_val = x
    return True


def main_func(input_filename: str, version: int) -> int:
    """Main function"""
    reports = handle_input(input_filename)
    result = 0
    for report in reports:
        if is_safe(report, version):
            result += 1
    print(result)
    return result


def main() -> None:
    """Top level function"""
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/02_test.txt", 1) == 2
    assert main_func("aoc/aoc_2024/inputs/02.txt", 1) == 526
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/02_test.txt", 2) == 4
    assert main_func("aoc/aoc_2024/inputs/02.txt", 2) == 566


if __name__ == "__main__":
    main()
