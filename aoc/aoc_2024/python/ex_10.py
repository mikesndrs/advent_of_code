"""https://adventofcode.com/2024/day/10"""

from typing import List, Set, Tuple

GRID = List[List[int]]


def handle_input(input_filename: str) -> GRID:
    """Get grid from raw input"""
    grid = []
    with open(input_filename, "r") as f:
        for line in f:
            if len(line.strip()) > 0:
                grid.append([int(x) for x in line.strip()])
    return grid


def get_trailheads(grid: GRID) -> List[Tuple[int, int]]:
    """Get list of trailheads from grid"""
    trailheads = []
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == 0:
                trailheads.append((y, x))
    return trailheads


def walk_grid(trailhead: Tuple[int, int], grid: GRID, version: int) -> int:
    """Walk grid from trailhead and see how many viable paths are available"""
    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1
    if version == 1:
        new_queue: Set[Tuple[int, int]] | List[Tuple[int, int]] = set([trailhead])
    else:
        new_queue = [trailhead]
    for i in range(9):
        old_queue = new_queue
        if version == 1:
            new_queue = set()
        else:
            new_queue = []
        for pos in old_queue:
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_y = pos[0] + dy
                new_x = pos[1] + dx
                if (
                    (0 <= new_y <= max_y)
                    and (0 <= new_x <= max_x)
                    and grid[new_y][new_x] == i + 1
                ):
                    if version == 1 and isinstance(new_queue, Set):
                        new_queue.add((new_y, new_x))
                    elif version == 2 and isinstance(new_queue, List):
                        new_queue.append((new_y, new_x))
    return len(new_queue)


def main_func(input_filename: str, version: int) -> int:
    """Main function"""
    grid = handle_input(input_filename)
    trailheads = get_trailheads(grid)
    result = 0
    for trailhead in trailheads:
        result += walk_grid(trailhead, grid, version)
    print(result)
    return result


def main() -> None:
    """Top level function"""
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/10_test.txt", 1) == 36
    assert main_func("aoc/aoc_2024/inputs/10.txt", 1) == 501
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/10_test.txt", 2) == 81
    assert main_func("aoc/aoc_2024/inputs/10.txt", 2) == 1017


if __name__ == "__main__":
    main()
