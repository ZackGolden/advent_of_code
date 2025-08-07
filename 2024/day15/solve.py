from typing import List, Tuple


def parse_lines(lines) -> Tuple[dict[Tuple[int, int], str], Tuple[Tuple[int, int],List[str]]]:
    # TODO: Instead of returning a 2d array, let's just store this whole thing in a map, and ignore the empty space
    split_point = 0
    warehouse: dict[Tuple[int, int], str] = {}
    robot = (0,0)

    for y, line in enumerate(lines):
        if line == "":
            split_point = y
            break
        for x, tile in enumerate(lines):
            if tile in {'#','O', '@'}:
              warehouse[(x,y)] = tile
              if tile is '@':
                  robot = (x,y)

    instructions: List[str] = lines[split_point:]
    return (warehouse,(robot,instructions))


def part_1(lines):
    sum = 0
    return sum


def part_2(lines):
    sum = 0
    return sum


def main():
    f = open("./day15/input", "r")
    lines = f.readlines()
    print("Day 15")
    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))


if __name__ == "__main__":
    main()
