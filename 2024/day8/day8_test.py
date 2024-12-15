from day8 import part_1, part_2, find_antennas, find_antinodes

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
    "............\n"
    ]
    result = find_antennas(lines)
    expected = {
       "0": [(8,1),(5,2),(7,3),(4,4)],
       "A": [(6,5),(8,8),(9,9)]
    }
    assert result == expected

def test_find_antinodes():
  antennas = {'a': [(4,3),(5,5)]}
  result = find_antinodes(antennas)
  expected = {
     (3,1),(6,7)
  }
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
    "............\n"
    ]
  result = part_1(lines)
  assert 14 == result
