"""https://adventofcode.com/2024/day/06"""

from typing import List, Set, Tuple

OBSTACLE = Tuple[int, int]
POSITION = Tuple[int, int]


def handle_input(input_filename: str) -> Tuple[Set[OBSTACLE], POSITION, List[int]]:
    """Obtain set of obstacles, starting position and grid size from raw input"""
    grid_size = [0, 0]
    obstacles = set()
    position = (0, 0)
    with open(input_filename, "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                grid_size[1] = len(line.strip())
            if len(line) > 0:
                grid_size[0] += 1
            for j, x in enumerate(line.strip()):
                if x == "#":
                    obstacles.add((i, j))
                elif x == "^":
                    position = (i, j)
    return obstacles, position, grid_size


def walk_path(
    obstacles: Set[OBSTACLE], position: POSITION, grid_size: List[int]
) -> Tuple[Set[POSITION], bool]:
    """
    Walk the path and return both the visited positions as well as whether the
    path is successfully finished without loops
    """
    positions = set()
    success = True
    turn_positions = set()
    direction = "up"
    while (0 <= position[0] <= grid_size[0] - 1) and (
        0 <= position[1] <= grid_size[1] - 1
    ):
        positions.add(position)
        next_position = (
            position[0] + move_dict[direction][0],
            position[1] + move_dict[direction][1],
        )
        if next_position in obstacles:
            if (position, direction) in turn_positions:
                return positions, False
            turn_positions.add((position, direction))
            direction = turn_dict[direction]
        else:
            position = next_position
    return positions, success


# Changes in position based on direction
move_dict = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}

# Changes in direction based on direction
turn_dict = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up",
}


def main_func(input_filename: str, version: int) -> int:
    """Main function"""
    obstacles, position, grid_size = handle_input(input_filename)
    if version == 1:
        positions, _ = walk_path(obstacles, position, grid_size)
        result = len(positions)
    if version == 2:
        result = 0
        for i in range(grid_size[0]):
            for j in range(grid_size[1]):
                new_obstacles = obstacles | set([(i, j)])
                _, success = walk_path(new_obstacles, position, grid_size)
                if not success:
                    result += 1
    print(result)
    return result


def main() -> None:
    """Top level function"""
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/06_test.txt", 1) == 41
    assert main_func("aoc/aoc_2024/inputs/06.txt", 1) == 4982
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/06_test.txt", 2) == 6
    assert main_func("aoc/aoc_2024/inputs/06.txt", 2) == 1663


if __name__ == "__main__":
    main()
