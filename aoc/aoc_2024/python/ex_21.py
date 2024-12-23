"""https://adventofcode.com/2024/day/21"""

from typing import Dict, List, Tuple

INT_INF = int(1e16)


class RecursiveRobot:
    # keypad grid for numbers
    num_keypad = {
        "A": (2, 3),
        "0": (1, 3),
        "1": (0, 2),
        "2": (1, 2),
        "3": (2, 2),
        "4": (0, 1),
        "5": (1, 1),
        "6": (2, 1),
        "7": (0, 0),
        "8": (1, 0),
        "9": (2, 0),
        "x": (0, 3),
    }

    # keypad grid for directions
    dir_keypad = {
        "A": (2, 0),
        "^": (1, 0),
        "<": (0, 1),
        "v": (1, 1),
        ">": (2, 1),
        "x": (0, 0),
    }

    # move direction per char
    move_dict = {
        "<": (-1, 0),
        "^": (0, -1),
        ">": (1, 0),
        "v": (0, 1),
        "A": (0, 0),
    }

    # char per move direction
    dir_dict = {val: key for key, val in move_dict.items()}

    def __init__(self, input_filename: str, version: int) -> None:
        with open(input_filename, "r") as f:
            self.codes = []
            for line in f:
                if len(line.strip()) > 0:
                    self.codes.append(line.strip())
        if version == 1:
            self.depth = 3
        else:
            self.depth = 26
        self.cost_dict: Dict[int, Dict[str, int]] = {}
        self.get_cost_dict()

    def get_cost_dict(self) -> None:
        """Iteratively build cost dictionary per A-to-A subsequence in code per level
        starting at end"""
        for i in range(self.depth, 0, -1):
            self.cost_dict[i] = self.cost_dict.get(i, {})
            if i == 1:
                subseqs = self.all_sub_sequences(self.num_keypad)
            else:
                subseqs = self.all_sub_sequences(self.dir_keypad)
            for subseq in subseqs:
                if i == self.depth:
                    self.cost_dict[i][subseq] = len(subseq)
                else:
                    codes = self.type_string(subseq, self.dir_keypad)
                    self.cost_dict[i][subseq] = min(
                        self.calc_code_cost(code, i) for code in codes
                    )

    def calc_code_cost(self, code: str, i: int) -> int:
        """Calc cost of typing code at level i based on cost of substrings at
        level i + 1"""
        code_seqs = [seq + "A" for seq in code.split("A")[:-1]]
        cost = sum(self.cost_dict[i + 1][seq] for seq in code_seqs)
        return cost

    def all_sub_sequences(self, keypad: Dict) -> List:
        """Find all sub_sequences resulting from all possible paths between any 2
        points on a given keypad"""
        sub_seqs = []
        for pos1 in keypad.keys():
            if pos1 == "x":
                continue
            for pos2 in keypad.keys():
                if pos2 == "x":
                    continue
                sub_seqs += self.type_string(pos1, keypad, start=pos2)
        return list(set(sub_seqs))

    def type_string(self, string: str, keypad: Dict, start: str = "A") -> List[str]:
        """Return list of codes that result in given string on lower level"""
        inputs = [""]
        pos = keypad[start]
        for char in string:
            dirs = ""
            dx = keypad[char][0] - pos[0]
            dy = keypad[char][1] - pos[1]
            if dx > 0:
                dirs += ">" * abs(dx)
            elif dx < 0:
                dirs += "<" * abs(dx)
            if dy > 0:
                dirs += "v" * abs(dy)
            elif dy < 0:
                dirs += "^" * abs(dy)
            seqs = self.get_sequences(pos, dirs, keypad)
            new_inputs = []
            for input in inputs:
                for seq in seqs:
                    new_inputs.append(input + seq + "A")
            inputs = new_inputs
            pos = keypad[char]
        return inputs

    def get_sequences(self, pos: Tuple[int, int], dirs: str, keypad: Dict) -> List[str]:
        """Return list of all valid sequences that result in a given code
        (only directions in this case)"""
        unique_chars = "".join(set(char for char in dirs))
        char_seqs = self.permutations(unique_chars)
        seqs = []
        for char_seq in char_seqs:
            seq = "".join(dirs.count(char) * char for char in char_seq)
            if self.validate_sequence(seq, pos, keypad):
                seqs.append(seq)
        if len(seqs) == 0:
            seqs = [""]
        return seqs

    def permutations(self, seq: str) -> List[str]:
        """Return valid permutations of direction character order"""
        if len(seq) == 1:
            return [seq]
        perms = []
        for i in range(len(seq)):
            current = seq[i]
            remaining = seq[:i] + seq[i + 1 :]
            for perm in self.permutations(remaining):
                perms.append(current + perm)
        return perms

    def validate_sequence(self, seq: str, pos: Tuple[int, int], keypad: Dict) -> bool:
        """Check whether sequence is valid"""
        for char in seq:
            pos = (pos[0] + self.move_dict[char][0], pos[1] + self.move_dict[char][1])
            if not (pos in keypad.values() and pos != keypad["x"]):
                return False
        return True

    def calc_complexity(self, code: str) -> int:
        """Calculate complexity of base level code"""
        num_part = int("".join(char for char in code if char.isnumeric()))
        codes = self.type_string(code, self.num_keypad)
        code_cost = min(self.calc_code_cost(code, 0) for code in codes)
        complexity = num_part * code_cost
        return complexity


def main_func(input_filename: str, version: int) -> int:
    """Main function"""
    rec_robot = RecursiveRobot(input_filename, version)
    result = 0
    for code in rec_robot.codes:
        result += rec_robot.calc_complexity(code)
    print(result)
    return result


def main() -> None:
    """Top level func"""
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/21_test.txt", 1) == 126384
    assert main_func("aoc/aoc_2024/inputs/21.txt", 1) == 219366
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/21_test.txt", 2) == 154115708116294
    assert main_func("aoc/aoc_2024/inputs/21.txt", 2) == 271631192020464


if __name__ == "__main__":
    main()

# loop solve per stage of i
# cache each subsequence from A to A per iteration level
# keep cache dictionary of A_to_A subsequence with result
# keep dictionary per level of A_to_A subsequence counts
# length is independent of A_to_A subsequence order -> dict with count per level
# create dictionaries per level backwards
