from random import randint
import numpy as np
import math
import pandas as pd
import pid
import queue
import time
import matplotlib
import matplotlib.pyplot as plt
import threading

# from xarm.wrapper import XArmAPI

# def setup(arms):
#     for a in arms:
#         a.set_simulation_robot(on_off=False)
#         a.motion_enable(enable=True)
#         a.clean_warn()
#         a.clean_error()
#         a.set_mode(0)
#         a.set_state(0)
#         a.set_servo_angle(angle=[0.0, 0.0, 0.0, 1.57, 0.0, 0, 0.0], wait=False, speed=0.4, acceleration=0.25,
#                           is_radian=True)

# def run_robots():
#     arm1 = XArmAPI('192.168.1.203')
#     arm3 = XArmAPI('192.168.1.236')
#     arm5 = XArmAPI('192.168.1.234')
#     arm7 = XArmAPI('192.168.1.208')
#     arm9 = XArmAPI('192.168.1.226')
#     arms = [arm1, arm3, arm5, arm7, arm9]
#     setup(arms)
#     repeat = input("do we need to repeat? [y/n]")
#     if repeat == 'y':
#         for a in arms:
#             print('state:', arm1.state)
#             print('mode:', arm1.mode)
#         setup(arms)
#     for a in arms:
#         a.set_mode(1)
#         a.set_state(0)
#     return arms


