def mapping_chain(input_filename, version):
    seeds, maps = handle_inputs(input_filename, version)
    values = seeds.copy()
    for map in maps:
        values = apply_map(map, values)
    result = min([value[0] for value in values])
    print(result)
    return result


def apply_map(map, values):
    new_values = values.copy()
    result_values = []
    for dest, source, length in map:
        old_values = new_values.copy()
        new_values = []
        end = source + length - 1
        diff = dest - source
        for min_val, max_val in old_values:
            if max_val < source:
                new_values.append([min_val, max_val])
            elif min_val > end:
                new_values.append([min_val, max_val])
            elif min_val >= source and max_val <= end:
                result_values.append([min_val + diff, max_val + diff])
            elif min_val < source and source <= max_val <= end:
                new_values.append([min_val, source - 1])
                result_values.append([dest, max_val + diff])
            elif source <= min_val <= end and max_val > end:
                result_values.append([min_val + diff, end + diff])
                new_values.append([end + 1, max_val])
            elif min_val < source and max_val > end:
                new_values.append([min_val, source - 1])
                result_values.append([dest, end + diff])
                new_values.append([end + 1, max_val])

    result_values += new_values
    return result_values


def handle_inputs(input_filename, version):
    with open(input_filename) as f:
        sections = f.read().split("\n\n")
        seed_section = sections[0].split(":")[-1].strip().split(" ")
        seeds_vals = [int(x) for x in seed_section]
        if version == 1:
            seeds = [[x, x] for x in seeds_vals]
        if version == 2:
            seeds = [
                [seeds_vals[i], seeds_vals[i] + seeds_vals[i + 1] - 1]
                for i in range(0, len(seeds_vals), 2)
            ]
        maps = []
        for map in sections[1:]:
            map_lines = []
            for map_line in map.split(":\n")[-1].strip().split("\n"):
                map_lines.append([int(x) for x in map_line.split(" ")])
            maps.append(map_lines)
        return seeds, maps


def main():
    # Part 1
    assert mapping_chain("2023/inputs/05_test.txt", 1) == 35
    assert mapping_chain("2023/inputs/05.txt", 1) == 214922730
    # Part 2
    assert mapping_chain("2023/inputs/05_test.txt", 2) == 46
    assert mapping_chain("2023/inputs/05.txt", 2) == 148041808


if __name__ == "__main__":
    main()
