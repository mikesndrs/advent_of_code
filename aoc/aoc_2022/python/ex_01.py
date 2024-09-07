"""https://adventofcode.com/2022/day/1"""

import numpy as np


def main() -> None:
    input_filename = "aoc/aoc_2022/inputs/01.txt"
    input = []
    with open(input_filename) as f:
        text = f.read()
        lists = text.split("\n\n")
        for list in lists:
            mini_list = list.split("\n")
            int_mini_list = [int(x) for x in mini_list if x != ""]
            input.append(int_mini_list)

    calories_list = [np.sum(np.array(elf)) for elf in input]
    result1 = np.max(calories_list)
    print(result1)

    # 2022-12-01 1st puzzle
    top_n = 3
    sorted_calories_list = np.sort(calories_list)[::-1]
    result2 = np.sum(sorted_calories_list[:top_n])
    print(result2)


if __name__ == "__main__":
    main()
