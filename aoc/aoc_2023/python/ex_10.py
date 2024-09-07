"""https://adventofcode.com/2023/day/10"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple

debug = True

pipe_dict = {
    "-": ["l", "r"],
    "|": ["u", "d"],
    "L": ["u", "r"],
    "J": ["u", "l"],
    "7": ["d", "l"],
    "F": ["d", "r"],
    "S": ["d", "u", "l", "r"],
    ".": [],
}


@dataclass
class Node:
    char: str
    x: int
    y: int
    shortest_walk: int = int(1e15)
    double: bool = False
    neighbors: List["Node"] = field(default_factory=list)


class Graph:
    def __init__(self, filename: str) -> None:
        self.nodes: Dict[Tuple[int, int], Node] = {}
        self.build_graph(filename)

    def build_graph(self, filename: str) -> None:
        # build grid
        with open(filename, mode="r") as f:
            grid = f.readlines()
        n = len(grid) * len(grid[0])
        # build nodes
        for y, line in enumerate(grid):
            for x, char in enumerate(line.strip()):
                node = Node(
                    char=char,
                    x=x,
                    y=y,
                    shortest_walk=n,
                    double=False,
                    neighbors=[],
                )
                if char == "S":
                    node.shortest_walk = 0
                self.nodes[(x, y)] = node
        # connect nodes
        w, h = self.graph_dims()
        for y in range(h):
            for x in range(w):
                node = self.nodes[(x, y)]
                if x < w - 1:
                    nbr_r = self.nodes[(x + 1, y)]
                    if "r" in pipe_dict[node.char] and "l" in pipe_dict[nbr_r.char]:
                        node.neighbors.append(nbr_r)
                        nbr_r.neighbors.append(node)
                if y < h - 1:
                    nbr_u = self.nodes[(x, y + 1)]
                    if "d" in pipe_dict[node.char] and "u" in pipe_dict[nbr_u.char]:
                        node.neighbors.append(nbr_u)
                        nbr_u.neighbors.append(node)
                self.nodes[(x, y)] = node

    def walk_graph(self) -> None:
        new_nodes = [node for node in self.nodes.values() if node.char == "S"]
        for i in range(len(self.nodes)):
            old_nodes = [node for node in new_nodes]
            new_nodes = []
            # find shortest_walk == i nodes
            for node in old_nodes:
                for nbr in node.neighbors:
                    if i + 1 == nbr.shortest_walk:
                        nbr.double = True
                    if nbr.shortest_walk > i + 1:
                        nbr.shortest_walk = i + 1
                        new_nodes.append(nbr)
            # break loop if no new nodes found
            if len(new_nodes) == 0:
                break

    def draw_loop(self) -> None:
        w, h = self.graph_dims()
        loop_draw = ["." * w] * h
        for i in range(self.max_dist() + 1):
            from_nodes = [
                node for node in self.nodes.values() if node.shortest_walk == i
            ]
            for node in from_nodes:
                start = loop_draw[node.y][: node.x]
                end = loop_draw[node.y][node.x + 1 :]
                loop_draw[node.y] = start + str(node.char) + end
        print("\n".join(loop_draw) + "\n")

    def calc_enclosed(self) -> int:
        w, h = self.graph_dims()

        part_of_loop = [[False for _ in range(w)] for _ in range(h)]
        loop = self.get_loop()
        for node in loop:
            part_of_loop[node.y][node.x] = True

        count_x_grid = [[False for _ in range(w)] for _ in range(h)]
        count_y_grid = [[False for _ in range(w)] for _ in range(h)]
        for y in range(h):
            count_x = False
            for x in range(w):
                # has upper neighbor
                if any(
                    [
                        nbr.y > y and part_of_loop[y][x]
                        for nbr in self.nodes[(x, y)].neighbors
                    ]
                ):
                    count_x = not count_x
                if count_x:
                    count_x_grid[y][x] = True
        for x in range(w):
            count_y = False
            for y in range(h):
                # has right neighbor
                if any(
                    [
                        nbr.x > x and part_of_loop[y][x]
                        for nbr in self.nodes[(x, y)].neighbors
                    ]
                ):
                    count_y = not count_y
                if count_y:
                    count_y_grid[y][x] = True

        res = 0
        for node in self.nodes.values():
            y = node.y
            x = node.x
            if not part_of_loop[y][x] and (count_y_grid[y][x] and count_x_grid[y][x]):
                res += 1
        return res

    def max_dist(self) -> int:
        return max(node.shortest_walk for node in self.nodes.values() if node.double)

    def end_node(self) -> Node:
        max_dist = self.max_dist()
        end_node = [
            node
            for node in self.nodes.values()
            if node.shortest_walk == max_dist and node.double
        ][0]
        return end_node

    def get_loop(self) -> List[Node]:
        end_node = self.end_node()
        loop = []
        new_nodes = [end_node]
        i = end_node.shortest_walk
        for i in range(end_node.shortest_walk, -1, -1):
            old_nodes = [node for node in new_nodes]
            new_nodes = []
            for node in old_nodes:
                for nbr in node.neighbors:
                    if nbr.shortest_walk == i - 1:
                        new_nodes.append(nbr)
                        loop.append(nbr)
        return loop

    def graph_dims(self) -> Tuple[int, int]:
        w = max(node.x for node in self.nodes.values()) + 1
        h = max(node.y for node in self.nodes.values()) + 1
        return w, h


def main_func(filename: str, version: int) -> int:
    graph = Graph(filename)
    graph.walk_graph()
    # graph.draw_loop()
    if version == 1:
        result = graph.max_dist()
    else:
        result = graph.calc_enclosed()
    print(result)
    return result


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2023/inputs/10_test.txt", 1) == 4
    assert main_func("aoc/aoc_2023/inputs/10_test_2.txt", 1) == 8
    assert main_func("aoc/aoc_2023/inputs/10.txt", 1) == 7086
    # # Part 2
    assert main_func("aoc/aoc_2023/inputs/10_test.txt", 2) == 1
    assert main_func("aoc/aoc_2023/inputs/10_test_2.txt", 2) == 1
    assert main_func("aoc/aoc_2023/inputs/10_test_3.txt", 2) == 4
    assert main_func("aoc/aoc_2023/inputs/10.txt", 2) == 317


if __name__ == "__main__":
    main()