class Robot:
    def __init__(self, num, x_pos, y_pos):
        self.num = num
        self.dance = []
        self.dance_t = []
        self.joint_1 = randint(0, 355)
        self.joint_1_PID = None
        self.joint_2 = 0
        self.joint_2_PID = None
        # self.joint_3 = randint(0, 355)
        self.joint_3 = randint(0, 355)
        self.joint_3_PID = None
        self.joint_4 = 0
        self.joint_4_PID = None
        self.joint_5 = randint(0, 355)
        self.joint_5_PID = None
        self.joint_6 = 0
        self.joint_6_PID = None
        self.joint_7 = 0
        self.joint_7_PID = None
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.live_pos = [0, 0, 0, 90, 0, 0, 0]
        self.que = queue.Queue()
        self.f = open(('live_traj' + str(num) + '.csv'), 'w')


    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def set_target(self, target):
        self.target = target

    def get_neighbors(self):
        return self.neighbors

    def get_num(self):
        return self.num

    def get_joint_1(self):
        return self.joint_1

    def get_joint_2(self):
        return self.joint_2

    def get_joint_3(self):
        return self.joint_3
    
    def get_joint_4(self):
        return self.joint_4

    def get_joint_4(self):
        return self.joint_4
    
    def get_joint_5(self):
        return self.joint_5

    def get_joint_6(self):
        return self.joint_6

    def get_joint_7(self):
        return self.joint_7

    def get_joints(self):
        return [self.joint_1, self.joint_2, self.joint_3, self.joint_4, self.joint_5, self.joint_6, self.joint_7]

    def update_joints(self, new_angles):
        self.joint_1 = new_angles[0]
        self.joint_2 = new_angles[1]
        self.joint_3 = new_angles[2]
        self.joint_4 = new_angles[3]
        self.joint_5 = new_angles[4]
        self.joint_6 = new_angles[5]
        self.joint_7 = new_angles[6]

    def add_to_que(self, angles):
        self.que.put(angles)

    def get_que(self):
        return self.que

    def get_pos(self):
        return [self.joint_1, self.joint_2, self.joint_3, self.joint_4, self.joint_5, self.joint_6, self.joint_7]
   
    def check_joints(self, new_angles):
        if abs(self.joint_1 + new_angles[0]) >= 360:
            raise ValueError("Joint 1 Out of Bounds")
        else:
            self.joint_1 += new_angles[0]

        if abs(self.joint_2 + new_angles[1]) >= 118:
            raise ValueError("Joint 2 Out of Bounds")
        else:
            self.joint_2 += new_angles[1]

        if abs(self.joint_3 + new_angles[2]) >= 360:
            raise ValueError("Joint 3 Out of Bounds")
        else:
            self.joint_3 += new_angles[2]

        if (self.joint_4 + new_angles[3]) >= 224 or (self.joint_4 + new_angles[3]) <= -10:
            raise ValueError("Joint 4 Out of Bounds")
        else:
            self.joint_4 += new_angles[3]

        if abs(self.joint_5 + new_angles[4]) >= 360:
            raise ValueError("Joint 5 Out of Bounds")
        else:
            self.joint_5 += new_angles[4]

        if (self.joint_6 + new_angles[5]) >= 179 or (self.joint_6 + new_angles[5]) <= -96:
            raise ValueError("Joint 6 Out of Bounds")
        else:
            self.joint_6 += new_angles[5]

        if abs(self.joint_7 + new_angles[6]) >= 360:
            raise ValueError("Joint 7 Out of Bounds")
        else:
            self.joint_7 += new_angles[6]
    
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

    # for all neighbors calculate the average joint_5 angle
    def align(self, joint_num):
        sum = 0
        num_neighbors = 0
        for neighbor in self.neighbors:
            sum += neighbor.choose_joint(joint_num)[0]
            num_neighbors += 1

        sum = sum / num_neighbors
        # steer = sum - self.joint_5
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

    def choose_joint(self, joint_num):
        if joint_num == 1:
            return [self.joint_1]
        if joint_num == 2:
            return [self.joint_2]
        if joint_num == 3:
            return [self.joint_3]
        if joint_num == 4:
            return [self.joint_4]
        if joint_num == 5:
            return [self.joint_5]
        if joint_num == 6:
            return [self.joint_6]
        if joint_num == 7:
            return [self.joint_7]

    def get_joint_PID(self, joint_num):
        if joint_num == 1:
            return [self.joint_1_PID]
        if joint_num == 2:
            return [self.joint_2_PID]
        if joint_num == 3:
            return [self.joint_3_PID]
        if joint_num == 4:
            return [self.joint_4_PID]
        if joint_num == 5:
            return [self.joint_5_PID]
        if joint_num == 6:
            return [self.joint_6_PID]
        if joint_num == 7:
            return [self.joint_7_PID]
   
    def init_PID(self, joint_nums=[1, 2, 3, 4, 5, 6, 7]):
        target_val = self.joint_1
        self.joint_1_PID = pid.PID(1.5, 0.01, 0.1, setpoint=target_val)
        self.joint_1_PID.output_limits = (0, 360)

        target_val = self.joint_2
        self.joint_2_PID = pid.PID(1.5, 0.01, 0.1, setpoint=target_val)
        self.joint_2_PID.output_limits = (0, 118)

        target_val = self.joint_3
        self.joint_3_PID = pid.PID(1.5, 0.01, 0.1, setpoint=target_val)
        self.joint_3_PID.output_limits = (0, 360)

        target_val = self.joint_4
        self.joint_4_PID = pid.PID(1.5, 0.01, 0.1, setpoint=target_val)
        self.joint_4_PID.output_limits = (0, 224)

        target_val = self.joint_5
        self.joint_5_PID = pid.PID(1.5, 0.01, 0.1, setpoint=target_val)
        self.joint_5_PID.output_limits = (0, 360)

        target_val = self.joint_6
        self.joint_6_PID = pid.PID(1.5, 0.01, 0.1, setpoint=target_val)
        self.joint_6_PID.output_limits = (0, 179)

        target_val = self.joint_7
        self.joint_7_PID = pid.PID(1.5, 0.01, 0.1, setpoint=target_val)
        self.joint_7_PID.output_limits = (0, 360)

    
    def call_PID(self, input_angle, joint_num):
        curr_PID = self.get_joint_PID(joint_num)
        return curr_PID[0](input_angle)


    def flock(self, joint_nums=[1, 2, 3, 4, 5, 6, 7], align_weight=0.5, target=False, target_weight=False, use_PID=False):
        curr_joints = self.get_joints()
        new_joints = [0, 0, 0, 0, 0, 0, 0]
        for i in range(0, len(joint_nums)):
            joint = curr_joints[i]
            align = self.align(i+1)

            if target:
                new_angle = ((align * align_weight) + (joint * (1 - align_weight - target_weight)) + (self.target[i-1] * target_weight))
            else:
                new_angle = ((align * align_weight) + (joint * (1 - align_weight)))

            if use_PID:
                new_angle = self.call_PID(new_angle, i+1)

            new_joints[i] = new_angle

        self.update_joints(new_joints)
        self.add_to_que(new_joints) 

            # return new_angle
            # coh = self.cohesion()

            # # apply weights
            # align = align * 1.2
            # coh = coh * .8

            # # find average angle to move
            # new_angle = (align + coh) / 2
            # return new_angle

    def change_joints(self):
        if not self.que.empty():
            # print("moving")
            tf = 50
            t_step = 0.006
            t_array = np.arange(0, tf, t_step)

            q_dot_f = np.zeros(7)
            q_dotdot_f = np.zeros(7)
            p = self.live_pos

            q = self.que.get()

            goal = q

            q_i = p
            q_dot_i = np.zeros(7)
            q_dotdot_i = np.zeros(7)
            q_f = goal

            j = 0

            while j < len(t_array):
                start_time = time.time()

                if abs(p[0] - q_f[0]) < 1.0 and abs(p[1] - q_f[1]) < 1.0 and abs(p[2] - q_f[2]) < 1.0 and abs(
                        p[3] - q_f[3]) < 1.0 and abs(p[4] - q_f[4]) < 1.0 and abs(p[5] - q_f[5]) < 1.0 and abs(
                    p[6] - q_f[6]) < 1.0:
                    break

                if j == len(t_array):
                    t = tf
                else:
                    t = t_array[j]

                a0 = q_i
                a1 = q_dot_i
                a2 = []
                a3 = []
                a4 = []
                a5 = []

                for i in range(0, 7):
                    a2.append(0.5 * q_dotdot_i[i])
                    a3.append(1.0 / (2.0 * tf ** 3.0) * (
                            20.0 * (q_f[i] - q_i[i]) - (8.0 * q_dot_f[i] + 12.0 * q_dot_i[i]) * tf - (
                            3.0 * q_dotdot_f[i] - q_dotdot_i[i]) * tf ** 2.0))
                    a4.append(1.0 / (2.0 * tf ** 4.0) * (
                            30.0 * (q_i[i] - q_f[i]) + (14.0 * q_dot_f[i] + 16.0 * q_dot_i[i]) * tf + (
                            3.0 * q_dotdot_f[i] - 2.0 * q_dotdot_i[i]) * tf ** 2.0))
                    a5.append(1.0 / (2.0 * tf ** 5.0) * (
                            12.0 * (q_f[i] - q_i[i]) - (6.0 * q_dot_f[i] + 6.0 * q_dot_i[i]) * tf - (
                            q_dotdot_f[i] - q_dotdot_i[i]) * tf ** 2.0))

                    p[i] = (a0[i] + a1[i] * t + a2[i] * t ** 2 + a3[i] * t ** 3 + a4[i] * t ** 4 + a5[i] * t ** 5)

                # self.arm.set_servo_angle_j(angles=p, is_radian=False)
                # print(f"{p} {self.num}")
                self.f.write(",".join(str(x) for x in p))
                self.f.write("\n")

                tts = time.time() - start_time
                sleep = t_step - tts

                if tts > t_step:
                    sleep = 0

                time.sleep(sleep)
                j += 1

                self.live_pos = p


