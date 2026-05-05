import random
import numpy as np

class QLearningAgent:
  def __init__(self,env,alpha=0.1,gamma=0.9,epsilon=1.0,epsilon_decay =0.995,epsilon_min=0.01):
    self.env = env
    self.alpha = alpha 
    self.gamma =gamma
    self.epsilon = epsilon
    self.epsilon_decay = epsilon_decay
    self.epsilon_min = epsilon_min

    self.actions = list(env.actions.keys())
    self.q_table={}

  def get_q(self,state):
    if state not in self.q_table:
      self.q_table[state] = np.zeros(len(self.actions))
    return self.q_table[state]
  
  def choose_action(self,state):
    if random.random()<self.epsilon: #Exploration
      return random.choice(self.actions)
    return int(np.argmax(self.get_q(state)))  #Explotation

  def train(self,episodes=500,max_steps=100):
    history=[]
    for ep in range(episodes):
      state = self.env.reset()
      total_reward=0
      for _ in range(max_steps):
        action = self.choose_action(state)
        next_state,reward,done = self.env.step(action)

        old_q = self.get_q(state)[action]
        if done:
          next_max=0
        else:
          next_max = np.max(self.get_q(next_state))

        new_q = old_q + self.alpha*(reward + self.gamma*next_max - old_q)

        self.q_table[state][action] = new_q
        state= next_state
        total_reward+=reward

        if done:
          break
      self.epsilon = max(self.epsilon_min, self.epsilon*self.epsilon_decay)
      history.append(total_reward)

      if ep%50==0:
        print(f"Episode {ep} | Reward: {total_reward} | Epsilon: {self.epsilon:.3f}")
    return history
        
  