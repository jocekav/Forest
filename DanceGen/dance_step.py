import numpy as np
from numpy.core.fromnumeric import transpose

class Dance_Step:
    def __init__(self, name, bpm=60, init_pos=[0, 0, 0, 90, 0, 0, 0], dance_step_arr=None, dance_step_t_arr=None, csv_path=None):
        self.name = name
        self.init_pos = init_pos
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
        if dance_step_arr:
            self.add_angles_as_array(dance_step_arr, dance_step_t_arr)
            self.bpm = bpm
        elif csv_path:
            self.add_angles_from_csv(csv_path)

    def add_angles_as_array(self, dance_step, dance_step_t):
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
    
    def add_angles_from_csv(self, csv_path):
        return
    
    def set_trajectory(self, end_pos='init', final_time= 2, time_step=0.001, csv=False):
        # joints = np.array([self.joint1[0], self.joint2[0], self.joint3[0], self.joint4[0], self.joint5[0], self.joint6[0], self.joint7[0]])
        # joints_t = np.array([self.joint1_t[0], self.joint2_t[0], self.joint3_t[0], self.joint4_t[0], self.joint5_t[0], self.joint6_t[0], self.joint7_t[0]])

<<<<<<< Updated upstream
        joints = [self.joint1[0], self.joint2[0], self.joint3[0], self.joint4[0], self.joint5[0], self.joint6[0], self.joint7[0]]
        joints_t = [self.joint1_t[0], self.joint2_t[0], self.joint3_t[0], self.joint4_t[0], self.joint5_t[0], self.joint6_t[0], self.joint7_t[0]]
=======
        joints = [self.joint1[0], self.joint2[0], self.joint3[0], self.joint4[0], self.joint5[0], self.joint6[0],
                  self.joint7[0]]
        joints_t = [self.joint1_t[0], self.joint2_t[0], self.joint3_t[0], self.joint4_t[0], self.joint5_t[0],
                    self.joint6_t[0], self.joint7_t[0]]
        
        for i in range(len(joints)):
            if isinstance(joints[i], (list, tuple, np.ndarray)):
                if end_pos == 'init':
                    reset_pos = -1 * sum(joints[i])
                else:
                    reset_pos = end_pos[i] - sum(joints[i])
                joints[i].append(reset_pos)
                joints_t[i].append(final_time)
            else:
                temp = joints[i]
                temp_t = joints_t[i]
                if end_pos == 'init':
                    joints[i] = [temp, -temp]
                else:
                    joints[i] = [temp, end_pos[i]-temp]
                joints_t[i] = [temp_t, final_time]

        # same_flag = True
        # for i in range(len(joints)):
        #     if isinstance(joints[i], (list, tuple, np.ndarray)):
        #         if end_pos == 'init' or end_pos == self.init_pos:
        #             reset_pos = -1 * sum(joints[i])
        #             if reset_pos != self.init_pos[i]:
        #                 same_flag = False
        #                 break
        #         else:
        #             reset_pos = end_pos[i] - sum(joints[i])
        #             if reset_pos != end_pos[i]:
        #                 same_flag = False
        #                 break
        #     else:
        #         temp = joints[i]
        #         temp_t = joints_t[i]
        #         if end_pos == 'init' or end_pos == self.init_pos:
        #             if -temp != self.init_pos[i]:
        #                 same_flag = False
        #                 break
        #         else:
        #             if (end_pos[i] - temp) != end_pos[i]:
        #                 same_flag = False
        #                 break
        # for i in range(len(joints)):
        #     if isinstance(joints[i], (list, tuple, np.ndarray)):
        #         if end_pos == 'init':
        #             reset_pos = -1 * sum(joints[i])
        #         elif end_pos == self.init_pos:
        #             reset_pos = -1 * sum(joints[i])
        #         else:
        #             reset_pos = end_pos[i] - sum(joints[i])
        #         joints[i].append(reset_pos)
        #         joints_t[i].append(final_time)
        #     else:
        #         temp = joints[i]
        #         temp_t = joints_t[i]
        #         if end_pos == 'init':
        #             joints[i] = [temp, -temp]
        #         elif end_pos == self.init_pos:
        #             joints[i] = [temp, -temp]
        #         else:
        #             joints[i] = [temp, end_pos[i] - temp]
        #         joints_t[i] = [temp_t, final_time]
>>>>>>> Stashed changes

        for i in range(len(joints)):
            if isinstance(joints[i], (list, tuple, np.ndarray)):
                if end_pos == 'init':
                    reset_pos = -1 * sum(joints[i])
                elif end_pos == self.init_pos:
                    reset_pos = -1 * sum(joints[i])
                else:
                    reset_pos = end_pos[i] - sum(joints[i])
                joints[i].append(reset_pos)
                joints_t[i].append(final_time)
            else:
                temp = joints[i]
                temp_t = joints_t[i]
                if end_pos == 'init':
                    joints[i] = [temp, -temp]
                elif end_pos == self.init_pos:
                    joints[i] = [temp, -temp]
                else:
                    joints[i] = [temp, end_pos[i]-temp]
                joints_t[i] = [temp_t, final_time]

        
        time_scale = 60 / self.bpm

        for i in range(len(joints)):
            joints_t[i] = np.around((time_scale * np.array(joints_t[i])), 3)

        time_sums = np.empty(len(joints_t))
        for i in range(len(joints_t)):
            if isinstance(joints_t[i], (list, tuple, np.ndarray)):
                time_sums[i] = sum(joints_t[i])
            else: 
                time_sums[i] = joints_t[i]

        time_max = max(time_sums)
        self.length = time_max
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

        trajectory_arr = np.asarray(trajectory)
        trajectory_arr = np.transpose(trajectory_arr)
        self.trajectory = trajectory_arr
        if csv:
<<<<<<< Updated upstream
            np.savetxt(self.name + ".csv", trajectory_arr, delimiter =", ", fmt ='% s')     
        # return trajectory_arr
=======
            np.savetxt(self.name + "_return.csv", trajectory_arr, delimiter=", ", fmt='% s')
            # return trajectory_arr
>>>>>>> Stashed changes

    def get_trajectory(self):
        return self.trajectory
    
    def get_name(self):
        return self.name

def get_consecutive_trajectories(dance_steps, dance_dict):
    trajectories = []
    for i in range(len(dance_steps)-1):
        curr_step = dance_dict[dance_steps[i]]
        next_step = dance_dict[dance_steps[i+1]]
        curr_step.set_trajectory(next_step.init_pos)
        trajectories.append(curr_step.get_trajectory())
    # dance_dict[dance_steps[len(dance_steps)-1]].set_trajectory()
    # trajectories.append(curr_step.get_trajectory())
    return trajectories


