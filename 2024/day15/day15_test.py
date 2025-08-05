from day15 import parse_lines, part_1, part_2


def test_parse_lines():
    lines = [
        "########",
        "#..O.O.#",
        "##@.O..#",
        "#...O..#",
        "#.#.O..#",
        "#...O..#",
        "#......#",
        "########",
        "",
        "<^^>>>vv<v>>v<<",
        ""
    ]
    actual = parse_lines(lines)
    print(actual)


def test_part1():
    lines = [""]
    result = part_1(lines)
    assert 0 == result


def test_part2():
    lines = [""]
    result = part_2(lines)
    assert 0 == result
