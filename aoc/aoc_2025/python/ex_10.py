"""https://adventofcode.com/2025/day/10"""

from typing import Dict, List, Tuple

INPUT = List[Dict]
BUTTON = List[int]
CACHE = Dict[Tuple[int, ...], List[int]]


def handle_input(input_filename: str) -> INPUT:
    """Parse raw input to get desired pattern, available buttons, desired switch
    count"""
    input_list = []
    with open(input_filename, "r") as f:
        for line in f:
            new_input: Dict = {"buttons": []}
            for x in line.strip().split(" "):
                if x[0] == "[":
                    x = x.strip("[").strip("]")
                    new_input["target"] = list([char == "#" for char in x])
                elif x[0] == "(":
                    x = x.strip("(").strip(")")
                    new_input["buttons"].append(
                        list(int(char) for char in x.split(","))
                    )
                elif x[0] == "{":
                    x = x.strip("{").strip("}")
                    new_input["mystery"] = list(int(char) for char in x.split(","))
                else:
                    raise RuntimeError("panic")
            input_list.append(new_input)
    return input_list


def main_func(input_filename: str, version: int) -> int:
    """Calculate shortest amount of presses to get given pattern or switch count"""
    input_list = handle_input(input_filename)
    res = 0
    for i, input in enumerate(input_list):
        if version == 1:
            combinations = check_combination(
                input["target"], input["buttons"], [], 0, []
            )
            res += min([len(x) for x in combinations])
        else:
            cache = get_cache(len(input["target"]), input["buttons"], [], 0, {})
            solutions = beep(input["mystery"], input["buttons"], cache)
            print(i, solutions)
            if all(x < 1e5 for x in solutions):
                res += sum(solutions)
    print(res)
    return res


def get_cache(
    n_target: int,
    buttons: List[BUTTON],
    used_buttons: List[BUTTON],
    n: int,
    cache: CACHE,
) -> CACHE:
    """Run all combinations once and cache for later use"""
    if n == len(buttons):
        new_target = [0] * n_target
        new_used_buttons = [0] * len(buttons)
        for button in used_buttons:
            new_used_buttons[buttons.index(button)] += 1
            for x in button:
                new_target[x] += 1
        if sum(new_used_buttons) < sum(cache.get(tuple(new_target), [1e6])):
            cache[tuple(new_target)] = new_used_buttons.copy()
    else:
        cache = get_cache(n_target, buttons, used_buttons, n + 1, cache)
        cache = get_cache(n_target, buttons, used_buttons + [buttons[n]], n + 1, cache)
    return cache


def beep(target: List[int], buttons: List[BUTTON], cache: CACHE) -> List[int]:
    """
    Return possible solutions to get given switch count
    [5,4,3,7] -> [#.##]
    [4,2,2,6] -> 2x [2,1,1,3]
    [2,1,1,3] -> [.###]
    [2,0,0,2] -> 2x [1,0,0,1]
    [1,0,0,1] -> [#..#]
    """
    if all(x == 0 for x in target):
        return [0] * len(buttons)
    else:
        used_buttons = [int(1e6) for x in buttons]
        solutions = check_combination([x % 2 == 1 for x in target], buttons, [], 0, [])
        for solution in solutions:
            new_used_buttons = [0] * len(buttons)
            new_target = target.copy()
            for button in solution:
                new_used_buttons[buttons.index(button)] += 1
                for idx in button:
                    new_target[idx] -= 1
            if any(x < 0 for x in new_target):
                continue
            new_beep = [
                2 * x for x in beep([int(x / 2) for x in new_target], buttons, cache)
            ]
            if any(x > 1e5 for x in new_beep):
                continue
            new_used_buttons = [
                new_used_buttons[i] + new_beep[i] for i in range(len(buttons))
            ]
            if sum(new_used_buttons) < sum(used_buttons):
                used_buttons = new_used_buttons
    return used_buttons


def check_combination(
    target: List[int],
    buttons: List[BUTTON],
    used_buttons: List[BUTTON],
    n: int,
    solutions: List[List[BUTTON]],
) -> List[List[BUTTON]]:
    """Return possible solutions to get given pattern"""
    if n == len(buttons):
        res = [False] * len(target)
        for val in used_buttons:
            for x in val:
                res[x] = not res[x]
        if res == target:
            solutions += [used_buttons]
    else:
        solutions += check_combination(target, buttons, used_buttons, n + 1, [])
        solutions += check_combination(
            target, buttons, used_buttons + [buttons[n]], n + 1, []
        )
    return solutions


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2025/inputs/10_test.txt", 1) == 7
    assert main_func("aoc/aoc_2025/inputs/10.txt", 1) == 502
    # # Part 2
    assert main_func("aoc/aoc_2025/inputs/10_test.txt", 2) == 33
    assert main_func("aoc/aoc_2025/inputs/10.txt", 2) == 21467


if __name__ == "__main__":
    main()
