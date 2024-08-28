"""https://adventofcode.com/2022/day/14"""


def build_grid():
    input_filename = "2022/inputs/14.txt"
    with open(input_filename) as f:
        rock_set = set()
        for line in f:
            sl = line.strip().split(" -> ")
            n = len(sl) - 1
            for i in range(n):
                start = [int(x) for x in sl[i].split(",")]
                end = [int(x) for x in sl[i + 1].split(",")]
                if start[0] == end[0]:
                    min_y = min(start[1], end[1])
                    max_y = max(start[1], end[1])
                    for y in range(min_y, max_y + 1):
                        rock_set.add((start[0], y))
                else:
                    min_x = min(start[0], end[0])
                    max_x = max(start[0], end[0])
                    for x in range(min_x, max_x + 1):
                        rock_set.add((x, start[1]))
    return rock_set


def sand(version=1):
    rock_set = build_grid()
    sand_spawn = [500, 0]
    lowest_rock = max([rock[1] for rock in rock_set])
    leftmost_rock = min([rock[0] for rock in rock_set])
    rightmost_rock = max([rock[0] for rock in rock_set])
    if version == 2:
        for x in range(-2 * (lowest_rock + 2), 2 * (lowest_rock + 3)):
            rock_set.add((sand_spawn[0] + x, lowest_rock + 2))
    grid_size = (lowest_rock - 0 + 1) * (rightmost_rock - leftmost_rock + 1)
    for ctr in range(grid_size**2):
        sand_x = sand_spawn[0]
        for i in range(lowest_rock + 4):
            if version == 1 and i == lowest_rock:
                return ctr
            if (sand_x, i + 1) not in rock_set:
                continue
            elif (sand_x - 1, i + 1) not in rock_set:
                sand_x -= 1
                continue
            elif (sand_x + 1, i + 1) not in rock_set:
                sand_x += 1
                continue
            if version == 2 and i == 0:
                return ctr + 1
            rock_set.add((sand_x, i))
            break
    raise ValueError("Didn't work :(")


def main():
    result1 = sand()
    print(result1)
    result2 = sand(version=2)
    print(result2)


if __name__ == "__main__":
    main()
