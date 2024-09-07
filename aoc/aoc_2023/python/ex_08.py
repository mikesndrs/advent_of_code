"""https://adventofcode.com/2023/day/8"""

from typing import Dict, Tuple

# TODO: FINISH actual exercise since the answer is not to the actual question
LR_dict = {
    "L": 0,
    "R": 1,
}


def pattern_divide_func(pattern: str) -> str:
    for i in reversed(range(2, len(pattern) // 2)):
        if len(pattern) % i == 0:
            pat1 = pattern[: i + 1]
            pats = [pattern[j * i : (j + 1) * i + 1] for j in range(len(pattern) // i)]
            if all([pat == pat1 for pat in pats]):
                pattern = pat1
    return pattern


def handle_input(input_filename: str) -> Tuple[str, Dict]:
    with open(input_filename) as f:
        lines = f.readlines()
        pattern = lines[0].strip()
        if len(pattern) > 2:
            pattern = pattern_divide_func(pattern)
        network = {}
        for line in lines[2:]:
            split_line = line.split(" = ")
            key = split_line[0].strip()
            val = [x.strip() for x in split_line[1].strip("()\n").split(",")]
            network[key] = val
    return pattern, network


def follow_network(pattern: str, network: Dict) -> int:
    pattern_len = len(pattern)
    val = "AAA"
    res = 0
    while val != "ZZZ":
        val = network[val][LR_dict[pattern[res % pattern_len]]]
        res += 1
    return res


# {start_val, [[z_vals] [start_pattern_idx, pattern_rep_freq]]}
def get_occ_list(pattern: str, network: Dict) -> Dict:
    vals = list(filter(lambda x: x[-1] == "A", list(network.keys())))
    pattern_len = len(pattern)
    occ_list = {}
    for val in vals:
        val_i = val
        ctr = 0
        iter = 0
        seen_vals: Dict[int, Dict[int, int]] = {}
        while True:
            val_i = network[val_i][LR_dict[pattern[ctr]]]
            ctr += 1
            if ctr == pattern_len:
                iter += 1
                ctr = 0
            if val_i[-1] == "Z":
                if val_i not in seen_vals:
                    seen_vals[val_i] = {}
                if ctr in seen_vals[val_i]:
                    z_vals = {key: seen_vals[val_i][key] for key in seen_vals[val_i]}
                    start_pattern = (ctr, seen_vals[val_i][ctr])
                    freq = iter - seen_vals[val_i][ctr]
                    occ_list[val] = [z_vals, start_pattern, freq]
                    break
                else:
                    seen_vals[val_i][ctr] = iter
    return occ_list


def follow_network_ghost(pattern: str, network: Dict) -> int:
    occ_list = get_occ_list(pattern, network)
    print(len(pattern))
    print(occ_list)

    beep = {}
    occ_vals = list(occ_list.values())
    for i in range(len(pattern)):
        if all([i in occ_val[0].keys() for occ_val in occ_vals]):
            beep[i] = [(occ_val[0][i], occ_val[2]) for occ_val in occ_vals]
    res = int(1e30)
    for key, val in beep.items():
        for x in val:
            print([((x[0] - y[0]) % y[1]) == 0 for y in val])
            if all([((x[0] - y[0]) % y[1]) == 0 for y in val]):
                res = min(res, len(pattern) * x[1] + key)

    return res


def steps_required(input_filename: str, version: int) -> int:
    pattern, network = handle_input(input_filename)
    if version == 1:
        res = follow_network(pattern, network)
    elif version == 2:
        res = follow_network_ghost(pattern, network)
    else:
        print("woops")
    print(res)
    return res


def main() -> None:
    # Part 1
    assert steps_required("aoc/aoc_2023/inputs/08_test.txt", 1) == 6
    assert steps_required("aoc/aoc_2023/inputs/08.txt", 1) == 23147
    # Part 2
    assert steps_required("aoc/aoc_2023/inputs/08_test_2.txt", 2) == 6
    assert steps_required("aoc/aoc_2023/inputs/08.txt", 2) == 22289513667691


if __name__ == "__main__":
    main()
