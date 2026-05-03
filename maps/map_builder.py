import random

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

def get_start_goal(rows,cols):
  print("Enter START Position (x,y): ")
  start = tuple(map(int, input().split()))
  print("Enter GOAL position (x y): ")
  goal = tuple(map(int, input().split()))
  return start, goal

