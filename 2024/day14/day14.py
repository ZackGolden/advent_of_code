from math import inf
import re
from typing import Tuple

def parse_lines(lines):
    robots = []
    for line in lines:
      matches = re.findall(r'-?\d+', line)
      if len(matches) == 4:
          robots.append(
                  (
                     (int(matches[0]),int(matches[1])),
                     (int(matches[2]),int(matches[3])))
                  )
    return robots

def move_robot(width, height, turns, start_x, start_y, step_x, step_y) -> Tuple[int, int]:
    x = (start_x + (turns * step_x))%width
    y = (start_y + (turns * step_y))%height
    return (x,y)

def part_1(height=103, width=101, turns=100, robots=[]):
  safety = 1
  quadrants = [0,0,0,0]

  for r in robots:
    (x,y) = move_robot(width, height, turns, r[0][0], r[0][1], r[1][0], r[1][1])
    if (x < (width//2)) and (y < height//2):
      quadrants[0] += 1
    elif (x > (width//2)) and (y < height//2):
      quadrants[1] += 1
    elif (x > (width//2)) and (y > height//2):
      quadrants[2] += 1
    elif (x < (width//2)) and (y > height//2):
      quadrants[3] += 1

  for q in quadrants:
      safety *= q

  return safety

def display(width, height, robots):
    room = []
    for i in range(height):
        room.append([0] * width)

    for (x,y) in robots:
        room[y][x] += 1

    for line in room:
        for spot in line:
            print(spot,end="")
        print()

def part_2(height=103, width=101, robots=[]):
  interval = 0
  min_safety = part_1(height=height, width=width, turns=0, robots=robots)

  for i in range(width*height):
    current_safety = part_1(height=height, width=width, turns=i, robots=robots)
    if current_safety < min_safety:
        min_safety = current_safety
        interval = i


  #final = []
  #for r in robots:
  #  final.append(move_robot(width, height, interval, r[0][0], r[0][1], r[1][0], r[1][1]))

  #display(width, height, final)

  return interval

def main():
  f = open("./day14/input", "r")
  lines = f.readlines()
  robots = parse_lines(lines)
  print("Day 14")
  print("Part 1:", part_1(robots=robots))
  print("Part 2:", part_2(robots=robots))

if __name__ == "__main__":
  main()
