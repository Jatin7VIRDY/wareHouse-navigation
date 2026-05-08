import os
import matplotlib.pyplot as plt

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
  
def plot_rewards(history):
  os.makedirs("plots",exist_ok =True)
  plt.figure(figsize=(10,5))
  plt.plot(history)
  plt.xlabel("Episodes")
  plt.ylabel("Reward")
  plt.title("Reward vs Episode")
  plt.grid(True)
  plt.savefig("plots/reward_vs_episode.png")
  plt.show()

def plot_learning_curve(history):
  window_size=20
  moving_avg=[]
  for i in range(len(history)):
    start_idx = max(0,i-window_size)
    avg = sum(history[start_idx:i+1])/(i-start_idx+1)
    moving_avg.append(avg)

  plt.figure(figsize=(10,5))
  plt.plot(moving_avg)
  plt.xlabel("Episodes")
  plt.ylabel("Average Reward")
  plt.title("Learning Curve")
  plt.grid(True)
  plt.savefig("plots/learning_curve.png")
  plt.show()