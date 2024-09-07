"""https://adventofcode.com/2022/day/4"""

import numpy as np


def main() -> None:
    input_filename = "aoc/aoc_2022/inputs/04.txt"
    input = []
    with open(input_filename) as f:
        text = f.read()
        lists = text.split("\n")[:-1]
        for pair in lists:
            input.append([[int(x) for x in elf.split("-")] for elf in pair.split(",")])

    overlap_list = []
    for pair in input:
        overlap_list.append(
            any(
                [
                    (pair[0][0] >= pair[1][0]) == (pair[0][1] <= pair[1][1]),
                    (pair[0][0] <= pair[1][0]) == (pair[0][1] >= pair[1][1]),
                ]
            )
        )

    result1 = np.sum(np.array(overlap_list))
    print(result1)

    overlap_list = []
    for pair in input:
        overlap_list.append(
            any(
                [
                    all([pair[0][1] >= pair[1][0], pair[0][1] <= pair[1][1]]),
                    all([pair[1][1] >= pair[0][0], pair[1][1] <= pair[0][1]]),
                ]
            )
        )

    result1 = np.sum(np.array(overlap_list))
    print(result1)


if __name__ == "__main__":
    main()
