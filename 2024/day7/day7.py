import re

def line_parse(line):
  ints = list(map(int,re.findall(r'\d+', line)))
  test_value = ints[0]
  numbers = ints[1:]
  return (test_value, numbers)

def valid_equation(test_value, numbers):
  complexity = 2**(len(numbers)-1)
  for attempt in range(complexity):
    current = numbers[0]
    for i,ops in enumerate("{0:b}".format(attempt).zfill(len(numbers)-1)):
      match ops:
        case '0': # +
          current += numbers[i+1]
        case '1': # *
          current *= numbers[i+1]
    if current == test_value:
      return True
  return False

def part_1(lines):
  sum = 0
  for line in lines:
    current = line_parse(line)
    if valid_equation(current[0], current[1]):
      sum += current[0]

  return sum

def ternary(num):
  if num == 0:
    return '0'
  current = num
  result = ""
  while current != 0:
    result = f'{current % 3}{result}'
    current = current//3
  return result

def valid_equation_with_concat(test_value, numbers):
  complexity = 3**(len(numbers)-1)
  for attempt in range(complexity):
    current = numbers[0]
    for i,ops in enumerate(ternary(attempt).zfill(len(numbers)-1)):
      match ops:
        case '0': # +
          current += numbers[i+1]
        case '1': # *
          current *= numbers[i+1]
        case '2':
          current = int(f'{current}{numbers[i+1]}')
    if current == test_value:
      return True
  return False

def part_2(lines):
  sum = 0
  for line in lines:
    current = line_parse(line)
    if valid_equation_with_concat(current[0], current[1]):
      sum += current[0]

  return sum

def main():
  f = open("./day7/input", "r")
  lines = f.readlines()
  print("Day 7")
  print("Part 1:", part_1(lines))
  print("Part 2:", part_2(lines))
  
if __name__ == "__main__":
  main()
