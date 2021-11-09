import wave
# import pyaudio
import numpy as np
from scipy.io.wavfile import read
import io

import simpleaudio as sa


def panner(angle, left, right='none'):
    """
    pan a mono audio source into stereo
    x is a numpy array, angle is the angle in radiants
    """
    if right == 'none':
        x = left
        left = np.sqrt(2)/2.0 * (np.cos(angle) - np.sin(angle)) * x
        right = np.sqrt(2)/2.0 * (np.cos(angle) + np.sin(angle)) * x
    else:
        left = np.sqrt(2)/2.0 * (np.cos(angle) - np.sin(angle)) * right
        right = np.sqrt(2)/2.0 * (np.cos(angle) + np.sin(angle)) * left
    return left, right

fs, arr = read('Joy.wav')
print(arr.shape)
# normalize to 16-bit range
left_2, right_2 = np.hsplit(arr, 2)
left_2, right_2 = panner(np.radians(200), left_2, right_2)
# left = left * (32767 / np.max(np.abs(left)))
# right = right * (32767 / np.max(np.abs(right)))
# # convert to 16-bit data
# left = left.astype(np.int16)
# right = right.astype(np.int16)

# joy_audio = np.dstack((left,right))

fs, arr = read('Sadness.wav')
print(arr.shape)
# normalize to 16-bit range
left_1, right_1 = np.hsplit(arr, 2)
left_1, right_1 = panner(np.radians(0), left_1, right_1)
# left = left * (32767 / np.max(np.abs(left)))
# right = right * (32767 / np.max(np.abs(right)))
# # convert to 16-bit data
# left = left.astype(np.int16)
# right = right.astype(np.int16)

# sad_audio = np.dstack((left,right))
if len(left_2) > len(left_1):
    pad = len(left_2) - len(left_1)
    left_1 = np.concatenate((left_1, np.zeros((pad, 1))))
else:
    pad = len(left_1) - len(left_2)
    left_2 = np.concatenate((left_2, np.zeros((pad, 1))))

left = left_1 + left_2

if len(right_2) > len(right_1):
    pad = len(right_2) - len(right_1)
    right_1 = np.concatenate((right_1, np.zeros((pad, 1))))
else:
    pad = len(right_1) - len(right_2)
    right_2 = np.concatenate((right_2, np.zeros((pad, 1))))

right = right_1 + right_2

left = left * (32767 / np.max(np.abs(left)))
right = right * (32767 / np.max(np.abs(right)))
# convert to 16-bit data
left = left.astype(np.int16)
right = right.astype(np.int16)

audio = np.dstack((left,right))

# stereo_arr = panner(arr, 0)

play_obj = sa.play_buffer(audio, 2, 2, fs)
# play_object = play_obj.play()
play_obj.wait_done()

