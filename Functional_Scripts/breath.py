import numpy as np
import copy

def breath(dur):
    repeats = int(dur / 4)
    remainder = dur % 4
    move = np.zeros(2 * repeats)
    # move = [0]*(2 * repeats)
    for j in range(2 * repeats):
        move[j] = -1^ j * 2
    move = np.insert(move, 0, 0)
    if dur < 4:
        traj = np.zeros(7)
        traj_t = np.zeros(7) + dur
    else:
        traj = np.array([0, (-move), 0, (-move), 0, 0, 0])
        joint_2_t = np.zeros(2 * repeats)+ 2
        joint_2_t[(2 * repeats) - 1] = 1.5 + remainder
        joint_4_t = copy.deepcopy(joint_2_t)
        joint_4_t[(2 * repeats) - 1] = 2 + remainder
        traj_t = np.array([dur, joint_2_t, dur, joint_4_t, dur, dur, dur])

    return traj, traj_t

def breath_t(dur):
    if dur < 4:
        traj_t = np.zeros(7) + dur
        # traj_t = ([0] * 7) + dur
    else:
        repeats = int(dur / 4)
        remainder = dur % 4
        move = np.zeros(2 * repeats) + 2
        # move = [2]*(2 * repeats)
        move = np.insert(move, 0, 0.5)
        move4 = move
        move4[(2 * repeats) - 1] = 2 + remainder
        move[(2 * repeats) - 1] = 1.5 + remainder
        traj_t = np.array([dur, move, dur, move4, dur, dur, dur])
        # traj_t = np.array([dur, [0.5, move.tolist()], dur, move4.tolist(), dur, dur, dur])
        # traj_t = [dur, [0.5, move], dur, move4, dur, dur, dur]
    
    return traj_t

print(breath(9))