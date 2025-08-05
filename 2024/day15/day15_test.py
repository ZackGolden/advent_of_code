from day15 import part_1, part_2, parse_lines


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
    ]


def test_part1():
    lines = [""]
    result = part_1(lines)
    assert 0 == result


def test_part2():
    lines = [""]
    result = part_2(lines)
    assert 0 == result
