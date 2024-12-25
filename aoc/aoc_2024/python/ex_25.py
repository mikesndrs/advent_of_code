"""https://adventofcode.com/2024/day/25"""

from typing import List, Tuple

key_height = 5
key_length = 5
KEY = List[int]
LOCK = List[int]


def handle_input(input_filename: str) -> Tuple[List[LOCK], List[KEY]]:
    with open(input_filename, "r") as f:
        keys = []
        locks = []
        current = ""
        count = 0
        cur_object = [-1] * key_length
        for line in f:
            if line.strip() == "":
                continue
            if count == 0:
                if line.strip() == "#" * key_length:
                    current = "lock"
                elif line.strip() == "." * key_length:
                    current = "key"
            for i, char in enumerate(line.strip()):
                if char == "#":
                    cur_object[i] += 1
            count += 1
            if count == 7:
                if current == "key":
                    keys.append(cur_object)
                elif current == "lock":
                    locks.append(cur_object)
                cur_object = [-1] * 5
                current = ""
                count = 0
    return locks, keys


def check_if_fits(lock: LOCK, key: KEY) -> bool:
    for i in range(len(lock)):
        if lock[i] + key[i] > key_height:
            return False
    return True


def main_func(input_filename: str, version: int) -> int:
    locks, keys = handle_input(input_filename)
    result = 0
    for lock in locks:
        for key in keys:
            if check_if_fits(lock, key):
                result += 1
    print(result)
    return result


def main() -> None:
    assert main_func("aoc/aoc_2024/inputs/25_test.txt", 1) == 3
    assert main_func("aoc/aoc_2024/inputs/25.txt", 1) == 3116


if __name__ == "__main__":
    main()
