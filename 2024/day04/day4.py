def check_for_xmas(lines, x, y):
    directions = []
    count = 0
    # check N
    if y > 0 and lines[y - 1][x] == "M":
        directions.append("N")
    # check NE
    if y > 0 and x + 1 < len(lines[0]) and lines[y - 1][x + 1] == "M":
        directions.append("NE")
    # check E
    if x + 1 < len(lines[0]) and lines[y][x + 1] == "M":
        directions.append("E")
    # Check SE
    if y + 1 < len(lines) and x + 1 < len(lines[0]) and lines[y + 1][x + 1] == "M":
        directions.append("SE")
    # Check S
    if y + 1 < len(lines) and lines[y + 1][x] == "M":
        directions.append("S")
    # Check SW
    if y + 1 < len(lines) and x > 0 and lines[y + 1][x - 1] == "M":
        directions.append("SW")
    # Check W
    if x > 0 and lines[y][x - 1] == "M":
        directions.append("W")
    # Check NW
    if y > 0 and x > 0 and lines[y - 1][x - 1] == "M":
        directions.append("NW")

    for direction in directions:
        x_dir = 0
        y_dir = 0
        match direction:
            case "N":
                y_dir = -1
            case "NE":
                x_dir = 1
                y_dir = -1
            case "E":
                x_dir = 1
            case "SE":
                x_dir = 1
                y_dir = 1
            case "S":
                y_dir = 1
            case "SW":
                x_dir = -1
                y_dir = 1
            case "W":
                x_dir = -1
            case "NW":
                x_dir = -1
                y_dir = -1

        # Check for A
        temp_x = x + (2 * x_dir)
        temp_y = y + (2 * y_dir)
        if (temp_x >= 0 and temp_x < len(lines[0])) and (
            temp_y >= 0 and temp_y < len(lines)
        ):
            if lines[temp_y][temp_x] == "A":
                # Check for S
                temp_x = x + (3 * x_dir)
                temp_y = y + (3 * y_dir)
                if (temp_x >= 0 and temp_x < len(lines[0])) and (
                    temp_y >= 0 and temp_y < len(lines)
                ):
                    if lines[temp_y][temp_x] == "S":
                        count += 1
    return count


def part_1(lines):
    count = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "X":
                count += check_for_xmas(lines, x, y)
    return count


def check_for_x_mas(lines, x, y):
    count = 0
    nw = lines[y - 1][x - 1]
    ne = lines[y - 1][x + 1]
    sw = lines[y + 1][x - 1]
    se = lines[y + 1][x + 1]

    if nw == "M" and ne == "M" and sw == "S" and se == "S":
        return 1
    elif nw == "M" and ne == "S" and sw == "M" and se == "S":
        return 1
    elif nw == "S" and ne == "S" and sw == "M" and se == "M":
        return 1
    elif nw == "S" and ne == "M" and sw == "S" and se == "M":
        return 1
    return 0


def part_2(lines):
    count = 0
    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines[0]) - 1):
            if lines[y][x] == "A":
                count += check_for_x_mas(lines, x, y)
    return count


def main():
    f = open("./day4/input", "r")
    lines = f.readlines()
    print("Day 4")
    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))


if __name__ == "__main__":
    main()
