def noop(x, cycle, add):
    cycle += 1
    if cycle >= 1:
        cycle = 0
    return x, cycle


def addx(x, cycle, add):
    cycle += 1
    if cycle >= 2:
        cycle = 0
        x += add
    return x, cycle


func_dict = {
    "noop": noop,
    "addx": addx,
}


def main():
    input_filename = "2022/inputs/10.txt"
    with open(input_filename) as f:
        i = 0
        x = 1
        cycle = 0
        add = 0
        result1 = 0
        crt_drawing = ""
        width = 40
        for line in f:
            split_line = line.strip().split(" ")
            if len(split_line) > 1:
                add = int(split_line[1])
            for iter in range(100):
                i += 1
                if i % width == 20:
                    result1 += x * i
                if any(
                    [
                        i % width - 1 == x,
                        i % width - 1 == x - 1 and i % width != 0,
                        i % width - 1 == x + 1 and i % width != 1,
                    ]
                ):
                    crt_drawing += "#"
                else:
                    crt_drawing += " "
                if i % width == 0:
                    crt_drawing += "\n"
                x, cycle = func_dict[split_line[0]](x, cycle, add)
                if cycle == 0:
                    break
        print(result1)
        print(crt_drawing)


if __name__ == "__main__":
    main()
