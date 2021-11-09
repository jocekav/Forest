from trajectory_generation import NUM_ROBOTS
import numpy as np
import csv
import pandas as pd

import breath, trajectory_generation


INIT_POS = np.array([0, 0, 0, 90, 0, 0, 0])
MAX_VEl = np.zeros(7) + 180
MAX_ACC = np.zeros(7) + 1000
NUM_ROBOTS = 10

phases = 5
joint = 0

BPM = 90
TIME = 60/BPM
TIME_STEP = 0.001
a = 2

nod = np.array([0,[-2, 2], 0, [10, -10], 0, [70, -70], 0])
nod_t = np.array([4, [2, 2], 4, [2, 2], 4, [2, 2], 4])
grooved = 70
grooveh = 10
len= 10
j1 = np.zeros(len) + grooved
j4 = np.zeros(2 * len) + grooveh
j6 = np.zeros(2 * len) + 30

for j in range(len):
    j1[j] = ((-1)** (j + 1)) * j1[j]


for j in range(len * 2):
    j4[j] = ((-1)** (j + 1)) * j4[j]
    j6[j] = ((-1)** j) * j6[j]

j1_t = np.zeros(len) + 2
j4_t = np.zeros(2 * len) + 1
groove = np.array([j1, 0, 0, j4, 0, j6, 0])
groove_t = np.array([j1_t, 0, 0, j4_t, 0, j4_t, 0])

routine1 = [nod, nod, nod, nod, nod]
routine1_t = [nod_t, nod_t, nod_t, nod_t, nod_t]

routine2 = [breath.breath(4), nod, nod, nod, nod]
routine2_t = [breath.breath_t(4), nod_t, nod_t, nod_t, nod_t]

routine3 = [breath.breath(8), nod, nod, nod]
routine3_t = [breath.breath_t(8), nod_t, nod_t, nod_t]

routine4 = [breath.breath(12), nod, nod]
routine4_t = [breath.breath_t(12), nod_t, nod_t]

routine5 = [breath.breath(4), nod, nod, nod, nod]
routine5_t = [breath.breath_t(4), nod_t, nod_t, nod_t, nod_t]

routine6 = [breath.breath(8), nod, nod, nod]
routine6_t = [breath.breath_t(8), nod_t, nod_t, nod_t]

routine7 = [breath.breath(12), nod, nod]
routine7_t = [breath.breath_t(12), nod_t, nod_t]

routine8 = [breath.breath(8), nod, nod, nod]
routine8_t = [breath.breath_t(8), nod_t, nod_t, nod_t]

routine9 = [breath.breath(12), nod, nod]
routine9_t = [breath.breath_t(12), nod_t, nod_t]

routine10 = [breath.breath(16), nod]
routine10_t = [breath.breath_t(16), nod_t]

dances = [routine1, routine2, routine3, routine4, routine5, routine6, routine7, routine8, routine9, routine10]

dances_t = [routine1_t, routine2_t, routine3_t, routine4_t, routine5_t, routine6_t, routine7_t, routine8_t, routine9_t, routine10_t]


[trajectory,velocity] = trajectory_generation.generate_trajectory(dances, dances_t, 1)


for robot in range(NUM_ROBOTS):
    robot_loc = 7 * (robot)
    for i in range(7):
        trajectory[i + robot_loc, :] = trajectory[i + robot_loc, :] + INIT_POS[i]
        if i < 3:
            trajectory[i, :] = -1 * trajectory[i, :]

final_position_db = np.transpose(trajectory)
final_position = final_position_db[0::6, :]

pd.DataFrame(final_position).to_csv("dance_pattern_pos.csv")

final_trajectory = velocity
final_trajectory = np.transpose(final_trajectory)

pd.DataFrame(final_trajectory).to_csv("dance_groove_vel.csv")




