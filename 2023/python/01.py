digit_strings = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def char_in_line(line, reversed=False):
  line = line[::-1]
  for char in line:
    if char.isdigit():
      return char


def string_in_line(line, reversed=False):
  if reversed:
    beep = -1
  else:
    beep = 1
  for idx in range(len(line))[::beep]:
    for digit in digit_strings.keys():
      if idx + len(digit) < len(line) and line[idx: idx + len(digit)] == digit:
        return str(digit_strings[digit])


def get_sum_first_and_list(input_filename, func):
    with open(input_filename) as f:
      coord_list = []
      for line in f:
        first = func(line)
        last = func(line, reversed=True)
        coord_list.append(int(first + last))
      result = sum(coord_list)
      print(result)


def main():
    input_filename = '2023/inputs/01.txt'

    get_sum_first_and_list(input_filename, char_in_line)
    get_sum_first_and_list(input_filename, string_in_line)


if __name__ == '__main__':
    main()
