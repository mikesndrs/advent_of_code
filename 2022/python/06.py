def beep(text, n):
    nbrs = n - 1
    skip_until = -1
    for i in range(n-1, len(text)):
        if i < skip_until:
            continue
        match_idx = None
        for j in range(nbrs):
            char = text[i - j]
            string = text[i - nbrs: i - j]
            if char in string:
                match_idx = string.index(char)
                skip_until = i + match_idx + 1
                break
        if match_idx is None:
            return i + 1
    return None


def main():
    input_filename = '2022/inputs/06.txt'
    with open(input_filename) as f:
        text = f.read()
        result1 = beep(text, 4)
        print(result1)
        result2 = beep(text, 14)
        print(result2)


if __name__ == '__main__':
    main()
