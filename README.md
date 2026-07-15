**Treasure Hunt using Reinforcement Learning (Q-Learning)**

Treasure Hunt is a Reinforcement Learning project in which an intelligent agent learns to navigate a grid environment to reach a hidden treasure while avoiding obstacles. The project uses the **Q-Learning algorithm**, allowing the agent to learn the optimal path through trial-and-error interactions with the environment. An interactive Streamlit application enables users to customize the environment, train the agent, and visualize its learning process in real time.

**Objectives**

1. Implement the Q-Learning algorithm.
2. Create an interactive Treasure Hunt environment.
3. Train an intelligent agent to find the shortest path.
4. Visualize agent movement.
5. Demonstrate Reinforcement Learning concepts.

**Features**

- Interactive Streamlit Dashboard
- Q-Learning Intelligent Agent
- Custom Grid Size
- Custom Start Position
- Custom Treasure Position
- User-defined Obstacles
- Adjustable Learning Rate (α)
- Adjustable Discount Factor (γ)
- Configurable Exploration Rate (ε)
- Real-time Agent Animation
- Treasure Found Notification
- Training Statistics

**Technologies Used**

- Python
- NumPy
- Matplotlib
- Streamlit
- Reinforcement Learning (Q-Learning)

**Reinforcement Learning Algorithm**

**Algorithm Used:**

Q-Learning : Q-Learning is a model-free Reinforcement Learning algorithm that enables an agent to learn the best action for every state by maximizing cumulative rewards through repeated interactions with the environment.

**Environment**

The environment consists of:

- Grid World
- Agent
- Treasure
- Obstacles
- Reward System

**Reward Function**

| Action | Reward |
|---------|--------|
| Reach Treasure | +100 |
| Hit Obstacle | -100 |
| Valid Move | -1 |

**Q-Learning Parameters**

- Learning Rate (α)
- Discount Factor (γ)
- Exploration Rate (ε)
- Number of Episodes
- Maximum Steps per Episode

**Workflow**

1. Initialize Environment
2. Create Q-Table
3. Train Agent using Q-Learning
4. Update Q-Values
5. Learn Optimal Path
6. Test Trained Agent
7. Visualize Agent Movement

**Project Structure**

Treasure-Hunt/

├── app.py

├── Treasure_Hunt.ipynb

├── README.md


**Results**

The trained Q-Learning agent successfully learns the optimal path to the treasure while avoiding obstacles. The Streamlit interface allows users to observe the learning process and interactively modify the environment to test different scenarios.

**Future Improvements**

- Multiple Treasure Locations
- Dynamic Obstacles
- Larger Grid Environments
- Deep Q-Network (DQN) Implementation
- Multi-Agent Treasure Hunt
