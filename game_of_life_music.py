# ROBOT_1_NEIGHBORS = [ROBOT_2, ROBOT_5]
# ROBOT_2_NEIGHBORS = [ROBOT_1, ROBOT_3, ROBOT_5, ROBOT_6, ROBOT_8]
# ROBOT_3_NEIGHBORS = [ROBOT_2, ROBOT_4, ROBOT_6, ROBOT_7, ROBOT_9]
# ROBOT_4_NEIGHBORS = [ROBOT_3, ROBOT_7]
# ROBOT_5_NEIGHBORS = [ROBOT_1, ROBOT_2, ROBOT_6, ROBOT_8]
# ROBOT_6_NEIGHBORS = [ROBOT_2, ROBOT_3, ROBOT_5, ROBOT_7, ROBOT_8, ROBOT_9]
# ROBOT_7_NEIGHBORS = [ROBOT_3, ROBOT_4, ROBOT_6, ROBOT_9]
# ROBOT_8_NEIGHBORS = [ROBOT_2, ROBOT_5, ROBOT_6, ROBOT_9, ROBOT_10]
# ROBOT_9_NEIGHBORS = [ROBOT_3, ROBOT_6, ROBOT_7, ROBOT_8, ROBOT_10]
# ROBOT_10_NEIGHBORS = [ROBOT_6, ROBOT_8, ROBOT_9]

from random import randint
import numpy as np
import trajectory_generation as traj
import pandas as pd
import csv

import play_dances_gameoflife
import threading
import socket
import pickle
import time
import pythonosc
from pythonosc import udp_client


class Robot:
    def __init__(self, num):
        self.status = 'Dead'
        self.num = num
        self.dance = []
        self.dance_t = []
        self.curr_angle = 90

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def get_neighbors(self):
        return self.neighbors

    def get_num(self):
        return self.num

    def set_die(self, first=False):
        self.status = 'Dead'
        # call die movement here
        # if first:
        #     self.death()
        # else:
        self.death()

    def set_alive(self, first=False):
        self.status = 'Alive'
        # call birth movement here
        # if first:
        #     self.first_birth()
        # else:
        self.birth()

    def set_living(self):
        self.status = 'Living'
        # call living movement here
        self.living()

    def set_dying(self):
        self.status = 'Dying'
        # call dying movement here
        self.dying()

    def set_inactive(self):
        self.status = 'Inactive'
        self.inactive()

    def is_alive(self):
        if self.status == 'Alive' or self.status == 'Living':
            return True
        else:
            return False

    def is_inactive(self):
        if self.status == 'Inactive':
            return True
        else:
            return False

    def get_status(self):
        return self.status

    def birth(self):
        # joint 4 starts at 90
        # full alive position for joint 4 at 120
        if self.curr_angle == 90:
            birth_move = np.array([0, -30, 0, 30, 0, 0, 0], dtype=object)
            birth_time = np.array([4, 4, 4, 4, 4, 4, 4], dtype=object)

            self.dance.append(birth_move)
            self.dance_t.append(birth_time)

            self.curr_angle = self.curr_angle + 30
        else:
            birth_move = np.array([0, -50, 0, 60, 0, 0, 0], dtype=object)
            birth_time = np.array([4, 4, 4, 4, 4, 4, 4], dtype=object)

            self.dance.append(birth_move)
            self.dance_t.append(birth_time)

            self.curr_angle = self.curr_angle + 60

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

    def inactive(self):
        inactive_move = np.array([0, 0, 0, 0, 0, 0, 0], dtype=object)
        inactive_time = np.array([4, 4, 4, 4, 4, 4, 4], dtype=object)

        self.dance.append(inactive_move)
        self.dance_t.append(inactive_time)




