**Autonomous Car Parking System using Deep Reinforcement Learning**

The Autonomous Car Parking System is a Reinforcement Learning-based simulation in which an intelligent car agent learns to navigate a parking environment, avoid obstacles, and successfully park in a designated parking space.The project utilizes the **Deep Q-Network (DQN)** algorithm, enabling the agent to learn optimal parking strategies through continuous interaction with the environment. A Streamlit web application is also provided to demonstrate the trained agent in an interactive and user-friendly interface.

**Objectives**

1. Develop an autonomous parking simulation using Reinforcement Learning.
2. Train an intelligent agent to navigate safely in a parking environment.
3. Enable obstacle avoidance while reaching the designated parking space.
4. Visualize the parking process through simulation.
5. Demonstrate Deep Reinforcement Learning concepts using an interactive Streamlit application.

**Features**

- Deep Q-Network (DQN) based autonomous parking
- Intelligent obstacle avoidance
- Reward-based learning mechanism
- Parking environment simulation
- Interactive Streamlit dashboard
- Real-time parking visualization
- Trained agent demonstration
- Customizable parking environment

**Technologies Used**

- Python
- Reinforcement Learning
- Deep Q-Network (DQN)
- Stable-Baselines3
- OpenAI Gym
- NumPy
- Matplotlib
- Streamlit

**Reinforcement Learning Algorithm**

**Algorithm Used**

Deep Q-Network (DQN)- Deep Q-Network combines Q-Learning with Deep Neural Networks to estimate optimal action values for each state. The agent improves its parking strategy by continuously interacting with the environment, receiving rewards, and updating its policy to maximize cumulative rewards.

**Environment**

The parking environment consists of:

- Car Agent
- Target Parking Space
- Static Obstacles
- Parking Area
- Reward System
- Collision Detection

**Available Actions**

The autonomous agent can perform the following actions:

- Move Forward
- Move Backward
- Turn Left
- Turn Right
 
**Reward Function**

The agent learns using a reward-based system:

| Action | Reward |
|---------|--------|
| Successfully Park | +100 |
| Collision with Obstacle | -100 |
| Move Closer to Parking Spot | +5 |
| Normal Movement | -1 |

The reward function encourages the agent to reach the parking location efficiently while avoiding unnecessary movements and collisions.

**Training Parameters**

- Algorithm: Deep Q-Network (DQN)
- Training Library: Stable-Baselines3
- Training Environment: OpenAI Gym
- Total Training Steps: **50,000**

**Results**

After training, the autonomous agent successfully learned to:

- Navigate the parking environment
- Avoid obstacles
- Reach the target parking location
- Park successfully with an overall success rate of approximately **81%**

**Performance Summary**

| Metric | Value |
|---------|-------|
| Algorithm | DQN |
| Training Steps | 50,000 |
| Success Rate | 81% |
| Collisions | 4 |
| Parking Completed | Yes |

**Project Structure**

Autonomous-Car-Parking-RL/

├── app.py
├── environment/
│   └── parking_env.py
├── notebooks/
│   └── training.ipynb
├── models/
├── data/
├── videos/
│   └── parking_agent_demo.gif
├── requirements.txt
└── README.me

**Installation**

Clone the repository:

```bash
git clone https://github.com/sivani2602/Autonomous-Car-Parking-RL.git
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
python -m streamlit run app.py
```


**Future Improvements**

- Dynamic moving obstacles
- Sensor-based perception
- Multi-level parking environments
- Continuous action space using PPO or SAC
- Integration with computer vision techniques
- Real-world autonomous vehicle simulation


**Learning Outcomes**

This project helped in understanding:

- Reinforcement Learning fundamentals
- Deep Q-Network (DQN)
- Reward function design
- Environment modeling using OpenAI Gym
- Agent training using Stable-Baselines3
- Interactive deployment using Streamlit
