from day3 import part_1, part_2

def test_part1():
  lines = [
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
     ]
  result = part_1(lines)
  assert 161 == result

def test_part2():
  lines = {
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
  }
  result = part_2(lines)
  assert 48 == result