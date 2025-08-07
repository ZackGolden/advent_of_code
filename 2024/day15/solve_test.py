from day15.solve import parse_lines, part_1, part_2, score


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
        "",
    ]
    actual = parse_lines(lines)
    print(actual)
    expected = (
        {
            (0, 0): "#",
            (1, 0): "#",
            (2, 0): "#",
            (3, 0): "#",
            (4, 0): "#",
            (5, 0): "#",
            (6, 0): "#",
            (7, 0): "#",
            (0, 1): "#",
            (3, 1): "O",
            (5, 1): "O",
            (7, 1): "#",
            (0, 2): "#",
            (1, 2): "#",
            (2, 2): "@",
            (4, 2): "O",
            (7, 2): "#",
            (0, 3): "#",
            (4, 3): "O",
            (7, 3): "#",
            (0, 4): "#",
            (2, 4): "#",
            (4, 4): "O",
            (7, 4): "#",
            (0, 5): "#",
            (4, 5): "O",
            (7, 5): "#",
            (0, 6): "#",
            (7, 6): "#",
            (0, 7): "#",
            (1, 7): "#",
            (2, 7): "#",
            (3, 7): "#",
            (4, 7): "#",
            (5, 7): "#",
            (6, 7): "#",
            (7, 7): "#",
        },
        ((2, 2), "<^^>>>vv<v>>v<<"),
    )
    assert actual == expected


def test_score_1():
    (warehouse, (_, _)) = parse_lines(
        [
            "########",
            "#....OO#",
            "###.....#",
            "#.....O#",
            "#.#O@..#",
            "#...O..#",
            "#...O..#",
            "########",
            "",
        ]
    )
    actual = score(warehouse)
    expected = 2028
    assert actual == expected


def test_score_2():
    (warehouse, (_, _)) = parse_lines(
        [
            "##########",
            "#.O.O.OOO#",
            "#........#",
            "#OO......#",
            "#OO@.....#",
            "#O#.....O#",
            "#O.....OO#",
            "#O.....OO#",
            "#OO....OO#",
            "##########",
            "",
        ]
    )
    actual = score(warehouse)
    assert actual == 10092


def test_part1_1():
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
        "",
    ]
    (warehouse, ((robot), moves)) = parse_lines(lines)
    actual = part_1(warehouse, robot, moves)
    assert 2028 == actual


def test_part1_2():
    lines = [
        "##########",
        "#..O..O.O#",
        "#......O.#",
        "#.OO..O.O#",
        "#..O@..O.#",
        "#O#..O...#",
        "#O..O..O.#",
        "#.OO.O.OO#",
        "#....O...#",
        "##########",
        "",
        "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^",
        "vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v",
        "><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<",
        "<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^",
        "^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><",
        "^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^",
        ">^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^",
        "<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>",
        "^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>",
        "v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^",
        "",
    ]
    (warehouse, ((robot), moves)) = parse_lines(lines)
    actual = part_1(warehouse, robot, moves)
    assert 10092 == actual


def test_part2():
    lines = [""]
    (warehouse, ((robot), moves)) = parse_lines(lines)
    actual = part_2(warehouse, robot, moves)
    assert 0 == actual
