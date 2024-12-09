"""https://adventofcode.com/2024/day/09"""


def handle_input(input_filename: str):
    """Get list of memory block"""
    with open(input_filename, "r") as f:
        a = f.readline().strip()
    ctr = 0
    mem = []
    for i, char in enumerate(a):
        if i % 2 == 0:
            mem += [ctr] * int(char)
            ctr += 1
        else:
            mem += ["."] * int(char)
    return mem


def badly_optimized_memory(mem):
    """Optimize memory per block"""
    for i, char in enumerate(mem):
        if char == ".":
            while mem[-1] == ".":
                mem.pop()
            if i > len(mem) - 1:
                break
            mem[i] = mem.pop()
    return mem


def semi_optimized_memory(input_filename):
    """Optimize memory per file"""
    with open(input_filename, "r") as f:
        a = f.readline().strip()
        a += "0"
    files = []
    for i in range(0, len(a), 2):
        idx = int(i / 2)
        files.append(
            {"files": [idx] * int(a[i]), "new_files": [], "space": int(a[i + 1])}
        )
    for i in range(len(files) - 1, 0, -1):
        for j in range(i):
            if len(files[i]["files"]) <= files[j]["space"]:
                files[j]["new_files"] += files[i]["files"]
                files[i]["new_files"] = ["."] * len(files[i]["files"]) + files[i][
                    "new_files"
                ]
                files[j]["space"] -= len(files[i]["files"])
                files[i]["files"] = []
    mem = []
    for file in files:
        mem += file["files"]
        mem += file["new_files"]
        mem += file["space"] * ["."]
    return mem


def main_func(input_filename: str, version: int) -> int:
    """Main function"""
    if version == 1:
        mem = handle_input(input_filename)
        mem = badly_optimized_memory(mem)
    else:
        mem = semi_optimized_memory(input_filename)
    result = 0
    for i, char in enumerate(mem):
        if char != ".":
            result += i * int(char)
    print(result)
    return result


def main() -> None:
    """Top level function"""
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/09_test.txt", 1) == 1928
    assert main_func("aoc/aoc_2024/inputs/09.txt", 1) == 6382875730645
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/09_test.txt", 2) == 2858
    assert main_func("aoc/aoc_2024/inputs/09.txt", 2) == 6420913943576


if __name__ == "__main__":
    main()
