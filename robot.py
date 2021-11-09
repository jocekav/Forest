from numpy.lib.function_base import iterable
import pandas as pd
import numpy as np
# import breath

class Robot:
    def __init__(self, init_pos=np.array([0, 0, 0, 90, 0, 0, 0])):
        self.dance_dict = {}
        self.joint1 = []
        self.joint2 = []
        self.joint3 = []
        self.joint4 = []
        self.joint5 = []
        self.joint6 = []
        self.joint7 = []

        self.joint1_t = []
        self.joint2_t = []
        self.joint3_t = []
        self.joint4_t = []
        self.joint5_t = []
        self.joint6_t = []
        self.joint7_t = []
        self.dance = []
        self.dance_t = []
        self.curr_angle = 90
        self.init_pos = init_pos
    
    def set_neighbors(self, neighbors):
        self.neighbors = neighbors
    
    def get_neighbors(self):
        return self.neighbors

# Add a dance step to the robot's stored list of joint angles and joint angle times
# Expects size 7 dance step and time steo arrays/lists 
    def add_dance_step(self, dance_step, dance_step_t):
        self.joint1.append(dance_step[0])
        self.joint2.append(dance_step[1])
        self.joint3.append(dance_step[2])
        self.joint4.append(dance_step[3])
        self.joint5.append(dance_step[4])
        self.joint6.append(dance_step[5])
        self.joint7.append(dance_step[6])

        self.joint1_t.append(dance_step_t[0])
        self.joint2_t.append(dance_step_t[1])
        self.joint3_t.append(dance_step_t[2])
        self.joint4_t.append(dance_step_t[3])
        self.joint5_t.append(dance_step_t[4])
        self.joint6_t.append(dance_step_t[5])
        self.joint7_t.append(dance_step_t[6])

# Calculates trajectory of robot's stored dance steps (stored as joint angles and joint angle times)
# Assigns constant bpm for all steps to create trajectory
    def calculate_robot_trajectory(self, bpm, final_time=0, time_step=0.001):
        joints = np.array([self.joint1[0], self.joint2[0], self.joint3[0], self.joint4[0], self.joint5[0], self.joint6[0], self.joint7[0]])
        joints_t = np.array([self.joint1_t[0], self.joint2_t[0], self.joint3_t[0], self.joint4_t[0], self.joint5_t[0], self.joint6_t[0], self.joint7_t[0]])

        # joints = [robot.joint1, robot.joint2, robot.joint3, robot.joint4, robot.joint5, robot.joint6, robot.joint7]
        # joints_t = [robot.joint1_t, robot.joint2_t, robot.joint3_t, robot.joint4_t, robot.joint5_t, robot.joint6_t, robot.joint7_t]

        time_scale = 60/bpm

        for i in range(len(joints)):
            if final_time != 0:
                reset_pos = -1 * sum(joints[i])
                joints[i].append(reset_pos)
                joints_t[i].append(final_time)

            joints_t[i] = np.around((time_scale * np.array(joints_t[i])), 3)


        time_sums = np.empty(len(joints_t))
        for i in range(len(joints_t)):
            if isinstance(joints_t[i], (list, tuple, np.ndarray)):
                time_sums[i] = sum(joints_t[i])
            else: 
                time_sums[i] = joints_t[i]


        time_max = max(time_sums)
        time_points = int(time_max / time_step) + 1
        #time_step_arr = np.arange(0, time_max, time_step)

        trajectory = np.zeros((7, time_points))
        velocity = np.zeros((7, time_points))

        for joint in range(len(joints)):
            if isinstance(joints[joint], (list, tuple, np.ndarray)):
                phases = len(joints[joint])
            else:
                phases = 1
            ind = 0
            
            curr_pos = 0
            
            vel_0 = 0
            q_i = 0

            while ind < phases:
                if isinstance(joints[joint], (list, tuple, np.ndarray)):
                    curr_phase = joints[joint][ind]
                    curr_phase_t = joints_t[joint][ind]
                else:
                    curr_phase = joints[joint]
                    curr_phase_t = joints_t[joint]
                q_f = q_i + curr_phase
                t_total = curr_phase_t
                t = np.arange(0, t_total, time_step)
                q_dot_i = 0
                q_dot_f = 0
                q_dotdot_i = 0
                q_dotdot_f = 0

                a0 = q_i
                a1 = q_dot_i
                a2 = 0.5 * q_dotdot_i
                a3 = 1.0 / (2.0 * t_total** 3.0) * (20.0 * (q_f - q_i) - (8.0 * q_dot_f + 12.0 * q_dot_i) * t_total - (3.0 * q_dotdot_f - q_dotdot_i) * t_total** 2.0)
                a4 = 1.0 / (2.0 * t_total** 4.0) * (30.0 * (q_i - q_f) + (14.0 * q_dot_f + 16.0 * q_dot_i) * t_total + (3.0 * q_dotdot_f - 2.0 * q_dotdot_i) * t_total** 2.0)
                a5 = 1.0 / (2.0 * t_total** 5.0) * (12.0 * (q_f - q_i) - (6.0 * q_dot_f + 6.0 * q_dot_i) * t_total - (q_dotdot_f - q_dotdot_i) * t_total** 2.0)

                traj_grid = a0 + a1 * t + a2 * t** 2 + a3 * t** 3 + a4 * t** 4 + a5 * t** 5
                velocity_grid = a1 + 2 * a2 * t + 3 * a3 * t** 2 + 4 * a4 * t** 3 + 5 * a5 * t** 4

                P = curr_phase
                t_a = curr_phase_t / 2
                a = (P - vel_0 * t_a) / (t_a** 2)
                vf = t_a * a

                # if abs(a) > MAX_ACC[joint] or abs(vf) > MAX_VEL[joint]
                #     rip = ['too fast at phase ', num2str(i), ' joint ', num2str(j),' velocity ',num2str(vf),' acceleration ',num2str(a)]

                new_pos = curr_pos + len(traj_grid)
                check = trajectory[joint, curr_pos:new_pos]
                trajectory[joint, curr_pos:new_pos] = traj_grid
                velocity[joint, curr_pos:new_pos] = velocity_grid

                curr_pos = new_pos
                q_i = q_i + curr_phase
                ind += 1
        
        for i in range(7):
            trajectory[i, :] = trajectory[i, :] + self.init_pos[i]
               # trajectory[i + robot_loc, :] = trajectory[i + robot_loc, :]
            if i < 3:
                trajectory[i, :] = -1 * trajectory[i, :]
        
        return trajectory

