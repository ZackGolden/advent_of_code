import re
from functools import cmp_to_key

def build_orderer(list):
  order = {}
  for item in list:
    if item[0] in order:
      order[item[0]].add(item[1])
    else:
      order[item[0]] = {item[1]}
  return order

def tupler(t):
  return (int(t[0]), int(t[1]))

def checker(order_map, pages):
  for i in range(len(pages)):
    for j in range(0,i):
      if pages[j] in order_map.get(pages[i], set()):
        return False
  return True

def part_1(lines):
  sum = 0
  i = 0
  order_list = []
  while lines[i] != "\n":
    current = re.findall(r'(?P<first>\d+)\|(?P<second>\d+)', lines[i])[0]
    order_list.append(tupler(current))
    i += 1
  
  orderer_map = build_orderer(order_list)

  for j in range(i+1, len(lines)):
    page_list = list(map(int,re.findall(r'\d+',lines[j])))
    if checker(orderer_map, page_list):
      sum += page_list[len(page_list)//2]

  return sum



def part_2(lines):
  sum = 0
  i = 0
  order_list = []
  while lines[i] != "\n":
    current = re.findall(r'(?P<first>\d+)\|(?P<second>\d+)', lines[i])[0]
    order_list.append(tupler(current))
    i += 1
  
  orderer_map = build_orderer(order_list)

  def compare(item1, item2):
    if item2 in orderer_map.get(item1, set()):
      return 1
    elif item1 in orderer_map.get(item2, set()):
      return -1
    else:
      return 0

  for j in range(i+1, len(lines)):
    page_list = list(map(int,re.findall(r'\d+',lines[j])))
    if not checker(orderer_map, page_list):
      page_list.sort(key=cmp_to_key(compare))
      sum += page_list[len(page_list)//2]

  return sum

def main():
  f = open("./day5/input", "r")
  lines = f.readlines()
  print("Day 5")
  print("Part 1:", part_1(lines))
  print("Part 2:", part_2(lines))
  
if __name__ == "__main__":
  main()
