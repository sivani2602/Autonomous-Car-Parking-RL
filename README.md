\*Autonomous Car Parking System\*



A Reinforcement Learning based autonomous parking system where a car agent learns to navigate a parking environment, avoid obstacles, and reach the target parking spot.



\## Project Demo



!\[Autonomous Parking Demo](videos/parking\_agent\_demo.gif)





\## About The Project



This project implements an autonomous car parking simulation using Deep Q-Learning (DQN).



The car learns through interactions with the environment by trying different actions, receiving rewards, and improving its movement strategy.



The main goal is to train an agent that can:



\- Move through the parking area

\- Avoid obstacles

\- Reach the target position

\- Successfully complete parking





\## Features



\- Autonomous car movement

\- Obstacle avoidance

\- Reinforcement learning based decision making

\- Reward based training

\- Parking simulation visualization

\- Streamlit dashboard for demonstration





\## Technologies Used



\- Python

\- Reinforcement Learning

\- Deep Q-Learning (DQN)

\- Stable-Baselines3

\- OpenAI Gym

\- NumPy

\- Matplotlib

\- Streamlit





\## Environment



The simulation contains:



\- Car starting position

\- Target parking location

\- Obstacles

\- Movement actions

\- Reward system





\## Actions



The car agent can perform:



\- Move forward

\- Move backward

\- Turn left

\- Turn right





\## Model Details



Algorithm Used:



Deep Q-Network (DQN)



The model learns better parking behaviour by improving its decisions based on previous experiences.





\## Results



Algorithm: DQN  

Training Steps: 50,000  

Success Rate: 81%  

Collisions: 4  

Parking Completed: Yes





\## Project Structure



Autonomous-Car-Parking-RL



├── app.py  

├── environment  

│   └── parking\_env.py  

├── notebooks  

│   └── training.ipynb  

├── videos  

│   └── parking\_agent\_demo.gif  

├── models  

└── data  





\## Run The Project



Install dependencies:



pip install -r requirements.txt





Run the dashboard:



python -m streamlit run app.py





\## Future Improvements



\- Add sensor-based inputs

\- Improve obstacle detection

\- Train in larger environments

\- Extend towards real-world autonomous vehicles





\## Author



Sivani Mohapatra



Computer Science Engineering  

Artificial Intelligence and Machine Learning

