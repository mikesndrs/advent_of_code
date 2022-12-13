def main():
    input_filename = "inputs/07.txt"
    with open(input_filename) as f:
        max_size = 100000
        total_size_dic = {}
        current_dir_list = ["root"]
        seen_list = []

        for line in f:
            split_line = line.strip().split(" ")
            if split_line[0] == "$":
                if split_line[1] == "cd":
                    if split_line[2] == "/":
                        current_dir_list = ["root"]
                    elif split_line[2] == "..":
                        current_dir_list.pop()
                    else:
                        current_dir_list.append(split_line[2])
                elif split_line[1] == "ls":
                    continue
            elif split_line[0] == "dir":
                continue
            elif split_line[0].isnumeric():
                full_path = "/".join(current_dir_list) + "/" + split_line[1]
                if full_path not in seen_list:
                    seen_list.append(full_path)
                    for i in range(len(current_dir_list)):
                        dir_path = "/".join(current_dir_list[: i + 1])
                        if dir_path in total_size_dic:
                            total_size_dic[dir_path] += int(split_line[0])
                        else:
                            total_size_dic[dir_path] = int(split_line[0])

        result1 = 0
        for dir in total_size_dic:
            if total_size_dic[dir] <= max_size:
                result1 += total_size_dic[dir]
        print(result1)
        total_disk_space = 70000000
        needed_space = 30000000
        root_size = total_size_dic['root']
        space_to_delete = needed_space - (total_disk_space - root_size)
        eligible_dirs = [
            x for x in list(total_size_dic.values()) if x >= space_to_delete
        ]
        result2 = min(eligible_dirs)
        print(result2)


if __name__ == "__main__":
    main()
