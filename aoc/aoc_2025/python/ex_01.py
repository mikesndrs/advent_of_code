"""https://adventofcode.com/2025/day/01"""

from typing import List

MOD = 100


def handle_input(input_filename: str) -> List[str]:
    """Get list of dial turns"""
    input = []
    with open(input_filename, "r") as f:
        for line in f:
            input.append(line.strip())
    return input


def get_rotations(pos: int, new_pos: int, version: int) -> int:
    """Calculate number of rotations for given move"""
    if version == 1:
        if new_pos % MOD == 0:
            return 1
        else:
            return 0
    else:
        if pos == 0 and new_pos < 0:
            return abs(new_pos // MOD) - 1
        elif pos > 0 and (new_pos % MOD) == 0 and new_pos <= 0:
            return abs(new_pos // MOD) + 1
        else:
            return abs(new_pos // MOD)


def main_func(input_filename: str, version: int) -> int:
    """Calculate number of rotations over course of multiple moves"""
    pos = 50
    res = 0
    turns = handle_input(input_filename)
    for turn in turns:
        if turn[0] == "R":
            new_pos = pos + int(turn[1:])
        else:
            new_pos = pos - int(turn[1:])
        res += get_rotations(pos, new_pos, version)
        pos = new_pos % MOD
    print(res)
    return res


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2025/inputs/01_test.txt", 1) == 3
    assert main_func("aoc/aoc_2025/inputs/01.txt", 1) == 1135
    # # Part 2
    assert main_func("aoc/aoc_2025/inputs/01_test.txt", 2) == 6
    assert main_func("aoc/aoc_2025/inputs/01.txt", 2) == 6558


if __name__ == "__main__":
    main()
