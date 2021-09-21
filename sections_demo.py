from random import randint
import numpy as np
import trajectory_generation as traj
import pandas as pd
import csv

nod = np.array([0,[-2, 2], 0, [10, -10], 0, [70, -70], 0])
nod_t = np.array([4, [2, 2], 4, [2, 2], 4, [2, 2], 4])

swivle = np.array([[45, -45], 0, 0, 0, 0, 0, 0])
swivle_t = np.array([[2, 2], 4, 4, 4, 4, 4, 4])

robot_dance = []
robot_t = []

duration = [30, 40, 15]
bpm = [60, 90, 50]

for i in range(len(duration)):
    num_beats = bpm[i]/60 * duration[i]
    even_beats = int(num_beats/4)
    left_over = num_beats % 4
    if i % 2 == 0:
        for j in range(even_beats):
            robot_dance.append(nod)
            robot_t.append(nod_t)
    else:
        for j in range(even_beats):
            robot_dance.append(swivle)
            robot_t.append(swivle_t)

dances = [robot_dance, robot_dance, robot_dance, robot_dance, robot_dance, robot_dance, robot_dance, robot_dance, robot_dance, robot_dance]
dances_t = [robot_t, robot_t, robot_t, robot_t, robot_t, robot_t, robot_t, robot_t, robot_t, robot_t]
print(dances)

[trajectory,velocity] = traj.generate_trajectory(dances, dances_t, 1)
INIT_POS = np.array([0, 0, 0, 90, 0, 0, 0])
for robot in range(10):
    robot_loc = 7 * (robot)
    for i in range(7):
        trajectory[i + robot_loc, :] = trajectory[i + robot_loc, :] + INIT_POS[i]
        # trajectory[i + robot_loc, :] = trajectory[i + robot_loc, :]
        if i < 3:
            trajectory[i, :] = -1 * trajectory[i, :]

final_position_db = np.transpose(trajectory)
final_position = final_position_db[0::6, :]

df = pd.DataFrame(final_position).astype(float)
#df.to_csv("/home/forest/Desktop/xArm/Trajectories2/000029sectionsdemo.csv", header=False, index=False)
df.to_csv("000029sectionsdemo.csv", header=False, index=False)

# final_trajectory = velocity
# final_trajectory = np.transpose(final_trajectory)

# pd.DataFrame(final_trajectory).to_csv("dance_groove_vel_1.csv")