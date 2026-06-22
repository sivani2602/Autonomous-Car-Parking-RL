import gymnasium as gym
from gymnasium import spaces
import numpy as np


class ParkingEnv(gym.Env):

    def __init__(self):
        super().__init__()

        self.action_space = spaces.Discrete(4)

        # car_x, car_y, angle, target_x, target_y
        self.observation_space = spaces.Box(
            low=0,
            high=10,
            shape=(5,),
            dtype=np.float32
        )

        self.max_steps = 200

        self.obstacles = [
            (4, 4),
            (4, 5),
            (5, 4),
            (6, 6)
        ]

    def _get_state(self):

        return np.array([
            self.car_x,
            self.car_y,
            self.angle,
            self.target_x,
            self.target_y
        ], dtype=np.float32)

    def reset(self, seed=None, options=None):

        super().reset(seed=seed)

        self.car_x = np.random.randint(0, 3)
        self.car_y = np.random.randint(0, 3)

        self.target_x = np.random.randint(7, 10)
        self.target_y = np.random.randint(7, 10)

        self.angle = np.random.randint(0, 4)

        self.steps = 0

        return self._get_state(), {}

    def step(self, action):

        old_distance = np.sqrt(
            (self.car_x - self.target_x) ** 2 +
            (self.car_y - self.target_y) ** 2
        )

        # Turn Left
        if action == 1:
            self.angle = (self.angle - 1) % 4

        # Turn Right
        elif action == 2:
            self.angle = (self.angle + 1) % 4

        # Forward
        elif action == 0:

            if self.angle == 0:
                self.car_y += 1

            elif self.angle == 1:
                self.car_x += 1

            elif self.angle == 2:
                self.car_y -= 1

            elif self.angle == 3:
                self.car_x -= 1

        # Reverse
        elif action == 3:

            if self.angle == 0:
                self.car_y -= 1

            elif self.angle == 1:
                self.car_x -= 1

            elif self.angle == 2:
                self.car_y += 1

            elif self.angle == 3:
                self.car_x += 1

        self.car_x = np.clip(self.car_x, 0, 10)
        self.car_y = np.clip(self.car_y, 0, 10)

        self.steps += 1

        if (self.car_x, self.car_y) in self.obstacles:
            return self._get_state(), -1000, True, False, {}

        new_distance = np.sqrt(
            (self.car_x - self.target_x) ** 2 +
            (self.car_y - self.target_y) ** 2
        )

        reward = (old_distance - new_distance) * 10

        reward -= 1

        terminated = False

        if new_distance < 1:
            reward = 1000
            terminated = True

        truncated = self.steps >= self.max_steps

        return self._get_state(), reward, terminated, truncated, {}

    def render(self):

        directions = {
            0: "North",
            1: "East",
            2: "South",
            3: "West"
        }

        print(
            f"Car=({self.car_x},{self.car_y}) "
            f"Direction={directions[self.angle]} "
            f"Target=({self.target_x},{self.target_y})"
        )