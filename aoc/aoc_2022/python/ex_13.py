"""https://adventofcode.com/2022/day/13"""


def compare(a: int, b: int) -> bool:
    if a < b:
        return True
    elif a == b:
        return "tie"
    elif a > b:
        return False


def is_sorted(list1: list[int], list2: list[int]) -> bool:
    if set([type(list1), type(list2)]) == {list}:
        min_length = min(len(list1), len(list2))
        for i in range(min_length):
            x = is_sorted(list1[i], list2[i])
            if isinstance(x, bool):
                return x
        return compare(len(list1), len(list2))
    elif set([type(list1), type(list2)]) == {int, list}:
        lists = []
        for lst in [list1, list2]:
            if isinstance(lst, int):
                lists.append([lst])
            elif isinstance(lst, list):
                lists.append(lst)
            else:
                raise ValueError("Item is neither int nor list")

        return is_sorted(*lists)
    elif set([type(list1), type(list2)]) == {int}:
        return compare(list1, list2)

    raise ValueError("Should never reach this point")


def main() -> int:
    input_filename = "aoc/aoc_2022/inputs/13.txt"
    with open(input_filename) as f:
        ctr = 0
        idx = 0
        lines = []
        for line in f:
            sl = line.strip()
            if sl == "":
                idx += 1
                if is_sorted(*lines):
                    ctr += idx
                lines = []
            else:
                lines.append(eval(sl))
    result1 = ctr
    print(result1)

    with open(input_filename) as f:
        key_packets = [[[2]], [[6]]]
        packets = []
        for line in f:
            sl = line.strip()
            if sl == "":
                pass
            else:
                packets.append(eval(line.strip()))
        for key_packet in key_packets:
            packets.append(key_packet)
        sorted_packets = [packets[0]]
        for packet in packets[1:]:
            for i in range(len(sorted_packets)):
                if is_sorted(packet, sorted_packets[i]):
                    sorted_packets.insert(i, packet)
                    break
        result2 = 1
        for key_packet in key_packets:
            result2 *= sorted_packets.index(key_packet) + 1
    print(result2)


if __name__ == "__main__":
    main()
