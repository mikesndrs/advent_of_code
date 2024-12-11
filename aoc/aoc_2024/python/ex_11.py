"""https://adventofcode.com/2024/day/11"""

from typing import Dict


def handle_input(input_filename: str) -> Dict[str, int]:
    """Get dictionary of how often each element occurs in collection"""
    with open(input_filename, "r") as f:
        init_arr = f.readlines()[0].strip().split(" ")

    init_dict: Dict[str, int] = {}
    for x in init_arr:
        init_dict[x] = init_dict.get(x, 0) + 1
    return init_dict


def blink(arr: Dict[str, int]) -> Dict[str, int]:
    """Generate new collection based on given rules"""
    new_dict: Dict[str, int] = {}
    for x in arr.keys():
        if x == "0":
            new_dict["1"] = new_dict.get("1", 0) + arr[x]
        elif len(x) % 2 == 0:
            el1 = x[: int(len(x) / 2)].lstrip("0") or "0"
            el2 = x[int(len(x) / 2) :].lstrip("0") or "0"
            new_dict[el1] = new_dict.get(el1, 0) + arr[x]
            new_dict[el2] = new_dict.get(el2, 0) + arr[x]
        else:
            new_dict[str(2024 * int(x))] = new_dict.get(str(2024 * int(x)), 0) + arr[x]
    return new_dict


def main_func(input_filename: str, version: int) -> int:
    """Main function"""
    arr = handle_input(input_filename)
    if version == 1:
        n = 25
    else:
        n = 75
    # print(arr)
    for i in range(n):
        arr = blink(arr)
        # print(arr)
    result = sum(arr.values())
    print(result)
    return result


def main() -> None:
    """Top level function"""
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/11_test.txt", 1) == 55312
    assert main_func("aoc/aoc_2024/inputs/11.txt", 1) == 198089
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/11_test.txt", 2) == 65601038650482
    assert main_func("aoc/aoc_2024/inputs/11.txt", 2) == 236302670835517


if __name__ == "__main__":
    main()
