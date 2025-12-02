"""https://adventofcode.com/2025/day/02"""

from typing import List


def handle_input(input_filename: str) -> List[str]:
    """Get list of ID ranges"""
    with open(input_filename, "r") as f:
        return f.readline().strip().split(",")


def get_eff_ranges(my_range: str) -> List[List[str]]:
    """Get list of effective ID ranges with the same number of characters"""
    start, end = my_range.split("-")
    if len(start) == len(end):
        return [[start, end]]
    eff_ranges = []
    for i in range(len(start), len(end) + 1):
        if i == len(start):
            eff_ranges.append([start, "9" * len(start)])
        elif i == len(end):
            eff_ranges.append(["1" + (i - 1) * "0", end])
        else:
            eff_ranges.append(["1" + (i - 1) * "0", "9" * i])
    return eff_ranges


def get_invalids(eff_range: List[str], version: int) -> List[int]:
    """Get list of unique invalid IDs within given range"""
    invalids = []
    start, end = eff_range
    if version == 1:
        n_list = [2]
    else:
        n_list = list(range(2, len(end) + 1))
    for n in n_list:
        if len(start) % n != 0:
            continue
        length = len(start) // n
        start_1 = start[:length]
        end_1 = end[:length]
        if int(n * start_1) >= int(start) and int(n * start_1) <= int(end):
            invalids.append(int(n * start_1))
        if all([
            int(end_1) - int(start_1) >= 1,
            int(n * end_1) >= int(start),
            int(n * end_1) <= int(end),
        ]):
            invalids.append(int(n * end_1))
        invalids += [int(n * str(i)) for i in range(int(start_1) + 1, int(end_1))]
    return list(set(invalids))


def main_func(input_filename: str, version: int) -> int:
    """Calculate total sum of invalid IDs"""
    res = 0
    ranges = handle_input(input_filename)
    for my_range in ranges:
        eff_ranges = get_eff_ranges(my_range)
        for eff_range in eff_ranges:
            res += sum(get_invalids(eff_range, version))
    print(res)
    return res


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2025/inputs/02_test.txt", 1) == 1227775554
    assert main_func("aoc/aoc_2025/inputs/02.txt", 1) == 23534117921
    # # Part 2
    assert main_func("aoc/aoc_2025/inputs/02_test.txt", 2) == 4174379265
    assert main_func("aoc/aoc_2025/inputs/02.txt", 2) == 31755323497


if __name__ == "__main__":
    main()
