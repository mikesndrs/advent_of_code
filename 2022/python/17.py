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
        # line = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
        n = len(line)
    gust_dir = {"<": -1, ">": 1}
    i = 0
    while True:
        yield gust_dir[line[i]]
        i = (i + 1) % n


def rock_shapes():
    i = 0
    n = len(rockshapes_list)
    while True:
        yield rockshapes_list[i].copy()
        i = (i + 1) % n


def main(n_rocks):
    rock_pile = [[x, 0] for x in range(x_bounds[0], x_bounds[1] + 1)]
    highest_rock = 0
    gust_gen = gust()
    rock_shapes_gen = rock_shapes()
    for rock_i in range(n_rocks):
        falling_rock = next(rock_shapes_gen)
        for i, (x, y) in enumerate(falling_rock):
            falling_rock[i] = [
                x + starting_position[0],
                y + starting_position[1] + highest_rock,
            ]
        min_x = min([x[0] for x in falling_rock])
        max_x = max([x[0] for x in falling_rock])
        falling = True
        while falling:
            # blow horizontally
            gust_dir = next(gust_gen)
            if all(
                [
                    min_x + gust_dir >= x_bounds[0],
                    max_x + gust_dir <= x_bounds[1],
                    all(
                        [[x + gust_dir, y] not in rock_pile for (x, y) in falling_rock]
                    ),
                ]
            ):
                for i, (x, y) in enumerate(falling_rock):
                    falling_rock[i][0] = x + gust_dir
                min_x = min([x[0] for x in falling_rock])
                max_x = max([x[0] for x in falling_rock])
            # fall vertically
            for i, (x, y) in enumerate(falling_rock):
                if [x, y - 1] in rock_pile:
                    falling = False
            if falling:
                for i, (x, y) in enumerate(falling_rock):
                    falling_rock[i][1] -= 1
            else:
                for x in falling_rock:
                    rock_pile.append(x)
                highest_rock = max(highest_rock, max([x[1] for x in falling_rock]))
                # remove from list
                for y in range(highest_rock):
                    if len([x for rock in rock_pile if rock[1] == y]) == width:
                        highest_full_y = y
                rock_pile = list(filter(lambda rock: rock[1] >= highest_full_y, rock_pile))

    print(highest_rock)


def print_rocks(rock_pile, falling_rock, highest_rock):
    for i in range(highest_rock + 1 + 5):
        y = highest_rock + 5 - i
        print(
            "".join(
                [
                    "#"
                    if [x, y] in rock_pile
                    else "$"
                    if [x, y] in falling_rock
                    else "."
                    for x in range(x_bounds[0], x_bounds[1] + 1)
                ]
            )
        )


if __name__ == "__main__":
    n_rocks = 2022
    main(n_rocks)
    # n_rocks = int(1e12)
    # main(n_rocks)
