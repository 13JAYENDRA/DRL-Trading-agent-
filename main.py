import gym
import numpy as np
from gym import spaces
import pymysql

class StockTradingEnv(gym.Env):
    def __init__(self):
        super(StockTradingEnv, self).__init__()
        self.conn = pymysql.connect(host="localhost", user="root", password="Jayshree13", database="stock_trading")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT close_price FROM stock_data ORDER BY date ASC")
        self.stock_prices = np.array([row[0] for row in self.cursor.fetchall()])
        
        self.current_step = 0
        self.balance = 10000
        self.shares = 0
        self.action_space = spaces.Discrete(3)  # Buy, Sell, Hold
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(1,), dtype=np.float32)

    def step(self, action):
        current_price = self.stock_prices[self.current_step]
        
        if action == 0:  
            self.shares += 1
            self.balance -= current_price
        elif action == 1 and self.shares > 0:  
            self.shares -= 1
            self.balance += current_price
            
        reward = self.balance + (self.shares * current_price) - 10000
        self.current_step += 1
        done = self.current_step >= len(self.stock_prices) - 1

        return np.array([current_price]), reward, done, {}

    def reset(self):
        self.current_step = 0
        self.balance = 10000
        self.shares = 0
        return np.array([self.stock_prices[self.current_step]])
    print('done')

import gym
import numpy as np
from gym import spaces
import pymysql

class StockTradingEnv(gym.Env):
    def __init__(self):
        super(StockTradingEnv, self).__init__()
        self.conn = pymysql.connect(host="localhost", user="root", password="Jayshree13", database="stock_trading")
        self.cursor = self.conn.cursor()
        
        # Load data from MySQL
        self.cursor.execute("SELECT close_price FROM stock_data ORDER BY date ASC")
        self.stock_prices = np.array([row[0] for row in self.cursor.fetchall()])
        
        self.current_step = 0
        self.balance = 10000
        self.shares = 0
        
        # Define action & observation spaces
        self.action_space = spaces.Discrete(3)  # Buy, Sell, Hold
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(1,), dtype=np.float32)

    def step(self, action):
        current_price = self.stock_prices[self.current_step]
        
        if action == 0:  # Buy
            self.shares += 1
            self.balance -= current_price
        elif action == 1 and self.shares > 0:  # Sell
            self.shares -= 1
            self.balance += current_price
            
        reward = self.balance + (self.shares * current_price) - 10000
        self.current_step += 1
        done = self.current_step >= len(self.stock_prices) - 1

        return np.array([current_price]), reward, done, {}

    def reset(self):
        self.current_step = 0
        self.balance = 10000
        self.shares = 0
        return np.array([self.stock_prices[self.current_step]])

from stable_baselines3 import DQN
from stock_trading_env import StockTradingEnv

env = StockTradingEnv()
model = DQN("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)
model.save("stock_trading_dqn")
print('done 2 ')
# Load trained model
model = DQN.load("stock_trading_dqn")

obs = env.reset()
done = False

while not done:
    action, _states = model.predict(obs)
    obs, reward, done, _ = env.step(action)
    print(f"Action: {action}, Reward: {reward}")
