"""https://adventofcode.com/2024/day/07"""

from typing import List

# EQUATION = List[int, List[int]]
EQUATION = List


def handle_input(input_filename: str) -> List[EQUATION]:
    """Get list of equations with result and numbers"""
    equations = []
    with open(input_filename, "r") as f:
        for line in f:
            split_line = line.strip().split(": ")
            equations.append(
                [int(split_line[0]), [int(x) for x in split_line[1].split(" ")]]
            )
    return equations


def check_valid_equation(
    result: int, list: List[int], version: int, val: int = 0
) -> bool:
    """Iterative function to determine whether an equation can be made valid"""
    if val > result:
        return False
    if len(list) == 0:
        return val == result
    if check_valid_equation(result, list[1:], version=version, val=val * list[0]):
        return True
    if check_valid_equation(result, list[1:], version=version, val=val + list[0]):
        return True
    if version == 2 and check_valid_equation(
        result, list[1:], version=version, val=int(f"{val}{list[0]}")
    ):
        return True
    return False


def main_func(input_filename: str, version: int) -> int:
    """Main function"""
    equations = handle_input(input_filename)
    result = 0
    for equation in equations:
        if check_valid_equation(equation[0], equation[1], version=version):
            result += equation[0]
    print(result)
    return result


def main() -> None:
    """Top level function"""
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/07_test.txt", 1) == 3749
    assert main_func("aoc/aoc_2024/inputs/07.txt", 1) == 2437272016585
    # # Part 2j
    assert main_func("aoc/aoc_2024/inputs/07_test.txt", 2) == 11387
    assert main_func("aoc/aoc_2024/inputs/07.txt", 2) == 162987117690649


if __name__ == "__main__":
    main()
