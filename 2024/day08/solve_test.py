from day08.solve import (
    find_antennas,
    find_antinodes,
    find_resonate_antinodes,
    part_1,
    part_2,
)


def test_find_antennas():
    lines = [
        "............\n",
        "........0...\n",
        ".....0......\n",
        ".......0....\n",
        "....0.......\n",
        "......A.....\n",
        "............\n",
        "............\n",
        "........A...\n",
        ".........A..\n",
        "............\n",
        "............\n",
    ]
    result = find_antennas(lines)
    expected = {"0": [(8, 1), (5, 2), (7, 3), (4, 4)], "A": [(6, 5), (8, 8), (9, 9)]}
    assert result == expected


def test_find_antinodes():
    antennas = {"a": [(4, 3), (5, 5)]}
    result = find_antinodes(antennas)
    expected = {(3, 1), (6, 7)}
    assert result == expected


def test_part1():
    lines = [
        "............\n",
        "........0...\n",
        ".....0......\n",
        ".......0....\n",
        "....0.......\n",
        "......A.....\n",
        "............\n",
        "............\n",
        "........A...\n",
        ".........A..\n",
        "............\n",
        "............\n",
    ]
    result = part_1(lines)
    assert 14 == result


def test_find_resonate_antinodes():
    antennas = {"T": [(0, 0), (3, 1), (1, 2)]}
    results = find_resonate_antinodes(antennas, 10, 9)
    expected = {(0, 0), (3, 1), (1, 2), (5, 0), (6, 2), (9, 3), (2, 4), (3, 6), (4, 8)}
    assert results == expected


def test_part2():
    lines = [
        "............\n",
        "........0...\n",
        ".....0......\n",
        ".......0....\n",
        "....0.......\n",
        "......A.....\n",
        "............\n",
        "............\n",
        "........A...\n",
        ".........A..\n",
        "............\n",
        "............\n",
    ]
    result = part_2(lines)
    assert 34 == result
