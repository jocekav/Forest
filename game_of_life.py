
# ROBOT_1_NEIGHBORS = [ROBOT_2, ROBOT_5]
# ROBOT_2_NEIGHBORS = [ROBOT_1, ROBOT_3, ROBOT_5, ROBOT_6, ROBOT_8]
# ROBOT_3_NEIGHBORS = [ROBOT_2, ROBOT_4, ROBOT_6, ROBOT_7, ROBOT_9]
# ROBOT_4_NEIGHBORS = [ROBOT_3, ROBOT_7]
# ROBOT_5_NEIGHBORS = [ROBOT_1, ROBOT_2, ROBOT_6, ROBOT_8]
# ROBOT_6_NEIGHBORS = [ROBOT_2, ROBOT_3, ROBOT_5, ROBOT_7, ROBOT_8, ROBOT_9]
# ROBOT_7_NEIGHBORS = [ROBOT_3, ROBOT_4, ROBOT_6, ROBOT_9]
# ROBOT_8_NEIGHTBORS = [ROBOT_2, ROBOT_5, ROBOT_6, ROBOT_9, ROBOT_10]
# ROBOT_9_NEIGHTBORS = [ROBOT_3, ROBOT_6, ROBOT_7, ROBOT_8, ROBOT_10]
# ROBOT_10_NEIGHBORS = [ROBOT_6, ROBOT_8, ROBOT_9]

from random import randint
import numpy as np
import trajectory_generation as traj
import pandas as pd
import csv

class Robot:
    def __init__(self):
        self.status = 'Dead'
        self.dance = []
        self.dance_t = []
    
    def set_neighbors(self, neighbors):
        self.neighbors = neighbors
    
    def get_neighbors(self):
        return self.neighbors

    def set_die(self):
        self.status = 'Dead'
        # call die movement here
        self.death()

    def set_alive(self):
        self.status = 'Alive'
        #call birth movement here
        self.birth()

    def set_living(self):
        self.status = 'Living'
        #call living movement here
        self.living()
    
    def set_dying(self):
        self.status = 'Dying'
        #call dying movement here
        self.dying()
    
    def is_alive(self):
        if self.status == 'Alive' or self.status == 'Living':
            return True
    
    def get_status(self):
        return self.status

    def birth(self):
        birth_move = np.array([90, 0, 0, 0, 0, 0, 0])
        birth_time = np.array([4, 4, 4, 4, 4, 4, 4])

        self.dance.append(birth_move)
        self.dance_t.append(birth_time)

    def death(self):
        death_move = np.array([-90, 0, 0, 0, 0, 0, 0])
        death_time = np.array([4, 4, 4, 4, 4, 4, 4])

        self.dance.append(death_move)
        self.dance_t.append(death_time)

    def living(self):
        living_move = np.array([0, 0, 0, 0, 0, [-10, 10], 0])
        living_time = np.array([4, 4, 4, 4, 4, [2, 2], 4])

        self.dance.append(living_move)
        self.dance_t.append(living_time)
    
    def dying(self):
        dying_move = np.array([0, 0, 0, 0, [-10, 10], 0, 0])
        dying_time = np.array([4, 4, 4, 4, [2, 2], 4, 4])

        self.dance.append(dying_move)
        self.dance_t.append(dying_time)



class Game:
    NUM_ROBOTS = 10
    INIT_POS = np.zeros(7)

    def _init_(self, robots):
        for robot in robots:
            random = randint(0, 2)
            robot.set_alive()

    def revive(self, robots):
        for robot in robots:
            random = randint(0, 2)
            robot.set_alive()


    def change_state(self, robots):
        birth = []
        kill = []
        living = []
        dying = []
        death_count = 0

        for robot in robots:
            
            neighbors = robot.get_neighbors()
            live_neighbors = 0
            total_neighbors = len(neighbors)
            half_neighbors = int(total_neighbors / 2)
            for neighbor in neighbors:
                if neighbor.is_alive():
                    live_neighbors += 1

            curr_robot_living = robot.is_alive()

            if curr_robot_living:
                if live_neighbors == 0:
                    kill.append(robot)
                elif live_neighbors >= half_neighbors:
                    kill.append(robot)
                else:
                    living.append(robot)
            else:
                if live_neighbors >= half_neighbors:
                    birth.append(robot)
                else:
                    dying.append(robot)
                    death_count += 1
            
        for i in birth:
            i.set_alive()
        for i in kill:
            i.set_die()
        for i in living:
            i.set_living()
        for i in dying:
            i.set_dying()
        
        if death_count == 9:
            self.revive(robots)
    
    def run_game(self, robots, iterations):
        for robot in robots:
            random = randint(0, 2)
            if random == 1:
                robot.set_alive()

        curr_state = ''
        for robot in robots:
            curr_state = curr_state + robot.get_status() + ' '
        print(curr_state)

        for i in range(iterations):
            self.change_state(robots)
            curr_state = ''
            for robot in robots:
                curr_state = curr_state + robot.get_status() + ' '
            print(curr_state)

    def print_dance(self, robots, final_time):
        dances = []
        dances_t = []
        for robot in robots:
            dances.append(robot.dance)
            dances_t.append(robot.dance_t)
        [trajectory,velocity] = traj.generate_trajectory(dances, dances_t, final_time)
        
        for robot in range(self.NUM_ROBOTS):
            robot_loc = 7 * (robot)
            for i in range(7):
                # trajectory[i + robot_loc, :] = trajectory[i + robot_loc, :] + self.INIT_POS
                trajectory[i + robot_loc, :] = trajectory[i + robot_loc, :]
                if i < 3:
                    trajectory[i, :] = -1 * trajectory[i, :]

        final_position_db = np.transpose(trajectory)
        final_position = final_position_db[0::6, :]

        pd.DataFrame(final_position).to_csv("dance_pattern_pos_1.csv")

        final_trajectory = velocity
        final_trajectory = np.transpose(final_trajectory)

        pd.DataFrame(final_trajectory).to_csv("dance_groove_vel_1.csv")


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

    ROBOT_1.set_neighbors([ROBOT_2, ROBOT_5])
    ROBOT_2.set_neighbors([ROBOT_1, ROBOT_3, ROBOT_5, ROBOT_6, ROBOT_8])
    ROBOT_3.set_neighbors([ROBOT_2, ROBOT_4, ROBOT_6, ROBOT_7, ROBOT_9])
    ROBOT_4.set_neighbors([ROBOT_3, ROBOT_7])
    ROBOT_5.set_neighbors([ROBOT_1, ROBOT_2, ROBOT_6, ROBOT_8])
    ROBOT_6.set_neighbors([ROBOT_2, ROBOT_3, ROBOT_5, ROBOT_7, ROBOT_8, ROBOT_9])
    ROBOT_7.set_neighbors([ROBOT_3, ROBOT_4, ROBOT_6, ROBOT_9])
    ROBOT_8.set_neighbors([ROBOT_2, ROBOT_5, ROBOT_6, ROBOT_9, ROBOT_10])
    ROBOT_9.set_neighbors([ROBOT_3, ROBOT_6, ROBOT_7, ROBOT_8, ROBOT_10])
    ROBOT_10.set_neighbors([ROBOT_6, ROBOT_8, ROBOT_9])

    return robots



def main():
    robots = init_robots()
    game = Game()
    game.run_game(robots, 4)
    game.print_dance(robots, 4)

main()
            
                



    

