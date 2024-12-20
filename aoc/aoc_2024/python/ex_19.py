"""https://adventofcode.com/2024/day/19"""

from typing import Dict, List, Set


class Beep:
    def __init__(self, input_filename: str, version: int):
        self.version = version
        self.towels: Set[str] = set()
        self.count_dict: Dict[str, int] = {}
        self.patterns: List[str] = []
        with open(input_filename, "r") as f:
            for i, line in enumerate(f):
                if i == 0:
                    for x in line.split(","):
                        self.towels.add(x.strip())
                elif len(line.strip()) > 0:
                    self.patterns.append(line.strip())

    def pattern_possible(self, pattern: str) -> int:
        if pattern in self.count_dict:
            count = self.count_dict[pattern]
        else:
            count = 0
            if pattern in self.towels:
                count = 1
            for towel in self.towels:
                if pattern.startswith(towel):
                    beep = self.pattern_possible(pattern[len(towel) :])
                    if beep:
                        count += beep
            self.count_dict[pattern] = count
        return count

    def count_valid_patterns(self) -> int:
        count = 0
        for pattern in self.patterns:
            if self.version == 1:
                if self.pattern_possible(pattern):
                    count += 1
            else:
                beep = self.pattern_possible(pattern)
                count += beep
        return count


def main_func(input_filename: str, version: int) -> int:
    beep = Beep(input_filename, version)
    result = beep.count_valid_patterns()
    print(result)
    return result


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/19_test.txt", 1) == 6
    assert main_func("aoc/aoc_2024/inputs/19.txt", 1) == 311
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/19_test.txt", 2) == 16
    assert main_func("aoc/aoc_2024/inputs/19.txt", 2) == 616234236468263


if __name__ == "__main__":
    main()
