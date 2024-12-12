"""https://adventofcode.com/2024/day/12"""

from dataclasses import dataclass
from typing import Dict, List, Set, Tuple


@dataclass
class Region:
    """Region inside grid"""

    char: str
    locations: Set[Tuple[int, int]]
    perimeter: int = 0
    sides: int = 0

    def area(self) -> int:
        return len(self.locations)

    def price(self, version: int) -> int:
        if version == 1:
            price = self.area() * self.perimeter
        else:
            price = self.area() * self.sides
        return price


def handle_input(input_filename: str) -> List[str]:
    """Get grid of chars from raw input"""
    grid = []
    with open(input_filename, "r") as f:
        grid = [x.strip() for x in f.readlines()]
    return grid


def get_neighbors(
    y: int, x: int, grid: List[str]
) -> List[Tuple[int, int, Tuple[int, int]]]:
    """Get location and direction of neighboring chars in same region"""
    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1
    neighbors = []
    for dy, dx in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        new_y = y + dy
        new_x = x + dx
        if (
            (0 <= new_y <= max_y)
            and (0 <= new_x <= max_x)
            and grid[y][x] == grid[new_y][new_x]
        ):
            neighbors.append((new_y, new_x, (dy, dx)))
    return neighbors


def get_regions(grid: List[str]) -> List[Region]:
    """Get list of regions of same char"""
    regions = []
    perimeters: Dict[Tuple[int, int], List[Tuple[int, int]]] = {}
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if (y, x) in perimeters.keys():
                continue
            queue = [(y, x)]
            region = Region(
                char=char,
                locations=set(),
            )
            while len(queue) > 0:
                y_cur, x_cur = queue[0]
                if not (y_cur, x_cur) in perimeters:
                    neighbors = get_neighbors(y_cur, x_cur, grid)
                    perimeters[(y_cur, x_cur)] = [neighbor[2] for neighbor in neighbors]
                    region.locations.add((y_cur, x_cur))
                    region.perimeter += 4 - len(neighbors)
                    queue += [neighbor[:2] for neighbor in neighbors]
                queue.pop(0)
            regions.append(region)

    for region in regions:
        region.sides = region.perimeter
        for y, x in region.locations:
            if x > 0:
                if (y, x - 1) in region.locations:
                    for dir in [(-1, 0), (1, 0)]:
                        if (
                            dir not in perimeters[(y, x - 1)]
                            and dir not in perimeters[(y, x)]
                        ):
                            region.sides -= 1
            if y > 0:
                if (y - 1, x) in region.locations:
                    for dir in [(0, -1), (0, 1)]:
                        if (
                            dir not in perimeters[(y - 1, x)]
                            and dir not in perimeters[(y, x)]
                        ):
                            region.sides -= 1
    return regions


def main_func(input_filename: str, version: int) -> int:
    """Main function"""
    grid = handle_input(input_filename)
    regions = get_regions(grid)
    result = 0
    for region in regions:
        result += region.price(version)
    print(result)
    return result


def main() -> None:
    """Top level function"""
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/12_test.txt", 1) == 1930
    assert main_func("aoc/aoc_2024/inputs/12.txt", 1) == 1387004
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/12_test.txt", 2) == 1206
    assert main_func("aoc/aoc_2024/inputs/12.txt", 2) == 844198


if __name__ == "__main__":
    main()
