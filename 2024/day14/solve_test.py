from day14.solve import move_robot, parse_lines, part_1


def test_parse1():
    lines = ["p=0,4 v=3,-3"]
    expected = [((0, 4), (3, -3))]
    actual = parse_lines(lines)
    assert actual == expected


def test_parse2():
    lines = [
        "p=0,4 v=3,-3",
        "p=6,3 v=-1,-3",
        "p=10,3 v=-1,2",
        "p=2,0 v=2,-1",
        "p=0,0 v=1,3",
        "p=3,0 v=-2,-2",
        "p=7,6 v=-1,-3",
        "p=3,0 v=-1,-2",
        "p=9,3 v=2,3",
        "p=7,3 v=-1,2",
        "p=2,4 v=2,-3",
        "p=9,5 v=-3,-3",
    ]
    expected = [
        ((0, 4), (3, -3)),
        ((6, 3), (-1, -3)),
        ((10, 3), (-1, 2)),
        ((2, 0), (2, -1)),
        ((0, 0), (1, 3)),
        ((3, 0), (-2, -2)),
        ((7, 6), (-1, -3)),
        ((3, 0), (-1, -2)),
        ((9, 3), (2, 3)),
        ((7, 3), (-1, 2)),
        ((2, 4), (2, -3)),
        ((9, 5), (-3, -3)),
    ]
    actual = parse_lines(lines)
    assert actual == expected


def test_move_robot1():
    actual = move_robot(11, 7, 5, 2, 4, 2, -3)
    expected = (1, 3)
    assert actual == expected


def test_part1():
    robots = [
        ((0, 4), (3, -3)),
        ((6, 3), (-1, -3)),
        ((10, 3), (-1, 2)),
        ((2, 0), (2, -1)),
        ((0, 0), (1, 3)),
        ((3, 0), (-2, -2)),
        ((7, 6), (-1, -3)),
        ((3, 0), (-1, -2)),
        ((9, 3), (2, 3)),
        ((7, 3), (-1, 2)),
        ((2, 4), (2, -3)),
        ((9, 5), (-3, -3)),
    ]
    result = part_1(height=7, width=11, robots=robots)
    assert 12 == result
