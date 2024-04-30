import numpy as np


def main():
    input_filename = "2022/inputs/03.txt"
    with open(input_filename) as f:
        text = f.read()
        lists = text.split("\n")
        input = [x for x in lists[:-1]]

    item_priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    item_priorities.index("D") + 1

    priority_list = []
    for rucksack in input:
        compartment1 = rucksack[: int(len(rucksack) / 2)]
        compartment2 = rucksack[int(len(rucksack) / 2) :]
        for item in compartment1:
            if item in compartment2:
                priority_list.append(item_priorities.index(item) + 1)
                break

    result1 = np.sum(np.array(priority_list))
    print(result1)

    # 2022_12_03 2nd puzzle
    group_size = 3
    input = [
        input[group_size * i : group_size * (i + 1)]
        for i in range(int(len(input) / group_size))
    ]

    priority_list = []
    for group in input:
        for item in group[0]:
            if all([item in group[i] for i in range(1, group_size)]):
                priority_list.append(item_priorities.index(item) + 1)
                break

    result2 = np.sum(np.array(priority_list))
    print(result2)


if __name__ == "__main__":
    main()
