"""https://adventofcode.com/2024/day/17"""

from typing import List, Tuple


class Computer:
    def __init__(self, input_filename: str) -> None:
        self.A: int
        self.B: int
        self.C: int
        self.program: List[int]
        self.output: List[int] = []
        with open(input_filename, "r") as f:
            for line in f:
                if line.startswith("Register A:"):
                    self.A = int(line.split(":")[1].strip())
                if line.startswith("Register B:"):
                    self.B = int(line.split(":")[1].strip())
                if line.startswith("Register C:"):
                    self.C = int(line.split(":")[1].strip())
                if line.startswith("Program:"):
                    val_list = line.split(":")[1].strip().split(",")
                    self.program = [int(x) for x in val_list]

    def run(self) -> None:
        pointer = 0
        while pointer < len(self.program):
            opcode, lop, cop = self.get_ops(pointer)
            if opcode == 0:
                self.A = int(self.A / 2**cop)
            elif opcode == 1:
                self.B = self.B ^ lop
            elif opcode == 2:
                self.B = cop % 8
            elif opcode == 3:
                if self.A > 0:
                    pointer = lop
                    continue
            elif opcode == 4:
                self.B = self.B ^ self.C
            elif opcode == 5:
                self.output.append(cop % 8)
            elif opcode == 6:
                self.B = int(self.A / 2**cop)
            elif opcode == 7:
                self.C = int(self.A / 2**cop)
            pointer += 2

    def get_ops(self, pointer: int) -> Tuple[int, int, int]:
        opcode = int(self.program[pointer])
        lop = int(self.program[pointer + 1])
        if lop in range(4):
            cop = lop
        elif lop == 4:
            cop = int(self.A)
        elif lop == 5:
            cop = int(self.B)
        elif lop == 6:
            cop = int(self.C)
        else:
            print("Made a whoopsie")
        return opcode, lop, cop

    def read_output(self) -> str:
        return ",".join(str(x) for x in self.output)

    def my_func(self, A: int) -> int:
        """
        2 4 B = A % 8 (take last 3 digits of A)
        1 5 B = B ^ 5 (xor 101)
        7 5 C = A / 2**B ( take last B digits of A)
        1 6 B = B ^ 6 (xor 110)
        4 3 B = B ^ C (xor)
        5 5 output.append(B % 8) (last 3 digits)
        0 3 A = A / 8 (remove last 3 digits)
        3 0 Return
        """
        B = A % 8
        B = B ^ 5
        C = int(A / 2**B)
        B = B ^ 6
        B = B ^ C
        return B % 8

    def int_to_bits(self, int: int) -> str:
        return bin(int)[2:]

    def bits_to_int(self, bits: str) -> int:
        return int(f"{bits:0<1}", 2)

    def ex2(self, j: int = 0, bits: str = "") -> Tuple[bool, str]:
        if j >= len(self.program):
            return True, bits
        val = self.program[-1 - j]
        if j == 0:
            power = 7
        else:
            power = 3
        for i in range(2**power):
            bit_str = self.int_to_bits(i)
            # new_bits = (bit_str + bits).rjust(3 * (j + 1), "0")
            new_bits = bits + bit_str.rjust(3, "0")
            A = self.bits_to_int(new_bits)
            res = self.my_func(A)
            if res == val:
                success, res_bits = self.ex2(j + 1, new_bits)
                if success:
                    return success, res_bits
        return False, ""


def main_func(input_filename: str, version: int) -> str:
    if version == 1:
        computer = Computer(input_filename)
        computer.run()
        result = computer.read_output()
    else:
        computer = Computer(input_filename)
        success, bits = computer.ex2()
        result = str(computer.bits_to_int(bits))
    print(result)
    return result


def main() -> None:
    pass
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/17_test.txt", 1) == "4,6,3,5,6,3,5,2,1,0"
    assert main_func("aoc/aoc_2024/inputs/17.txt", 1) == "2,1,3,0,5,2,3,7,1"
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/17.txt", 2) == "107416732707226"


if __name__ == "__main__":
    main()