class Flock:

    def __init__(self, robots):
        self.robots = robots
        for robot in self.robots:
            robot.init_PID()

    def check_alignment(self, robots):
        joints_1 = []
        joints_2 = []
        joints_3 = []
        joints_4 = []
        joints_5 = []
        joints_6 = []
        joints_7 = []

        for i in range(8):
            pos = robots[i].get_pos()
            joints_1.append(pos[0])
            joints_2.append(pos[1])
            joints_3.append(pos[2])
            joints_4.append(pos[3])
            joints_5.append(pos[4])
            joints_6.append(pos[5])
            joints_7.append(pos[6])

        if all(x in joints_1 for x in range(int(joints_1[0] - 5), int(joints_1[0] + 5))):
            print('joints 1 aligned')
        if all(x in joints_3 for x in range(int(joints_3[0] - 5), int(joints_3[0] + 5))):
            print('joints 3 aligned')
        if all(x in joints_5 for x in range(int(joints_5[0] - 5), int(joints_5[0] + 5))):
            print('joints 5 aligned')

    def run(self):
        self.move_state(self.robots)  
        for i in range(10):
            for robot in self.robots:
                # robot.flock(use_PID=True)
                robot.flock(align_weight=0.5, target=False, target_weight=0.25, use_PID=False)
                # robot.flock(align_weight=0.5, target=False, target_weight=0.25, use_PID=True)
                print("Robot " + str(robot.get_num()) + ": " + str(robot.get_pos()))
            self.check_alignment(self.robots)
            # self.move_state(self.robots)
    
    def move_state(self, robots):
        t1 = threading.Thread(target=robots[0].change_joints, args=())
        t2 = threading.Thread(target=robots[1].change_joints, args=())
        t3 = threading.Thread(target=robots[2].change_joints, args=())
        t4 = threading.Thread(target=robots[3].change_joints, args=())
        t5 = threading.Thread(target=robots[4].change_joints, args=())

        # start threads
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()

        # t1.join()
        # t2.join()
        # t3.join()
        # t4.join()
        # t5.join()
            


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

    # ROBOT_1.set_neighbors([ROBOT_2, ROBOT_4])
    # ROBOT_2.set_neighbors([ROBOT_1, ROBOT_3, ROBOT_5])
    # ROBOT_3.set_neighbors([ROBOT_2, ROBOT_6])
    # ROBOT_4.set_neighbors([ROBOT_1, ROBOT_5, ROBOT_7])
    # ROBOT_5.set_neighbors([ROBOT_2, ROBOT_4, ROBOT_6, ROBOT_8])
    # ROBOT_6.set_neighbors([ROBOT_3, ROBOT_5, ROBOT_9])
    # ROBOT_7.set_neighbors([ROBOT_4, ROBOT_8])
    # ROBOT_8.set_neighbors([ROBOT_5, ROBOT_7, ROBOT_9])
    # ROBOT_9.set_neighbors([ROBOT_6, ROBOT_8])

    ROBOT_1.set_target([0, 0, 0, 0, randint(0, 350), 0, 0])
    ROBOT_2.set_target([0, 0, 0, 0, randint(0, 350), 0, 0])
    ROBOT_3.set_target([0, 0, 0, 0, randint(0, 350), 0, 0])
    ROBOT_4.set_target([0, 0, 0, 0, randint(0, 350), 0, 0])
    ROBOT_5.set_target([0, 0, 0, 0, randint(0, 350), 0, 0])
    ROBOT_6.set_target([0, 0, 0, 0, randint(0, 350), 0, 0])
    ROBOT_7.set_target([0, 0, 0, 0, randint(0, 350), 0, 0])
    ROBOT_8.set_target([0, 0, 0, 0, randint(0, 350), 0, 0])
    ROBOT_9.set_target([0, 0, 0, 0, randint(0, 350), 0, 0])

    # With diagonal neighbors
    ROBOT_1.set_neighbors([ROBOT_2, ROBOT_4, ROBOT_5])
    ROBOT_2.set_neighbors([ROBOT_1, ROBOT_3, ROBOT_4, ROBOT_5, ROBOT_6])
    ROBOT_3.set_neighbors([ROBOT_2, ROBOT_5, ROBOT_6])
    ROBOT_4.set_neighbors([ROBOT_1, ROBOT_2, ROBOT_5, ROBOT_7, ROBOT_8])
    ROBOT_5.set_neighbors([ROBOT_2, ROBOT_3, ROBOT_4, ROBOT_5, ROBOT_6, ROBOT_7, ROBOT_8])
    ROBOT_6.set_neighbors([ROBOT_2, ROBOT_3, ROBOT_5, ROBOT_8, ROBOT_9])
    ROBOT_7.set_neighbors([ROBOT_4, ROBOT_5, ROBOT_8])
    ROBOT_8.set_neighbors([ROBOT_4, ROBOT_5, ROBOT_6, ROBOT_7, ROBOT_9])
    ROBOT_9.set_neighbors([ROBOT_5, ROBOT_6, ROBOT_8])

    return robots

