op_dict = {
    "+": (lambda val1, val2: val1 + val2),
    "*": (lambda val1, val2: val1 * val2),
    # '-': (lambda val1, val2: val1 - val2),
    # '/': (lambda val1, val2: val1 / val2),
}


class Monkey:
    def __init__(self, lines, inspect_worry_div):
        self.name = lines[0].strip(":").split(" ")[-1]
        self.items = []
        for item in lines[1].split(" ")[2:]:
            self.items.append(int(item.strip(",")))
        self.op = op_dict[lines[2].split(" ")[-2]]
        self.vals = [lines[2].split(" ")[-3], lines[2].split(" ")[-1]]
        self.test_val = int(lines[3].split(" ")[-1])
        self.true_target = int(lines[4].split(" ")[-1])
        self.false_target = int(lines[5].split(" ")[-1])
        self.inspect_worry_div = inspect_worry_div
        self.test_val_prod = 1

    def throw(self, monkeys, item):
        item = self.inspect(item)
        if self.inspect_worry_div is not None:
            item = self.bored(item)
        else:
            item = self.mem_optim(item)
        target = self.test(item)
        monkeys[target].items.append(item)

    def inspect(self, item):
        vals = []
        for i, val in enumerate(self.vals):
            if val.isnumeric():
                vals.append(int(val))
            elif val == "old":
                vals.append(item)
            else:
                raise ValueError("Unexpected argument")
        item = self.op(*vals)
        return item

    def bored(self, item):
        item = int(item / self.inspect_worry_div)
        return item

    def test(self, item):
        if item % self.test_val == 0:
            return self.true_target
        else:
            return self.false_target

    def mem_optim(self, item):
        return item % self.test_val_prod


def monkey_shenanigans(input_filename, n_rounds, inspect_worry_div):
    monkeys = []
    with open(input_filename) as f:
        lines = []
        for line in f:
            if line.strip() == "":
                monkeys.append(Monkey(lines, inspect_worry_div))
                lines = []
            else:
                lines.append(line.strip())
        test_val_prod = 1
        for monkey in monkeys:
            test_val_prod *= monkey.test_val
        for monkey in monkeys:
            monkey.test_val_prod = test_val_prod

        inspect_count_list = [0] * len(monkeys)
        for i in range(n_rounds):
            for j, monkey in enumerate(monkeys):
                n = len(monkey.items)
                inspect_count_list[j] += n
                for _ in range(n):
                    item = monkey.items.pop(0)
                    monkey.throw(monkeys, item)

    inspect_count_list.sort(reverse=True)
    result = inspect_count_list[0] * inspect_count_list[1]
    return result


def main():
    input_filename = "2022/inputs/11.txt"
    n_rounds = 20
    inspect_worry_div = 3
    result1 = monkey_shenanigans(input_filename, n_rounds, inspect_worry_div)
    print(result1)
    n_rounds = 10000
    inspect_worry_div = None
    result2 = monkey_shenanigans(input_filename, n_rounds, inspect_worry_div)
    print(result2)


if __name__ == "__main__":
    main()
