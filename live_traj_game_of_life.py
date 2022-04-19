from random import randint
import numpy as np
# import trajectory_generation as traj
import csv

import threading
import queue
import time
from pythonosc import udp_client
from random import randrange

from xarm.wrapper import XArmAPI

def setup(arms):
    for a in arms:
        a.set_simulation_robot(on_off=False)
        a.motion_enable(enable=True)
        a.clean_warn()
        a.clean_error()
        a.set_mode(0)
        a.set_state(0)
        a.set_servo_angle(angle=[0.0, 0.0, 0.0, 1.57, 0.0, 0, 0.0], wait=False, speed=0.4, acceleration=0.25,
                          is_radian=True)

def run_robots():
    arm1 = XArmAPI('192.168.1.203')
    arm3 = XArmAPI('192.168.1.236')
    arm5 = XArmAPI('192.168.1.234')
    arm7 = XArmAPI('192.168.1.208')
    arm9 = XArmAPI('192.168.1.211')
    arms = [arm1, arm3, arm5, arm7, arm9]
    setup(arms)
    repeat = input("do we need to repeat? [y/n]")
    if repeat == 'y':
        for a in arms:
            print('state:', arm1.state)
            print('mode:', arm1.mode)
        setup()
    for a in arms:
        a.set_mode(1)
        a.set_state(0)

class Robot:
    def __init__(self, num):
        self.status = 'Dead'
        self.num = num
        self.dance = []
        self.dance_t = []
        self.core_neighbor = False
        self.joint_1 = 0
        self.joint_2 = 0
        self.joint_3 = 0
        self.joint_4 = 90
        self.joint_5 = 0
        self.joint_6 = 0
        self.joint_7 = 0
        self.live_pos = [0, 0, 0, 90, 0, 0, 0]
        self.que = queue.Queue()
        self.f = open(('live_traj' + str(num) + '.csv'), 'w')

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def get_neighbors(self):
        return self.neighbors
    
    def get_core_neighbor(self):
        return self.core_neighbor
    
    def set_core_neighbor(self, state):
        self.core_neighbor = state

    def set_neighbor_angle(self, angles):
        self.neighbor_angle = angles

    def get_neighbor_angle(self):
        return self.neighbor_angle

    def get_num(self):
        return self.num

    def set_die(self, first=False):
        self.status = 'Dead'
        self.death()

    def set_alive(self):
        self.status = 'Alive'
        self.birth()

    def set_living(self):
        self.status = 'Living'
        self.living()

    def set_dying(self):
        self.status = 'Dying'
        self.dying()

    def set_inactive(self):
        self.status = 'Inactive'
        self.inactive()

    def set_first_birth(self):
        self.status = 'First Birth'
        self.first_birth()

    def set_first_death(self):
        self.status = 'First Death'
        self.first_death()

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
    
    def add_to_que(self, angles):
        self.que.put(angles)

    def get_que(self):
        return self.que

    def get_pos(self):
        return [self.joint_1, self.joint_2, self.joint_3, self.joint_4, self.joint_5, self.joint_6, self.joint_7]

    def birth(self):
        birth_move = np.array([0, (self.joint_2 - 50), 0, (self.joint_4 + 60), 0, 0, 0], dtype=object)
        self.update_joints(birth_move)
        self.add_to_que(birth_move)

    def first_birth(self):
        birth_move = np.array([0, (self.joint_2 - 20), 0, (self.joint_4 + 30), 0, 0, 0])
        self.update_joints(birth_move)
        self.add_to_que(birth_move)

    def death(self):
        death_move = np.array([0, (self.joint_2 + 50), 0, (self.joint_4 - 60), 0, 0, 0], dtype=object)
        self.update_joints(death_move)
        self.add_to_que(death_move)

    def first_death(self):
        death_move = np.array([0, (self.joint_2 + 20), 0, (self.joint_4 - 30), 0, 0, 0])
        self.update_joints(death_move)
        self.add_to_que(death_move)

    def living(self):
        living_move_1 = np.array([0, 0, (self.joint_3 - 15), 0, 0, 0, 0], dtype=object)
        living_move_2 = np.array([0, 0, (self.joint_3 + 15), 0, 0, 0, 0], dtype=object)

        self.update_joints(living_move_1)
        self.add_to_que(living_move_1)
        self.update_joints(living_move_2)
        self.add_to_que(living_move_2)

    def dying(self):
        dying_move_1 = np.array([(self.joint_1 + 20), 0, 0, 0, 0, 0, 0], dtype=object)
        dying_move_2 = np.array([(self.joint_1 - 40), 0, 0, 0, 0, 0, 0], dtype=object)
        dying_move_3 = np.array([(self.joint_1 + 20), 0, 0, 0, 0, 0, 0], dtype=object)

        self.update_joints(dying_move_1)
        self.add_to_que(dying_move_1)
        self.update_joints(dying_move_2)
        self.add_to_que(dying_move_2)
        self.update_joints(dying_move_3)
        self.add_to_que(dying_move_3)

    def rotate(self, angle, action):
        if action == "death":
            rotate_move = np.array([-(self.joint_1), 0, 0, 0, 0, 0, 0], dtype=object)

        if action == "birth":
            rotate_move = np.array([angle, 0, 0, 0, 0, 0, 0], dtype=object)

        self.update_joints(rotate_move)
        self.add_to_que(rotate_move)


    def update_joints(self, new_angles):
        self.joint_1 = new_angles[0]
        self.joint_2 = new_angles[1]  
        self.joint_3 = new_angles[2]
        self.joint_4 = new_angles[3]
        self.joint_5 = new_angles[4]
        self.joint_6 = new_angles[5]
        self.joint_7 = new_angles[6]

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
            raise ValueError("Joint 5 Out of Bounds")
        else:
            self.joint_7 += new_angles[6] 

    def change_joints(self):
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

            # arm.set_servo_angle_j(angles=p, is_radian=False)
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

