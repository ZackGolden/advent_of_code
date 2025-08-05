from day7 import (
    part_1,
    part_2,
    line_parse,
    ternary,
    valid_equation,
    valid_equation_with_concat,
)


def test_line_parse():
    line = "190: 10 19\n"
    result = line_parse(line)
    assert (190, [10, 19]) == result


def test_valid_equation_true():
    assert valid_equation(190, [10, 19])


def test_valid_equation_false():
    assert not valid_equation(192, [17, 8, 14])


def test_part1():
    lines = [
        "190: 10 19\n",
        "3267: 81 40 27\n",
        "83: 17 5\n",
        "156: 15 6\n",
        "7290: 6 8 6 15\n",
        "161011: 16 10 13\n",
        "192: 17 8 14\n",
        "21037: 9 7 18 13\n",
        "292: 11 6 16 20\n",
    ]
    result = part_1(lines)
    assert 3749 == result


def test_ternary():
    assert ternary(3) == "10"


def test_valid_equation_with_concat_true():
    assert valid_equation_with_concat(7290, [6, 8, 6, 15])


def test_valid_equation_with_concat_false():
    assert not valid_equation_with_concat(83, [17, 5])


def test_part2():
    lines = [
        "190: 10 19\n",
        "3267: 81 40 27\n",
        "83: 17 5\n",
        "156: 15 6\n",
        "7290: 6 8 6 15\n",
        "161011: 16 10 13\n",
        "192: 17 8 14\n",
        "21037: 9 7 18 13\n",
        "292: 11 6 16 20\n",
    ]
    result = part_2(lines)
    assert 11387 == result
