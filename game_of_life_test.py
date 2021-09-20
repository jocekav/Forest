
# ROBOT_1_NEIGHBORS = [ROBOT_2, ROBOT_5]
# ROBOT_2_NEIGHBORS = [ROBOT_1, ROBOT_3, ROBOT_5, ROBOT_6, ROBOT_8]
# ROBOT_3_NEIGHBORS = [ROBOT_2, ROBOT_4, ROBOT_6, ROBOT_7, ROBOT_9]
# ROBOT_4_NEIGHBORS = [ROBOT_3, ROBOT_7]
# ROBOT_5_NEIGHBORS = [ROBOT_1, ROBOT_2, ROBOT_6, ROBOT_8]
# ROBOT_6_NEIGHBORS = [ROBOT_2, ROBOT_3, ROBOT_5, ROBOT_7, ROBOT_8, ROBOT_9]
# ROBOT_7_NEIGHBORS = [ROBOT_3, ROBOT_4, ROBOT_6, ROBOT_9]
# ROBOT_8_NEIGHBORS = [ROBOT_2, ROBOT_5, ROBOT_6, ROBOT_9, ROBOT_10]
# ROBOT_9_NEIGHBORS = [ROBOT_3, ROBOT_6, ROBOT_7, ROBOT_8, ROBOT_10]
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
        self.curr_angle = 90
    
    def set_neighbors(self, neighbors):
        self.neighbors = neighbors
    
    def get_neighbors(self):
        return self.neighbors

    def set_die(self, first=False):
        self.status = 'Dead'
        # call die movement here
        # if first:
        #     self.death()
        # else:
        self.death()

    def set_alive(self, first=False):
        self.status = 'Alive'
        #call birth movement here
        # if first:
        #     self.first_birth()
        # else:
        self.birth()

    def set_living(self):
        self.status = 'Living'
        #call living movement here
        self.living()
    
    def set_dying(self):
        self.status = 'Dying'
        #call dying movement here
        self.dying()

    def set_inactive(self):
        self.status = 'Inactive'
        self.inactive()
    
    def is_alive(self):
        if self.status == 'Alive' or self.status == 'Living':
            return True
        else:
            return False
    
    def is_inactive(self):
        if self.status == 'Inactive':
            return True
        else:
            return False
    
    def get_status(self):
        return self.status

    def birth(self):
        #joint 4 starts at 90
        #full alive position for joint 4 at 120
        if self.curr_angle == 90:
            birth_move = np.array([0, -30, 0, 30, 0, 0, 0], dtype=object)
            birth_time = np.array([4, 4, 4, 4, 4, 4, 4], dtype=object)

            self.dance.append(birth_move)
            self.dance_t.append(birth_time)

            self.curr_angle = self.curr_angle + 30
        else:
            birth_move = np.array([0, -50, 0, 60, 0, 0, 0], dtype=object)
            birth_time = np.array([4, 4, 4, 4, 4, 4, 4], dtype=object)

            self.dance.append(birth_move)
            self.dance_t.append(birth_time)

            self.curr_angle = self.curr_angle + 60

    # def first_birth(self):
    #     birth_move = np.array([0, -20, 0, 30, 0, 0, 0])
    #     birth_time = np.array([4, 4, 4, 4, 4, 4, 4])
    #
    #     self.dance.append(birth_move)
    #     self.dance_t.append(birth_time)

    def death(self):
        # joint 4 starts at 90
        # full death position for joint 4 at 60
        if self.curr_angle == 90:
            death_move = np.array([0, 30, 0, -30, 0, 0, 0], dtype=object)
            death_time = np.array([4, 4, 4, 4, 4, 4, 4], dtype=object)

            self.dance.append(death_move)
            self.dance_t.append(death_time)

            self.curr_angle = self.curr_angle - 30
        elif self.curr_angle == 60:
            self.dying()
        elif self.curr_angle == 120:
            death_move = np.array([0, 50, 0, -60, 0, 0, 0], dtype=object)
            death_time = np.array([4, 4, 4, 4, 4, 4, 4], dtype=object)

            self.dance.append(death_move)
            self.dance_t.append(death_time)

            self.curr_angle = self.curr_angle - 60

    # def first_death(self):
    #     death_move = np.array([0, 20, 0, -30, 0, 0, 0])
    #     death_time = np.array([4, 4, 4, 4, 4, 4, 4])
    #
    #     self.dance.append(death_move)
    #     self.dance_t.append(death_time)

    def living(self):
        living_move = np.array([0, 0, [-15, 15, 15, -15], 0, 0, 0, 0], dtype=object)
        living_time = np.array([4, 4, [1, 1, 1, 1], 4, 4, 4, 4], dtype=object)

        self.dance.append(living_move)
        self.dance_t.append(living_time)
    
    def dying(self):
        dying_move = np.array([[20, -40, 20], 0, 0, 0, 0, 0, 0], dtype=object)
        dying_time = np.array([[1, 2, 1], 4, 4, 4, 4, 4, 4], dtype=object)

        self.dance.append(dying_move)
        self.dance_t.append(dying_time)
    
    def inactive(self):
        inactive_move = np.array([0, 0, 0, 0, 0, 0, 0], dtype=object)
        inactive_time = np.array([4, 4, 4, 4, 4, 4, 4], dtype=object)

        self.dance.append(inactive_move)
        self.dance_t.append(inactive_time)

