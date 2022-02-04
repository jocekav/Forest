import socket
from xarm.wrapper import XArmAPI
import numpy as np
from threading import Thread
import time
from pythonosc import udp_client
import struct
import os
import sys
import time
import csv
import pdb
import queue
from queue import Queue
from threading import Thread
import time
import random

#Rose Script functions
def setup():
    for a in arms:
        a.set_simulation_robot(on_off=False)
        a.motion_enable(enable=True)
        a.clean_warn()
        a.clean_error()
        a.set_mode(0)
        a.set_state(0)
        a.set_servo_angle(angle=[0.0, 0.0, 0.0, 1.57, 0.0, 0, 0.0], wait=False, speed=0.4, acceleration=0.25,
                          is_radian=True)
def newsetup():
    for a in arm:
        a.set_simulation_robot(on_off=False)
        a.motion_enable(enable=True)
        a.clean_warn()
        a.clean_error()
        a.set_mode(2)
        a.set_state(0)
        #a.set_servo_angle(angle=[0.0, 0.0, 0.0, 1.57, 0.0, 0, 0.0], wait=False, speed=0.4, acceleration=0.25,
                          #is_radian=True)

#Michaels scripts functions
def setup2():
    for a in arms2:
        a.set_simulation_robot(on_off=False)
        a.motion_enable(enable=True)
        a.clean_warn()
        a.clean_error()
        a.set_mode(0)
        a.set_state(0)
        # a.set_servo_angle(angle=[0.0, 0.0, 0.0, 1.57, 0.0, 0, 0.0], wait=True, speed=0.4, acceleration=0.25,
        #                   is_radian=True)
        a.set_position(*[121, -1, 585, -2, -86, -178], wait=False)


def findDistance(origin, newpoint):
    distance = ((((newpoint[0] - origin[0]) ** 2) + ((newpoint[1] - origin[1]) ** 2)) ** 0.5)
    return distance


gerd = XArmAPI('192.168.1.208')
arm2 = XArmAPI('192.168.1.244')
arm3 = XArmAPI('192.168.1.203')
arm4 = XArmAPI('192.168.1.236')
arm5 = XArmAPI('192.168.1.226')
arm6 = XArmAPI('192.168.1.242')
arm7 = XArmAPI('192.168.1.215')
arm8 = XArmAPI('192.168.1.234')
# arm9 = XArmAPI('192.168.1.237')
arm10 = XArmAPI('192.168.1.204')

arms = [gerd, arm4, arm5, arm7, arm8, arm10]
arm = [arm6, arm2, arm3]
totalArms = len(arms)


if __name__ == '__main__':

    #sc is script choice, 1 is roses
    sc = 1
    # gerd = XArmAPI('192.168.1.208')
    newsetup()
    setup()
    repeat = input("do we need to repeat? [y/n]")
    if repeat == 'y':
        newsetup()
        setup()

    # dances = []
    # directory = '/home/forest/Desktop/xArm/Trajectories2/'
    # trajectories = sorted(os.listdir(directory))
    # for filename in trajectories:
    #     if filename.endswith(".csv"):
    #         print(filename)
    #         currentDance = (readFile(os.path.join(directory, filename)))
    #         dances.append(currentDance)
    #         continue

