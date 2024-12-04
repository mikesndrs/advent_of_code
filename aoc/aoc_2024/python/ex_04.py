"""https://adventofcode.com/2024/day/04"""

from typing import List

dir_dict = {
    "vertical": [1, 0],
    "horizontal": [0, 1],
    "diag_up": [-1, 1],
    "diag_down": [1, 1],
}


def handle_input(input_filename: str) -> List[str]:
    """Get list of lines from input"""
    text: List[str] = []
    with open(input_filename, "r") as f:
        for line in f:
            text.append(line.strip())
    return text


def word_count(text: List[str], version: int) -> int:
    """Count amount of times a given word is found in text"""
    count = 0
    for i, line in enumerate(text):
        for j, char in enumerate(line):
            if version == 1:
                word = "XMAS"
                for dir in ("vertical", "horizontal", "diag_up", "diag_down"):
                    my_word = get_word(text, i, j, len(word), dir)
                    if my_word == word or my_word == word[::-1]:
                        count += 1
            else:
                word = "MAS"
                if any(
                    [
                        i == 0,
                        j == 0,
                        i == len(text) - 1,
                        j == len(line) - 1,
                    ]
                ):
                    continue
                word_up = get_word(text, i + 1, j - 1, len(word), "diag_up")
                word_down = get_word(text, i - 1, j - 1, len(word), "diag_down")
                if (word_up == word or word_up == word[::-1]) and (
                    word_down == word or word_down == word[::-1]
                ):
                    count += 1
    return count


def get_word(text: List[str], i: int, j: int, length: int, dir: str) -> str:
    """Get word in given direction from starting point in grid"""
    y_mod, x_mod = dir_dict[dir]
    word = ""
    for n in range(length):
        y = i + y_mod * n
        x = j + x_mod * n
        if any(
            [
                y < 0,
                y >= len(text),
                x < 0,
                x >= len(text[i]),
            ]
        ):
            return word
        word += text[y][x]
    return word


def main_func(input_filename: str, version: int) -> int:
    """Main function"""
    text = handle_input(input_filename)
    result = word_count(text, version)
    print(result)
    return result


def main() -> None:
    """Top level function"""
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/04_test.txt", 1) == 18
    assert main_func("aoc/aoc_2024/inputs/04.txt", 1) == 2500
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/04_test.txt", 2) == 9
    # print(main_func("aoc/aoc_2024/inputs/04.txt", 2))
    assert main_func("aoc/aoc_2024/inputs/04.txt", 2) == 1933


if __name__ == "__main__":
    main()
