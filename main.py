import numpy as np
import time
from algorithms.q_learning import QLearningAgent
from env.grid_env import WareHouseEnv
from maps.map_builder import *
from utils import (print_grid,plot_rewards,plot_learning_curve)
from algorithms.a_star import a_star
def input_grid():
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
  return grid,start,goal

def run_astar(grid,start,goal):
  print("-----A* Algo-----\n")
  a_star_start=time.time()
  path,cost = a_star(grid,start,goal)
  a_start_end = time.time()
  astar_time = a_start_end-a_star_start
  if path:
    astar_length = len(path)
    print(f"Path found!\n Cost: {cost}")
    print("Path: ", path)
    print(f"Path Length : {astar_length}")
    print(f"Execution Time: {astar_time:.6f} sec")
    print("Grid with shortest path:")
    print_grid(grid,path=path,agent=start,goal=goal)
    return path,astar_length,astar_time
  else:
    print("No path found!")
  return None,0,astar_time

def train_rl_agent(env):
  agent = QLearningAgent(env)
  rl_train_start = time.time()
  history = agent.train(episodes=500,max_steps=100)
  rl_train_end = time.time()
  training_time = rl_train_end - rl_train_start
  print("\nTraining Complete!")
  print(f"Episodes Trained : {len(history)}")
  print(f"Training Time    : {training_time:.6f} sec")
  return agent,history,training_time

def run_rl_agent(env,agent,start,goal):
  state =env.reset()
  done = False
  steps=0
  max_steps=50
  rl_start=time.time()
  rl_path = [start]

  while not done and steps<max_steps:
    q_values = agent.get_q(state)
    action = int(np.argmax(q_values))
    state,reward,done = env.step(action)
    rl_path.append(state)
    print(f"Step {steps} | State: {state} | Reward: {reward}")
    print_grid(env.grid,agent=state,goal=env.goal)
    steps+=1
  rl_end = time.time()
  rl_time = rl_end - rl_start

  if done:
    print("GOAL REACHED!!")
    rl_length = len(rl_path)
    print(f"RL Path Length : {rl_length}")
    print(f"RL Execution Time : {rl_time:.6f} sec")
    print("\nRL Path:")
    print(rl_path)
    print("\nFinal RL Grid:")
    print_grid(env.grid, path=rl_path, agent=start, goal=goal)
  else:
    print("Agent did NOT reach Goal")
  return rl_path,len(rl_path),rl_time,done

def menu():
  print("1. Create Custom Map")
  print("2. Generate Easy Map")
  print("3. Generate Medium Map")
  print("4. Generate Hard Map")
  print("5. Run A*")
  print("6. Train RL Agent")
  print("7. Run RL Agent")
  print("8. Show Graphs")
  print("9. Compare Results")
  print("0. Exit")

def main():
    grid = None
    start = None
    goal = None
    env = None
    agent = None
    history = None
    astar_len = None
    rl_len = None
    while True:
        menu()
        choice = input("\nEnter choice: ")
        if choice == "1":
            grid, start, goal = input_grid()
            env = WareHouseEnv(grid, start, goal)
        elif choice == "2":
            rows = int(input("Rows: "))
            cols = int(input("Cols: "))
            grid = generate_difficulty_map(rows, cols, "easy")
            print_grid(grid)
            start, goal = get_start_goal(rows, cols, grid)
            env = WareHouseEnv(grid, start, goal)
        elif choice == "3":
            rows = int(input("Rows: "))
            cols = int(input("Cols: "))
            grid = generate_difficulty_map(rows, cols, "medium")
            print_grid(grid)
            start, goal = get_start_goal(rows, cols, grid)
            env = WareHouseEnv(grid, start, goal)
        elif choice == "4":
            rows = int(input("Rows: "))
            cols = int(input("Cols: "))
            grid = generate_difficulty_map(rows, cols, "hard")
            print_grid(grid)
            start, goal = get_start_goal(rows, cols, grid)
            env = WareHouseEnv(grid, start, goal)
        elif choice == "5":
            if env is None:
                print("Create map first!")
                continue
            astar_path, astar_len, astar_time = run_astar(grid, start, goal)
        elif choice == "6":
            if env is None:
                print("Create map first!")
                continue
            agent, history, training_time = train_rl_agent(env)
        elif choice == "7":
            if agent is None:
                print("Train RL Agent first!")
                continue
            rl_path, rl_len, rl_time, success = run_rl_agent(env, agent, start, goal)
        elif choice == "8":
            if history is None:
                print("Train RL first!")
                continue
            plot_rewards(history)
            plot_learning_curve(history)
        elif choice == "9":
            if astar_len is None or rl_len is None:
                print("Run both A* and RL first!")
                continue
            print("\n===== Comparison =====")
            print(f"A* Path Length : {astar_len}")
            print(f"RL Path Length : {rl_len}")
            efficiency = rl_len / astar_len
            print(f"Efficiency (RL/A*): {efficiency:.2f}")
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
  main()