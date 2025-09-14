from day16.solve import Vertex, part_1, part_2, walk


def test_walk_1():
    lines = [
        "#####",
        "#...#",
        "###.#",
    ]
    ((x, y), distance) = walk(current=(2, 1), dir=(1, 0), distance=1, maze=lines)
    assert ((x, y), distance) == ((3, 1), 2)


def test_walk_2():
    lines = [
        "#####",
        "#...#",
        "#####",
    ]
    ((x, y), distance) = walk(current=(2, 1), dir=(1, 0), distance=1, maze=lines)
    assert ((x, y), distance) == ((3, 1), 2)


def test_walk_3():
    lines = [
        "########",
        "#...E..#",
        "########",
    ]
    ((x, y), distance) = walk(current=(2, 1), dir=(1, 0), distance=1, maze=lines)
    assert ((x, y), distance) == ((4, 1), 3)


def test_walk_4():
    lines = [
        "####.###",
        "#......#",
        "####.###",
    ]
    ((x, y), distance) = walk(current=(2, 1), dir=(1, 0), distance=1, maze=lines)
    assert ((x, y), distance) == ((4, 1), 3)


def test_part1_1():
    lines = [
        "###############",
        "#.......#....E#",
        "#.#.###.#.###.#",
        "#.....#.#...#.#",
        "#.###.#####.#.#",
        "#.#.#.......#.#",
        "#.#.#####.###.#",
        "#...........#.#",
        "###.#.#####.#.#",
        "#...#.....#.#.#",
        "#.#.#.###.#.#.#",
        "#.....#...#.#.#",
        "#.###.#.#.#.#.#",
        "#S..#.....#...#",
        "###############",
        "",
    ]
    result = part_1(lines)
    assert 7036 == result


def test_part1_2():
    lines = [
        "#################",
        "#...#...#...#..E#",
        "#.#.#.#.#.#.#.#.#",
        "#.#.#.#...#...#.#",
        "#.#.#.#.###.#.#.#",
        "#...#.#.#.....#.#",
        "#.#.#.#.#.#####.#",
        "#.#...#.#.#.....#",
        "#.#.#####.#.###.#",
        "#.#.#.......#...#",
        "#.#.###.#####.###",
        "#.#.#...#.....#.#",
        "#.#.#.#####.###.#",
        "#.#.#.........#.#",
        "#.#.#.#########.#",
        "#S#.............#",
        "#################",
        "",
    ]
    result = part_1(lines)
    assert 11048 == result


def test_part2():
    lines = [""]
    result = part_2(lines)
    assert 0 == result
