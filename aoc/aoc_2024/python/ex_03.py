"""https://adventofcode.com/2024/day/03"""

from typing import List, Optional

MAX_DIGITS = 3


def handle_input(input_filename: str) -> str:
    """Get full text from input"""
    result = ""
    with open(input_filename, "r") as f:
        for line in f:
            result += line.strip()
    return result


def get_pairs(text: str, version: int) -> List[List[int]]:
    """Retrieve all pairs from text"""
    pairs: List[List[int]] = []
    enabled = True
    for i in range(len(text)):
        if version == 2 and text[i : min(i + 7, len(text))] == "don't()":
            enabled = False
        elif version == 2 and text[i : min(i + 4, len(text))] == "do()":
            enabled = True
        elif enabled and text[i : min(i + 4, len(text))] == "mul(":
            my_pair = find_pair(
                text[i + 4 : min(i + 4 + 2 * MAX_DIGITS + 2, len(text))]
            )
            if my_pair is not None:
                pairs.append(my_pair)
    return pairs


def find_pair(text: str) -> Optional[List[int]]:
    """Find a pair in a given piece of text"""
    my_pair = []
    my_str = ""
    for char in text:
        if char == ",":
            my_pair.append(int(my_str))
            my_str = ""
        elif char == ")":
            my_pair.append(int(my_str))
            return my_pair
        elif char.isnumeric():
            my_str += char
        else:
            return None
    return None


def main_func(input_filename: str, version: int) -> int:
    """Main function"""
    text = handle_input(input_filename)
    pairs = get_pairs(text, version)
    result = 0
    for pair in pairs:
        result += pair[0] * pair[1]
    print(result)
    return result


def main() -> None:
    """Top level function"""
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/03_test.txt", 1) == 161
    assert main_func("aoc/aoc_2024/inputs/03.txt", 1) == 174960292
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/03_test.txt", 2) == 48
    assert main_func("aoc/aoc_2024/inputs/03.txt", 2) == 56275602


if __name__ == "__main__":
    main()
