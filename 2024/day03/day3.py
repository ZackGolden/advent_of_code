import re

def int_and_mult(operands):
  return int(operands[0]) * int(operands[1])

def part_1(lines):
  sum = 0
  for line in lines:
    mulls = list(map(int_and_mult,re.findall(r'mul\((?P<first>\d+),(?P<second>\d+)\)', line)))
    for i in mulls:
      sum += i
  return sum

def part_2(lines):
  sum = 0
  is_enabled = True
  for line in lines:
    mulls = list(re.findall(r"(mul\((?P<first>\d+),(?P<second>\d+)\)|do\(\)|don't\(\))", line))
    for mull in mulls:
      if mull[0] == "don't()":
        is_enabled = False
      elif mull[0] == "do()":
        is_enabled = True
      else:
        if is_enabled:
          sum += int(mull[1]) * int(mull[2])
  return sum

def main():
  f = open("./day3/input", "r")
  lines = f.readlines()
  print("Day 3")
  print("Part 1:", part_1(lines))
  print("Part 2:", part_2(lines))
  
if __name__ == "__main__":
  main()
