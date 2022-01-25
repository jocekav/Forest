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
from tracemalloc import start
import numpy as np
# import trajectory_generation as traj
import pandas as pd
import csv

# import play_dances_gameoflife
# from Game_Of_Life.play_dances_gameoflife import playDance
import threading
import socket
import pickle
import time
from pythonosc import udp_client
from random import randrange


class Robot:
    def __init__(self, num):
        self.status = 'Dead'
        self.num = num
        self.dance = []
        self.dance_t = []
        self.curr_angle = 90
        self.core_neighbor = False

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def get_neighbors(self):
        return self.neighbors
    
    def get_core_neighbor(self):
        return self.core_neighbor
    
    def set_core_neighbor(self, state):
        self.core_neighbor = state

    def get_num(self):
        return self.num

    def set_die(self):
        self.status = 'Dead'
        # call death movement
        self.death()

    def set_alive(self):
        self.status = 'Alive'
        # call birth movement
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

    def set_first_birth(self):
        self.status = 'First Birth'
    
    def set_first_death(self):
        self.status = 'First Death'

    def is_alive(self):
        if self.status == 'Alive' or self.status == 'Living' or self.status == 'First Birth':
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
                robot.set_alive()
            else:
                robot.set_die()
        self.dances = dances
        self.arms = arms

        # IP = "128.61.25.122"
        IP = "128.61.27.43"
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

        sound_states = np.zeros(20)

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
            robot_num = i.get_num()
            birth_ids.append(robot_num)
            sound_states[robot_num * 2] = 1
            sound_states[(robot_num * 2) + 1] = .75
        for i in kill:
            i.set_die()
            robot_num = i.get_num()
            kill_ids.append(robot_num)
            sound_states[robot_num * 2] = 2
            sound_states[(robot_num * 2) + 1] = .5
        for i in living:
            i.set_living()
            robot_num = i.get_num()
            living_ids.append(robot_num)
            sound_states[robot_num * 2] = 3
            sound_states[(robot_num * 2) + 1] = .75
        for i in dying:
            i.set_dying()
            robot_num = i.get_num()
            dying_ids.append(robot_num)
            sound_states[robot_num * 2] = 4
            sound_states[(robot_num * 2) + 1] = .25
        if death_count == 9:
            self.revive(robots)

        # call_sound(self.client, sound_states)

        for robot in robots:
            curr_state = robot.get_status()
            neighbors = robot.get_neighbors()
            total_neighbors = len(neighbors)
            matching_states = 0
            for neighbor in neighbors:
                if neighbor.get_status() == curr_state:
                    matching_states += 1
                else:
                    break
            if matching_states == total_neighbors:
                robot.set_core_neighbor(True)
                for neighbor in neighbors:
                    robot_num = neighbor.get_num()
                    sound_states[robot_num * 2] = 0
                    sound_states[(robot_num * 2) + 1] = 0
            else:
                robot.set_core_neighbor(False)
        
        # call_sound(self.client, sound_states)

        for robot in robots:
            if robot.get_core_neighbor == True:
                status = robot.get_status()
                num = robot.get_num()
                sound_states[(num * 2) + 1] = 1
                if status == 'Alive':
                    sound_states[num * 2] = 1
                if status == 'Dead':
                    sound_states[num * 2] = 2
                if status == 'Living':
                    sound_states[num * 2] = 3
                if status == 'Dying':
                    sound_states[num * 2] = 4
                

        # call_sound(self.client, sound_states, sleep_time)
        # call_dances(self.dances, self.arms, birth_ids, kill_ids, living_ids, dying_ids)

    def print_status(self, robots):
            curr_state = ''
            for robot in robots:
                if robot.get_num() == 0 or robot.get_num() == 3 or robot.get_num() == 6:
                    curr_state += '\n'
                if robot.get_status() == 'Dead':
                    curr_state += 'X '
                elif robot.get_status() == 'Alive':
                    curr_state += 'A '
                elif robot.get_status() == 'First Birth':
                    curr_state += 'FA '
                elif robot.get_status() == 'First Death':
                    curr_state += 'FX '
                elif robot.get_status() == 'Living':
                    curr_state += 'L '
                elif robot.get_status() == 'Dying':
                    curr_state += 'D '
            curr_state += '\n------'
            print(curr_state)

    def run_game(self, robots, iterations, start_alive=False, start_dead=False):
        birth_ids = []
        kill_ids = []
        if start_alive:
            birth_ids = start_alive
            kill_ids = start_dead
            for i in birth_ids:
                robots[i].set_first_birth()
            for i in kill_ids:
                robots[i].set_first_death()
        else:
            for robot in robots:
                random = randint(0, 2)
                if random == 1:
                    # robot.set_alive(True)
                    robot.set_first_birth()
                    birth_ids.append(robot.get_num())
                else:
                    robot.set_first_death()
                    kill_ids.append(robot.get_num())

        first_birth_dance(birth_ids, self.dances, self.arms)
        first_death_dance(kill_ids, self.dances, self.arms)

        self.print_status(robots)
        
        for i in range(iterations):
            self.change_state(robots)
            self.print_status(robots)
            

    def change_state_contagion(self, robots, sleep_time, final_flag):
        birth = []
        birth_ids = []
        first_birth = []
        first_birth_ids = []
        kill = []
        kill_ids = []
        first_kill = []
        first_kill_ids = []
        living = []
        living_ids = []
        dying = []
        dying_ids = []
        death_count = 0

        sound_states = np.zeros(20)

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
                    first_birth.append(robot)
            else:
                if live_neighbors >= half_neighbors:
                    birth.append(robot)
                else:
                    dying.append(robot)
                    death_count += 1

        for i in birth:
            i.set_alive()
            robot_num = i.get_num()
            birth_ids.append(robot_num)
            sound_states[robot_num * 2] = 1
            sound_states[(robot_num * 2) + 1] = .75
        for i in first_birth:
            i.set_alive()
            i.set_first_birth()
            robot_num = i.get_num()
            first_birth_ids.append(robot_num)
            sound_states[robot_num * 2] = 1
            sound_states[(robot_num * 2) + 1] = .75
        for i in kill:
            i.set_die()
            robot_num = i.get_num()
            kill_ids.append(robot_num)
            sound_states[robot_num * 2] = 2
            sound_states[(robot_num * 2) + 1] = .5
        for i in living:
            i.set_living()
            robot_num = i.get_num()
            living_ids.append(robot_num)
            sound_states[robot_num * 2] = 3
            sound_states[(robot_num * 2) + 1] = .75
        for i in dying:
            i.set_dying()
            robot_num = i.get_num()
            dying_ids.append(robot_num)
            sound_states[robot_num * 2] = 4
            sound_states[(robot_num * 2) + 1] = .25
        if death_count == 9:
            self.revive(robots)

        # call_sound(self.client, sound_states, sleep_time)
        # call_dances(self.dances, self.arms, birth_ids, kill_ids, living_ids, dying_ids, first_birth_ids, final_flag)

    def run_game_contagion(self, robots, first_robot, iterations, sleep_time):
        for robot in robots:
            robot.set_inactive()
        robots[first_robot].set_first_birth()

        sound_states = np.zeros(20)

        self.print_status(robots)

        sound_states[first_robot * 2] = 1
        sound_states[(first_robot * 2) + 1] = .75

        # call_sound(self.client, sound_states, sleep_time)
        #alive_dance(first_robot, self.dances, self.arms)
        # first_birth_dance(first_robot, self.dances, self.arms)

        for robot in robots:
            robot.set_inactive()
        robots[first_robot].set_living()

        self.print_status(robots)

        sound_states[first_robot * 2] = 3
        sound_states[(first_robot * 2) + 1] = .75

        # call_sound(self.client, sound_states, sleep_time)
        # living_dance(first_robot, self.dances, self.arms)

        # look at neighbors before waking up?

        # robots[first_robot].get_neighbors()
        for i in range(iterations):
            if i == (iterations - 1):
                self.change_state_contagion(robots, sleep_time, True)
                curr_state = 'FINAL: '
                self.print_status(robots)
                # for robot in robots:
                #     curr_state = curr_state + robot.get_status() + ' '
                # print(curr_state)
            else:
                self.change_state_contagion(robots, sleep_time, False)
                self.print_status(robots)
                # curr_state = ''
                # for robot in robots:
                #     curr_state = curr_state + robot.get_status() + ' '
                # print(curr_state)


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


