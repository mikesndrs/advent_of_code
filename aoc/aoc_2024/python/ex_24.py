"""https://adventofcode.com/2024/day/24"""

from typing import Any, Dict, Tuple

INPUT_GATES = Dict[str, Any]
OUTPUT_GATES = Dict[str, Tuple[str, str, str]]


def handle_input(input_filename: str) -> Tuple[INPUT_GATES, OUTPUT_GATES]:
    input_gates: INPUT_GATES = {}
    output_gates: OUTPUT_GATES = {}
    with open(input_filename, "r") as f:
        for line in f:
            if len(line.strip()) == 0:
                continue
            elif ":" in line:
                gate, val = line.strip().split(":")
                input_gates[gate.strip()] = int(val.strip())
            elif "->" in line:
                inputs, gate = line.strip().split("->")
                input1, op, input2 = inputs.strip().split(" ")
                output_gates[gate.strip()] = (
                    input1.strip(),
                    op.strip(),
                    input2.strip(),
                )
    for key in output_gates.keys():
        input_gates[key] = input_gates.get(key, None)
    return input_gates, output_gates


def do_func(input1: int, op: str, input2: int) -> int:
    if op == "AND":
        result = input1 and input2
    elif op == "OR":
        result = input1 or input2
    elif op == "XOR":
        result = input1 ^ input2
    else:
        print("Made a whoopsie")
    return result


def get_score(input_gates: INPUT_GATES) -> int:
    z_keys = [key for key in input_gates if key.startswith("z")]
    z_keys = sorted(z_keys)
    bit_string = ""
    for key in z_keys:
        bit_string = str(input_gates[key]) + bit_string
    score = int(bit_string, 2)
    return score


def main_func(input_filename: str, version: int) -> Any:
    result: Any
    input_gates, output_gates = handle_input(input_filename)
    if version == 1:
        empty_output_gates = [
            key for key in output_gates.keys() if input_gates[key] is None
        ]
        while len(empty_output_gates) > 0:
            new_gates = []
            for key in empty_output_gates:
                input1, op, input2 = output_gates[key]
                if input_gates[input1] is None or input_gates[input2] is None:
                    new_gates.append(key)
                    continue
                input_gates[key] = do_func(input_gates[input1], op, input_gates[input2])
            empty_output_gates = new_gates
        result = get_score(input_gates)
    else:
        # lots of assumptions
        # rely on the the fact that the system tries to be a binary number adder
        # in all cases we should effectively get
        # z_0 = x_0 ^ y_0
        # z_1 = (x_1 ^ y_1) ^ (x_0 & y_0)
        # z_2 = (x_2 ^ y_2) ^ ((x_1 ^ y_1) & (x_0 & y_0))
        # ...
        # z_n = (x_n ^ y_n) ^ c_n with c_n = (x_n-1 & y_n-1) | ((x_n-1 ^ y_n-1) & c_n-1)
        # therefore:
        # any z gate except the last obtained through XOR
        # any XOR should involve an x, y or z gate
        # any result of an AND operation should be followed by an OR operation
        # the result of an XOR operation cannot be lost in an OR operation
        # assume that there are no abstractions hidden behind unneccesary layers
        wrong_gates = set()
        z_max = max([int(key[1:]) for key in output_gates if key.startswith("z")])
        for res, val in output_gates.items():
            op1, op, op2 = val
            if res[0] == "z" and int(res[1:]) != z_max and op != "XOR":
                wrong_gates.add(res)
            if all(
                (
                    op == "XOR",
                    op1[0] not in ["x", "y", "z"],
                    op2[0] not in ["x", "y", "z"],
                    res[0] not in ["x", "y", "z"],
                )
            ):
                wrong_gates.add(res)
            if op == "AND" and "x00" not in [op1, op2]:
                for subres, subval in output_gates.items():
                    subop1, subop, subop2 = subval
                    if res in [subop1, subop2] and subop != "OR":
                        wrong_gates.add(res)
            if op == "XOR":
                for subres, subval in output_gates.items():
                    subop1, subop, subop2 = subval
                    if res in [subop1, subop2] and subop == "OR":
                        wrong_gates.add(res)
        result = ",".join(sorted(list(wrong_gates)))
    print(result)
    return result


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/24_test_small.txt", 1) == 4
    assert main_func("aoc/aoc_2024/inputs/24_test.txt", 1) == 2024
    assert main_func("aoc/aoc_2024/inputs/24.txt", 1) == 60614602965288
    # # Part 2
    assert (
        main_func("aoc/aoc_2024/inputs/24.txt", 2) == "cgr,hpc,hwk,qmd,tnt,z06,z31,z37"
    )


if __name__ == "__main__":
    main()
