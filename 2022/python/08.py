import numpy as np


def viewing_distance(grid, tallest_tree):
    view_dist = 0
    for tree in grid:
        view_dist += 1
        if tree >= tallest_tree:
            break
    return view_dist


def main():
    input_filename = "2022/inputs/08.txt"
    with open(input_filename) as f:
        invisible_trees = 0
        grid = []
        for line in f:
            grid.append([int(x) for x in line.strip()])
    grid = np.array(grid)
    n = len(grid)
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            val = grid[i, j]
            if all(
                [
                    val <= np.max(grid[:i, j]),
                    val <= np.max(grid[i + 1 :, j]),
                    val <= np.max(grid[i, :j]),
                    val <= np.max(grid[i, j + 1 :]),
                ]
            ):
                invisible_trees += 1

    result1 = n**2 - invisible_trees
    print(result1)

    result2 = 0
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            scenic_score = np.prod(
                [
                    viewing_distance(np.flip(grid[:i, j]), grid[i, j]),
                    viewing_distance(grid[i + 1 :, j], grid[i, j]),
                    viewing_distance(np.flip(grid[i, :j]), grid[i, j]),
                    viewing_distance(grid[i, j + 1 :], grid[i, j]),
                ]
            )
            result2 = max([result2, scenic_score])
    print(result2)


if __name__ == "__main__":
    main()
