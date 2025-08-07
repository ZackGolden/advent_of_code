import re


def part_1(lines):
    list_1 = []
    list_2 = []
    for line in lines:
        current = list(map(int, re.findall(r"\d+", line)))
        list_1.append(current[0])
        list_2.append(current[1])
    list_1.sort()
    list_2.sort()
    sum = 0
    for i in range(len(min(list_1, list_2))):
        sum += abs(list_1[i] - list_2[i])
    return sum


def part_2(lines):
    left = []
    right = {}
    for line in lines:
        current = list(map(int, re.findall(r"\d+", line)))
        left.append(current[0])
        if current[1] in right:
            right[current[1]] += 1
        else:
            right[current[1]] = 1

    sum = 0
    for e in left:
        sum += e * right.get(e, 0)
    return sum


def main():
    f = open("./day1/input", "r")

    lines = f.readlines()
    print("Day 1")
    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))


if __name__ == "__main__":
    main()
