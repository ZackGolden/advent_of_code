def find_antennas(lines):
  antennas = {}
  for y,line in enumerate(lines):
    for x,c in enumerate(line):
      if c in {'.', '\n'}:
        continue
      elif c in antennas:
        antennas[c].append((x,y))
      else:
        antennas[c] = [(x,y)]
  return antennas

def find_antinodes(antennas):
  antinodes = set()
  for freq in antennas:
    for i,antenna in enumerate(antennas[freq]):
      for other in antennas[freq][i+1:]:
        x_dif, y_dif = antenna[0]-other[0], antenna[1]-other[1]
        print("x_dif:",x_dif,"y_dif",y_dif)
        antinode_1 = (antenna[0]+x_dif, antenna[1]+y_dif)
        antinode_2 = (other[0]-x_dif, other[1]-y_dif)
        if antinode_1 not in {antenna, other}:
          antinodes.add(antinode_1)
        if antinode_2 not in {antenna, other}:
          antinodes.add(antinode_2)
  return antinodes

def part_1(lines):
  sum = 0

  antennas = find_antennas(lines)
  antinodes = find_antinodes(antennas)

  x_max, y_max = len(lines[0])-1, len(lines)

  for antinode in antinodes:
    if antinode[0] < x_max and antinode[0] >= 0:
      if antinode[1] < y_max and antinode[1] >= 0:
        sum += 1 

  return sum

def part_2(lines):
  sum = 0
  return sum

def main():
  f = open("./day8/input", "r")
  lines = f.readlines()
  print("Day 8")
  print("Part 1:", part_1(lines))
  print("Part 2:", part_2(lines))
  
if __name__ == "__main__":
  main()