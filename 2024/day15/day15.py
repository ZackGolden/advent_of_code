def parse_lines(lines):
    # TODO: Instead of returning a 2d array, let's just store this whole thing in a map, and ignore the empty space
  split_point = 0
  for i, line in enumerate(lines):
    if line is "":
      split_point = i
      break
  return (lines[:split_point], lines[split_point:])



def part_1(lines):
  sum = 0
  return sum

def part_2(lines):
  sum = 0
  return sum

def main():
  f = open("./day15/input", "r")
  lines = f.readlines()
  print("Day 15")
  print("Part 1:", part_1(lines))
  print("Part 2:", part_2(lines))

if __name__ == "__main__":
  main()
