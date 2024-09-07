"""https://adventofcode.com/2023/day/1"""

from typing import Callable

digit_strings = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def char_in_line(line: str, reversed: bool = False) -> str:
    direction = -1 if reversed else 1
    for char in line[::direction]:
        if char.isdigit():
            return char
    return ""


def string_in_line(line: str, reversed: bool = False) -> str:
    direction = -1 if reversed else 1
    for idx in range(len(line))[::direction]:
        for digit in digit_strings.keys():
            if idx + len(digit) < len(line) and line[idx : idx + len(digit)] == digit:
                return str(digit_strings[digit])
    return ""


def get_sum_first_and_list(input_filename: str, func: Callable) -> None:
    with open(input_filename) as f:
        result = 0
        for line in f:
            first = func(line)
            last = func(line, reversed=True)
            result += int(first + last)
        print(result)


def main() -> None:
    input_filename = "aoc/aoc_2023/inputs/01.txt"

    # Part 1
    get_sum_first_and_list(input_filename, char_in_line)
    # Part 2
    get_sum_first_and_list(input_filename, string_in_line)


if __name__ == "__main__":
    main()
