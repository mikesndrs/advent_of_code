"""https://adventofcode.com/2025/day/09"""

from typing import List, Tuple, Sequence


POS = Tuple[int, ...]


def handle_input(input_filename: str) -> List[POS]:
    """Get list of connected positions from raw input"""
    pos_list = []
    with open(input_filename, "r") as f:
        for line in f:
            pos_list.append(tuple(int(x) for x in line.strip().split(",")))
    return pos_list


def main_func(input_filename: str, version: int) -> int:
    """Calculate biggest area for valid box"""
    # TODO: calc in reasonable time
    pos_list = handle_input(input_filename)
    res = 0
    dist_list: List[Tuple[int, POS, POS]] = []
    for i, pos in enumerate(pos_list):
        for pos2 in pos_list[i + 1 :]:
            height = abs(pos[0] - pos2[0]) + 1
            width = abs(pos[1] - pos2[1]) + 1
            new_dist = height * width
            dist_list.append((new_dist, pos, pos2))
    for new_dist, pos, pos2 in reversed(sorted(dist_list, key=lambda x: x[0])):
        if new_dist > res and (version == 1 or is_valid(pos, pos2, pos_list)):
            res = new_dist
            break
    print(res)
    return res


def is_inside(pos: POS, pos_list: Sequence[POS]) -> bool:
    """Check if position is surrounded by directional trace of positions"""
    # has uneven amount of lines per side
    # or is on a line
    ctr = 0
    for i in range(len(pos_list)):
        if pos_list[i][0] != pos_list[i - 1][0]:
            continue
        if all(
            (
                pos[0] > pos_list[i][0],
                pos[1] >= min(pos_list[i][1], pos_list[i - 1][1]),
                pos[1] <= max(pos_list[i][1], pos_list[i - 1][1]),
            )
        ):
            if pos_list[i][1] > pos_list[i - 1][1]:
                sign = 1
            else:
                sign = -1
            if pos_list[i][1] == pos[1] or pos_list[i - 1][1] == pos[1]:
                mult = 1
            else:
                mult = 2
            ctr += sign * mult
    if (ctr % 4) == 0:
        return False
    ctr = 0
    for i in range(len(pos_list)):
        if pos_list[i][1] != pos_list[i - 1][1]:
            continue
        if all(
            (
                pos[1] > pos_list[i][1],
                pos[0] >= min(pos_list[i][0], pos_list[i - 1][0]),
                pos[0] <= max(pos_list[i][0], pos_list[i - 1][0]),
            )
        ):
            if pos_list[i][0] > pos_list[i - 1][0]:
                sign = 1
            else:
                sign = -1
            if pos_list[i][0] == pos[0] or pos_list[i - 1][0] == pos[0]:
                mult = 1
            else:
                mult = 2
            ctr += sign * mult
    if (ctr % 4) == 0:
        return False
    return True


def is_valid(pos: POS, pos2: POS, pos_list: List[POS]) -> bool:
    """Check if box defined by 2 corners is fully surrounded by list of directional
    positions"""
    # is_valid with reduced grid implementation(misses parallel lines with gaps)
    new_x_list = sorted(list(set([x[1] for x in pos_list])))
    new_y_list = sorted(list(set([x[0] for x in pos_list])))
    new_pos_list = [(new_y_list.index(x[0]), new_x_list.index(x[1])) for x in pos_list]
    greens_list = set()
    for i, new_pos in enumerate(new_pos_list):
        new_pos2 = new_pos_list[i - 1]
        if new_pos2[0] == new_pos[0]:
            greens_list.update(
                set(
                    [
                        (new_pos[0], x)
                        for x in range(
                            min(new_pos[1], new_pos2[1]),
                            max(new_pos[1], new_pos2[1]) + 1,
                        )
                    ]
                )
            )
        elif new_pos2[1] == new_pos[1]:
            greens_list.update(
                set(
                    [
                        (x, new_pos[1])
                        for x in range(
                            min(new_pos[0], new_pos2[0]),
                            max(new_pos[0], new_pos2[0]) + 1,
                        )
                    ]
                )
            )
    new_pos = (new_y_list.index(pos[0]), new_x_list.index(pos[1]))
    new_pos2 = (new_y_list.index(pos2[0]), new_x_list.index(pos2[1]))
    min_y = min(new_pos[0], new_pos2[0])
    min_x = min(new_pos[1], new_pos2[1])
    max_y = max(new_pos[0], new_pos2[0])
    max_x = max(new_pos[1], new_pos2[1])
    for x in range(min_x, max_x + 1):
        if (
            (min_y, x) not in greens_list and not is_inside((min_y, x), new_pos_list)
        ) or (
            (max_y, x) not in greens_list and not is_inside((max_y, x), new_pos_list)
        ):
            return False
    for y in range(min_y, max_y + 1):
        if (
            (y, min_x) not in greens_list and not is_inside((y, min_x), new_pos_list)
        ) or (
            (y, max_x) not in greens_list and not is_inside((y, max_x), new_pos_list)
        ):
            return False
    return True


def print_grid(pos_list: List[POS], greens_list: List[POS]) -> None:
    """Print grid for debug purposes"""
    max_y = max(x[0] for x in pos_list)
    max_x = max(x[1] for x in pos_list)
    pic = ""
    for y in range(max_y + 2):
        for x in range(max_x + 2):
            if (y, x) in greens_list:
                pic += "#"
            else:
                pic += "."
        pic += "\n"
    print(pic)


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2025/inputs/09_test.txt", 1) == 50
    assert main_func("aoc/aoc_2025/inputs/09.txt", 1) == 4763509452
    # # Part 2
    assert main_func("aoc/aoc_2025/inputs/09_test.txt", 2) == 24
    assert main_func("aoc/aoc_2025/inputs/09.txt", 2) == 1516897893


if __name__ == "__main__":
    main()
