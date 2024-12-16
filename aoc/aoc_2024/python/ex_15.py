"""https://adventofcode.com/2024/day/15"""

from typing import Tuple

POS = Tuple[int, int]

dir_dict = {
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
}


class Grid:
    def __init__(self, input_filename: str, version: int) -> None:
        """Set up grid based on raw input data"""
        part = 1
        self.version: int = version
        self.robot: POS = (0, 0)
        self.crates = set()
        self.walls = set()
        self.path = ""
        with open(input_filename, "r") as f:
            for y, line in enumerate(f):
                if len(line.strip()) == 0:
                    part = 2
                elif part == 1 and version == 1:
                    for x, char in enumerate(line):
                        if char == "#":
                            self.walls.add((x, y))
                        elif char == "O":
                            self.crates.add((x, y))
                        elif char == "@":
                            self.robot = (x, y)
                elif part == 1 and version == 2:
                    for x, char in enumerate(line):
                        if char == "#":
                            self.walls.add((2 * x, y))
                            self.walls.add((2 * x + 1, y))
                        elif char == "O":
                            self.crates.add((2 * x, y))
                        elif char == "@":
                            self.robot = (2 * x, y)
                else:
                    self.path += line.strip()

    def move(self, char: str) -> None:
        """Move robot for first version"""
        dx, dy = dir_dict[char]
        new_pos = (self.robot[0] + dx, self.robot[1] + dy)
        if new_pos in self.walls:
            pass
        elif new_pos not in self.crates:
            self.robot = new_pos
        elif self.move_crate(char, new_pos):
            self.robot = new_pos

    def move_crate(self, char: str, pos: POS) -> bool:
        """Iteratively move crates if possible for first version"""
        dx, dy = dir_dict[char]
        new_pos = (pos[0] + dx, pos[1] + dy)
        if new_pos in self.walls:
            return False
        elif new_pos not in self.crates:
            self.crates.remove(pos)
            self.crates.add(new_pos)
            return True
        elif self.move_crate(char, new_pos):
            self.crates.remove(pos)
            self.crates.add(new_pos)
            return True
        return False

    def move_2(self, char: str) -> None:
        """Move robot for second version"""
        dx, dy = dir_dict[char]
        new_pos_1 = (self.robot[0] + dx, self.robot[1] + dy)
        new_pos_2 = (self.robot[0] + dx - 1, self.robot[1] + dy)
        crates_overlap = (
            set([new_pos_1, new_pos_2]).difference(set([self.robot])) & self.crates
        )
        if new_pos_1 in self.walls:
            pass
        elif len(crates_overlap) == 0:
            self.robot = new_pos_1
        elif all(
            [
                self.move_crate_2(char, new_pos, tryout=True)
                for new_pos in crates_overlap
            ]
        ):
            self.robot = new_pos_1
            for new_pos in crates_overlap:
                self.move_crate_2(char, new_pos)

    def move_crate_2(self, char: str, pos: POS, tryout: bool = False) -> bool:
        """Iteratively move crates if possible for second version"""
        dx, dy = dir_dict[char]
        new_pos_1 = (pos[0] + dx, pos[1] + dy)
        new_pos_2 = (pos[0] + dx - 1, pos[1] + dy)
        new_pos_3 = (pos[0] + dx + 1, pos[1] + dy)
        wall_overlap = set([new_pos_1, new_pos_3]) & self.walls
        crates_overlap = (
            set([new_pos_1, new_pos_2, new_pos_3]).difference(set([pos])) & self.crates
        )
        if len(wall_overlap) > 0:
            return False
        elif pos not in self.crates:
            return True
        elif len(crates_overlap) == 0:
            if not tryout:
                self.crates.remove(pos)
                self.crates.add(new_pos_1)
            return True
        elif all(
            [
                self.move_crate_2(char, new_pos, tryout=True)
                for new_pos in crates_overlap
            ]
        ):
            if not tryout:
                for new_pos in crates_overlap:
                    self.move_crate_2(char, new_pos)
                self.crates.remove(pos)
                self.crates.add(new_pos_1)
            return True
        return False

    def score(self) -> int:
        """Calculate scoreof final grid"""
        score = 0
        for x, y in self.crates:
            score += 1 * x + 100 * y
        return score

    def walk_path(self) -> None:
        """Walk given path once"""
        for char in self.path:
            if self.version == 1:
                self.move(char)
            if self.version == 2:
                self.move_2(char)

    def print_grid(self) -> None:
        """Print grid for debugging purposes"""
        max_x = max(x[0] for x in self.walls)
        max_y = max(x[1] for x in self.walls)
        grid = ""
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                if (x, y) == self.robot:
                    grid += "@"
                elif (x, y) in self.walls:
                    grid += "#"
                elif (x, y) in self.crates and self.version == 1:
                    grid += "O"
                elif (x, y) in self.crates and self.version == 2:
                    grid += "["
                elif (x - 1, y) in self.crates and self.version == 2:
                    grid += "]"
                else:
                    grid += "."
            grid += "\n"
        print(grid)


def main_func(input_filename: str, version: int) -> int:
    """Main function"""
    grid = Grid(input_filename, version)
    grid.walk_path()
    result = grid.score()
    print(result)
    return result


def main() -> None:
    """Top level function"""
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/15_test_small.txt", 1) == 2028
    assert main_func("aoc/aoc_2024/inputs/15_test.txt", 1) == 10092
    assert main_func("aoc/aoc_2024/inputs/15.txt", 1) == 1486930
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/15_test.txt", 2) == 9021
    assert main_func("aoc/aoc_2024/inputs/15.txt", 2) == 1492011


if __name__ == "__main__":
    main()
