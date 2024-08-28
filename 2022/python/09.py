"""https://adventofcode.com/2022/day/9"""


dir_dict = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}


def calc_trail(input_filename, n_knots, dir_dict):
    pos = [[0, 0] for x in range(n_knots)]
    trail = set()
    trail.add(tuple(pos[-1]))

    with open(input_filename) as f:
        for line in f:
            split_line = line.strip().split(" ")
            dir = split_line[0]
            mv_H = dir_dict[dir]
            n = int(split_line[1])
            for _ in range(n):
                for j in range(2):
                    pos[0][j] += mv_H[j]
                for j in range(1, n_knots):
                    for k in range(2):
                        dif = pos[j - 1][k] - pos[j][k]
                        if abs(dif) >= 2:
                            pos[j][k] += (dif) / abs(dif)
                            for i in range(2):
                                dif_l = pos[j - 1][i] - pos[j][i]
                                if i != k and abs(dif_l) > 0:
                                    pos[j][i] += dif_l / abs(dif_l)
                trail.add(tuple((pos[-1])))
    return trail


def main():
    input_filename = "2022/inputs/09.txt"
    n_knots = 2
    result1 = len(calc_trail(input_filename, n_knots, dir_dict))
    print(result1)
    n_knots = 10
    result1 = len(calc_trail(input_filename, n_knots, dir_dict))
    print(result1)


if __name__ == "__main__":
    main()
