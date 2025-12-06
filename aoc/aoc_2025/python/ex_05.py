"""https://adventofcode.com/2025/day/05"""

from typing import List, Tuple

RANGE = List[int]


def handle_input(input_filename: str) -> Tuple[List[RANGE], List[int]]:
    """Get list of ranges and list of IDS from raw input data"""
    ranges: List[RANGE] = []
    ids: List[int] = []
    with open(input_filename, "r") as f:
        first_half = True
        for line in f:
            if len(line.strip()) == 0:
                first_half = False
            elif first_half:
                new_ranges = [[int(x) for x in line.strip().split("-")]]
                while len(new_ranges):
                    new_range = new_ranges.pop()
                    for i, range in enumerate(ranges):
                        if new_range[0] == range[0] and new_range[1] == range[1]:
                            ranges.pop(i)
                            break
                        if new_range[0] >= range[0] and new_range[1] <= range[1]:
                            ranges.pop(i)
                            new_ranges.append(range)
                        elif new_range[0] <= range[0] and new_range[1] >= range[1]:
                            ranges.pop(i)
                            new_ranges.append(new_range)
                            break
                        elif (
                            new_range[0] < range[0]
                            and new_range[1] >= range[0]
                            and new_range[1] <= range[1]
                        ):
                            ranges.pop(i)
                            new_ranges.append([new_range[0], range[1]])
                            break
                        elif (
                            new_range[1] > range[1]
                            and new_range[0] >= range[0]
                            and new_range[0] <= range[1]
                        ):
                            ranges.pop(i)
                            new_ranges.append([range[0], new_range[1]])
                            break
                ranges.append(new_range)
            else:
                ids.append(int(line.strip()))

    ranges.sort()
    return ranges, ids


def is_valid(ranges: List[RANGE], id: int) -> bool:
    """check if id is valid within available ranges"""
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            return True
    return False


def main_func(input_filename: str, version: int) -> int:
    ranges, ids = handle_input(input_filename)
    res = 0
    if version == 1:
        for id in ids:
            if is_valid(ranges, id):
                res += 1
    else:
        for range in ranges:
            res += range[1] - range[0] + 1
    print(res)
    return res


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2025/inputs/05_test.txt", 1) == 3
    assert main_func("aoc/aoc_2025/inputs/05.txt", 1) == 770
    # # Part 2
    assert main_func("aoc/aoc_2025/inputs/05_test.txt", 2) == 14
    assert main_func("aoc/aoc_2025/inputs/05.txt", 2) == 357674099117260


if __name__ == "__main__":
    main()