class Game:
    NUM_ROBOTS = 10
    INIT_POS = np.array([0, 0, 0, 90, 0, 0, 0])

    def _init_(self, robots):
        # for robot in robots:
        #     random = randint(0, 2)
        #     if random == 1:
        #         robot.set_alive(True)
        #     else:
        #         robot.set_die(True)
        return

    def revive(self, robots):
        for robot in robots:
            random = randint(0, 2)
            if random == 1:
                robot.set_alive()
            else:
                robot.set_die()


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
                robot.set_alive(True)
            else:
                robot.set_die(True)

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

    def change_state_contagion(self, robots):
        birth = []
        kill = []
        living = []
        dying = []
        inactive = []
        death_count = 0

        for robot in robots:
            
            neighbors = robot.get_neighbors()
            live_neighbors = 0
            active_neighbors = 0
            total_neighbors = len(neighbors)
            half_neighbors = int(total_neighbors / 2)
            for neighbor in neighbors:
                if neighbor.is_alive():
                    live_neighbors += 1
                if not neighbor.is_inactive():
                    active_neighbors += 1

            curr_robot_living = robot.is_alive()
            curr_robot_inactive = robot.is_inactive()

            if curr_robot_living:
                if live_neighbors == 0:
                    kill.append(robot)
                elif live_neighbors >= half_neighbors:
                    kill.append(robot)
                else:
                    living.append(robot)
            elif curr_robot_inactive:
                if live_neighbors >= half_neighbors or active_neighbors >= 1:
                    birth.append(robot)
                else:
                    inactive.append(robot)
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
        for i in inactive:
            i.set_inactive()
        
        if death_count == 9:
            self.revive(robots)

    def run_game_contagion(self, robots, first_robot, iterations):
        # for i in range(len(robots)):
        #     if i == first_robot:
        #         robots[first_robot].set_alive()
        #     else:
        #         robots[i].set_inactive()
        for robot in robots:
            if robot == robots[first_robot]:
                robot.set_alive()
            else:
                # robot.set_inactive()
                robot.set_die()

        curr_state = ''
        for robot in robots:
            curr_state = curr_state + robot.get_status() + ' '
        print(curr_state)

        for robot in robots:
            if robot == robots[first_robot]:
                robot.set_alive()
            else:
                # robot.set_inactive()
                robot.set_die()

        curr_state = ''
        for robot in robots:
            curr_state = curr_state + robot.get_status() + ' '
        print(curr_state)

        # look at neighbors before waking up?

        # robots[first_robot].get_neighbors()

        for i in range(iterations):
            self.change_state_contagion(robots)
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
            robot_loc = 7 * robot
            for i in range(7):
                trajectory[i + robot_loc, :] = trajectory[i + robot_loc, :] + self.INIT_POS[i]
               # trajectory[i + robot_loc, :] = trajectory[i + robot_loc, :]
                if i < 3:
                    trajectory[i, :] = -1 * trajectory[i, :]

        final_position_db = np.transpose(trajectory)
        final_position = final_position_db[0::6, :]

        df = pd.DataFrame(final_position).astype(float)
        df.to_csv("/home/forest/Desktop/xArm/Trajectories2/000027gameoflife.csv", header=False, index=False)

        # final_trajectory = velocity
        # final_trajectory = np.transpose(final_trajectory)
        #
        # pd.DataFrame(final_trajectory).to_csv("dance_groove_vel_1.csv")


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



# def main():
#     robots = init_robots()
#     game = Game()
#     iterations = 5
#     game.run_game(robots, iterations)
#     game.print_dance(robots, iterations)

def main():
    robots = init_robots()
    game = Game()
    iterations = 5
    # game.run_game(robots, iterations)
    game.run_game_contagion(robots, 0, iterations)
    game.print_dance(robots, 4)

main()
            
                



    

