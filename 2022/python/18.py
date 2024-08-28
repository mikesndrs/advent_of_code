"""https://adventofcode.com/2022/day/18"""


def main(input_filename):
    # get bounds
    with open(input_filename) as f:
        x_max = 0
        y_max = 0
        z_max = 0
        for line in f:
            x, y, z = [int(coor) for coor in line.strip().split(",")]
            x_max = max(x_max, x)
            y_max = max(y_max, y)
            z_max = max(z_max, z)

    # create grid
    grid = [
        [[False for _ in range(z_max + 1)] for _ in range(y_max + 1)]
        for _ in range(x_max + 1)
    ]
    # put in blocks 1 by one and calculate neighbours
    nbr_funcs = [
        lambda x, y, z, grid: x - 1 >= 0 and grid[x - 1][y][z],
        lambda x, y, z, grid: x + 1 <= x_max and grid[x + 1][y][z],
        lambda x, y, z, grid: y - 1 >= 0 and grid[x][y - 1][z],
        lambda x, y, z, grid: y + 1 <= y_max and grid[x][y + 1][z],
        lambda x, y, z, grid: z - 1 >= 0 and grid[x][y][z - 1],
        lambda x, y, z, grid: z + 1 <= z_max and grid[x][y][z + 1],
    ]
    ctr = 0
    with open(input_filename) as f:
        for line in f:
            x, y, z = [int(coor) for coor in line.strip().split(",")]
            grid[x][y][z] = True
            nbrs = 0
            for func in nbr_funcs:
                if func(x, y, z, grid):
                    nbrs += 1
            ctr += 6 - 2 * nbrs
    print(ctr)


if __name__ == "__main__":
    input_filename = "2022/inputs/beep.txt"
    main(input_filename)
    input_filename = "2022/inputs/18_test.txt"
    main(input_filename)
    input_filename = "2022/inputs/18.txt"
    main(input_filename)
