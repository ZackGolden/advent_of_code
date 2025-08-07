from typing import List, Tuple


def parse_lines(
    lines,
) -> Tuple[dict[Tuple[int, int], str], Tuple[Tuple[int, int], str]]:
    # TODO: Instead of returning a 2d array, let's just store this whole thing in a map, and ignore the empty space
    split_point = 0
    warehouse: dict[Tuple[int, int], str] = {}
    robot = (0, 0)

    for y, line in enumerate(lines):
        if line == "":
            split_point = y
            break
        for x, tile in enumerate(line):
            if tile in {"#", "O", "@"}:
                warehouse[(x, y)] = tile
                if tile is "@":
                    robot = (x, y)

    instructions: str = "".join(lines[split_point:])
    return (warehouse, (robot, instructions))


def score(warehouse: dict[Tuple[int, int], str]) -> int:
    sum = 0
    for (x, y), tile in warehouse.items():
        if tile is "O":
            sum += y * 100 + x
    return sum


def part_1(warehouse, robot, moves):
    def do(current: Tuple[int, int], dir: Tuple[int, int]):
        next = (current[0] + dir[0], current[1] + dir[1])
        match warehouse.get(next, "."):
            case "#":
                return False
            case "O":
                if do(next, dir):
                    tile = warehouse.pop(current)
                    warehouse[next] = tile
                    return True
                else:
                    return False
            case _:
                tile = warehouse.pop(current)
                warehouse[next] = tile
                return True

    for move in moves:
        dir = (0, 0)
        match move:
            case "<":
                dir = (-1, 0)
            case "^":
                dir = (0, -1)
            case ">":
                dir = (1, 0)
            case "v":
                dir = (0, 1)
        if do(robot, dir):
            robot = (robot[0] + dir[0], robot[1] + dir[1])

    for y in range(100):
        for x in range(100):
            c = warehouse.get((x, y), ".")
            print(c, end="")
        print()
    return score(warehouse)


def part_2(warehouse, robot, moves):
    sum = 0
    return sum


def main():
    f = open("./day15/input", "r")
    lines = f.readlines()
    (warehouse, ((robot), moves)) = parse_lines(lines)
    print("Day 15")
    print("Part 1:", part_1(warehouse, robot, moves))
    print("Part 2:", part_2(warehouse, robot, moves))


if __name__ == "__main__":
    main()
