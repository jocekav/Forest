import robot, dance_step, dance_funcs


dance_step_database = dance_funcs.get_database()

robots = robot.init_robots()
robots[0].add_dance_step_dict(["ISO_LEFT", "ISO_LEFT", "ISO_RIGHT"])

robot.set_up_robots(robots)

robots[0].play_dances_from_dict(dance_step_database)

