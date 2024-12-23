"""https://adventofcode.com/2024/day/16"""

from typing import Dict, Set, Tuple

POS = Tuple[int, int]

dir_dict = {
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
}

opposite_dict = {
    "v": "^",
    "<": ">",
    ">": "<",
    "^": "v",
}


class Path:
    """Object holding path and its score inside a grid"""

    score: int
    path: Set[Tuple[POS, str]]

    def __init__(self, score: int, path: Set[Tuple[POS, str]]):
        self.score = score
        self.path: Set[Tuple[POS, str]] = path


class Grid:
    """Object representing grid and the ways to walk through it"""

    def __init__(self, input_filename: str, version: int):
        self.start = (0, 0)
        self.end = (0, 0)
        self.walls = set()
        with open(input_filename, "r") as f:
            for y, line in enumerate(f):
                for x, char in enumerate(line.strip()):
                    if char == "S":
                        self.start = (x, y)
                    elif char == "E":
                        self.end = (x, y)
                    elif char == "#":
                        self.walls.add((x, y))
        self.shortest_paths: Dict[Tuple[POS, str], Path] = {}
        self.shortest_paths[(self.start, ">")] = Path(0, set([(self.start, ">")]))
        self.queue = [(self.start, ">")]

    def walk(self) -> None:
        """Walk every possible path through grid to find the quickest way to get from
        the start to a given point"""
        while len(self.queue) > 0:
            pos, dir = self.queue.pop(0)
            for new_dir in ["<", ">", "v", "^"]:
                self.step(pos, dir, new_dir)

    def step(self, pos: POS, dir: str, new_dir: str) -> None:
        """Take a single step from a given position and orientatien in a given
        direction"""
        path = self.shortest_paths[(pos, dir)]
        curr_score = path.score
        curr_path = path.path
        if new_dir == dir:
            new_x = pos[0] + dir_dict[dir][0]
            new_y = pos[1] + dir_dict[dir][1]
            new_score = curr_score + 1
        elif new_dir == opposite_dict[dir]:
            new_x, new_y = pos
            new_score = curr_score + 2000
        else:
            new_x, new_y = pos
            new_score = curr_score + 1000
        if (new_x, new_y) not in self.walls:
            if (
                self.shortest_paths.get(
                    ((new_x, new_y), new_dir), Path(int(1e10), set())
                ).score
                > new_score
            ):
                self.shortest_paths[((new_x, new_y), new_dir)] = Path(
                    new_score, curr_path | set([((new_x, new_y), new_dir)])
                )
                self.queue.append(((new_x, new_y), new_dir))
            elif (
                self.shortest_paths.get(
                    ((new_x, new_y), new_dir), Path(int(1e10), set())
                ).score
                == new_score
            ):
                new_path = (
                    self.shortest_paths[((new_x, new_y), new_dir)].path | curr_path
                )
                self.shortest_paths[((new_x, new_y), new_dir)] = Path(
                    new_score, new_path
                )

    def shortest_path(self) -> int:
        """Calculate length of shortest path to end out of all possible paths"""
        return min(
            [
                self.shortest_paths[(self.end), char].score
                for char in ["<", ">", "v", "^"]
            ]
        )

    def cumulative_length_shortest_paths(self) -> int:
        """Calculate length of all grid positions that are part of a shortest path to
        the end"""
        a = [self.shortest_paths[(self.end), char] for char in ["<", ">", "v", "^"]]
        el = next((p for p in a if p.score == self.shortest_path()))
        path_set: Set[POS] = set()
        for beep in el.path:
            new_el = self.shortest_paths[beep]
            path_set = path_set | set([x[0] for x in new_el.path])
        count = len(path_set)
        return count


def main_func(input_filename: str, version: int) -> int:
    """Main function"""
    grid = Grid(input_filename, version)
    grid.walk()
    if version == 1:
        result = grid.shortest_path()
    else:
        result = grid.cumulative_length_shortest_paths()
    print(result)
    return result


def main() -> None:
    """Top level function"""
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/16_test_small.txt", 1) == 7036
    assert main_func("aoc/aoc_2024/inputs/16_test.txt", 1) == 11048
    assert main_func("aoc/aoc_2024/inputs/16.txt", 1) == 79404
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/16_test_small.txt", 2) == 45
    assert main_func("aoc/aoc_2024/inputs/16_test.txt", 2) == 64
    assert main_func("aoc/aoc_2024/inputs/16.txt", 2) == 451


if __name__ == "__main__":
    main()
