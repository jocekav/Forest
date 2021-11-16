import numpy as np
import pandas as pd
import trajectory_generation as traj

def print_dance(robots, final_time):
    dances = []
    dances_t = []
    # for robot in robots:
    #     dances.append(robot.dance)
    #     dances_t.append(robot.dance_t)
    [trajectory, velocity] = traj.generate_trajectory(dances, dances_t, final_time)

    for robot in range(self.NUM_ROBOTS):
        robot_loc = 7 * (robot)
        for i in range(7):
            trajectory[i + robot_loc, :] = trajectory[i + robot_loc, :] + self.INIT_POS[i]
            # trajectory[i + robot_loc, :] = trajectory[i + robot_loc, :]
            if i < 3:
                trajectory[i, :] = -1 * trajectory[i, :]

    final_position_db = np.transpose(trajectory)
    final_position = final_position_db[0::6, :]

    df = pd.DataFrame(final_position).astype(float)
    # df.to_csv("/home/forest/Desktop/xArm/Trajectories2/000027gameoflife.csv", header=False, index=False)


def birth():
    # joint 4 starts at 90
    # full alive position for joint 4 at 120
    # if self.curr_angle == 90:
    birth_move = np.array([0, -30, 0, 30, 0, 0, 0], dtype=object)
    birth_time = np.array([4, 4, 4, 4, 4, 4, 4], dtype=object)

    [trajectory, velocity] = traj.generate_trajectory(birth_move, birth_time, 0, 60)

    for robot in range(10):
        robot_loc = 7 * robot
        for i in range(7):
            trajectory[i + robot_loc, :] = trajectory[i + robot_loc, :] + self.INIT_POS[i]
            # trajectory[i + robot_loc, :] = trajectory[i + robot_loc, :]
            if i < 3:
                trajectory[i, :] = -1 * trajectory[i, :]

    final_position_db = np.transpose(trajectory)
    final_position = final_position_db[0::6, :]

    df = pd.DataFrame(final_position).astype(float)
    df.to_csv("/home/forest/Desktop/xArm/Trajectories2/000031birthgameoflife.csv", header=False, index=False)
    # else:
    #     birth_move = np.array([0, -50, 0, 60, 0, 0, 0], dtype=object)
    #     birth_time = np.array([4, 4, 4, 4, 4, 4, 4], dtype=object)
    #
    #     self.dance.append(birth_move)
    #     self.dance_t.append(birth_time)
    #
    #     self.curr_angle = self.curr_angle + 60


# def first_birth(self):
#     birth_move = np.array([0, -20, 0, 30, 0, 0, 0])
#     birth_time = np.array([4, 4, 4, 4, 4, 4, 4])
#
#     self.dance.append(birth_move)
#     self.dance_t.append(birth_time)

def death(self):
    # joint 4 starts at 90
    # full death position for joint 4 at 60
    if self.curr_angle == 90:
        death_move = np.array([0, 30, 0, -30, 0, 0, 0], dtype=object)
        death_time = np.array([4, 4, 4, 4, 4, 4, 4], dtype=object)

        self.dance.append(death_move)
        self.dance_t.append(death_time)

        self.curr_angle = self.curr_angle - 30
    elif self.curr_angle == 60:
        self.dying()
    elif self.curr_angle == 120:
        death_move = np.array([0, 50, 0, -60, 0, 0, 0], dtype=object)
        death_time = np.array([4, 4, 4, 4, 4, 4, 4], dtype=object)

        self.dance.append(death_move)
        self.dance_t.append(death_time)

        self.curr_angle = self.curr_angle - 60


# def first_death(self):
#     death_move = np.array([0, 20, 0, -30, 0, 0, 0])
#     death_time = np.array([4, 4, 4, 4, 4, 4, 4])
#
#     self.dance.append(death_move)
#     self.dance_t.append(death_time)

def living(self):
    living_move = np.array([0, 0, [-15, 15, 15, -15], 0, 0, 0, 0], dtype=object)
    living_time = np.array([4, 4, [1, 1, 1, 1], 4, 4, 4, 4], dtype=object)

    self.dance.append(living_move)
    self.dance_t.append(living_time)


def dying(self):
    dying_move = np.array([[20, -40, 20], 0, 0, 0, 0, 0, 0], dtype=object)
    dying_time = np.array([[1, 2, 1], 4, 4, 4, 4, 4, 4], dtype=object)

    self.dance.append(dying_move)
    self.dance_t.append(dying_time)

birth()