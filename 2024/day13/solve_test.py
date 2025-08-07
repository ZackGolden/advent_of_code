from day13.solve import Machine, part_1, part_2, read_file


def test_read_file1():
    lines = [
        "Button A: X+94, Y+34",
        "Button B: X+22, Y+67",
        "Prize: X=8400, Y=5400",
        "",
    ]
    machines = read_file(lines)
    expected = [Machine(i=94, j=34, k=22, l=67, x=8400, y=5400)]
    assert expected == machines


def test_read_file2():
    lines = [
        "Button A: X+94, Y+34",
        "Button B: X+22, Y+67",
        "Prize: X=8400, Y=5400",
        "",
        "Button A: X+26, Y+66",
        "Button B: X+67, Y+21",
        "Prize: X=12748, Y=12176",
        "",
        "Button A: X+17, Y+86",
        "Button B: X+84, Y+37",
        "Prize: X=7870, Y=6450",
        "",
        "Button A: X+69, Y+23",
        "Button B: X+27, Y+71",
        "Prize: X=18641, Y=10279",
    ]
    machines = read_file(lines)
    expected = [
        Machine(i=94, j=34, k=22, l=67, x=8400, y=5400),
        Machine(i=26, j=66, k=67, l=21, x=12748, y=12176),
        Machine(i=17, j=86, k=84, l=37, x=7870, y=6450),
        Machine(i=69, j=23, k=27, l=71, x=18641, y=10279),
    ]
    assert expected == machines


def test_part1_1():
    machines = [Machine(i=94, j=34, k=22, l=67, x=8400, y=5400)]
    result = part_1(machines)
    assert 280 == result


def test_part1_2():
    machines = [Machine(i=26, j=66, k=67, l=21, x=12748, y=12176)]
    result = part_1(machines)
    assert 0 == result


def test_part1_3():
    machines = [Machine(i=17, j=86, k=84, l=37, x=7870, y=6450)]
    result = part_1(machines)
    assert 200 == result


def test_part1_4():
    machines = [Machine(i=69, j=23, k=27, l=71, x=18641, y=10279)]
    result = part_1(machines)
    assert 0 == result


def test_part2_1():
    machines = [Machine(i=94, j=34, k=22, l=67, x=8400, y=5400)]
    result = part_2(machines)
    assert 0 == result


def test_part2_2():
    machines = [Machine(i=26, j=66, k=67, l=21, x=12748, y=12176)]
    result = part_2(machines)
    assert 459236326669 == result


def test_part2_3():
    machines = [Machine(i=17, j=86, k=84, l=37, x=7870, y=6450)]
    result = part_2(machines)
    assert 0 == result


def test_part2_4():
    machines = [Machine(i=69, j=23, k=27, l=71, x=18641, y=10279)]
    result = part_2(machines)
    assert 416082282239 == result
