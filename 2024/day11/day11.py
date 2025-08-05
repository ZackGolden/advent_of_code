import re
import math


def parse_it(lines):
    return list(map(int, re.findall(r"\d+", lines[0])))


def blink(line):
    new_line = []
    for rock in line:
        if rock == 0:
            new_line.append(1)
        elif int(math.log10(rock) + 1) % 2 == 0:
            digits = int(math.log10(rock) + 1)
            new_line.append(rock // (10 ** (digits // 2)))
            new_line.append(rock % (10 ** (digits // 2)))
        else:
            new_line.append(rock * 2024)

    return new_line


def part_1(lines):
    line = parse_it(lines)

    for i in range(25):
        line = blink(line)

    sum = len(line)
    return sum


def blink_map(line_map):
    new_line_map = {}
    for rock in line_map:
        if rock == 0:
            if 1 in new_line_map:
                new_line_map[1] += line_map[rock]
            else:
                new_line_map[1] = line_map[rock]
        elif int(math.log10(rock) + 1) % 2 == 0:
            digits = int(math.log10(rock) + 1)
            left, right = rock // (10 ** (digits // 2)), rock % (10 ** (digits // 2))
            if left in new_line_map:
                new_line_map[left] += line_map[rock]
            else:
                new_line_map[left] = line_map[rock]
            if right in new_line_map:
                new_line_map[right] += line_map[rock]
            else:
                new_line_map[right] = line_map[rock]
        else:
            if rock * 2024 in new_line_map:
                new_line_map[rock * 2024] += line_map[rock]
            else:
                new_line_map[rock * 2024] = line_map[rock]

    return new_line_map


def part_2(lines):
    line = parse_it(lines)

    line_map = {}
    for i in line:
        if i in line_map:
            line_map[i] += 1
        else:
            line_map[i] = 1

    for i in range(75):
        line_map = blink_map(line_map)

    sum = 0
    for rock in line_map:
        sum += line_map[rock]

    return sum


def main():
    f = open("./day11/input", "r")
    lines = f.readlines()
    print("Day 11")
    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))


if __name__ == "__main__":
    main()