class Game:

    def __init__(self, robots, dances, arms):
        for robot in robots:
            random = randint(0, 2)
            if random == 1:
                robot.set_alive(True)
            else:
                robot.set_die(True)
        self.dances = dances
        self.arms = arms

        IP = "192.168.0.19"
        PORT_TO_MAX = 7980
        self.client = udp_client.SimpleUDPClient(IP, PORT_TO_MAX)

    def set_dances_arms(self, dances, arms):
        self.dances = dances
        self.arms = arms

    def get_dances_arms(self):
        return self.dances, self.arms

    def revive(self, robots):
        for robot in robots:
            random = randint(0, 2)
            if random == 1:
                robot.set_alive()
            else:
                robot.set_die()

    def change_state(self, robots):
        birth = []
        birth_ids = []
        kill = []
        kill_ids = []
        living = []
        living_ids = []
        dying = []
        dying_ids = []
        death_count = 0

        for robot in robots:

            neighbors = robot.get_neighbors()
            live_neighbors = 0
            total_neighbors = len(neighbors)
            half_neighbors = int(total_neighbors / 2)
            for neighbor in neighbors:
                if neighbor.is_alive():
                    live_neighbors += 1

            curr_robot_living = robot.is_alive()

            if curr_robot_living:
                if live_neighbors == 0:
                    kill.append(robot)
                elif live_neighbors >= half_neighbors:
                    kill.append(robot)
                else:
                    living.append(robot)
            else:
                if live_neighbors >= half_neighbors:
                    birth.append(robot)
                else:
                    dying.append(robot)
                    death_count += 1

        for i in birth:
            i.set_alive()
            birth_ids.append(i.get_num())
        for i in kill:
            i.set_die()
            kill_ids.append(i.get_num())
        for i in living:
            i.set_living()
            living_ids.append(i.get_num())
        for i in dying:
            i.set_dying()
            dying_ids.append(i.get_num())
        if death_count == 9:
            self.revive(robots)

        call_sound(self.client, birth_ids, kill_ids, living_ids, dying_ids)
        call_dances(self.dances, self.arms, birth_ids, kill_ids, living_ids, dying_ids)


    def run_game(self, robots, iterations):
        for robot in robots:
            random = randint(0, 2)
            if random == 1:
                robot.set_alive(True)
            else:
                robot.set_die(True)

        curr_state = ''
        for robot in robots:
            curr_state = curr_state + robot.get_status() + ' '
        print(curr_state)

        for i in range(iterations):
            self.change_state(robots)
            curr_state = ''
            for robot in robots:
                curr_state = curr_state + robot.get_status() + ' '
            print(curr_state)

    def change_state_contagion(self, robots):
        birth = []
        birth_ids = []
        kill = []
        kill_ids = []
        living = []
        living_ids = []
        dying = []
        dying_ids = []
        death_count = 0

        for robot in robots:

            neighbors = robot.get_neighbors()
            live_neighbors = 0
            active_neighbors = 0
            total_neighbors = len(neighbors)
            half_neighbors = int(total_neighbors / 2)
            for neighbor in neighbors:
                if neighbor.is_alive():
                    live_neighbors += 1
                if not neighbor.is_inactive():
                    active_neighbors += 1

            curr_robot_living = robot.is_alive()
            curr_robot_inactive = robot.is_inactive()

            if curr_robot_living:
                if live_neighbors == 0:
                    kill.append(robot)
                elif live_neighbors >= half_neighbors:
                    kill.append(robot)
                else:
                    living.append(robot)
            elif curr_robot_inactive:
                if live_neighbors >= half_neighbors or active_neighbors >= 1:
                    birth.append(robot)
            else:
                if live_neighbors >= half_neighbors:
                    birth.append(robot)
                else:
                    dying.append(robot)
                    death_count += 1

        for i in birth:
            i.set_alive()
            birth_ids.append(i.get_num())
        for i in kill:
            i.set_die()
            kill_ids.append(i.get_num())
        for i in living:
            i.set_living()
            living_ids.append(i.get_num())
        for i in dying:
            i.set_dying()
            dying_ids.append(i.get_num())
        if death_count == 9:
            self.revive(robots)

        call_sound(self.client, birth_ids, kill_ids, living_ids, dying_ids)
        call_dances(self.dances, self.arms, birth_ids, kill_ids, living_ids, dying_ids)

    def run_game_contagion(self, robots, first_robot, iterations):
        for robot in robots:
            robot.set_inactive()
        robots[first_robot].set_alive()


        curr_state = ''
        for robot in robots:
            curr_state = curr_state + robot.get_status() + ' '
        print(curr_state)

        call_sound(self.client, [first_robot], [], [], [])
        #alive_dance(first_robot, self.dances, self.arms)

        for robot in robots:
            robot.set_inactive()
        robots[first_robot].set_living()

        curr_state = ''
        for robot in robots:
            curr_state = curr_state + robot.get_status() + ' '
        print(curr_state)

        call_sound(self.client, [], [], [first_robot], [])
        #living_dance(first_robot, self.dances, self.arms)

        # look at neighbors before waking up?

        # robots[first_robot].get_neighbors()

        for i in range(iterations):
            self.change_state_contagion(robots)
            curr_state = ''
            for robot in robots:
                curr_state = curr_state + robot.get_status() + ' '
            print(curr_state)


    def print_dance(self, robots, final_time):
        dances = []
        dances_t = []
        for robot in robots:
            dances.append(robot.dance)
            dances_t.append(robot.dance_t)
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

        # final_trajectory = velocity
        # final_trajectory = np.transpose(final_trajectory)
        #
        # pd.DataFrame(final_trajectory).to_csv("dance_groove_vel_1.csv")


