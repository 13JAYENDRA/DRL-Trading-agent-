import gym
from gym import spaces
import numpy as np

class StockTradingEnv(gym.Env):  # Ensure it inherits from gym.Env
    metadata = {"render.modes": ["human"]}

    def __init__(self):
        super(StockTradingEnv, self).__init__()

        # Define action and observation space
        self.action_space = spaces.Discrete(3)  # Example: Buy, Hold, Sell
        self.observation_space = spaces.Box(low=0, high=1, shape=(10,), dtype=np.float32)  

    def step(self, action):
        """
        Executes a step in the environment
        """
        print(f"Performing action: {action}")
        next_state = np.random.rand(10)  # Example: Dummy next state
        reward = np.random.rand()  # Example: Dummy reward
        done = False  # Example: Define termination condition
        info = {}  # Additional information
        return next_state, reward, done, info

    def reset(self):
        """
        Resets the environment to an initial state and returns the initial observation.
        """
        return np.random.rand(10)  # Example: Dummy initial state

    def render(self, mode="human"):
        """
        Renders the environment (not needed for training but useful for debugging).
        """
        print("Rendering environment state...")

    def close(self):
        """
        Closes the environment and releases any resources.
        """
        print("Closing environment...")
