import heapq

def heuristics(a,b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(node,grid):
  rows = len(grid)
  cols = len(grid[0])

  directions = [(0,1),(0,-1),(1,0),(-1,0)]

  neighbors =[]

  for dx,dy in directions:
    nx = node[0]+ dx
    ny = node[1]+ dy

    if 0<=nx <rows and 0<=ny<cols:
      if grid[nx][ny]!=-1:
        neighbors.append((nx,ny))
  
  return neighbors

def construct_path(came_from,current):
  path = [current]
  while current in came_from:
    current = came_from[current]
    path.append(current)
  path.reverse()
  return path

def a_star(grid,start,goal):
  open_set=[]
  heapq.heappush(open_set,(0,start))
  came_from={}
  g_score = {start:0}
  f_score = {start : heuristics(start,goal)}

  while open_set:
    _,current = heapq.heappop(open_set)
    if current == goal:
      path = construct_path(came_from,current)
      return path,len(path)-1
    for neighbor in get_neighbors(current,grid):
      tentative_g = g_score[current]+1
      if neighbor not in g_score or tentative_g < g_score[neighbor]:
        came_from[neighbor] = current
        g_score[neighbor] = tentative_g
        f_score[neighbor] = tentative_g + heuristics(neighbor,goal)

        heapq.heappush(open_set,(f_score[neighbor],neighbor))
  return None,float('inf')

