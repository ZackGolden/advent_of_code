def part_1(lines):
    disk_map = []
    for i in lines[0]:
        if i.isdigit():
            disk_map.append(int(i))

    left = 0
    right = len(disk_map) // 2 if len(disk_map) % 2 == 0 else len(disk_map) // 2 + 1
    block = 0
    l_index = 0
    r_index = len(disk_map) - 2 if len(disk_map) % 2 == 0 else len(disk_map) - 1
    hopper = []
    checksum = 0

    while l_index <= r_index:
        if l_index % 2 == 0:
            for i in range(disk_map[l_index]):
                checksum += left * block
                block += 1
            left += 1
        else:
            for i in range(disk_map[l_index]):
                if len(hopper) == 0:
                    hopper = [right] * disk_map[r_index]
                    r_index -= 2
                    right -= 1
                hopper.pop()
                checksum += right * block
                block += 1
        l_index += 1

    for i in hopper:
        checksum += right * block
        block += 1
    return checksum


def part_2(lines):
    disk_map = []
    for i in lines[0]:
        if i.isdigit():
            disk_map.append(int(i))

    len(disk_map) // 2 if len(disk_map) % 2 == 0 else len(disk_map) // 2 + 1
    block = 0
    len(disk_map) - 2 if len(disk_map) % 2 == 0 else len(disk_map) - 1

    free_space = []
    files = []
    for i, file_size in enumerate(disk_map):
        if i % 2 == 0:
            files.append((block, file_size))
        else:
            free_space.append((block, file_size))

        block += file_size

    checksum = 0
    i = len(files) - 1
    while i >= 0:
        file = files[i]
        not_moved = True
        for j, free in enumerate(free_space):
            if free[0] < file[0] and free[1] >= file[1]:
                for k in range(file[1]):
                    checksum += (k + free[0]) * i
                free_space[j] = (free[0] + file[1], free[1] - file[1])
                not_moved = False
                break
        if not_moved:
            for k in range(file[1]):
                checksum += (k + file[0]) * i
        else:
            if free_space[0][1] == 0:
                free_space.pop(0)
        i -= 1

    return checksum


def main():
    f = open("./day9/input", "r")
    lines = f.readlines()
    print("Day 9")
    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))


if __name__ == "__main__":
    main()
