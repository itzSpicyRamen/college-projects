import pandas as pd
import matplotlib.pyplot as plt

# Load the training log
df = pd.read_csv('training_log.csv')

#Total reward per episode
plt.figure(figsize=(12, 6))
plt.plot(df['Episode'], df['Total Reward'], label='Total Reward')
plt.xlabel('Episode')
plt.ylabel('Total Reward')
plt.title('Training Progress')
plt.legend()
plt.grid(True)
plt.show()

#Reward ratio
plt.figure(figsize=(12, 6))
plt.plot(df['Episode'], df['Reward Ratio'], label='Reward Ratio')
plt.xlabel('Episode')
plt.ylabel('Reward Ratio')
plt.title('Training Progress')
plt.legend()
plt.grid(True)
plt.show()

#Epsilon decay
plt.figure(figsize=(12, 6))
plt.plot(df['Episode'], df['Epsilon'], label='Epsilon', color='orange')
plt.xlabel('Episode')
plt.ylabel('Epsilon')
plt.title('Epsilon Decay Over Time')
plt.legend()
plt.grid(True)
plt.show()

