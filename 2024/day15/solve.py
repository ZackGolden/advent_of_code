from typing import Tuple


def parse_lines(
    lines,
) -> Tuple[dict[Tuple[int, int], str], Tuple[Tuple[int, int], str]]:
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
                if tile == "@":
                    robot = (x, y)

    instructions: str = "".join(lines[split_point:])
    return (warehouse, (robot, instructions))


def score(warehouse: dict[Tuple[int, int], str]) -> int:
    sum = 0
    for (x, y), tile in warehouse.items():
        if tile == "O":
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

    # for y in range(50):
    #    for x in range(50):
    #        c = warehouse.get((x, y), ".")
    #        print(c, end="")
    #    print()
    return score(warehouse)


def parse_lines_part2(
    lines,
) -> Tuple[dict[Tuple[int, int], str], Tuple[Tuple[int, int], str]]:
    split_point = 0
    warehouse: dict[Tuple[int, int], str] = {}
    robot = (0, 0)

    for y, line in enumerate(lines):
        if line == "":
            split_point = y
            break
        for x, tile in enumerate(line):
            if tile in {"#", "O", "@"}:
                match tile:
                    case "@":
                        robot = (2 * x, y)
                        warehouse[(2 * x, y)] = "@"
                    case "#":
                        warehouse[(2 * x, y)] = "#"
                        warehouse[(2 * x + 1, y)] = "#"
                    case "O":
                        warehouse[(2 * x, y)] = "["
                        warehouse[(2 * x + 1, y)] = "]"

    instructions: str = "".join(lines[split_point:])
    return (warehouse, (robot, instructions))


def parse_lines_already_expanded(
    lines,
) -> Tuple[dict[Tuple[int, int], str], Tuple[Tuple[int, int], str]]:
    split_point = 0
    warehouse: dict[Tuple[int, int], str] = {}
    robot = (0, 0)

    for y, line in enumerate(lines):
        if line == "":
            split_point = y
            break
        for x, tile in enumerate(line):
            if tile in {"#", "O", "@", "[", "]"}:
                warehouse[(x, y)] = tile
                if tile == "@":
                    robot = (x, y)

    instructions: str = "".join(lines[split_point:])
    return (warehouse, (robot, instructions))


def score_part2(warehouse: dict[Tuple[int, int], str]) -> int:
    sum = 0
    for (x, y), tile in warehouse.items():
        if tile == "[":
            sum += y * 100 + x
    return sum


def part_2(warehouse, robot, moves):
    tile_stack = list()
    tile_set = set()

    def do(current: Tuple[int, int], dir: Tuple[int, int]):
        next = (current[0] + dir[0], current[1] + dir[1])
        match warehouse.get(next, "."):
            case "#":
                return False
            case "[" | "]":
                if dir in {(0, -1), (0, 1)}:
                    if warehouse.get(next, ".") == "]":
                        if do(next, dir) and do((next[0] - 1, next[1]), dir):
                            if (tile := (current, next)) not in tile_set:
                                tile_stack.append(tile)
                                tile_set.add(tile)
                            return True
                        else:
                            return False
                    else:
                        if do(next, dir) and do((next[0] + 1, next[1]), dir):
                            if (tile := (current, next)) not in tile_set:
                                tile_stack.append(tile)
                                tile_set.add(tile)
                            return True
                        else:
                            return False
                else:
                    if do(next, dir):
                        if (tile := (current, next)) not in tile_set:
                            tile_stack.append(tile)
                            tile_set.add(tile)
                        return True
                    else:
                        return False
            case _:
                if (tile := (current, next)) not in tile_set:
                    tile_stack.append(tile)
                    tile_set.add(tile)
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
        tile_stack = list()
        tile_set = set()

        ## Check the movement and update the warehouse
        if do(robot, dir):
            robot = (robot[0] + dir[0], robot[1] + dir[1])
            for tile_coord in tile_stack:
                tile = warehouse.pop(tile_coord[0])
                warehouse[tile_coord[1]] = tile

    ## Print the Map
    # for y in range(50):
    #    for x in range(100):
    #        c = warehouse.get((x, y), ".")
    #        print(c, end="")
    #    print()
    return score_part2(warehouse)


def main():
    f = open("./day15/input", "r")
    lines = f.readlines()
    print("Day 15")
    (warehouse, ((robot), moves)) = parse_lines(lines)
    print("Part 1:", part_1(warehouse, robot, moves))
    (warehouse, ((robot), moves)) = parse_lines_part2(lines)
    print("Part 2:", part_2(warehouse, robot, moves))


if __name__ == "__main__":
    main()
