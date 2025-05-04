import re

def safety_test(levels):
  asc = True
  desc = True
  dist = True
  for i in range(1, len(levels)):
    current = 0
    if levels[i-1] > levels[i]:
      current = levels[i-1] - levels[i]
      asc = False
    else:
      current = levels[i] - levels[i-1]
      desc = False
    if abs(current) > 3 or abs(current) == 0:
      dist = False
  if dist and (asc or desc):
    return True

def part_1(lines):
  safe = 0
  for line in lines:
    levels = list(map(int, re.findall(r'\d+', line)))
    if safety_test(levels):
      safe += 1

  return safe

def part_2(lines):
  safe = 0
  for line in lines:
    levels = list(map(int, re.findall(r'\d+', line)))
    if safety_test(levels):
      safe += 1
    else:
      for i in range(len(levels)):
        new_list = levels.copy()
        new_list.pop(i)
        if safety_test(new_list):
          safe += 1
          break
  return safe

def main():
  f = open("./day2/input", "r")
  lines = f.readlines()
  print("Day 2")
  print("Part 1:", part_1(lines))
  print("Part 2:", part_2(lines))
  
if __name__ == "__main__":
  main()
