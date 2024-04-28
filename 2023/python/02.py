def prep_line(line):
  split_line = line.split(':')
  id = int(split_line[0].split(' ')[-1])
  subsets = split_line[1].split(';')
  return id, subsets


def get_max_occ(subsets):
  max_occ = {}
  for subset in subsets:
    for color_occ in subset.split(','):
      occ = int(color_occ.strip().split(' ')[0])
      color = color_occ.strip().split(' ')[1]
      if occ > max_occ.get(color, 0):
        max_occ[color] = occ
  return max_occ


def game_is_possible(max_occ, occ_dict):
  possible_dict = [
      occ >= max_occ.get(color, 0)
      for color, occ in occ_dict.items()
  ]
  return all(possible_dict)


def get_power_minimal_cube(max_occ, occ_dict):
  result = 1
  for color in occ_dict.keys():
    result *= max_occ.get(color, 0)
  return result


def sum_possible_ids(input_filename, occ_dict):
  with open(input_filename) as f:
    result = 0
    for line in f:
      id, subsets = prep_line(line)
      max_occ = get_max_occ(subsets)
      if game_is_possible(max_occ, occ_dict):
        result += id

  return result


def sum_power_minimal_cubes(input_filename, occ_dict):
  with open(input_filename) as f:
    result = 0
    for line in f:
      _, subsets = prep_line(line)
      max_occ = get_max_occ(subsets)
      result += get_power_minimal_cube(max_occ, occ_dict)
  return result


def main():
    occ_dict = {'red': 12, 'green': 13, 'blue': 14}
    # Part 1
    assert sum_possible_ids('2023/inputs/02_test.txt', occ_dict) == 8
    assert sum_possible_ids('2023/inputs/02.txt', occ_dict) == 2085
    # Part 2
    assert sum_power_minimal_cubes('2023/inputs/02_test.txt', occ_dict) == 2286
    assert sum_power_minimal_cubes('2023/inputs/02.txt', occ_dict) == 79315


if __name__ == '__main__':
    main()
