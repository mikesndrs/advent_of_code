"""https://adventofcode.com/2024/day/13"""

from typing import List, Tuple


class Equation:
    def __init__(self, xa: int, ya: int, xb: int, yb: int, x: int, y: int) -> None:
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.x = x
        self.y = y
        self.a_cost = 3
        self.b_cost = 1

    def solve(self) -> Tuple[int, int]:
        # na * xa  + nb * xb = x
        # na * ya  + nb * yb = y
        nb = round(
            (self.x - self.xa * self.y / self.ya)
            / (self.xb - self.xa * self.yb / self.ya)
        )
        na = round((self.y - nb * self.yb) / self.ya)
        return (na, nb)

    def cost(self) -> int:
        na, nb = self.solve()
        if all(
            [
                na >= 0,
                nb >= 0,
                self.xa * na + self.xb * nb == self.x,
                self.ya * na + self.yb * nb == self.y,
            ]
        ):
            cost = self.a_cost * na + self.b_cost * nb
        else:
            cost = 0
        return cost


def handle_input(input_filename: str, version: int) -> List[Equation]:
    with open(input_filename, "r") as f:
        equations = []
        equation = Equation(0, 0, 0, 0, 0, 0)
        for line in f:
            if line.startswith("Button A: "):
                equation.xa = int(line.split(": ")[1].split(", ")[0].split("+")[1])
                equation.ya = int(line.split(": ")[1].split(", ")[1].split("+")[1])
            elif line.startswith("Button B: "):
                equation.xb = int(line.split(": ")[1].split(", ")[0].split("+")[1])
                equation.yb = int(line.split(": ")[1].split(", ")[1].split("+")[1])
            elif line.startswith("Prize: "):
                equation.x = int(line.split(": ")[1].split(", ")[0].split("=")[1])
                equation.y = int(line.split(": ")[1].split(", ")[1].split("=")[1])
                if version == 2:
                    equation.x += int(1e13)
                    equation.y += int(1e13)
                equations.append(equation)
                equation = Equation(0, 0, 0, 0, 0, 0)
    return equations


def main_func(input_filename: str, version: int) -> int:
    equations = handle_input(input_filename, version)
    result = 0
    for equation in equations:
        result += equation.cost()
    print(result)
    return result


def main() -> None:
    # Part 1
    assert main_func("aoc/aoc_2024/inputs/13_test.txt", 1) == 480
    assert main_func("aoc/aoc_2024/inputs/13.txt", 1) == 29388
    # # Part 2
    assert main_func("aoc/aoc_2024/inputs/13_test.txt", 2) == 875318608908
    assert main_func("aoc/aoc_2024/inputs/13.txt", 2) == 99548032866004


if __name__ == "__main__":
    main()
