from random import randint
import numpy as np

import math


class Robot:
    def __init__(self, num, x_pos, y_pos):
        self.num = num
        self.dance = []
        self.dance_t = []
        self.joint_0 = randint(0, 360)
        self.x_pos = x_pos
        self.y_pos = y_pos

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def get_neighbors(self):
        return self.neighbors

    def get_num(self):
        return self.num

    # calculates a steering force toward a target
    def steer(self, target_x, target_y):
        desired_x = target_x - self.x_pos
        desired_y = target_y - self.y_pos
        direction = math.degrees(math.atan((desired_x / desired_y)))
        return direction

    # for all neighbors calculate the average joint_0 angle
    def align(self):
        sum = 0
        num_neighbors = 0
        for neighbor in self.neighbors:
            sum += neighbor.joint_0
            num_neighbors += 1
        
        sum = sum / num_neighbors
        steer = sum - self.joint_0
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
        coh = self.cohesion()

        # apply weights
        align = align * 1.2
        coh = coh * .8

        # find average angle to move 
        new_angle = (align + coh) / 2
        



class Flock:

    def __init__(self, robots):
        self.robots = robots
    
    def run(self):
        for robot in self.robots:
            robot.flock()



def init_robots():
    ROBOT_1 = Robot(0, 0, 0)
    ROBOT_2 = Robot(1, 1, 0)
    ROBOT_3 = Robot(2, 2, 0)
    ROBOT_4 = Robot(3, 0, 1)
    ROBOT_5 = Robot(4, 1, 1)
    ROBOT_6 = Robot(5, 2, 1)
    ROBOT_7 = Robot(6, 0, 2)
    ROBOT_8 = Robot(7, 1, 2)
    ROBOT_9 = Robot(8, 2, 2)
    # ROBOT_10 = Robot(9)

    robots = [ROBOT_1, ROBOT_2, ROBOT_3, ROBOT_4, ROBOT_5, ROBOT_6, ROBOT_7, ROBOT_8, ROBOT_9]

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

def main():
    robots = init_robots()
    flock = Flock(robots)
    flock.run()


main()




