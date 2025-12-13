"""https://adventofcode.com/<year>/day/<number>"""

from typing import List


def handle_input(input_filename: str) -> List[str]:
    with open(input_filename, "r") as f:
        for line in f:
            pass


def main_func(input_filename: str, version: int) -> int:
    input = handle_input(input_filename)
    res = 0

    print(res)
    return res


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_<year>/inputs/<number>_test.txt", 1) == 0
    # print(main_func("aoc/aoc_<year>/inputs/<number>.txt", 1))
    # assert main_func("aoc/aoc_<year>/inputs/<number>.txt", 1) == 0
    # # Part 2
    # assert main_func("aoc/aoc_<year>/inputs/<number>_test.txt", 2) == 0
    # print(main_func("aoc/aoc_<year>/inputs/<number>.txt", 2))
    # assert main_func("aoc/aoc_<year>/inputs/<number>.txt", 2) == 0


if __name__ == "__main__":
    main()
