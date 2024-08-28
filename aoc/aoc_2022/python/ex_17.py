"""https://adventofcode.com/2022/day/17"""
import numpy as np

rockshapes_list = [
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]],
    [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]],
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [0, 1], [1, 0], [1, 1]],
]

input_filename = "2022/inputs/17.txt"
starting_position = [2, 4]
x_bounds = [0, 6]
width = x_bounds[1] + x_bounds[0] + 1


def gust():
    with open(input_filename) as f:
        line = f.readlines()[0].strip()
        n = len(line)
    gust_dir = {"<": -1, ">": 1}
    i = 0
    while True:
        yield [gust_dir[line[i]], (i + 1) % n]
        i = (i + 1) % n


def rock_shapes():
    i = 0
    n = len(rockshapes_list)
    while True:
        yield [rockshapes_list[i].copy(), (i + 1) % n]
        i = (i + 1) % n


def main(n_rocks):
    rm_ctr = np.int64(0)
    rock_pile = [[True] * width]
    gust_gen = gust()
    rock_shapes_gen = rock_shapes()
    rep_list = []
    rep_list_2 = []
    rock_i = 0
    jumped = False
    while rock_i < n_rocks:
        falling_rock, rock_shapes_i = next(rock_shapes_gen)
        highest_rock = max([i for i, x in enumerate(rock_pile) if any(x)])
        while len(rock_pile) < highest_rock + starting_position[1] + 4:
            rock_pile.append([False] * width)
        for i, (x, y) in enumerate(falling_rock):
            falling_rock[i] = [
                x + starting_position[0],
                y + starting_position[1] + highest_rock,
            ]
        falling = True
        while falling:
            # blow horizontally
            gust_dir, gust_i = next(gust_gen)
            if all(
                [
                    min([x[0] for x in falling_rock]) + gust_dir >= x_bounds[0],
                    max([x[0] for x in falling_rock]) + gust_dir <= x_bounds[1],
                ]
            ):
                if all(
                    [rock_pile[y][x + gust_dir] is False for (x, y) in falling_rock]
                ):
                    for i, (x, y) in enumerate(falling_rock):
                        falling_rock[i][0] = x + gust_dir
            # fall vertically
            for i, (x, y) in enumerate(falling_rock):
                if rock_pile[y - 1][x] == True:
                    falling = False
            if falling:
                for i, (x, y) in enumerate(falling_rock):
                    falling_rock[i][1] -= 1
            else:
                for x, y in falling_rock:
                    rock_pile[y][x] = True
                # remove from list
                beep = max([i for i, x in enumerate(rock_pile) if all(x)])
                if beep > 0:
                    if [beep, gust_i, rock_shapes_i] in rep_list and jumped is False:
                        rep_idx = rep_list.index([beep, gust_i, rock_shapes_i])
                        rep_n = rock_i - rep_list_2[rep_idx]
                        boop = (n_rocks - rock_i) // rep_n
                        rm_ctr += boop * sum([x[0] for x in rep_list[rep_idx:]])
                        rock_i += boop * rep_n
                        jumped = True
                    rep_list.append([beep, gust_i, rock_shapes_i])
                    rep_list_2.append(rock_i)
                del rock_pile[:beep]
                rm_ctr += beep
                highest_rock = max([i for i, x in enumerate(rock_pile) if any(x)])
        rock_i += 1
    print(np.int64(rm_ctr + highest_rock))


def print_rocks(rock_pile, falling_rock, highest_rock):
    for y in range(len(rock_pile) - 1, -1, -1):
        print(
            "".join(
                [
                    "#"
                    if rock_pile[y][x] is True
                    else "$"
                    if [x, y] in falling_rock
                    else "."
                    for x in range(x_bounds[0], x_bounds[1] + 1)
                ]
            )
        )
    print("-" * width)


if __name__ == "__main__":
    n_rocks = 2022
    main(n_rocks)
    n_rocks = np.int64(1e12)
    main(n_rocks)
