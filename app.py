import streamlit as st
import os


st.set_page_config(
    page_title="Autonomous Parking RL",
    layout="wide"
)


# Title
st.title("Autonomous Car Parking System using Reinforcement Learning")


st.markdown("""
## Project Overview

This project uses Deep Q-Learning (DQN) to train an autonomous vehicle agent.

The agent learns by interacting with a simulated parking environment.

Objective:

- Move the car from the initial position
- Avoid obstacles
- Reach the target parking location
- Maximize the reward
""")


# Pipeline
st.header("Reinforcement Learning Pipeline")


st.code("""
Environment
      |
      v
Agent observes current state
(car position, target position, direction)
      |
      v
DQN selects an action
(move up, down, left, right)
      |
      v
Environment gives reward
(success / collision)
      |
      v
Agent improves decision making
""")


# Metrics
st.header("Model Performance")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Algorithm",
        "DQN"
    )


with col2:
    st.metric(
        "Success Rate",
        "81%"
    )


with col3:
    st.metric(
        "Training Steps",
        "50K"
    )


# Animation
st.header("Autonomous Parking Simulation")


gif_path = "videos/parking_agent_demo.gif"


if os.path.exists(gif_path):

    with open(gif_path, "rb") as file:
        gif_bytes = file.read()

    st.image(
        gif_bytes,
        caption="DQN agent navigating obstacles and reaching parking target",
        use_container_width=True
    )

else:

    st.error(
        "GIF file not found. Check videos/parking_agent_demo.gif"
    )



# Explanation
st.header("Simulation Explanation")


st.markdown("""
### Autonomous Car Agent

The moving object represents the trained parking agent.

At every step, the agent observes the environment and chooses the next action.


### Obstacles

The blocks represent obstacles inside the parking area.

The agent receives a negative reward when it collides.


### Target Position

The target represents the final parking spot.

The agent receives a positive reward after successfully reaching it.


### DQN Learning Process

The model learns through:

State → Action → Reward → Updated Policy


State contains:

- Current car position
- Target position
- Direction


Possible actions:

- Move forward
- Turn left
- Turn right
- Reverse


After training, the agent learns an efficient path to park safely.
""")


st.success(
    "Reinforcement Learning agent successfully learned autonomous parking behaviour."
)