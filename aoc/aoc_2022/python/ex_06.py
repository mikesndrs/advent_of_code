"""https://adventofcode.com/2022/day/6"""

from typing import Union


def beep(text: str, n: int) -> Union[int, None]:
    nbrs = n - 1
    skip_until = -1
    for i in range(n - 1, len(text)):
        if i < skip_until:
            continue
        match_idx = None
        for j in range(nbrs):
            char = text[i - j]
            string = text[i - nbrs : i - j]
            if char in string:
                match_idx = string.index(char)
                skip_until = i + match_idx + 1
                break
        if match_idx is None:
            return i + 1
    return None


def main() -> None:
    input_filename = "aoc/aoc_2022/inputs/06.txt"
    with open(input_filename) as f:
        text = f.read()
        result1 = beep(text, 4)
        print(result1)
        result2 = beep(text, 14)
        print(result2)


if __name__ == "__main__":
    main()
