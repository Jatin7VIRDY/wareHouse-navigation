def print_grid(grid,path=None,agent=None,goal=None):
  temp = [row[:] for row in grid]
  if path:
    for x,y in path:
      if(x,y) != agent  and (x,y)!=goal:
        temp[x][y]="*"
  
  if agent:
    x,y =agent
    temp[x][y]="A"

  if goal:
    gx,gy=goal
    temp[gx][gy] = "G"

  for row in temp:
    print(row)
  print()
  
