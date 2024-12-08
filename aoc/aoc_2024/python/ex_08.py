"""https://adventofcode.com/2024/day/08"""

from typing import Dict, List, Set, Tuple

ANTENNA_DICT = Dict[str, List[Tuple[int, int]]]


def handle_input(input_filename: str) -> Tuple[int, int, ANTENNA_DICT]:
    """Get grid size and antenna locations from raw input"""
    max_x = 0
    max_y = 0
    antenna_dict: ANTENNA_DICT = {}
    with open(input_filename, "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                max_x = len(line.strip()) - 1
            if len(line.strip()) > 0:
                max_y = i
            for j, char in enumerate(line.strip()):
                if char != ".":
                    antenna_dict[char] = antenna_dict.get(char, []) + [(j, i)]

    return max_y, max_x, antenna_dict


def get_antinodes(
    max_y: int, max_x: int, antenna_dict: ANTENNA_DICT, version: int
) -> Set[Tuple[int, int]]:
    """Get set of antinodes based on antenna dict"""
    antinodes = set()
    for antenna_list in antenna_dict.values():
        for i, (x, y) in enumerate(antenna_list):
            for x2, y2 in antenna_list[i + 1 :]:
                if version == 1:
                    my_range = [-2, 1]
                else:
                    my_range = list(range(-max_y, max_y))
                for n in my_range:
                    if (0 <= x + n * (x - x2) <= max_x) and (
                        0 <= y + n * (y - y2) <= max_y
                    ):
                        antinodes.add((x + n * (x - x2), y + n * (y - y2)))
    return antinodes


def main_func(input_filename: str, version: int) -> int:
    """main function"""
    max_y, max_x, antenna_dict = handle_input(input_filename)
    antinodes = get_antinodes(max_y, max_x, antenna_dict, version)
    result = len(antinodes)
    print(result)
    return result


def main() -> None:
    """Top level function"""
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/08_test.txt", 1) == 14
    assert main_func("aoc/aoc_2024/inputs/08.txt", 1) == 336
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/08_test.txt", 2) == 34
    assert main_func("aoc/aoc_2024/inputs/08.txt", 2) == 1131


if __name__ == "__main__":
    main()
