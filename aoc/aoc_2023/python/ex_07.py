"""https://adventofcode.com/2023/day/7"""


card_strength = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

card_strength_2 = dict(card_strength, **{"J": 1})


type_strength = {
    "five of a kind": 600,
    "four of a kind": 500,
    "full house": 400,
    "three of a kind": 300,
    "two pair": 200,
    "one pair": 100,
    "high card": 0,
}


def get_hand_dict(hand):
    nums = {}
    for char in hand:
        nums[char] = nums.get(char, 0) + 1
    sorted_hand = {
        x: nums[x]
        for x in sorted(
            nums, key=lambda x: 100 * nums[x] + card_strength[x], reverse=True
        )
    }
    return sorted_hand


def get_hand_type(hand_dict, version):
    if version == 2 and "J" in hand_dict.keys() and len(hand_dict) > 1:
        n_jokers = hand_dict.pop("J")
        key = list(hand_dict.keys())[0]
        hand_dict[key] = hand_dict.get(key, 0) + n_jokers
    if 5 in hand_dict.values():
        return "five of a kind"
    elif 4 in hand_dict.values():
        return "four of a kind"
    elif 3 in hand_dict.values() and 2 in hand_dict.values():
        return "full house"
    elif 3 in hand_dict.values():
        return "three of a kind"
    elif list(hand_dict.values()).count(2) == 2:
        return "two pair"
    elif list(hand_dict.values()).count(2) == 1:
        return "one pair"
    else:
        return "high card"


def compare_hand_strengths(i, hands, version):
    hand_dict = get_hand_dict(hands[i])
    my_type_strength = type_strength[get_hand_type(hand_dict, version)]
    if version == 1:
        my_card_strength = [card_strength[card] for card in hands[i]]
    else:
        my_card_strength = [card_strength_2[card] for card in hands[i]]
    res = (my_type_strength, *my_card_strength)
    return res


def sort_by_hand_strength(hands, bids, version):
    idcs = list(range(len(hands)))
    sorted_idcs = sorted(
        idcs, key=lambda i: compare_hand_strengths(i, hands, version), reverse=True
    )
    sorted_hands = [hands[i] for i in sorted_idcs]
    sorted_bids = [bids[i] for i in sorted_idcs]

    return sorted_hands, sorted_bids


def total_winnings(input_filename, version):
    with open(input_filename) as f:
        hands = []
        bids = []
        for line in f:
            inputs = line.strip().split(" ")
            hands.append(inputs[0])
            bids.append(int(inputs[1]))
        hands, bids = sort_by_hand_strength(hands, bids, version)
    result = 0
    for i in range(len(bids)):
        result += (len(bids) - i) * bids[i]
    print(result)
    return result


def main():
    # Part 1
    assert total_winnings("2023/inputs/07_test.txt", 1) == 6440
    assert total_winnings("2023/inputs/07.txt", 1) == 251058093
    # Part 2
    assert total_winnings("2023/inputs/07_test.txt", 2) == 5905
    assert total_winnings("2023/inputs/07.txt", 2) == 249781879


if __name__ == "__main__":
    main()
