from day10 import get_map, part_1, part_2, walk_path


def test_get_map():
    lines = ["0123\n", "1234\n", "8765\n", "9876\n", ""]
    actual = get_map(lines)
    expected = [[0, 1, 2, 3], [1, 2, 3, 4], [8, 7, 6, 5], [9, 8, 7, 6]]
    assert actual == expected


def test_walk_path():
    map = [[0, 1, 2, 3], [1, 2, 3, 4], [8, 7, 6, 5], [9, 8, 7, 6]]
    actual = walk_path(0, 0, 0, map)
    expected = {(0, 3)}
    assert actual == expected


def test_part1_1():
    lines = ["0123\n", "1234\n", "8765\n", "9876\n", ""]
    result = part_1(lines)
    assert 1 == result


def test_part1_2():
    lines = [
        "89010123\n",
        "78121874\n",
        "87430965\n",
        "96549874\n",
        "45678903\n",
        "32019012\n",
        "01329801\n",
        "10456732\n",
        "",
    ]
    result = part_1(lines)
    assert 36 == result


def test_part2():
    lines = [
        "89010123\n",
        "78121874\n",
        "87430965\n",
        "96549874\n",
        "45678903\n",
        "32019012\n",
        "01329801\n",
        "10456732\n",
        "",
    ]
    result = part_2(lines)
    assert 81 == result
