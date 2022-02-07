import socket
from xarm.wrapper import XArmAPI
import numpy as np
from threading import Thread
import time
from pythonosc import udp_client
import os
import sys
import time
import csv
import pdb
from queue import Queue
from threading import Thread
import time
import random

def setup():
    for a in arms:
        a.set_simulation_robot(on_off=False)
        # a.motion_enable(enable=True)
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
        a.set_servo_angle(angle=[0.0, 0.0, 0.0, 1.57, 0.0, 0, 0.0], wait=False, speed=0.4, acceleration=0.25,
                          is_radian=True)
# gerd = XArmAPI('192.168.1.208')
arm2 = XArmAPI('192.168.1.244')
arm3 = XArmAPI('192.168.1.203')
arm4 = XArmAPI('192.168.1.236')
arm5 = XArmAPI('192.168.1.226')
arm6 = XArmAPI('192.168.1.242')
arm7 = XArmAPI('192.168.1.215')
arm8 = XArmAPI('192.168.1.234')
arm9 = XArmAPI('192.168.1.237')
arm10 = XArmAPI('192.168.1.204')

arms = [arm2, arm3, arm4, arm5, arm6, arm7, arm8, arm9, arm10]
totalArms = len(arms)

if __name__ == '__main__':
    gerd = XArmAPI('192.168.1.208')
    arm = [gerd]
    newsetup()
    setup()
    repeat = input("do we need to repeat? [y/n]")
    if repeat == 'y':
        newsetup()
        setup()



# a two element klist first number joint, the angle of the joint
UDP_IP = "192.168.1.73"
UDP_PORT = 7980
while True:
    # update the message
    IP = "192.168.1.73"
    PORT_TO_MAX = 7980
    message = [0, 0]
    for b in range(6):
        message[0] = b + 1
        message[1] = gerd.angles[b]
        # time.sleep(1)
        print(message)
        client = udp_client.SimpleUDPClient(IP, PORT_TO_MAX)
        client.send_message('arms', message)
    for c in arms:
        j = [0, 0, 0, 0, 0, 0, 0]
        j[1] = gerd.angles[1]
        j[2] = gerd.angles[2]
        j[3] = gerd.angles[3]
        j[4] = gerd.angles[4]
        j[5] = gerd.angles[5]
        j[6] = gerd.angles[6]
        time.sleep(0.05)
        c.set_servo_angle(angle=j, wait=False, speed=20, acceleration=5, is_radian=False)
