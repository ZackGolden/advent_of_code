from day02.solve import part_1, part_2


def test_part1():
    lines = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    ]
    result = part_1(lines)
    assert 2 == result


def test_part2():
    lines = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    ]
    result = part_2(lines)
    assert 4 == result
