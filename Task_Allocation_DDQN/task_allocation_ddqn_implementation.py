### This is a project for my intorduction to project management class          ###
### There is a report/paper to go along with that can be provided upon request ###

import numpy as np
import random
from collections import deque
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import LeakyReLU, BatchNormalization
import csv

class Task_Assignment_DDQN_Implementation:
    def __init__(self, num_tasks, num_agents, random_seed=42):
        self.num_tasks = num_tasks
        self.num_agents = num_agents
        self.state_size = (self.num_agents * 4) + (self.num_tasks * 5)
        self.action_size = self.num_tasks * self.num_agents
        np.random.seed(random_seed) 
        self.reset()

    def reset(self):
        self.agents = np.zeros((self.num_agents, 4))  #[availability, skill level, workload, efficiency]
        for i in range(self.num_agents):
            self.agents[i, 0] = np.random.randint(1, 11)  #Availability
            self.agents[i, 1] = np.random.normal(loc=6, scale=2)  #Skill level
            self.agents[i, 2] = np.random.randint(1, 11)  #Workload
            self.agents[i, 3] = np.random.normal(loc=5, scale=2)  #Efficiency

        self.tasks = np.zeros((self.num_tasks, 5))  #[type, duration, complexity, priority, deadline]
        for j in range(self.num_tasks):
            self.tasks[j, 1] = np.random.randint(1, 11)  #Duration
            self.tasks[j, 2] = np.random.normal(loc=5, scale=2)  #Complexity
            self.tasks[j, 3] = np.random.normal(loc=6, scale=3)  #Priority
            self.tasks[j, 4] = np.random.randint(1, 11)  #Deadline

        self.tasks = np.clip(self.tasks, 1, 10)
        self.agents = np.clip(self.agents, 1, 10)
        self.assigned_tasks = np.zeros(self.num_tasks, dtype=bool)
        self.total_reward = 0
        return self.get_model_state()

    def get_model_state(self):
        #Normalize, flatten, and concatenate
        normalized_agents = self.agents / 10.0
        normalized_tasks = self.tasks / 10.0
        state = np.concatenate([normalized_agents.flatten(), normalized_tasks.flatten()])
        return state

    def calculate_model_reward(self, agent, task):
        """ TO-DO: This reward function may be a bit to complicated for initial testing.
                Due to the nature of the random variables, the reward function may not be 
                100% viable. The reward function may need to be modified in the future as 
                well as possibly normalizing the random values (or generate a set of fixed
                values for more concrete testing).
        """
        reward = 0

        availability, skill_level, workload, efficiency = agent[0], agent[1], agent[2], agent[3]
        duration, complexity, priority, deadline = task[1], task[2], task[3], task[4]


        if deadline <= 3 and complexity > 6:
            if skill_level >= 7:
                if efficiency >= 6:
                    reward += 4
                else:
                    reward += 3
            else:
                reward -= 2
        elif deadline <= 3:
            if efficiency >= 6:
                reward += 2
            else:
                reward -= 1
        
        if not(deadline <= 3 and complexity > 6):
            if complexity > 5 and skill_level > 5:
                reward += 2 
            elif complexity <= 5 and skill_level <= 5:
                reward += 1 
            else:
                reward -= 1 
            
        if priority >= 7 and skill_level >= 6:
            reward += 2
        elif priority > 7 and skill_level < 5:
            reward -= 2

        return reward

    def calculate_max_reward(self):
        #Try to calculate the maximum reward for debugging purposes
        max_reward = 0
        for task_id in range(self.num_tasks):
            best_task_reward = float('-inf')
            for agent_id in range(self.num_agents):
                agent = self.agents[agent_id]
                task = self.tasks[task_id]
                reward = self.calculate_model_reward(agent, task)
                if reward > best_task_reward:
                    best_task_reward = reward
            max_reward += best_task_reward
        return max_reward
    
    def step(self, action):
        task_id = action // self.num_agents
        agent_id = action % self.num_agents

        done = False
        reward = 0

        if self.assigned_tasks[task_id]:
            reward = 0
        else:
            self.assigned_tasks[task_id] = True
            agent = self.agents[agent_id]
            task = self.tasks[task_id]
            reward = self.calculate_model_reward(agent, task)
            if np.all(self.assigned_tasks):
                done = True

        self.total_reward += reward
        next_state = self.get_model_state()

        return next_state, reward, done

