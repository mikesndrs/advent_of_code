"""https://adventofcode.com/2023/day/3"""


def sum_part_engines(input_filename):
    num_list, sym_list = get_num_and_sym_list(input_filename)
    result = 0
    for num, idcs in num_list:
        for pos in idcs:
            if touches(pos, sym_list):
                result += num
                break
    print(result)
    return result


def sum_gear_ratios(input_filename):
    num_list, sym_list = get_num_and_sym_list(input_filename)
    gear_dict = {}
    for num, idcs in num_list:
        for pos in idcs:
            touched = touches_gear(pos, sym_list)
            if touched:
                touched_idx_str = " ".join([str(x) for x in touched])
                gear_dict[touched_idx_str] = gear_dict.get(touched_idx_str, []) + [num]
                break
    result = 0
    for val in gear_dict.values():
        if len(val) == 2:
            result += val[0] * val[1]
    print(result)
    return result


def get_num_and_sym_list(input_filename):
    num_list = []
    sym_list = []
    with open(input_filename) as f:
        for x, line in enumerate(f):
            number_string = ""
            idcs = []
            for y, char in enumerate(line.strip()):
                if char.isdigit():
                    number_string += char
                    idcs.append([x, y])
                else:
                    if len(number_string):
                        num_list.append([int(number_string), idcs])
                        number_string = ""
                        idcs = []
                    if char != "." and char != " ":
                        sym_list.append([char, [x, y]])
            if len(number_string):
                num_list.append([int(number_string), idcs])
    return num_list, sym_list


def touches(pos, sym_list):
    for char, sym_pos in sym_list:
        if abs(sym_pos[0] - pos[0]) <= 1 and abs(sym_pos[1] - pos[1]) <= 1:
            return True
    return False


def touches_gear(pos, sym_list):
    for char, sym_pos in sym_list:
        if all(
            [
                char == "*",
                abs(sym_pos[0] - pos[0]) <= 1,
                abs(sym_pos[1] - pos[1]) <= 1,
            ]
        ):
            return sym_pos
    return False


def main():
    # Part 1
    assert sum_part_engines("2023/inputs/03_test.txt") == 4361
    assert sum_part_engines("2023/inputs/03.txt") == 521515
    # Part 2
    assert sum_gear_ratios("2023/inputs/03_test.txt") == 467835
    assert sum_gear_ratios("2023/inputs/03.txt") == 69527306


if __name__ == "__main__":
    main()
