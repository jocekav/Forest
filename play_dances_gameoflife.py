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


def cvt(path):
    return_vector = []
    for i in range(7):
        return_vector.append(float(path[i]))
    return return_vector


def playDance(step, robots):
    step = dances[step]
    length = len(step)

    # for a in range (3):
    #     print(2-a)
    #     time.sleep(1)
    for i in range(length):
        start_time = time.time()
        # board.digital[4].mode = pyfirmata.INPUT
        # board.digital[2].mode = pyfirmata.INPUT
        # red = board.digital[4].read()

        j_angles = (step[i])
        # b=6
        # arms[b].set_servo_angle_j(angles=j_angles[(b * 7):((b + 1) * 7)], is_radian=False)

        for b in robots:
            arms[b].set_servo_angle_j(angles=j_angles, is_radian=False)
        tts = time.time() - start_time
        sleep = 0.006 - tts

        if tts > 0.006:
            sleep = 0

        print(tts)
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
        #a.motion_enable(enable=True)
        a.clean_warn()
        a.clean_error()
        a.set_mode(0)
        a.set_state(0)
        a.set_servo_angle(angle=[0.0, 0.0, 0.0, 1.57, 0.0, 0, 0.0], wait=False, speed=0.4, acceleration=0.25,
                          is_radian=True)


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
    arm9 = XArmAPI('192.168.1.237')
    arm10 = XArmAPI('192.168.1.204')


    arms = [arm1, arm2, arm3, arm4, arm5, arm6, arm7, arm8, arm9, arm10]
    totalArms = len(arms)


    directory = '/home/forest/Desktop/xArm/contagion/'
    global dances
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

    # plt.show()
    robots_in_cycle = []
    # dance = int(input("Please Type the Dance"))
    start = int(input("Type 1 to start"))
    if start == 1:
        game_of_life_music.init_and_run()
    # startbot.append(firstbot)

    # endbot = int(input("Please type the finishing Robot"))