# a two element klist first number joint, the angle of the joint
UDP_IP = "192.168.1.73"
UDP_PORT = 7981
while sc==1:
    # update the message
    client = udp_client.SimpleUDPClient(UDP_IP, UDP_PORT)
    MESSAGE = [0, 0]
    for b in range(6):
        MESSAGE[0] = b+1
        MESSAGE[1] = arm2.angles[b]
        client.send_message('arms', MESSAGE)
    MESSAGE2 = [0, 0]
    for r in range(6):
        MESSAGE2[0] = r+1
        MESSAGE2[1] = arm6.angles[r]
        client.send_message('arms2', MESSAGE2)
    MESSAGE3 = [0, 0]
    for s in range(6):
        MESSAGE3[0] = s+1
        MESSAGE3[1] = arm3.angles[s]
        client.send_message('arms3', MESSAGE3)
        # client = udp_client.SimpleUDPClient(UDP_IP, UDP_PORT)
        # client.send_message('arms', MESSAGE)
        # client.send_message('arms2', MESSAGE2)
        # client.send_message('arms3', MESSAGE3)
        #print(MESSAGE3)
    # playDance(dances[Dance])

    # for c in arms:
    j = [0,0,0,0,0,0,0]
    j[0] = arm2.angles[0]
    j[1] = arm2.angles[1]
    j[2] = arm2.angles[2]
    j[3] = arm2.angles[3]
    j[4] = arm2.angles[4]
    j[5] = arm2.angles[5]
    j[6] = arm2.angles[6]
    negj = [0,0,0,0,0,0,0]
    negj[0] = arm2.angles[0]
    negj[1] = arm2.angles[1]
    negj[2] = -arm2.angles[2]
    negj[3] = arm2.angles[3]
    negj[4] = -arm2.angles[4]
    negj[5] = arm2.angles[5]
    negj[6] = arm2.angles[6]
    x = [0,0,0,0,0,0,0]
    x[1] = arm3.angles[1]
    x[2] = arm3.angles[2]
    x[3] = arm3.angles[3]
    x[4] = arm3.angles[4]
    x[5] = arm3.angles[5]
    x[6] = arm3.angles[6]
    negx = [0,0,0,0,0,0,0]
    negx[1] = arm3.angles[1]
    negx[2] = -arm3.angles[2]
    negx[3] = arm3.angles[3]
    negx[4] = -arm3.angles[4]
    negx[5] = arm3.angles[5]
    negx[6] = arm3.angles[6]
    y = [0,0,0,0,0,0,0]
    y[1] = arm6.angles[1]
    y[2] = arm6.angles[2]
    y[3] = arm6.angles[3]
    y[4] = arm6.angles[4]
    y[5] = arm6.angles[5]
    y[6] = arm6.angles[6]
    negy = [0,0,0,0,0,0,0]
    negy[1] = arm6.angles[1]
    negy[2] = -arm6.angles[2]
    negy[3] = arm6.angles[3]
    negy[4] = -arm6.angles[4]
    negy[5] = arm6.angles[5]
    negy[6] = arm6.angles[6]
    time.sleep(0.006)
    gerd.set_servo_angle(angle=j, wait=False, speed=40, acceleration=10, is_radian=False)
    arm5.set_servo_angle(angle=negj, wait=False, speed=40, acceleration=10, is_radian=False)
    arm4.set_servo_angle(angle=x, wait=False, speed=40, acceleration=10, is_radian=False)
    arm7.set_servo_angle(angle=negx, wait=False, speed=40, acceleration=10, is_radian=False)
    arm8.set_servo_angle(angle=y, wait=False, speed=40, acceleration=10, is_radian=False)
    arm10.set_servo_angle(angle=negy, wait=False, speed=40, acceleration=10, is_radian=False)

    # print(j[0])
    if(j[0] > 70):
        sc = 2
        print("ahhhh")
        # c.set_servo_angle(angle=j, wait=False, speed=20, acceleration=5, is_radian=False)

print("time4script2")
time.sleep(3)
print("script2starting")

arms2 = [gerd, arm2, arm3, arm4, arm5, arm6, arm7, arm8, arm10]
setup2()
repeat = input("do we need to repeat? [y/n]")
if repeat == 'y':
    setup2()
print("Setup Finished")

for a in arms2:
    a.set_mode(1)
    a.set_state(0)
#[[1.417, 0.92], [1.748, 1.276], [2.503, 1.897], [3.92, 2.906], [2.93, 0.81], [3.78, 1.205], [4.861, 1.654], [4.30, 0.742], [5.48, 1.028]])
coordinates = np.array(
    [[1.417, 1.84], [1.748, 2.552], [2.503, 3.794], [3.92, 5.812], [2.93, 1.62], [3.78, 2.41], [4.861, 3.308], [4.30, 1.484], [5.48, 2.056]])
xValue = []
yValue = []
coordinateScale = []
for c in coordinates:
    x = np.interp(c[0], (0, 6), (0, 127))
    y = np.interp(c[1], (0, 6), (0, 127))
    coordinateScale.append([x, y])

# print("coordscale", coordinateScale)

distances = []
for s in coordinateScale:
    d = findDistance(s, [0, 0])
    distances.append(d)
lastdist = distances


# print(lastdist)