def call_sound(client, sound_states, sleep_time):
    # print(sound_states)
    client.send_message('arms', sound_states)
    time.sleep(sleep_time)

def call_dances(dances, arms, alive, dead, living, dying):
    t1 = threading.Thread(target=alive_dance, args=([alive], dances, arms))
    t2 = threading.Thread(target=dead_dance, args=([dead], dances, arms))
    t3 = threading.Thread(target=living_dance, args=([living], dances, arms))
    t4 = threading.Thread(target=dying_dance, args=([dying], dances, arms))
    t5 = threading.Thread(target=first_birth_dance, args=([dying], dances, arms))
    t6 = threading.Thread(target=first_death_dance, args=([dying], dances, arms))

    # start threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()


def alive_dance(robots, dances, arms):
    return
    play_dances_gameoflife.playDance(3, robots, dances, arms)
    ### ADD PROPER DANCE NUMBER ONCE YOU RUN THE CSVS!!!!


def dead_dance(robots, dances, arms):
    return
    play_dances_gameoflife.playDance(4, robots, dances, arms)
    ### ADD PROPER DANCE NUMBER ONCE YOU RUN THE CSVS!!!!


def living_dance(robots, dances, arms):
    return
    play_dances_gameoflife.playDance(0, robots, dances, arms)
    ### ADD PROPER DANCE NUMBER ONCE YOU RUN THE CSVS!!!!


def dying_dance(robots, dances, arms):
    return
    play_dances_gameoflife.playDance(5, robots, dances, arms)
    ### ADD PROPER DANCE NUMBER ONCE YOU RUN THE CSVS!!!!

def first_birth_dance(robots, dances, arms):
    return
    play_dances_gameoflife.playDance(1, robots, dances, arms)

def first_death_dance(robots, dances, arms):
    return
    play_dances_gameoflife.playDance(2, robots, dances, arms)

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
    iterations = 3
    first_robot = 0
    game.run_game_contagion(robots, first_robot, iterations, 4)


def test_without_arms():
    # start = time.time()
    robots = init_robots()
    game = Game(robots, [], [])
    # iterations = 10
    # game.init_audio('Joy.wav', 'Sadness.wav')
    # game.run_game(robots, 4)
    start_alive = [0, 3, 7]
    start_dead = [1, 2, 4, 5, 6, 8]
    game.run_game(robots, 4, start_alive, start_dead)
    # first_robot = randrange(10)
    # game.run_game_contagion(robots, 0, 6, 5)
    # first_robot = randrange(10)
    # game.run_game_contagion(robots, first_robot, 6, 3)
    # first_robot = randrange(10)
    # game.run_game_contagion(robots, first_robot, 6, 1)



test_without_arms()