class DDQN_Model:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size

        #Hyperparameters
        self.memory = deque(maxlen=150000)
        self.gamma = 0.99
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.999
        self.learning_rate = 0.001
        self.batch_size = 256
        self.target_update_freq = 20  


        self.model = self._build_model()
        self.target_model = self._build_model()
        self.update_target_model()

        self.losses = [] 

    def _build_model(self):
        model = Sequential()
        model.add(Dense(256, input_dim=self.state_size, activation=None))
        model.add(LeakyReLU(alpha=0.1))
        model.add(BatchNormalization())
        model.add(Dense(256, activation=None))
        model.add(LeakyReLU(alpha=0.1))
        model.add(BatchNormalization())
        model.add(Dense(128, activation=None))
        model.add(LeakyReLU(alpha=0.1))
        model.add(BatchNormalization())
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(learning_rate=self.learning_rate))
        return model

    def update_target_model(self):
        self.target_model.set_weights(self.model.get_weights())

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        q_values = self.model.predict(state, verbose=0)
        return np.argmax(q_values[0])

    def replay(self):
        if len(self.memory) < self.batch_size:
            return

        minibatch = random.sample(self.memory, self.batch_size)

        for state, action, reward, next_state, done in minibatch:
            target = self.model.predict(state, verbose=0)[0]

            if done:
                target[action] = reward
            else:
                best_action = np.argmax(self.model.predict(next_state, verbose=0)[0])
                target_q = self.target_model.predict(next_state, verbose=0)[0][best_action]
                target[action] = reward + self.gamma * target_q

            history = self.model.fit(state, target.reshape(-1, self.action_size), epochs=1, verbose=0)
            loss = history.history['loss'][0] 
            self.losses.append(loss)

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def save(self, name):
        self.model.save_weights(name)

    def load(self, name):
        self.model.load_weights(name)

def sliding_window(values, window_size=100):
    if len(values) < window_size:
        return np.mean(values)
    return np.convolve(values, np.ones(window_size), 'valid') / window_size

if __name__ == "__main__":
    NUM_TASKS = 25
    NUM_AGENTS = 10
    EPISODES = 5000
    total_rewards = []

    env = Task_Assignment_DDQN_Implementation(NUM_TASKS, NUM_AGENTS, random_seed=42)
    state_size = env.state_size
    action_size = env.action_size
    agent = DDQN_Model(state_size, action_size)

    with open('training_log.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Episode', 'Total Reward', 'Max Reward', 'Reward Ratio', 'Epsilon'])

        for e in range(1, EPISODES + 1):
            state = env.reset()
            state = np.reshape(state, [1, state_size])
            total_reward = 0
            done = False

            while not done:
                action = agent.act(state)
                next_state, reward, done = env.step(action)
                next_state = np.reshape(next_state, [1, state_size])
                agent.remember(state, action, reward, next_state, done)
                state = next_state
                total_reward += reward

            agent.replay()

            if e % agent.target_update_freq == 0:
                agent.update_target_model()

            max_reward = env.calculate_max_reward()
            reward_ratio = total_reward / max_reward if max_reward > 0 else 0
            total_rewards.append(total_reward)

            print(f"Episode: {e}/{EPISODES}, Total Reward: {total_reward:.2f}, Max Reward: {max_reward:.2f}, Reward Ratio: {reward_ratio:.2f}, Epsilon: {agent.epsilon:.2f}")
            writer.writerow([e, total_reward, max_reward, reward_ratio, agent.epsilon])

    agent.save("ddqn.h5")