# def changeDir():
#     while True:
#         angle = int(input("desired angle"))
#         q.put(angle)
def UDP():
    print("started!")
    x = [0, 0]
    xP = [0, 0]
    while True:
        IP = "192.168.1.2"
        # IP = "10.0.0.1"
        PORT_TO_MAX = 7980

        message = [2, 2]  # Message is [robot to make sound, track in playlist to play]
        # list can be anything
        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        sock.bind((IP, PORT_TO_MAX))
        # sock.set t(None)
        sock.settimeout(None)
        data, server = sock.recvfrom(1024)
        received = []

        if data.startswith(b'int'):
            received = struct.unpack('!I', data[-4:])[0]
        elif data.startswith(b'list'):
            for a in range(len(x)):
                if a == 0:
                    x[a + 1] = int((repr(struct.unpack('!I', data[-4:])[0])))
                else:
                    x[a - 1] = int((repr(struct.unpack('!I', data[-(4 * (a + 1)):-(4 * a)])[0])))

            # x[0] = (repr(struct.unpack('!I', data[-4:])[0]))
            # print(repr(struct.unpack('!I', data[-8:-4])[0]))
            # print(repr(struct.unpack('!I', data[-12:-8])[0]))  # eight
            # print(repr(struct.unpack('!I', data[-16:-12])[0])) # seven
            # print(repr(struct.unpack('!I', data[-20:-16])[0]))  # six
            # print(repr(struct.unpack('!I', data[-24:-20])[0]))  # fifth
            # print(repr(struct.unpack('!I', data[-28:-24])[0]))  # fourth
            # print(repr(struct.unpack('!I', data[-32:-28])[0]))  # third
            # print(repr(struct.unpack('!I', data[-36:-32])[0]))  # second
            # print(repr(struct.unpack('!I', data[-40:-36])[0]))  # First
        else:
            received = data.decode('utf-8')

        # if (x - xP) != 0:
        #     xP = x
        #     print("switch", x)
        # if (x[1] - xP[1]) != 0:
        #     xP = x
        #     print("switch", x)

        # print(x, xP)
        print(x)
        # print("sent!")
        q0.put(x)


def livetraj(inq, robot):
    tf = 2
    # q i
    # 0.2 * np.floor(xi / 0.2)
    # range is 200 to -200
    t0 = 0
    t = t0
    q_i = 0
    q_dot_i = 0
    q_dot_f = 0
    q_dotdot_i = 0
    q_dotdot_f = 0
    t_array = np.arange(0, tf, 0.006)
    p = 0
    v = 0
    a = 0
    dancet = 0
    while True:
        goal = inq.get()
        print("moving", robot)
        q_i = p
        q_dot_i = 0
        q_dotdot_i = 0
        q_f = goal
        i = 0
        # or dancet != 0
        while (i <= len(t_array) or dancet != 0):
            start_time = time.time()
            if inq.empty() == False:
                goal = inq.get()
                print("switch bot", robot)
                q_i = p
                q_dot_i = v
                q_dotdot_i = 0
                q_f = goal
                i = 0
                # IF YOU WANT TO ADD SPEED CHANGES THEN SWAP THE ABOVE LINES WITH THE BELOW LINES
                # # q should input an array of [*absolute* position of joint, time(in seconds) to reach there]
                # q_f = goal[0]
                # tf = goal[1]
                # t_array = np.arange(0, tf, 0.006)
                # print("switch")
            if i >= len(t_array):
                t = tf
                # if at end, append more time
                # t_array = np.append(t_array, tf+0.006)
                # print(t_array)
                dancet += 0.006
            else:
                t = t_array[i]
                dancet = t

            a0 = q_i
            a1 = q_dot_i
            a2 = 0.5 * q_dotdot_i
            a3 = 1.0 / (2.0 * tf ** 3.0) * (20.0 * (q_f - q_i) - (8.0 * q_dot_f + 12.0 * q_dot_i) * tf - (
                    3.0 * q_dotdot_f - q_dotdot_i) * tf ** 2.0)
            a4 = 1.0 / (2.0 * tf ** 4.0) * (30.0 * (q_i - q_f) + (14.0 * q_dot_f + 16.0 * q_dot_i) * tf + (
                    3.0 * q_dotdot_f - 2.0 * q_dotdot_i) * tf ** 2.0)
            a5 = 1.0 / (2.0 * tf ** 5.0) * (12.0 * (q_f - q_i) - (6.0 * q_dot_f + 6.0 * q_dot_i) * tf - (
                    q_dotdot_f - q_dotdot_i) * tf ** 2.0)

            p = a0 + a1 * t + a2 * t ** 2 + a3 * t ** 3 + a4 * t ** 4 + a5 * t ** 5
            v = a1 + 2 * a2 * t + 3 * a3 * t ** 2 + 4 * a4 * t ** 3 + 5 * a5 * t ** 4
            a = 2 * a2 + 6 * a3 * t + 12 * a4 * t ** 2 + 20 * a5 * t ** 3

            # amplitude returns sin wave to oscillate over

            # print(amplitude)
            # p needs to be less than 400 for safety
            if (p > 380):
                p = 380
                print("More than 380")

            amplitude = np.sin(dancet * 5) * (p / 60)
            amplitude2 = np.sin(dancet * 2.5) * (p / 50)
            amplitude3 = np.sin(dancet * 1.25) * (p / 40)
            amplitude4 = np.sin(dancet * 5) * (p / 40)
            amplitude5 = np.sin(dancet * 2.5) * (p / 30)
            amplitude6 = np.sin(dancet * 1.25) * (p / 20)
            amplitude7 = np.sin(dancet * 5) * (p / 20)

            #mvpose = [121, -1, 585 + p, -2 + amplitude2, -86 + amplitude2, -178 + amplitude]  # x y z roll pitch yaw
            # print(mvpose)
            if(robot == 0):
                mvpose = [121, -1, 585 + p, -2 + amplitude5, -86 + amplitude4, -178] #head u shape
            if(robot == 1):
                mvpose = [121, -1, 585 + p, -2 + amplitude2, -86 + amplitude2, -178 + amplitude]
            if(robot == 2):
                mvpose = [121, -1, 585 + p, -2 + amplitude2, -86 + amplitude2, -178 + amplitude]
            if(robot == 3):
                mvpose = [121, -1 - amplitude, 585 + p/4, -2 + amplitude4, -86, -178] #no nod
            if(robot == 4):
                mvpose = [121 + amplitude7, -1, 585 + p, -2 + amplitude6, -86 + amplitude4, -178] #sway back and nod
            if(robot == 5):
                mvpose = [121, -1, 585 + p, -2 + amplitude2, -86 + amplitude2, -178 + amplitude]
            if(robot == 6):
                mvpose = [121 + p/2, -1 + amplitude5, 585, -2, -86, -178 + amplitude5] #sway for a pet
            if(robot == 7):
                mvpose = [121, -1, 585 + p, -2 + amplitude5, -86 + amplitude4, -178] #head u shape
            if(robot == 8):
                mvpose = [121 - p/2, -1, 585, -2, -86, -178 + amplitude6] #scaredy
            # print("robot", robot, "position", p)
            # print(tf)

            arms2[robot].set_servo_cartesian(mvpose, speed=100, mvacc=2000)
            tts = time.time() - start_time
            sleep = 0.006 - tts

            if tts > 0.006:
                sleep = 0

            # print(tts)
            time.sleep(sleep)
            i += 1
            # if t == 1:
            # print(t, p, v, a)
        print("done")


