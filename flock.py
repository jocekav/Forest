from ast import Num
from random import randint
import numpy as np
import math
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

import trajectory_generation as traj


class Robot:
    def __init__(self, num, x_pos, y_pos):
        self.num = num
        self.dance = []
        self.dance_t = []
        self.joint_0 = randint(0, 360)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.joint_0_moves = [self.joint_0]

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def get_neighbors(self):
        return self.neighbors

    def get_num(self):
        return self.num

    def get_joint_0(self):
        return self.joint_0
    
    def get_joint_0_moves(self):
        return self.joint_0_moves

    # calculates a steering force toward a target
    def steer(self, target_x, target_y):
        desired_x = target_x - self.x_pos
        desired_y = target_y - self.y_pos
        if desired_y == 0:
            if desired_x == 0:
                direction = 0
            elif desired_x < 0:
                direction = 90
            elif desired_x > 0:
                direction = 270
        else:
            direction = math.degrees(math.atan((desired_x / desired_y)))
        # print(direction)
        return direction

    # for all neighbors calculate the average joint_0 angle
    def align(self):
        sum = 0
        num_neighbors = 0
        for neighbor in self.neighbors:
            sum += neighbor.joint_0
            num_neighbors += 1

        sum = sum / num_neighbors
        # steer = sum - self.joint_0
        steer = sum
        return steer

    # find the center of neighbors and steer toward them
    def cohesion(self):
        x_sum = 0
        y_sum = 0
        num_neighbors = 0
        for neighbor in self.neighbors:
            x_sum += neighbor.x_pos
            y_sum += neighbor.y_pos
            num_neighbors += 1
        x_sum = x_sum / num_neighbors
        y_sum = y_sum / num_neighbors
        return self.steer(x_sum, y_sum)

    def flock(self):
        align = self.align()
        # new_angle = (align + self.joint_0) / 2
        new_angle = ((align * 0.5) + self.joint_0) / 2
        self.joint_0_moves.append(self.joint_0 - new_angle)
        self.joint_0 = new_angle
        return new_angle
        coh = self.cohesion()

        # apply weights
        align = align * 1.2
        coh = coh * .8

        # find average angle to move
        new_angle = (align + coh) / 2
        return new_angle

    def define_dance(self):
        for i in range(len(self.joint_0_moves)):
            new_step = [0, 0, 0, 0, self.joint_0_moves[i], 0, 0]
            self.dance.append(new_step)
            new_time = [5, 5, 5, 5, 5, 5, 5]
            self.dance_t.append(new_time)


class Flock:

    def __init__(self, robots):
        self.robots = robots

    def run(self):
        for i in range(10):
            for robot in self.robots:
                print('Robot: ' + str(robot.get_num()) +
                      ' Angle: ' + str(robot.flock()))


