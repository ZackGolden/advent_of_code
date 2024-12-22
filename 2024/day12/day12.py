def parse_it(lines):
  garden_set = {}
  for y,line in enumerate(lines):
    for x,plot in enumerate(line):
      if plot not in {"\n"}:
        garden_set[(x,y)] = plot
  return garden_set

def find_region(x,y,map):
  def go(x, y, region):
    plant = map[(x,y)]
    region.add((x,y))
    dirs = [
      (x-1,y),
      (x+1,y),
      (x,y-1),
      (x,y+1)
    ]
    for dir in dirs:
      if (dir in map) and (dir not in region) and (map[(dir[0],dir[1])] == plant):
        go(dir[0],dir[1],region)
    map.pop((x,y))
    return region
  return go(x,y,set())

def find_perimeter(region):
  perimeter = 0
  for x,y in region[1]:
    dirs = [
      (x-1,y),
      (x+1,y),
      (x,y-1),
      (x,y+1)
    ]
    perimeter += 4
    for dir in dirs:
      if dir in region[1]:
        perimeter -= 1
  return perimeter

def part_1(lines):
  map = parse_it(lines)
  
  regions = []
  while len(map) > 0:
    current = list(map.keys())[0]
    regions.append((
        map[current],
        find_region(current[0],current[1],map)
      ))

  sum = 0
  for region in regions:
    print(len(region[1]),find_perimeter(region))
    sum += len(region[1])*find_perimeter(region)

  return sum

def part_2(lines):
  sum = 0
  return sum

def main():
  f = open("./day12/input", "r")
  lines = f.readlines()
  print("Day 12")
  print("Part 1:", part_1(lines))
  print("Part 2:", part_2(lines))

if __name__ == "__main__":
  main()
