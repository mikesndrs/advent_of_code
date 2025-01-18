"""https://adventofcode.com/2023/day/11"""

from typing import List

GALAXY = List[int]


def handle_input(input_filename: str, expansion: int) -> List[GALAXY]:
    galaxies = []
    seen_x = set()
    seen_y = set()
    max_x = 0
    max_y = 0
    with open(input_filename, "r") as f:
        for y, line in enumerate(f):
            if line.strip() == "":
                continue
            max_x = len(line.strip()) - 1
            max_y = y
            for x, char in enumerate(line.strip()):
                if char == "#":
                    galaxies.append([x, y])
                    seen_x.add(x)
                    seen_y.add(y)
    for x in range(max_x, 0, -1):
        if x not in seen_x:
            for galaxy in galaxies:
                if galaxy[0] > x:
                    galaxy[0] += expansion - 1
    for y in range(max_y, 0, -1):
        if y not in seen_y:
            for galaxy in galaxies:
                if galaxy[1] > y:
                    galaxy[1] += expansion - 1
    return galaxies


def calc_distances(galaxies: List[GALAXY]) -> int:
    dist = 0
    for i, galaxy_1 in enumerate(galaxies):
        for galaxy_2 in galaxies[i + 1 :]:
            dist += abs(galaxy_1[0] - galaxy_2[0]) + abs(galaxy_1[1] - galaxy_2[1])
    return dist


def main_func(input_filename: str, expansion: int) -> int:
    galaxies = handle_input(input_filename, expansion)
    result = calc_distances(galaxies)
    print(result)
    return result


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2023/inputs/11_test.txt", 2) == 374
    assert main_func("aoc/aoc_2023/inputs/11.txt", 2) == 9918828
    # # Part 2
    assert main_func("aoc/aoc_2023/inputs/11_test.txt", 10) == 1030
    assert main_func("aoc/aoc_2023/inputs/11_test.txt", 100) == 8410
    assert main_func("aoc/aoc_2023/inputs/11.txt", 1000000) == 692506533832


if __name__ == "__main__":
    main()
