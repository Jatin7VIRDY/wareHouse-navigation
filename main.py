from env.grid_env import WareHouseEnv
from maps.map_builder import *
from utils import print_grid
import random

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of cols: "))

print("\nChoose Option: ")
print("1. Create Grid Manually")
print("2. Generate Random grid")

choice=int(input("Enter a choice: "))

if choice==1:
  grid = grid_user_input(rows,cols)
else:
  prob = float(input("Enter obstacle probability(0-1): "))
  grid = generate_random_grid(rows,cols,prob)

print("Initial Grid: ")
print_grid(grid)

start,goal = get_start_goal(rows,cols)

edit = input("Do u want to edit the grid? (Y/N)")
if edit.lower()=="y":
  grid = edit_grid(grid,start,goal)

print("Final Grid: ")
print_grid(grid)

env = WareHouseEnv(grid,start,goal)
state = env.reset()

print("Simulation Start: ")
print_grid(env.grid,env.agent_pos,env.goal)


for _ in range(20):
  action = random.choice([0,1,2,3])
  state,reward,done = env.step(action)
  print(f"State: {state}, Reward: {reward}")
  print_grid(env.grid,env.agent_pos,env.goal)
  if done:
    print("GOAL REACHED!!")
    break