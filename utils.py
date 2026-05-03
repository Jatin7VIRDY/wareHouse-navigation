def print_grid(grid,agent,goal):
  temp = [row[:] for row in grid]
  if agent:
    x,y= agent
    temp[x][y]="A"
  
  if goal:
    gx,gy = goal
    temp[gx][gy]="G"

  for row in temp:
    print(row)
  print()
  
