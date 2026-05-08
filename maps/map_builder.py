import random
def generate_difficulty_map(rows,cols,level):
  if level == "easy":
    obstacle_prob = 0.1
  elif level == "medium":
    obstacle_prob = 0.25
  elif level == "hard":
    obstacle_prob = 0.4
  else:
    obstacle_prob = 0.2
  return generate_random_grid(rows, cols, obstacle_prob)

def create_empty_grid(rows,cols):
  return [[0 for _ in range(cols)] for _ in range(rows)]

def generate_random_grid(rows,cols,obstacle_prob=0.2):
  grid =[]
  for i in range(rows):
    row = []
    for j in range(cols):
      if random.random() < obstacle_prob:
        row.append(-1)
      else:
        row.append(0)
    grid.append(row)
  return grid

def grid_user_input(rows,cols):
  print("Enter grid row by row (0->EMPTY || -1->OBSTACLE)\n")
  grid=[]
  for i in range(rows):
    while True:
      row = list(map(int,input(f"Row{i}: ").split()))
      if len(row) != cols:
        print("Incorrect number of Columns, Please TRY AGAIN")
      else:
        grid.append(row)
        break
  return grid

def edit_grid(grid,start,goal):
  rows = len(grid)
  cols = len(grid[0])

  print("EDIT MODE: Enter coordinates to toggle obstacle: ")
  print("Type 'done' to Finish\n")

  while True:
    cmd = input("Enter (x,y) or 'done': ")
    if cmd.lower() == "done":
      break
    try:
      x, y = map(int, cmd.split())
    except:
      print("Invalid input! Enter like: 2 3")
      continue
    
    if 0<=x<rows and 0<=y<cols:
      if (x, y) == start or (x, y) == goal:
        print("Cannot modify start/goal position")
      else:
        grid[x][y] = 0 if grid[x][y] == -1 else -1
    else:
      print("Invalid Position")
  return grid

def valid_move(grid,pos):
  x,y = pos
  rows = len(grid)
  cols = len(grid[0])

  directions = [(0,-1),(0,1),(-1,0),(1,0)]

  for dx,dy in directions:
    nx = x + dx 
    ny = y + dy 
    if 0<=nx<rows  and 0<=ny < cols:
      if grid[nx][ny]!=-1:
        return True
  return False

def get_start_goal(rows,cols,grid):
  while True:
    print("Enter START Position (x,y): ")
    start = tuple(map(int, input().split()))
    print("Enter GOAL position (x y): ")
    goal = tuple(map(int, input().split()))
    x,y = start
    gx,gy = goal
    if not(0<=x<rows and 0<=y<cols):
      print("Start Position Out of Bounds")
      continue
    if not(0<=gx<rows and 0<=gy<cols):
      print("End Position Out of Bounds")
      continue
    if grid[x][y]==-1:
      print("Start Position is on Obstacle, Please TRY AGAIN!")
      continue
    if grid[gx][gy]==-1:
      print("End Position is on Obstacle, Please TRY AGAIN!")
      continue
    if not valid_move(grid,start):
      print("Start Position is blocked all sides")
      continue
    if start == goal:
      print("Start and End Position cannot be Same")
      continue
    return start, goal

