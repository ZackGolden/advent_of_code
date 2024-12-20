from day11 import part_1, part_2, parse_it

def test_parse():
  lines = [
    "125 17",
    ""]
  results = parse_it(lines)
  expected = [125, 17]
  assert results == expected

def test_part1():
  lines = [
    "125 17",
    ""]
  result = part_1(lines)
  assert 55312 == result
