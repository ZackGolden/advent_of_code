import re
from dataclasses import dataclass
from typing import List


@dataclass
class Machine:
    # Button A
    i: int  # +x
    j: int  # +y
    # Button B
    k: int  # +x
    e: int  # +y
    # Targets
    x: int
    y: int


def read_file(lines) -> List[Machine]:
    machines: List[Machine] = []
    i, j, k, e, x, y = 0, 0, 0, 0, 0, 0
    for num, line in enumerate(lines):
        matches = re.findall(r"\d+", line)
        match num % 4:
            case 0:  # Button A
                i = int(matches[0])
                j = int(matches[1])
            case 1:  # Button B
                k = int(matches[0])
                e = int(matches[1])
            case 2:  # Prize
                x = int(matches[0])
                y = int(matches[1])
                machines.append(Machine(i, j, k, e, x, y))
            case 3:  # Skip
                continue
    return machines


def part_1(machines):
    sum = 0
    for m in machines:
        a = ((m.y * m.k) - (m.x * m.l)) / ((m.j * m.k) - (m.i * m.l))
        b = ((m.y * m.i) - (m.x * m.j)) / ((m.l * m.i) - (m.k * m.j))
        if (a % 1 == 0) and (b % 1 == 0):
            sum += 3 * a + b
    return int(sum)


def part_2(machines):
    sum = 0
    for m in machines:
        x = m.x + 10000000000000
        y = m.y + 10000000000000
        a = ((y * m.k) - (x * m.l)) / ((m.j * m.k) - (m.i * m.l))
        b = ((y * m.i) - (x * m.j)) / ((m.l * m.i) - (m.k * m.j))
        if (a % 1 == 0) and (b % 1 == 0):
            sum += 3 * a + b
    return int(sum)


def main():
    f = open("./day13/input", "r")
    lines = f.readlines()
    machines = read_file(lines)
    print("Day 13")
    print("Part 1:", part_1(machines))
    print("Part 2:", part_2(machines))


if __name__ == "__main__":
    main()
