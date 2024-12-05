"""https://adventofcode.com/2024/day/05"""

from typing import Dict, List, Tuple

ORDER_DICT = Dict[int, List[int]]
UPDATE = List[int]


def handle_input(input_filename: str) -> Tuple[ORDER_DICT, List[UPDATE]]:
    """Get ordering dictionary and list of updates from raw inputs"""
    order_dict: ORDER_DICT = {}
    updates = []
    input_first_part = True
    with open(input_filename, "r") as f:
        for line in f:
            if line == "\n":
                input_first_part = False
            elif input_first_part:
                key, val = line.strip().split("|")
                order_dict[int(key)] = order_dict.get(int(key), []) + [int(val)]
            else:
                updates.append([int(x) for x in line.strip().split(",")])
    return order_dict, updates


def check_valid(order_dict: ORDER_DICT, update: UPDATE) -> bool:
    """Check whether input is valid or not"""
    for i, val in enumerate(update):
        if any([update[j] in order_dict.get(val, []) for j in range(i)]):
            return False
    return True


def get_middle_value(update: UPDATE) -> int:
    """Get middle value of update"""
    idx = int(len(update) / 2)
    val = update[idx]
    return val


def order_update(order_dict: ORDER_DICT, update: UPDATE) -> UPDATE:
    """Get proper ordered version of update based on ordering dictionary"""
    updated = False
    new_update: UPDATE = []
    for val in update:
        updated = False
        for i, new_val in enumerate(new_update):
            if new_val in order_dict.get(val, []):
                new_update.insert(i, val)
                updated = True
                break
        if not updated:
            new_update.append(val)
    return new_update


def main_func(input_filename: str, version: int) -> int:
    """Main function"""
    order_dict, updates = handle_input(input_filename)
    result = 0
    for update in updates:
        if check_valid(order_dict, update):
            if version == 1:
                result += get_middle_value(update)
        else:
            if version == 2:
                new_update = order_update(order_dict, update)
                result += get_middle_value(new_update)
    print(result)
    return result


def main() -> None:
    """Top level function"""
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/05_test.txt", 1) == 143
    assert main_func("aoc/aoc_2024/inputs/05.txt", 1) == 5588
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/05_test.txt", 2) == 123
    assert main_func("aoc/aoc_2024/inputs/05.txt", 2) == 5331


if __name__ == "__main__":
    main()
