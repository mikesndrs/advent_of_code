#2022_12_12 1st puzzle
input_filename = '2022/inputs/12.txt'
temp = [
    'Sabqponm',
    'abcryxxl',
    'accszExk',
    'acctuvwj',
    'abdefghi',
    '',
]

dir_list = [[0,1],[1,0],[-1,0],[0,-1]]

def height(char):
    if char.islower():
        height = ord(char) - ord('a') + 1
    elif char == 'S':
        height = 1
    elif char == 'E':
        height = ord('z') - ord('a') + 1
    return height

def viable_path(grid, pos, visited_list, dir):
    new_pos = [pos[0] + dir[0], pos[1] + dir[1]]
    if any([
        new_pos[0] < 0,
        new_pos[1] < 0,
        new_pos[0] == len(grid),
        new_pos[1] == len(grid[0]),
    ]):
        return False
    if any([
        abs(height(grid[new_pos[0]][new_pos[1]]) - height(grid[pos[0]][pos[1]])) > 1,
        new_pos in visited_list,
    ]):
        return False
    return True

def explore_path(grid):
    shortest_path = None
    for i, row in enumerate(grid):
        if 'S' in row:
            pos = [i, row.index('S')]
    visited_list = [pos]
    dir_ctr_list = [0]
    while len(dir_ctr_list):
        if dir_ctr_list[-1] == 4:
            dir_ctr_list.pop()
            visited_list.pop()
            continue
        if shortest_path is not None and len(dir_ctr_list) >= shortest_path:
            pos = visited_list.pop()
            continue
        if grid[pos[0]][pos[1]] == 'E':
            shortest_path = len(dir_ctr_list)
            pos = visited_list.pop()
            dir_ctr_list[-1] += 1
            continue
        
        # print(dir_ctr_list)
        dir = dir_list[dir_ctr_list[-1]]
        if viable_path(grid, pos, visited_list, dir):
            pos = [pos[0] + dir[0], pos[1] + dir[1]]
            dir_ctr_list.append(0)
            visited_list.append(pos)
            continue
        dir_ctr_list[-1] += 1
    return shortest_path


with open(input_filename) as f:
    grid = []
    # for line in temp:
    for line in f:
        if line.strip() != '':
            grid.append([char for char in line.strip()])
    result1 = explore_path(grid)
    print(result1)
