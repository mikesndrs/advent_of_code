"""https://adventofcode.com/2025/day/04"""

from typing import Dict, Tuple, List

MAX_NEIGHBORS = 4
MY_GRID = Dict[Tuple[int, int], List[Tuple[int, int]]]


def handle_input(input_filename: str) -> MY_GRID:
    """Get dict of positions of rolls of paper with counter at 0"""
    grid: MY_GRID = {}
    with open(input_filename, "r") as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line.strip()):
                if char == "@":
                    grid[(y, x)] = []
                    for dy in [-1, 0]:
                        for dx in [-1, 0, 1]:
                            if dy == 0 and dx == 0:
                                continue
                            if (y + dy, x + dx) in grid.keys():
                                grid[(y + dy, x + dx)].append((y, x))
                                grid[(y, x)].append((y + dy, x + dx))
    return grid


def main_func(input_filename: str, version: int) -> int:
    """Calculate amount of rolls of paper to move using forklifts"""
    grid = handle_input(input_filename)
    if version == 1:
        res = len([x for x in grid.values() if len(x) < MAX_NEIGHBORS])
    else:
        res = 0
        old_n = 1e16
        while len(grid.values()) < old_n:
            old_n = len(grid.values())
            remove_list = [key for key, val in grid.items() if len(val) < MAX_NEIGHBORS]
            res += len(remove_list)
            for key in remove_list:
                for nbr in grid[key]:
                    grid[nbr].remove(key)
                del grid[key]
    print(res)
    return res


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2025/inputs/04_test.txt", 1) == 13
    assert main_func("aoc/aoc_2025/inputs/04.txt", 1) == 1409
    # # Part 2
    assert main_func("aoc/aoc_2025/inputs/04_test.txt", 2) == 43
    assert main_func("aoc/aoc_2025/inputs/04.txt", 2) == 8366


if __name__ == "__main__":
    main()
