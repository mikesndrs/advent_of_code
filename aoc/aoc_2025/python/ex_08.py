"""https://adventofcode.com/2025/day/08"""

from typing import List, Tuple, Set

POS = Tuple[int, ...]
GROUP = Set[POS]


def handle_input(input_filename: str) -> List[POS]:
    """Get list of coordinates per box"""
    pos_list = []
    with open(input_filename, "r") as f:
        for line in f:
            pos_list.append(tuple(int(x) for x in line.strip().split(",")))
    return pos_list


def connect_largest(pos_list: List[POS], n_connections: int, version: int) -> int:
    """Connect circuits and multiply size of largest n"""
    connect_list: List[Tuple[int, POS, POS]] = []
    for i, pos in enumerate(pos_list):
        for pos2 in pos_list[i + 1 :]:
            dist = sum((pos[x] - pos2[x]) ** 2 for x in range(3)) ** 0.5
            connect_list.append((dist, pos, pos2))
    sorted_connect_list = sorted(connect_list, key=lambda x: x[0])

    res = 0
    if version == 1:
        group_list: List[GROUP] = []
        for dist, pos, pos2 in sorted_connect_list[:n_connections]:
            add_to_group_list(pos, pos2, group_list)
        group_list = sorted(group_list, key=len)

        import math

        res = math.prod(len(group) for group in group_list[-3:])
        return res
    else:
        group_list = [
            {
                pos,
            }
            for pos in pos_list
        ]
        for dist, pos, pos2 in sorted_connect_list:
            add_to_group_list(pos, pos2, group_list)
            if len(group_list) == 1:
                return pos[0] * pos2[0]
    return res


def add_to_group_list(pos: POS, nbr: POS, group_list: List[GROUP]) -> List[GROUP]:
    """Add new box to group"""
    new_group = set([pos, nbr])
    for i, group in reversed(list(enumerate(group_list))):
        if pos in group or nbr in group:
            new_group = new_group | set(group)
            group_list.pop(i)
    group_list.append(new_group)
    return group_list


def main_func(input_filename: str, version: int, n_connections: int) -> int:
    """Connect largest groups of boxes"""
    pos_list = handle_input(input_filename)
    res = connect_largest(pos_list, n_connections, version)
    print(res)
    return res
    # sol 1 > 3420


def main() -> None:
    """Main func"""
    # Part 1
    assert main_func("aoc/aoc_2025/inputs/08_test.txt", 1, 10) == 40
    assert main_func("aoc/aoc_2025/inputs/08.txt", 1, 1000) == 131580
    # # Part 2
    assert main_func("aoc/aoc_2025/inputs/08_test.txt", 2, 10) == 25272
    assert main_func("aoc/aoc_2025/inputs/08.txt", 2, 1000) == 6844224


if __name__ == "__main__":
    main()
