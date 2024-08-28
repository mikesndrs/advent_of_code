"""https://adventofcode.com/2022/day/12"""


dir_list = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def height(char):
    if char.islower():
        height = ord(char) - ord("a") + 1
    elif char == "S":
        height = 1
    elif char == "E":
        height = ord("z") - ord("a") + 1
    return height


def viable_path(grid, visited_list, row, col, dir):
    row_t = row + dir[0]
    col_t = col + dir[1]
    if any(
        [
            row_t < 0,
            col_t < 0,
            row_t >= len(grid),
            col_t >= len(grid[0]),
            [row_t, col_t] in visited_list,
        ]
    ):
        return False
    if height(grid[row_t][col_t]) - height(grid[row][col]) > 1:
        return False
    return True


def explore_path(input_filename, viable_starter=lambda char: char == "S"):
    grid = []
    reach_grid = []
    visited_list = []
    latest_list = []
    with open(input_filename) as f:
        # for line in temp:
        for line in f:
            if line.strip() != "":
                grid.append([char for char in line.strip()])
                reach_grid.append([None for char in line.strip()])
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if viable_starter(char):
                visited_list.append([row, col])
                latest_list.append([row, col])
                reach_grid[row][col] = 0

    max_n = len(grid) * len(grid[0])
    for i in range(max_n):
        if len(latest_list) == 0:
            break
        old_latest_list = latest_list[:]
        latest_list = []
        for [row, col] in old_latest_list:
            for dir in dir_list:
                if viable_path(grid, visited_list, row, col, dir):
                    row_t = row + dir[0]
                    col_t = col + dir[1]
                    if grid[row_t][col_t] == "E":
                        return i + 1
                    visited_list.append([row_t, col_t])
                    latest_list.append([row_t, col_t])
                    reach_grid[row_t][col_t] = i + 1
    raise Warning("Not found")


def main():
    input_filename = "2022/inputs/12.txt"
    result1 = explore_path(
        input_filename,
    )
    print(result1)
    result2 = explore_path(
        input_filename, viable_starter=lambda char: height(char) == 1
    )
    print(result2)


if __name__ == "__main__":
    main()
