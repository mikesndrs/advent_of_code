"""https://adventofcode.com/2024/day/23"""

from typing import Any, Dict, Set


def handle_input(input_filename: str) -> Dict[str, Set[str]]:
    connect_dict: Dict[str, Set[str]] = {}
    with open(input_filename) as f:
        for line in f:
            if len(line.strip()) == 0:
                continue
            name_pair = line.strip().split("-")
            for names in [name_pair, list(reversed(name_pair))]:
                connect_dict[names[0]] = connect_dict.get(names[0], set())
                connect_dict[names[0]].add(names[1])
    return connect_dict


def main_func(input_filename: str, version: int) -> Any:
    result: Any
    connect_dict = handle_input(input_filename)
    if version == 1:
        n = 3
    else:
        n = 20

    old_sets = {tuple([key]): values for key, values in connect_dict.items()}
    for i in range(n):
        new_sets = {}
        if i == 0:
            for key, connections in connect_dict.items():
                if key.startswith("t"):
                    new_sets[tuple([key])] = connections
        else:
            for key1, connections in old_sets.items():
                for key2 in connections:
                    new_connect = connections & connect_dict[key2]
                    new_sets[tuple(sorted(list(key1) + [key2]))] = new_connect
        if len(new_sets) == 1:
            result = ",".join(list(new_sets.keys())[0])
            break
        old_sets = new_sets

    if version == 1:
        result = len(new_sets)
    print(result)
    return result


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/23_test.txt", 1) == 7
    assert main_func("aoc/aoc_2024/inputs/23.txt", 1) == 1314
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/23_test.txt", 2) == "co,de,ka,ta"
    assert (
        main_func("aoc/aoc_2024/inputs/23.txt", 2)
        == "bg,bu,ce,ga,hw,jw,nf,nt,ox,tj,uu,vk,wp"
    )


if __name__ == "__main__":
    main()
