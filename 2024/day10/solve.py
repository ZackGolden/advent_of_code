def get_map(lines):
    map = []
    for line in lines:
        if len(line) == 0:
            break
        temp = []
        for h in line:
            if h.isdigit():
                temp.append(int(h))
        map.append(temp)
    return map


def walk_path(x, y, c_h, map):
    if c_h == 9:
        return {(x, y)}
    peaks = set()
    if y - 1 >= 0 and (c_h + 1) == map[y - 1][x]:
        peaks = peaks.union(walk_path(x, y - 1, c_h + 1, map))
    if y + 1 < len(map) and (c_h + 1) == map[y + 1][x]:
        peaks = peaks.union(walk_path(x, y + 1, c_h + 1, map))
    if x - 1 >= 0 and (c_h + 1) == map[y][x - 1]:
        peaks = peaks.union(walk_path(x - 1, y, c_h + 1, map))
    if x + 1 < len(map[0]) and (c_h + 1) == map[y][x + 1]:
        peaks = peaks.union(walk_path(x + 1, y, c_h + 1, map))

    return peaks


def part_1(lines):
    map = get_map(lines)

    trailheads = []

    for y, row in enumerate(map):
        for x, height in enumerate(row):
            if height == 0:
                trailheads.append((x, y))

    sum = 0
    for trailhead in trailheads:
        result = walk_path(trailhead[0], trailhead[1], 0, map)
        sum += len(result)

    return sum


def walk_path_2(x, y, c_h, map):
    if c_h == 9:
        return 1
    peaks = 0

    if y - 1 >= 0 and (c_h + 1) == map[y - 1][x]:
        peaks += walk_path_2(x, y - 1, c_h + 1, map)
    if y + 1 < len(map) and (c_h + 1) == map[y + 1][x]:
        peaks += walk_path_2(x, y + 1, c_h + 1, map)
    if x - 1 >= 0 and (c_h + 1) == map[y][x - 1]:
        peaks += walk_path_2(x - 1, y, c_h + 1, map)
    if x + 1 < len(map[0]) and (c_h + 1) == map[y][x + 1]:
        peaks += walk_path_2(x + 1, y, c_h + 1, map)

    return peaks


def part_2(lines):
    map = get_map(lines)

    trailheads = []

    for y, row in enumerate(map):
        for x, height in enumerate(row):
            if height == 0:
                trailheads.append((x, y))

    sum = 0
    for trailhead in trailheads:
        result = walk_path_2(trailhead[0], trailhead[1], 0, map)
        sum += result

    return sum


def main():
    f = open("./day10/input", "r")
    lines = f.readlines()
    print("Day 10")
    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))


if __name__ == "__main__":
    main()
