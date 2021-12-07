import os
import sys
import time
import csv
import pdb
from queue import Queue
from threading import Thread
import time
import math
import numpy as np
import game_of_life_music

global play_state
play_state = 'combine'


def cvt(path):
    return_vector = []
    for i in range(7):
        return_vector.append(float(path[i]))
    return return_vector

def playDance(step, robots, dances, arms):
    global play_state
    state = play_state
    if state == "combine":
        playDance_combo(step, robots, dances, arms)
    elif state == 'pattern_a':
        playDance_same(step, robots, dances, arms, 'pattern_a')
    elif state == 'pattern_b':
        playDance_same(step, robots, dances, arms, 'pattern_b')

def playDance_same(step, robots, dances, arms, type):
    print('Current csv call: ' + str(step))
    print(type)
    if type == 'pattern_a':
        step = dances[step]
    elif type == 'pattern_b':
        step = dances[step + 6]

    length = len(step)

    # for a in range (3):
    #     print(2-a)
    #     time.sleep(1)
    # print(robots)
    for i in range(length):
        start_time = time.time()
        # board.digital[4].mode = pyfirmata.INPUT
        # board.digital[2].mode = pyfirmata.INPUT
        # red = board.digital[4].read()

        j_angles = (step[i])
        # b=6k
        # arms[b].set_servo_angle_j(angles=j_angles[(b * 7):((b + 1) * 7)], is_radian=False)
        if isinstance(robots, int):
            arms[robots].set_servo_angle_j(angles=j_angles, is_radian=False)
        else:
            for b in robots[0]:
                arms[b].set_servo_angle_j(angles=j_angles, is_radian=False)
        tts = time.time() - start_time
        sleep = 0.006 - tts

        if tts > 0.006:
            sleep = 0

        time.sleep(sleep)

def playDance_combo(step, robots, dances, arms):
    print('Current csv call: ' + str(step))
    step_a = dances[step]
    step_b = dances[step + 6]

    length_a = len(step_a)
    length_b = len(step_b)
    longer = 'a'
    if length_a > length_b:
        length = length_a
    else:
        length = length_b
        longer = 'b'
    # for a in range (3):
    #     print(2-a)
    #     time.sleep(1)
    # print(robots)
    for i in range(length):
        start_time = time.time()
        # board.digital[4].mode = pyfirmata.INPUT
        # board.digital[2].mode = pyfirmata.INPUT
        # red = board.digital[4].read()
        if longer == 'a':
            if i <= length_b:
                j_angles_b = (step_b[i])
            else:
                j_angles_b = 'done'
            j_angles_a = (step_a[i])

        elif longer == 'b':
            if i <= length_a:
                j_angles_a = (step_a[i])
            else:
                j_angles_a = 'done'
            j_angles_b = (step_b[i])

        if isinstance(robots, int):
            if robots < 4 or robots > 8:
                if j_angles_a != 'done':
                    arms[robots].set_servo_angle_j(angles=j_angles_a, is_radian=False)
            else:
                if j_angles_b != 'done':
                    arms[robots].set_servo_angle_j(angles=j_angles_b, is_radian=False)
        else:
            for b in robots[0]:
                if b < 4 or b > 8:
                    if j_angles_a != 'done':
                        arms[b].set_servo_angle_j(angles=j_angles_a, is_radian=False)
                else:
                    if j_angles_b != 'done':
                        arms[b].set_servo_angle_j(angles=j_angles_b, is_radian=False)
        tts = time.time() - start_time
        sleep = 0.006 - tts

        if tts > 0.006:
            sleep = 0

        # print(tts)
        time.sleep(sleep)
    # print(step)
    # print(time.time())


def readFile(csvFile):
    dance_steps = []
    with open(csvFile, newline='') as csvfile:
        paths_reader_j = csv.reader(csvfile, delimiter=',', quotechar='|')
        for path in paths_reader_j:
            dance_steps.append(cvt(path))
    return dance_steps


def setup():
    for a in arms:
        a.set_simulation_robot(on_off=False)
        # a.motion_enable(enable=True)
        a.clean_warn()
        a.clean_error()
        a.set_mode(0)
        a.set_state(0)
        a.set_servo_angle(angle=[0.0, 0.0, 0.0, 1.57, 0.0, 0, 0.0], wait=False, speed=0.2, acceleration=0.25,
                          is_radian=True)
def run(start):
    global play_state
    if start == 'a':
        #game_of_life_music.init_and_run(dances, arms)
        play_state = 'pattern_a'
        print(play_state)
        print("iter 1" + play_state)
        game_of_life_music.init_and_run_contagion(dances, arms, 0)
        setup()
    elif start == 'b':
        # game_of_life_music.init_and_run(dances, arms)
        play_state = 'pattern_b'
        print(play_state)
        print("iter 2" + play_state)
        game_of_life_music.init_and_run_contagion(dances, arms, 3)
        setup()
    elif start == 'c':
        play_state = 'combine'
        print(play_state)
        print("iter 3" + play_state)
        game_of_life_music.init_and_run_contagion(dances, arms, 5)
        setup()

if __name__ == "__main__":
    ROBOT = "xArms"
    PORT = 5004

    sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
    from xarm.wrapper import XArmAPI
    arm1 = XArmAPI('192.168.1.208')
    arm2 = XArmAPI('192.168.1.244')
    arm3 = XArmAPI('192.168.1.203')
    arm4 = XArmAPI('192.168.1.236')
    arm5 = XArmAPI('192.168.1.226')
    arm6 = XArmAPI('192.168.1.242')
    arm7 = XArmAPI('192.168.1.215')
    arm8 = XArmAPI('192.168.1.234')
    # arm9 = XArmAPI('192.168.1.237')
    arm10 = XArmAPI('192.168.1.204')


    arms = [arm1, arm2, arm3, arm4, arm5, arm6, arm7, arm8, arm10]
    # arms = [arm1]
    totalArms = len(arms)
    # totalArms = 1

    # directory = '/home/codmusic/Desktop/FOREST/game_of_life_csvs'
    directory = '/home/codmusic/Desktop/FOREST/game_of_life_total_csvs'

    dances = []
    trajectories = sorted(os.listdir(directory))
    s = time.time()
    for filename in trajectories:
        if filename.endswith(".csv"):
            print(filename)
            currentDance = (readFile(os.path.join(directory, filename)))
            dances.append(currentDance)
            continue
    e = time.time()
    print("the loading time is", (e-s))
    setup()
    repeat = input("do we need to repeat? [y/n]")
    if repeat == 'y':
        print('state:', arm1.state)
        print('mode:', arm1.mode)
        setup()
    for a in arms:
        a.set_mode(1)
        a.set_state(0)


    start = input("Type pattern a, b, or c")
    run(start)

