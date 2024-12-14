"""https://adventofcode.com/2024/day/14"""

from typing import List, Tuple


class Robot:
    def __init__(self, pos: Tuple[int, int], vel: Tuple[int, int]) -> None:
        # pos: (x, y)
        self.pos = pos
        self.vel = vel

    def move(self, time: int, grid_size: Tuple[int, int]) -> Tuple[int, int]:
        new_x = (self.pos[0] + time * self.vel[0]) % grid_size[0]
        new_y = (self.pos[1] + time * self.vel[1]) % grid_size[1]
        return (new_x, new_y)


def handle_input(input_filename: str) -> List[Robot]:
    robots = []
    with open(input_filename, "r") as f:
        for line in f:
            pos_str, vel_str = line.strip().split(" ")
            pos = (int(pos_str[2:].split(",")[0]), int(pos_str[2:].split(",")[1]))
            vel = (int(vel_str[2:].split(",")[0]), int(vel_str[2:].split(",")[1]))
            robots.append(Robot(pos, vel))
    return robots


def find_quadrant_product(
    robots: List[Robot], grid_size: Tuple[int, int], time: int
) -> int:
    positions = [robot.move(time, grid_size) for robot in robots]
    result = 0
    quadrant_ctr = {1: 0, 2: 0, 3: 0, 4: 0}
    mid_x = (grid_size[0] - 1) // 2
    mid_y = (grid_size[1] - 1) // 2
    for position in positions:
        if position[0] > mid_x and position[1] < mid_y:
            quadrant_ctr[1] += 1
        elif position[0] > mid_x and position[1] > mid_y:
            quadrant_ctr[2] += 1
        elif position[0] < mid_x and position[1] > mid_y:
            quadrant_ctr[3] += 1
        elif position[0] < mid_x and position[1] < mid_y:
            quadrant_ctr[4] += 1
    result = quadrant_ctr[1] * quadrant_ctr[2] * quadrant_ctr[3] * quadrant_ctr[4]
    return result


def find_tree(robots: List[Robot], grid_size: Tuple[int, int], time: int) -> int:
    positions = [robot.move(time, grid_size) for robot in robots]
    if calc_avg_nbrs(positions) > 1:
        print("!" * grid_size[0])
        print(time)
        grid = [["."] * grid_size[0] for i in range(grid_size[1])]
        for x, y in positions:
            grid[y][x] = "#"
        print("\n".join("".join(line) for line in grid))
        print("!" * grid_size[0])
        return True
    return False


def calc_avg_nbrs(positions: List[Tuple[int, int]]) -> float:
    pos_set = set(positions)
    nbrs_list = []
    for x, y in pos_set:
        nbrs = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if (x + dx, y + dy) in pos_set:
                    nbrs += 1
        nbrs_list.append(nbrs)
    avg_nbrs = sum(nbrs_list) / len(nbrs_list)
    return avg_nbrs


def main_func(input_filename: str, version: int, grid_size: Tuple[int, int]) -> int:
    time = 100
    robots = handle_input(input_filename)
    result = 0
    if version == 1:
        result = find_quadrant_product(robots, grid_size, time)
    else:
        for i in range(int(1e5)):
            if find_tree(robots, grid_size, i):
                result = i
                break

    print(result)
    return result


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/14_test.txt", 1, (11, 7)) == 12
    assert main_func("aoc/aoc_2024/inputs/14.txt", 1, (101, 103)) == 218965032
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/14.txt", 2, (101, 103)) == 7037


if __name__ == "__main__":
    main()
