"""https://adventofcode.com/2023/day/9"""


def sum_next_entry(filename: str, version: int = 1) -> int:
    with open(filename) as f:
        res = 0
        for line in f:
            arr = [int(x) for x in line.strip().split(" ")]
            if version == 1:
                s_res = next_entry(arr)
            else:
                s_res = prev_entry(arr)
            res += s_res
    return res


def next_entry(arr: list) -> int:
    der = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
    if all([x == 0 for x in der]):
        res = arr[-1] + 0
    else:
        res = arr[-1] + next_entry(der)
    return res


def prev_entry(arr: list) -> int:
    der = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
    if all([x == 0 for x in der]):
        res = arr[0] - 0
    else:
        res = arr[0] - prev_entry(der)
    return res


def main() -> None:
    # Part 1
    assert sum_next_entry("2023/inputs/09_test.txt", 1) == 114
    assert sum_next_entry("2023/inputs/09.txt", 1) == 1637452029
    # Part 2
    assert sum_next_entry("2023/inputs/09_test.txt", 2) == 2
    assert sum_next_entry("2023/inputs/09.txt", 2) == 908


if __name__ == "__main__":
    main()
