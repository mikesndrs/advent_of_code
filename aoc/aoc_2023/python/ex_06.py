"""https://adventofcode.com/2023/day/6"""


def list_from_line(line: str, version: int) -> list[int]:
    preprocessed_line = line.split(":")[1].strip().split(" ")
    int_list = [x.strip() for x in preprocessed_line if len(x) > 0]
    if version == 1:
        return [int(x) for x in int_list]
    else:
        return [int("".join(int_list))]


def count_winning_permutations(time: int, distance: int) -> int:
    last_pos = 0
    j = round((time + 1) / 2) // 2
    step = j // 2
    for _ in range(time + 1):
        dist = j * (time - j)
        if dist > distance:
            last_pos = int(j)
            j -= step
        else:
            j += step
        if step == 0:
            break
        step //= 2
    return time + 1 - (2 * last_pos)


def product_race_winners(input_filename: str, version: int) -> int:
    with open(input_filename) as f:
        for line in f:
            if "Time" in line:
                times = list_from_line(line, version)
            elif "Distance" in line:
                distances = list_from_line(line, version)
    ctrs = []
    for i in range(len(times)):
        ctrs.append(count_winning_permutations(times[i], distances[i]))
    result = 1
    for ctr in ctrs:
        result *= ctr
    print(result)

    return result


def main() -> None:
    # Part 1
    assert product_race_winners("aoc/aoc_2023/inputs/06_test.txt", 1) == 288
    assert product_race_winners("aoc/aoc_2023/inputs/06.txt", 1) == 211904
    # Part 2
    assert product_race_winners("aoc/aoc_2023/inputs/06_test.txt", 2) == 71503
    assert product_race_winners("aoc/aoc_2023/inputs/06.txt", 2) == 43364472


if __name__ == "__main__":
    main()
