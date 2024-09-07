"""https://adventofcode.com/2022/day/5"""


def main() -> None:
    input_filename = "aoc/aoc_2022/inputs/05.txt"
    with open(input_filename) as f:
        crate_lines = []
        for line in f:
            if line == "\n":
                break
            crate_lines.append(line.strip("\n")[1::4])
        crates = [[] for _ in range(len(crate_lines[-1]))]
        for crate_line in crate_lines[-2::-1]:
            for i, x in enumerate(crate_line):
                if x != " ":
                    crates[i].append(x)
        for line in f:
            move_n, crate_from_num, crate_to_num = (
                line.strip("\n")
                .replace("move ", "")
                .replace("from ", "")
                .replace("to ", "")
                .split(" ")
            )
            crate_from_idx = int(crate_from_num) - 1
            crate_to_idx = int(crate_to_num) - 1
            for _ in range(int(move_n)):
                crates[crate_to_idx].append(crates[crate_from_idx].pop(-1))
        result1 = "".join([crate[-1] for crate in crates])
        print(result1)

    with open(input_filename) as f:
        crate_lines = []
        for line in f:
            if line == "\n":
                break
            crate_lines.append(line.strip("\n")[1::4])
        crates = [[] for x in range(len(crate_lines[-1]))]
        for crate_line in crate_lines[-2::-1]:
            for i, x in enumerate(crate_line):
                if x != " ":
                    crates[i].append(x)
        for line in f:
            move_n, crate_from_num, crate_to_num = (
                line.strip("\n")
                .replace("move ", "")
                .replace("from ", "")
                .replace("to ", "")
                .split(" ")
            )
            crate_from_idx = int(crate_from_num) - 1
            crate_to_idx = int(crate_to_num) - 1
            for i in range(int(move_n), 0, -1):
                crates[crate_to_idx].append(crates[crate_from_idx][-i])
            crates[crate_from_idx] = crates[crate_from_idx][: -int(move_n)]
        result2 = "".join([crate[-1] for crate in crates])
        print(result2)


if __name__ == "__main__":
    main()
