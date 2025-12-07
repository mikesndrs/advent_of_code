"""https://adventofcode.com/2025/day/07"""

from typing import Tuple, Set, Dict

POS = Tuple[int, int]


def handle_input(input_filename: str) -> Tuple[int, POS, Set[POS]]:
    """Get positions of splitters and tachyon beam start"""
    splitter_set = set()
    start: POS
    with open(input_filename, "r") as f:
        for y, line in enumerate(f):
            height = y + 1
            for x, char in enumerate(line.strip()):
                if char == "S":
                    start = (y, x)
                if char == "^":
                    splitter_set.add((y, x))
    return height, start, splitter_set


def main_func(input_filename: str, version: int) -> int:
    """Run tachyon beam through system of splitters"""
    height, start, splitter_set = handle_input(input_filename)
    res = 0
    beam_set = {start: 1}
    for i in range(height):
        new_beam_set: Dict[POS, int] = {}
        for (y, x), ctr in beam_set.items():
            if (y + 1, x) in splitter_set:
                new_beam_set[(y + 1, x - 1)] = new_beam_set.get((y + 1, x - 1), 0) + ctr
                new_beam_set[(y + 1, x + 1)] = new_beam_set.get((y + 1, x + 1), 0) + ctr
                res += 1
            else:
                new_beam_set[(y + 1, x)] = new_beam_set.get((y + 1, x), 0) + ctr
        beam_set = new_beam_set
    if version == 2:
        res = sum([val for val in beam_set.values()])
    print(res)
    return res


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2025/inputs/07_test.txt", 1) == 21
    assert main_func("aoc/aoc_2025/inputs/07.txt", 1) == 1613
    # # Part 2
    assert main_func("aoc/aoc_2025/inputs/07_test.txt", 2) == 40
    assert main_func("aoc/aoc_2025/inputs/07.txt", 2) == 48021610271997


if __name__ == "__main__":
    main()