def print_dance(robots, final_time):
        NUM_ROBOTS = 9
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
        # df.to_csv("/home/codmusic/Desktop/FOREST/Jocelyn_Scripts/flock.csv", header=False, index=False)
        df.to_csv("/Users/jocekav/Documents/GitHub/Forest/flock.csv", header=False, index=False)
        #
        final_trajectory = velocity
        final_trajectory = np.transpose(final_trajectory)
        #
        for robot in robots:
            robot_pos = robot.get_num() * 7
            robot_vel = []
            for i in range(7):
                print(len(final_trajectory[(i+robot_pos), :]))
                print(np.max(final_trajectory[(i+robot_pos), :]))
                plt.plot(final_trajectory[:, (i+robot_pos)])
            plt.show()

        for robot in robots:
            robot_pos = robot.get_num() * 7
            robot_vel = []
            for i in range(7):
                print(len(final_position[(i+robot_pos), :]))
                print(np.max(final_position[(i+robot_pos), :]))
                plt.plot(final_position[:, (i+robot_pos)])
            plt.show()

        
        # pd.DataFrame(final_trajectory).to_csv("flock_vel.csv", header=False, index=False)

        

def main():
    robots = init_robots()
    for robot in robots:
        print('Robot: ' + str(robot.get_num()) +
                ' Angle: ' + str(robot.get_joints()))
    flock = Flock(robots)
    flock.run()
    # for robot in robots:
    #     print('Robot: ' + str(robot.get_num()) +
    #             ' Angle: ' + str(robot.get_joints()))
    #     robot.define_dance()
    # print_dance(robots, 5)
    


main()