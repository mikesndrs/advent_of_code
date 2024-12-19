"""https://adventofcode.com/2024/day/18"""

from typing import Any, Dict, Set, Tuple

INT_INF = int(2**16)


class Grid:
    def __init__(self, input_filename: str, size: int, n_bytes: int) -> None:
        with open(input_filename, "r") as f:
            self.bytes: Set[Tuple[int, int]] = set()
            for i, line in enumerate(f):
                if i < n_bytes:
                    split_line = line.strip().split(",")
                    byte_pos = (int(split_line[0]), int(split_line[1]))
                    self.bytes.add(byte_pos)
                if i == n_bytes - 1:
                    self.last_byte = byte_pos
            self.size = size
            self.dist: Dict[Tuple[int, int], int] = {(0, 0): 0}

    def walk(self) -> int:
        queue = [(0, 0)]
        while len(queue) > 0:
            pos = queue.pop(0)
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                x = pos[0] + dx
                y = pos[1] + dy
                if any(
                    [x < 0, y < 0, x > self.size, y > self.size, (x, y) in self.bytes]
                ):
                    continue
                old_dist = self.dist.get((x, y), INT_INF)
                if self.dist[pos] + 1 < old_dist:
                    queue.append((x, y))
                    self.dist[(x, y)] = self.dist[pos] + 1
        return self.dist.get((self.size, self.size), INT_INF)

    def print_grid(self) -> None:
        grid = ""
        for y in range(self.size + 1):
            for x in range(self.size + 1):
                if (x, y) in self.bytes:
                    grid += "#"
                elif (x, y) in self.dist.keys():
                    grid += "O"
                else:
                    grid += "."
            grid += "\n"
        print(grid)


def main_func(input_filename: str, version: int, size: int, n_bytes: int) -> Any:
    result: Any
    if version == 1:
        grid = Grid(input_filename, size, n_bytes)
        result = grid.walk()
    else:
        for i in range(4000):
            grid = Grid(input_filename, size, i)
            if grid.walk() == INT_INF:
                result = grid.last_byte
                break
    print(result)
    return result


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/18_test.txt", 1, 6, 12) == 22
    assert main_func("aoc/aoc_2024/inputs/18.txt", 1, 70, 1024) == 306
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/18_test.txt", 2, 6, 12) == (6, 1)
    assert main_func("aoc/aoc_2024/inputs/18.txt", 2, 70, 1024) == (38, 63)


if __name__ == "__main__":
    main()
