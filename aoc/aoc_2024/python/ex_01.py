"""https://adventofcode.com/2024/day/1"""


def handle_input(input_filename: str) -> tuple[list, list]:
    list1, list2 = [], []
    with open(input_filename, "r") as f:
        for line in f:
            split_line = line.strip().split("   ")
            list1.append(int(split_line[0]))
            list2.append(int(split_line[1]))
    return list1, list2


def calculate_difference(list1: list, list2: list) -> int:
    list1.sort()
    list2.sort()
    result = 0
    for i in range(len(list1)):
        result += abs(list1[i] - list2[i])
    return result


def calculate_similarity(list1: list, list2: list) -> int:
    result = 0
    count_dict1: dict[int, int] = {}
    count_dict2: dict[int, int] = {}
    for x in list1:
        count_dict1[x] = count_dict1.get(x, 0) + 1
    for x in list2:
        count_dict2[x] = count_dict2.get(x, 0) + 1
    for x in count_dict1.keys():
        result += count_dict1[x] * x * count_dict2.get(x, 0)
    return result


def main_func(input_filename: str, version: int) -> int:
    list1, list2 = handle_input(input_filename)
    if version == 1:
        result = calculate_difference(list1, list2)
    elif version == 2:
        result = calculate_similarity(list1, list2)
    print(result)
    return result


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/01_test.txt", 1) == 11
    assert main_func("aoc/aoc_2024/inputs/01.txt", 1) == 1830467
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/01_test.txt", 2) == 31
    assert main_func("aoc/aoc_2024/inputs/01.txt", 2) == 26674158


if __name__ == "__main__":
    main()