class Game:

    def __init__(self, robots):
        # for robot in robots:
        #     random = randint(0, 2)
        #     if random == 1:
        #         robot.set_alive()
        #     else:
        #         robot.set_die()
        self.setup_music()

    def setup_music(self):
        IP = "192.168.2.31"
        # IP = "192.168.1.73"
        # IP = "128.6.27.43"
        PORT_TO_MAX = 7980
        # self.client = udp_client.SimpleUDPClient(IP, PORT_TO_MAX)
    

    def revive(self, robots):
        print("revive")
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
            random = randint(0, 2)
            if random == 1:
                robot.set_alive()
                robot_num = robot.get_num()
                birth_ids.append(robot_num)
                sound_states[robot_num * 2] = 1
                sound_states[(robot_num * 2) + 1] = .75
            else:
                robot.set_dying()
                robot_num = robot.get_num()
                dying_ids.append(robot_num)
                sound_states[robot_num * 2] = 4
                sound_states[(robot_num * 2) + 1] = .25

        # call_sound(self.client, sound_states, 0)
        # call_dances(self.dances, self.arms, self.play_state, birth_ids, kill_ids, living_ids, dying_ids, first_birth_ids)

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
                if neighbor[0].is_alive():
                    live_neighbors += 1

            curr_robot_living = robot.is_alive()

            move = ""
            if curr_robot_living:
                if live_neighbors == 0:
                    kill.append(robot)
                    move = "death"
                elif live_neighbors >= half_neighbors:
                    kill.append(robot)
                    move = "death"
                else:
                    living.append(robot)
            else:
                if live_neighbors >= half_neighbors:
                    birth.append(robot)
                    move = "birth"
                else:
                    dying.append(robot)
                    death_count += 1

        # if move == "birth" or move == "death":
        #     for robot in robots:
        #         neighbors = robot.get_neighbors()
        #         # has_rotate = false
        #         if move == "birth":
        #             robot.rotate(neighbors[0][1], move)
        #         if move == "death":
        #             robot.rotate(0, move)
        
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

        # call_sound(self.client, sound_states, sleep_time)

        self.move_state(robots)


    def run_game(self, robots, iterations):
        birth = []
        death = []

        for robot in robots:
            print("Robot: " + str(robot.get_num()) + " Position: " + str(robot.get_pos()) + " " +
                  str(robot.get_status()))

            random = randint(0, 2)
            if random == 1:
                robot.set_first_birth()
                birth.append(robot)
            else:
                robot.set_first_death()
                death.append(robot)

        sound_states = np.zeros(20)

        curr_state = ''
        for robot in robots:
            print("Robot: " + str(robot.get_num()) + " Position: " + str(robot.get_pos()) + " " +
                  str(robot.get_status()))
            # curr_state = curr_state + robot.get_status() + ' '
        print(curr_state)

        for robot in birth:
            sound_states[robot.get_num() * 2] = 1
            sound_states[(robot.get_num() * 2) + 1] = .75
        for robot in death:
            sound_states[robot.get_num() * 2] = 2
            sound_states[(robot.get_num() * 2) + 1] = .5

        # call_sound(self.client, sound_states, sleep_time)
        self.move_state(robots)

        for i in range(iterations):
            self.change_state(robots)
            curr_state = ''
            for robot in robots:
                curr_state = curr_state + robot.get_status() + ' '
                print("Robot: " + str(robot.get_num()) + " Position: " + str(robot.get_pos()) + " " +
                      str(robot.get_status()))
            # print(curr_state)

    def change_state_contagion(self, robots, sleep_time):
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
            return


    def run_game_contagion(self, robots, first_robot, iterations, sleep_time):
        for robot in robots:
            robot.set_inactive()
        for robot in first_robot:
            robots[robot].set_first_birth()

        sound_states = np.zeros(20)

        curr_state = ''
        for robot in robots:
            curr_state = curr_state + robot.get_status() + ' '
        print(curr_state)

        for robot in first_robot:
            sound_states[robot * 2] = 1
            sound_states[(robot * 2) + 1] = .75

        # call_sound(self.client, sound_states, sleep_time)
        # #alive_dance(first_robot, self.dances, self.arms)
        # first_birth_dance(first_robot, self.dances, self.arms, self.play_state)

        for robot in robots:
            robot.set_inactive()
        for robot in first_robot:
            robots[robot].set_living()

        curr_state = ''
        for robot in robots:
            curr_state = curr_state + robot.get_status() + ' '
        print(curr_state)

        for robot in first_robot:
            sound_states[robot * 2] = 3
            sound_states[(robot * 2) + 1] = .75

        # call_sound(self.client, sound_states, sleep_time)
        # living_dance(first_robot, self.dances, self.arms, self.play_state)

        # look at neighbors before waking up?

        # robots[first_robot].get_neighbors()

        for i in range(iterations):
            curr_state = ''
            for robot in robots:
                curr_state = curr_state + robot.get_status() + ' '
            print(curr_state)
            self.change_state_contagion(robots, sleep_time)

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

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()

    def call_sound(client, sound_states, sleep_time):
        print(sound_states)
        client.send_message('arms', sound_states)
        time.sleep(sleep_time)


def init_robots():

    ROBOT_1 = Robot(0)
    ROBOT_3 = Robot(2)
    ROBOT_5 = Robot(4)
    ROBOT_7 = Robot(6)
    ROBOT_9 = Robot(8)

    robots = [ROBOT_1, ROBOT_3, ROBOT_5, ROBOT_7, ROBOT_9]
    
    ROBOT_1.set_neighbors([(ROBOT_5, 135)])
    ROBOT_3.set_neighbors([(ROBOT_5, -135)])
    ROBOT_5.set_neighbors([(ROBOT_1, -45), (ROBOT_3, 45), (ROBOT_7, -135), (ROBOT_9, 135)])
    ROBOT_7.set_neighbors([(ROBOT_5, 45)])
    ROBOT_9.set_neighbors([(ROBOT_5, -45)])

    return robots


def init_and_run_wo_robots():
    robots = init_robots()
    game = Game(robots)
    iterations = 2
    game.run_game(robots, iterations)

# def init_and_run():
#     run_robots()
#     robots = init_robots()
#     game = Game(robots)
#     iterations = 2
#     game.run_game(robots, iterations)

if __name__ == '__main__':
    init_and_run_wo_robots()
