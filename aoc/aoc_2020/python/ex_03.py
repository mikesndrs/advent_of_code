"""https://adventofcode.com/2020/day/03"""

from typing import Set, Tuple


def handle_input(input_filename: str) -> Tuple[int, int, Set[Tuple[int, int]]]:
    """Get set of trees and edges of grid"""
    trees = set()
    with open(input_filename, "r") as f:
        for y, line in enumerate(f):
            max_x = len(line.strip()) - 1
            max_y = y
            for x, char in enumerate(line.strip()):
                if char == "#":
                    trees.add((x, y))
    return max_x, max_y, trees


def main_func(input_filename: str, version: int) -> int:
    """Get product of number of trees met for given slopes on given grid of trees"""
    max_x, max_y, trees = handle_input(input_filename)
    res = 1
    if version == 1:
        slopes = [[3, 1]]
    else:
        slopes = [
            [1, 1],
            [3, 1],
            [5, 1],
            [7, 1],
            [1, 2],
        ]
    for slope in slopes:
        res_i = 0
        pos = [0, 0]
        while pos[1] < max_y:
            pos = [(pos[0] + slope[0]) % (max_x + 1), (pos[1] + slope[1])]
            if tuple(pos) in trees:
                res_i += 1
        res *= res_i
    print(res)
    return res


def main() -> None:
    """Main function"""
    # Part 1
    assert main_func("aoc/aoc_2020/inputs/03_test.txt", 1) == 7
    assert main_func("aoc/aoc_2020/inputs/03.txt", 1) == 200
    # # Part 2
    assert main_func("aoc/aoc_2020/inputs/03_test.txt", 2) == 336
    assert main_func("aoc/aoc_2020/inputs/03.txt", 2) == 3737923200


if __name__ == "__main__":
    main()