def call_sound(client, alive, dead, living, dying):
    sound_states = np.zeros(10)
    for i in alive:
        sound_states[i] = 1
    for i in dead:
        sound_states[i] = 2
    for i in living:
        sound_states[i] = 3
    for i in dying:
        sound_states[i] = 4

    print(sound_states)
    client.send_message('arms', sound_states)
    time.sleep(8)

def call_dances(dances, arms, alive, dead, living, dying):
    t1 = threading.Thread(target=alive_dance, args=([alive], dances, arms))
    t2 = threading.Thread(target=dead_dance, args=([dead], dances, arms))
    t3 = threading.Thread(target=living_dance, args=([living], dances, arms))
    t4 = threading.Thread(target=dying_dance, args=([dying], dances, arms))

    # start threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()


def alive_dance(robots, dances, arms):
    play_dances_gameoflife.playDance(4, robots, dances, arms)
    ### ADD PROPER DANCE NUMBER ONCE YOU RUN THE CSVS!!!!


def dead_dance(robots, dances, arms):
    play_dances_gameoflife.playDance(8, robots, dances, arms)
    ### ADD PROPER DANCE NUMBER ONCE YOU RUN THE CSVS!!!!


def living_dance(robots, dances, arms):
    play_dances_gameoflife.playDance(5, robots, dances, arms)
    ### ADD PROPER DANCE NUMBER ONCE YOU RUN THE CSVS!!!!


def dying_dance(robots, dances, arms):
    play_dances_gameoflife.playDance(9, robots, dances, arms)
    ### ADD PROPER DANCE NUMBER ONCE YOU RUN THE CSVS!!!!


def init_robots():
    ROBOT_1 = Robot(0)
    ROBOT_2 = Robot(1)
    ROBOT_3 = Robot(2)
    ROBOT_4 = Robot(3)
    ROBOT_5 = Robot(4)
    ROBOT_6 = Robot(5)
    ROBOT_7 = Robot(6)
    ROBOT_8 = Robot(7)
    ROBOT_9 = Robot(8)
    ROBOT_10 = Robot(9)

    robots = [ROBOT_1, ROBOT_2, ROBOT_3, ROBOT_4, ROBOT_5, ROBOT_6, ROBOT_7, ROBOT_8, ROBOT_9, ROBOT_10]

    ROBOT_1.set_neighbors([ROBOT_2, ROBOT_5])
    ROBOT_2.set_neighbors([ROBOT_1, ROBOT_3, ROBOT_5, ROBOT_6, ROBOT_8])
    ROBOT_3.set_neighbors([ROBOT_2, ROBOT_4, ROBOT_6, ROBOT_7, ROBOT_9])
    ROBOT_4.set_neighbors([ROBOT_3, ROBOT_7])
    ROBOT_5.set_neighbors([ROBOT_1, ROBOT_2, ROBOT_6, ROBOT_8])
    ROBOT_6.set_neighbors([ROBOT_2, ROBOT_3, ROBOT_5, ROBOT_7, ROBOT_8, ROBOT_9])
    ROBOT_7.set_neighbors([ROBOT_3, ROBOT_4, ROBOT_6, ROBOT_9])
    ROBOT_8.set_neighbors([ROBOT_2, ROBOT_5, ROBOT_6, ROBOT_9, ROBOT_10])
    ROBOT_9.set_neighbors([ROBOT_3, ROBOT_6, ROBOT_7, ROBOT_8, ROBOT_10])
    ROBOT_10.set_neighbors([ROBOT_6, ROBOT_8, ROBOT_9])

    return robots

def init_and_run(dances, arms):
    robots = init_robots()
    game = Game(robots, dances, arms)
    # game.init_audio('Joy.wav', 'Sad.wav')
    iterations = 2
    game.run_game(robots, iterations)

def init_and_run_contagion(dances, arms):
    robots = init_robots()
    game = Game(robots, dances, arms)
    # game.init_audio('Joy.wav', 'Sad.wav')
    iterations = 5
    first_robot = 0
    game.run_game_contagion(robots, first_robot, iterations)


def test_without_arms():
    # start = time.time()
    robots = init_robots()
    game = Game(robots, [], [])
    # game.init_audio('Joy.wav', 'Sadness.wav')
    # game.run_game(robots, iterations)
    iterations = 2
    first_robot = 0
    game.run_game_contagion(robots, first_robot, iterations)