def init_robots():
    # ROBOT_1 = Robot(0, 0, 0)
    # ROBOT_2 = Robot(1, 1, 0)
    # ROBOT_3 = Robot(2, 2, 0)
    # ROBOT_4 = Robot(3, 0, 1)
    # ROBOT_5 = Robot(4, 1, 1)
    # ROBOT_6 = Robot(5, 2, 1)
    # ROBOT_7 = Robot(6, 0, 2)
    # ROBOT_8 = Robot(7, 1, 2)
    # ROBOT_9 = Robot(8, 2, 2)

    ROBOT_1 = Robot(0, 1, 1)
    ROBOT_2 = Robot(1, 2, 1)
    ROBOT_3 = Robot(2, 3, 1)
    ROBOT_4 = Robot(3, 1, 2)
    ROBOT_5 = Robot(4, 2, 2)
    ROBOT_6 = Robot(5, 3, 2)
    ROBOT_7 = Robot(6, 1, 3)
    ROBOT_8 = Robot(7, 2, 3)
    ROBOT_9 = Robot(8, 3, 3)
    # ROBOT_10 = Robot(9)

    robots = [ROBOT_1, ROBOT_2, ROBOT_3, ROBOT_4,
              ROBOT_5, ROBOT_6, ROBOT_7, ROBOT_8, ROBOT_9]

    ROBOT_1.set_neighbors([ROBOT_2, ROBOT_4])
    ROBOT_2.set_neighbors([ROBOT_1, ROBOT_3, ROBOT_5])
    ROBOT_3.set_neighbors([ROBOT_2, ROBOT_6])
    ROBOT_4.set_neighbors([ROBOT_1, ROBOT_5, ROBOT_7])
    ROBOT_5.set_neighbors([ROBOT_2, ROBOT_4, ROBOT_6, ROBOT_8])
    ROBOT_6.set_neighbors([ROBOT_3, ROBOT_5, ROBOT_9])
    ROBOT_7.set_neighbors([ROBOT_4, ROBOT_8])
    ROBOT_8.set_neighbors([ROBOT_5, ROBOT_7, ROBOT_9])
    ROBOT_9.set_neighbors([ROBOT_6, ROBOT_8])

    # With diagonal neighbors
    # ROBOT_1.set_neighbors([ROBOT_2, ROBOT_4, ROBOT_5])
    # ROBOT_2.set_neighbors([ROBOT_1, ROBOT_3, ROBOT_4, ROBOT_5, ROBOT_6])
    # ROBOT_3.set_neighbors([ROBOT_2, ROBOT_5, ROBOT_6])
    # ROBOT_4.set_neighbors([ROBOT_1, ROBOT_2, ROBOT_5, ROBOT_7, ROBOT_8])
    # ROBOT_5.set_neighbors([ROBOT_2, ROBOT_3, ROBOT_4, ROBOT_5, ROBOT_6, ROBOT_7, ROBOT_8])
    # ROBOT_6.set_neighbors([ROBOT_2, ROBOT_3, ROBOT_5, ROBOT_8, ROBOT_9])
    # ROBOT_7.set_neighbors([ROBOT_4, ROBOT_5, ROBOT_8])
    # ROBOT_8.set_neighbors([ROBOT_4, ROBOT_5, ROBOT_6, ROBOT_7, ROBOT_9])
    # ROBOT_9.set_neighbors([ROBOT_5, ROBOT_6, ROBOT_8])

    return robots

def print_dance(robots, final_time):
        NUM_ROBOTS = 8
        INIT_POS = [0, 0, 0, 90, 0, 0, 0]
        dances = []
        dances_t = []
        for robot in robots:
            dances.append(robot.dance)
            dances_t.append(robot.dance_t)
        [trajectory,velocity] = traj.generate_trajectory(dances, dances_t, final_time)
        
        for robot in range(NUM_ROBOTS):
            robot_loc = 7 * (robot)
            for i in range(7):
                trajectory[i + robot_loc, :] = trajectory[i + robot_loc, :] + INIT_POS[i]
               # trajectory[i + robot_loc, :] = trajectory[i + robot_loc, :]
                if i < 3:
                    trajectory[i, :] = -1 * trajectory[i, :]

        final_position_db = np.transpose(trajectory)
        final_position = final_position_db[0::6, :]

        df = pd.DataFrame(final_position).astype(float)
        # df.to_csv("/home/forest/Desktop/xArm/Trajectories2/000027gameoflife.csv", header=False, index=False)
        df.to_csv("flock.csv", header=False, index=False)

        final_trajectory = velocity
        final_trajectory = np.transpose(final_trajectory)

        for robot in robots:
            robot_pos = robot.get_num() * 7
            robot_vel = []
            for i in range(7):
                # print(len(final_trajectory[(i+robot_pos), :]))
                # print(np.max(final_trajectory[(i+robot_pos), :]))
                plt.plot(final_trajectory[:, (i+robot_pos)])
            plt.show()

        
        pd.DataFrame(final_trajectory).to_csv("flock_vel.csv", header=False, index=False)

        

def main():
    robots = init_robots()
    for robot in robots:
        print('Robot: ' + str(robot.get_num()) +
                ' Angle: ' + str(robot.get_joint_0()))
    flock = Flock(robots)
    flock.run()
    for robot in robots:
        print('Robot: ' + str(robot.get_num()) +
                ' Angle: ' + str(robot.get_joint_0_moves()))
        robot.define_dance()
    print_dance(robots, 5)
    


main()
