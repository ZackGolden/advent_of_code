def part_1(lines):
  disk_map = []
  for i in lines[0]:
    if i.isdigit():
      disk_map.append(int(i))
  
  left = 0
  right = len(disk_map)//2 if len(disk_map)%2 == 0 else len(disk_map)//2 + 1
  block = 0
  l_index = 0
  r_index = len(disk_map)-2 if len(disk_map)%2 ==0 else len(disk_map)-1
  hopper = []
  checksum = 0
  
  while l_index <= r_index:
    if l_index % 2 ==0:
      for i in range(disk_map[l_index]):
        checksum += left * block
        block += 1
      left += 1
    else:
      for i in range(disk_map[l_index]):
        if len(hopper) == 0:
          hopper = [right] * disk_map[r_index]
          r_index -= 2
          right -= 1
        hopper.pop()
        checksum += right * block
        block += 1
    l_index += 1

  for i in hopper:
    checksum += right * block
    block += 1
  return checksum

def part_2(lines):
  sum = 0

  return sum

def main():
  f = open("./day9/input", "r")
  lines = f.readlines()
  print("Day 9")
  print("Part 1:", part_1(lines))
  print("Part 2:", part_2(lines))
  
if __name__ == "__main__":
  main()
