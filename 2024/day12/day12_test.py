from day12 import part_1, part_2, parse_it, find_region


def test_parse_it():
    lines = ["AA\n", "BB\n", ""]
    result = parse_it(lines)
    expected = {(0, 0): "A", (1, 0): "A", (0, 1): "B", (1, 1): "B"}
    print("Result:", result)
    print("expected:", expected)
    assert result == expected


def test_find_region():
    map = {(0, 0): "A", (1, 0): "A", (0, 1): "B", (1, 1): "B"}
    result = find_region(0, 0, map)
    expected = {(0, 0), (1, 0)}
    assert result == expected


def test_part1_1():
    lines = ["AAAA\n", "BBCD\n", "BBCC\n", "EEEC\n", ""]
    result = part_1(lines)
    assert 140 == result


def test_part1_2():
    lines = ["OOOOO\n", "OXOXO\n", "OOOOO\n", "OXOXO\n", "OOOOO\n", ""]
    result = part_1(lines)
    assert 772 == result


def test_part1_3():
    lines = [
        "RRRRIICCFF\n",
        "RRRRIICCCF\n",
        "VVRRRCCFFF\n",
        "VVRCCCJFFF\n",
        "VVVVCJJCFE\n",
        "VVIVCCJJEE\n",
        "VVIIICJJEE\n",
        "MIIIIIJJEE\n",
        "MIIISIJEEE\n",
        "MMMISSJEEE\n",
        "",
    ]
    result = part_1(lines)
    assert 1930 == result


def test_part2_1():
    lines = ["AAAA\n", "BBCD\n", "BBCC\n", "EEEC\n", ""]
    result = part_2(lines)
    assert 80 == result


def test_part2_2():
    lines = ["OOOOO\n", "OXOXO\n", "OOOOO\n", "OXOXO\n", "OOOOO\n", ""]
    result = part_2(lines)
    assert 436 == result


def test_part2_3():
    lines = ["EEEEE\n", "EXXXX\n", "EEEEE\n", "EXXXX\n", "EEEEE\n", ""]
    result = part_2(lines)
    assert 236 == result


def test_part2_4():
    lines = ["AAAAAA\n", "AAABBA\n", "AAABBA\n", "ABBAAA\n", "ABBAAA\n", "AAAAAA\n", ""]
    result = part_2(lines)
    assert 368 == result


def test_part2_5():
    lines = [
        "RRRRIICCFF\n",
        "RRRRIICCCF\n",
        "VVRRRCCFFF\n",
        "VVRCCCJFFF\n",
        "VVVVCJJCFE\n",
        "VVIVCCJJEE\n",
        "VVIIICJJEE\n",
        "MIIIIIJJEE\n",
        "MIIISIJEEE\n",
        "MMMISSJEEE\n",
        "",
    ]
    result = part_2(lines)
    assert 1206 == result
