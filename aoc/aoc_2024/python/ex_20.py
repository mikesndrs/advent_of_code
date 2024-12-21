"""https://adventofcode.com/2024/day/20"""

from typing import Dict, List, Tuple

INT_INF = int(2**16)
POS = Tuple[int, int]


class Grid:
    def __init__(self, input_filename: str, version: int) -> None:
        self.version = version
        self.walls = set()
        with open(input_filename, "r") as f:
            for y, line in enumerate(f):
                if len(line.strip()) > 0:
                    self.max_y = y
                    self.max_x = len(line.strip()) - 1
                for x, char in enumerate(line.strip()):
                    if char == "S":
                        self.start = (x, y)
                    elif char == "E":
                        self.end = (x, y)
                    elif char == "#":
                        self.walls.add((x, y))

    def walk(
        self, start: POS, cheat_mode: bool = False, max_dist: int = INT_INF
    ) -> Dict[POS, int]:
        queue = [start]
        dist = {start: 0}
        while len(queue) > 0:
            pos = queue.pop(0)
            for x, y in self.get_neighbors(pos):
                if any(
                    [
                        x < 0,
                        y < 0,
                        x > self.max_x,
                        y > self.max_y,
                        dist[pos] + 1 > max_dist,
                    ]
                ):
                    continue
                old_dist = dist.get((x, y), INT_INF)
                if dist[pos] + 1 < old_dist:
                    dist[(x, y)] = dist[pos] + 1
                    if cheat_mode or ((x, y) not in self.walls):
                        queue.append((x, y))
        return dist

    def count_shortcuts(self, cutoff: int, version: int) -> int:
        dist_s = self.walk(self.start)
        dist_e = self.walk(self.end)

        result = 0
        if version == 1:
            cheat_time = 2
        else:
            cheat_time = 20
        for pos in dist_s.keys() - self.walls:
            dist_wall = self.walk(pos, cheat_mode=True, max_dist=cheat_time)
            for end_pos in dist_wall.keys() - self.walls:
                new_dist = dist_s[pos] + dist_wall[end_pos] + dist_e[end_pos]
                if dist_wall[end_pos] <= cheat_time:
                    if dist_s[self.end] - new_dist >= cutoff:
                        result += 1
        return result

    def get_neighbors(self, pos: POS) -> List[POS]:
        nbrs = []
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nbrs.append((pos[0] + dx, pos[1] + dy))
        return nbrs


def main_func(input_filename: str, version: int, cutoff: int) -> int:
    grid = Grid(input_filename, version)
    result = grid.count_shortcuts(cutoff, version)
    print(cutoff, result)
    return result


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/20_test.txt", 1, 5) == 16
    assert main_func("aoc/aoc_2024/inputs/20_test.txt", 1, 20) == 5
    assert main_func("aoc/aoc_2024/inputs/20.txt", 1, 100) == 1307
    # Part 2
    assert main_func("aoc/aoc_2024/inputs/20_test.txt", 2, 60) == 129
    assert main_func("aoc/aoc_2024/inputs/20_test.txt", 2, 70) == 41
    assert main_func("aoc/aoc_2024/inputs/20_test.txt", 2, 72) == 29
    assert main_func("aoc/aoc_2024/inputs/20_test.txt", 2, 74) == 7
    assert main_func("aoc/aoc_2024/inputs/20_test.txt", 2, 76) == 3
    assert main_func("aoc/aoc_2024/inputs/20.txt", 2, 100) == 986545


if __name__ == "__main__":
    main()