# Generate and combine trajectories for an array of robot objects 
# (uses a constant bpm across all steps and robots)
def combine_trajectories(robots, bpm, final_time=0, time_step=0.001):
    total_traj_df = pd.DataFrame().astype(float)
    for robot in robots:
        trajectory = robot.calculate_robot_trajectory(bpm, final_time=0, time_step=0.001)
        final_position_db = np.transpose(trajectory)
        final_position = final_position_db[0::6, :]
        df = pd.DataFrame(final_position).astype(float)
        total_traj_df = pd.concat([total_traj_df, df], axis=1)
    return total_traj_df

def init_robots():
    
    ROBOT_1 = Robot()
    ROBOT_2 = Robot()
    ROBOT_3 = Robot()
    ROBOT_4 = Robot()
    ROBOT_5 = Robot()
    ROBOT_6 = Robot()
    ROBOT_7 = Robot()
    ROBOT_8 = Robot()
    ROBOT_9 = Robot()
    ROBOT_10 = Robot()

    robots = [ROBOT_1, ROBOT_2, ROBOT_3, ROBOT_4, ROBOT_5, ROBOT_6, ROBOT_7, ROBOT_8, ROBOT_9, ROBOT_10]

    return robots


nod = np.array([0,[-2, 2], 0, [10, -10], 0, [70, -70], 0])
nod_t = np.array([4, [2, 2], 4, [2, 2], 4, [2, 2], 4])

# breaths = breath.breath(4)
# breaths_t = breath.breath_t(4)

robots = init_robots()
for robot in robots:
    # robot.add_dance_step(breaths, breaths_t)
    robot.add_dance_step(nod, nod_t)
traj = robots[0].calculate_robot_trajectory(60)
# traj = combine_trajectories(robots, 60)
print(traj)

