"""https://adventofcode.com/2024/day/22"""

from typing import Dict, List, Tuple


def handle_input(input_filename: str) -> List[int]:
    numbers = []
    with open(input_filename, "r") as f:
        for line in f:
            if len(line.strip()) == 0:
                continue
            numbers.append(int(line.strip()))
    return numbers


def main_func(input_filename: str, version: int) -> int:
    numbers = handle_input(input_filename)
    result = 0
    if version == 1:
        for num in numbers:
            for _ in range(2000):
                num = new_secret_number(num)
            result += num
    else:
        profit_dict: Dict[Tuple[int, ...], int] = {}
        for num in numbers:
            encountered = set()
            price = num % 10
            diff_list: List[int] = []
            for i in range(2000):
                if len(diff_list) == 4:
                    diff_list.pop(0)
                new_num = new_secret_number(num)
                new_price = num % 10
                diff_list.append(new_price - price)
                if len(diff_list) == 4 and (not tuple(diff_list) in encountered):
                    profit_dict[tuple(diff_list)] = (
                        profit_dict.get(tuple(diff_list), 0) + new_price
                    )
                    encountered.add(tuple(diff_list))

                num, price = new_num, new_price
        result = max(profit_dict.values())
    print(result)
    return result


def new_secret_number(num: int) -> int:
    num = ((num * 64) ^ num) % 16777216
    num = (int(num / 32) ^ num) % 16777216
    num = ((num * 2048) ^ num) % 16777216
    return num


def main() -> None:
    # Part 1
    assert new_secret_number(123) == 15887950
    assert main_func("aoc/aoc_2024/inputs/22_test.txt", 1) == 37327623
    assert main_func("aoc/aoc_2024/inputs/22.txt", 1) == 19927218456
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/22_test.txt", 2) == 25
    assert main_func("aoc/aoc_2024/inputs/22_test_2.txt", 2) == 23
    assert main_func("aoc/aoc_2024/inputs/22.txt", 2) == 2189


if __name__ == "__main__":
    main()
