import numpy as np

# Constants
INIT_POS = np.zeros(7)
MAX_VEl = np.zeros(7) + 180
MAX_ACC = np.zeros(7) + 1000
NUM_ROBOTS = 10
NUM_JOINTS = 7

BPM = 90
TIME = 60/BPM


def generate_trajectory(dances_arr, dances_time_arr, final_time):

    for robot in range(NUM_ROBOTS):
        robot_loc = robot * NUM_JOINTS
        routine = dances_arr[robot_loc]
        routine_time = dances_time_arr[robot_loc]
        
        num_elem = sum(len(x) for x in routine)
        
        for joint in range(NUM_JOINTS):
            phase_arr = np.array([])
            time_arr = np.array([])
            
            for i in range(num_elem):
                phase_arr.append(routine[joint][i])
                time_arr.append(routine_time[joint][i])
        
        reset_pos = -1 * sum(phase_arr)
        phase_arr.append(reset_pos)
        time_arr.append(final_time)
        

