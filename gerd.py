import socket
from xarm.wrapper import XArmAPI
import numpy as np
from threading import Thread
import time
from pythonosc import udp_client

def setup():
    for a in arms:
        a.set_simulation_robot(on_off=False)
        a.motion_enable(enable=True)
        a.clean_warn()
        a.clean_error()
        a.set_mode(2)
        a.set_state(0)
        a.set_position(*[121, -1, 785, -2, -86, -178], wait=True)

# gerd = XArmAPI('192.168.1.208')

if __name__ == '__main__':
    gerd = XArmAPI('192.168.1.208')
    arms = [gerd]
    setup()
    repeat = input("do we need to repeat? [y/n]")
    if repeat == 'y':
        setup()


while True:
    IP = "192.168.1.73"
    PORT_TO_MAX = 7980
    message = [0, 0]
    for b in range(6):
        message[0] = b+1
        message[1] = gerd.angles[b]
        # time.sleep(1)
        print(message)
        client = udp_client.SimpleUDPClient(IP, PORT_TO_MAX)
        client.send_message('arms', message)
    # MESSAGE = [0, 0]
    # for b in range(6):
    #     MESSAGE[0] = b+1
    #     MESSAGE[1] = gerd.angles[b]
    # MESSAGE = int(1)
    # print(MESSAGE)
    # client = udp_client.SimpleUDPClient(UDP_IP, UDP_PORT)
    # client.send_message('arms', MESSAGE)
        # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        # sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))