q0 = queue.Queue()
t = Thread(target=UDP)
# t2 = Thread(target=changeDir)
# t3 = Thread(target=livetraj(q))
# #t2.start()
# t3.start()
t.start()
i = 0

q = Queue()
q1 = Queue()
q2 = Queue()
q3 = Queue()
q4 = Queue()
q5 = Queue()
q6 = Queue()
q7 = Queue()
q8 = Queue()

quay = [q, q1, q2, q3, q4, q5, q6, q7, q8]

t2 = Thread(target=livetraj, args=(q, 0,))
t3 = Thread(target=livetraj, args=(q1, 1,))
t4 = Thread(target=livetraj, args=(q2, 2,))
t5 = Thread(target=livetraj, args=(q3, 3,))
t6 = Thread(target=livetraj, args=(q4, 4,))
t7 = Thread(target=livetraj, args=(q5, 5,))
t8 = Thread(target=livetraj, args=(q6, 6,))
t9 = Thread(target=livetraj, args=(q7, 7,))
t10 = Thread(target=livetraj, args=(q8, 8,))
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

while True:
    # IP = "192.168.1.1"
    # print("start")
    # # IP = "10.0.0.1"
    # PORT_TO_MAX = 7980
    # sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # sock.bind((IP, PORT_TO_MAX))
    # data, server = sock.recvfrom(1024)
    # received = []
    # xP = [0,0]
    # x = [0, 0]
    # if data.startswith(b'int'):
    #     received = struct.unpack('!I', data[-4:])[0]
    # elif data.startswith(b'list'):
    #     for a in range(len(x)):
    #         if a == 0:
    #             x[a] = (repr(struct.unpack('!I', data[-4:])[0]))
    #         else:
    #             x[a] = (repr(struct.unpack('!I', data[-(4 * (a + 1)):-(4 * a)])[0]))
    # else:
    #     received = data.decode('utf-8')
    #
    # if x[0] != xP[0] or x[1] != xP[1]:
    #     x = xP
    x = q0.get()

    # print("myxy", x)
    for s in range(len(coordinateScale)):
        d = findDistance(coordinateScale[s], x)
        if abs(lastdist[s] - d) > 10:
            distances[s] = d
            # 40 instead of 127 to only have close interactions
            # 10 instead of 0 to make it so max height is reached easier
            height = np.interp(d, (10, 40), (400, 0))
            if height > 400:
                height = 400
            quay[s].put(height)
            lastdist[s] = d

    # dNP = np.array(distances)
    # heights = np.interp(dNP, (0, 127), (400, 0))
    # print(heights)
    # for a in range(len(heights)):
    #     heights