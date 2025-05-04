def find_cursor(lines):
  i,j = 0,0
  x,y = None, None
  found = False
  while i < len(lines) and not found:
    j = 0
    while j < len(lines[0]) and not found:
      if lines[i][j] in {'<','>','V','^'}:
        x,y = j,i
        found = True
      j += 1
    i += 1
  return (x,y)

def build_path(lines):
  (x,y) = find_cursor(lines)

  x_dir, y_dir = 0,0
  match lines[y][x]:
    case '<':
      x_dir = -1
    case '>':
      y_dir = 1
    case '^':
      y_dir = -1
    case 'V':
      y_dir = 1

  done = False
  new_lines = []
  for line in lines:
    current = []
    for c in line:
      current.append(c)
    new_lines.append(current)

  new_lines[y][x] = 'X'
  while not done:
    if y+y_dir == len(new_lines) or y+y_dir < 0:
      done = True
    elif x+x_dir == len(new_lines[0]) or x+x_dir < 0:
      done = True
    else:
      match new_lines[y + y_dir][x + x_dir]:
        case '.' | 'X':
          y += y_dir
          x += x_dir
          new_lines[y][x] = 'X'
        case '#':
          if x_dir == 1:
            x_dir = 0
            y_dir = 1
          elif x_dir == -1:
            x_dir = 0
            y_dir = -1
          elif y_dir == 1:
            x_dir = -1
            y_dir = 0
          elif y_dir == -1:
            x_dir = 1
            y_dir = 0
  return new_lines

def part_1(lines):
  solved_path = build_path(lines)

  sum = 0
        
  for line in solved_path:
    for c in line:
      if c == 'X':
        sum += 1

  return sum


def is_loop(lines):
  (x,y) = find_cursor(lines)

  x_dir, y_dir = 0,0
  match lines[y][x]:
    case '<':
      x_dir = -1
    case '>':
      y_dir = 1
    case '^':
      y_dir = -1
    case 'V':
      y_dir = 1

  done = False
  new_lines = lines
  while not done:
    if y+y_dir >= len(new_lines) or y+y_dir < 0:
      done = True
    elif x+x_dir >= len(new_lines[0]) or x+x_dir < 0:
      done = True
    else:
      match new_lines[y + y_dir][x + x_dir]:
        case '.' | '|' | '-' | '+' | 'V' | '^' | '>' | '<':
          y += y_dir
          x += x_dir
          new_val = None
          if x_dir == 0:
            if y_dir == 1:
              new_val = 'V'
              if new_lines[y][x] in {'^','|'}:
                new_val = '|'
            else:
              new_val = '^'
              if new_lines[y][x] in {'V', '|'}:
                new_val = '|'
          elif y_dir == 0:
            if x_dir == 1:
              new_val = '>'
              if new_lines[y][x] in {'<', '-'}:
                new_val = '-'
            else:
              new_val = '<'
              if new_lines[y][x] in {'>', '-'}:
                new_val = '-'
          if new_val == new_lines[y][x]:
            return True
          new_lines[y][x] = new_val
        case '#' | 'O':
          if x_dir == 1:
            x_dir = 0
            y_dir = 1
          elif x_dir == -1:
            x_dir = 0
            y_dir = -1
          elif y_dir == 1:
            x_dir = -1
            y_dir = 0
          elif y_dir == -1:
            x_dir = 1
            y_dir = 0
        case _:
          print('x:',x,'y:',y)
          done = True
  return False

def part_2(lines):
  solved_path = build_path(lines)

  # Find Cursor
  (c_x,c_y) = find_cursor(lines)

  new_lines = []
  for line in lines:
    current = []
    for c in line:
      if c != '\n':
        current.append(c)
    new_lines.append(current)

  sum = 0
  # Iterate through obstacle locations
  i = 0
  while i < len(solved_path):
    j = 0
    while j < len(solved_path[0]):
      if solved_path[i][j] == 'X':
        if i == c_y and j == c_x:
          j += 1
          continue

        temp = []
        for line in new_lines:
          temp.append(line.copy())
        temp[i][j] = 'O'
        if is_loop(temp):
          sum += 1
      j += 1
    i += 1

  return sum

def main():
  f = open("./day6/input", "r")
  lines = f.readlines()
  print("Day 6")
  print("Part 1:", part_1(lines))
  print("Part 2:", part_2(lines))
  
if __name__ == "__main__":
  main()
