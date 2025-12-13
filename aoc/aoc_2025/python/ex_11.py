"""https://adventofcode.com/2025/day/11"""

from typing import Dict, List

CONNECT_GRAPH = Dict[str, Dict]


def handle_input(input_filename: str) -> CONNECT_GRAPH:
    """Get graph with incoming and outgoing connections per node"""
    input_graph: CONNECT_GRAPH = {}
    with open(input_filename, "r") as f:
        for line in f:
            orig = line.strip().split(":")[0]
            dest = line.strip().split(":")[1]
            for key in dest.strip().split(" "):
                input_graph[orig] = input_graph.get(orig, {"in": [], "out": []})
                input_graph[key] = input_graph.get(key, {"in": [], "out": []})
                input_graph[orig]["out"].append(key)
                input_graph[key]["in"].append(orig)
    return input_graph


def main_func(input_filename: str, version: int) -> int:
    """Check how many options are available to go from a to b"""
    connect_graph = handle_input(input_filename)
    if version == 1:
        routes = [
            ["you", "out"],
        ]
    else:
        routes = [
            ["svr", "fft"],
            ["fft", "dac"],
            ["dac", "out"],
        ]

    order_list = get_order_list(connect_graph)

    res = 1
    for start, end in routes:
        count_graph = {start: 1}
        for key in order_list:
            if key not in count_graph:
                continue
            for dest in connect_graph.get(key, {"out": []})["out"]:
                count_graph[dest] = count_graph.get(dest, 0) + count_graph.get(key, 0)
            if key == end:
                break
        res *= count_graph.get(end, 0)
    print(res)
    return res


def get_order_list(connect_graph: CONNECT_GRAPH) -> List[str]:
    """Get order of connection graph. Assumes no cycles"""
    queue = [key for key in connect_graph if len(connect_graph[key]["in"]) == 0]
    order = []
    while queue:
        point = queue.pop(0)
        order.append(point)
        for dest in connect_graph[point]["out"]:
            connect_graph[dest]["in"].remove(point)
            if len(connect_graph[dest]["in"]) == 0:
                queue.append(dest)
    return order


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2025/inputs/11_test.txt", 1) == 5
    assert main_func("aoc/aoc_2025/inputs/11.txt", 1) == 749
    # Part 2
    assert main_func("aoc/aoc_2025/inputs/11_test2.txt", 2) == 2
    assert main_func("aoc/aoc_2025/inputs/11.txt", 2) == 420257875695750


if __name__ == "__main__":
    main()
