class WareHouseEnv:
  def __init__(self,grid,start,goal):
    self.grid = grid
    self.start = start
    self.goal = goal

    self.rows=len(grid)
    self.cols = len(grid[0])
    self.agent_pos = start

    self.actions = {
      0:(-1,0),
      1:(1,0),
      2:(0,-1),
      3:(0,1)
    }
    self._validate_inputs()
  
  def _validate_inputs(self):
    x,y = self.start
    gx,gy = self.goal

    if not(0<=x<self.rows and 0<=y<self.cols):
      raise ValueError("Start position out of Bounds")
    if not(0<=gx<self.rows and 0<=gy<self.cols):
      raise ValueError("Goal position out of Bounds")

    if self.grid[x][y] == -1:
      raise ValueError("Start Position cannot be Obstacle")
    if self.grid[gx][gy] == -1:
      raise ValueError("Goal Position cannot be Obstacle")
    
  def reset(self):
    self.agent_pos = self.start
    return self.agent_pos
  
  def step(self,action):
    x,y=self.agent_pos
    dx,dy = self.actions[action]

    new_x = x+dx
    new_y = y+dy

    if new_x < 0 or new_x >=self.rows or new_y<0 or new_y >= self.cols:
      return self.agent_pos, -1 ,False

    if self.grid[new_x][new_y]==-1:
      return self.agent_pos,-5,False
    
    self.agent_pos = (new_x,new_y)

    if self.agent_pos == self.goal:
      return self.agent_pos,10,True
    
    return self.agent_pos,-1,False