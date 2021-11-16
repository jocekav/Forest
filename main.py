import robot
import dance_step
import dance_funcs
import numpy as np

dance_step_database = dance_funcs.get_database()

robots = robot.init_robots()
# robots[0].add_dance_step_dict(["ISO_LEFT", "ISO_LEFT", "ISO_RIGHT"])
robots[1].add_dance_step_dict(["HEAD_UP"])

robot.set_up_robots(robots, False)
robots[1].play_dances_from_dict(dance_step_database)



# steps = np.arange(0, 2, 0.006)
# sine = np.transpose(np.sin(2 * np.pi * 10 * steps) + 10)
# zeros = np.transpose(np.zeros(len(steps)))
# traj = np.stack((zeros, zeros, zeros, sine, zeros, zeros, zeros), axis=1)
# robots[2].play_dances_from_traj(traj)


