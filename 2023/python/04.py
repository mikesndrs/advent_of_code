def sum_of_points(input_filename, version):
    result = 0
    card_counter = {}
    with open(input_filename) as f:
        for line in f:
            card_num, winning_nums, my_nums = get_inputs(line)
            intersection = winning_nums & my_nums
            intersection.discard("")
            if version == 1:
                if intersection:
                    result += 2 ** (len(intersection) - 1)
            elif version == 2:
                card_counter[card_num] = card_counter.get(card_num, 0) + 1
                for i in range(len(intersection)):
                    new_id = card_num + i + 1
                    card_counter[new_id] = (
                        card_counter.get(new_id, 0) + card_counter[card_num]
                    )
                result += card_counter[card_num]
            else:
                print("Something weird happened")

    print(result)
    return int(result)


def get_inputs(line):
    inputs = line.strip("\n").split(":")
    card_num = int(inputs[0].split(" ")[-1].strip())
    nums = inputs[1].split("|")
    winning_nums = set(nums[0].strip().split(" "))
    my_nums = set(nums[1].strip().split(" "))
    return card_num, winning_nums, my_nums


def main():
    # Part 1
    assert sum_of_points("2023/inputs/04_test.txt", 1) == 13
    assert sum_of_points("2023/inputs/04.txt", 1) == 26914
    # Part 2
    assert sum_of_points("2023/inputs/04_test.txt", 2) == 30
    assert sum_of_points("2023/inputs/04.txt", 2) == 13080971


if __name__ == "__main__":
    main()
