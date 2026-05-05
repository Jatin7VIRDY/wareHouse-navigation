from algorithms.q_learning import QLearningAgent
from env.grid_env import WareHouseEnv
from maps.map_builder import *
from utils import print_grid
from algorithms.a_star import a_star
import random
import numpy as np

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

start,goal = get_start_goal(rows,cols,grid)

edit = input("Do u want to edit the grid? (Y/N)")
if edit.lower()=="y":
  grid = edit_grid(grid,start,goal)

print("Final Grid: ")
print_grid(grid)

env = WareHouseEnv(grid,start,goal)
print("-----A* Algo-----\n")
path,cost = a_star(grid,start,goal)
if path:
  print(f"Path found!\n Cost: {cost}")
  print("Path: ", path)

  print("Grid with shortest path:")
  print_grid(grid,path=path,agent=start,goal=goal)
else:
  print("No path found!")

agent = QLearningAgent(env)
history = agent.train(episodes=500,max_steps=100)

state =env.reset()
print_grid(env.grid,agent=state,goal=env.goal)

done = False
steps=0
max_steps=50

while not done and steps<max_steps:
  q_values = agent.get_q(state)
  action = int(np.argmax(q_values))
  state,reward,done = env.step(action)
  print(f"Step {steps} | State: {state} | Reward: {reward}")
  print_grid(env.grid,agent=state,goal=env.goal)

  steps+=1
if done:
  print("GOAL REACHED!!")
else:
  print("Agent did NOT reach Goal")